FROM debian

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update -y && apt-get upgrade -y &&\
	apt-get install -y curl sudo openssh-server ca-certificates apt-utils apt-transport-https wget &&\
	mkdir -p /root/gitlab && \
	cd /root/gitlab

RUN apt-get install dialog -y

RUN sudo apt-get install -y postfix

RUN curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash

RUN sudo chown -R root:root /var

USER root

#RUN sudo cp /opt/gitlab/embedded/cookbooks/runit/files/default/gitlab-runsvdir.conf /etc/init/ &&\
#RUN	sudo initctl restart gitlab-runsvdir
#	sudo gitlab-ctl reconfigure  EXTERNAL_URL="http://192.168.99.100:3000" 
RUN sudo apt-get install -yq --no-install-recommends gitlab-ce

#RUN sudo initctl restart gitlab-runsvdir

RUN sudo cp /opt/gitlab/embedded/cookbooks/runit/files/default/gitlab-runsvdir.conf /etc/init/
RUN sudo initctl start gitlab-runsvdir
# RUN sudo gitlab-ctl reconfigure # Resume gitlab-ctl reconfigure
RUN EXTERNAL_URL="http://192.168.99.100:3000" apt-get install -yq --no-install-recommends gitlab-ce


ENV USER="root"
WORKDIR /root/gitlab



