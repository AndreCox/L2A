import { action, makeAutoObservable, observable } from 'mobx';
import { instanceOf } from 'prop-types';
import Cookies from 'universal-cookie';

//define store class which will be used to store data, add extra states here

class SettingsStore {
  //define your data here
  snapback: number = 1;
  steeringLimit: number = 90;
  steeringCenter: number = 90;
  powerLimit: number = 100;

  constructor() {
    const cookies = new Cookies();
    this.snapback = cookies.get('snapback') || 1;
    this.steeringLimit = cookies.get('steerLimit') || 90;
    this.powerLimit = cookies.get('powerLimit') || 100;
    this.steeringCenter = cookies.get('steeringCenter') || 90;
    makeAutoObservable(this);
  }
  //you can add functions to manipulate data here
}

export const settingsStore = new SettingsStore();
