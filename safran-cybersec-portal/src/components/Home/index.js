import React from 'react';
import './index.scss';

const Home = () => {
  return (
    <div className='container'>
      <div className='row'>
        <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src='https://www.bleepstatic.com/content/hl-images/2023/06/09/MOVEit-headpic.jpg' alt="Tile Image" />
            <h2>New MOVEit Transfer critical flaws found after security audit, patch now</h2>
          </div>
        </div>
        <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src='https://www.bleepstatic.com/content/hl-images/2022/10/28/Windows.jpg' alt="Tile Image" />
            <h2>PoC released for Windows Win32k bug exploited in attacks</h2>
          </div>
        </div>
        <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src='https://www.bleepstatic.com/content/hl-images/2023/06/07/honda-2.jpg' alt="Tile Image" />
            <h2>Honda API flaws exposed customer data, dealer panels, internal docs</h2>
          </div>
        </div>
      </div>
      <div className='row'>
        <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src='https://www.bleepstatic.com/content/hl-images/2021/09/22/VMware-headpic.jpg' alt="Tile Image" />
            <h2>VMware fixes critical vulnerabilities in vRealize network analytics tool</h2>
          </div>
        </div>
        <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src='https://www.bleepstatic.com/content/hl-images/2022/04/07/android.jpg' alt="Tile Image" />
            <h2>Android security update fixes Mali GPU bug exploited as zero-day</h2>
          </div>
        </div>
        <div className='col-md-4 col-sm-6 col-xs-12 tile'>
          <div className="tile-content">
            <img src='https://www.bleepstatic.com/content/hl-images/2022/12/08/Google_Chrome.jpg' alt="Tile Image" />
            <h2>Google fixes new Chrome zero-day flaw with exploit in the wild</h2>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
