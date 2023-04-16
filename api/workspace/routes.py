from fastapi import APIRouter

workspace_router = APIRouter()


@workspace_router.post()
def create_workspace():
    ...


@workspace_router.get()
def get_workspace():
    ...


@workspace_router.patch()
def update_workspace():
    ...


@workspace_router.delete()
def delete_workspace():
    ...
