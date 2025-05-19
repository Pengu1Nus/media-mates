build:
	docker compose build
up:
	docker compose up
down:
	docker compose down
run:
	docker compose run --rm backend sh -c 'ls'
