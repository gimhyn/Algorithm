from datetime import datetime, timedelta

kst_now = datetime.utcnow() + timedelta(hours=9)
print(kst_now.strftime('%Y-%m-%d'))
