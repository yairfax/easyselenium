reinstall: dist/
	pip uninstall -y easy-selenium-yairfax
	pip install dist/easy_selenium_yairfax-0.0.3-py3-none-any.whl
	
dist/: src/*.py setup.cfg
	python3 -m build

clean:
	rm -rf dist easy_selenium_yairfax.egg-info build

upload: dist/
	python3 -m twine upload --repository testpypi dist/*

test: reinstall
	python3 -m unittest -v tests.easyselenium_tests