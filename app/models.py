from dataclasses import dataclass


class Actor(models.Model):

    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def str(self) -> str:
        return f"{self.first_name} {self.last_name}"
