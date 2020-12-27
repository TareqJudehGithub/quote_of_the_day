# Challenge: Send an email on daily bases, containing a random quote from quotes.txt

import smtplib
import datetime as dt
from random import choice


def motivational_quote():
    # Obtain the current day of the week:
    date_time = dt.datetime.now()
    day_of_the_week = date_time.weekday()
    if day_of_the_week == 0:
        # convert quotes.txt to a list:
        with open("quotes.txt") as file:
            quotes_list = file.readlines()
            random_quote = choice(quotes_list)

        # Setup Email
        # Instantiate a new object from SMPT class:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # User Credentials:
            my_user = "tj.coder1975@gmail.com"
            my_pass = "BlueOcean75@"

            # Secure connection to Mail server:
            connection.starttls()

            # Log to Gmail:
            connection.login(user=my_user, password=my_pass)

            # Send an email:

            connection.sendmail(
                from_addr=my_user,
                to_addrs="tareq.joudeh@gmail.com",
                msg=f"Subject:Quote of the day\n\n{random_quote}".encode("utf8")
            )


motivational_quote()
