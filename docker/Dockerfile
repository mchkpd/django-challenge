FROM python:3.7.3-stretch as build
ENV PYTHONUNBUFFERED=1 \
    PYROOT=/pyroot \
    PROJECT_DIR=/project/app

ENV PYTHONUSERBASE=$PYROOT \
    PATH=$PYROOT/bin:$PATH \
    PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/src \
    MYPYPATH=$PYTHONPATH:$PROJECT_DIR/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libxml2 \
        libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

RUN PIP_USER=1 pip install --upgrade pip'>=9.2<9.3' pip-tools'>=4.0<4.1'
WORKDIR $PROJECT_DIR
COPY requirements.txt $PROJECT_DIR/
RUN PIP_USER=1 pip-sync

FROM python:3.7.3-slim-stretch
ENV PYTHONUNBUFFERED=1 \
    PYROOT=/pyroot \
    PROJECT_DIR=/project/app

ENV PYTHONUSERBASE=$PYROOT \
    PATH=$PYROOT/bin:$PATH \
    PYTHONPATH=$PYTHONPATH:$PROJECT_DIR/src \
    MYPYPATH=$PYTHONPATH:$PROJECT_DIR/src


RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libxml2 \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system --gid 101 django \
    && useradd -m -g django django \
    && mkdir -p /project/media /project/static $PYROOT

COPY --from=build $PYROOT $PYROOT

WORKDIR $PROJECT_DIR

COPY . $PROJECT_DIR

RUN chown -R django: /project

USER django

# Can't use PROJECT_DIR env var in exec ENTRYPOINT
ENTRYPOINT ["/project/app/docker/entrypoint.sh"]
CMD ["uwsgi"]
EXPOSE 8000
