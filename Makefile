

help: ## Help Command
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:
	clear

install: clean ## Install game
	pip install .

unittests:  ## Runs all the unittests
	@cd game
	python -m unittest -v game.utils_test
	python -m unittest -v game.game_test
	@echo "\nComplete test:"
	python game/game.py
	@cd ..
