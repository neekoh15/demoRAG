#from models.conversational.llama3_2 import Llama3_2
from models.vectors.chroma_client import ChromaHttp


if __name__ == "__main__":

    doc_retriever = ChromaHttp()
    #conversational_model = Llama3_2()

    # Dialogar con la base de datos:
    while True:

        query = input('insert query >>> ')

        documents = doc_retriever.retrieve_documents(query)
        print("Documents: ", documents, '\n\n')

        #model_answer = conversational_model.answer(query, documents)
        #print("Model answer: ", model_answer, '\n\n')