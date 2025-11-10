# News Reader Agent

An intelligent AI-powered news aggregation and summarization system built with CrewAI. This agent automatically discovers, analyzes, and curates news articles on any topic, producing professional-grade news briefings with multi-tier summaries and editorial insights.

## Overview

The News Reader Agent is a multi-agent system that simulates a newsroom workflow:
1. **News Hunter** - Discovers and collects relevant articles from diverse sources
2. **Summarizer** - Transforms raw articles into clear, comprehensive summaries
3. **Curator** - Assembles content into a cohesive, publication-ready news briefing

The system uses AI agents to automate the entire news collection and curation pipeline, from web scraping to final editorial output.

### Workflow

```
User Input (Topic) 
    ↓
News Hunter Agent → Searches & Collects Articles → content_harvest.md
    ↓
Summarizer Agent → Generates Multi-Tier Summaries → summary.md
    ↓
Curator Agent → Assembles Final Report → final_report.md
```

## Features

- **Intelligent News Discovery**: Automatically searches and identifies relevant, credible news articles
- **Multi-Tier Summarization**: Creates headline, executive, and comprehensive summaries for different reader needs
- **Web Scraping**: Uses Playwright to handle JavaScript-heavy websites and extract clean content
- **Content Filtering**: Removes low-quality content, duplicates, and non-article pages
- **Editorial Curation**: Produces professional news briefings with context and analysis
- **Source Credibility Scoring**: Evaluates article quality and source reliability
- **Markdown Output**: Generates well-formatted markdown documents for easy reading and sharing

## Prerequisites

- Python 3.13 or higher
- `uv` package manager (recommended) or `pip`
- OpenAI API key
- Serper API key (for web search)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd news-reader-agent
```

### 2. Install Dependencies

Using `uv` (recommended):
```bash
uv sync
```

Or using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Install Playwright Browsers

```bash
uv run playwright install chromium
```

Or:
```bash
python -m playwright install chromium
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root:

```.env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

### 5. Run the agent:

```bash
uv run main.py
```

**Getting API Keys:**
- **OpenAI API Key**: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Serper API Key**: Get from [Serper.dev](https://serper.dev/)

## ⚙️ Configuration

### Agents Configuration

Edit `config/agents.yaml` to customize agent roles, goals, and backstories.

### Tasks Configuration

Edit `config/tasks.yaml` to customize task descriptions, expected outputs, and output file paths.

### Tools Configuration
Edit `tools.py` to add or remove tools for the agents to use.

### Output Directory

By default, outputs are saved to the `output/` directory:
- `output/content_harvest.md` - Collected articles
- `output/summary.md` - Article summaries
- `output/final_report.md` - Final news briefing


## Limitations

- **API Costs**: Uses OpenAI API, which incurs costs based on usage
- **Search Limits**: Serper API has rate limits based on your plan
- **Scraping Speed**: Playwright scraping can be slow for multiple articles
- **Content Quality**: Depends on source article quality and accessibility
- **JavaScript Sites**: Some heavily JavaScript-rendered sites may require additional wait times

## Learning Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Playwright Documentation](https://playwright.dev/python/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Serper API Documentation](https://serper.dev/)

## Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI)
- Web scraping powered by [Playwright](https://playwright.dev/)
- Search powered by [Serper.dev](https://serper.dev/)

## Contact

[bookyle02@gmail.com]

---

