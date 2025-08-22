# Business-Architecture-Playbook
import streamlit as st
import graphviz as graphviz
from streamlit.components.v1 import html

# Set page configuration
st.set_page_config(
    page_title="Business Architecture Transformation Roadmap - Framework Navigator",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the detailed content for each HOBA stage
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
    
    **How the Objective is Executed within the HOBA Stage:**
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
    - Work with project teams and architects...
    - Work on highly complex projects...
    - Support all architectural disciplines...
    
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
    **Primary Objective(s) Mapped:**
    - Establish metrics to improve business processes
    - Identify opportunities to improve EA maturity
    - Facilitate the EA governance processes.
    
    **How the Objective is Executed within the HOBA Stage:**
    This is the "measure and govern" stage. 
    - Metrics are established at the Capability level (e.g., cost, performance of a capability).
    - Governance is the process of ensuring Initiatives (Stage 4) align with the Model (Stage 3) to achieve Motivation (Stage 2).
    
    **Key Activities:**
    - Establish metrics at the capability level
    - Maintain the 3-5 year target architecture roadmap as a capability evolution plan
    - Improve EA maturity by demonstrating how architecture ties to business outcomes
    """
}

# Function to create the HOBA diagram
def create_hoba_diagram():
    # Create a graph
    dot = graphviz.Digraph(comment='HOBA Framework')
    dot.attr(rankdir='TB', size='12,8', bgcolor='lightgray')
    
    # Define nodes with styling
    dot.node('A', '1. Business Problem', 
             shape='box', style='filled', fillcolor='#90be6d', fontsize='14', width='2', height='1')
    dot.node('B', '2. Business Motivation', 
             shape='box', style='filled', fillcolor='#e9c46a', fontsize='14', width='2', height='1')
    dot.node('C', '3. Business Model\n(Capabilities & Value Streams)', 
             shape='box', style='filled', fillcolor='#f8961e', fontsize='14', width='2.5', height='1.2')
    dot.node('D', '4. Business Requirements\n(Initiatives)', 
             shape='box', style='filled', fillcolor='#f3722c', fontsize='14', width='2.5', height='1.2')
    dot.node('E', '5. Design the Business Change\n(Solution Architecture)', 
             shape='box', style='filled', fillcolor='#f94144', fontsize='14', width='2.5', height='1.2')
    dot.node('F', '6. Implement the Business Change\n(Transformation)', 
             shape='box', style='filled', fillcolor='#577590', fontsize='14', width='2.5', height='1.2')
    
    # Define edges
    dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])
    
    # Add cross-cutting elements
    dot.node('G', 'Technical Standards', 
             shape='box', style='filled,dashed', fillcolor='white', fontsize='12', width='2', height='0.7')
    dot.node('H', 'Governance Process', 
             shape='box', style='filled,dashed', fillcolor='white', fontsize='12', width='2', height='0.7')
    
    # Connect cross-cutting elements
    dot.edge('G', 'D', style='dashed', arrowhead='none')
    dot.edge('H', 'F', style='dashed', arrowhead='none')
    dot.edge('G', 'H', style='invis')
    
    return dot

# Main app
def main():
    # Initialize session state for page navigation
    if 'current_stage' not in st.session_state:
        st.session_state.current_stage = None
    
    # Sidebar
    with st.sidebar:
        st.title("HOBA Framework Navigator")
        st.markdown("""
        The **House of Business Architecture (HOBA)** framework provides a structured, 
        business-out approach to transformation, ensuring that technical activities are 
        directly traceable to business objectives.
        
        Select a stage to learn more about how it maps to enterprise architecture objectives.
        """)
        
        # Create buttons for each stage
        for stage in stage_content.keys():
            if st.button(stage, use_container_width=True):
                st.session_state.current_stage = stage
                
        st.markdown("---")
        st.markdown("### About")
        st.markdown("This application demonstrates how enterprise architecture objectives map to the HOBA framework.")
    
    # Main content area
    if st.session_state.current_stage:
        # Show detailed content for the selected stage
        st.title(st.session_state.current_stage)
        st.markdown(stage_content[st.session_state.current_stage])
        
        if st.button("Back to Diagram"):
            st.session_state.current_stage = None
            st.rerun()
    else:
        # Show the diagram
        st.title("HOBA Framework: Mapping Enterprise Architecture Objectives")
        
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            # Display the diagram
            diagram = create_hoba_diagram()
            st.graphviz_chart(diagram, use_container_width=True)
            
            st.markdown("""
            **How to use this diagram:**
            - Each box represents a stage in the HOBA framework
            - Click on any stage in the sidebar to view detailed information
            - The diagram shows the flow from business problem to implementation
            - Cross-cutting elements (Technical Standards and Governance Process) apply across multiple stages
            """)
            
            # Add explanation of the visual workflow
            with st.expander("Understanding the Visual Workflow"):
                st.markdown("""
                The flowchart shows how the outputs of each HOBA stage directly enable you to 
                achieve enterprise architecture objectives more effectively:
                
                1. **Business Problem** provides justification for all architecture work
                2. **Business Motivation** outputs strategies and principles
                3. **Business Model** enables core EA activities like creating roadmaps and identifying interdependencies
                4. **Business Requirements** guides project implementation, technology selection, and exception management
                5. **Design the Business Change** focuses on solution architecture
                6. **Implement the Business Change** establishes metrics and runs the governance process
                
                The **Technical Standards** and **Governance Process** (in dashed boxes) are cross-cutting 
                activities that apply to multiple stages.
                """)

if __name__ == "__main__":
    main()
