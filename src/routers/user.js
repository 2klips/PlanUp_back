import express from "express";
import * as authController from '../controllers/user.js';
import { body } from 'express-validator';
import { validate } from "../middlewares/validator.js";
import { isAuth } from '../middlewares/user.js';

const router = express.Router()


router.delete('/:userid', isAuth, authController.del_user);

router.post('/signup', authController.signup);

router.post('/login', authController.login);

router.get('/:userid', authController.me);


export default router