# Task
- Create a web server
- accepts a put request to create entry in database
- if the entry already exists update the birthday if it is different.
- gets the entry from database and displays the difference in days

# Do things

- [x] Python setup
- [x] Docker setup
- [x] Create http listener
- [x] TDD setup
- [x] Basic classes for requests
- [x] DB schema management
- [ ] Systems diagram
- [ ] Kubernetes deployment file
- [ ] Deployment instructions
- [ ] docker-compose setup for local testing
- [ ] create database index for better query response
- [ ] Read and write database routes
- [ ] Use server side caching maybe?

# Instructions

The following instructions assume that the developer has Docker installed.

## Commands

- `make build` : This builds the app image.
- `make build-prod`: This builds the image for production use.
- `make port=80 dev`: Starts up the server on port 80. For development we are using in-memory sqlite database.
- `make test`: run tests

## Directory structure

- `scripts`: This holds the scripts required for distinguishing dependecies installation in dev and prod environment.
- `server`: Holds the application code.
- `tests`: Tests reside here.

## HTTP endpoints

- `/`: 
  - Description: Index, responds with `Hello, world!`
  - Supported Methods: `['Get']`
- `/hello/<username>`:
  - Description: If the http method is `GET` then it returns the day remaining for birthday of user. Otherwise, if the method is `PUT` then it sets/updates the user's birthdate.
  - Supported Methods: `['GET', 'PUT']`
