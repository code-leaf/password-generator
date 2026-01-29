# Password Generator（Python）

`secrets` モジュールを使って、**推測されにくい**（暗号学的に安全な）パスワードを生成するCLIツールです。

## 使い方

作業ディレクトリ:

```bash
cd "password-generator"
```

デフォルト（12文字、英大文字/小文字/数字/記号すべてON）:

```bash
python3 generator.py
```

長さを指定:

```bash
python3 generator.py --length 20
```

含める文字種をOFFにする例:

```bash
python3 generator.py --no-symbols
python3 generator.py --no-upper --no-digits
```

ヘルプ:

```bash
python3 generator.py -h
```

## 初心者向け解説

### なぜ `secrets` が重要？

- `random` は「ゲーム・シミュレーション」などに向く乱数で、**パスワードやトークン生成には不向き**です（攻撃者に推測される可能性が上がります）。
- `secrets` は OS が提供する **CSPRNG（暗号学的に安全な疑似乱数生成器）** を利用します。  
  そのため、パスワードのように「推測されにくさ」が最重要の用途では `secrets` を使います。

このツールでは `secrets.choice(...)` で文字を選び、`secrets.SystemRandom().shuffle(...)` で並び順も安全にシャッフルしています。

### CLI引数（`argparse`）の扱い方

- `argparse` は `--length 20` のような **オプション引数** を簡単に扱えます。
- `--no-symbols` のような **フラグ** も定義でき、実行時に機能をON/OFFできます。

実際の引数定義は `generator.py` の `build_parser()` を参照してください。
