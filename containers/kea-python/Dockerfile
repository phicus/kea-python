ARG KEA_VERSION=2.6.0

FROM kea-dev:$KEA_VERSION AS build

WORKDIR /source
COPY . .

# RUN make clean install \
#     && mkdir /dist \
#     && cd /usr/local \
#     && find lib -name \*.so\* | tar cf - -T - | (cd /dist; tar xf -) \
#     && tar cf - etc share/man bin sbin var | (cd /dist; tar xf -)

RUN autoreconf -i && \
    ./configure --prefix=/usr --libdir=${prefix}/lib/x86_64-linux-gnu --libexecdir=${prefix}/lib/x86_64-linux-gnu && \
    make install

# FROM ubuntu:21.04
# ENV DEBIAN_FRONTEND noninteractive

# RUN apt-get update -y \
#     && apt-get -y install \
#         procps \
#         socat \
#         python3 \
#         libpython3.9 \
#         liblog4cplus-2.0.5 \
#         libboost-system1.74.0 \
#         libffi8ubuntu1 \
#         libpq5 \
#         libmariadb3

# COPY --from=build /dist /usr/local

# RUN ldconfig


# podman build  -f ./containers/kea-python/Dockerfile --build-arg KEA_VERSION=2.6.0 -t kea-python:2.6.0 -t kea-python . && podman run -it kea-python bash
