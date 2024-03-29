const TodosApp = {
    data() {
        return {
            todos: [],
            enteredTodoText: '',
            editedTodoId: null
        };
    },
    methods: {
        async saveTodo(event) {
            event.preventDefault();

            if (this.editedTodoId) {
                // Updating a todo
                const todoId = this.editedTodoId;
                const todoIndex = this.todos.findIndex(function(todoItem) {
                    return todoItem.id === todoId;
                });

                const updatedTodoItem = {
                    id: this.todos[todoIndex].id,
                    text: this.enteredTodoText
                };

                this.todos[todoIndex] = updatedTodoItem;
                this.editedTodoId = null;
            } else {
                // Creating...
                const newTodo = {
                    text: this.enteredTodoText,
                    id: new Date().toISOString(),
                };

                // let response;

                // try {
                //     response = await fetch('http://localhost:3000/todos', {
                //     method: 'POST',
                //     body: JSON.stringify({
                //         text: this.enteredTodoText,
                //     }),
                //     headers: {
                //         'Content-Type': 'application/json',
                //     },
                //     });
                // } catch (error) {
                //     alert('Something went wrong!');
                //     return;
                // }

                // if (!response.ok) {
                //     alert('Something went wrong!');
                //     return;
                // }

                // const responseData = await response.json();
                // const todoId = responseData.createdTodo.id;
                
                // const newTodo = {
                //     text: this.enteredTodoText,
                //     id: todoId
                // };

                this.todos.push(newTodo);
            }

            

            this.enteredTodoText = '';
        },
        startEditTodo(todoId) {
            this.editedTodoId = todoId;
            const todo = this.todos.find(function(todoItem) {
                return todoItem.id === todoId;
            });
            this.enteredTodoText = todo.text;
        },
        deleteTodo(todoId) {
            this.todos = this.todos.filter(function(todoItem) {
                return todoItem.id !== todoId;
            });
        }
    },
    async created() {
        // let response;
        // try {
        //     response = await fetch('http://localhost:3000/todos');
        // } catch (error) {
        //     alert('Something went wrong!');
        //     return;
        // }

        // if (!response.ok) {
        //     alert('Something went wrong!');
        //     return;
        // }

        // const responseData = await response.json();
        // const todos = responseData.todos;
    }
};

Vue.createApp(TodosApp).mount('#todos-app');