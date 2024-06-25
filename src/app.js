import express from 'express'
import morgan from 'morgan'
import cors from 'cors'
import { connectDB } from "./models/database.js";
import routers from './routers/index.js';
import {config}  from './config/config.js';


const app = express()

app.use(cors())

app.use(express.json())
app.use(morgan('dev'))


app.use('/', routers);


connectDB()
    .then((db) => {
        app.listen(config.host.port, () => {
            console.log(`서버:${config.host.port} 연결성공`);
        });
}).catch(console.error);


