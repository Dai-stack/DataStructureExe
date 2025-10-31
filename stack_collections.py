import collections

# deque デック スタックとキューをまとめてこういう
st = collections.deque()

print(st)

st.append(300)
st.append(200)
st.append(100)
st.append(500)
st.append(200)

print(st)

print("pop ->", st.pop())
print(st)

print("pop ->", st.pop())
print(st)
