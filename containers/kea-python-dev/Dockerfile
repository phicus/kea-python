# SPDX-License-Identifier: MPL-2.0

FROM debian:bookworm-slim

LABEL org.opencontainers.image.authors="Juan Gomez <jgomez@phicus.es>"

ENV DEBIAN_FRONTEND=noninteractive

ARG VERSION=2.6.0

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
        apt-transport-https \
        bash \
        ca-certificates \
        curl \
        gnupg && \
    curl -1sLf "https://dl.cloudsmith.io/public/isc/kea-$(echo "${VERSION}" | cut -c1;)-$(echo "${VERSION}" | cut -c3;)/setup.deb.sh" | bash && \
    apt-get update && \
    apt-get install --no-install-recommends -y \
        autoconf \
        automake \
        autoconf-archive \
        libtool \
        libffi-dev \
        libboost-dev \
        libboost-system-dev \
        make \
        g++ \
        python-is-python3 \
        python3-dev \
        python3-setuptools \
        python3-pytest \
        isc-kea-dev \
        isc-kea-hooks \
        isc-kea-dhcp4 && \
    # Clean up to reduce image size
    apt-get clean && \
    rm -rf /etc/apt/sources.list.d/isc-kea-* /var/lib/apt/lists/* /tmp/* /var/tmp/*
