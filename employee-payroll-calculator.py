name=input('Name:')
hourlyrate=float(input('Hourly rate:'))
hoursworked=int(input('Hours worked:'))
np=40*hourlyrate
it=hoursworked-40
ot= hourlyrate*1.5
bt=ot*it
if hoursworked>40:
    grosspay=np+bt
else:
    grosspay=hoursworked * hourlyrate
tax= grosspay*10/100
net=grosspay-tax
print(f'Name:{name}')
print(f'Hourly rate:{hourlyrate}')
print(f'Hours worked:{hoursworked}')
print(f'Grosspay:{grosspay}')
print(f'Tax:{tax}')
print(f'Net pay:{net}')
