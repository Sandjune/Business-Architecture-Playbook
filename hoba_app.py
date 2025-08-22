# Business-Architecture-Playbook
import os
import streamlit as st
from streamlit.components.v1 import html

# >>> Hardcoded path to your attached image (already available)
IMAGE_PATH = "Playbook_framework_complete.png"

st.set_page_config(
    page_title="Business Transformation - Roadmap Navigator",
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
    
    **How the Objective is Executed within the Playbook Stage:**
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
    
    **How the Objective is Executed within the Playbook Stage:**
    This is the "how" for projects. 
    - Projects (Initiatives) are assessed against the target capability model (Governance).
    - Technology selection is guided by the requirements of the capabilities the project is enhancing.
    - Exceptions are managed by evaluating their impact on the target business capability model.
    
    **Key Activities:**
    - Require architects to identify which business capabilities each project impacts
    - Use EA governance process to review projects against capability-centric view
    - Frame RFP/RFI questions around capability requirements
    """,
    "Design the Business Change": """
    **Central 1 Objective(s) Mapped:**
    - Work with project teams and architects to ensure adherence to standards
    - Work on highly complex projects that require in-depth knowledge across multiple specialized architecture domains.
    - Support all architectural disciplines.
    
    **How the Objective is Executed within the Playbook Stage:**
    At this stage, architects design solutions that fulfill the requirements. 
    Their designs must show how they enable the Value Streams and Capabilities from Stage 3, 
    using the Standards defined in Stage 4.
    
    **Key Activities:**
    - Mandate that solution architects use the defined capability map and value streams
    - Research and develop position papers on new technologies
    - Evaluate technologies based on their potential to enable business capabilities
    """,
    "Implement the Business Change": """
    **Central 1 Objective(s) Mapped:**
    - Establish metrics to improve business processes
    - Identify opportunities to improve EA maturity
    - Facilitate the EA governance processes.
    
    **How the Objective is Executed within the Playbook Stage:**
    This is the "measure and govern" stage. 
    - Metrics are established at the Capability level (e.g., cost, performance of a capability).
    - Governance is the process of ensuring Initiatives (Stage 4) align with the Model (Stage 3) to achieve Motivation (Stage 2).
    
    **Key Activities:**
    - Establish metrics at the capability level
    - Maintain the 3-5 year target architecture roadmap as a capability evolution plan
    - Improve EA maturity by demonstrating how architecture ties to business outcomes
    """
}

def show_picture():
    st.title("Business Architecture Playbook - Framework: Visual Overview")
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        if os.path.exists(IMAGE_PATH):
            st.image(IMAGE_PATH, use_container_width=True)
        else:
            st.warning(f"Image not found at **{IMAGE_PATH}**.")
        st.markdown("""
        **How to use this view:**
        - Use the sidebar to navigate to any Playbook stage for detailed information.
        - Click **Back to Picture** on a stage page to return to this image.
        """)
    with st.expander("Understanding the Visual Workflow"):
        st.markdown("""
        The picture above serves as the entry-point to your Business Architecture playbook.
        Use the sidebar to jump into each stage:
        1. **Business Problem** → establish the why.
        2. **Business Motivation** → define strategies and principles.
        3. **Business Model** → map capabilities and value streams.
        4. **Business Requirements** → guide initiatives and selections.
        5. **Design the Business Change** → architect solutions.
        6. **Implement the Business Change** → measure and govern.
        """)

def main():
    if "current_stage" not in st.session_state:
        st.session_state.current_stage = None

    with st.sidebar:
        st.title("Business Architecture Transformer - Framework Navigator")
        st.markdown("""
        The **The Business Architecture Playbook** framework provides a structured, 
        business-out approach to transformation, ensuring that technical activities are 
        directly traceable to business objectives.
        """)
        st.markdown("### Stages")
        for stage in stage_content.keys():
            if st.button(stage, use_container_width=True):
                st.session_state.current_stage = stage
        st.markdown("---")
        st.markdown("### About")
        st.markdown("This application demonstrates how enterprise architecture objectives map to the HOBA framework.")

    if st.session_state.current_stage:
        st.title(st.session_state.current_stage)
        st.markdown(stage_content[st.session_state.current_stage])
        if st.button("Back to Picture"):
            st.session_state.current_stage = None
            st.rerun()
    else:
        show_picture()

if __name__ == "__main__":
    main()
