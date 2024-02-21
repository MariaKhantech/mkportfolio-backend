from fastapi import FastAPI, Query
from mangum import Mangum
import os.path
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,StorageContext,load_index_from_storage

app = FastAPI()


#----STEP4: create a function to create_index----#
def create_index():
    PERSIST_DIR = "./stored_data"
    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index



#---STEP5: create a function called 'chat' to get the response---#
def chat(index, question):
    chat_engine = index.as_chat_engine()
    response = chat_engine.chat(question)
    print(response)


@app.get("/chat")
def read_root():
    #--- call the create_index function---#
    index = create_index()
    chat(index, "How much python experiance does Maria Have?")
    
    return {"data": "Hello World"}


handler = Mangum(app)

