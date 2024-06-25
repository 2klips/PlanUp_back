import express from "express";
import * as authController from '../controllers/user.js';
import { isAuth } from '../middlewares/user.js';

const router = express.Router()


router.delete('/:userid', isAuth, authController.del_user);

router.post('/signup', authController.signup);

router.post('/login', authController.login);

router.get('/:userid', authController.me);

router.get('/verifyToken', isAuth
    , (req, res) => {
        user = req.user;
        token = req.token;
        console.log('verifyToken:', user);
        res.status(200).json({success: true, user, token});
    }
)

export default router