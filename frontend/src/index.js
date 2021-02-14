import React from 'react'
import ReactDom from 'react-dom'
import './index.css'
import './navigation.js'
import Navbar from './navigation.js';
import 'bootstrap/dist/css/bootstrap.min.css';

// stateless functional component
// always return JSX

const image =  'https://images-na.ssl-images-amazon.com/images/I/81eB+7+CkUL.jpg';

function App(){
  return (
    <Navbar />
  );
}

ReactDom.render(<App />, document.getElementById('root'));


