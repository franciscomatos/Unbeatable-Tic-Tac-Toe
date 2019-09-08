# Unbeatable Tic-Tac-Toe

Web App consisting of the classic Tic-Tac-Toe game with different difficulty modes created using Angular, Flask and Python.
Contains an Unbeatable Mode which makes it impossible for the player to beat the CPU. This was achieved using the Minimax algorithm.

## Getting Started

Download the .zip and open two command lines to run the backend and the frontend.

### Prerequisites

To start, you will need an up to date version of Python 3. 
If you don't have Python 3 available on your machine, please, browse to the [Python download page](https://www.python.org/downloads/) and install it.

After installing Python, you will have to install the pipenv tool:

```
pip install pipenv
```

Now you will need to install Flask. You will also need to install marshmallow to handle serialization and deserialization of JSON objects. 
To install both dependencies, issue the following command in the backend directory:

```
pipenv install flask marshmallow
```

As Angular was used to create your frontend application, you will need Node.js and NPM installed on your machine. 
You can install both tools simultaneously by downloading and executing an installer (choose one based on your operating system) from the [Node.js download page](https://nodejs.org/en/download/).


### Installing

After properly installing Node.js and NPM, you can use the npm command to install the Angular CLI tool and all dependencies.
Just run the following command inside the frontend directory:

```
npm install
```

Now everything should be ready to run the servers. 
In the backend repository make the bootstrap.sh script executable and execute it in the background.

```
chmod u+x bootstrap.sh

./bootstrap.sh &
```

With all these changes in place, you can run your Angular application (run ng serve on the frontend directory) to check if everything is working as expected.
After Angular finishes compiling your app, you can browse to http://localhost:4200 and start playing!

## Authors

* **Francisco Matos**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
