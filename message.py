data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('We have read all the data, totally', len(data), 'files')

print(data[0])

wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('這個字沒有出現過喔')

print('感謝使用本功能')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('average length is', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('totally', len(new), 'files have less than 100 words')
print(new[0])



good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('totally', len(good), 'messages have good inside')
print(good[0])

good = [d for d in data if 'good' in d]
