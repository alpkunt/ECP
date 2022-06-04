from datetime import datetime
from sqlalchemy.sql import func

print(func.now())


print(datetime.utcnow().timestamp())
print(datetime.date().)