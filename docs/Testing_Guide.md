# Testing Guide

## Run Full Pipeline

```bash
py -m scripts.run_full_pipeline
```

## Build Index Only

```bash
py -m scripts.build_index
```

## Run Demo Query

```bash
py -m scripts.run_demo_query
```

## Run Evaluation

```bash
py -m scripts.evaluate_project
```

Expected output:

```text
Retrieval Hit Rate: 100.00%
```

## Run API

```bash
py -m uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
py -m pytest tests
```
