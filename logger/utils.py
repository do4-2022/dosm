from datetime import datetime

def get_current_time():
  return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def get_current_date():
  return datetime.today().strftime('%Y-%m-%d')
