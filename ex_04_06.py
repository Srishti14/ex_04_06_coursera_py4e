def computepay(h,r):
    if (h <= 40):
        return h * r
    if (h > 40):
        return 40 * r + (h - 40) * 1.5 * r

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per hour:")
r = float(rate)
pay = computepay(h,r)
print(pay)
