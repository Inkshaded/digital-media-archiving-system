from abc import ABC, abstractmethod

class UserState(ABC):
    """State interface for user permissions."""

    @abstractmethod
    def can_upload(self) -> bool:
        pass
    def can_view_files(self) -> bool:
        pass
    def can_view_logs(self) -> bool:
        pass


class ReaderState(UserState):
    """Reader mode: can browse and search, but not upload."""

    def can_upload(self) -> bool:
        return False

    def can_view_files(self) -> bool:
        return True

    def can_view_logs(self) -> bool:
        return True


class ArchivistState(UserState):
    """Archivist mode: full permissions."""

    def can_upload(self) -> bool:
        return True

    def can_view_files(self) -> bool:
        return True

    def can_view_logs(self) -> bool:
        return True