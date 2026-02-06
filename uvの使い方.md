### 今後に向けての制約条件

- ライブラリは uv を統一的に利用すること。メリットは環境を汚さずに使えることです。
- ライブラリが必要な場合はインストール前に uv pip show でインストール済みか確認してください。
```
uv pip show numpy pandas
```

### uv の使い方

以下の順番で環境構築する

- 仮想環境の作成
```
uv venv --python 3.10
uv venv --python 3.11
uv venv --python 3.12
```

- 初期化
```
uv init
```

- パッケージ追加・削除
```
uv add numpy pandas
uv add -r requirements.txt
uv remove numpy

# 一時的な依存関係追加
uv run --with requests python -c "import requests"
```

- スクリプトやコマンドを仮想環境で実行
```
uv run hello.py
uv run TURSO_script.py
uv run pytest tests/
uv run ruff check
uv run python -c \"print('Hello from uv')\"

# ツール実行
uv run pytest tests/
uv run ruff check .
uv run black .
```

- プロジェクト環境でCLIツールやシェルスクリプトも実行可能
```
uv run bash scripts/foo.sh
uv run example-cli foo
```

- Python ver管理
```
uv python install 3.11	# Python 3.11 インストール
uv python list	        # インストール済み一覧
uv python pin 3.11	    # プロジェクトバージョン固定
```

### uv 利用時の注意事項

- OneDrive 等クラウド同期フォルダはハードリンクをサポートしていません。そのため、os error 396（incompatible hardlinks）となりインストールに失敗することがあります。
- 対処法として、ハードリンクではなくコピーを強制することで問題を回避できます。
- 常に --link-mode=copy を使用してください。
```
uv run --link-mode=copy script.py
または
set UV_LINK_MODE=copy && uv run python script.py
```

### ライブラリのインストール

$env:UV_LINK_MODE="copy"
echo $env:UV_LINK_MODE

```
uv add python-dotenv
uv add libsql==0.1.11
uv add rich
```
