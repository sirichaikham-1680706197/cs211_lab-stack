class MyStack:
    def __init__(self, n):
        self.capacity = n              # ความจุสูงสุดของ stack
        self.arr = [0] * n             # อาร์เรย์สำหรับเก็บข้อมูล
        self.top = -1                  # ดัชนีของสมาชิกตัวบนสุด (-1 คือว่าง)

    def push(self, x):
        if self.isFull():
            return
        self.top += 1
        self.arr[self.top] = x


    def pop(self):
        if self.isEmpty():
            return
        self.top -= 1
        
    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity -1


# ---------- Driver code: ห้ามแก้ไขส่วนนี้ ----------
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1
    st = MyStack(n)
    out = []
    for _ in range(q):
        op = int(data[idx]); idx += 1
        if op == 1:
            x = int(data[idx]); idx += 1
            st.push(x)
        elif op == 2:
            st.pop()
        elif op == 3:
            out.append(str(st.peek()))
        elif op == 4:
            out.append("true" if st.isEmpty() else "false")
        elif op == 5:
            out.append("true" if st.isFull() else "false")
    print(" ".join(out))


if __name__ == "__main__":
    main()