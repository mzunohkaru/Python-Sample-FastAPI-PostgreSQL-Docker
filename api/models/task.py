from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    # テーブル名
    __tablename__ = "tasks"

    # カラム
    id = Column(Integer, primary_key=True)
    title = Column(String(1024))

    # TaskクラスとDoneクラスの間のリレーションシップを定義　 (TaskインスタンスからDoneインスタンスにアクセスできる)
    # back_populates : Task <-> Done の双方向リレーションシップを定義 (参照が可能になる)
    # cascade : Taskインスタンスが削除されたときに、関連するDoneインスタンスも削除される
    done = relationship("Done", back_populates="task", cascade="delete")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

    task = relationship("Task", back_populates="done")