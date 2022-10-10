// import './App.css';
import Card from "./components/card.js"
import Header from "./components/header.js"
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import axios from "axios";

import { API_URL } from "../constants";



function App() {
    getPets = () => {
        axios.get(API_URL).then(res => this.setState({ pets: res.data }));
      };
      
    const cards = rest.map(item => {
      return (
        <div className="card">
          
          <Card
              key={item.id}
              {...item}
          />
        </div>
      )
  })    
  
  return (
    <div className="body">
      <Header />
      {cards}
    </div>
  )

}

export default App;
