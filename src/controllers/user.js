import * as authRepository from '../models/user.js';
import bcrypt from "bcrypt";
import jwt from 'jsonwebtoken';
import { config } from "../config/config.js";

function createJwtToken(id){
    return jwt.sign({id}, config.jwt.secretKey, {expiresIn: config.jwt.expiresInSec});
}

//회원가입
export async function signup(req, res, next) {
    let {name, userid, password, hp, email, ssn1, ssn2, gender} = req.body;
    const found = await authRepository.findByUserId(userid);
    if(found){
        return res.status(409).json({message:`${userid}이 이미 있습니다.`});
    }
    password = await bcrypt.hash(password, config.bcrypt.saltRounds);
    const userId = await authRepository.createUser({name, userid, password, hp, email, ssn1, ssn2, gender});
    console.log('회원가입완료')
    res.status(200).json(userId)
}

//로그인
export async function login(req, res, next) {
    const {userid, password} = req.body;
    const user = await authRepository.findByUserId(userid);
    if(!user){
        return res.status(401).json({message: `아이디를 찾을 수 없음`});
    }
    const isValidpassword = await bcrypt.compareSync(password, user.password);
    if(!isValidpassword){
        return res.status(401).json({message: `비밀번호가 틀렸음`});
    }
    const token = createJwtToken(user.id);
    res.status(200).json({token, userid});
}

//회원정보 수정
export async function mod_user(req,res,next){
    let {name, userid, password, hp, email, ssn1, ssn2, gender} = req.body;
    const user = await authRepository.findByOne({userid : userid});
    if(!user){
        return res.status(401).json({message: `해당 유저가 존재하지않음`});
    }
    return user.update({password : password, hp:hp, email:email })
}

//회원탈퇴
export async function del_user(req,res,next){
    const {userid} = req.params
    // const user = await authRepository.findAll();
    await authRepository.delete_(userid);
    console.log('회원가입 탈퇴 완료')
    res.status(204).json({ msg: "successfully deleted" });
}

//내정보 찾기
export async function me(req,res,next){
    const {userid} = req.params
    const myinfo = await authRepository.findByUserId(userid);
    console.log('내 정보 조회 완료')
    res.status(200).json(myinfo);
}