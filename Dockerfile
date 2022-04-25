FROM python:3.8
WORKDIR /data-profiling
ADD . /data-profiling/
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD python3 app.py