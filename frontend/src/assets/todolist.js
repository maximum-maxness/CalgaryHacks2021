import React, {Component} from 'react';
import Form from "react-bootstrap/Form";
class Task {
    descr = "";
    date = ""; 
    constructor(descr, date){
        this.descr = descr;
        this.date = date;
    }
}
// example date: 02/07/21
    function NewTask(descr, date) {
        var task = new Task(descr, date)
        return task;
    }
    function AddTask(task, list) {
        List.state.list.push(task)
    }
class List extends Component {
    state = []; 
    count = 0;
    // FiveTasksCompleted(list){
    //     for (i=0; i < list.size(); i++) {
    //         if (list.get(i)
    //     }
    // }



    
    EditList() {
        let descr;
        let date;


        return(
            <div className= "List">
            {/* <h1> List Your Tasks:  </h1>
                <input type='descr' id='descr'
                placeholder='Enter Task'
                onChange={ e => this.updateInput("newTask", e.target.T) }/>
                <input type='date' id='date'
                placeholder='Enter Date'
                // T = {this.newTask(descr, date)} //T= task
                onChange={ e => this.updateInput("newTask", e.target.T) }/>
                {descr = document.getElementById("descr").value}
                {date = document.getElementById("date").value} */}
            <Form className="login_form">
                <Form.Group className="form_element" controlId="formBasicEmail">
                <Form.Label>Enter Task</Form.Label>
                <Form.Control type="descr" placeholder="Enter Task" />
                </Form.Group>

                <Form.Group className="form_element" controlId="formBasicPassword">
                <Form.Label>Enter Due Date</Form.Label>
                <Form.Control type="date" placeholder="Due Date" />
                </Form.Group>
            </Form>

                

                
                <button
        
                    onClick={()=>AddTask(NewTask(descr, date), this.state)}
                >
                add
                </button>
            
                </div>)}

}








export default List