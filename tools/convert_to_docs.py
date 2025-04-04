#!/usr/bin/env python3
"""
Convert MkDocs markdown files to Microsoft Word and PDF formats.

This script requires pandoc to be installed on your system.
On Ubuntu/Debian: sudo apt-get install pandoc
On macOS: brew install pandoc
On Windows: choco install pandoc

It also requires the pypandoc Python package:
pip install pypandoc
"""

import os
import glob
import shutil
from pathlib import Path
try:
    import pypandoc
except ImportError:
    print("ERROR: pypandoc package is required. Install with: pip install pypandoc")
    exit(1)

# Configure output directories
WORD_OUTPUT_DIR = "exports/word"
PDF_OUTPUT_DIR = "exports/pdf"

def ensure_directory(directory):
    """Create directory if it doesn't exist."""
    os.makedirs(directory, exist_ok=True)

def clean_directory(directory):
    """Remove and recreate directory."""
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

def convert_to_docx(md_file, output_path):
    """Convert markdown file to DOCX format."""
    try:
        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Convert the file
        pypandoc.convert_file(
            md_file,
            'docx',
            outputfile=output_path,
            extra_args=['--extract-media=./media']
        )
        return True
    except Exception as e:
        print(f"Error converting {md_file} to DOCX: {str(e)}")
        return False

def convert_to_pdf(md_file, output_path):
    """Convert markdown file to PDF format."""
    try:
        # Create parent directories if they don't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Convert the file
        pypandoc.convert_file(
            md_file,
            'pdf',
            outputfile=output_path,
            extra_args=['--pdf-engine=xelatex']
        )
        return True
    except Exception as e:
        print(f"Error converting {md_file} to PDF: {str(e)}")
        return False

def merge_markdown_files(directory, output_file):
    """Merge all markdown files in a directory into a single file."""
    # Get all markdown files sorted by filename
    md_files = sorted(glob.glob(f"{directory}/**/*.md", recursive=True))
    
    # Create the output directory if needed
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Merge the files
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write("# Detailed Functional Specification Documentation\n\n")
        
        for md_file in md_files:
            # Add a section title based on the filename
            rel_path = os.path.relpath(md_file, directory)
            section_name = os.path.splitext(os.path.basename(md_file))[0]
            section_name = section_name.replace('-', ' ').title()
            
            # Read and write the file content
            with open(md_file, 'r', encoding='utf-8') as infile:
                content = infile.read()
                
                # Skip the first heading if it's similar to the section name
                lines = content.split('\n')
                if lines and lines[0].startswith('# '):
                    # Keep the original heading instead of our generated one
                    outfile.write(f"{lines[0]}\n\n")
                    content = '\n'.join(lines[1:])
                else:
                    outfile.write(f"## {section_name}\n\n")
                
                outfile.write(content)
                outfile.write("\n\n---\n\n")
    
    print(f"Created merged file: {output_file}")
    return output_file

def main():
    """Convert markdown documentation to Word and PDF formats."""
    # Clean output directories
    clean_directory(WORD_OUTPUT_DIR)
    clean_directory(PDF_OUTPUT_DIR)
    
    print("Step 1: Creating merged markdown file...")
    merged_file = "exports/dfs_documentation.md"
    merge_markdown_files("docs", merged_file)
    
    print("\nStep 2: Converting merged file to DOCX...")
    docx_output = os.path.join(WORD_OUTPUT_DIR, "dfs_documentation.docx")
    if convert_to_docx(merged_file, docx_output):
        print(f"✅ Successfully created: {docx_output}")
    
    print("\nStep 3: Converting merged file to PDF...")
    pdf_output = os.path.join(PDF_OUTPUT_DIR, "dfs_documentation.pdf")
    if convert_to_pdf(merged_file, pdf_output):
        print(f"✅ Successfully created: {pdf_output}")
    
    print("\nStep 4: Converting individual files...")
    # Get all markdown files
    markdown_files = glob.glob("docs/**/*.md", recursive=True)
    
    word_count = 0
    pdf_count = 0
    
    for md_file in markdown_files:
        # Create output paths
        rel_path = os.path.relpath(md_file, "docs")
        word_path = os.path.join(WORD_OUTPUT_DIR, rel_path.replace(".md", ".docx"))
        pdf_path = os.path.join(PDF_OUTPUT_DIR, rel_path.replace(".md", ".pdf"))
        
        # Convert to DOCX
        if convert_to_docx(md_file, word_path):
            word_count += 1
        
        # Convert to PDF
        if convert_to_pdf(md_file, pdf_path):
            pdf_count += 1
    
    print(f"\n✅ Conversion complete!")
    print(f"Successfully converted {word_count} files to DOCX format.")
    print(f"Successfully converted {pdf_count} files to PDF format.")
    print(f"\nWord documents are in: {os.path.abspath(WORD_OUTPUT_DIR)}")
    print(f"PDF documents are in: {os.path.abspath(PDF_OUTPUT_DIR)}")

if __name__ == "__main__":
    main()
