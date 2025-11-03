class Mystack:

    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def display(self):
        print(self.data)

    def isEmpty(self):
        if len(self.data) == 0:
            # print("This stack is empty ")
            return True
        else:
            # print("This stack isNOT empty size ->", len(self.data))
            return False


# クラス定義ここまで
st = Mystack()

st.display()

st.push("K")
st.push("A")
st.push("W")
st.push("A")
st.push("I")
st.push("I")

st.display()
print("IsEmpty? ->", st.isEmpty())

print("pop->", st.pop())
print("pop->", st.pop())
print("pop->", st.pop())
print("pop->", st.pop())
print("pop->", st.pop())
print("pop->", st.pop())

st.display()


print("IsEmpty? ->", st.isEmpty())
