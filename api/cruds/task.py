from typing import List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(
    db: AsyncSession, task_create: task_schema.TaskCreate
) -> task_model.Task:
    # 引数として受け取ったスキーマをDBモデル (task_model) に変換
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
    # Result インスタンスはこの時点ではまだすべてのDBリクエストの結果を持ちません
    result: Result = await db.execute(
        # select : 必要なフィールドを指定
        select(
            task_model.Task.id,
            task_model.Task.title,
            # Done.idが存在する場合は done=True、存在しない場合は done=False
            task_model.Done.id.isnot(None).label("done"),
        ).outerjoin(task_model.Done)  # outerjoin : DoneテーブルとTaskテーブルを結合
    )
    # 初めてすべてのDBレコードを取得
    return result.all()


async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    # Result は select() で指定する要素が１つであってもtupleで返却されますので、tupleではなく値として取り出すためにはflatten処理が必要
    task: Optional[Tuple[task_model.Task]] = result.first()
    return (
        task[0] if task is not None else None
    )


async def update_task(
    db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()