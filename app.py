import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import json
import os

# Page config
st.set_page_config(
    page_title="🤖 Sentiment Analysis Chatbot",
    page_icon="🤖",
    layout="wide"
)

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
    
    # Title and header
    st.title("🤖 Sentiment Analysis Chatbot")
    st.markdown("---")
    
    # Sidebar for history and settings
    with st.sidebar:
        st.header("📊 Dashboard")
        
        if st.button("📈 View History Chart"):
            if 'analysis_history' in st.session_state and st.session_state.analysis_history:
                st.session_state.show_history = True
            else:
                st.info("No analysis history available!")
        
        if st.button("🗑️ Clear History"):
            st.session_state.analysis_history = []
            if os.path.exists('sentiment_history.json'):
                os.remove('sentiment_history.json')
            st.success("History cleared!")
    
    # Main input section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Text Input")
        user_text = st.text_area(
            "Enter your text for sentiment analysis:",
            height=150,
            placeholder="Type your text here... (reviews, feedback, social media posts, etc.)"
        )
        
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            analyze_button = st.button("🔍 Analyze Sentiment", type="primary")
        
        with col_btn2:
            if st.button("🗑️ Clear Text"):
                st.rerun()
        
        with col_btn3:
            if st.button("📋 Sample Text"):
                st.session_state.sample_text = True
    
    with col2:
        st.subheader("ℹ️ Instructions")
        st.info("""
        **How to use:**
        1. Enter any text in the input area
        2. Click 'Analyze Sentiment'
        3. View detailed results below
        4. Check history in sidebar
        
        **Best for:**
        - Customer reviews
        - Social media posts
        - Feedback analysis
        - Survey responses
        """)
    
    # Sample text functionality
    if 'sample_text' in st.session_state and st.session_state.sample_text:
        sample_texts = [
            "I absolutely love this product! It exceeded my expectations.",
            "This service was terrible and the staff was rude.",
            "The weather forecast indicates rain tomorrow.",
            "I'm feeling okay about this decision, not great but not bad either."
        ]
        selected_sample = st.selectbox("Choose a sample text:", sample_texts)
        if st.button("Use This Sample"):
            st.session_state.selected_sample = selected_sample
            st.session_state.sample_text = False
            st.rerun()
    
    # Use selected sample text
    if 'selected_sample' in st.session_state:
        user_text = st.session_state.selected_sample
        del st.session_state.selected_sample
    
    # Analysis section
    if analyze_button and user_text.strip():
        with st.spinner("🔄 Analyzing sentiment..."):
            polarity, subjectivity, sentiment_label, color = analyzer.analyze_sentiment(user_text)
            
            if polarity is not None:
                # Save to history
                analyzer.save_to_history(user_text, polarity, subjectivity, sentiment_label)
                
                # Get detailed analysis
                details = analyzer.create_detailed_analysis(user_text, polarity, subjectivity, sentiment_label)
                
                st.markdown("---")
                st.subheader("📊 Analysis Results")
                
                # Main results in columns
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
                
                # Detailed breakdown
                st.subheader("🔍 Detailed Breakdown")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**📊 Basic Statistics:**")
                    stats_df = pd.DataFrame({
                        'Metric': ['Word Count', 'Character Count', 'Estimated Sentences'],
                        'Value': [details['word_count'], details['char_count'], details['sentence_count']]
                    })
                    st.dataframe(stats_df, hide_index=True)
                    
                    st.markdown("**🎯 Sentiment Details:**")
                    st.info(f"**Subjectivity Type:** {details['subjectivity_desc']}")
                
                with col2:
                    st.markdown("**💡 Interpretation:**")
                    st.write(f"**Polarity:** {analyzer.interpret_polarity(polarity)}")
                    st.write(f"**Subjectivity:** {analyzer.interpret_subjectivity(subjectivity)}")
                    
                    st.markdown("**📈 Business Insights:**")
                    insights = analyzer.generate_business_insights(polarity, subjectivity)
                    st.success(insights)
                
                # Visualization
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
                
                # Polarity gauge
                ax1.barh(['Polarity'], [polarity], color=color, alpha=0.7)
                ax1.set_xlim(-1, 1)
                ax1.axvline(x=0, color='gray', linestyle='--', alpha=0.7)
                ax1.set_title('Polarity Score', fontweight='bold')
                ax1.set_xlabel('Score')
                
                # Subjectivity gauge
                ax2.barh(['Subjectivity'], [subjectivity], color='#2196F3', alpha=0.7)
                ax2.set_xlim(0, 1)
                ax2.set_title('Subjectivity Score', fontweight='bold')
                ax2.set_xlabel('Score')
                
                plt.tight_layout()
                st.pyplot(fig)
                
                st.success(f"✅ Analysis complete! Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    elif analyze_button and not user_text.strip():
        st.warning("⚠️ Please enter some text to analyze!")
    
    # History chart section
    if 'show_history' in st.session_state and st.session_state.show_history:
        st.markdown("---")
        st.subheader("📈 Sentiment Analysis History")
        
        if 'analysis_history' in st.session_state and st.session_state.analysis_history:
            history = st.session_state.analysis_history[-20:]  # Last 20 entries
            
            # Prepare data
            polarities = [entry['polarity'] for entry in history]
            timestamps = [entry['timestamp'][:10] for entry in history]  # Date only
            
            # Create charts
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
            
            # Polarity trend
            ax1.plot(range(len(polarities)), polarities, 'bo-', linewidth=2, markersize=6)
            ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
            ax1.set_title('Sentiment Polarity Over Time', fontsize=14, fontweight='bold')
            ax1.set_ylabel('Polarity Score')
            ax1.set_xlabel('Analysis Number')
            ax1.grid(True, alpha=0.3)
            ax1.set_ylim(-1.1, 1.1)
            
            # Sentiment distribution
            positive = sum(1 for p in polarities if p > 0.1)
            negative = sum(1 for p in polarities if p < -0.1)
            neutral = len(polarities) - positive - negative
            
            labels = ['Positive', 'Neutral', 'Negative']
            sizes = [positive, neutral, negative]
            colors = ['#4CAF50', '#FF9800', '#f44336']
            
            ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax2.set_title('Sentiment Distribution', fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            
            # Summary statistics
            avg_polarity = np.mean(polarities)
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Total Analyses", len(st.session_state.analysis_history))
            with col2:
                st.metric("Average Polarity", f"{avg_polarity:.3f}")
            with col3:
                st.metric("Positive %", f"{positive/len(polarities)*100:.1f}%")
            with col4:
                st.metric("Negative %", f"{negative/len(polarities)*100:.1f}%")
            
            # Recent history table
            st.subheader("📋 Recent Analysis History")
            history_df = pd.DataFrame(history).tail(10)
            history_df['timestamp'] = pd.to_datetime(history_df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')
            st.dataframe(history_df[['timestamp', 'text', 'sentiment', 'polarity', 'subjectivity']], 
                        use_container_width=True)
        
        if st.button("❌ Close History"):
            st.session_state.show_history = False
            st.rerun()

if __name__ == "__main__":
    main()
