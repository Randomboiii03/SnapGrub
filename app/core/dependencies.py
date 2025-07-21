from fastapi import Header, HTTPException

async def get_current_tenant(x_tenant_id: str = Header(...)):
    if not x_tenant_id:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"x_tenant_id": x_tenant_id}
