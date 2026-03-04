from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
    
)
database_models.Base.metadata.create_all(bind=engine)
@app.get("/health")
def health():
    return {"status":"ok"}
@app.get("/")
def greet():
    return "Welcome Tesco"
products=[Product(id=1,name="Brown Bread",description="This is brown bread",price=99,quantity=10),
          Product(id=2,name="Basmati Rice",description="This is Basmati Rice",price=85,quantity=6),
          Product(id=3,name="Pasta",description="This is Pasta",price=89,quantity=4),
          Product(id=4,name="Dove Soap",description="This is Dove Soap",price=94,quantity=4),
          Product(id=5,name="Coco Cola",description="This is Coco Cola",price=82,quantity=5)]
def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()
def init_db():
    db=session()
    count=db.query(database_models.Product).count()
    if count==0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
    db.commit()
init_db()
@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products
@app.get("/products/{id}")
def get_product_id(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    return "Product Not Found"
@app.post("/products")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product
@app.put("/products/{id}")
def update_product(id:int,product: Product,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()
        return "Product Updated"
    else:
        return "No Product found"

@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product not found"

    
        
    
    
       
    
