from ..object import Armor


__all__ = ['ARMOR_PIECES']

ARMOR_PIECES = [
    Armor('leather_helmet', rarity='common', part='helmet',
          defense=5),
    Armor('leather_chestplate', rarity='common', part='chestplate',
          defense=15),
    Armor('leather_leggings', rarity='common', part='leggings',
          defense=10),
    Armor('leather_boots', rarity='common', part='boots',
          defense=5),

    Armor('golden_helmet', rarity='common', part='helmet',
          defense=10),
    Armor('golden_chestplate', rarity='common', part='chestplate',
          defense=25),
    Armor('golden_leggings', rarity='common', part='leggings',
          defense=15),
    Armor('golden_boots', rarity='common', part='boots',
          defense=5),

    Armor('chainmail_helmet', rarity='uncommon', part='helmet',
          defense=12),
    Armor('chainmail_chestplate', rarity='uncommon', part='chestplate',
          defense=30),
    Armor('chainmail_leggings', rarity='uncommon', part='leggings',
          defense=20),
    Armor('chainmail_boots', rarity='uncommon', part='boots',
          defense=7),

    Armor('iron_helmet', rarity='common', part='helmet',
          defense=10),
    Armor('iron_chestplate', rarity='common', part='chestplate',
          defense=30),
    Armor('iron_leggings', rarity='common', part='leggings',
          defense=25),
    Armor('iron_boots', rarity='common', part='boots',
          defense=10),

    Armor('diamond_helmet', rarity='uncommon', part='helmet',
          defense=15),
    Armor('diamond_chestplate', rarity='uncommon', part='chestplate',
          defense=40),
    Armor('diamond_leggings', rarity='uncommon', part='leggings',
          defense=30),
    Armor('diamond_boots', rarity='uncommon', part='boots',
          defense=15),

    Armor('farm_suit_helmet', rarity='common', part='helmet',
          defense=15,
          abilities=['farm_suit_speed']),
    Armor('farm_suit_chestplate', rarity='common', part='chestplate',
          defense=40,
          abilities=['farm_suit_speed']),
    Armor('farm_suit_leggings', rarity='common', part='leggings',
          defense=30,
          abilities=['farm_suit_speed']),
    Armor('farm_suit_boots', rarity='common', part='boots',
          defense=15,
          abilities=['farm_suit_speed']),

    Armor('farm_helmet', rarity='rare', part='helmet',
          health=20, defense=40,
          abilities=['farm_armor_speed']),
    Armor('farm_chestplate', rarity='rare', part='chestplate',
          health=20, defense=75,
          abilities=['farm_armor_speed']),
    Armor('farm_leggings', rarity='rare', part='leggings',
          health=20, defense=50,
          abilities=['farm_armor_speed']),
    Armor('farm_boots', rarity='rare', part='boots',
          health=20, defense=35,
          abilities=['farm_armor_speed']),

    Armor('pumpkin_helmet', rarity='common', part='helmet',
          health=8, defense=8,
          abilities=['pumpkin_buff']),
    Armor('pumpkin_chestplate', rarity='common', part='chestplate',
          health=14, defense=14,
          abilities=['pumpkin_buff']),
    Armor('pumpkin_leggings', rarity='common', part='leggings',
          health=10, defense=10,
          abilities=['pumpkin_buff']),
    Armor('pumpkin_boots', rarity='common', part='boots',
          health=8, defense=8,
          abilities=['pumpkin_buff']),

    Armor('farmer_boots', rarity='uncommon', part='boots',
          health=40, defense=20, speed=10),
    Armor('ranchers_boots', rarity='rare', part='boots',
          health=100, defense=70, speed=50),

    Armor('mushroom_helmet', rarity='common', part='helmet',
          health=20),
    Armor('mushroom_chestplate', rarity='common', part='chestplate',
          health=10, defense=10),
    Armor('mushroom_leggings', rarity='common', part='leggings',
          health=10, defense=5),
    Armor('mushroom_boots', rarity='common', part='boots',
          health=15),

    Armor('cactus_helmet', rarity='common', part='helmet',
          health=5, defense=10,
          abilities=['deflect']),
    Armor('cactus_chestplate', rarity='common', part='chestplate',
          health=15, defense=25,
          abilities=['deflect']),
    Armor('cactus_leggings', rarity='common', part='leggings',
          health=10, defense=20,
          abilities=['deflect']),
    Armor('cactus_boots', rarity='common', part='boots',
          health=5, defense=10,
          abilities=['deflect']),

    Armor('speedster_helmet', rarity='epic', part='helmet',
          defense=70, speed=15,
          abilities=['speester_bonus']),
    Armor('speedster_chestplate', rarity='epic', part='chestplate',
          defense=120, speed=15,
          abilities=['speester_bonus']),
    Armor('speedster_leggings', rarity='epic', part='leggings',
          defense=95, speed=15,
          abilities=['speester_bonus']),
    Armor('speedster_boots', rarity='epic', part='boots',
          defense=65, speed=15,
          abilities=['speester_bonus']),

    Armor('cow_head', rarity='common', part='helmet',
          health=15, defense=5),

    Armor('miners_outfit_helmet', rarity='uncommon', part='helmet',
          defense=15,
          abilities=['miners_outfit_haste']),
    Armor('miners_outfit_chestplate', rarity='uncommon', part='chestplate',
          defense=40,
          abilities=['miners_outfit_haste']),
    Armor('miners_outfit_leggings', rarity='uncommon', part='leggings',
          defense=30,
          abilities=['miners_outfit_haste']),
    Armor('miners_outfit_boots', rarity='uncommon', part='boots',
          defense=15,
          abilities=['miners_outfit_haste']),

    Armor('golem_hat', rarity='common', part='helmet'),

    Armor('golem_armor_helmet', rarity='rare', part='helmet',
          health=45, defense=45),
    Armor('golem_armor_chestplate', rarity='rare', part='chestplate',
          health=65, defense=90),
    Armor('golem_armor_leggings', rarity='rare', part='leggings',
          health=55, defense=75),
    Armor('golem_armor_boots', rarity='rare', part='boots',
          health=40, defense=40),

    Armor('hardened_diamond_helmet', rarity='rare', part='helmet',
          defense=60),
    Armor('hardened_diamond_chestplate', rarity='rare', part='chestplate',
          defense=120),
    Armor('hardened_diamond_leggings', rarity='rare', part='leggings',
          defense=95),
    Armor('hardened_diamond_boots', rarity='rare', part='boots',
          defense=55),

    Armor('perfect_helmet', rarity='rare', part='helmet',
          defense=110),
    Armor('perfect_chestplate', rarity='rare', part='chestplate',
          defense=160),
    Armor('perfect_leggings', rarity='rare', part='leggings',
          defense=140),
    Armor('perfect_boots', rarity='rare', part='boots',
          defense=500),

    Armor('emerald_helmet', rarity='epic', part='helmet',
          defense=50),
    Armor('emerald_chestplate', rarity='epic', part='chestplate',
          defense=100),
    Armor('emerald_leggings', rarity='epic', part='leggings',
          defense=75),
    Armor('emerald_boots', rarity='epic', part='boots',
          defense=45),

    Armor('frozen_blaze_helmet', rarity='epic', part='helmet',
          strength=40, defense=110, speed=2),
    Armor('frozen_blaze_chestplate', rarity='epic', part='chestplate',
          strength=40, defense=180, speed=2),
    Armor('frozen_blaze_leggings', rarity='epic', part='leggings',
          strength=40, defense=140, speed=2),
    Armor('frozen_blaze_boots', rarity='epic', part='boots',
          strength=40, defense=100, speed=2),

    Armor('mithril_coat', rarity='epic', part='chestplate',
          defense=125, speed=15),

    Armor('zombie_hat', rarity='common', part='helmet',
          defense=10),
    Armor('zombies_heart', rarity='rare', part='helmet',
          health=50),
    Armor('zombie_chestplate', rarity='epic', part='chestplate',
          health=200, defense=40),
    Armor('zombie_leggings', rarity='epic', part='leggings',
          health=160, defense=30),
    Armor('zombie_boots', rarity='epic', part='boots',
          health=120, defense=25),

    Armor('skeleton_hat', rarity='common', part='helmet',
          intelligence=10, speed=2),
    Armor('skeletons_helmet', rarity='rare', part='helmet',
          defense=75),

    Armor('spiders_boots', rarity='rare', part='boots',
          defense=45, intelligence=50, speed=5),
    Armor('spider_hat', rarity='common', part='helmet',
          crit_chance=2),

    Armor('creeper_hat', rarity='common', part='helmet',
          strength=5, crit_chance=5, crit_damage=5,
          health=5, defense=5, intelligence=5),
    Armor('creeper_pants', rarity='rare', part='leggings',
          health=200, defense=65),

    Armor('ghast_head', rarity='common', part='helmet',
          health=100),

    Armor('slime_hat', rarity='common', part='helmet',
          health=50),

    Armor('blaze_hat', rarity='common', part='helmet',
          strength=20),

    Armor('blaze_helmet', rarity='epic', part='helmet',
          strength=10, defense=50, speed=2),
    Armor('blaze_chestplate', rarity='epic', part='chestplate',
          strength=10, defense=150, speed=2),
    Armor('blaze_leggings', rarity='epic', part='leggings',
          strength=10, defense=110, speed=2),
    Armor('blaze_boots', rarity='epic', part='boots',
          strength=10, defense=70, speed=2),

    Armor('leaflet_helmet', rarity='common', part='helmet',
          health=20),
    Armor('leaflet_chestplate', rarity='common', part='chestplate',
          health=35),
    Armor('leaflet_leggings', rarity='common', part='leggings',
          health=30),
    Armor('leaflet_boots', rarity='common', part='boots',
          health=15),

    Armor('growth_helmet', rarity='rare', part='helmet',
          health=50, defense=30),
    Armor('growth_chestplate', rarity='rare', part='chestplate',
          health=100, defense=50),
    Armor('growth_leggings', rarity='rare', part='leggings',
          health=80, defense=40),
    Armor('growth_boots', rarity='rare', part='boots',
          health=50, defense=25),

    Armor('magma_cube_head', rarity='common', part='helmet',
          health=25, defense=25),

    Armor('armor_of_magma_helmet', rarity='epic', part='helmet',
          health=50, defense=15),
    Armor('armor_of_magma_chestplate', rarity='epic', part='chestplate',
          health=100, defense=30),
    Armor('armor_of_magma_leggings', rarity='epic', part='leggings',
          health=75, defense=25),
    Armor('armor_of_magma_boots', rarity='epic', part='boots',
          health=45, defense=15),

    Armor('cheap_tuxedo_jacket', rarity='epic', part='chestplate',
          crit_damage=50, intelligence=50),
    Armor('cheap_tuxedo_pants', rarity='epic', part='leggings',
          crit_damage=25, intelligence=25),
    Armor('cheap_tuxedo_oxfords', rarity='epic', part='boots',
          crit_damage=25, intelligence=25),

    Armor('fancy_tuxedo_jacket', rarity='legendary', part='chestplate',
          crit_damage=80, intelligence=150),
    Armor('fancy_tuxedo_pants', rarity='legendary', part='leggings',
          crit_damage=35, intelligence=75),
    Armor('fancy_tuxedo_oxfords', rarity='legendary', part='boots',
          crit_damage=35, intelligence=75),

    Armor('elegant_tuxedo_jacket', rarity='legendary', part='chestplate',
          crit_damage=100, intelligence=300),
    Armor('elegant_tuxedo_pants', rarity='legendary', part='leggings',
          crit_damage=50, intelligence=100),
    Armor('elegant_tuxedo_oxfords', rarity='legendary', part='boots',
          crit_damage=50, intelligence=100, speed=10),

    Armor('lapis_helmet', rarity='uncommon', part='helmet',
          defense=25,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),
    Armor('lapis_chestplate', rarity='uncommon', part='chestplate',
          defense=40,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),
    Armor('lapis_leggings', rarity='uncommon', part='leggings',
          defense=35,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),
    Armor('lapis_boots', rarity='uncommon', part='boots',
          defense=20,
          abilities=['lapis_armor_exp_bonus', 'lapis_armor_health']),

    Armor('miner_helmet', rarity='uncommon', part='helmet',
          defense=45),
    Armor('miner_chestplate', rarity='uncommon', part='chestplate',
          defense=95),
    Armor('miner_leggings', rarity='uncommon', part='leggings',
          defense=70),
    Armor('miner_boots', rarity='uncommon', part='boots',
          defense=45),

    Armor('goblin_helmet', rarity='rare', part='helmet',
          defense=70, intelligence=-1, mining_speed=10),
    Armor('goblin_chestplate', rarity='rare', part='chestplate',
          defense=140, intelligence=-1, mining_speed=10),
    Armor('goblin_leggings', rarity='rare', part='leggings',
          defense=125, intelligence=-1, mining_speed=10),
    Armor('goblin_boots', rarity='rare', part='boots',
          defense=60, intelligence=-1, mining_speed=10),

    Armor('glacite_helmet', rarity='rare', part='helmet',
          defense=70, speed=10, mining_speed=10, true_defense=5,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),
    Armor('glacite_chestplate', rarity='rare', part='chestplate',
          defense=150, speed=15, mining_speed=10, true_defense=20,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),
    Armor('glacite_leggings', rarity='rare', part='leggings',
          defense=125, speed=15, mining_speed=10, true_defense=20,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),
    Armor('glacite_boots', rarity='rare', part='boots',
          defense=70, speed=10, mining_speed=10, true_defense=5,
          abilities=['glacite_expert_miner', 'glacite_double_defense']),

    Armor('sorrow_helmet', rarity='legendary', part='helmet',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=100),
    Armor('sorrow_chestplate', rarity='legendary', part='chestplate',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=200),
    Armor('sorrow_leggings', rarity='legendary', part='leggings',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=150),
    Armor('sorrow_boots', rarity='legendary', part='boots',
          magic_find=10, mining_speed=50, mining_fortune=20, true_defense=75),

    Armor('ender_helmet', rarity='epic', part='helmet',
          health=20, defense=35,
          combat_skill_req=12,
          abilities=['ender_armor']),
    Armor('ender_chestplate', rarity='epic', part='chestplate',
          health=30, defense=60,
          combat_skill_req=12,
          abilities=['ender_armor']),
    Armor('ender_leggings', rarity='epic', part='leggings',
          health=25, defense=50,
          combat_skill_req=12,
          abilities=['ender_armor']),
    Armor('ender_boots', rarity='epic', part='boots',
          health=15, defense=25,
          combat_skill_req=12,
          abilities=['ender_armor']),

    Armor('obsidian_chestplate', rarity='epic', part='chestplate',
          defense=250,
          combat_skill_req=14),

    Armor('protector_dragon_helmet', rarity='legendary', part='helmet',
          health=70, defense=135,
          combat_skill_req=16,
          abilities=['protective_blood']),
    Armor('protector_dragon_chestplate', rarity='legendary', part='chestplate',
          health=120, defense=185,
          combat_skill_req=16,
          abilities=['protective_blood']),
    Armor('protector_dragon_leggings', rarity='legendary', part='leggings',
          health=100, defense=165,
          combat_skill_req=16,
          abilities=['protective_blood']),
    Armor('protector_dragon_boots', rarity='legendary', part='boots',
          health=60, defense=115,
          combat_skill_req=16,
          abilities=['protective_blood']),

    Armor('old_dragon_helmet', rarity='legendary', part='helmet',
          health=110, defense=90,
          combat_skill_req=16,
          abilities=['old_blood']),
    Armor('old_dragon_chestplate', rarity='legendary', part='chestplate',
          health=160, defense=150,
          combat_skill_req=16,
          abilities=['old_blood']),
    Armor('old_dragon_leggings', rarity='legendary', part='leggings',
          health=130, defense=140,
          combat_skill_req=16,
          abilities=['old_blood']),
    Armor('old_dragon_boots', rarity='legendary', part='boots',
          health=80, defense=90,
          combat_skill_req=16,
          abilities=['old_blood']),

    Armor('unstable_dragon_helmet', rarity='legendary', part='helmet',
          crit_chance=5, crit_damage=15,
          health=70, defense=110, intelligence=25,
          combat_skill_req=16),
    Armor('unstable_dragon_chestplate', rarity='legendary', part='chestplate',
          crit_chance=5, crit_damage=15,
          health=120, defense=160,
          combat_skill_req=16),
    Armor('unstable_dragon_leggings', rarity='legendary', part='leggings',
          crit_chance=5, crit_damage=15,
          health=100, defense=140,
          combat_skill_req=16),
    Armor('unstable_dragon_boots', rarity='legendary', part='boots',
          crit_chance=5, crit_damage=15,
          health=60, defense=90,
          combat_skill_req=16),

    Armor('holy_dragon_helmet', rarity='legendary', part='helmet',
          health=110, defense=110,
          combat_skill_req=16,
          abilities=['holy_blood']),
    Armor('holy_dragon_chestplate', rarity='legendary', part='chestplate',
          health=180, defense=160,
          combat_skill_req=16,
          abilities=['holy_blood']),
    Armor('holy_dragon_leggings', rarity='legendary', part='leggings',
          health=155, defense=140,
          combat_skill_req=16,
          abilities=['holy_blood']),
    Armor('holy_dragon_boots', rarity='legendary', part='boots',
          health=100, defense=90,
          combat_skill_req=16,
          abilities=['holy_blood']),

    Armor('wise_dragon_helmet', rarity='legendary', part='helmet',
          health=70, defense=110, intelligence=125,
          combat_skill_req=16),
    Armor('wise_dragon_chestplate', rarity='legendary', part='chestplate',
          health=120, defense=160, intelligence=75,
          combat_skill_req=16),
    Armor('wise_dragon_leggings', rarity='legendary', part='leggings',
          health=100, defense=140, intelligence=75,
          combat_skill_req=16),
    Armor('wise_dragon_boots', rarity='legendary', part='boots',
          health=60, defense=90, intelligence=75,
          combat_skill_req=16),

    Armor('young_dragon_helmet', rarity='legendary', part='helmet',
          health=70, defense=110, speed=20,
          combat_skill_req=16,
          abilities=['young_blood']),
    Armor('young_dragon_chestplate', rarity='legendary', part='chestplate',
          health=120, defense=160, speed=20,
          combat_skill_req=16,
          abilities=['young_blood']),
    Armor('young_dragon_leggings', rarity='legendary', part='leggings',
          health=100, defense=140, speed=20,
          combat_skill_req=16,
          abilities=['young_blood']),
    Armor('young_dragon_boots', rarity='legendary', part='boots',
          health=60, defense=90, speed=20,
          combat_skill_req=16,
          abilities=['young_blood']),

    Armor('strong_dragon_helmet', rarity='legendary', part='helmet',
          strength=25, health=70, defense=110,
          combat_skill_req=16,
          abilities=['strong_blood']),
    Armor('strong_dragon_chestplate', rarity='legendary', part='chestplate',
          strength=25, health=120, defense=160,
          combat_skill_req=16,
          abilities=['strong_blood']),
    Armor('strong_dragon_leggings', rarity='legendary', part='leggings',
          strength=25, health=100, defense=140,
          combat_skill_req=16,
          abilities=['strong_blood']),
    Armor('strong_dragon_boots', rarity='legendary', part='boots',
          strength=25, health=60, defense=90,
          combat_skill_req=16,
          abilities=['strong_blood']),

    Armor('superior_dragon_helmet', rarity='legendary', part='helmet',
          strength=10, crit_chance=2, crit_damage=10,
          health=90, defense=130, intelligence=25, speed=3,
          combat_skill_req=20,
          abilities=['superior_blood']),
    Armor('superior_dragon_chestplate', rarity='legendary', part='chestplate',
          strength=10, crit_chance=2, crit_damage=10,
          health=150, defense=190, intelligence=25, speed=3,
          combat_skill_req=20,
          abilities=['superior_blood']),
    Armor('superior_dragon_leggings', rarity='legendary', part='leggings',
          strength=10, crit_chance=2, crit_damage=10,
          health=130, defense=170, intelligence=25, speed=3,
          combat_skill_req=20,
          abilities=['superior_blood']),
    Armor('superior_dragon_boots', rarity='legendary', part='boots',
          strength=10, crit_chance=2, crit_damage=10,
          health=80, defense=110, intelligence=25, speed=3,
          combat_skill_req=20,
          abilities=['superior_blood'])]
