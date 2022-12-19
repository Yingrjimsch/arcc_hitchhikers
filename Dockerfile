FROM python:3-slim

ADD arcdata/* /
ADD * .

RUN pip install numpy
RUN pip install matplotlib

CMD ["python", "./main.py"]