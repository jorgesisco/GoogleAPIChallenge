#Install pipenv and required dependencies

install env:
	pipenv install
	pipenv shell

dependencies:
	pipenv install -r requirements.txt