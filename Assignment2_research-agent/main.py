from agent import agent
from report_generator import generate_report

def run_agent(topic):
    query = f"Research the topic: {topic}"

    result = agent.run(query[:1000])  # limit input size

    report = generate_report(topic, result[:2000])  # limit output size

    print(report)

    with open(f"{topic}.txt", "w", encoding="utf-8") as f:
        f.write(report)

if __name__ == "__main__":
    topic = input("Enter topic: ")
    run_agent(topic)