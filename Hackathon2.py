import hashlib
class Word:
    def __init__(self,word,capacity):
        self.word=word
        self.capacity=capacity

class HashTable:

    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[]
        for i in range(capacity):
            self.table.append(None)

    def hashCode(self,word):
        idx=int(hashlib.sha256(word.encode("utf-8")).hexdigest(),16)%self.capacity
        return idx

    def put(self,data):
        idx=self.hashCode(data)
        if self.table[idx]==None:
            self.size+=1
        else:
            print("Data is Colliding")


        self.table[idx]=data
        print("Data is inserted {} at {} index".format(data,idx))

    def find(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            return idx
        else:
            return -1



review1="Really good institution teachers are very helpful and caring also environment of this college is very attractive.proud to be part of this college"
review2="Best institution Education level is high"
review3="What so ever I am today is due to this Technology temple"
review4="Nice place a big also it provides you good education"
review5="Great institution with opportunities for those who want it"

