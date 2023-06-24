
import { Route, Routes } from 'react-router-dom';
import './App.scss';
import Layout from './components/Layout';
import Home from './components/Home';
import ReactPaginate from 'react-paginate';
import { useEffect, useState } from 'react';

function App() {

  const [items , setItems] = useState([]);

  useEffect(() => {
    const getArticles = async () => {
      const res = await fetch("http://localhost:3004/Articles?_page=1&_limit=6");
      const data = await res.json();
      setItems(data)
    };

    getArticles();

  }, []);

  const handlePageClick = (data) => {
    
  }

  return (
    <>
      <Routes>
        <Route path='/' element={<Layout />}>
        <Route index element={<Home />} />
        </Route>
      </Routes>
      <ReactPaginate
        previousLabel = {'previous'}
        nextLabel = {'next'}
        breakLabel = {'...'}
        pageCount={25}
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
    </>


  );
}

export default App;
