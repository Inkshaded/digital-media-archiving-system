import os

class SearchInterface:
    """
    Interface for searching through previously archived files

    Methods: 
        search_files : Searches through the files stored in directory based on query
    """
    def search_files(self, directory, query) -> list: ...