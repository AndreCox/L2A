import { action, makeAutoObservable, observable } from 'mobx';

//define store class which will be used to store data, add extra states here

class Store {
  //driving data
  angle: number = 90;
  power: number = 0;
  //camera settings
  tilt: number = 90;
  pan: number = 90;
  // connection state
  connected = false;
  ip: string = '0.0.0.0';

  constructor() {
    makeAutoObservable(this);
  }
  //you can add functions to manipulate data here
}

export const store = new Store();
