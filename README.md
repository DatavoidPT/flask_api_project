# Flask API Project

Template for starting a flask API project with unittest using coverage and nose2.

What Is This?
-------------

This is a simple Python/Flask web application intended to provide a working example of a WebAPI for multiple testing and playing purposes. The goal of the only existing endpoint is to be simple and return a simple message. The application is container ready and can be initialized using its dockerfile also in the repository.


Environment Requirements?
-------------

- Python 3 Installed in your local envirnoment
- Docker Installed in your local envirnoment 


How To Use This
---------------

1. Clone the repository to your local environment.
5. Run `pip install -r requirements.txt` to install dependencies
2. If you want to run it without docker just run `python app.py`.
4. If you want to run it from docker:
  4.1 Run `docker build -t app .`
  4.2 Run `docker run --name app_nike -d -p 5000:5000 --restart on-failure app`
6. Navigate to http://localhost:5000 in your browser
