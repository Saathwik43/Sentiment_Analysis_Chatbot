"""
Sentiment Analysis Chatbot - Easy Level Project
===============================================

A beginner-friendly GUI-based sentiment analysis chatbot using TextBlob and Tkinter.
This project demonstrates basic NLP concepts and GUI development.

Real-world applications:
- Customer feedback analysis
- Social media sentiment monitoring  
- Basic chatbot development
- Text analysis for businesses

Author: Generated for Portfolio Project
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from textblob import TextBlob
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from datetime import datetime
import json
import os

class SentimentAnalysisChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Sentiment Analysis Chatbot")
        self.root.geometry("800x700")
        self.root.configure(bg="#FFFFFF")
        
        # History storage
        self.analysis_history = []
        self.load_history()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🤖 Sentiment Analysis Chatbot", 
            font=('Arial', 20, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(
            input_frame, 
            text="Enter your text:", 
            font=('Arial', 12),
            bg='#f0f0f0'
        ).pack(anchor='w')
        
        self.text_entry = tk.Text(
            input_frame, 
            height=4, 
            width=60,
            font=('Arial', 11),
            wrap=tk.WORD,
            relief='solid',
            bd=1
        )
        self.text_entry.pack(pady=5, fill='x')
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        self.analyze_btn = tk.Button(
            button_frame,
            text="🔍 Analyze Sentiment",
            command=self.analyze_sentiment,
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            relief='raised',
            bd=2,
            width=15
        )
        self.analyze_btn.pack(side='left', padx=5)
        
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_text,
            font=('Arial', 12),
            bg='#f44336',
            fg='white',
            relief='raised',
            bd=2,
            width=10
        )
        self.clear_btn.pack(side='left', padx=5)
        
        self.history_btn = tk.Button(
            button_frame,
            text="📈 View History",
            command=self.show_history_chart,
            font=('Arial', 12),
            bg='#2196F3',
            fg='white',
            relief='raised',
            bd=2,
            width=12
        )
        self.history_btn.pack(side='left', padx=5)
        
        # Results frame
        results_frame = tk.LabelFrame(
            self.root, 
            text="Analysis Results", 
            font=('Arial', 12, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        results_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Results display
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            height=15,
            width=70,
            font=('Arial', 11),
            wrap=tk.WORD,
            state='disabled',
            relief='sunken',
            bd=1
        )
        self.results_text.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to analyze sentiment...")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief='sunken',
            anchor='w',
            bg='#e0e0e0'
        )
        status_bar.pack(side='bottom', fill='x')
        
    def analyze_sentiment(self):
        text = self.text_entry.get(1.0, tk.END).strip()
        
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to analyze!")
            return
            
        try:
            self.status_var.set("Analyzing sentiment...")
            self.root.update()
            
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
                
            # Create detailed analysis
            analysis_result = self.create_detailed_analysis(
                text, polarity, subjectivity, sentiment_label
            )
            
            # Display results
            self.display_results(analysis_result, color)
            
            # Save to history
            self.save_to_history(text, polarity, subjectivity, sentiment_label)
            
            self.status_var.set(f"Analysis complete - Sentiment: {sentiment_label}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Analysis failed: {str(e)}")
            self.status_var.set("Analysis failed")
            
    def create_detailed_analysis(self, text, polarity, subjectivity, sentiment_label):
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
            
        analysis = f"""
📝 TEXT ANALYSIS REPORT
{'='*50}

📊 BASIC STATISTICS:
• Word Count: {word_count}
• Character Count: {char_count}
• Estimated Sentences: {sentence_count}

🎯 SENTIMENT ANALYSIS:
• Overall Sentiment: {sentiment_label}
• Polarity Score: {polarity:.3f} (Range: -1 to +1)
• Sentiment Strength: {strength_desc}

🔍 DETAILED BREAKDOWN:
• Subjectivity: {subjectivity:.3f} (Range: 0 to 1)
• Subjectivity Type: {subjectivity_desc}

💡 INTERPRETATION:
• Polarity: {self.interpret_polarity(polarity)}
• Subjectivity: {self.interpret_subjectivity(subjectivity)}

📈 BUSINESS INSIGHTS:
{self.generate_business_insights(polarity, subjectivity)}

⏰ Analysis Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""
        return analysis
        
    def interpret_polarity(self, polarity):
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
        if subjectivity > 0.7:
            return "Highly subjective - personal opinions and emotions dominate"
        elif subjectivity > 0.4:
            return "Moderately subjective - mix of facts and opinions"
        else:
            return "Objective - primarily factual information"
            
    def generate_business_insights(self, polarity, subjectivity):
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
        
    def display_results(self, analysis_result, color):
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, analysis_result)
        self.results_text.config(state='disabled')
        
    def clear_text(self):
        self.text_entry.delete(1.0, tk.END)
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state='disabled')
        self.status_var.set("Ready to analyze sentiment...")
        
    def save_to_history(self, text, polarity, subjectivity, sentiment_label):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "text": text[:100] + "..." if len(text) > 100 else text,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "sentiment": sentiment_label,
        }
        self.analysis_history.append(entry)
        
        # Keep only last 50 entries
        if len(self.analysis_history) > 50:
            self.analysis_history = self.analysis_history[-50:]
            
        # Save to file
        try:
            with open('sentiment_history.json', 'w') as f:
                json.dump(self.analysis_history, f, indent=2)
        except Exception as e:
            print(f"Failed to save history: {e}")
            
    def load_history(self):
        try:
            if os.path.exists('sentiment_history.json'):
                with open('sentiment_history.json', 'r') as f:
                    self.analysis_history = json.load(f)
        except Exception as e:
            print(f"Failed to load history: {e}")
            self.analysis_history = []
            
    def show_history_chart(self):
        if not self.analysis_history:
            messagebox.showinfo("Info", "No analysis history available!")
            return
            
        # Create chart window
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Sentiment Analysis History")
        chart_window.geometry("800x600")
        
        # Prepare data
        polarities = [entry['polarity'] for entry in self.analysis_history[-20:]]  # Last 20 entries
        timestamps = [entry['timestamp'][-8:-3] for entry in self.analysis_history[-20:]]  # Time only
        
        # Create matplotlib figure
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
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
        
        # Embed plot in tkinter
        canvas = FigureCanvasTkAgg(fig, chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        # Summary statistics
        avg_polarity = np.mean(polarities)
        summary_text = f"""
Summary Statistics:
• Total Analyses: {len(self.analysis_history)}
• Average Polarity: {avg_polarity:.3f}
• Positive: {positive} ({positive/len(polarities)*100:.1f}%)
• Neutral: {neutral} ({neutral/len(polarities)*100:.1f}%)  
• Negative: {negative} ({negative/len(polarities)*100:.1f}%)
        """
        
        summary_label = tk.Label(chart_window, text=summary_text, justify='left', font=('Arial', 10))
        summary_label.pack(pady=10)

def main():
    root = tk.Tk()
    app = SentimentAnalysisChatbot(root)
    root.mainloop()

if __name__ == "__main__":
    main()