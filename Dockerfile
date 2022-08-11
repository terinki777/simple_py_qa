FROM python:3.6-alpine

#building
RUN apk add --no-cache netcat-openbsd
WORKDIR /usr/src/x5
COPY . /usr/src/x5
RUN ["chmod", "+x", "/usr/src/x5/wait-for"]
RUN pip install -r requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/x5"

#running
CMD pytest ${PYTEST_ARGS}
