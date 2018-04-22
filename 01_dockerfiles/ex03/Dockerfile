FROM debian:sid

RUN apt-get update && \
	apt-get install -y curl openssh-sever ca-certificates &&\
	git golang-go sqlite libsqlite3-dev openssl openssh-server -y && \
	mkdir -p /root/go/src/gitlab.com/gitlab && \
	cd /root/go/src/gitlab.com/gitlab && \
	git clone --recurse-submodules -b develop https://gitlab.com/gitlab-org/gitlab-ce && \
	cd gitlab-ce

	EXTERNAL_URL="http://gitlab.example.com" apt-get install gitlab-ee

ENV USER="root"
WORKDIR /root/go/src/github.com/gogits/gogs



