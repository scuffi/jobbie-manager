from fastapi import APIRouter

from config import Endpoints

workspace_router = APIRouter()


@workspace_router.post(Endpoints.CREATE_WORKSPACE)
def create_workspace():
    ...


@workspace_router.get(Endpoints.GET_WORKSPACE)
def get_workspace():
    ...


@workspace_router.patch(Endpoints.UPDATE_WORKSPACE)
def update_workspace():
    ...


@workspace_router.delete(Endpoints.DELETE_WORKSPACE)
def delete_workspace():
    ...
