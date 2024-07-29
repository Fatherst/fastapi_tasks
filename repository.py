from sqlalchemy import select

from database import TasksOrm, new_session
from schemas import STaskAdd, STask


class TaskRepository:

    @classmethod
    async def add_task(cls, task: STaskAdd)->int:
       async with new_session() as session:
           task_dict = task.model_dump()
           task = TasksOrm(**task_dict)
           session.add(task)
           await session.flush()
           await session.commit()
           return task.id

    @classmethod
    async def find_all(cls)->list[STask]:
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
