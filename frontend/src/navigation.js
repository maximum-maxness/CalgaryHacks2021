import React, { useState, useEffect } from 'react';
// import { Button } from './Button';
import './navigation.css';
import logging_in from './login-page'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams
} from "react-router-dom";
import List from './assets/todolist';

/*
    This file is a modified version of Brian Codex's React website tutorial 
    found here: https://github.com/briancodex/react-website-v1/blob/master/src/components/Navbar.js

*/
var d = new Date();

function dates(){
  currDate = d.getDay();
  // switch(currDate):
  //   case 
}


function NavbarItem(props) {
    return(
        <div className='navbar-item'>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
             </style>
            {props.text}
        </div>
    )
}

function About() {
      return(
        <div className='about'>
          <section className='about-header'>
            
            <h1>
             A Place of Productivity
             </h1>
          </section>
          <section className='about-body'>
            Gather your friends and feel the motivation to do what you need to do.
          </section>
        </div>
        
        // <div className='about-header'>
        //   <h1>A Place of Productivity</h1>
        //   <div className='about-body'>
        //     Gather your friends and never feel unmotivated again.
        //   </div>
        // </div>
      )
}

function Chores() {
  var list = new List();
      return(
        <div>
          <section className='chores'>
          <h1>
            ToDo:
          </h1>
          <li>Do Homework: Due Monday Feb 15</li>
        </section>
        <list.EditList/>
        {/* <section className="chore-day">Next Chores Day: {d.getDay()}</section> */}
        </div>
        
        // <div className='about-header'>
        //   <h1>A Place of Productivity</h1>
        //   <div className='about-body'>
        //     Gather your friends and never feel unmotivated again.
        //   </div>
        // </div>
      )
}

function Home() {
      return(
        <div className='home'>
          <h1>
            ToDo:
          </h1>
          <li>Do Homework</li>
        </div>
        
        // <div className='about-header'>
        //   <h1>A Place of Productivity</h1>
        //   <div className='about-body'>
        //     Gather your friends and never feel unmotivated again.
        //   </div>
        // </div>
      )
}



function Navbar() {
  const [click, setClick] = useState(false);
  const [button, setButton] = useState(true);

  const handleClick = () => setClick(!click);
  const closeMobileMenu = () => setClick(false);
  var log_in = new logging_in();

//   const showButton = () => {
//     if (window.innerWidth <= 960) {
//       setButton(false);
//     } else {
//       setButton(true);
//     }
//   };

//   useEffect(() => {
//     showButton();
//   }, []);

//   window.addEventListener('resize', showButton);

  return (
    <>
          <Router>
            <nav className='navigation'>
              <Link to="/about">
                <NavbarItem text="About"/>
              </Link> 
              <Link to="/signup">
                <NavbarItem text="Signup/Login"/>
              </Link> 
              <Link to="/chores">
                <NavbarItem text="My Chores"/>
              </Link> 
              <Link to="/home">
                <NavbarItem text="My House"/>
              </Link> 
              
            </nav>

            <Switch>
              <Route path="/about">
                <About />
              </Route>
              <Route path='/signup'>
                <log_in.Login />
              </Route>
              <Route path='/chores'>
                <Chores />
              </Route>
              <Route path='/home'>
                <Home />
              </Route>
            </Switch>
          </Router>
    </>
  )
}

  

  export default Navbar;