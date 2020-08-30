## pytest

fixutureを使用する時のコメント例
```
def test_add_increase_count(db_with_3_task):
    # GIVEN a db with 3 tasks (dbにタスクが3つ含まれていれば)
    # WHEN another task is added (新しいタスクを追加したときに)
    tasks.add(Task('throw a party'))
    # THEN the count increases by 1 (countの値が1増える)
    assert tasks.count() == 4
```

#### GIVEN/WHEN/THENを使う理由
1. テストの可読性と管理しやすさ
2. フィクスチャでのERRORとテストでのFAILEDの切り分け


## ディレクトリ構成
```
.
├── Dockerfile
├── README.rst
├── poetry.lock
├── pyproject.toml
├── pytest_tdd_app
│   ├── __init__.py
│   └── api.py
└── tests
    ├── __init__.py
    ├── conftest.py
    ├── func
    │   ├── __init__.py
    │   └── test_api_execptions.py
    ├── test_pytest_tdd_app.py
    └── unit
        ├── __init__.py
        ├── test_fixture.py
        └── test_tasks.py
```