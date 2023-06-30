import React, { useEffect, useState } from 'react';
import './index.scss';
import ReactPaginate from 'react-paginate';

const Home = () => {

  const [items , setItems] = useState([]);

  useEffect(() => {
    const getArticles = async () => {
      const res = await fetch("http://localhost:8000/1");
      const data = await res.json();
      setItems(data)
    };

    getArticles();

  }, []);

  const fetchOnPageChange = async (currentpage) => {
    const res = await fetch(`http://localhost:8000/${currentpage}`);
    let data = await res.json()
    setItems(data)
  }

  const handlePageClick = (data) => {

    let currentpage = data.selected + 1
    fetchOnPageChange(currentpage)
    
  }

  return (
    <div className='container'>
      <div className='row md-2'>

      { items.map((item) => {
         return (
         <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src={item.Picture} alt="Tile thumbnail" />
            <h2>{item.Title}</h2>
          </div>
        </div>
        )
      })}

      </div>

      <div className='row md-2'>

        <ReactPaginate
          previousLabel = {'previous'}
          nextLabel = {'next'}
          breakLabel = {'...'}
          pageCount={3}
          marginPagesDisplayed={'2'}
          pageRangeDisplayed={'3'}
          onPageChange={handlePageClick}
          containerClassName={'pagination justify-content-center'}
          pageClassName= {'page-item'}
          pageLinkClassName= {'page-link'}
          activeClassName= {'active'}
          previousClassName= {'page-item'}
          previousLinkClassName={'page-link'}
          breakClassName= {'page-item'}
          breakLinkClassName= {'page-link'}
          nextClassName= {'page-item'}
          nextLinkClassName= {'page-link'}
        />

      </div>
      
      </div>
  );
};

export default Home;
