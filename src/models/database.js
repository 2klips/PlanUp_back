import { config } from "../config/config.js";
import mongoose from 'mongoose'



export async function connectDB(){
   try {
      await mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true, dbName: dbName});
      console.log('데이터베이스 연결 성공');
   } catch (error) {
      console.error('데이터베이스 연결 실패', error);
   }
};

export function useVirtualId(schema){
   schema.virtual('id').get(function(){return this._id.toString()})
   schema.set('toJSN',{virtuals:true})
   schema.set('toObj',{virtuals:true})
}
