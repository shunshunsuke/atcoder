# 復習用メモ

|  問題  |  日付  |  結果  |  日付  |  結果  |  日付  |  結果  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|  ABC226_C  |  21/11/12  | ✕ |
|  ABC225_D  |  21/10/31  | ✕ | 21/11/27 | ◯ |
|  ABC222_D  |  21/10/30  | ✕ |
|  ABC182_D  |  21/10/17  | ✕ |
|  ABC154_D  |  21/10/9  | ✕ |
|  ABC165_D  |  21/10/8  | ✕ |
|  ABC221_D  |  21/10/2  | ✕ |
|  ABC217_D  |  21/9/4  | △ |

## ABC225
### D
- 双方向リスト

## ABC158
### D
- 先頭・末尾の要素をO(1)で追加・削除できる[deque](https://note.nkmk.me/python-collections-deque/) を利用した

## ABC222
### C
- [第1キーは昇順・第2キーは降順でソート](https://pashango-p.hatenadiary.org/entry/20090614/1244984058)

## ABC154
### D
- 期待値の線形性

## ABC181
### D
- [collections.Counter](https://www.headboost.jp/python-counter/) でリスト内それぞれの要素の個数が辞書形式で取得できる
- 演算子を使って集合演算も可能

## ABC217
### D
- listではTLEだったがarrayを利用することで回避できた
- 二分探索法のライブラリbisectがあることを知る

## 参考ページ
- [処理速度向上(ソート・ループ・リスト)](https://www.kumilog.net/entry/python-speed-comp)
- [リスト計算量](https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb)


## 競プロ典型90門
### 001 ✗ △
- 答えで二分探索

### 002 ✗ ○
- bit全探索
```python
import itertools

for A in itertools.product((0, 1), repeat=n):
```

### 003 ✗ ○
- 木の直径

### 007 ◯
- 二分探索
- bisectを使う

### 010 ✕ ○
- 累積和

### 012 △
- union find

### 014 ◯
- 貪欲法

### 016 ✕ ○
- 工夫した全探索

### 018 ✕
- 三角関数

### 020 ✕ ○
- 小数の誤差

### 22 △ ○
- 再帰関数
- ユークリッドの互除法

### 026 ✗ ○
- 二部グラフ
- DFS

### 28 ✗ ✗
- [いもす法](https://imoz.jp/algorithms/imos_method.html)

### 34 ✗ ○
- 単調性を利用した尺取法

### 38 △ ✗
- 最小公倍数
- ユークリッドの互除法

### 42 ✗
- 9の倍数の性質

### 43 ✗
- 01-BFS

### 44 ◯
- deque
- 見かけ上の変化をメモ

### 46 ✕ ✗
- 同じ意味のものをまとめて考える

### 52 ✕
- 因数分解

### 58 ✗
- まずは小さい数で考えてみる

### 63 ✗
- 変な制約に着目する

### 64 ✕
- 階差

### 69 ✕
- 繰り返し二乗法
- pythonはpow関数が使える

### 70 ✗
- 中央値が絶対値総和の最小となる
  - statistics.median()
