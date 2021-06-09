coverage run --source=./src -m pytest tests/tests.py
coverage report -m
coverage html -d tests/html_report

# --skip-covered ommits modules 100% covered

# nosetests -v --with-coverage --cover-package=ocbauthencryption --cover-inclusive --cover-erase tests/
# nosetests -v --with-coverage --cover-package=associated_data_hash --cover-inclusive --cover-erase tests/
