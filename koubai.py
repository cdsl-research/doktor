def step_count(data):
    status = ""
    # 初期フラグを立てる
    # data[0] data[1]のどっちがおおきいか
    if data[0] < data[1]:
        status = "up"
    else:
        status = "down"

    last = data[0]
    count = 0
    for n in data[1:]:

        # 向きが逆になったときに歩数を+1する
        if status == "up" and n < last:
            count += 1
            status = "down"

        if status == "down" and n > last:
            count += 1
            status = "up"
        print("count", count, last, "->", n, status)
        last = n


# テスト
# dataのグラフをデータ化
data = [0.3, -0.2, 0.4, 0.1, 0.3, -0.1, 0.3, 0.35, 0.1, 0.2, -0.3, -0.1]
# data = [0.3, 0.4, 0.5, 0.1, 0.3, -0.1, 0.3, 0.35, 0.1, 0.2, -0.3, -0.1]
step_count(data)
