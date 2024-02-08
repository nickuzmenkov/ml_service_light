# ML Service Light

Lightweight ML Service with Streamlit UI served in Docker container.

The model is a naive Logistic Regression iris classifier retrained every time the button is pressed. You can replace it with model of your choice.

## Usage

First, build the image:

```bash
docker build -t ml_service_light:latest .
```

Then run it with the following command:

```bash
docker run -p 8501:8501 ml_service_light:latest
```

You can also add `-d` flag to run it in detached mode.

## Authors

- Nick Kuzmenkov (@nickuzmenkov)
