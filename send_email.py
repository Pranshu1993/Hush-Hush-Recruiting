from utils import create_collection, read_records
import smtplib
from time import sleep
import pandas as pd


def send_email(from_addr, to_addr,
               subject, message,
               login, password,
               smtpserver='smtp.gmail.com:587'):
    header = f'From: {from_addr}'
    header += f"\r\nTo: {to_addr}"
    header += f'\r\nSubject: {subject}\r\n'
    message = header + message

    print(header)

    try:
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(login, password)
        server.sendmail(from_addr, to_addr, message)
        server.quit()
        print(f'Email sent sucessfully to {to_addr}\n\n')
    except Exception as e:
        print(f'Error sending in the email to {to_addr}')
        print(e)


# Sender information
login = 'bigdataprogrammingteam1@gmail.com'
password = 'Bdba.2102'
fromaddr = 'bigdataprogrammingteam1@gmail.com'
subject = 'Doodle Job opportunity'

# Retrieving the scandidates from our database and creating a dataframe
selected_candidates = create_collection('Selected_candidates')
candidates = [candidate for candidate in read_records(selected_candidates)]
df = pd.DataFrame(candidates)
df = df.set_index('_id')

# Other information
interface_link = 'http://127.0.0.1:5000/login'
doodle_hiring_manager = 'Ashish Chouhan'

# Send the emails
for index, row in df.iterrows():
    # Personalized message
    name = str(row['display_name'].encode("utf-8")).split("\'")[1]
    message = (f'Dear {name},\n\nYou have been '
               'selected to an interview for a developer position at Doodle. '
               'If interested please take our questionaire available in the '
               'link below. You will be given 3 coding questions that you '
               'have to finish in 30 minutes. Once the time expires the '
               'answers will be submitted automatically.\nYour results will '
               'be reviewed by our team and you will receive an email with '
               'further instructions.\n\n'
               f'Link to the coding interview: {interface_link}')
    message += (f'\n\nBest Regards,\n{doodle_hiring_manager}\n'
                'Doodle hiring manager')

    # Send email
    send_email(fromaddr, row['email'], subject, message, login, password)

    # Sleep between emails to avoid being listed as spam
    sleep(5)
