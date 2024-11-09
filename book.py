book={"py":452,"c":5,"java":890}
ch=1
while(ch!=5):
    print("1.add\n2.sell\n3.display\n4.sort")
    ch=int(input("choice:"))

    if(ch==1):
        name=input("name:")
        count=int(input("count:"))
        key=book.keys()
        for i in key:
            if name==i:
                book[i]=book[i]+count
                break
        else:
            book[name]=count
    elif(ch==2):
        name=input("name:")
        count=int(input("count:"))
        key=book.keys()
        for i in key:
            if name==i:
              if count<=book[i]:

                    book[i]=book[i]-count
                    break
              else:
                    print("not sufficient")
                    break
        else:
            print("no book")
    elif(ch==3):
        print(book)
    elif(ch==4):
        for i in book.items():

              print(i[0],":",i[1])