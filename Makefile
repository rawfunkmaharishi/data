PROJECT = $(shell basename $(shell pwd))
ID = rfm/${PROJECT}

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

format:
	python -m isort .
	python -m black .

deploy:
	curl -X POST -d {} https://api.netlify.com/build_hooks/63ac59de37c6b11675856637
