.PHONY: dev, run

dev:
	pipenv install
	pipenv run pip freeze > requirements.txt

run:
	docker build -t product-lookuper .
	docker run -d -v ${PWD}/persistence:/usr/src/app/persistence --name product-lookuper product-lookuper
