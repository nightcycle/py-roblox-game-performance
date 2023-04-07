from requests import Session as Session
from typing import TypedDict

GAME_URL_PREFIX: str

def dump_element(element) -> str: ...

class AdIntValueData(TypedDict):
    Current: int
    Total: int

class AdFloatValueData(TypedDict):
    Current: float
    Total: float

class AdData(TypedDict):
    Title: str
    Id: str
    PlaceId: int
    Type: str
    IsRunning: bool
    Clicks: AdIntValueData
    CTR: AdFloatValueData
    Bid: AdIntValueData
    Impressions: AdIntValueData
    CPC: AdFloatValueData

class RatingData(TypedDict):
    Likes: int
    Dislikes: int

class GameData(TypedDict):
    Rating: RatingData
    Favorites: int
    Visits: int
    Concurrents: int

class RecordData(TypedDict):
    Timestamp: str
    PlaceId: int
    Advertisements: list[AdData]
    Game: GameData | None

class PerformanceTracker:
    session: Session
    place_id: int
    universe_id: int
    group_id: int
    def __init__(self, rbx_security_cookie: str, place_id: int, group_id: int) -> None: ...
    def read_ads(self) -> list[AdData]: ...
    def read_concurrents(self) -> int: ...
    def get_game_data(self) -> GameData | None: ...
    def dump(self) -> RecordData: ...
