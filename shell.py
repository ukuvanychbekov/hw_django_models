from credit.models import Client, Credit, Account
from django.utils import timezone
import random

Client.objects.all()
c1 = Client(name='Нурсултан Бердиев', citizenship='Кыргызстан', birth_year='1995-11-09', work_place='Codify',
            update_date=timezone.now())
c1.save()
c2 = Client(name='Адилет Асылбаев', citizenship='Кыргызстан', birth_year='1997-26-07', work_place='IPVES',
            update_date=timezone.now())
c2.save()

Account.objects.all()
def random_number():
    number = random.randint(1000000000000000, 9999999999999999)
    return number
a1=Account(number=random_number(), client=c1)
a1.save()
a2=Account(number=random_number(), client=c2)
a2.save()
a3=Account(number=random_number(), client=c1)
a3.save()
a4=Account(number=random_number(), client=c2)
a4.save()


Credit.objects.all()
cr1=Credit(sum=1000, account=a1)
cr1.save()
cr2=Credit(sum=2000, account=a1)
cr2.save()
cr3=Credit(sum=3000, account=a1)
cr3.save()
cr4=Credit(sum=4000, account=a1)
cr4.save()