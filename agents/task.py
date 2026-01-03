from crewai import Task

from agents.agents import ba_agent, engineer_a, engineer_b, qa_agent

user_stories_task = Task(
    description="""
    Create a PRODUCT REQUIREMENTS DOCUMENT in Markdown.

    Include:
    - User personas
    - Epics
    - User stories (As a user, I want...)
    - Acceptance criteria
    - Non-functional requirements
    - Analytics metrics
    """,
    agent=ba_agent,
    expected_output="Markdown PRD with user stories and acceptance criteria"
)

engineer_a_task = Task(
    description="""
    Implement backend + frontend based on user stories.
    - Use public Bitcoin APIs
    - Build analytics engine
    - Build UI dashboard
    - Commit code to Git (describe repo structure)
    - Prepare AWS deployment plan (ECS/Fargate or EC2)
    """,
    agent=engineer_a,
    expected_output="Code, repo structure, AWS deployment steps"
)

engineer_b_review_task = Task(
    description="""
    Review Engineer A's code.
    - Identify bugs, security gaps, performance issues
    - Suggest refactors
    - Implement missing features
    - Approve or reject code
    """,
    agent=engineer_b,
    expected_output="Code review report + approved fixes"
)

engineer_a_fix_task = Task(
    description="""
    Address code review feedback.
    - Refactor code
    - Improve tests
    - Push final version to Git
    - Deploy application to AWS
    """,
    agent=engineer_a,
    expected_output="Production-ready deployed system"
)

qa_certification_task = Task(
    description="""
    Certify the platform.
    - Execute test strategy
    - Validate user stories acceptance criteria
    - Test performance and UI
    - Approve or BLOCK release
    """,
    agent=qa_agent,
    expected_output="QA certification report (PASS or FAIL)"
)

