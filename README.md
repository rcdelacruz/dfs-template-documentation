# Detailed Functional Specification Documentation

This repository contains a comprehensive guide and template for creating Detailed Functional Specifications (DFS) for software development projects, with a particular focus on outsourcing scenarios.

## Overview

A Detailed Functional Specification (DFS) is a comprehensive document that describes both what a system should do (functional requirements) and how it should be implemented (technical specifications). It serves as a bridge between business requirements and technical implementation.

This documentation is built using MkDocs with the Material theme and includes:

1. **DFS Guide**: General information about DFS documents, when to use them, and how to customize them
2. **Template**: A complete, section-by-section breakdown of the DFS template with guidance
3. **Example**: A sample DFS for a full-stack e-commerce application using NestJS and NextJS

## Running Locally

### Using Docker (Recommended)

The easiest way to run this documentation locally is with Docker:

```bash
# Clone the repository
git clone https://github.com/rcdelacruz/dfs-template-documentation.git

# Navigate to the repository
cd dfs-template-documentation

# Run using the official Material for MkDocs Docker image
docker run --rm -it -p 8000:8000 -v "${PWD}":/docs squidfunk/mkdocs-material serve -a 0.0.0.0:8000
```

Alternative Docker command if you prefer using a Python base image:

```bash
docker run --rm -it -p 8000:8000 -v "${PWD}":/docs -w /docs python:3.9-slim /bin/sh -c "pip install mkdocs mkdocs-material mkdocs-mermaid2-plugin && mkdocs serve -a 0.0.0.0:8000"
```

Then open your browser and navigate to: `http://localhost:8000`

### Using Python

If you prefer to run without Docker:

```bash
# Clone the repository
git clone https://github.com/rcdelacruz/dfs-template-documentation.git

# Navigate to the repository
cd dfs-template-documentation

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install mkdocs mkdocs-material mkdocs-mermaid2-plugin

# Start the MkDocs server
mkdocs serve
```

Then open your browser and navigate to: `http://127.0.0.1:8000`

## Building for Production

To build the static site for production hosting:

```bash
# Using Python
mkdocs build

# Using Docker
docker run --rm -it -v "${PWD}":/docs squidfunk/mkdocs-material build
```

This will create a `site` directory containing the generated static website.

## Repository Structure

```
.
├── docs/                    # Documentation source files
│   ├── guide/               # General guidance on DFS
│   ├── template/            # Template sections with examples
│   ├── example/             # Complete DFS example
│   └── index.md             # Home page
├── mkdocs.yml               # MkDocs configuration
└── README.md                # This file
```

## Customizing for Your Projects

This template is designed to be flexible and adaptable to various project types and sizes. See the Customization guide in the documentation for details on adapting the template to your specific needs.

## Contributing

Contributions to improve the templates, examples, or guidance are welcome! Please feel free to submit a pull request.

## License

This project is open source and available under the MIT License.
