def check_digit(i):
    # คืนเลขตรวจสอบของเลข 12 หลักแรกของเลขบัตรประจำตัวประชำชน
    # n: สตริงเก็บเลขสิบสองหลักแรกของเลขบัตรประจำตัวประชำชน
    sum1 = 0
    for x in range(12):
      sum1 += (13-x) * int(i[x])
    return (11 - (sum1 % 11)) % 10

exec(input()) # DON'T remove this line
