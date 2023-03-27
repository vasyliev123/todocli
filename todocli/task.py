import datetime
class Task():

    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"
        self.created_at = str(datetime.datetime.now())

    def __str__(self):
        return f"{self.description} {self.due_date} {self.status}"
    
    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "created_at": self.created_at
        }

    def mark_as_complete(self):
        self.status = "Complete"

    def mark_as_incomplete(self):
        self.status = "Incomplete"