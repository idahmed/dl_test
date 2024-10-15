# pytest in docker playwright container
bash:
	docker-compose exec playwright bash
rm:
	docker-compose down && docker-compose rm -f
up:
	docker-compose up -d
down:
	docker-compose down
test:
	docker-compose run --rm playwright pytest -v