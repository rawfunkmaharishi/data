FROM python:3.12

ARG PROJECT
WORKDIR /opt/${PROJECT}

COPY ./ /opt/${PROJECT}

RUN make install

COPY container-config/bashrc /root/.bashrc
COPY ./container-config/entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
