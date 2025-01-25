import os
import pdfplumber

def find_pdf_file(filename):
    """Searches for the PDF file in the current working directory."""
    current_directory = os.getcwd()  # Get the current working directory
    file_path = os.path.join(current_directory, filename)
    
    if os.path.isfile(file_path):  # Check if the file exists
        return file_path
    else:
        print(f"Error: '{filename}' not found in the current directory.")
        return None

def pdf_to_text(pdf_path, output_txt_path):
    """Converts PDF to text, saving the text to a file."""
    try:
        # Open the PDF file using pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            # Initialize an empty string to hold the extracted text
            full_text = ""
            
            # Iterate over each page in the PDF
            for page_number, page in enumerate(pdf.pages, start=1):
                # Extract text from the page
                text = page.extract_text()
                
                if text:
                    # Handle potential newlines and extra spaces
                    lines = text.split('\n')
                    
                    # Clean up and join the lines with proper newline characters
                    cleaned_text = "\n".join([line.strip() for line in lines if line.strip()])
                    
                    # Add the cleaned text from this page to the full_text
                    full_text += f"Page {page_number}\n" + cleaned_text + "\n\n"
                else:
                    # If no text is extracted, you can add a placeholder
                    full_text += f"Page {page_number} has no extractable text.\n\n"
            
            # Write the extracted text to the output file
            with open(output_txt_path, "w", encoding="utf-8") as output_file:
                output_file.write(full_text)
            
            print(f"PDF text extraction successful. Output written to {output_txt_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    pdf_filename = "PythonWeeklyAssignment_Merged.pdf"
    pdf_path = find_pdf_file(pdf_filename)
    
    if pdf_path:
        # Define output text file path (same as PDF file but with .txt extension)
        output_txt_path = os.path.splitext(pdf_path)[0] + ".txt"
        
        # Convert PDF to text and save the result to the text file
        pdf_to_text(pdf_path, output_txt_path)

# Run the program
if __name__ == "__main__":
    main()
