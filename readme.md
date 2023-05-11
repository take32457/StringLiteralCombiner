# String Literal Combiner

## 概要

このプログラムは、入力ファイル内の連結された文字列リテラルを置換するPythonスクリプトです。

## 例

```python
print("Hel" +  "lo" + "W"+'or'+"ld!")
```

to:

```python
print("HelloWorld!")
```

## 必要条件

Python 3.x

## 使い方

以下のようにコマンドラインから実行します。

```
python string_combiner.py inputfile [-o outputfile] [-d]
```

### 引数

- `inputfile`：入力ファイルのパス
- `-o outputfile`：出力ファイルのパス（省略時は`inputfile.o`となります）
- `-d`：デバッグモードを有効にします
