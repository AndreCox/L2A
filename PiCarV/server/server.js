import { Server } from "socket.io";

const io = new Server();

io.on("connection", (socket) => {
  console.log("Client Connected");

  const sndPower = (power) => {
    socket.volatile.emit("power", power);
  };

  const sndSteer = (steer) => {
    socket.volatile.emit("steering", steer);
  };

  socket.on("drive", (data) => sndPower(data)); //It's about drive it's about power
  socket.on("steer", (data) => sndSteer(data));
});

io.listen(3000);
