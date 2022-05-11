FROM python
WORKDIR /work
RUN pip3 install flask
RUN pip3 install pyvi
COPY . .

ENTRYPOINT [ "python3", "src/app.py" ]