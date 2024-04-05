#---
# name: opencv
# group: core
# config: config.py
# depends: [cuda, cudnn, python, numpy]
# test: test.py
# notes: install OpenCV (with CUDA) from binaries built by `opencv_builder`
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG OPENCV_DEB
RUN mkdir /opencv
COPY OpenCV-4.5.0-aarch64.tar /opencv/OpenCV-4.5.0-aarch64.tar

COPY opencv_install.sh /opt/opencv_install.sh

# leave the installer script under /opt and patch it with the
# build args hardcoded in case it needs re-installed later
RUN /opt/opencv_install.sh
RUN echo 'export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1' >> ~/.bashrc
