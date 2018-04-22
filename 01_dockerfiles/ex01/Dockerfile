FROM debian
ENV TS3SERVER_LICENSE=accept
RUN apt-get -y update && apt-get -y install bzip2 && apt-get -y install wget &&\
	wget http://dl.4players.de/ts/releases/3.1.1/teamspeak3-server_linux_amd64-3.1.1.tar.bz2 &&\
	tar xfvj teamspeak3-server_linux_amd64-3.1.1.tar.bz2
CMD ["sh", "teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]
