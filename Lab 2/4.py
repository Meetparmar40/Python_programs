from datetime import datetime

now = datetime.now()

# Format the date and time
formatted_date = now.strftime('%a %B %d %H:%M:%S IST %Y')

# Print the formatted date and time
print(formatted_date)

