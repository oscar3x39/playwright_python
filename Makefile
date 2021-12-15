.PHONY: del up down tests

del:
	docker system prune -a

up:
	docker-compose up --d

down:
	docker-compose down

tests:
	docker-compose run tests