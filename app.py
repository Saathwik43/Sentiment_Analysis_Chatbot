import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import json
import os
import plotly.graph_objects as go
import plotly.express as px

# Page config
st.set_page_config(
    page_title="🤖 Sentiment Analysis Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .analysis-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e1e5e9;
    }
    .stButton > button {
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

class StreamlitSentimentAnalyzer:
    def __init__(self):
        self.history_file = 'sentiment_history.json'
        self.load_history()
    
    def load_history(self):
        """Load analysis history from file"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r') as f:
                    st.session_state.analysis_history = json.load(f)
            else:
                st.session_state.analysis_history = []
        except Exception as e:
            st.session_state.analysis_history = []
    
    def save_to_history(self, text, polarity, subjectivity, sentiment_label):
        """Save analysis to history"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "text": text[:100] + "..." if len(text) > 100 else text,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment_label,
        }
        
        if 'analysis_history' not in st.session_state:
            st.session_state.analysis_history = []
        
        st.session_state.analysis_history.append(entry)
        
        # Keep only last 50 entries
        if len(st.session_state.analysis_history) > 50:
            st.session_state.analysis_history = st.session_state.analysis_history[-50:]
        
        # Save to file
        try:
            with open(self.history_file, 'w') as f:
                json.dump(st.session_state.analysis_history, f, indent=2)
        except Exception as e:
            st.error(f"Failed to save history: {e}")
    
    def interpret_polarity(self, polarity):
        """Interpret polarity score"""
        if polarity > 0.5:
            return "Highly positive sentiment - indicates strong satisfaction or approval"
        elif polarity > 0.1:
            return "Positive sentiment - generally favorable opinion"
        elif polarity > -0.1:
            return "Neutral sentiment - balanced or factual content"
        elif polarity > -0.5:
            return "Negative sentiment - indicates dissatisfaction or criticism"
        else:
            return "Highly negative sentiment - strong disapproval or anger"
    
    def interpret_subjectivity(self, subjectivity):
        """Interpret subjectivity score"""
        if subjectivity > 0.7:
            return "Highly subjective - personal opinions and emotions dominate"
        elif subjectivity > 0.4:
            return "Moderately subjective - mix of facts and opinions"
        else:
            return "Objective - primarily factual information"
    
    def generate_business_insights(self, polarity, subjectivity):
        """Generate business insights"""
        insights = []
        
        if polarity > 0.3 and subjectivity < 0.5:
            insights.append("• Strong positive feedback - consider using as testimonial")
        elif polarity < -0.3 and subjectivity > 0.6:
            insights.append("• Negative emotional response - requires immediate attention")
        elif abs(polarity) < 0.1:
            insights.append("• Neutral feedback - may need follow-up for clarity")
        
        if subjectivity > 0.8:
            insights.append("• Highly emotional content - focus on empathy in response")
        elif subjectivity < 0.2:
            insights.append("• Factual content - suitable for data-driven analysis")
        
        return "\n".join(insights) if insights else "• Standard sentiment analysis - no special recommendations"
    
    def analyze_sentiment(self, text):
        """Perform sentiment analysis"""
        try:
            # Perform sentiment analysis
            blob = TextBlob(text)
            sentiment = blob.sentiment
            polarity = sentiment.polarity
            subjectivity = sentiment.subjectivity
            
            # Determine sentiment category
            if polarity > 0.1:
                sentiment_label = "Positive 😊"
                color = "#4CAF50"
            elif polarity < -0.1:
                sentiment_label = "Negative 😞"
                color = "#f44336"
            else:
                sentiment_label = "Neutral 😐"
                color = "#FF9800"
            
            return polarity, subjectivity, sentiment_label, color
            
        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")
            return None, None, None, None
    
    def create_detailed_analysis(self, text, polarity, subjectivity, sentiment_label):
        """Create detailed analysis report"""
        # Word count and basic stats
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        sentence_count = len([s for s in text.split('.') if s.strip()])
        
        # Sentiment strength
        strength = abs(polarity)
        if strength > 0.7:
            strength_desc = "Very Strong"
        elif strength > 0.4:
            strength_desc = "Strong"
        elif strength > 0.1:
            strength_desc = "Moderate"
        else:
            strength_desc = "Weak"
        
        # Subjectivity interpretation
        if subjectivity > 0.7:
            subjectivity_desc = "Very Subjective (Opinion-based)"
        elif subjectivity > 0.4:
            subjectivity_desc = "Moderately Subjective"
        else:
            subjectivity_desc = "Objective (Fact-based)"
        
        return {
            'word_count': word_count,
            'char_count': char_count,
            'sentence_count': sentence_count,
            'strength_desc': strength_desc,
            'subjectivity_desc': subjectivity_desc
        }

