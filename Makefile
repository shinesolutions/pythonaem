ci: clean deps lint test-unit package install

clean:
	rm -rf *.egg-info build dist htmlcov pythonaem/_pycache_/ pythonaem/*.pyc tests/_pycache_/ tests/*.pyc .coverage

deps:
	pip3 install --ignore-installed -r requirements.txt
	pip3 install --ignore-installed -r requirements-dev.txt

lint:
	pylint pythonaem/*.py pythonaem/*/*.py

test-unit:
	python3 -m unittest discover -s tests/unit/

test-integration:
	python3 -m unittest discover -s tests/integration/

coverage:
	coverage run --source=./pythonaem -m unittest discover
	coverage html
	coverage report --fail-under=100

package:
	python3 setup.py sdist bdist_wheel

install: package
	pip3 install dist/pythonaem-`yq -r .version conf/info.yaml`-py3-none-any.whl

# Since rtk only supports semver, we need to pre and post massage
# the version number in conf/info.yaml .
# Example: version 0.10.0rc0 needs to be pre-massaged to 0.10.0-rc0
# and then we let rtk to prepare the release version number as 0.11.0,
# and then rtk will prepare the next pre release version number which would be 0.11.0-rc0.0,
# so then we'll have to post-massage it to 0.11.0rc0 so that it is compatible
# with Python setuptools versioning scheme.
# This pre and post massage steps can be removed later when rtk
# supports Python setuptools versioning scheme.
release:
	sed -i '' -e 's/rc0/-rc0/' conf/info.yaml
	rtk release
	sed -i '' -e 's/-rc0.0/rc0/' conf/info.yaml
	git commit conf/info.yaml -m "Revert semver back to Python setuptools versioning scheme"

publish:
	python3 setup.py sdist
	twine upload dist/*

publish-test:
	python3 setup.py register -r pypitest && \
		python3 setup.py sdist upload -r pypitest

.PHONY: ci clean deps lint test-unit test-integration coverage package install release publish publish-test