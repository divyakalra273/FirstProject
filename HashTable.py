

class HashTable:

    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[]
        for i in range(capacity):
            self.table.append(None)

    def hashCode(self,data):
        idx = id(data) % self.capacity
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

    def delete(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            self.table[idx] == None
            self.size -= 1
            print("Data Deleted", data)
        else:
            print("Data Not Found", data)

def main():

    hashtable1=HashTable(15)
    hashtable1.put(20)
    hashtable1.put(15)
    hashtable1.put(25)
    hashtable1.put(40)


    print("~~~~~~~~~~~~")
    print(hashtable1.size)


if __name__== "__main__":
    main()






