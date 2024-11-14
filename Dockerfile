# Use Python base image with slim version
FROM python:3.8-slim

# Install necessary packages
RUN pip install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory in the container
RUN mkdir -p /home/doc-bd-a1

# Copy the dataset into the container directory
COPY train_titanic.csv /home/doc-bd-a1/

# Set the default command to open bash
CMD ["/bin/bash"]
