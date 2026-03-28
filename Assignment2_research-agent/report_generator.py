def generate_report(topic, research_data):
    return f"""
COVER PAGE
Title: {topic}

INTRODUCTION
{research_data[:500]}

KEY FINDINGS
{research_data}

CHALLENGES
- Privacy issues
- Cost
- Ethics

FUTURE SCOPE
- Better AI
- Automation

CONCLUSION
AI is transforming industries.
"""