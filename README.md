# cybersec-bulletin

This is a completely dockerized cybersecurity bulletin web application built over FastAPI, ReactJS and MongoDB.

## Use cases:
- Refines the traditional methods of looking up information for articles
- Short and crisp bursts of information
- Great for staying updated with the latest trends and features in cybersecurity

## How to use it:
### Pre-requisites:
- Docker must be installed and running on the user's system ( [Link to docker download page](https://www.docker.com) )
- For Windows users
  - Please make sure you're using Windows 10 or Above, With WSL setup ( usually takes less than 5 minutes , You can refer to this [official documentation from Microsoft](https://learn.microsoft.com/en-us/windows/wsl/install) )
- For UNIX users, Only docker installed is enough
- That's it!

### Running this application:
I have provided a ./dist folder which contains executables for major Operating System

#### For windows:
- Execute the `run-web-app.bat` located in th dist/ directory of this project.
- Please be patient as docker builds your application, First time execution can take upto 4-5 minutes

#### For UNIX based operating systems(MAC OS, Ubuntu, Arch etc.)
 - Open your terminal and redirect into dist/ directory
 - Now run `sudo sh ./run-web-app.sh` ( Heads up! It might ask you for your system password, Please provide that )
 - Again, Please be patient for the first instantiation, The process is a lot quicker henceforth

##### (A quick note: Please keep the terminals made by the executables open as long as you want to run the application, Since it is a local deployment)
##### (A quick note: running the .bat file might give you a warning of unknown signature, Please rest assured and run the file anyways. This happens because the file needs official certificate signing which was not possible in the development phase)
  
### Where can I see my application:
The application is hosted at https://localhost:3000
You can access the bulletin by opening this url in your web browser

### (This section is only for developers/maintainers of this project)
- For deployment on servers, Please setup an orchestration tool like kubernetes
- Make necessary adjustments to `dockerfiles` and `docker-compose.yaml`
- The Web scraper folder contains `Scraperv1.py` which contains the logic of scrapping, Same has been implemented in the backend
- If you encounter any issues/bugs/queries pertaining the bulletin, Please feel free to contact me over my E-Mail, gauravpadam2@gmail.com
- Safran must have rest of my details as well, Please feel free to contact me over other platforms as well


#### I hereby hand over complete ownership of this project to Safran Digit, This repository will be made private for maintainence purposes only within 5 business days
#### Sign-off: Gaurav Padam, Ex- Safran Digit Intern


