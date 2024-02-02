import threading
import time

class NumThread(threading.Thread):
    def __init__(self, count, chat_id, bot):
        threading.Thread.__init__(self)
        self.count = count
        self.chat_id = chat_id
        self.bot = bot

    def run(self):
        self.bot.send_message(self.chat_id, f"Counting started for {self.count} numbers:")
        for num in range(self.count + 1):
            time.sleep(1) 
            self.bot.send_message(self.chat_id, str(num))

        self.bot.send_message(self.chat_id, f"Counting completed for {self.count} numbers.")

