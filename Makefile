IMAGE="revolut-test"
build:
	docker build --build-arg ENV=development -t ${IMAGE} .
build-prod:
	docker build --build-arg ENV=production -t ${IMAGE}-prod .
dev: build
	#docker run -p 80:80 -e FLASK_ENV=development -e SECRET_KEY=dev -e LOGLEVEL=INFO ${IMAGE}
	docker run -p 80:80 -e ENV=development ${IMAGE}
test: build
	docker run ${IMAGE} nosetests --with-spec --spec-color
