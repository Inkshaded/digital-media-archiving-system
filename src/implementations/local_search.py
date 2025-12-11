import os
from search.search_interface import SearchInterface

class LocalSearch(SearchInterface):
    def search_files(self, directory, query):
        """Return a list of filenames in 'directory' containing 'query'."""
        results = []
        for root, _, files in os.walk(directory):
            for file in files:
                if query.lower() in file.lower():
                    results.append(os.path.join(root, file))
        return results