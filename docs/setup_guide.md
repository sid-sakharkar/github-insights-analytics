# Setup Guide for GitHub Insights Analytics

## Prerequisites
Before you start, ensure you have the following installed:
- **Git** (version 2.25 or higher)
- **Node.js** (version 14 or higher)
- **npm** (Node Package Manager, comes with Node.js)

## Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sid-sakharkar/github-insights-analytics.git
   cd github-insights-analytics
   ```

2. **Install Dependencies**:
   Run the following command to install the required packages:
   ```bash
   npm install
   ```

3. **Build the Project**:
   After installing the dependencies, build the project:
   ```bash
   npm run build
   ```

4. **Run the Application**:
   Start the application with:
   ```bash
   npm start
   ```

## Configuration
- **Environment Variables**: Create a `.env` file in the root directory with the following variables:
  ```
  API_KEY=your_api_key_here
  DATABASE_URL=your_database_url_here
  ```

- **Modify Configurations**: Adjust `config.js` as needed to fit your environment settings.

## Troubleshooting
- If you encounter issues, check the following:
  - Ensure all dependencies are correctly installed.
  - Verify your environment variables are set up correctly.

For further assistance, refer to the **Issues** section of the repository or contact support.