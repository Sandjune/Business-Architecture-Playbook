# Business-Architecture-Playbook
import os
import streamlit as st
from streamlit.components.v1 import html

# >>> Hardcoded path to your attached image (already available)
IMAGE_PATH = "/mnt/data/deepseek_mermaid_20250821_480e45.png"

st.set_page_config(
    page_title="Business Architecture Transformation Roadmap - Framework Navigator",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------
# HOBA stage content (unchanged)
# ------------------------------
stage_content = {
    "Business Problem": """
    **Central 1 Objective(s) Mapped:**
    - Communicate enterprise objectives and transformation roadmaps with infrastructure, applications, solutions, and business leaders
    - Review existing business processes and establish metrics to improve business processes, as well as support of all architectural disciplines under their direction.
    
    **How the Objective is Executed within the Playbook Stage:**
    This is the "why." You start by understanding and communicating the business problems, 
    pain points, and strategic objectives that the transformation aims to solve. 
    This justifies all subsequent architecture work.
    
    **Key Activities:**
    - Conduct stakeholder interviews with business and IT leaders
    - Document specific "business problems" the architecture must solve
    - Formalize a "Problem Statement" agreed upon by all key stakeholders
    """,
    "Business Motivation": """
    **Central 1 Objective(s) Mapped:**
    - Communicate enterprise objectives and transformation roadmaps with infrastructure, applications, solutions, and business leaders.
    - Integrate strategic guidelines into project implementation
    - Research new tech trends and develop position papers
    
    **How the Objective is Executed within the HOBA Stage:**
    This is the "what." You translate business objectives into concrete strategies and principles. 
    Position papers on new technologies are created here to evaluate their potential to support business motivations.
    
    **Key Activities:**
    - Map each proposed technical standard and target state to top-level business objectives
    - Create a "Motivation Model" showing architectural principles and decisions
    - Develop position papers on new technologies
    """,
    "Business Model": """
    **Central Objective(s) Mapped:**
    - Define and maintain comprehensive technical standards and 3–5-year target architecture roadmaps for key technologies (infrastructure, application layers);
    - Find and resolve portfolio-wide and project-wide interdependencies and ensure project scheduled accordingly
    - Review existing business processes and establish metrics to improve business processes, as well as support of all architectural disciplines under their direction.
    - Work on highly complex projects that require in-depth knowledge across multiple specialized architecture domains.
    
    **How the Objective is Executed within the Playbook Stage:**
    This is the CORE of the mapping. 
    - Target Roadmaps are defined based on evolving Business Capabilities.
    - Interdependencies are found by analyzing Value Streams that cut across capabilities.
    - Business processes are reviewed to inform the Value Stream and Capability models.
    
    **Key Activities:**
    - Create a Business Capability Map for the organization
    - Assess current and desired maturity level for each capability
    - Define technical standards and target architecture by capability
    - Model key value streams to identify bottlenecks
    """,
    "Business Requirements": """
    **Central 1 Objective(s) Mapped:**
    - Work with project teams to ensure adherence to standards
    - Integrate strategic guidelines into project implementation
    - Participate and contribute to technology selection due diligence processes (RFP, RFI, etc.)
    - Manage exceptions to architectural standards at an enterprise level.
    
    **How the Objective is Executed within**

