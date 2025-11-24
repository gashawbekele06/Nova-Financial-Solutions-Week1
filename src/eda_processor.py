import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class EDAProcessor:
    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()  # Always work on a copy to avoid modifying original
        self._prepare_date_column()  # Auto-clean date on init

    def publication_frequency(self, top_n: int = 10, show_print: bool = True, figsize=(10, 6)):
      
        if 'publisher' not in self.df.columns:
            raise ValueError("DataFrame must contain a 'publisher' column.") 
        
        # Count articles per publisher
        publisher_counts = self.df['publisher'].value_counts()
        
        if show_print:
            print("\nNumber of articles per publisher:")
            print(publisher_counts)
            
        plt.figure(figsize=figsize)
        sns.barplot(
            x=publisher_counts.index[:top_n],
            y=publisher_counts.values[:top_n],
            hue=publisher_counts.index[:top_n],   
            legend=False,                         
            palette="viridis",                    
            edgecolor="black",                   
        )
        plt.title(f'Top {top_n} Publishers by Article Count')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        return publisher_counts
    
    def _prepare_date_column(self):
        """Internal method: Clean and standardize the 'date' column"""
        if 'date' not in self.df.columns:
            raise ValueError("DataFrame must have a 'date' column")
        
        # Convert to datetime, remove timezone, handle errors
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df = self.df.dropna(subset=['date']).copy()
        self.df['date'] = self.df['date'].dt.tz_localize(None)  # Remove timezone
        
    def plot_daily_trends(self):
        """Plot number of articles published per day"""
        daily_counts = self.df.groupby(self.df['date'].dt.date).size().reset_index(name='article_count')
        daily_counts['date'] = pd.to_datetime(daily_counts['date'])

        plt.figure(figsize=(14, 6))
        sns.lineplot(data=daily_counts, x='date', y='article_count', color='steelblue', linewidth=2)
        plt.title('Articles Published Over Time (Daily)', fontsize=16, fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
    def plot_monthly_trends(self, rolling_window: int = 3):
        """Plot monthly trends with optional rolling average"""
        self.df['month'] = self.df['date'].dt.to_period('M').apply(lambda r: r.start_time)
        monthly_counts = self.df.groupby('month').size().reset_index(name='article_count')
        monthly_counts['rolling_avg'] = monthly_counts['article_count'].rolling(window=rolling_window).mean()

        plt.figure(figsize=(14, 6))
        sns.lineplot(data=monthly_counts, x='month', y='article_count', 
                     label='Monthly Count', color='royalblue', linewidth=2)
        sns.lineplot(data=monthly_counts, x='month', y='rolling_avg', 
                     label=f'{rolling_window}-Month Rolling Average', color='orange', linewidth=2.5)

        plt.title('Articles Published Over Time (Monthly)', fontsize=16, fontweight='bold')
        plt.xlabel('Month')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
    def plot_yearly_trends(self):
        """Plot yearly publication trends"""
        self.df['year'] = self.df['date'].dt.year
        yearly_counts = self.df.groupby('year').size().reset_index(name='article_count')

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=yearly_counts, x='year', y='article_count', 
                     marker='o', markersize=8, color='darkgreen', linewidth=3)
        plt.title('Articles Published Over Time (Yearly)', fontsize=16, fontweight='bold')
        plt.xlabel('Year')
        plt.ylabel('Number of Articles')
        plt.xticks(yearly_counts['year'].astype(int))
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show() 
        
    