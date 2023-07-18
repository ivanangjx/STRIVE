FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-devel

RUN pip install --upgrade pip && pip install numpy==1.19.5
RUN ls
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
RUN pip uninstall -y opencv-python && pip install opencv-python-headless shapely==1.7.1

RUN rm /etc/apt/sources.list.d/cuda.list
RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-key del 7fa2af80
RUN apt-get update && apt-get install -y --no-install-recommends wget

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt update && apt install -y ffmpeg

RUN echo "export PATH=/usr/bin:$PATH" >> ~/.bashrc