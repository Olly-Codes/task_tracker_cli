class Task():
    def __init__(self, id, description, createdAt, updatedAt, status):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt