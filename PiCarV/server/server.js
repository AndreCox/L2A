import { Server } from "socket.io";
import http from "http";

const httpServer = http.createServer();
const io = new Server(httpServer, { cors: { origins: ["*"] } });

io.on("connection", (socket) => {
  console.log("Client Connected");

  socket.on("drive", (data) => {
    io.sockets.emit("drive", data);
  }); //It's about drive it's about power
  socket.on("steer", (data) => {
    io.sockets.emit("steering", data);
  });
  socket.on("pan", (data) => {
    io.sockets.emit("pan", data);
  });
  socket.on("tilt", (data) => {
    io.sockets.emit("pan", data);
  });
});

io.listen(3000);
