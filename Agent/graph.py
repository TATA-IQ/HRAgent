from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from  Agent.consts import RETRIEVE_LLAMA,RETRIEVE_MAXBAI,RETRIEVE_Recursive,  GRADE_DOCUMENTS, GENERATE_LLAMA, GENERATE_RECURSIVE, ENHANCE_QUERY
from Agent.nodes.retriver import StateRetrieveLLAMA, StateRetrieveMaxbai, StateRetrieveRecursive
from Agent.nodes.generation import generate_llama, generate_recursive 
from Agent.nodes.enhance_query import generate_query
from Agent.nodes.grade_documents import grade_documents
from Agent.state import GraphState
from Agent.chain.hallucination import  hallucination_grader
from Agent.chain.answer_grader import  answer_grader
from Agent.chain.router import question_router

load_dotenv()


def decide_to_generate(state):
    print("++++++++++Asses Node Graph+++++++++")

    if state["web_search"]:
        print("------Not Relevant Document------")
        return  WEBSEARCH
    else:

        print("------Relevant Document------")
        return GENERATE
# def decide_generaton_grounded_in_documents_and_questions(state: GraphState):
#     print("=====check Hallucination=====")
#     question=state["question"]
#     generation= state["generation"]
#     document= state["documents"]
#     score= hallucination_grader.invoke({
#         "documents":document, "generation":generation
#     })
#     if score.binary_score:
#         print("====Not Halllucinated=======")
#         score=answer_grader.invoke({
#             "question":question,
#             "generation":generation
#         })
#         if score.binary_score:
#             return "useful"
#         else:
#             return "not useful"
#     else:
#         return "not supported"
def route_question(state:GraphState):
    print("====Route Question=====")
    question= state["question"]
    source=question_router.invoke({"question":question})
    if source.datasource==WEBSEARCH:
        return WEBSEARCH
    else:
        return RETRIEVE

# stateretrievellama=StateRetrieveLLAMA("knowledgebase","llama_embed_knolwdge")
stateretrievellama=StateRetrieveLLAMA("knowledgebase","hrcolection")

# stateretrievemaxbai= StateRetrieveMaxbai("knowledgebase","maxbai_embed_knolwdge")
# stateretrieverecursive=StateRetrieveRecursive("knowledgebase","recursive_embed_knolwdge")
workflow=StateGraph(GraphState)
workflow.add_node(RETRIEVE_LLAMA, stateretrievellama.retrieve)
# workflow.add_node(RETRIEVE_MAXBAI, stateretrievemaxbai.retrieve)

# workflow.add_node(RETRIEVE_Recursive, stateretrieverecursive.retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
# workflow.add_node(ENHANCE_QUERY,generate_query)
workflow.add_node(GENERATE_LLAMA, generate_llama)
# workflow.add_node(GENERATE_RECURSIVE, generate_recursive)
# workflow.add_node(GENERATE_LLAMA, tavily_web_search)
# workflow.add_node(GENERATE_LLAMA, tavily_web_search)
workflow.set_entry_point(RETRIEVE_LLAMA)
# workflow.add_edge(ENHANCE_QUERY,RETRIEVE_LLAMA)
workflow.add_edge(RETRIEVE_LLAMA, GRADE_DOCUMENTS)
workflow.add_edge(GRADE_DOCUMENTS, GENERATE_LLAMA)
# workflow.set_conditional_entry_point(
#     route_question,
#     {
        
#         RETRIEVE:RETRIEVE
#     }
# )
# workflow.add_conditional_edges(
#     GRADE_DOCUMENTS,
#     decide_to_generate,
#     {
        
#      GENERATE:GENERATE,
#      },

# )
# workflow.add_conditional_edges(
#     GENERATE,
#     decide_generaton_grounded_in_documents_and_questions,
#     {
#         "not supported": GENERATE,
#         "useful": END,
#         "not useful": END
#     }

# )
# workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE_LLAMA, END)

app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")