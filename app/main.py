from fastapi import FastAPI
from app.views import actor_view, category_view, country_view, city_view, address_view,film_view, film_actor_view, film_category_view, film_text_view,inventory_view, language_view, store_view, payment_view, rental_view, staff_view, customer_view
from app.core.database import Base, engine

app = FastAPI(title="Grupo Colaborativo 04 - CRUD Sakila Rest API MVVC")

Base.metadata.create_all(bind=engine)

app.include_router(actor_view.router)
app.include_router(category_view.router)
app.include_router(country_view.router)
app.include_router(city_view.router)
app.include_router(address_view.router)
app.include_router(film_view.router)
app.include_router(film_actor_view.router)
app.include_router(film_category_view.router)
app.include_router(film_text_view.router)
app.include_router(inventory_view.router)
app.include_router(language_view.router)
app.include_router(store_view.router)
app.include_router(payment_view.router)
app.include_router(rental_view.router)
app.include_router(staff_view.router)
app.include_router(customer_view.router)




