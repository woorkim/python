"""
Adds the host to OBJECTNAME
"""
#OBJECTNAME = "/NetObjects/HostTrigger/Add To NetObject"
#class Trigger(HostTrigger):
#    def trigger(self):
#        obj = self.pldb.object_get(OBJECTNAME)
#        if obj is None:
#            print "Couldn't find object '%s'" % OBJECTNAME
#            return
#        self.pld.dyn_add(obj.id, self.ip)
#    def reset(self):
#        obj = self.pldb.object_get(OBJECTNAME)
#        if obj is None:
#            return
#        self.pld.dyn_remove(obj.id, self.ip)

print() #class =data type!!!
class Singer:                      # 가수를 정의하겠느니라…
    def sing(self):                # 노래하기 메서드
        return "Lalala~"
taeji = Singer()                   # 태지를 만들어랏!
taeji.sing()                       # 노래 한 곡 부탁해요~
ricky = Singer()
ricky.sing()

print()
class BusinessCard:
     def set_info(self, name, email, addr):
                self.name = name
                self.email = email
                self.addr = addr
     def print_info(self):
                print("--------------------")
                print("Name: ", self.name)
                print("E-mail: ", self.email)
                print("Address: ", self.addr)
                print("--------------------")
member1 = BusinessCard()
member1.set_info("YunaKim", "yuna.kim@naver.com", "Seoul")

#num = 1
#while num <= 100:
#     print(num)
#     num = num + 1

print()
#family = ['mother', 'father', 'gentleman', 'sexy lady']
#for x in family:        # family의 각 항목 x에 대하여:
#     print(x, len(x))    # x와 x의 길이를 출력하라.

#print()
#a = [4, 5, 6, 7]
#for i in a:
#     print(i)

print()
#for i in range(4, 8):
#    print(i)
power = 1
for expo in range(16):
    power *= 2
    print("2 to the power of", expo, "is", power)
   