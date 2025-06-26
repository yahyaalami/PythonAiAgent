from dotenv import load_dotenv
import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv()


###print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
###print("SERPAPI_API_KEY", os.getenv("SERPAPI_API_KEY"))
embed_model = OpenAIEmbedding(api_key=os.getenv("OPENAI_API_KEY"))



def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        embed_model = OpenAIEmbedding(api_key=os.getenv("OPENAI_API_KEY"))
        index = VectorStoreIndex.from_documents(data, show_progress=True, embed_model=embed_model)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index




pdf_path = os.path.join("data", "Canada.pdf")
canada_pdf = PDFReader().load_data(file=pdf_path)
canada_index = get_index(canada_pdf, "canada")
canada_engine = canada_index.as_query_engine()
