from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub

# Llama gibi yerel modeller genellikle 'react' tarzı düşünmeye yatkındır
prompt = hub.pull("hwchase17/react")

# Agent'ı oluştur (llm değişkeninin Llama'ya bağlı olduğunu varsayıyorum)
agent = create_react_agent(llm, tools, prompt)

# Çalıştırıcıyı başlat
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)