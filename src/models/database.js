import { config } from "../config/config.js";
import mongoose from 'mongoose'


export async function connectDB(){
   console.log(mongoose.connect(config.db.host))
   console.log(config.db.database)
   return mongoose.connect(`${config.db.host}`, { useNewUrlParser: true, useUnifiedTopology: true ,dbName: config.db.database})
}

// export async function connectDB(){
//    return mongoose.connect(config.db.host)
// }

export function useVirtualId(schema){
   schema.virtual('id').get(function(){return this._id.toString()})
   schema.set('toJSN',{virtuals:true})
   schema.set('toObj',{virtuals:true})
   // json과 object로 사용할 수 있게 적용
}

// let db;

// export function getUsers(){
//     return db.collection('members');
// }

// export function getTweets(){
//     return db.collection('tweets');
// }
