from services.h3.h3_service import H3Service
from storage.memory_store import MemoryStore
from repository.driver_repository import DriverRepository
from services.h3.matching_service import MatchingService


h3_service = H3Service()
memory_store = MemoryStore()
driver_repository = DriverRepository()


def get_matching_service() -> MatchingService:
    return MatchingService(
        h3_service=h3_service,
        store=memory_store,
        repository=driver_repository
    )
