ACLOCAL_AMFLAGS = -I m4macros ${ACLOCAL_FLAGS}
# ^^^^^^^^ This has to be the first line and cannot come later in this
# Makefile.am due to some bork in some versions of autotools.

# We don't want to follow GNU file setup (no README, no AUTHORS, etc)
AUTOMAKE_OPTIONS = foreign

SUBDIRS = keahook keamodule

KEA_VESION ?= 2.4.1
CONTAINER_RUNTIME ?= $(if $(shell command -v podman ;),podman,docker)

.PHONY: build-kea-dev
build-kea-dev:
	$(CONTAINER_RUNTIME) build --build-arg KEA_VESION=$(KEA_VESION) -f DockerfileDev --tag kea-dev:$(KEA_VESION) .

.PHONY: build-kea
build-kea:
	$(CONTAINER_RUNTIME) build --build-arg KEA_VESION=$(KEA_VESION) --tag kea:$(KEA_VESION) .

.PHONY: build-dhtest
build-dhtest:
	cd dhtest && $(CONTAINER_RUNTIME) build --tag dhtest .

.PHONY: run-kea-dev
run-kea-dev: kea-network
	$(CONTAINER_RUNTIME) run --rm -it --network kea -e LANG=C.UTF-8 --privileged -v`pwd`:/workdir --name kea-dev kea-dev:$(KEA_VESION) bash

.PHONY: run-kea
run-kea: kea-network
	$(CONTAINER_RUNTIME) run --rm -it --network kea -e LANG=C.UTF-8 --privileged -v`pwd`:/workdir --name kea kea:$(KEA_VESION) bash

.PHONY: run-mysql
run-mysql: kea-network dhcpdb_create.mysql.sql
	$(CONTAINER_RUNTIME) run --rm --network kea \
		-e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=kea -e MYSQL_USER=kea -eMYSQL_PASSWORD=kea \
		--name mysql \
		-v `pwd`/dhcpdb_create.mysql.sql:/docker-entrypoint-initdb.d/dhcpdb_create.mysql.sql \
		mariadb

.PHONY: run-dhtest
run-dhtest: kea-network
	$(CONTAINER_RUNTIME) run --rm -it --network kea --privileged -v`pwd`:/workdir --name dhtest dhtest bash

.PHONY: kea-network
kea-network:
	$(CONTAINER_RUNTIME) network ls | grep -q kea || $(CONTAINER_RUNTIME) network create --subnet=172.28.5.0/24 --ip-range=172.28.5.0/24 kea

.PHONY: dhcpdb_create.mysql.sql
dhcpdb_create.mysql.sql:
	tar xz --strip-components 6 -f kea-$(KEA_VESION).tar.gz kea-$(KEA_VESION)/src/share/database/scripts/mysql/dhcpdb_create.mysql
	mv dhcpdb_create.mysql dhcpdb_create.mysql.sql