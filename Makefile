install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

check:
	poetry check

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

gendiff:
	poetry run gendiff

compare:
	poetry run gendiff ./files_to_compare/file1.json ./files_to_compare/file2.json
