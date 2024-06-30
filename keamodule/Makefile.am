

EXTRA_DIST = setup.py

install: setup.py
	$(PYTHON) setup.py install

all-local: setup.py
	$(PYTHON) setup.py build

clean-local: setup.py
	-$(PYTHON) setup.py clean --all
	-find $(srcdir) \( -name "build" -o -name "dist" -o -name "*.pyc" \
		-o -name "*.egg-info" \) -exec rm -rf '{}' \+