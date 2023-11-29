import PyPDF2

PDF_PATH = "debito.pdf"
PDF_OUT_PATH = "debito_cut.pdf"

A4_WIDTH = 595.275590551181
A4_HEIGHT = 841.8897637795276
A4_RATIO =  A4_WIDTH / A4_HEIGHT

def cut_pdf_page(input_pdf, output_pdf):
    # Open the input PDF file
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Create a PDF writer object to write the cut page
        pdf_writer = PyPDF2.PdfWriter()
        
        # Get the first page from the input PDF
        page = pdf_reader.pages[0]
        
        # Cut the page at the specified height
        box = page.mediabox
        width = box.width
        height = box.height

        cut_height = A4_RATIO * float(width) #this should be a parameter of the function
        
        if cut_height > height or cut_height < 0:
            print("improper cut height.")
            return
        
        cropped_page = page
        cropped_page.mediabox.upper_right = (
            cropped_page.mediabox.right,
            cut_height,
        ) 
        
        pdf_writer.add_page(cropped_page)

        # write to document-output.pdf
        with open(PDF_OUT_PATH, "wb") as fp:
            pdf_writer.write(fp)


cut_pdf_page(PDF_PATH, PDF_OUT_PATH)