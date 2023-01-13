from fastapi import APIRouter

example_router = APIRouter()


@example_router.get("")
async def example_func(name: str):
    return {'response': {'200'},
            'message': f'selam {name}'}
