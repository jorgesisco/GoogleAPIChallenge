#Install pipenv and required dependencies

install:
	pipenv install
	pipenv shell

dependencies:
	pipenv install -r requirements.txt