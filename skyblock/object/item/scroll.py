from ...function.io import red

from ..object import TravelScroll


__all__ = ['TRAVEL_SCROLLS', 'get_scroll']

TRAVEL_SCROLLS = [
    TravelScroll('hub', 'castle', rarity='epic'),
    TravelScroll('hub', 'crypt', rarity='epic'),
    TravelScroll('barn'),
    TravelScroll('desert'),
    TravelScroll('gold'),
    TravelScroll('deep'),
    TravelScroll('mines'),
    TravelScroll('park'),
    TravelScroll('park', 'howl', rarity='epic'),
    TravelScroll('park', 'jungle', rarity='epic'),
    TravelScroll('spider'),
    TravelScroll('spider', 'nest', rarity='epic'),
    TravelScroll('nether'),
    TravelScroll('nether', 'magma', rarity='epic'),
    TravelScroll('end'),
    TravelScroll('end', 'drag', rarity='epic'),
]


def get_scroll(name: str) -> TravelScroll:
    for scroll in TRAVEL_SCROLLS:
        scroll_name = scroll.island if scroll.zone is None else scroll.zone
        if name == scroll_name:
            return scroll
    red(f'Travel Scroll not found: {name!r}')
