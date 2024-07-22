install:
	poetry install

test:
	poetry run pytest

test_coverage:
	poetry run pytest --cov

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

compare-1-2:
	poetry run gendiff ./files_to_compare/file1.json ./files_to_compare/file2.json

compare-3-4:
	poetry run gendiff ./files_to_compare/file3.json ./files_to_compare/file4.json

compare-3-4-yml:
	poetry run gendiff ./files_to_compare/file3.yml ./files_to_compare/file4.yaml
