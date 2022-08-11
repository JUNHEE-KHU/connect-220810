def check_id(id) :
    if(id[6] == '-' and len(id) == 14) :
        for a in ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21'] :
            if(id.startswith(a)) :
                ans = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
                if(ans == 'o') :
                    if(id[7] == '3'):
                        pri = id[0]+id[1]+'년'+id[2]+id[3]+'월'+' '+'남자'
                        print(pri)
                    elif(id[7] == '4'):
                        pri = id[0]+id[1]+'년'+id[2]+id[3]+'월'+' '+'여자'
                        print(pri)
                    else:
                        print("잘 못된 번호입니다.\n올바른 번호를 넣어주세요")
                        return
        if(id[7] == '1'):
            pri = id[0]+id[1]+'년'+id[2]+id[3]+'월'+' '+'남자'
            print(pri)
        elif(id[7] == '2'):
            pri = id[0]+id[1]+'년'+id[2]+id[3]+'월'+' '+'여자'
            print(pri)
    else :
        print("잘 못된 번호입니다")

a = "500629-2222222"
check_id(a)
