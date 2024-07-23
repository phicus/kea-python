# SPDX-License-Identifier: MPL-2.0

ARG BASE_OS_VERSION=ubuntu-20.04
FROM mcr.microsoft.com/vscode/devcontainers/cpp:${BASE_OS_VERSION}

ARG PYTHON_VERSION=3.8
ARG KEA_VERSION=2.6.0

LABEL org.opencontainers.image.authors="Juan Gomez <jgomez@phicus.es>"

ENV DEBIAN_FRONTEND=noninteractive \
    BASE_OS_VERSION=${BASE_OS_VERSION} \
    PYTHON_VERSION=${PYTHON_VERSION} \
    KEA_VERSION=${KEA_VERSION}


RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
        software-properties-common \
        apt-transport-https \
        apt-utils \
        bash \
        ca-certificates \
        curl \
        gnupg \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && curl -1sLf "https://dl.cloudsmith.io/public/isc/kea-$(echo "${KEA_VERSION}" | cut -c1;)-$(echo "${KEA_VERSION}" | cut -c3;)/setup.deb.sh" | bash \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        autoconf \
        automake \
        autoconf-archive \
        libtool \
        libffi-dev \
        libboost-dev \
        libboost-system-dev \
        make \
        g++ \
        python${PYTHON_VERSION} \
        python${PYTHON_VERSION}-dev \
        python3-pip \
        isc-kea-dev \
        isc-kea-hooks \
        isc-kea-dhcp4 \
    # Clean up to reduce image size
    && apt-get clean \
    && rm -rf /etc/apt/sources.list.d/isc-kea-* /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${PYTHON_VERSION} 1
