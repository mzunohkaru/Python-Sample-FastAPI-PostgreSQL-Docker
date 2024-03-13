from typing import Optional

from pydantic import BaseModel, Field

# BaseModel : FastAPIのスキーマモデル
class TaskBase(BaseModel):
    # Field : フィールドに関する付加情報
    title: Optional[str] = Field(None, example="Task Title")


class TaskCreate(TaskBase):
    # idはDBで自動的に採番し、doneフィールドはデフォルトでFalseが入るため
    # Postのリクエストボディは、titleだけで良い。よって、TaskBaseを継承する
    
    # pass : 「何もしない」 or 「実装予定」
    pass

# TaskCreate のレスポンス型の定義
class TaskCreateResponse(TaskCreate):
    # TaskCreate (title)と id だけのレスポンス型
    id: int

    # ORMを受け取り、レスポンススキーマに変換することを意味します
    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ") # False をデフォルト値に取っている

    class Config:
        orm_mode = True