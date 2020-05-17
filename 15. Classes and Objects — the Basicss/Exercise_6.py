"""
Create a new class, SMS_store. The class will instantiate SMS_store objects,
similar to an inbox or outbox on a cellphone:
my_inbox = SMS_store()
This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages).
Each message will be represented as a tuple:
(has_been_viewed, from_number, time_arrived, text_of_SMS)
The inbox object should provide these methods:
my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
  # Makes new SMS tuple, inserts it after other messages
  # in the store. When creating this message, its
  # has_been_viewed status is set False.
my_inbox.message_count()
  # Returns the number of sms messages in my_inbox
my_inbox.get_unread_indexes()
  # Returns list of indexes of all not-yet-viewed SMS messages
my_inbox.get_message(i)
  # Return (from_number, time_arrived, text_of_sms) for message[i]
  # Also change its state to "has been viewed".
  # If there is no message at position i, return None
my_inbox.delete(i)     # Delete the message at index i
my_inbox.clear()       # Delete all messages from inbox
Write the class, create a message store object, write tests for these methods, and implement the methods.
"""
# I copied, but I also think that I understand this now.
import time
class SMS_store:
    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, text_of_sms,read_status = False):
        number = str(from_number)
        time_received = time.strftime("%D %T")
        self.inbox.append([time_received, number, text_of_sms, read_status])

    def message_count(self):
        return "There are {0} messages in your Inbox".format(len(self.inbox))

    def get_unread_indexes(self):
        unread = []
        for index, message in enumerate(self.inbox):
            if False in message:
                unread.append(index)
        return "Unread Messages in:", unread

    def get_message(self, index):
        message = self.inbox[index]
        message[3] = "Read"
        return message[ : 3]

    def delete(self, index):
        del self.inbox[index]
        return "Deleted Message", index

    def clear(self):
        self.inbox = []
        return "Empty Inbox"

index = 0
my_inbox = SMS_store()
my_inbox.add_new_arrival("number", "time", "text")
my_inbox.message_count()
my_inbox.get_message(index)
my_inbox.delete(index)
my_inbox.clear()