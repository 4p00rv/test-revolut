IMAGE="revolut-test"
build:
	docker build --build-arg ENV=development -t ${IMAGE} .
build-prod:
	docker build --build-arg ENV=production -t ${IMAGE}-prod .
dev: build
	docker run -p $(port):8080 -e ENV=development ${IMAGE}
prod: build-prod
	docker run -p $(port):8080 -e ENV=production ${IMAGE}-prod
test: build
	docker run -e ENV=testing ${IMAGE} nose2 tests
