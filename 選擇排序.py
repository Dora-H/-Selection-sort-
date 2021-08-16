box = [16, 25, 39, 27, 12, 8, 45, 63]
layers = len(box)
print('鞋櫃總共的層數:', layers)
print('好奇的打開鞋櫃，裡面尺寸好亂:', box, '\n')

for shoes in range(layers):
    size = box[shoes]
    for shoes_c in range(shoes+1,layers):
        if box[shoes_c] < box[shoes]:
            box[shoes], box[shoes_c] = box[shoes_c], box[shoes]
            size = box[shoes_c]
    print('第%d次打開鞋櫃%s' % (shoes+1, box) )
print('最後排好的鞋櫃:', box)
