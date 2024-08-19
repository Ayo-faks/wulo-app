import os
from textwrap import dedent
from dotenv import load_dotenv
from crewai import Agent
from tools.neo4j_tool import SearchTool
from langchain_openai import AzureChatOpenAI

# Load environment variables from the .env file
load_dotenv()

class LegalResearchAgents:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            openai_api_version=os.environ.get("AZURE_OPENAI_VERSION"),
            azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY")
        )
        self.search_tool = SearchTool()

    def legal_issue_identifier(self):
        return Agent(
            role="Legal Issue Analyst",
            goal=dedent("""\
                Clearly define the legal question or issue that needs to be addressed."""),
            backstory=dedent("""\
                You are skilled at distilling complex legal scenarios into clear, concise legal questions.
                Your experience allows you to identify the core issues that need to be addressed in any legal case."""),
            tools=[self.search_tool.search],
            verbose=True,
            cache=True,
            allow_delegation=False,
            llm=self.llm
        )

    def legal_source_gatherer(self):
        return Agent(
            role="Legal Researcher",
            goal=dedent("""\
                Collect statutes, regulations, case law, and other legal materials pertinent to the issue."""),
            backstory=dedent("""\
                You have a vast knowledge of legal databases and resources.
                Your expertise lies in quickly gathering all relevant legal materials needed
                to address specific legal issues."""),
            tools=[self.search_tool.search],
            llm=self.llm,
            cache=True,
            allow_delegation=False,
            verbose=True
        )

    def legal_source_analyst(self):
        return Agent(
            role="Legal Analyst",
            goal=dedent("""\
                Examine and interpret the gathered legal materials to understand their application to the legal issue."""),
            backstory=dedent("""\
                You excel in analyzing and interpreting legal texts, ensuring that every nuance of the law is considered.
                Your analytical skills help in understanding how laws and precedents apply to specific cases."""),
            tools=[self.search_tool.search],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def legal_application_specialist(self):
        return Agent(
            role="Case Law Applier",
            goal=dedent("""\
                Relate the legal principles and precedents to the specific facts of the case at hand."""),
            backstory=dedent("""\
                You excel in applying legal principles to real-world scenarios, ensuring the law is applied accurately and effectively."""),
            tools=[self.search_tool.search],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def legal_documentation_expert(self):
        return Agent(
            role="Legal Writer",
            goal=dedent("""\
                Write a legal memorandum or brief that outlines the research findings, legal arguments, and conclusions."""),
            backstory=dedent("""\
                You are adept at crafting clear, persuasive legal documents.
                Your writing helps communicate complex legal arguments in a concise and logical manner."""),
            tools=[self.search_tool.search],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )

    def legal_research_reviewer(self):
        return Agent(
            role="Legal Research Auditor",
            goal=dedent("""\
                Continuously review and update the research to ensure it reflects the most current legal standards and precedents."""),
            backstory=dedent("""\
                You have a meticulous eye for detail and are constantly up-to-date with the latest legal standards and precedents.
                Your role is to ensure that legal research is always current and accurate."""),
            tools=[self.search_tool.search],
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
