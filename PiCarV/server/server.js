import { Server } from "socket.io";

const io = new Server();

io.on("connection", (socket) => {
  console.log("Client Connected");
  console.log(socket.data);

  // client-side
  let count = 0;
  setInterval(() => {
    socket.volatile.emit("steering", ++count);
    if (count > 180) {
      count = 0;
    }
  }, 50);

  let speed = -100;
  setInterval(() => {
    socket.volatile.emit("drive", ++speed);
    if (speed > 100) {
      speed = -100;
    }
  }, 50);
});

io.listen(3000);
