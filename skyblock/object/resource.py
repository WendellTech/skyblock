from typing import Optional

from ..function.io import red
from ..function.util import get, includes

from .object import ItemType, Crop, Mineral, Tree

__all__ = ['RESOURCES', 'get_resource']


RESOURCES = [
    Crop('wheat', drop='wheat', amount=1, farming_exp=4),
    Crop('potato', drop='potato', amount=1, farming_exp=4),
    Crop('carrot', drop='carrot', amount=1, farming_exp=4),
    Crop('melon', drop='melon', amount=(3, 7), farming_exp=4),
    Crop('pumpkin', drop='pumpkin', amount=1, farming_exp=4.5),
    Crop('cactus', drop='cactus', amount=(5, 15), farming_exp=2),
    Crop('sugar_cane', drop='sugar_cane', amount=(3, 5), farming_exp=2),
    Crop('cocoa', drop='cocoa', amount=(2, 3), farming_exp=4),
    Crop('mushroom', drop='mushroom', amount=1, farming_exp=3),

    Mineral('stone', drop='cobblestone', amount=1, breaking_power=1,
            hardness=1, exp=0, mining_exp=1),
    Mineral('gravel', drop='gravel', amount=1, breaking_power=0,
            hardness=0.6, exp=0, mining_exp=4),
    Mineral('coal_ore', drop='coal', amount=1, breaking_power=1,
            hardness=3, exp=1, mining_exp=5),
    Mineral('iron_ore', drop='iron', amount=1, breaking_power=2,
            hardness=3, exp=0, mining_exp=5),
    Mineral('gold_ore', drop='gold', amount=1, breaking_power=3,
            hardness=3, exp=0, mining_exp=6),
    Mineral('lapis_ore', drop='lapis', amount=(4, 9), breaking_power=2,
            hardness=3, exp=(2, 5), mining_exp=7),
    Mineral('redstone_ore', drop='redstone', amount=(4, 5), breaking_power=3,
            hardness=3, exp=(1, 5), mining_exp=7),
    Mineral('emerald_ore', drop='emerald', amount=1, breaking_power=3,
            hardness=3, exp=(3, 7), mining_exp=9),
    Mineral('diamond_ore', drop='diamond', amount=1, breaking_power=3,
            hardness=3, exp=(3, 7), mining_exp=10),
    Mineral('diamond_block', drop='diamond', amount=9, breaking_power=3,
            hardness=5, exp=0, mining_exp=15),
    Mineral('obsidian', drop='obsidian', amount=1, breaking_power=4,
            hardness=50, exp=0, mining_exp=20),
    Mineral('end_stone', drop='end_stone', amount=1, breaking_power=1,
            hardness=3, exp=0, mining_exp=3),
    Mineral('sand', drop='sand', amount=1, breaking_power=0,
            hardness=0.5, exp=0, mining_exp=3),

    Tree('oak', 'oak_wood',
         hardness=2, foraging_exp=6),
    Tree('birch', 'birch_wood',
         hardness=2, foraging_exp=6),
    Tree('spruce', 'spruce_wood',
         hardness=2, foraging_exp=6),
    Tree('dark_oak', 'dark_oak_wood',
         hardness=2, foraging_exp=6),
    Tree('acacia', 'acacia_wood',
         hardness=2, foraging_exp=6),
    Tree('jungle', 'jungle_wood',
         hardness=2, foraging_exp=6),
]


def get_resource(name: str, **kwargs) -> Optional[ItemType]:
    if not includes(RESOURCES, name):
        red(f'Invalid resource: {name!r}')
        return
    return get(RESOURCES, name, **kwargs)
