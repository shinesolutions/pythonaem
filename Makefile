all: deps clean install test test-integration doc
ci: deps clean install test doc

deps:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

clean:
	echo "TODO"

install:
	python setup.py install

lint:
	pylint --rcfile=.pylintrc pythonaem test

test:
	nose2 test

test-integration: install
	nose2 test/integration

doc:
	sphinx-apidoc -o ../../doc/api/master/ --full -H "Python AEM" -A "Shine Solutions" pythonaem
	cd ../../doc/python/master/stage/ && \
	make html && \
	cd .. && \
	cp -R stage/_build/html/* ./ && \
	rm -rf stage/

doc-publish:
	gh-pages --dist doc/

publish:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi

publish-test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

tools:
	npm install -g gh-pages

.PHONY: all ci deps clean build install lint test test-integration doc doc-publish publish publish-test tools
