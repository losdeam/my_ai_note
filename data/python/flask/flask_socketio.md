<font size="5">[返回python笔记](../../../python.md/#31-flask)</font>
____
# flask_socketio 
## 1.安装
```
pip install flask_socketio
```

## 2.基础

### 2.1 flask端

`socketio = SocketIO(app)`
- 通过flask对象app创建一个新的SocketIO对象socketio
  
`@socketio.on('par') `
- 当接受到前端返回的par信息执行被修饰的函数

    - connect : 当socketio成功连接时自动启用而不需要额外发送请求
    - disconnect : 当socketio断开连接时自动启用而不需要额外发送请求

`socketio.emit('play',data) `
-  发送名为play的信息，具体的数据为data

### 2.2 js端

`<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.1.0/socket.io.js" ></script>`
- 导入socket.io包，需要与flask_socketio版本对应

`const socket = io();  `
- 建立连接

`socket.on(msg, function(data) { });`
- 接受名为msg的信息，具体数据为data，接收到的格式为json

`socketio.emit('play',data);`
-  发送名为play的信息，具体的数据为data