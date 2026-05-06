FROM python:3.12-slim AS builder

WORKDIR /build

RUN pip install --upgrade pip

COPY pyproject.toml .

RUN --mount=type=cache,target=/root/.cache/pip \ 
    pip wheel --wheel-dir=/wheels -e .

FROM python:3.12-slim

RUN groupadd -r geomagnesis && \
    useradd -r -g geomagnesis -u 1000 -m -s /bin/bash geomagnesis

WORKDIR /geomagnesis

COPY pyproject.toml .

RUN --mount=type=bind,from=builder,source=/wheels,target=/wheels \
    pip install --no-index --find-links=/wheels --no-cache-dir -e .

COPY . .

RUN chown -R geomagnesis:geomagnesis /geomagnesis

COPY docker-entrypoint.sh .

RUN chmod +x docker-entrypoint.sh

USER geomagnesis

ENTRYPOINT [ "./docker-entrypoint.sh" ]