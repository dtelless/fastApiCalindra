from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import uvicorn
import tools

app = FastAPI()


class Address(BaseModel):
    address: str


class Adresses(BaseModel):
    adresses: List[Address]


@app.post('/adresses')
async def say_desafio(adresses: Adresses):
    if len(adresses.adresses) >= 3:
        results = tools.get_geocodes(adresses)
        results = tools.get_distances(results)

        if len(results['distances']) < 3:
            raise HTTPException(status_code=418, detail="Nope! I don't like less than 3 results.")

        results = tools.set_nearest_farest(results)

    else:
        raise HTTPException(status_code=418, detail="Nope! I don't like less than 3 arguments.")

    return {
        "status": "SUCCESS",
        "data": results
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
