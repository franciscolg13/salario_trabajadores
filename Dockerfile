FROM python:3.8
RUN pip install streamlit pandas matplotlib
COPY src/* /app/
#Cargar directorio de csv
COPY csv/employees.csv /app/csv/employees.csv 
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]