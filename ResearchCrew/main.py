import sys
import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Crew, Process
from tasks import LegalResearchTasks
from agents import LegalResearchAgents



# Initialize the agents and tasks classes
agents = LegalResearchAgents()
tasks = LegalResearchTasks()

# Welcome message and input for case details
print("Please provide the case details:")
case_details = input()

# Create Agents (Note that we're calling the methods to get instances of Agent)
legal_issue_analyst = agents.legal_issue_identifier()
legal_researcher = agents.legal_source_gatherer()
legal_analyst = agents.legal_source_analyst()
case_law_applier = agents.legal_application_specialist()
legal_writer = agents.legal_documentation_expert()
legal_research_auditor = agents.legal_research_reviewer()

# Create Tasks
identify_legal_issue_task = tasks.identify_legal_issue_task(legal_issue_analyst, case_details)
gather_sources_task = tasks.gather_sources_task(legal_researcher, case_details)
analyze_sources_task = tasks.analyze_sources_task(legal_analyst, case_details)
apply_law_task = tasks.apply_law_task(case_law_applier, case_details) 
document_findings_task = tasks.document_findings_task(legal_writer, case_details)
review_update_task = tasks.review_update_task(legal_research_auditor, case_details)

# Create Crew responsible for process document writing
legal_research_crew = Crew(
    agents=[
        legal_issue_analyst, 
        legal_researcher,  
        legal_analyst,
        case_law_applier,
        legal_writer,
        legal_research_auditor
    ],
    tasks=[
        identify_legal_issue_task,
        gather_sources_task,
        analyze_sources_task, 
        apply_law_task,
        document_findings_task,
        review_update_task
    ],
    verbose=True,
    manager_llm=ChatOpenAI(temperature=0, model="gpt-4o"),  # Mandatory for hierarchical process
    process=Process.hierarchical,  # Specifies the hierarchical management approach
    memory=True,
)

# Execute the crew's tasks
legal_research_document = legal_research_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("response:")
print(legal_research_document)
