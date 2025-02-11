
from fastapi import APIRouter,HTTPException
from models .todos import Todo
from config.database import collection_name
from schema.schemas import list_indivijual_serial
from bson import ObjectId

router = APIRouter()

@router.get("get_todo")
async def get_todo():
    todos= list_indivijual_serial(collection_name.find())
    return todos

@router.post("/add")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return {"message": "Todo added successfully"}

@router.put("/update/{id}")
async def update_todo(id: str, todo: Todo):
    result = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(todo)},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo updated successfully", "updated_todo": result}

    # 🔹 Delete Todo by ID
@router.delete("/delete/{id}")
async def delete_todo(id: str):
    result = collection_name.find_one_and_delete({"_id": ObjectId(id)})
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {"message": "Todo deleted successfully"}



