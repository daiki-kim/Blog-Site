# Demo-Blog-Site

## 概要
以下の機能を含んだ簡単なブログサイトです。
- ユーザー登録
- ログイン、ログアウト機能
- ブログの閲覧
- ブログの投稿（ログイン時のみ）

## 技術スタック
- Python
- Django
- HTML
- SQLite

## 環境のセットアップ

### 仮想環境の作成

このプロジェクトはPythonの `venv` を使用して仮想環境を構築します。

仮想環境を作成するには、次のコマンドを実行してください：

```bash
python -m venv venv
```

そして、仮想環境をアクティベートします：

Windowsの場合：
```bash
venv\Scripts\activate
```

MacOS/Linuxの場合：
```bash
source venv/bin/activate
```

## インストール方法
- インストールコマンド:
```bash
pip install -r requirements.txt
```

## 使用方法
データベースのマイグレーションを作成して適用します：
```bash
python manage.py makemigrations
python manage.py migrate
```
プロジェクトディレクトリで以下のコマンドで実行します：
```bash
python manage.py runserver
```

## サイトの使い方
サイトにアクセスするとブログを閲覧できます。ユーザー登録をするとブログのポストができるようになります。
