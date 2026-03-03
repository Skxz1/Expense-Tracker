# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy project config first
# This improves build caching
COPY pyproject.toml /app/pyproject.toml

# Upgrade pip and install project dependencies
RUN pip install --no-cache-dir -U pip \
  && pip install --no-cache-dir .

# Copy application source code
COPY src /app/src

# Expose port used by the server
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "expense_tracker.web.app:app", "--host", "0.0.0.0", "--port", "8000"]