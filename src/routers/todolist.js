import express from 'express';
import * as todolistController from '../controllers/todolist.js';
import { body } from 'express-validator';
import { validate } from "../middlewares/validator.js";
import { isAuth } from '../middlewares/user.js';

const router = express.Router();


router.get('/', isAuth, todolistController.getAllTodolist);

router.post('/', isAuth, todolistController.createTodolist);

router.get('/userid', isAuth, todolistController.getUserTodolist);

router.put('/update', isAuth, todolistController.updateTodolist);

router.delete('/delete', isAuth, todolistController.deleteTodolist);


export default router;

