PROJECT = $(shell basename $(shell pwd))
ID = rfm/${PROJECT}

all: format lint test clean  ## format, lint, test, clean (default)

black:
	python -m black .

isort:
	python -m isort .

format: black isort  ## run the formatters

lint:  ## run the linters
	python -m pylama

test:  ## run the tests
	PYTHONDONTWRITEBYTECODE=1 \
	python -m pytest \
		--random-order \
		--verbose \
		--capture no \
		--failed-first \
		--cov \
		--exitfirst

clean:  ## clean up artefacts
	@rm -fr .pytest_cache
	@rm -fr $$(find . -name __pycache__)

install:  ## install dependencies
	python -m pip install -r requirements.txt

generate:
	python generator.py

###

build:
	docker build \
		--build-arg PROJECT=${PROJECT} \
		--tag ${ID} .

run:
	docker run \
		--name ${PROJECT} \
		--hostname ${PROJECT} \
		--volume $(shell pwd):/opt/${PROJECT} \
		--interactive \
		--tty \
		--rm \
		--publish 8000:8000 \
		${ID} \
		bash

exec:
	docker exec \
		--interactive \
		--tty \
		${PROJECT} \
		bash

deploy:
	curl -X POST -d {} https://api.netlify.com/build_hooks/63ac59de37c6b11675856637
