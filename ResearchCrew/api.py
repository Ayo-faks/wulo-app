from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from crewai import Crew, Process
from tasks import LegalResearchTasks
from agents import LegalResearchAgents

app = FastAPI()

class CaseDetails(BaseModel):
    details: str

# Initialize the agents and tasks classes
agents = LegalResearchAgents()
tasks = LegalResearchTasks()

@app.post("/process_case/")
async def process_case(case: CaseDetails):
    try:
        # Create Agents
        legal_issue_analyst = agents.legal_issue_identifier()
        legal_researcher = agents.legal_source_gatherer()
        legal_analyst = agents.legal_source_analyst()
        case_law_applier = agents.legal_application_specialist()
        legal_writer = agents.legal_documentation_expert()
        legal_research_auditor = agents.legal_research_reviewer()

        # Create Tasks
        identify_legal_issue_task = tasks.identify_legal_issue_task(legal_issue_analyst, case.details)
        gather_sources_task = tasks.gather_sources_task(legal_researcher, case.details)
        analyze_sources_task = tasks.analyze_sources_task(legal_analyst, case.details)
        apply_law_task = tasks.apply_law_task(case_law_applier, case.details)
        document_findings_task = tasks.document_findings_task(legal_writer, case.details)
        review_update_task = tasks.review_update_task(legal_research_auditor, case.details)

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

        return {"output": legal_research_document}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)