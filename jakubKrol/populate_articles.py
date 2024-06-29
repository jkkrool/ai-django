from faker import Faker
import random
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jakubKrol.settings")

import django
django.setup()

from django.core.management import call_command

from jakubKrol_zaliczenie.models import Article


def populate(N=100):  # N określa liczbę rekordów do stworzenia
    fake = Faker()

    for _ in range(N):
        title = fake.sentence(nb_words=6)
        description = fake.text(max_nb_chars=2000)
        body = fake.text(max_nb_chars=2000)
        date = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)
        author = fake.sentence(nb_words=5)
        year = random.randint(1990, 2023)
        image = fake.image_url(width=None, height=None)

        # Tworzenie nowego rekordu Article
        article = Article(title=title, description=description, body=body, date=date, author=author, year=year, image=image)
        article.save()


if __name__ == '__main__':
    print("Populating the databases... Please Wait")
    populate(10)  # Wpisz liczbę artykułów, które chcesz wygenerować
    print('Populating Complete')
