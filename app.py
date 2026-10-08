import streamlit as st

from llm import get_llm, generate_response
from prompt_template import create_prompt


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="PromptXpert AI",
    page_icon="⚡",
    layout="wide"
)


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>

    /* Main page */
    .main {
        padding-top: 1rem;
    }

    /* Hero section */
    .hero-box {
        padding: 35px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #0f172a,
            #1e3a8a
        );
        text-align: center;
        margin-bottom: 30px;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 800;
        color: white;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 19px;
        color: #dbeafe;
        margin: 0;
    }

    /* Feature cards */
    .feature-card {
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #334155;
        background: #0f172a;
        min-height: 180px;
    }

    .feature-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
        color: #60a5fa;
    }

    .feature-text {
        font-size: 15px;
        line-height: 1.6;
        color: #cbd5e1;
    }

    /* Generate button */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        font-size: 17px;
        font-weight: 700;
    }

    /* Text area */
    textarea {
        border-radius: 10px !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 25px;
        color: #94a3b8;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# HERO SECTION
# ==================================================

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">⚡ PROMPTXPERT AI</div>
        <div class="hero-subtitle">
            Transform Simple Ideas into Powerful AI Prompts
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.title("Prompt Settings")

    st.caption(
        "Configure how your prompt should be generated."
    )

    technique = st.selectbox(
        "Prompt Engineering Technique",
        [
            "Zero-Shot",
            "One-Shot",
            "Few-Shot",
            "Chain of Thought",
            "Manual CoT",
            "Tree of Thoughts",
            "MCOT"
        ]
    )

    st.divider()

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.5,
        value=0.7,
        step=0.1,
        help="Higher values produce more creative responses."
    )

    max_tokens = st.slider(
        "Maximum Tokens",
        min_value=100,
        max_value=2000,
        value=1000,
        step=100
    )

    st.divider()

    st.info(
        "Select a prompting technique, enter your idea, "
        "and let PromptXpert AI generate the response."
    )


# ==================================================
# MAIN INPUT SECTION
# ==================================================

st.header("Describe Your Idea")

st.write(
    "Enter a question, task, or idea that you want "
    "the AI to work on."
)

user_input = st.text_area(
    "Your Idea",
    placeholder=(
        "Example: Explain Artificial Intelligence "
        "to a beginner."
    ),
    height=160,
    label_visibility="collapsed"
)


# ==================================================
# GENERATE BUTTON
# ==================================================

generate = st.button(
    "⚡ Generate Powerful Prompt",
    type="primary"
)


# ==================================================
# GENERATION
# ==================================================

if generate:

    if not user_input.strip():

        st.warning(
            "Please enter an idea or question first."
        )

    else:

        try:

            # Create prompt using selected technique
            optimized_prompt = create_prompt(
                technique,
                user_input
            )

            # Connect to Hugging Face
            client = get_llm()

            # Generate AI response
            with st.spinner(
                "PromptXpert AI is generating your response..."
            ):

                response = generate_response(
                    client,
                    optimized_prompt,
                    temperature,
                    max_tokens
                )

            # ==================================================
            # GENERATED PROMPT
            # ==================================================

            st.divider()

            st.subheader("Generated Prompt")

            st.code(
                optimized_prompt,
                language="text"
            )

            # Download button
            st.download_button(
                label="Download Prompt",
                data=optimized_prompt,
                file_name="generated_prompt.txt",
                mime="text/plain"
            )

            # ==================================================
            # AI RESPONSE
            # ==================================================

            st.subheader("AI Response")

            st.write(response)

        except Exception as error:

            st.error(
                f"Unable to generate response: {error}"
            )


# ==================================================
# FEATURES
# ==================================================

st.divider()

st.header("Why PromptXpert AI?")


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        <div class="feature-card">

        <div class="feature-title">
        Prompt Techniques
        </div>

        <div class="feature-text">

        Supports Zero-Shot, One-Shot, Few-Shot,
        Chain of Thought, Manual CoT, Tree of Thoughts
        and MCOT techniques.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="feature-card">

        <div class="feature-title">
        AI Powered
        </div>

        <div class="feature-text">

        Uses Hugging Face AI models to transform
        prompts into useful and meaningful responses.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="feature-card">

        <div class="feature-title">
        Easy to Use
        </div>

        <div class="feature-text">

        Enter your idea, choose a prompting technique,
        and generate an AI-powered response instantly.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="footer">

    PROMPTXPERT AI | Prompt Engineering Project

    </div>
    """,
    unsafe_allow_html=True
)
