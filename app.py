from agent import run_agent

while True:
    q = input("Sen: ")
    result = run_agent(q)
    print("Agent:", result["output"])