import express from 'express';
import * as checklistController from '../controllers/checklist.js';
import { isAuth } from '../middlewares/user.js';

const router = express.Router();


router.get('/', isAuth, checklistController.getAllChecklist);

router.post('/', isAuth, checklistController.createChecklist);

router.get('/userid', isAuth, checklistController.getUserChecklist);

router.get('/useriddate', isAuth, checklistController.getUserDateChecklist);

router.put('/update', isAuth, checklistController.updateChecklist);

router.delete('/delete', isAuth, checklistController.deleteChecklist);


export default router;