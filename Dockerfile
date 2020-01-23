FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY requirements.txt /requirements/requirements.txt
COPY . /code/
WORKDIR /code/todoberry
RUN python3 -m pip install -U pip && python -m pip install --no-cache-dir  -r /requirements/requirements.txt

EXPOSE 7000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7000"]
