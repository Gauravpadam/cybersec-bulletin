# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY ./package*.json ./

# Install app dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . .

# Build the React app
RUN npm run build

# Expose port 3000
EXPOSE 3000

# Run the app
CMD ["npm", "start"]
