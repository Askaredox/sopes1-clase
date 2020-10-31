FROM python:3.8
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip3 install Flask
RUN pip3 install flask_cors
RUN pip3 install requests
RUN pip3 install flask_mysqldb
CMD python app.py