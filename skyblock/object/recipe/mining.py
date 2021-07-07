from skyblock.object.item_wrapper import item_type
from ..item import get_item, get_scroll
from ..object import Item, Recipe, EnchantedBook


__all__ = ['MINING_RECIPES']

MINING_RECIPES = [
    Recipe('wooden_pickaxe', 'mining',
           [(Item('planks'), 3),
            (Item('stick'), 2)],
           (get_item('wooden_pickaxe'), 1)),
    Recipe('gold_pickaxe', 'mining',
           [(Item('gold'), 3),
            (Item('stick'), 2)],
           (get_item('golden_pickaxe'), 1)),
    Recipe('stone_pickaxe', 'mining',
           [(Item('cobblestone'), 3),
            (Item('stick'), 2)],
           (get_item('stone_pickaxe'), 1)),
    Recipe('iron_pickaxe', 'mining',
           [(Item('iron'), 3),
            (Item('stick'), 2)],
           (get_item('iron_pickaxe'), 1)),
    Recipe('diamond_pickaxe', 'mining',
           [(Item('diamond'), 3),
            (Item('stick'), 2)],
           (get_item('diamond_pickaxe'), 1)),

    Recipe('coal_to_block', 'mining',
           [(Item('coal'), 9)],
           (Item('coal_block'), 1)),
    Recipe('block_to_coal', 'mining',
           [(Item('coal_block'), 1)],
           (Item('coal'), 9)),

    Recipe('iron_to_block', 'mining',
           [(Item('iron'), 9)],
           (Item('iron_block'), 1)),
    Recipe('block_to_iron', 'mining',
           [(Item('iron_block'), 1)],
           (Item('iron'), 9)),
    Recipe('nugget_to_iron', 'mining',
           [(Item('iron_nugget'), 9)],
           (Item('iron'), 1)),
    Recipe('iron_to_nugget', 'mining',
           [(Item('iron'), 1)],
           (Item('iron_nugget'), 9)),

    Recipe('gold_to_block', 'mining',
           [(Item('gold'), 9)],
           (Item('gold_block'), 1)),
    Recipe('block_to_gold', 'mining',
           [(Item('gold_block'), 1)],
           (Item('gold'), 9)),
    Recipe('nugget_to_gold', 'mining',
           [(Item('gold_nugget'), 9)],
           (Item('gold'), 1)),
    Recipe('gold_to_nugget', 'mining',
           [(Item('gold'), 1)],
           (Item('gold_nugget'), 9)),
    Recipe('golden_apple', 'mining',
           [(Item('gold'), 8),
            (Item('apple'), 1)],
           (Item('golden_apple'), 1)),
    Recipe('enchanted_golden_apple', 'mining',
           [(Item('gold_block'), 8),
            (Item('apple'), 1)],
           (Item('enchanted_golden_apple'), 1)),

    Recipe('diamond_to_block', 'mining',
           [(Item('diamond'), 9)],
           (Item('diamond_block'), 1)),
    Recipe('block_to_diamond', 'mining',
           [(Item('diamond_block'), 1)],
           (Item('diamond'), 9)),

    Recipe('lapis_to_block', 'mining',
           [(Item('lapis'), 9)],
           (Item('lapis_block'), 1)),
    Recipe('block_to_lapis', 'mining',
           [(Item('lapis_block'), 1)],
           (Item('lapis'), 9)),

    Recipe('emerald_to_block', 'mining',
           [(Item('emerald'), 9)],
           (Item('emerald_block'), 1)),
    Recipe('block_to_emerald', 'mining',
           [(Item('emerald_block'), 1)],
           (Item('emerald'), 9)),

    Recipe('redstone_to_block', 'mining',
           [(Item('redstone'), 9)],
           (Item('redstone_block'), 1)),
    Recipe('block_to_redstone', 'mining',
           [(Item('redstone_block'), 1)],
           (Item('redstone'), 9)),

    Recipe('glowstone_to_block', 'mining',
           [(Item('glowstone'), 4)],
           (Item('glowstone_block'), 1)),

    Recipe('cobblestone_to_enchanted', 'mining',
           [(Item('cobblestone'), 160)],
           (Item('enchanted_cobblestone'), 1),
           collection_req=('cobblestone', 4)),

    Recipe('uncommon_silverfish_pet', 'mining',
           [(Item('enchanted_cobblestone'), 64),
            (Item('enchanted_egg'), 1)],
           (get_item('silverfish_pet', rarity='uncommon'), 1),
           collection_req=('cobblestone', 6)),
    Recipe('epic_silverfish_pet', 'mining',
           [(Item('enchanted_cobblestone'), 64),
            (Item('super_enchanted_egg'), 1)],
           (get_item('silverfish_pet', rarity='epic'), 1),
           collection_req=('cobblestone', 6)),
    Recipe('miners_outfit_helmet', 'mining',
           [(Item('enchanted_cobblestone'), 5)],
           (get_item('miners_outfit_helmet'), 1),
           collection_req=('cobblestone', 7)),
    Recipe('miners_outfit_chestplate', 'mining',
           [(Item('enchanted_cobblestone'), 8)],
           (get_item('miners_outfit_chestplate'), 1),
           collection_req=('cobblestone', 7)),
    Recipe('miners_outfit_leggings', 'mining',
           [(Item('enchanted_cobblestone'), 7)],
           (get_item('miners_outfit_leggings'), 1),
           collection_req=('cobblestone', 7)),
    Recipe('miners_outfit_boots', 'mining',
           [(Item('enchanted_cobblestone'), 4)],
           (get_item('miners_outfit_boots'), 1),
           collection_req=('cobblestone', 7)),

    Recipe('coal_to_enchanted', 'mining',
           [(Item('coal'), 160)],
           (Item('enchanted_coal'), 1),
           collection_req=('coal', 4)),
    Recipe('scroll_to_gold', 'mining',
           [(Item('enchanted_ender_pearl'), 16),
            (Item('enchanted_iron'), 48),
            (Item('enchanted_gold'), 80)],
           (get_scroll('gold'), 1),
           collection_req=('coal', 6)),
    Recipe('coal_to_enchanted_block', 'mining',
           [(Item('enchanted_coal'), 160)],
           (Item('enchanted_coal_block'), 1),
           collection_req=('coal', 7)),
    Recipe('epic_wither_skeleton_pet', 'mining',
           [(Item('enchanted_coal_block'), 8),
            (Item('super_enchanted_egg'), 1)],
           (get_item('wither_skeleton_pet', rarity='epic'), 1),
           collection_req=('coal', 9)),

    Recipe('golem_hat', 'mining',
           [(Item('iron'), 40)],
           (get_item('golem_hat'), 1),
           collection_req=('iron', 2)),
    Recipe('protection_book', 'mining',
           [(Item('paper'), 24),
            (Item('iron'), 8)],
           (EnchantedBook(enchantments={'protection': 4}), 1),
           collection_req=('iron', 3)),
    Recipe('iron_to_enchanted', 'mining',
           [(Item('iron'), 160)],
           (Item('enchanted_iron'), 1),
           collection_req=('iron', 4)),

    Recipe('golem_armor_helmet', 'mining',
           [(Item('enchanted_iron'), 50)],
           (get_item('golem_armor_helmet'), 1),
           collection_req=('iron', 6)),
    Recipe('golem_armor_chestplate', 'mining',
           [(Item('enchanted_iron'), 80)],
           (get_item('golem_armor_chestplate'), 1),
           collection_req=('iron', 6)),
    Recipe('golem_armor_leggings', 'mining',
           [(Item('enchanted_iron'), 70)],
           (get_item('golem_armor_leggings'), 1),
           collection_req=('iron', 6)),
    Recipe('golem_armor_boots', 'mining',
           [(Item('enchanted_iron'), 40)],
           (get_item('golem_armor_boots'), 1),
           collection_req=('iron', 6)),

    Recipe('iron_to_enchanted_block', 'mining',
           [(Item('enchanted_iron'), 160)],
           (Item('enchanted_iron_block'), 1),
           collection_req=('iron', 7)),
    Recipe('golem_sword', 'mining',
           [(Item('enchanted_iron_block'), 2),
            (Item('stick'), 1)],
           (get_item('golem_sword'), 1),
           collection_req=('iron', 8)),

    Recipe('cleaver', 'mining',
           [(Item('gold'), 4),
            (Item('stick'), 2)],
           (get_item('cleaver'), 1),
           collection_req=('gold', 2)),
    Recipe('looting_book', 'mining',
           [(Item('paper'), 6),
            (Item('gold_block'), 4)],
           (EnchantedBook(enchantments={'looting': 2}), 1),
           collection_req=('gold', 3)),
    Recipe('gold_to_enchanted', 'mining',
           [(Item('gold'), 160)],
           (Item('enchanted_gold'), 1),
           collection_req=('gold', 4)),
    Recipe('scavenger_book', 'mining',
           [(Item('paper'), 6),
            (Item('gold_sword'), 1)],
           (EnchantedBook(enchantments={'scavenger': 2}), 1),
           collection_req=('gold', 6)),
    Recipe('gold_to_enchanted_block', 'mining',
           [(Item('enchanted_gold'), 160)],
           (Item('enchanted_gold_block'), 1),
           collection_req=('gold', 7)),
    Recipe('fortune_book', 'mining',
           [(Item('paper'), 6),
            (Item('enchanted_gold'), 2)],
           (EnchantedBook(enchantments={'fortune': 2}), 1),
           collection_req=('gold', 8)),

    Recipe('execute_book', 'mining',
           [(Item('paper'), 24),
            (Item('diamond'), 40),
            (Item('flint'), 40)],
           (EnchantedBook(enchantments={'execute': 4}), 1),
           collection_req=('diamond', 2)),
    Recipe('diamond_to_enchanted', 'mining',
           [(Item('diamond'), 160)],
           (Item('enchanted_diamond'), 1),
           collection_req=('diamond', 4)),
    Recipe('critical_book', 'mining',
           [(Item('paper'), 24),
            (Item('enchanted_diamond'), 8)],
           (EnchantedBook(enchantments={'critical': 4}), 1),
           collection_req=('diamond', 5)),

    Recipe('hardened_diamond_helmet', 'mining',
           [(Item('enchanted_diamond'), 5)],
           (get_item('hardened_diamond_helmet'), 1),
           collection_req=('diamond', 7)),
    Recipe('hardened_diamond_chestplate', 'mining',
           [(Item('enchanted_diamond'), 8)],
           (get_item('hardened_diamond_chestplate'), 1),
           collection_req=('diamond', 7)),
    Recipe('hardened_diamond_leggings', 'mining',
           [(Item('enchanted_diamond'), 7)],
           (get_item('hardened_diamond_leggings'), 1),
           collection_req=('diamond', 7)),
    Recipe('hardened_diamond_boots', 'mining',
           [(Item('enchanted_diamond'), 4)],
           (get_item('hardened_diamond_boots'), 1),
           collection_req=('diamond', 7)),

    Recipe('diamond_to_enchanted_block', 'mining',
           [(Item('enchanted_diamond'), 160)],
           (Item('enchanted_diamond_block'), 1),
           collection_req=('diamond', 8)),

    Recipe('perfect_helmet', 'mining',
           [(Item('enchanted_diamond_block'), 5)],
           (get_item('perfect_helmet'), 1),
           collection_req=('diamond', 9)),
    Recipe('perfect_chestplate', 'mining',
           [(Item('enchanted_diamond_block'), 8)],
           (get_item('perfect_chestplate'), 1),
           collection_req=('diamond', 9)),
    Recipe('perfect_leggings', 'mining',
           [(Item('enchanted_diamond_block'), 7)],
           (get_item('perfect_leggings'), 1),
           collection_req=('diamond', 9)),
    Recipe('perfect_boots', 'mining',
           [(Item('enchanted_diamond_block'), 4)],
           (get_item('perfect_boots'), 1),
           collection_req=('diamond', 9)),

    Recipe('experience_bottle', 'mining',
           [(Item('lapis'), 6),
            (Item('bottle'), 1)],
           (Item('experience_bottle'), 1),
           collection_req=('lapis', 2)),
    Recipe('experience_book', 'mining',
           [(Item('paper'), 6),
            (Item('lapis'), 2)],
           (EnchantedBook(enchantments={'experience': 2}), 1),
           collection_req=('lapis', 3)),
    Recipe('lapis_to_enchanted', 'mining',
           [(Item('lapis'), 160)],
           (Item('enchanted_lapis'), 1),
           collection_req=('lapis', 4)),
    Recipe('grand_experience_bottle', 'mining',
           [(Item('enchanted_lapis'), 6),
            (Item('bottle'), 1)],
           (Item('grand_experience_bottle'), 1),
           collection_req=('lapis', 5)),
    Recipe('lapis_to_enchanted_block', 'mining',
           [(Item('enchanted_lapis'), 160)],
           (Item('enchanted_lapis_block'), 1),
           collection_req=('lapis', 7)),
    Recipe('titanic_experience_bottle', 'mining',
           [(Item('enchanted_lapis_block'), 6),
            (Item('bottle'), 1)],
           (Item('titanic_experience_bottle'), 1),
           collection_req=('lapis', 8)),

    Recipe('emerald_to_enchanted', 'mining',
           [(Item('emerald'), 160)],
           (Item('enchanted_emerald'), 1),
           collection_req=('emerald', 4)),
    Recipe('emerald_to_enchanted_block', 'mining',
           [(Item('enchanted_emerald'), 160)],
           (Item('enchanted_emerald_block'), 1),
           collection_req=('emerald', 7)),
    Recipe('emerald_blade', 'mining',
           [(Item('enchanted_emerald_block'), 2),
            (Item('stick'), 1)],
           (get_item('emerald_blade'), 1),
           collection_req=('emerald', 8)),

    Recipe('emerald_helmet', 'mining',
           [(Item('enchanted_emerald_block'), 5)],
           (get_item('emerald_helmet'), 1),
           collection_req=('emerald', 9)),
    Recipe('emerald_chestplate', 'mining',
           [(Item('enchanted_emerald_block'), 8)],
           (get_item('emerald_chestplate'), 1),
           collection_req=('emerald', 9)),
    Recipe('emerald_leggings', 'mining',
           [(Item('enchanted_emerald_block'), 7)],
           (get_item('emerald_leggings'), 1),
           collection_req=('emerald', 9)),
    Recipe('emerald_boots', 'mining',
           [(Item('enchanted_emerald_block'), 4)],
           (get_item('emerald_boots'), 1),
           collection_req=('emerald', 9)),

    Recipe('efficiency_book', 'mining',
           [(Item('paper'), 24),
            (Item('redstone'), 8)],
           (EnchantedBook(enchantments={'efficiency': 4}), 1),
           collection_req=('redstone', 3)),
    Recipe('redstone_to_enchanted', 'mining',
           [(Item('redstone'), 160)],
           (Item('enchanted_redstone'), 1),
           collection_req=('redstone', 4)),
    Recipe('scroll_to_deep', 'mining',
           [(Item('enchanted_ender_pearl'), 16),
            (Item('enchanted_redstone'), 48),
            (Item('enchanted_lapis'), 80)],
           (get_scroll('deep'), 1),
           collection_req=('redstone', 7)),
    Recipe('redstone_to_enchanted_block', 'mining',
           [(Item('enchanted_redstone'), 160)],
           (Item('enchanted_redstone_block'), 1),
           collection_req=('redstone', 8)),

    Recipe('quartz_to_enchanted', 'mining',
           [(Item('quartz'), 160)],
           (Item('enchanted_quartz'), 1),
           collection_req=('quartz', 4)),
    Recipe('quartz_to_enchanted_block', 'mining',
           [(Item('enchanted_quartz'), 160)],
           (Item('enchanted_quartz_block'), 1),
           collection_req=('quartz', 6)),

    Recipe('lethality_book', 'mining',
           [(Item('paper'), 24),
            (Item('obsidian'), 24)],
           (EnchantedBook(enchantments={'lethality': 4}), 1),
           collection_req=('obsidian', 2)),
    Recipe('obsidian_to_enchanted', 'mining',
           [(Item('obsidian'), 160)],
           (Item('enchanted_obsidian'), 1),
           collection_req=('obsidian', 4)),
    Recipe('treecapitator', 'mining',
           [(Item('jungle_axe'), 1),
            (Item('enchanted_obsidian'), 512)],
           (get_item('treecapitator'), 1),
           collection_req=('obsidian', 8)),

    Recipe('glowstone_to_enchanted', 'mining',
           [(Item('glowstone'), 160)],
           (Item('enchanted_glowstone'), 1),
           collection_req=('glowstone', 4)),
    Recipe('glowstone_to_enchanted_block', 'mining',
           [(Item('enchanted_glowstone'), 192)],
           (Item('enchanted_glowstone_block'), 1),
           collection_req=('glowstone', 6)),
    Recipe('glowstone_to_enchanted_lamp', 'mining',
           [(Item('enchanted_redstone'), 32),
            (Item('enchanted_glowstone'), 128)],
           (Item('enchanted_redstone_lamp'), 1),
           collection_req=('glowstone', 7)),

    Recipe('sharpness_book', 'mining',
           [(Item('paper'), 24),
            (Item('gravel'), 8),
            (Item('iron_sword'), 1)],
           (EnchantedBook(enchantments={'sharpness': 4}), 1),
           collection_req=('gravel', 4)),
    Recipe('gravel_to_enchanted', 'mining',
           [(Item('gravel'), 160)],
           (Item('enchanted_flint'), 1),
           collection_req=('gravel', 5)),
    Recipe('first_strike_book', 'mining',
           [(Item('paper'), 12),
            (Item('enchanted_flint'), 4),
            (Item('iron_sword'), 1)],
           (EnchantedBook(enchantments={'first_strike': 3}), 1),
           collection_req=('gravel', 6)),
    Recipe('scroll_to_spider', 'mining',
           [(Item('enchanted_ender_pearl'), 16),
            (Item('enchanted_flint'), 128)],
           (get_scroll('spider'), 1),
           collection_req=('gravel', 8)),

    Recipe('ice_to_packed', 'mining',
           [(Item('ice'), 160)],
           (Item('packed_ice'), 1),
           collection_req=('ice', 3)),
    Recipe('ice_to_enchanted', 'mining',
           [(Item('ice'), 160)],
           (Item('enchanted_ice'), 1),
           collection_req=('ice', 4)),
    Recipe('ice_bait', 'mining',
           [(Item('ice'), 1),
            (Item('fish'), 1)],
           (Item('ice_bait'), 1),
           collection_req=('ice', 6)),
    Recipe('ice_to_enchanted_packed', 'mining',
           [(Item('enchanted_ice'), 192)],
           (Item('enchanted_packed_ice'), 1),
           collection_req=('ice', 7)),
    Recipe('frozen_scythe', 'mining',
           [(Item('enchanted_packed_ice'), 64),
            (Item('stick'), 2)],
           (get_item('frozen_scythe'), 1),
           collection_req=('ice', 8)),

    Recipe('frozen_blaze_helmet', 'mining',
           [(Item('enchanted_packed_ice'), 64),
            (get_item('blaze_helmet'), 1)],
           (get_item('emerald_helmet'), 1),
           collection_req=('ice', 9)),
    Recipe('frozen_blaze_chestplate', 'mining',
           [(Item('enchanted_packed_ice'), 64),
            (get_item('blaze_chestplate'), 1)],
           (get_item('emerald_chestplate'), 1),
           collection_req=('ice', 9)),
    Recipe('frozen_blaze_leggings', 'mining',
           [(Item('enchanted_packed_ice'), 64),
            (get_item('blaze_leggings'), 1)],
           (get_item('emerald_leggings'), 1),
           collection_req=('ice', 9)),
    Recipe('frozen_blaze_boots', 'mining',
           [(Item('enchanted_packed_ice'), 64),
            (get_item('blaze_boots'), 1)],
           (get_item('emerald_boots'), 1),
           collection_req=('ice', 9)),

    Recipe('netherrack_to_enchanted', 'mining',
           [(Item('netherrack'), 160)],
           (Item('enchanted_netherrack'), 1),
           collection_req=('netherrack', 4)),

    Recipe('sand_to_enchanted', 'mining',
           [(Item('sand'), 160)],
           (Item('enchanted_sand'), 1),
           collection_req=('sand', 5)),

    Recipe('end_stone_to_enchanted', 'mining',
           [(Item('end_stone'), 160)],
           (Item('enchanted_end_stone'), 1),
           collection_req=('end_stone', 4)),
    Recipe('uncommon_endermite_pet', 'mining',
           [(Item('enchanted_end_stone'), 512),
            (Item('enchanted_egg'), 1)],
           (get_item('endermite_pet', rarity='uncommon'), 1),
           collection_req=('end_stone', 7)),
    Recipe('epic_endermite_pet', 'mining',
           [(Item('enchanted_end_stone'), 512),
            (Item('super_enchanted_egg'), 1)],
           (get_item('endermite_pet', rarity='epic'), 1),
           collection_req=('end_stone', 7)),
    Recipe('scroll_to_end', 'mining',
           [(Item('enchanted_ender_pearl'), 16),
            (Item('enchanted_obsidian'), 48),
            (Item('enchanted_end_stone'), 80)],
           (get_scroll('end'), 1),
           collection_req=('end_stone', 8)),
    Recipe('end_stone_sword', 'mining',
           [(Item('enchanted_end_stone'), 128),
            (Item('stick'), 1)],
           (get_item('end_stone_sword'), 1),
           collection_req=('end_stone', 10)),

    Recipe('mithril_to_enchanted', 'mining',
           [(Item('mithril'), 160)],
           (Item('enchanted_mithril'), 1),
           collection_req=('mithril', 3)),
    Recipe('mithril_coat', 'mining',
           [(Item('enchanted_mithril'), 32)],
           (get_item('mithril_coat'), 1),
           collection_req=('mithril', 5)),
    Recipe('uncommon_mithril_golem_pet', 'mining',
           [(Item('enchanted_cobblestone'), 64),
            (Item('enchanted_egg'), 1)],
           (get_item('mithril_golem_pet', rarity='uncommon'), 1),
           collection_req=('mithril', 7)),
    Recipe('epic_mithril_golem_pet', 'mining',
           [(Item('enchanted_cobblestone'), 64),
            (Item('super_enchanted_egg'), 1)],
           (get_item('mithril_golem_pet', rarity='epic'), 1),
           collection_req=('mithril', 7)),

    Recipe('titanium_to_enchanted', 'mining',
           [(Item('titanium'), 160)],
           (Item('enchanted_titanium'), 1)),

    Recipe('sorrow_helmet', 'mining',
           [(Item('sorrow'), 15)],
           (get_item('sorrow_helmet'), 1)),
    Recipe('sorrow_chestplate', 'mining',
           [(Item('sorrow'), 24)],
           (get_item('sorrow_chestplate'), 1)),
    Recipe('sorrow_leggings', 'mining',
           [(Item('sorrow'), 21)],
           (get_item('sorrow_leggings'), 1)),
    Recipe('sorrow_boots', 'mining',
           [(Item('sorrow'), 12)],
           (get_item('sorrow_boots'), 1)),
]
