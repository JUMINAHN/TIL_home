const todoForm = document.querySelector("#todo-form") // form
const todoInput = document.querySelector("#todo-form input") // input 태그 자체를 넣어야 함
const toDoList = document.querySelector("#todo-list") // ul

const TODOS_KEY = "toDos";

//to do list 삭제하기
function deleteToDo(event) { 
  const li = event.target.parentElement; 
  li.remove();
}

const toDos = [];

function saveToDos() { 
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos));
}


//to do list 만들기
function paintTodo(newTodo) { 
  const li = document.createElement("li");
  const span = document.createElement("span");
  span.innerText = newTodo; 
  const button = document.createElement("button");
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo); //click을 할 때 todo를 삭제할 것

  li.appendChild(span);   
  li.appendChild(button); 

  toDoList.appendChild(li);
}


//새로 고침 event를 막을 것
function handleToDoSubmit(event) { 
  event.preventDefault();
  const newTodo = todoInput.value;
  todoInput.value = ""; 
  toDos.push(newTodo); 
  paintTodo(newTodo); 
  saveToDos(); 
}

todoForm.addEventListener("submit", handleToDoSubmit)



//local에 있는 내용 저장
const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos) {
  const parsedToDos = JSON.parse(savedToDos); 
  parsedToDos.forEach((item) => console.log("this is the turn of", item))


} else {

}