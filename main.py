import function.interest as it
import function.monthly_saving as ms
import function.exchange as ex
import function.deposit as dp
import function.withdraw as wd
import function.balance_status as bs

# 입급후 남은 잔액
balance = 0
amount = 0
result = dp.deposit(balance, amount)
print(result)

#출금 후 남은 잔액
balance = amount = 0
withdraws = wd.withdraw(balance,amount)
print(withdraws)

#환율 계산
exchange = 0
amount = exchange__rate = 0
exchange = ex.exchange_money(amount, exchange__rate)
print(exchange)

#이자 계산
interst = balance = rate = 0
interst = it.calculate_interest(balance, rate)
print(interst)

#월 저축액
saving = target = months = 0
saving = ms.monthly_saving(target,months)
print(months)

#잔액확인
result = 0
balance = 0
result = bs.balance_status(balance)



