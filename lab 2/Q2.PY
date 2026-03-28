class Notification:
    def send_message(self):
        print("Sending generic notification...")


class EmailNotification(Notification):
    def send_message(self):
        print("Sending Email to user@example.com")


class SMSNotification(Notification):
    def send_message(self):
        print("Sending SMS to +923001234567")


# create objects
email = EmailNotification()
sms = SMSNotification()

email.send_message()
sms.send_message()