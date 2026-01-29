#!/usr/bin/env python3
"""
パスワード生成ツール（CLI）

初心者向けメモ:
- `random` モジュールは「統計的な乱数」用途が中心で、暗号用途（パスワード・トークン等）には不向きです。
- `secrets` は OS が提供する暗号学的に安全な乱数源（CSPRNG）を使うため、
  「推測されにくい値」を生成したいときに必ず使います。
"""

from __future__ import annotations

import argparse
import secrets
import string


DEFAULT_LENGTH = 12


def build_parser() -> argparse.ArgumentParser:
    """
    CLI引数の扱い方（初心者向け）:
    - `argparse` を使うと `--length 16` のような「オプション引数」を簡単に受け取れます。
    - `--no-upper` のように「ON/OFF」を切り替えるフラグも作れます。
    """
    parser = argparse.ArgumentParser(
        description="secrets を使った安全なパスワード生成ツール",
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=DEFAULT_LENGTH,
        help=f"パスワード長（デフォルト: {DEFAULT_LENGTH}）",
    )

    # 既定はすべて有効。必要に応じて --no-xxx で無効化できます。
    parser.add_argument("--upper", dest="upper", action="store_true", default=True, help="英大文字を含める")
    parser.add_argument("--no-upper", dest="upper", action="store_false", help="英大文字を含めない")

    parser.add_argument("--lower", dest="lower", action="store_true", default=True, help="英小文字を含める")
    parser.add_argument("--no-lower", dest="lower", action="store_false", help="英小文字を含めない")

    parser.add_argument("--digits", dest="digits", action="store_true", default=True, help="数字を含める")
    parser.add_argument("--no-digits", dest="digits", action="store_false", help="数字を含めない")

    parser.add_argument("--symbols", dest="symbols", action="store_true", default=True, help="記号を含める")
    parser.add_argument("--no-symbols", dest="symbols", action="store_false", help="記号を含めない")

    return parser


def generate_password(length: int, *, upper: bool, lower: bool, digits: bool, symbols: bool) -> str:
    if length <= 0:
        raise ValueError("length は 1 以上にしてください。")

    charsets: list[str] = []
    if upper:
        charsets.append(string.ascii_uppercase)
    if lower:
        charsets.append(string.ascii_lowercase)
    if digits:
        charsets.append(string.digits)
    if symbols:
        # `string.punctuation` は一般的な記号セットです（空白は含みません）。
        charsets.append(string.punctuation)

    if not charsets:
        raise ValueError("少なくとも1種類（upper/lower/digits/symbols）を有効にしてください。")

    # 選択されたカテゴリを「必ず1文字以上含む」ようにする（よくある要件）。
    if length < len(charsets):
        raise ValueError(f"length が短すぎます（選択カテゴリ数: {len(charsets)}）。最低 {len(charsets)} にしてください。")

    # まず各カテゴリから1文字ずつ確保
    password_chars = [secrets.choice(cs) for cs in charsets]

    # 残りは全体プールから埋める
    pool = "".join(charsets)
    password_chars.extend(secrets.choice(pool) for _ in range(length - len(password_chars)))

    # 並びをシャッフル（secrets 由来の乱数で）
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        password = generate_password(
            args.length,
            upper=args.upper,
            lower=args.lower,
            digits=args.digits,
            symbols=args.symbols,
        )
    except ValueError as e:
        parser.error(str(e))
        return 2

    print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
