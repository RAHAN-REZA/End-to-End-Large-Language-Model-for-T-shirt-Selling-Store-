from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
import os
from few_shots import few_shots
from urllib.parse import quote

from dotenv import load_dotenv
load_dotenv()


def get_few_shot_db_chain():
    llm= GooglePalm(google_api_key= os.environ["GOOGLE_API_KEY"], temperature= 0.1)
    db_user = 'root'
    db_password = 'FarHan@07'
    db_host = 'localhost'
    db_name = 'atliq_tshirts'
    encoded_password = quote(db_password)
    # Construct the URI with the encoded password
    db_uri = f'mysql+pymysql://{db_user}:{encoded_password}@{db_host}/{db_name}'
    db = SQLDatabase.from_uri(db_uri, sample_rows_in_table_info=3)





    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    to_vectorize=["  ".join(example.values()) for example in few_shots]
    vectorstore=Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(
    vectorstore=vectorstore,
    k=2,
    )

    example_prompt=PromptTemplate(
        input_variables=["Question","SQLQuery","SQLResult","Answer",],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",)


    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
        )

    new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return new_chain

if __name__ == "__main__":
    new_chain = get_few_shot_db_chain()
    print(new_chain.run("How many total t shirts are left in total in stock"))
    print(new_chain.run("how much is the price of all extra large size t-shirts?"))