import os
from langchain_text_splitters import MarkdownHeaderTextSplitter
import json
from configuration.config import config
from utils.logger import Logger


class MarkdownSplitter:
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on, strip_headers=True
    )
    MD_DIR = config["dirs"]["md_dir"]
    SPLITS_DIR = config["dirs"]["splits_dir"]
    logger = Logger("MarkdownSplitter").logger

    @classmethod
    def split_one_doc(cls, doc: str):
        """
        Split a single Markdown document into chunks.

        :param doc: Markdown content as a string.
        :return: List of split chunks.
        """
        return cls.splitter.split_text(doc)

    @classmethod
    def split_multiple_docs(cls, docs: list[str]):
        if not docs:
            print("No documents provided for splitting.")
            return []

        return [chunk for doc in docs for chunk in cls.split_one_doc(doc)]

    @classmethod
    def locate_and_split_markdown(cls, upload_id: str):
        os.makedirs(cls.MD_DIR, exist_ok=True)

        md_path = os.path.join(cls.MD_DIR, f"{upload_id}.md")
        splits_path = os.path.join(cls.SPLITS_DIR, f"{upload_id}.json")

        if not os.path.exists(md_path):
            print(f"Markdown file not found: {md_path}")
            raise FileNotFoundError(f"Markdown file not found: {md_path}")

        try:
            with open(md_path, "r", encoding="utf-8") as md_file:
                content = md_file.read()
            splits = cls.split_one_doc(content)

            serializable_splits = [
                {"content": chunk.page_content, "metadata": chunk.metadata}
                for chunk in splits
            ]
            with open(splits_path, "w", encoding="utf-8") as json_file:
                json.dump(serializable_splits, json_file, indent=4, ensure_ascii=False)

            cls.logger.info(f"Markdown file split into {len(splits)} chunks.")
            return splits
        except Exception as e:
            cls.logger.error(f"Error splitting markdown file {md_path}: {e}")
            raise
