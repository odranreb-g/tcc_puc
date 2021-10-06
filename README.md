# Project

## GraphModels

### How to use

Add follow code to Dockerfile

```bash
RUN apt-get update \
    && apt-get install -y --no-install-recommends graphviz \
    && rm -rf /var/lib/apt/lists/* \
    && poetry add pyparsing pydot
```

### How to conect to docker?

```bash
docker run --network host -it --entrypoint=bash deliveries_api:0.0.1
```

### How to generate?

1. Enter into container

```bash

```

2. Type the command

```bash
./<api>/manage.py graph_models -g -X TimeStampedModel -o my_project_visualized.png
```

### How to copy from container?

```bash
docker cp b278c7bffe49:/app/my_project_visualized.png
```
