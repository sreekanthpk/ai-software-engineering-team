from crewai import Crew

from agents.agents import ba_agent, engineer_a, engineer_b, qa_agent
from agents.task import user_stories_task, engineer_a_task, engineer_b_review_task, engineer_a_fix_task, qa_certification_task

crew = Crew(
    agents=[ba_agent, engineer_a, engineer_b, qa_agent],
    tasks=[user_stories_task, engineer_a_task, engineer_b_review_task, engineer_a_fix_task, qa_certification_task],
    verbose=True
)
if __name__ == "__main__":
    result = crew.kickoff()
    print("\nFINAL RESULT:\n", result)