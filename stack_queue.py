import queue

# スタック＝Lifoキュー

st = queue.LifoQueue(maxsize=64)

print("size->", st.qsize())

st.put(400)
st.put(300)
st.put(800)

print("size->", st.qsize())

print("pop->", st.get())
print("pop->", st.get())
print("size->", st.qsize())
