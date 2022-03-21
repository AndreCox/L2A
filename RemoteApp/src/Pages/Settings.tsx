import React from 'react';
import { observer } from 'mobx-react-lite';
import { autorun } from 'mobx';
import { MdArrowBack } from 'react-icons/md';
import { GiSteeringWheel, GiElectric } from 'react-icons/gi';
import { Link } from 'react-router-dom';
import { settingsStore } from '../StoreSettings';
import { useCookies } from 'react-cookie';

//autorun(() => {

const Settings = observer(() => {
  const [cookies, setCookie] = useCookies(['powerLimit']);
  const [cookies2, setCookie2] = useCookies(['steerLimit']);
  const [cookies3, setCookie3] = useCookies(['snapback']);
  const [cookies4, setCookie4] = useCookies(['steeringCenter']);

  autorun(() => {
    if (settingsStore.powerLimit !== cookies.powerLimit) {
      setCookie('powerLimit', settingsStore.powerLimit, { path: '/' });
    }
    if (settingsStore.steeringLimit !== cookies2.steerLimit) {
      setCookie2('steerLimit', settingsStore.steeringLimit, { path: '/' });
    }
    if (settingsStore.snapback !== cookies3.snapback) {
      setCookie3('snapback', settingsStore.snapback, { path: '/' });
    }
    if (settingsStore.steeringCenter !== cookies4.steeringCenter) {
      setCookie4('steeringCenter', settingsStore.steeringCenter, { path: '/' });
    }
  });

  return (
    <div className="m-4">
      <h1 className="text-white mb-4 ml-4 text-lg font-semibold">Settings</h1>
      <div className="w-full text-gray-900 bg-white rounded-lg border border-gray-200 dark:bg-gray-700 dark:border-gray-600 dark:text-white">
        <Link to="/">
          <button
            type="button"
            className="inline-flex relative items-center py-2 px-4 w-full text-sm font-medium rounded-t-lg border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
          >
            <MdArrowBack className="mr-2 text-lg" />
            Back
          </button>
        </Link>

        {/* 
        <button
          type="button"
          className="inline-flex relative items-center py-2 px-4 w-full text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
        >
          <GiSteeringWheel className="mr-2 text-lg" />
          Steering Snapback Speed
          <input
            type="range"
            min={0}
            max={1}
            step={0.1}
            value={settingsStore.snapback}
            onChange={(e) => {
              settingsStore.snapback = Number(e.target.value);
            }}
            className="ml-auto"
          />
          <label className="ml-2">{settingsStore.snapback}</label>
        </button>
          */}
        <button
          type="button"
          className="inline-flex relative items-center py-2 px-4 w-full text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
        >
          <GiSteeringWheel className="mr-2 text-lg" />
          Steering Limits
          <input
            className="ml-auto"
            min={0}
            max={90}
            value={settingsStore.steeringLimit}
            onChange={(e) =>
              (settingsStore.steeringLimit = Number(e.target.value))
            }
            type="range"
          />
          <label className="ml-2">{settingsStore.steeringLimit}°</label>
        </button>
        <button
          type="button"
          className="inline-flex relative items-center py-2 px-4 w-full text-sm font-medium border-b border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
        >
          <GiSteeringWheel className="mr-2 text-lg" />
          Steering Center
          <input
            type="range"
            min={0}
            max={180}
            value={settingsStore.steeringCenter}
            onChange={(e) => {
              settingsStore.steeringCenter = Number(e.target.value);
            }}
            className="ml-auto"
          />
          <label className="ml-2">{settingsStore.steeringCenter}</label>
        </button>
        <button
          type="button"
          className="inline-flex relative items-center py-2 px-4 w-full text-sm font-medium rounded-b-lg hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-2 focus:ring-blue-700 focus:text-blue-700 dark:border-gray-600 dark:hover:bg-gray-600 dark:hover:text-white dark:focus:ring-gray-500 dark:focus:text-white"
        >
          <GiElectric className="mr-2 text-lg" />
          Power Limit
          <input
            min={0}
            max={100}
            value={settingsStore.powerLimit}
            type="range"
            className="ml-auto"
            onChange={(e) => {
              settingsStore.powerLimit = Number(e.target.value);
            }}
          />
          <label className="ml-2">{settingsStore.powerLimit} %</label>
        </button>
      </div>
    </div>
  );
});

export default Settings;
