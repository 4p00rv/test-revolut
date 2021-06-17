IMAGE=revolut-test
TAG=$(shell git rev-parse --short HEAD)
build:
	docker build --build-arg ENV=development -t ${IMAGE} .
upload-prod:
	docker build --build-arg ENV=production -t $(org)/${IMAGE}:$(TAG) .
	docker push $(org)/$(IMAGE):$(TAG)
	export TAG=$(TAG); envsubst < kube-deploy.yml.tpl > deployment.yml
dev: build
	docker run -p $(port):8080 -e ENV=development ${IMAGE}
test: build
	docker run -e ENV=testing ${IMAGE} nose2 tests
