FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /project
WORKDIR /project
COPY requirements.txt /project
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /project
EXPOSE 5000
CMD [ "python", "api.py" ]