import React, {Component} from 'react';
import 'todolist'
class Pictures extends Component {

    constructor(props) {
        super(props);
        this.onMove = this.onMove.bind(this);
        const V = 9;
        
    }

    onMove() {
        console.log(this.testVarible);
    }

render() {
    
    
    
   /* if(.equals(True)){V--;}
    else{V++}*/
    
    
    
    
    
    if (V==9) {
        return(
            <img src ="/CalgaryHack2021/frontend/src/assets/shack.png" alt=""/>)
    } else if(V==8) {
        return (
            <img src ="/CalgaryHack2021/frontend/src/assets/brokenhouse.jpg" alt=""/>) }

        else if (V==7) {
                return(
                    <img src ="/CalgaryHack2021/frontend/src/assets/house.jpg" alt=""/>)
            } else if(V==6) {
                return (
                    <img src ="/CalgaryHack2021/frontend/src/assets/medium_house_broken(1).png" alt=""/>)    } 

                    if (V==5) {
                        return(
                            <img src ="/CalgaryHack2021/frontend/src/assets/medium_house.png" alt=""/>)
                    } else if(V==4) {
                        return (
                            <img src ="/CalgaryHack2021/frontend/src/assets/brokemansion.jpg" alt=""/>)}
                            if (V==3) {
                                return(
                                    <img src ="/CalgaryHack2021/frontend/src/assets/mansion.jpg" alt=""/>)
                            } else if(V==2) {
                                return (
                                    <img src ="/CalgaryHack2021/frontend/src/assets/brokehouse3.jpg" alt=""/>)}

                                    if (V<=1) {
                                        return(
                                            <img src ="/CalgaryHack2021/frontend/src/assets/house3" alt=""/>)
                                    } else {
                                        return (
                                            <img src ="/CalgaryHack2021/frontend/src/assets/shack_broken.png" alt=""/>)

}}}