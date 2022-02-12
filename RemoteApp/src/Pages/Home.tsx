import React, { useState, useEffect } from 'react';
import { Manager, io } from 'socket.io-client';
import isIP from 'validator/lib/isIP';
import { Link } from 'react-router-dom';
import { observer } from 'mobx-react-lite';
import { store } from '../Store';

var socket: any;

const TryConnect = () => {
  socket = io(`http://${store.ip}:3000`);
  socket.on('connect', function () {
    console.log('connected');
    socket.emit('steer', 0);
  });
};

//interval
const interval = setInterval(() => {
  if (store.ip !== '') {
    TryConnect();
    clearInterval(interval);
  }
}, 1000);

const Home = observer(() => {
  // Return the App component.
  return (
    <div className="">
      <input
        className="absolute rounded-lg left-2 top-2 p-1 text-sm shadow-lg border-black border-2 shadow-black"
        placeholder="ip"
        type="text"
        value={store.ip}
        onChange={(e) => {
          store.ip = e.target.value;
          if (isIP(store.ip)) {
            console.log('valid ip');
            TryConnect();
          }
        }}
      />
      <div className="absolute flex flex-row bottom-8 justify-evenly w-full">
        <div className="text-center bg-white rounded-md p-4 shadow-black shadow-lg">
          <p>Steering</p>
          <input
            type="range"
            min="0"
            max="180"
            value={store.angle}
            onChange={(e) => {
              store.angle = Number(e.target.value);
              socket.emit('steer', store.angle);
            }}
          />
          <p>{store.angle}</p>
        </div>

        <div className="bg-white rounded-md p-4 shadow-black shadow-lg text-center">
          <p>Status</p>
          <p>Connected: {String(store.connected)}</p>
        </div>

        <div className="text-center bg-white rounded-md p-4 shadow-black shadow-lg">
          <p>Power</p>
          <input
            type="range"
            min="-100"
            max="100"
            value={store.power}
            onChange={(e) => {
              store.power = Number(e.target.value);
              socket.emit('drive', store.power);
            }}
          />
          <p>{store.power}</p>
        </div>
      </div>

      <img
        className="w-full"
        src={'http://' + store.ip + ':8080/?action=stream'}
      />
    </div>
  );
});

export default Home;
