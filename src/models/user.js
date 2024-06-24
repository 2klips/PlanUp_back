import mongoose from 'mongoose';
import { useVirtualId } from './database.js';

// userid,
// password,
// email,
// name,
// hp,
// zoneCode,
// address,
// addrDetail,
// rrn1,
// rrn2,
const userSchema = new mongoose.Schema({
    name : {type:String,require:true},
    userid : {type:String,require:true},
    password : {type:String,require:true},
    hp : {type:String,require:true},
    email : {type:String,require:true},
    zoneCode : {type:String,require:true},
    address : {type:String,require:true},
    addrDetail : {type:String,require:true},
    ssn1 : {type:String,require:true, maxlength: 6},
    ssn2 : {type:String,require:true, maxlength: 7},
    gender : {type:String,require:true}
})

useVirtualId(userSchema)

const User = mongoose.model('member',userSchema)


export async function findAll(){
    return User.find({});
}

// 아이디(userid) 중복검사  // 아이디 찾기 
export async function findByUserId(userid){
    return User.findOne({userid:userid});
}

// id 중복검사
export async function findById(id){
    return User.findById(id);
}

// 회원가입
export async function createUser(user){
    return new User(user).save().then((data)=>{data.id});
}

//로그인
export async function login(username){
    const user = User.find((user) => user.username === username)
    return user;
}

//회원탈퇴
export async function delete_(userid){
    return User.deleteOne({userid:userid})
}
