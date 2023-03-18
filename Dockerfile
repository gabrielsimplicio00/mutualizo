FROM python:3.11

ADD src .

RUN pip install -r requirements.txt

CMD ["uvicorn", "./src/main:app --reload"]