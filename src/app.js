import express from 'express'
import morgan from 'morgan'
import fs from 'fs'
import { connectDB } from "./models/database.js";
import userRouter from './routers/user.js' //회원정보
import todolistRouter from './routers/todolist.js' // todolist 
import {config}  from './config/config.js';


const app = express()

const html = fs.readFileSync('index.html')
app.use(express.json())
app.use(morgan('combined'))

app.use('/user', userRouter)
app.use('/list', todolistRouter)


app.get('/',(req,res)=>{
  res.writeHead(200)
  res.write(html)
  res.end()
})

app.get('/index.html',(req,res)=>{
  res.writeHead(200)
  res.write(html)
  res.end()
})


connectDB().then((db) => {
  console.log('몽구스를 사용하여 연결성공')
  app.listen(config.host.port, () => {
    console.log(`서버가 포트 ${config.host.port}에서 실행 중입니다.`);
});
}).catch(console.error);



// "type": "module",
// npm install express-validator
// npm install bcrypt
// npm install jsonwebtoken

