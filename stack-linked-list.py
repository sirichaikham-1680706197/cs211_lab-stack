class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None   # โหนดบนสุดของ stack
        self.count = 0     # จำนวนสมาชิกใน stack

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.count -= 1


    def peek(self):
        if self.head is None:
            return -1
        return self.head.data

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.count


# ---------- Driver code: ห้ามแก้ไขส่วนนี้ ----------
import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    q = int(data[idx]); idx += 1
    st = MyStack()
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
            out.append(str(st.size()))
    print(" ".join(out))


if __name__ == "__main__":
    main()