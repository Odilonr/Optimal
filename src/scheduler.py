import schedule
import time
from datetime import date
from threading import Thread
from src.data.database_manager import database

def initialize_daily_records():
    today = date.today()
    athlete_ids = database.get_all_athlete_ids()

    for athlete_id in athlete_ids:
        if not database.daily_record_exists(athlete_id, today):
            database.empty_daily_record(athlete_id=athlete_id, date=today)

def run_scheduler():
    schedule.every().day.at("06:00:00").do(initialize_daily_records)
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    schedule_thread = Thread(target=run_scheduler)
    schedule_thread.daemon = True
    schedule_thread.start()