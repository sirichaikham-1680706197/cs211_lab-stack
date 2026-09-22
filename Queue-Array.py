class MyQueue:
    def __init__(self, n):
        self.capacity = n          # ความจุสูงสุดของคิว
        self.arr = [0] * n         # อาร์เรย์สำหรับเก็บข้อมูล
        self.front = 0             # ดัชนีของสมาชิกตัวหน้าสุด
        self.rear = -1             # ดัชนีของสมาชิกตัวท้ายสุด
        self.count = 0             # จำนวนสมาชิกในคิว

    def enqueue(self, x):
        if self.isFull():
           return
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return
        self.front = (self.front + 1) % self.capacity
        self.count -= 1

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity


# ---------- Driver code: ห้ามแก้ไขส่วนนี้ ----------
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    qu = MyQueue(n)
    out = []
    for _ in range(q):
        op = int(data[idx]); idx += 1
        if op == 1:
            x = int(data[idx]); idx += 1
            qu.enqueue(x)
        elif op == 2:
            qu.dequeue()
        elif op == 3:
            out.append(str(qu.getFront()))
        elif op == 4:
            out.append(str(qu.getRear()))
        elif op == 5:
            out.append("true" if qu.isEmpty() else "false")
        elif op == 6:
            out.append("true" if qu.isFull() else "false")
    print(" ".join(out))


if __name__ == "__main__":
    main()