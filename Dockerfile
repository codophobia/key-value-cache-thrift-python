FROM python:3
MAINTAINER Shivam Mitra "shivamm389@gmail.com"
COPY gen-py /cache/gen-py
COPY src/lib /cache/src/lib
COPY src/server /cache/src/server
RUN pip install thrift
EXPOSE 9090
WORKDIR /cache
CMD ["python", "src/server/server.py"]
