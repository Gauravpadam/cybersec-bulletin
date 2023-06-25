import React from 'react';
import './index.scss';

const Home = ({items}) => {
  return (
    <div className='container'>
      <div className='row md-2'>

      { items.map((item) => {
         return (
         <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src={item.Picture} alt="Tile Image" />
            <h2>{item.Title}</h2>
          </div>
        </div>
        )
      })}
      
      </div>
    </div>
  );
};

export default Home;
