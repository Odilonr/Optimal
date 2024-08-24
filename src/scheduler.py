import schedule
import time
from datetime import date, timedelta
from threading import Thread
from src.data.database_manager import database

def initialize_daily_records():
    to_day = date.today()
    yesterday = to_day - timedelta(1)
    athlete_ids = database.get_all_athlete_ids()
    
    if athlete_ids:

        for athlete_id in athlete_ids:
            if not database.daily_record_exists(athlete_id, to_day):
                current_records = database.get_current_daily_record(athlete_id=athlete_id, date=yesterday)
                weight = current_records[16]
                activity = current_records[17]
                phase = current_records[18]
                database.empty_daily_record(athlete_id=athlete_id, date=to_day, weight=weight, activity=activity,
                                            phase=phase)
    else:
        return

def run_scheduler():
    schedule.every().day.at("06:00:00").do(initialize_daily_records)
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    schedule_thread = Thread(target=run_scheduler)
    schedule_thread.daemon = True
    schedule_thread.start()