from sys import argv

script_name, work_time, rate, bonus, *other = argv

payroll = (int(work_time) * int(rate)) + int(bonus)
print(payroll)
