def main():
    num = 10
    count = 1
    stopat = 15

    while (count<=stopat):
        num += 9
         
        if Getsum(num) == 10:
            if count == stopat:
                print(f"| {count} | {num} |")
                break
            count+=1



def Getsum(num):
    num = str(num)
    sum = 0
    for i in num:
        sum += int(i)
    return sum

main()