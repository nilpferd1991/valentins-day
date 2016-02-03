#!/usr/bin/env python3.4


def get_newest_tag():
    from git import Repo

    repo = Repo(".")
    tags = repo.tags
    sorted_tags = sorted(tags, key=lambda tag: tag.commit.count())
    newest_tag = sorted_tags[-1]

    return newest_tag.name


def get_http_from_tag(tag_name):
    import urllib.request

    with urllib.request.urlopen('http://www-ekp.physik.uni-karlsruhe.de/~nbraun/valentin/' + tag_name) as response:
           html = response.read()
           return html


def send_mail(body):
    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # me == my email address
    # you == recipient's email address
    me = "valentinedaycommit@googlemail.com"
    you = "area51.nils@googlemail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "You solved it!"
    msg['From'] = me
    msg['To'] = you

    # Record the MIME types of both parts - text/plain and text/html.
    email_text = MIMEText(body.decode(), 'html')

    # Attach parts into message container.
    msg.attach(email_text)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.googlemail.com')
    s.starttls()
    s.login("valentinedaycommit@gmail.com", "ValentinTagsCommit")
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, you, msg.as_string())
    s.quit()
    
if __name__ == "__main__":

    import unittest
    import os
    import sys

    all_test = unittest.defaultTestLoader.discover("")
    if unittest.TextTestRunner(verbosity=2).run(all_test).wasSuccessful():
        if os.getenv("CI", "false") == "true":
            newest_tag = get_newest_tag()
            html_site = get_http_from_tag(newest_tag)
            send_mail(html_site)

            sys.exit(0)
    else:
        sys.exit(1)
