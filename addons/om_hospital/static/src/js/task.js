const {Component, mount, xml, useState} = owl

odoo.define('hospital.task', function(require) {
  var ajax = require('web.ajax');

class Task extends Component {
    static template = xml`
    <li t-attf-style="background-color:#{state.color}" class="d-flex align-items-center justify-content-between border-bottom p-1 border rounded mb-1">
      <div t-if="state.isEditing" class="d-flex align-items-center flex-grow-1 me-2">
        <input t-ref="text1" t-model="state.title" class="form-control me-2"/>
        <input style="width:60px" type="color" class="form-control-lg border-0 bg-white m-0 form-control-color" id="color" t-att-value="state.color" t-model="state.color" title="Choose your color"/>
      </div>
      <div t-if="!state.isEditing" class="form-check form-switch fs-5 name-dark">
        <input class="form-check-input" type="checkbox" value="" role="switch" 
        t-att-id="state.id" t-att-checked="state.isCompleted" t-on-click="toggleTask"/>
        <label t-att-for="state.id" t-attf-class="#{state.isCompleted ? 'text-decoration-line-through':''}">
            <t t-esc="state.title"/>
        </label>
      </div>
      <div>
        <button t-if="!state.isEditing" class="btn btn-primary me-2" t-on-click="editTask">
          <i class="bi bi-pencil"></i>
        </button>
        <button t-if="state.isEditing" class="btn btn-primary me-2" t-on-click="saveTask">
          <i class="bi bi-check-lg"></i>
        </button>
        <button class="btn btn-danger" t-on-click="deleteTask"><i class="bi bi-trash"></i></button>
      </div>
    </li>
    `
  
    // use to get the states from parent component
    static props = ["task", "onDelete", "onEdit"];

    // initialize our state based on parent states
    setup(){
        this.state = useState({
        isEditing:false,
        title: this.props.task.title,
        id: this.props.task.id,
        isCompleted: this.props.task.isCompleted,
        color: this.props.task.color,
        })
    }

    // toggle task
    toggleTask() {
        this.state.isCompleted = !this.state.isCompleted;
      }
    
      deleteTask() {
        this.props.onDelete(this.props.task);
      }
    
      // save the edited task
      saveTask() {
        this.state.isEditing = false
        this.props.onEdit(this.state);
      }
    
      // use to show and hide form input
      editTask() {
        this.state.isEditing = true
      }
    }

class Root extends Component {
  static template = xml`
    <div class="m-0 p-2 bg-white rounded">
        <div class="input-group-lg bg-white rounded border d-flex w-100 align-items-center">
        <input type="title" class="form-control-lg fs-3 flex-fill border-0" placeholder="Add your new task" aria-label="Add your new task" id="title" name="title" aria-describedby="button-addon2" 
            t-att-value="state.title" t-model="state.title"/>
        <input type="color" class="form-control-lg border-0 bg-white m-0 form-control-color" id="color" title="Choose your color" 
            t-att-value="state.color" t-model="state.color"/>
        <button class="btn btn-primary" type="button" id="button-addon2" 
            t-on-click="addTask"><i class="bi bi-plus-lg fs-3"></i></button>
        </div>

        <ul class="tasks d-flex flex-column p-0 mt-4">
            <t t-foreach="tasks" t-as="task" t-key="task.id">
                <Task task="task" onDelete.bind="deleteTask"  onEdit.bind="editTask"/>
            </t>
        </ul>
    </div>
  `

  // use to add sub component
  static components = { Task };

  // constructor(){
    // super(...arguments);
  setup(){
    this.state = useState({
      title: "",
      color: "#0000FF",
      isCompleted: false,
      isEditing: false
    });

    this.tasks = useState([])
    this._fetchTasks();
  }

  async _fetchTasks() {
    let tasks = await ajax.rpc('/hospital/task', { });
    tasks = JSON.parse(tasks)
    tasks.map(task=>{
      this.tasks.push(task)
    })
  }

  async _addTask(title,color,isCompleted) {
    let task = await ajax.rpc('/hospital/task/create', {title,color,isCompleted})
    task = JSON.parse(task)
    return task
  }
  
  async addTask(){
    // do not allow empty task name
    if (!this.state.title){
      alert("Please add task title.")
      return
    }

    let newTask = await this._addTask(this.state.title,this.state.color,this.state.isCompleted,);
   
    // add new task
    this.tasks.push(newTask)
    // this.tasks.push({
    //   id,
    //   title: this.state.title,
    //   color: this.state.color,
    //   isCompleted: this.state.isCompleted,
    // })

    // reset states after saving
    this.state = {isCompleted:false, title:"", color: "#FFF700"}
  }

    // delete task
    deleteTask(task){
        const index = this.tasks.findIndex((t) => t.id === task.id);
        this.tasks.splice(index, 1);
      }

    // edit task
    editTask(ta){
        const index = this.tasks.findIndex((t) => t.id === ta.id);
        this.tasks.splice(index, 1, ta)
    }
}
mount(Root, document.getElementById("task_root"));

});