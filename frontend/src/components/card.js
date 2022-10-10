import React from 'react'

export default function Card(props) {
  function animalType () {
    if(props.animalType == "dog")
      return "dog.png"
    else if (props.animalType == "cat")
      return "cat.png"
  }
  function imageName() { 
    return props.name + ".jpg"
  }


  return (
    <div className="Card">
        <img className="card--img" src={imageName()}/>
          <div className="card--body">
          <div className="card--header">
            <img className="card--type" src={animalType()} />
            <h2 className="card--name">{props.name}</h2>
          </div>
          <h3 className="card--age">
            <div className="card--lived">Adopted {props.adoptionYear} </div> 
            {props.death && <div className="card--death">&nbsp;and said farewell&nbsp;{props.death}</div>}
          </h3>
          <p className="card--description">{props.description}</p>
        </div>

    </div>
  );
}

