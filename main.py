from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import pytz
import uvicorn

app = FastAPI()

# dummie petition to check response
@app.get("/")
async def root():
    return {"message": "Hello World"}


def time_log_job():
    try:
        utc_time = datetime.now()
        correction_factor = timedelta(hours= 5)
        col_time = utc_time - correction_factor

        with open('myTimeLog', 'a') as file:
            file.write(f'Hora UTC: {utc_time}\n')
            file.write(f'Hora COL: {col_time}\n')
        print("Se ha realizado el registro con exito")
    
    except Exception as e:
        print(f"Error al registrar la hora: {str(e)}")

#scheduler config
scheduler = BackgroundScheduler()
scheduler.add_job(func=time_log_job, trigger="interval", minutes=0.1)

scheduler.start()

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)