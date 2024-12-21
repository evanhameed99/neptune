import pymupdf4llm
import pymupdf
import os
from configuration.config import config


class DocTextExtractor:
    PDF_DIR = config["dirs"]["pdf_dir"]
    MD_DIR = config["dirs"]["md_dir"]

    @classmethod
    def parse_doc_as_markdown(cls, content: bytes) -> str:
        """Parse PDF content into Markdown."""
        doc = pymupdf.open(stream=content, filetype="pdf")
        return pymupdf4llm.to_markdown(doc)

    @classmethod
    def save_doc_markdown(cls, upload_id: str):
        """Read PDF content and save as Markdown."""
        pdf_path = os.path.join(cls.PDF_DIR, f"{upload_id}.pdf")
        md_path = os.path.join(cls.MD_DIR, f"{upload_id}.md")

        # Ensure the directories exist
        os.makedirs(cls.PDF_DIR, exist_ok=True)
        os.makedirs(cls.MD_DIR, exist_ok=True)

        try:
            with open(pdf_path, "rb") as pdf_file:
                content = pdf_file.read()

            markdown = cls.parse_doc_as_markdown(content)

            with open(md_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown)

            print(f"Markdown saved: {md_path}")
        except Exception as e:
            print(f"Error processing file {upload_id}: {e}")
            raise
