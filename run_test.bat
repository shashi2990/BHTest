@echo off
REM Set environment variable (Windows)
set PYTHONPATH=$(pwd)

# Clean up previous Allure reports
echo "Cleaning up old Allure reports..."
rm -rf allure-results allure-report

# Run tests with Allure
echo "Running Pytest with Allure reporting..."
pytest --alluredir=allure-results

# Generate Allure report
echo "Generating Allure report..."
allure generate allure-results --clean -o allure-report

# Serve the report
echo "Serving Allure report..."
allure serve allure-results
