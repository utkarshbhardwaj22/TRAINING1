def get_max(data, length):

    if length== 1:
        return data[0]
    else:
        num= get_max(data, length-1)

    if num > data[length-1]:
        return num
    else:
        return data[length-1]



def main():
    data=[10,20,30,40]
    max_num= get_max(data,len(data))
    print("Max number is:",max_num)

if __name__ == '__main__':
    main()


