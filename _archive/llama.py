from llama_cpp import Llama

llm = Llama(model_path="./models/Llama-2-7b-Chat-GGUF/llama-2-7b-chat.Q3_K_M.gguf", n_ctx=4096)
company_description = "ABB is a technology leader in electrification and automation"
requirements = "Machine Learning Engineer looking for a full-time job"
output = llm("Q: Should I contact the company ABB if I am a ML Engineer looking for a job? The company description is: technology leader in electrification and automation.  A:", max_tokens=2048, stop=["Q:", "\n"], echo=True)
print(output)