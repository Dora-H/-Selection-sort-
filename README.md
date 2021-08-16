## 使用鞋櫃上有多少雙不同尺寸的鞋子，解說選擇排序法。
鞋櫃裡有不同尺寸的鞋子，沒有按照大小排列，請將亂掉的鞋櫃從第一層到最後一層依照尺寸小到大，依序排好。


### 鞋櫃(box)裡裝了八雙不同尺寸的鞋子，每一雙都代表一層
    box = [16, 25, 39, 27, 12, 8, 45, 63]
    
### 鞋櫃的層命名為數 :層數(layers)，len為length縮寫
    layers = len(box)
    print('鞋櫃總共的層數:', layers)
    print('好奇的打開鞋櫃，裡面尺寸好亂:', box, '\n')

### 按照最底層往上數，第一層為:0，依此類推，最後一層(第八層:7)
#### 打開第一層時第一雙鞋尺寸:16 ,在第一層:0
        for shoes in range(layers):
        # 尺寸 = 鞋櫃層裡的鞋子
        size = box[shoes]
        # 打開第一層後，假設往上層的鞋子命名為shoes_c，再來就以除了開過的鞋層剩餘做較，所以shoes+1
        for shoes_c in range(shoes+1,layers):
            # 如果往上層的鞋子尺寸 < 剛剛的
            if box[shoes_c] < box[shoes]:
                # 兩者位置互換
                box[shoes], box[shoes_c] = box[shoes_c], box[shoes]
                # 將這次打開看到的鞋子尺寸做為下一次依據的尺寸去做比較
                size = box[shoes_c]
        print('第%d次打開鞋櫃%s' % (shoes+1, box) )
    print('最後排好的鞋櫃:', box)
