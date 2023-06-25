
import { Route, Routes, json } from 'react-router-dom';
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

  const fetchOnPageChange = async (currentpage) => {
    const res = await fetch(`http://localhost:3004/Articles?_page=${currentpage}&_limit=6`);
    let data = await res.json()
    setItems(data)
  }

  const handlePageClick = (data) => {

    let currentpage = data.selected + 1
    fetchOnPageChange(currentpage)
    
  }

  return (
    <>
      <Routes>
        <Route path='/' element={<Layout />}>
        <Route index element={<Home items={items}/>} />
        </Route>
      </Routes>
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
    </>


  );
}

export default App;
