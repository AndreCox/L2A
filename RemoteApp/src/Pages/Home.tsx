import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';
import isIP from 'validator/lib/isIP';
import { Link } from 'react-router-dom';
import { observer } from 'mobx-react-lite';
import { store } from '../Store';
import { settingsStore } from '../StoreSettings';
import { useCookies } from 'react-cookie';
import { configure, autorun } from 'mobx';
import Gamepads from 'gamepads';
import { MdSettings } from 'react-icons/md';

Gamepads.start();

Gamepads.addEventListener('connect', (e: any) => {
  console.log('Gamepad connected');
  e.gamepad.addEventListener(
    'joystickmove',
    (e: any) => {
      store.angle =
        Number(settingsStore.steeringCenter) +
        Number(e.gamepad.gamepad.axes[0]) * Number(settingsStore.steeringLimit);
      steeringDown = true;
      if (store.connected) {
        socket.emit('steer', store.angle);
      }
    },
    [0],
  );
  e.gamepad.addEventListener(
    'joystickmove',
    (e: any) => {
      console.log(e.gamepad.gamepad.axes[3]);
      if (store.connected) {
        socket.emit('pan', e.gamepad.gamepad.axes[2] * -90 + 90);
        socket.emit('tilt', -e.gamepad.gamepad.axes[3] * 90 + 90);
      }
    },
    [2, 3],
  );
  e.gamepad.addEventListener('buttonvaluechange', (e: any) => {
    powerDown = true;
    store.power =
      e.gamepad.gamepad.buttons[7].value * settingsStore.powerLimit -
      e.gamepad.gamepad.buttons[6].value * settingsStore.powerLimit;
    if (store.connected) {
      socket.emit('drive', store.power);
    }
  });
});

Gamepads.addEventListener('disconnect', (e: any) => {
  console.log('Gamepad disconnected');
});

configure({
  enforceActions: 'never',
});

var socket: any;

const TryConnect = (setCookie: any) => {
  socket = io(`http://${store.ip}:3000`);
  socket.on('connect', function () {
    console.log('connected');
    store.connected = true;
    setCookie('ip', store.ip, { path: '/' });
  });
  socket.on('disconnect', function () {
    store.connected = false;
  });
};

var componentDisplay = 'block';

autorun(() => {
  if (!store.connected) {
    store.ip = '0.0.0.0';
    componentDisplay = 'block';
  } else {
    componentDisplay = 'none';
  }
});

var powerDown = false;
var steeringDown = false;
const ElasticControls = setInterval(() => {
  //if power is not 0 pull it back to 0
  if (powerDown === false) {
    if (store.power > 0) {
      store.power--;
    } else if (store.power < 0) {
      store.power++;
    }
    if (store.connected) {
      socket.emit('drive', store.power);
    }
  }
  if (steeringDown === false) {
    if (store.angle > settingsStore.steeringCenter) {
      store.angle--;
    } else if (store.angle < settingsStore.steeringCenter) {
      store.angle++;
    }
    if (store.connected) {
      socket.emit('steer', store.angle);
    }
  }
}, 20);

const TurnSpeed: number = 10;
const PowerSpeed: number = 10;

const handleKeyDown = (e: any) => {
  if (e.keyCode === 87 && store.power + PowerSpeed <= 100) {
    powerDown = true;
    store.power = store.power + PowerSpeed;
    if (store.connected) {
      socket.emit('drive', store.power);
    }
  } else if (e.keyCode === 83 && store.power - PowerSpeed >= -100) {
    powerDown = true;
    store.power = store.power - PowerSpeed;
    if (store.connected) {
      socket.emit('drive', store.power);
    }
  } else if (e.keyCode === 65 && store.angle - TurnSpeed >= 0) {
    steeringDown = true;
    store.angle = store.angle - TurnSpeed;
    if (store.connected) {
      socket.emit('steer', store.angle);
    }
  } else if (e.keyCode === 68 && store.angle + TurnSpeed <= 180) {
    steeringDown = true;
    store.angle = store.angle + TurnSpeed;
    if (store.connected) {
      socket.emit('steer', store.angle);
    }
  }
};

const handleKeyUp = (e: any) => {
  if (e.keyCode === 87 || e.keyCode === 83) {
    powerDown = false;
  } else if (e.keyCode === 65 || e.keyCode === 68) {
    steeringDown = false;
  }
};

const VideoStream = observer(() => {
  if (store.connected) {
    return (
      <img
        className="bg-cover rounded-lg absolute -z-50 max-h-screen max-w-screen"
        src={'http://' + store.ip + ':8080/?action=stream'}
      />
    );
  } else {
    return (
      <div className="w-full h-screen flex justify-center items-center">
        <h1 className="text-white absolute animate-pulse">Connect to a car</h1>
        <div className=" border-2 animate-ping border-white w-32 h-32 absolute rounded-full " />
        <div className=" border-2 animate-ping border-white w-36 h-36 absolute rounded-full " />
      </div>
    );
  }
});

