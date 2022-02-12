import { action, makeAutoObservable, observable } from 'mobx';

//define store class which will be used to store data, add extra states here

class Store {
  //define your data here
  ip: string = '0.0.0.0';
  angle: number = 90;
  power: number = 0;
  connected = false;

  constructor() {
    makeAutoObservable(this);
  }
  //you can add functions to manipulate data here
}

export const store = new Store();
