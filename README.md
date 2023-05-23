🔗 [Kanban board](https://github.com/users/SzymkowskiDev/projects/10/views/1)

# Estate Marketplace
Lessons learned from Workforce Data Platform, we start with: sourced data, docker setup, relational database and key-value database (both filled with data). We focus on Python development of: REST API and Django app.


## 🔗 Related Projects
* First edition: [Workfroce Data Platform](https://github.com/SzymkowskiDev/workforce-data-platform)


## 🏛️ Architecture
![architecture](https://github.com/SzymkowskiDev/estate-marketplace/blob/main/assets/arch.png?raw=true)


## 🚀 How to get started?
Step 1. Install Docker Desktop [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)

Step 2. Clone the repository `git clone https://github.com/SzymkowskiDev/estate-marketplace.git`

Step 2.5 Replicate python environment
- Step 2.5 Create a virtual environment and activate it: 
    - `python -m venv myenv`
    - `myenv\Scripts\activate.bat`
- Step 2.5 B) Install dependencies: `pip install -r requirements.txt`

Step 3. Launch Docker Desktop

~~`Step 4. Open terminal in the project and run build docker image: `docker build -t estate-db .`~~

Step 5. Start the container: `docker-compose up -d`

Step 6. Create the postgres database:

- Step 6.1 Identify container id with: `docker ps` 

- Step 6.2 Open a terminal session inside the container: `docker exec -it <paste here container id> bash`

- Step 6.3 Connect to the PostgreSQL server running inside the container: `psql -U postgres`

- Step 6.4 Create the estate database by running the command: `CREATE DATABASE estate;`

- Step 6.5 Exit postgres CLI with: `\q` and terminal session with: `exit`

Step 7. Populate relational database by executing script `postgres/populate.py`

Step 8. Populate key-valye database by executing script `redis/populate.py`

Step 9. Run the app:
- A) To run FastAPI app run the command: `uvicorn main:app --reload` and open [http://127.0.0.1:8000](http://127.0.0.1:8000)
- B) To run Django app run the command: `python manage.py runserver` and open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 


## 📅 Development schedule

- 27/05/2023: Introductory meeting & Start of Sprint 1
- 10/07/2023: Sprint 1 review
- 24/07/2023: Sprint 2 review

**Pre-development: System Architecture**

- [x] Docker setup
- [x] Postgres setup
- [x] Redis setup
- [x] Django skeleton
- [x] FastAPI skeleton

**Development - Microservices (FastAPI) & Django App**

- [ ] `interactive-map`
- [ ] `data-migration`
- [ ] `offers-listing`
- [ ] `mortgage-advisor`
- [ ] `analytics-client`
- [ ] `msgs`
- [ ] `transation-system`
- [ ] `auth`
- [ ] `micro-arch`
- [ ] `row-level-security`


## 🗃️ Data
Our data comprises of:
- 4657 real estate offers
- 3000 sellers
- 2000 buyers
- 1000 transactions involving these three entities

__Entity Relationship Diagram__

![erd](https://github.com/SzymkowskiDev/estate-marketplace/blob/main/assets/erd.PNG?raw=true)

While offers, sellers and buyers data is held in relational database, transactions are stored in key-value database. Example of key-value pair: ``"offer_1496_seller_2997_buyer_1231_date_2020-07-12": "aborted"``

We can note, that keys hold IDs of offers as well as those of parties involved and the date. Values on the other hand represent the status of each transaction. Possible statuses are: 

`placed` (buyer asks to buy) -> `accepted` (seller accepted, awaiting payment) -> `completed` (buyer made payment) and `aborted` (any system error or unexpected situation in the business flow)


## 🎓 Learning Materials
* How to install `docker` for Windows [docs.docker.com](https://docs.docker.com/desktop/install/windows-install/)
* `Postgres` documentation [postgresql.org](https://www.postgresql.org/)
* `psycopg2` documentation [psycopg.org](https://www.psycopg.org/docs/)
* `Redis` documentation [redis.io](https://redis.io/)
* How to use `redis` with Python [realpython.com](https://realpython.com/python-redis/)
* `FastAPI` documentation [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
* `Django` documentation [djangoproject.com](https://www.djangoproject.com/)


## 👨‍💻 Contributing
- a
- b
- c
- d
- e
- f
- g

![logo](https://github.com/SzymkowskiDev/estate-marketplace/blob/main/assets/logo.png?raw=true)

## 📄 License
[MIT License](https://choosealicense.com/licenses/mit/) ©️ 2019-2020 [Kamil Szymkowski](https://github.com/SzymkowskiDev "Get in touch!")

[![](https://img.shields.io/badge/license-MIT-green?style=plastic)](https://choosealicense.com/licenses/mit/)
