from dataclasses import dataclass


@dataclass
class SearchInput:
    searched_item: str
    image_alt_text: str
    test_description: str