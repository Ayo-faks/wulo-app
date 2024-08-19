from crewai import Task
from textwrap import dedent

class LegalResearchTasks:
    def identify_legal_issue_task(self, agent, case_details):
        return Task(
            description=dedent(f"""\
                Analyze the given case details: {case_details}.

                Identify the primary legal issue or question that needs to be researched.

                Your final report should clearly articulate the key legal references and their applicability to the case.
                Emphasize the most pertinent legal precedents and statutes.

                Attention to detail is crucial for a comprehensive analysis. It's currently 2024.
            """),
            agent=agent,
            expected_output='A list of clearly defined legal questions or issue statements.'
        )

    def gather_sources_task(self, agent, case_details):
        return Task(
            description=dedent(f"""\
                Gather all relevant legal sources, including statutes, regulations, and case law, that pertain to the identified legal issue: {case_details}.

                Focus on obtaining precise search results and compiling a comprehensive list of sources.
            """),
            agent=agent,
            expected_output='A comprehensive list of relevant legal sources, with links or references to the materials.'
        )

    def analyze_sources_task(self, agent, case_details):
        return Task(
            description=dedent(f"""\
                Analyze the gathered legal sources to determine their relevance and how they apply to the identified legal issue: {case_details}.

                Confirm the accuracy and applicability of the legal references, and provide any necessary corrections or additional insights.

                Maintain a high standard of review to ensure the reliability of the findings.
            """),
            agent=agent,
            expected_output='A detailed analysis of the legal sources, explaining how each one applies to the legal issue.'
        )

    def apply_law_task(self, agent, case_details):
        return Task(
            description=dedent(f"""\
                Apply the analyzed legal principles and precedents to the specific facts of the case: {case_details}.

                Ensure that the application of the law is precise and relevant to the case at hand.
            """),
            agent=agent,
            expected_output='A report explaining how the legal principles and precedents apply to the facts of the case.'
        )

    def document_findings_task(self, agent, case_details):
        return Task(
            description=dedent(f"""\
                Based on the outputs from gather_sources_task and review_update_task, document the findings of the legal research in the form of a legal memorandum or brief: {case_details}.

                The document should be well-structured and convey the research findings, legal arguments, and conclusions clearly.
            """),
            agent=agent,
            expected_output='A well-structured legal memorandum or brief that outlines the research findings, legal arguments, and conclusions.'
        )

    def review_update_task(self, agent, case_details):
        return Task(
            description=dedent(f"""\
                Review and update the legal research regularly to ensure it remains current and accurate: {case_details}.

                Ensure that the research reflects the most recent legal standards and precedents.
            """),
            agent=agent,
            expected_output='An updated version of the legal memorandum or brief, reflecting the most recent legal standards and precedents.'
        )
