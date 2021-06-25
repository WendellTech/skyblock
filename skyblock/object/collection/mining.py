from ..object import Collection
from ..recipe import get_recipe

__all__ = ['MINING_COLLECTIONS']

MINING_COLLECTIONS = [
    Collection(
        'cobblestone', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('cobblestone_to_enchanted')),
            (2_500, 250),
            (5_000, (get_recipe('uncommon_silverfish_pet'),
                     get_recipe('epic_silverfish_pet'))),
            (10_000, (get_recipe('miners_outfit_helmet'),
                      get_recipe('miners_outfit_chestplate'),
                      get_recipe('miners_outfit_leggings'),
                      get_recipe('miners_outfit_boots'))),
            (25_000, 2_500),
            (40_000, 4_000),
        ],
    ),
    Collection(
        'coal', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('coal_to_enchanted')),
            (2_500, 250),
            (5_000, get_recipe('scroll_to_gold')),
            (10_000, get_recipe('coal_to_enchanted_block')),
            (25_000, 2_500),
            (50_000, get_recipe('epic_wither_skeleton_pet')),
        ],
    ),
    Collection(
        'iron', 'mining',
        [
            (50, 5),
            (100, get_recipe('golem_hat')),
            (250, 25),
            (1_000, get_recipe('iron_to_enchanted')),
            (2_500, 250),
            (5_000, (get_recipe('golem_armor_helmet'),
                     get_recipe('golem_armor_chestplate'),
                     get_recipe('golem_armor_leggings'),
                     get_recipe('golem_armor_boots'))),
            (10_000, get_recipe('iron_to_enchanted_block')),
            (25_000, get_recipe('golem_sword')),
            (50_000, 5_000),
            (100_000, 10_000),
            (200_000, 20_000),
            (400_000, 40_000),
        ],
    ),
    Collection(
        'gold', 'mining',
        [
            (50, 5),
            (100, get_recipe('cleaver')),
            (250, 25),
            (1_000, get_recipe('gold_to_enchanted')),
            (2_500, 250),
            (5_000, 500),
            (10_000, get_recipe('gold_to_enchanted_block')),
            (25_000, 2_500),
            (50_000, 5_000),
        ],
    ),
    Collection(
        'diamond', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('diamond_to_enchanted')),
            (2_500, 250),
            (5_000, 500),
            (10_000, (get_recipe('hardened_diamond_helmet'),
                      get_recipe('hardened_diamond_chestplate'),
                      get_recipe('hardened_diamond_leggings'),
                      get_recipe('hardened_diamond_boots'))),
            (25_000, get_recipe('diamond_to_enchanted_block')),
            (50_000, (get_recipe('perfect_helmet'),
                      get_recipe('perfect_chestplate'),
                      get_recipe('perfect_leggings'),
                      get_recipe('perfect_boots'))),
        ],
    ),
    Collection(
        'lapis', 'mining',
        [
            (250, 25),
            (500, 50),
            (1_000, 100),
            (2_000, get_recipe('lapis_to_enchanted')),
            (10_000, 1_000),
            (25_000, 2_500),
            (50_000, get_recipe('lapis_to_enchanted_block')),
            (100_000, 10_000),
            (150_000, 15_000),
        ],
    ),
    Collection(
        'emerald', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('emerald_to_enchanted')),
            (5_000, 500),
            (15_000, 1_500),
            (30_000, get_recipe('emerald_to_enchanted_block')),
            (50_000, get_recipe('emerald_blade')),
            (100_000, (get_recipe('emerald_helmet'),
                       get_recipe('emerald_chestplate'),
                       get_recipe('emerald_leggings'),
                       get_recipe('emerald_boots'))),
        ],
    ),
    Collection(
        'redstone', 'mining',
        [
            (100, 10),
            (250, 25),
            (750, 75),
            (1_500, get_recipe('redstone_to_enchanted')),
            (3_000, 300),
            (5_000, 500),
            (10_000, get_recipe('scroll_to_deep')),
            (25_000, get_recipe('redstone_to_enchanted_block')),
            (50_000, 5_000),
            (200_000, 20_000),
            (400_000, 40_000),
            (600_000, 60_000),
            (800_000, 80_000),
            (1_000_000, 100_000),
            (1_200_000, 120_000),
            (1_400_000, 140_000),
        ],
    ),
    Collection(
        'quartz', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('quartz_to_enchanted')),
            (2_500, 250),
            (5_000, get_recipe('quartz_to_enchanted_block')),
            (10_000, 1_000),
            (25_000, 2_500),
            (50_000, 5_000),
        ],
    ),
    Collection(
        'obsidian', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('obsidian_to_enchanted')),
            (2_500, 250),
            (5_000, 500),
            (10_000, 1_000),
            (25_000, 2_500),
            (50_000, 5_000),
            (100_000, 10_000),
        ],
    ),
    Collection(
        'glowstone', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('glowstone_to_enchanted')),
            (2_500, 250),
            (5_000, get_recipe('glowstone_to_enchanted_block')),
            (10_000, get_recipe('glowstone_to_enchanted_lamp')),
            (25_000, 2_500),
            (50_000, 5_000),
        ],
    ),
    Collection(
        'gravel', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, 100),
            (2_500, get_recipe('gravel_to_enchanted')),
            (5_000, 500),
            (10_000, 1_000),
            (15_000, get_recipe('scroll_to_spider')),
            (50_000, 5_000),
        ],
    ),
    Collection(
        'ice', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, get_recipe('ice_to_packed')),
            (500, get_recipe('ice_to_enchanted')),
            (1_000, 100),
            (5_000, 500),
            (10_000, get_recipe('ice_to_enchanted_packed')),
            (50_000, get_recipe('frozen_scythe')),
            (100_000, 10_000),
            (250_000, 25_000),
        ],
    ),
    Collection(
        'netherrack', 'mining',
        [
            (50, 5),
            (250, 25),
            (500, 50),
            (1_000, get_recipe('netherrack_to_enchanted')),
            (5_000, 500),
        ],
    ),
    Collection(
        'sand', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (500, 50),
            (1_000, get_recipe('sand_to_enchanted')),
            (2_500, 250),
            (5_000, 500),
        ],
    ),
    Collection(
        'end_stone', 'mining',
        [
            (50, 5),
            (100, 10),
            (250, 25),
            (1_000, get_recipe('end_stone_to_enchanted')),
            (2_500, 250),
            (5_000, 500),
            (10_000, (get_recipe('uncommon_endermite_pet'),
                      get_recipe('epic_endermite_pet'))),
            (15_000, get_recipe('scroll_to_end')),
            (25_000, 2_500),
            (50_000, get_recipe('end_stone_sword')),
        ],
    ),
    Collection(
        'mithril', 'mining',
        [
            (50, 5),
            (250, 25),
            (1_000, get_recipe('mithril_to_enchanted')),
            (2_500, 250),
            (5_000, get_recipe('mithril_coat')),
            (10_000, 1_000),
            (250_000, (get_recipe('uncommon_mithril_golem_pet'),
                       get_recipe('epic_mithril_golem_pet'))),
            (500_000, 50_000),
            (1_000_000, 100_000),
        ],
    ),
]
