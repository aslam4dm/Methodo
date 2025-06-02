from datetime import datetime, timedelta

# Starting and ending dates
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 9, 1)

# Generate log filenames for the entire date range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime('%y%m%d')  # YYMMDD format
    print(f'C:\\inetpub\\logs\\LogFiles\\W3SVC1\\u_ex{date_str}.log')
    current_date += timedelta(days=1)
