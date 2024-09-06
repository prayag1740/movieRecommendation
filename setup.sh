#!/bin/sh

# Create the .streamlit directory in the correct location
mkdir -p /app/.streamlit

# Write the Streamlit config file
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
" > /app/.streamlit/config.toml