const Home = observer(() => {
  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown, false);
    document.addEventListener('keyup', handleKeyUp, false);
  }, []);

  const [cookies, setCookie] = useCookies(['ip']);

  // Return the App component.
  return (
    <div className="">
      <Link to="/settings">
        <div className="absolute right-2 top-2 text-white text-4xl hover:rotate-45 transition-all">
          <MdSettings />
        </div>
      </Link>

      {/* IP connection code  top left*/}
      <form className="left-2 top-2 p-2 flex flex-col text-white  absolute rounded-lg  text-sm shadow-black  max-w-sm border  shadow-md  bg-gray-800 border-gray-700">
        <div className="flex flex-row justify-between">
          <label>IP</label>
          <label>Connected: {String(store.connected)}</label>
        </div>
        <input
          className="my-1 outline-none border bg-gray-700 border-gray-600 ring-2 focus:ring-blue-500 focus:border-blue-500 rounded-lg p-1"
          placeholder="IP"
          type="text"
          disabled={store.connected}
          value={store.ip}
          onClick={() => {
            console.log('clicked');
          }}
          onChange={(e) => {
            store.ip = e.target.value;
            if (isIP(store.ip)) {
              console.log('valid ip');
              TryConnect(setCookie);
            }
          }}
        />
        <label style={{ display: componentDisplay }}>Previous Connection</label>
        <div
          onClick={() => {
            console.log('clicked');
            if (cookies['ip'] !== undefined) {
              store.ip = cookies['ip'];
              TryConnect(setCookie);
            }
          }}
        >
          <input
            style={{ display: componentDisplay }}
            className="my-1 outline-none border bg-gray-700 border-gray-600 rounded-lg p-1"
            type="text"
            value={cookies['ip']}
            disabled
          />
        </div>
      </form>
      {/* ////////////////////////////////////////////////////////////////////////////////////////////////////////////// */}

      {/* Steering Display Code Bottom Right */}
      <div className="text-center p-4 absolute bottom-2 right-2 text-white rounded-lg  text-sm shadow-black  max-w-sm border  shadow-md  bg-gray-800 border-gray-700">
        <p>Steering</p>
        <input
          className="shadow-black drop-shadow-lg my-2"
          type="range"
          min={
            Number(settingsStore.steeringCenter) -
            Number(settingsStore.steeringLimit)
          }
          max={
            Number(settingsStore.steeringCenter) +
            Number(settingsStore.steeringLimit)
          }
          value={store.angle}
          onMouseDown={() => {
            steeringDown = true;
          }}
          onMouseUp={() => {
            steeringDown = false;
          }}
          onTouchStart={() => {
            steeringDown = true;
          }}
          onTouchEnd={() => {
            steeringDown = false;
          }}
          onChange={(e) => {
            store.angle = Number(e.target.value);
            if (store.connected) {
              socket.emit('steer', store.angle);
            }
          }}
        />
        <p>{Number(store.angle).toFixed(0)}°</p>
      </div>
      {/* ////////////////////////////////////////////////////////////////////////////////////////////////////////////// */}

      {/* Power Display Code Bottom Left */}
      <div className="text-center rounded-md absolute bottom-2 left-2 text-white p-4  text-sm shadow-black  max-w-sm border  shadow-md  bg-gray-800 border-gray-700">
        <p>Power</p>
        <div className="flex flex-row space-x-2">
          <input
            type="checkbox"
            onChange={(e) => {
              if (store.connected) {
                if (e.target.checked) {
                  powerDown = true;
                  socket.emit('drive', 35);
                } else {
                  socket.emit('drive', 0);
                }
              }
            }}
          />
          <label className="text-white">Constant Speed</label>
        </div>
        <div className="flex flex-row space-x-2">
          <input
            type="checkbox"
            onChange={(e) => {
              if (store.connected) {
                if (e.target.checked) {
                  socket.emit('tilt', 45);
                } else {
                  socket.emit('tilt', 90);
                }
              }
            }}
          />
          <label className="text-white">Tilt Down</label>
        </div>
        <input
          className="shadow-black drop-shadow-lg my-2"
          type="range"
          min={-settingsStore.powerLimit}
          max={settingsStore.powerLimit}
          value={store.power}
          onMouseDown={() => {
            powerDown = true;
          }}
          onMouseUp={() => {
            powerDown = false;
          }}
          onTouchStart={() => {
            powerDown = true;
          }}
          onTouchEnd={() => {
            powerDown = false;
          }}
          onChange={(e) => {
            store.power = Number(e.target.value);
            if (store.connected) {
              socket.emit('drive', store.power);
            }
          }}
        />
        <p>{store.power.toFixed(0)} %</p>
      </div>
      {/* ////////////////////////////////////////////////////////////////////////////////////////////////////////////// */}

      {/* Video Stream Code */}
      <div className="flex w-full h-full justify-center align-middle">
        <VideoStream />
      </div>
      {/* ////////////////////////////////////////////////////////////////////////////////////////////////////////////// */}
    </div>
  );
});

export default Home;
