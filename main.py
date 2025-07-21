from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, feedback, menu, orders, subscriptions, tenants

app = FastAPI(title="SnapGrub API", description="SnapGrub API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="api/auth", tags=["Auth"])
app.include_router(feedback.router, prefix="api/feedback", tags=["Feedback"])
app.include_router(menu.router, prefix="api/menu", tags=["Menu"])
app.include_router(orders.router, prefix="api/orders", tags=["Orders"])
app.include_router(subscriptions.router, prefix="api/subscriptions", tags=["Subscriptions"])
app.include_router(tenants.router, prefix="api/tenants", tags=["Tenants"])
