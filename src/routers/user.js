import express from "express";
import * as authController from '../controllers/user.js';
import { body } from 'express-validator';
import { validate } from "../middlewares/validator.js";
import { isAuth } from '../middlewares/user.js';

const router = express.Router()

const validateLogin = [
    body('userid').trim().notEmpty().withMessage('username을 입력하세요'),
    body('password').trim().isLength({min: 4}).withMessage('password는 최소 4자 이상 입력하세요'), validate
];

const validateSignup = [
    ... validateLogin,
    body('name').trim().notEmpty().withMessage('name을 입력하세요'),
    body('email').isEmail().withMessage('이메일 형식 확인하세요'), validate
];


router.use((req,res,next)=>{
    console.log('users에 존재하는 미들웨어')
    next()
})

router.get('/',(req,res)=>{
    res.status(200).send('회원정보 확인')
})


router.delete('/:userid', isAuth, authController.del_user);

router.post('/signup', validateSignup, authController.signup);

router.post('/login', validateLogin, authController.login);

router.get('/:userid', authController.me);


export default router