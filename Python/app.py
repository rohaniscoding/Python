import Agent
agent_1=Agent.agent('Shaktiman',32)
agent_1.health=agent_1.health*100
print(agent_1.info())
print('-'*15)

agent_2=Agent.agent('Gangadhar',32)
print(agent_2.info())
print('-'*15)

boss=Agent.agent('Kilvish',32)
boss.health*=1000
print(boss.info())
print('-'*15)