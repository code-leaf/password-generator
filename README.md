# Password Generator（Python）

`secrets` モジュールと `secrets.SystemRandom()` を使って、**推測されにくい（暗号学的に安全な）パスワード**を生成するCLIツールです。  
生成したパスワードは、自動的にクリップボードへコピーされます。

---

## プロジェクト構成

```text
password-generator/
  ├── generator.py        # パスワード生成のメインスクリプト
  ├── requirements.txt    # 必要なPythonライブラリ
  ├── scripts/
  │   ├── windows/        # Windows用バッチファイル（.bat）
  │   ├── mac/            # Mac用ダブルクリック実行ファイル（.command）
  │   └── linux/          # Linux用シェルスクリプト（.sh）
  └── README.md
```

---

## インストール方法

Python 3.x がインストールされている前提です。

### インストール手順

1. **プロジェクトルートに移動**

   ```bash
   cd password-generator
   ```

2. **仮想環境の作成とアクティベート (任意)**
   - **Linux/Macの場合**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - **Windowsの場合 (コマンドプロンプト)**

     ```bash
     python3 -m venv .venv
     .venv\Scripts\activate
     ```

   - **Windowsの場合 (PowerShell)**

     ```bash
     python3 -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

3. **依存ライブラリのインストール**

   ```bash
   pip install -r requirements.txt
   ```

---

## 使い方 (generator.py)

このツールは、コマンドラインから `generator.py` を直接実行して使用します。  
必要に応じて、先に仮想環境をアクティベートしてください。

### 基本的な使い方

1. **プロジェクトルートへの移動**

   ```bash
   cd password-generator
   ```

2. **仮想環境のアクティベート (任意)**
   - **Linux/Mac:** `source .venv/bin/activate`
   - **Windows (CMD):** `.venv\Scripts\activate`
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`

3. **パスワードの生成**

   以下のコマンドでパスワードを生成します。生成されたパスワードはコンソールに表示され、自動的にクリップボードにコピーされます。
   - **デフォルト (12文字, 記号あり)**

     ```bash
     python3 generator.py
     ```

   - **長さ指定 (例: 16文字)**

     ```bash
     python3 generator.py --length 16
     ```

   - **記号なし**

     ```bash
     python3 generator.py --no-symbols
     ```

   - **安全な記号 (`-` と `_`) のみ**

     ```bash
     python3 generator.py --safe-symbols
     ```

   - **特定の文字種を含まない**

     ```bash
     # 数字を含まない
     python3 generator.py --no-digits
     # 大文字を含まない
     python3 generator.py --no-upper
     # 小文字を含まない
     python3 generator.py --no-lower
     ```

### 主なオプション

| オプション       | 説明                                      | デフォルト値 |
| ---------------- | ----------------------------------------- | ------------ |
| `--length N`     | パスワードの長さを `N` 文字に指定します。 | `12`         |
| `--no-symbols`   | 記号を含まないようにします。              | `False`      |
| `--safe-symbols` | 記号を `-` と `_` のみに限定します。      | `False`      |
| `--no-digits`    | 数字を含まないようにします。              | `False`      |
| `--no-upper`     | 大文字を含まないようにします。            | `False`      |
| `--no-lower`     | 小文字を含まないようにします。            | `False`      |

**組み合わせの例:**

- **16文字で、安全な記号のみを含むパスワード**

  ```bash
  python3 generator.py --length 16 --safe-symbols
  ```

- **10文字で、記号を含まないパスワード**

  ```bash
  python3 generator.py --length 10 --no-symbols
  ```

---

## 使い方（Windows）

Windows では、`scripts/windows/` 内の `.bat` ファイルを実行するだけで、よく使うパターンのパスワードを簡単に生成できます。

- `scripts/windows/gen_std.bat` : 12文字 / 記号ふくむ
- `scripts/windows/gen_safe.bat` : 12文字 / 記号は「-\_」のみ
- `scripts/windows/gen_alphanum.bat` : 10文字 / 記号なし
- `scripts/windows/gen_minimal.bat` : 8文字 / 記号なし
- `scripts/windows/gen_strong.bat` : 16文字 / 記号ふくむ

各バッチファイルは、実行後に自動的にパスワードを生成し、結果を表示したあと **5秒待ってからウィンドウを閉じます**。

---

## 使い方（Mac）

Mac では、`scripts/mac/` 内の `.command` ファイルを **ダブルクリック**するだけでOKです。  
内部的には対応するLinux用 `.sh` をターミナルから実行します。

例:

- `scripts/mac/gen_std.command` : 12文字 / 記号ふくむ
- `scripts/mac/gen_safe.command` : 12文字 / 記号は「-\_」のみ
- `scripts/mac/gen_alphanum.command` : 10文字 / 記号なし
- `scripts/mac/gen_minimal.command` : 8文字 / 記号なし
- `scripts/mac/gen_strong.command` : 16文字 / 記号ふくむ

初回のみ、Gatekeeperの警告が出る場合があります。その際は  
「システム設定 > プライバシーとセキュリティ」から実行を許可してください。

---

## 使い方（Linux）

Linux では、`scripts/linux/` 内の `.sh` ファイルを使います。
最初に一度だけ、実行権限を付与してください。

1. **プロジェクトルートに移動 (一度行えば不要)**

   ```bash
   cd password-generator
   ```

2. **実行権限の付与 (初回のみ必要)**

   ```bash
   chmod +x scripts/linux/*.sh
   ```

3. **パスワード生成スクリプトの実行**

   必要に応じて仮想環境をアクティベートしてから、各スクリプトを実行してください。
   - **仮想環境のアクティベート (必要に応じて)**

     ```bash
     source .venv/bin/activate
     ```

   - **通常のパスワード生成 (12文字、記号含む)**

     ```bash
     ./scripts/linux/gen_std.sh
     ```

   - **安全な記号 (`-`と`_`) のみを含むパスワード生成 (12文字)**

     ```bash
     ./scripts/linux/gen_safe.sh
     ```

   - **英数字のみのパスワード生成 (10文字)**

     ```bash
     ./scripts/linux/gen_alphanum.sh
     ```

   - **最小限のパスワード生成 (8文字、英数字のみ)**

     ```bash
     ./scripts/linux/gen_minimal.sh
     ```

   - **強力なパスワード生成 (16文字、記号含む)**

     ```bash
     ./scripts/linux/gen_strong.sh
     ```

各スクリプトは、パスワードを表示したあと **「Press enter to continue...」と表示して一時停止**します。  
Enterキーを押すと終了します。

---

## 機能紹介

- **暗号学的に安全な乱数生成**
  - Python標準ライブラリの `secrets` と `secrets.SystemRandom()` を利用し、  
    パスワードやトークン用途に適した乱数を生成します。

- **柔軟な文字種の指定**
  - 英大文字 / 英小文字 / 数字 / 記号のON/OFF切り替え
  - 記号を「-\_」のみに制限できる `--safe-symbols` オプション

- **クリップボードへの自動コピー**
  - 生成したパスワードは `pyperclip` により自動的にクリップボードへコピーされます。
  - 成功時は「コピーしました」とコンソールに表示されます。
  - Linux など、環境によってはコピーに失敗することがあるため、  
    その場合でもパスワード表示は行い、エラーメッセージのみ表示します。