def main():
    # Initialize analyzer
    analyzer = StreamlitSentimentAnalyzer()
    
    # Modern header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Sentiment Analysis</h1>
        <p>Analyze emotions and opinions in text with advanced NLP</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Modern sidebar
    with st.sidebar:
        st.markdown("### 📊 Analytics Dashboard")
        
        # Quick stats
        if 'analysis_history' in st.session_state and st.session_state.analysis_history:
            total_analyses = len(st.session_state.analysis_history)
            recent_sentiment = st.session_state.analysis_history[-1]['sentiment'] if st.session_state.analysis_history else "None"
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total", total_analyses)
            with col2:
                st.metric("Latest", recent_sentiment.split()[0])
        
        st.markdown("---")
        
        if st.button("📈 View Analytics", use_container_width=True):
            if 'analysis_history' in st.session_state and st.session_state.analysis_history:
                st.session_state.show_history = True
            else:
                st.info("No analysis history available!")
        
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.analysis_history = []
            if os.path.exists('sentiment_history.json'):
                os.remove('sentiment_history.json')
            st.success("History cleared!")
            
        st.markdown("---")
        st.markdown("### 💡 Quick Tips")
        st.info("""
        **Best Results:**
        • Use complete sentences
        • Include context
        • Try different text types
        """)
    
    # Modern input section
    st.markdown("### 📝 Text Analysis")
    
    # Initialize user_text
    default_text = ""
    if 'selected_sample' in st.session_state:
        default_text = st.session_state.selected_sample
        del st.session_state.selected_sample
    
    # Input container
    with st.container():
        user_text = st.text_area(
            "Enter your text for sentiment analysis:",
            value=default_text,
            height=120,
            placeholder="✨ Paste your text here... (reviews, feedback, social media posts, etc.)",
            help="Enter any text to analyze its emotional tone and subjectivity"
        )
        
        # Action buttons in a clean row
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            analyze_button = st.button("🚀 Analyze Sentiment", type="primary", use_container_width=True)
        with col2:
            if st.button("🔄 Clear", use_container_width=True):
                st.rerun()
        with col3:
            if st.button("📋 Sample", use_container_width=True):
                st.session_state.sample_text = True
        with col4:
            st.button("💡 Help", use_container_width=True, help="Tips: Use complete sentences for better accuracy")
    
    # Enhanced sample text functionality
    if 'sample_text' in st.session_state and st.session_state.sample_text:
        st.markdown("#### 📋 Sample Texts")
        sample_texts = {
            "😊 Positive Review": "I absolutely love this product! It exceeded my expectations and the customer service was amazing.",
            "😞 Negative Feedback": "This service was terrible and the staff was completely unhelpful and rude.",
            "😐 Neutral Statement": "The weather forecast indicates rain tomorrow with temperatures around 20 degrees.",
            "🤔 Mixed Opinion": "I'm feeling okay about this decision, not great but not bad either. It has pros and cons."
        }
        
        selected_key = st.selectbox("Choose a sample:", list(sample_texts.keys()))
        st.text_area("Preview:", sample_texts[selected_key], height=60, disabled=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Use This Sample", use_container_width=True):
                st.session_state.selected_sample = sample_texts[selected_key]
                st.session_state.sample_text = False
                st.rerun()
        with col2:
            if st.button("❌ Cancel", use_container_width=True):
                st.session_state.sample_text = False
                st.rerun()
    
    # Use selected sample text
    if 'selected_sample' in st.session_state:
        user_text = st.session_state.selected_sample
        del st.session_state.selected_sample
        st.rerun()
    
    # Analysis section
    if analyze_button and user_text.strip():
        with st.spinner("🔄 Analyzing sentiment..."):
            polarity, subjectivity, sentiment_label, color = analyzer.analyze_sentiment(user_text)
            
            if polarity is not None:
                # Save to history
                analyzer.save_to_history(user_text, polarity, subjectivity, sentiment_label)
                
                # Get detailed analysis
                details = analyzer.create_detailed_analysis(user_text, polarity, subjectivity, sentiment_label)
                
                # Modern results section
                st.markdown("### 📊 Analysis Results")
                
                # Main results with modern cards
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        label="Overall Sentiment",
                        value=sentiment_label,
                        delta=f"Strength: {details['strength_desc']}"
                    )
                
                with col2:
                    st.metric(
                        label="Polarity Score",
                        value=f"{polarity:.3f}",
                        delta="Range: -1 to +1"
                    )
                
                with col3:
                    st.metric(
                        label="Subjectivity Score",
                        value=f"{subjectivity:.3f}",
                        delta="Range: 0 to 1"
                    )
                
                # Enhanced detailed breakdown
                st.markdown("### 🔍 Detailed Analysis")
                
                # Create tabs for better organization
                tab1, tab2, tab3 = st.tabs(["📊 Statistics", "💡 Insights", "📈 Visualization"])
                
                with tab1:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**Text Statistics**")
                        stats_data = {
                            "📝 Words": details['word_count'],
                            "🔤 Characters": details['char_count'],
                            "📄 Sentences": details['sentence_count']
                        }
                        for key, value in stats_data.items():
                            st.metric(key, value)
                    
                    with col2:
                        st.markdown("**Sentiment Profile**")
                        st.info(f"**Type:** {details['subjectivity_desc']}")
                        st.info(f"**Strength:** {details['strength_desc']}")
                
                with tab2:
                    st.markdown("**🎯 Interpretation**")
                    st.write(f"**Polarity:** {analyzer.interpret_polarity(polarity)}")
                    st.write(f"**Subjectivity:** {analyzer.interpret_subjectivity(subjectivity)}")
                    
                    st.markdown("**💼 Business Insights**")
                    insights = analyzer.generate_business_insights(polarity, subjectivity)
                    st.success(insights)
                
                with tab3:
                    # Modern gauge charts using Plotly
                    fig_polarity = go.Figure(go.Indicator(
                        mode = "gauge+number+delta",
                        value = polarity,
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Polarity Score"},
                        delta = {'reference': 0},
                        gauge = {
                            'axis': {'range': [-1, 1]},
                            'bar': {'color': color},
                            'steps': [
                                {'range': [-1, -0.1], 'color': "#ffcccc"},
                                {'range': [-0.1, 0.1], 'color': "#fff2cc"},
                                {'range': [0.1, 1], 'color': "#ccffcc"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 0
                            }
                        }
                    ))
                    fig_polarity.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
                    st.plotly_chart(fig_polarity, use_container_width=True)
                    
                    fig_subjectivity = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = subjectivity,
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "Subjectivity Score"},
                        gauge = {
                            'axis': {'range': [0, 1]},
                            'bar': {'color': "#2196F3"},
                            'steps': [
                                {'range': [0, 0.4], 'color': "#e3f2fd"},
                                {'range': [0.4, 0.7], 'color': "#bbdefb"},
                                {'range': [0.7, 1], 'color': "#90caf9"}
                            ]
                        }
                    ))
                    fig_subjectivity.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
                    st.plotly_chart(fig_subjectivity, use_container_width=True)
                
                # Success message with modern styling
                st.success(f"✅ Analysis completed at {datetime.now().strftime('%H:%M:%S')}")
    
    elif analyze_button and not user_text.strip():
        st.warning("⚠️ Please enter some text to analyze!")
    
    # Modern analytics dashboard
    if 'show_history' in st.session_state and st.session_state.show_history:
        st.markdown("### 📈 Analytics Dashboard")
        
        if 'analysis_history' in st.session_state and st.session_state.analysis_history:
            history = st.session_state.analysis_history[-20:]
            polarities = [entry['polarity'] for entry in history]
            
            # Modern interactive charts with Plotly
            col1, col2 = st.columns(2)
            
            with col1:
                # Trend line chart
                fig_trend = px.line(
                    x=range(len(polarities)), 
                    y=polarities,
                    title="Sentiment Trend",
                    labels={'x': 'Analysis #', 'y': 'Polarity Score'}
                )
                fig_trend.add_hline(y=0, line_dash="dash", line_color="gray")
                fig_trend.update_layout(height=400)
                st.plotly_chart(fig_trend, use_container_width=True)
            
            with col2:
                # Distribution pie chart
                positive = sum(1 for p in polarities if p > 0.1)
                negative = sum(1 for p in polarities if p < -0.1)
                neutral = len(polarities) - positive - negative
                
                fig_pie = px.pie(
                    values=[positive, neutral, negative],
                    names=['Positive', 'Neutral', 'Negative'],
                    title="Sentiment Distribution",
                    color_discrete_sequence=['#4CAF50', '#FF9800', '#f44336']
                )
                fig_pie.update_layout(height=400)
                st.plotly_chart(fig_pie, use_container_width=True)
            
            # Summary metrics
            avg_polarity = np.mean(polarities)
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("📊 Total", len(st.session_state.analysis_history))
            with col2:
                st.metric("📈 Avg Polarity", f"{avg_polarity:.3f}")
            with col3:
                st.metric("😊 Positive", f"{positive/len(polarities)*100:.1f}%")
            with col4:
                st.metric("😞 Negative", f"{negative/len(polarities)*100:.1f}%")
            
            # Recent history with modern styling
            st.markdown("#### 📋 Recent Analyses")
            history_df = pd.DataFrame(history).tail(10)
            history_df['timestamp'] = pd.to_datetime(history_df['timestamp']).dt.strftime('%m-%d %H:%M')
            st.dataframe(
                history_df[['timestamp', 'text', 'sentiment', 'polarity', 'subjectivity']], 
                use_container_width=True,
                hide_index=True
            )
        
        if st.button("❌ Close Analytics", use_container_width=True):
            st.session_state.show_history = False
            st.rerun()

if __name__ == "__main__":
    main()
