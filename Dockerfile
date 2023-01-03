FROM python:3.10

ARG PROJECT
WORKDIR /opt/${PROJECT}

COPY ./ /opt/${PROJECT}

RUN make install

COPY docker-config/bashrc /root/.bashrc
COPY ./docker-config/entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
