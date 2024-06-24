import { config } from "../config/config.js";
import mongoose from 'mongoose'


export async function connectDB(){
   console.log(mongoose.connect(config.db.host))
   console.log(config.db.database)
   return mongoose.connect(`${config.db.host}`, { useNewUrlParser: true, useUnifiedTopology: true ,dbName: config.db.database})
}


export function useVirtualId(schema){
   schema.virtual('id').get(function(){return this._id.toString()})
   schema.set('toJSN',{virtuals:true})
   schema.set('toObj',{virtuals:true})
}
