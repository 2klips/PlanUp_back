import express from 'express';
import * as recruitmentController from '../controllers/recruitment.js';
import { isAuth } from '../middlewares/user.js';

const router = express.Router();


router.post('/get_details', isAuth, recruitmentController.getJobDetails);


export default router