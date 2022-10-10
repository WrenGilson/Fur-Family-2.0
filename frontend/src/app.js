// import './App.css';
import Card from "./components/card.js"
import Header from "./components/header.js"
import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import axios from "axios";

import { getList } from './list';

function App() {
    const [list, setList] = useState([]);
  
    useEffect(() => {
      let mounted = true;
      getList()
        .then(items => {
          if(mounted) {
            setList(items)
          }
        })
      return () => mounted = false;
    }, [])

    const cards = list.map(item => {
        console.log(item)
        return (
          <div className="card">
            
            <Card
                key={item.name}
                {...item}
            />
          </div>
        )
    })   
  
    return(
      <div className="body">
       <Header />
       {cards}
     </div>
    )
  }
  
  export default App;