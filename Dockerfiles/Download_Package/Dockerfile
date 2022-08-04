FROM ubuntu:latest 

RUN apt-get update
RUN apt-get install -y wget gpg
RUN wget -O- https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor > signal-desktop-keyring.gpg
RUN cat signal-desktop-keyring.gpg | tee -a /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null
RUN echo deb [arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] https://updates.signal.org/desktop/apt xenial main | tee -a /etc/apt/sources.list.d/signal-xenial.list
RUN  apt update -y 
#RUN apt-get download signal-desktop

