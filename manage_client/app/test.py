from decouple import config
from datetime import datetime, timedelta, timezone

secret_key = config('SECRET_KEY')

print(secret_key)

print(datetime.now(timezone.utc))
print(timedelta(minutes=7))

x = datetime.now(timezone.utc) + timedelta(minutes=10)

print(x)