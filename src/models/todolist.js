import Mongoose from 'mongoose';
import { useVirtualId } from './database.js';

// id 자동으로 생성됨 
const todolistSchema = new Mongoose.Schema({
    userid: {type: String, require: true},
    title: {type: String, require: true},
    text: {type: String, require: true},
    color: {type: String, require: true},
    examDate: { type: Date,  require: true},
    createdAt: { type: Date, default: Date.now }
})

useVirtualId(todolistSchema);
const Todolist = Mongoose.model('list', todolistSchema);

// 모든 리스트를 리턴
export async function getAll() {
    return Todolist.find().sort({ createdAt: -1 });
}

// 해당 아이디에 대한 리스트를 리턴
export async function getAllByUserid(userid) {
    return Todolist.find({ userid }).sort({ createdAt: -1 });
}

// 새로운 To-Do 리스트 생성
export async function createTodolist({ userid, title, text, color, examDate }) {
    return new Todolist({ userid, title, text, color, examDate }).save().then(data => data.userid);
}

// To-Do 리스트 업데이트
export async function updateTodolist(_id, { title, text, color, examDate }) {
    return Todolist.findByIdAndUpdate(_id, { title, text, color, examDate }, { new: true });
}

// To-Do 리스트 삭제
export async function removeTodolist(_id) {
    return Todolist.findByIdAndDelete(_id);
}
