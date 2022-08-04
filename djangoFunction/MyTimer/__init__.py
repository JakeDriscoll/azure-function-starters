import logging
import string
import azure.functions as func
import random
from MyApp.models import TestTimeZones



def main(mytimer: func.TimerRequest) -> None:

    n = TestTimeZones()
    n.random_int = random.randint(1, 1000)
    letters = string.ascii_lowercase    
    n.name = ''.join(random.choice(letters) for i in range(10))
    n.save()
