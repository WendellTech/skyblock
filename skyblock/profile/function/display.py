from math import ceil, floor, radians, tan
from os import get_terminal_size
from time import sleep
from typing import Iterable, Optional

from ...constant.color import *
from ...constant.main import ARMOR_PARTS
from ...constant.stat import ALL_STAT, HIDDEN_STATS, PERC_STATS
from ...constant.util import Number
from ...function.io import *
from ...function.math import (
    calc_bestiary_lvl, calc_bestiary_upgrade_amount, calc_skill_lvl_info,
    display_skill_reward, fround,
)
from ...function.util import (
    format_name, format_number, format_roman, format_short, format_zone,
    get, get_family, index,
)
from ...object.collection import COLLECTIONS, get_collection
from ...object.item import get_item
from ...object.mob import MOBS
from ...object.object import *
from ...object.recipe import RECIPES
from ...map.island import ISLANDS
from ...map.object import *


__all__ = [
    'display_armor', 'display_bestiary', 'display_bestiaries',
    'display_collection_info', 'display_collection', 'display_collections',
    'display_item', 'display_inv', 'display_location', 'display_money',
    'display_pets', 'display_playtime', 'display_recipe_info', 'display_recipe',
    'display_recipes', 'display_shop', 'display_stats', 'display_skill_add',
    'display_skill', 'display_skills', 'display_warp',
    'npc_silent', 'npc_speak',
]


def display_armor(self, part: Optional[str] = None, /):
    if part:
        item = self.armor[ARMOR_PARTS.index(part)]
        self.display_item(item)
        return

    for piece, name in zip(self.armor, ARMOR_PARTS):
        gray(f'{format_name(name)}: {piece.display()}')


def display_bestiary(self, name: str, /):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)

    display = format_name(name)
    family = get_family(name)

    kills = self.stats.get(f'kills_{family}', 0)
    deaths = self.stats.get(f'deaths_{name}', 0)
    lvl = self.get_bestiary_lvl(family)

    if kills == 0:
        red("You haven't unlocked this bestiary family yet!")
        return

    yellow(f"{BOLD}{'':-^{width}}")
    aqua(f'{display} {format_roman(lvl)}\n')
    gray(f'Kills: {GREEN}{kills}')
    gray(f'Deaths: {GREEN}{deaths}\n')

    amt_left, amt_to_next = calc_bestiary_upgrade_amount(kills)

    stat_boost = min(lvl, 5)
    stat_boost += 2 * max(min(lvl - 5, 5), 0)
    stat_boost += 3 * max(lvl - 10, 0)

    xp_orbs, chance = divmod(100 + lvl * 20, 100)
    if chance == 0:
        xp_orbs -= 1
        chance = 100

    magic_find = STAT_COLORS['magic_find']
    strength = STAT_COLORS['strength']
    aqua(
        f' {BOLD}REWARDS\n'
        f'  {DARK_GRAY}+{AQUA}{stat_boost} {magic_find} Magic Find\n'
        f'  {DARK_GRAY}+{RED}{stat_boost} {strength} Strength\n'
        f'  {DARK_GRAY}+{GOLD}{lvl}% {GRAY}coin gain\n'
        f'  {DARK_GRAY}+{GREEN}{chance}% {GRAY}chance for'
        f' {GREEN}+{xp_orbs}{GRAY} XP orbs\n'
    )

    perc = fround(amt_left / amt_to_next * 100, 2)
    gray(f'Progress to Tier {format_roman(lvl + 1)}: {AQUA}{perc}%')

    bar = min(floor(amt_left / amt_to_next * 20), 20)
    left, right = '-' * bar, '-' * (20 - bar)
    green(f'{BOLD}{left}{GRAY}{BOLD}{right} {AQUA}{format_number(amt_left)}'
          f'{DARK_AQUA}/{AQUA}{format_short(amt_to_next)}')

    gray(f'\nTier {format_roman(lvl + 1)} Rewards:')
    if lvl < 5:
        stat_delta = 1
    elif lvl < 10:
        stat_delta = 2
    else:
        stat_delta = 3
    aqua(
        f' {BOLD}REWARDS\n'
        f'  {DARK_GRAY}+{GREEN}{stat_delta} {AQUA}{display}'
        f' {magic_find} Magic Find\n'
        f'  {DARK_GRAY}+{GREEN}{stat_delta} {AQUA}{display}'
        f' {strength} Strength\n'
        f'  {DARK_GRAY}+{GOLD}1% {AQUA}{display} {GRAY}coins\n'
        f'  {DARK_GRAY}+{GREEN}20% {GRAY}chance for extra XP orbs'
    )

    yellow(f"{BOLD}{'':-^{width}}")


def display_bestiaries(self, /):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)

    yellow(f"{BOLD}{'':-^{width}}")

    displayed_families = []

    for mob in MOBS:
        family = get_family(mob.name)
        if family in displayed_families:
            continue
        displayed_families.append(family)

        bestiary_lvl = self.get_bestiary_amount(family)
        kills = self.stats.get(f'kills_{family}', 0)
        if kills == 0:
            gray('  unknown')
            continue
        bestiary_lvl = self.get_bestiary_lvl(mob.name)
        aqua(f'  {format_name(mob.name)} {format_roman(bestiary_lvl)}')

    yellow(f"{BOLD}{'':-^{width}}")


def display_collection_info(self, name: str, /):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)
    yellow(f"{BOLD}{'':-^{width}}")

    coll = get_collection(name)
    lvl = self.coll_lvl(name)
    lvl_str = f' {format_roman(lvl)}' if lvl != 0 else ''
    display = format_name(name)

    current = self.coll_amount(name)

    yellow(f'{display}{lvl_str}')
    last_lvl = 0
    next_lvl = None
    rewards = None
    past_amount = 0

    for index, (amount, rwds) in enumerate(coll.levels):
        display = display

        if not hasattr(rwds, '__iter__'):
            rwds = [rwds]

        if amount > current and next_lvl is None:
            next_lvl = amount - last_lvl
            rewards = [reward for reward in rwds]
            past_amount = last_lvl
        last_lvl = amount

        gray(f'\n{display} {format_roman(index + 1)} Reward:')
        for reward in rwds:
            if isinstance(reward, (float, int)):
                dark_gray(f' +{DARK_AQUA}{reward}{GRAY}'
                          f' {format_name(coll.category)} Experience')
            elif isinstance(reward, Recipe):
                item = reward.result[0]
                color = RARITY_COLORS[item.rarity]
                print(f'  {color}{format_name(item.name)} {GRAY}Recipe'
                      f' {DARK_GRAY}{reward.name}')

    this_lvl = current - past_amount
    if next_lvl is None:
        next_lvl = 0

    progress = min(this_lvl / next_lvl, 1)
    bar = floor(progress * 20)
    left, right = '-' * bar, '-' * (20 - bar)
    if rewards is not None:
        gray(f'\nProgress: {YELLOW}{floor(progress * 100)}{GOLD}%')
    green(f'{BOLD}{left}{GRAY}{BOLD}{right} {YELLOW}{format_number(this_lvl)}'
          f'{GOLD}/{YELLOW}{format_short(next_lvl)}\n')
    if rewards is not None:
        gray(f'{display} {format_roman(lvl + 1)} Reward:')
        for reward in rewards:
            if isinstance(reward, (float, int)):
                dark_gray(f'  +{DARK_AQUA}{reward}{GRAY}'
                          f' {format_name(coll.category)} Experience')
            elif isinstance(reward, Recipe):
                item = reward.result[0]
                color = RARITY_COLORS[item.rarity]
                print(f'  {color}{format_name(item.name)} {GRAY}Recipe')

    yellow(f"{BOLD}{'':-^{width}}")


def display_collection(self, category: str, /, *, end=True):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)
    yellow(f"{BOLD}{'':-^{width}}")

    green(f'{format_name(category)} Collections')
    colls = [coll for coll in COLLECTIONS if coll.category == category]

    if len(colls) == 0:
        gray('  none')
    else:
        for coll in colls:
            if self.collection[coll.name] == 0:
                gray('  unknown')
                continue
            name = format_name(coll.name)
            lvl = self.coll_lvl(coll.name)
            lvl_str = f' {format_roman(lvl)}' if lvl != 0 else ''
            yellow(f'  {name}{lvl_str}')

    if end:
        yellow(f"{BOLD}{'':-^{width}}")


def display_collections(self, /):
    for category in ('farming', 'mining', 'combat',
                     'foraging', 'fishing'):
        self.display_collection(category, end=False)


def display_item(self, item: ItemType, /):
    if isinstance(item, Empty):
        gray('Empty')
        return

    width, _ = get_terminal_size()
    width = ceil(width * 0.85)
    yellow(f"{BOLD}{'':-^{width}}")
    gray(item.info(self))
    yellow(f"{BOLD}{'':-^{width}}")


def display_inv(self, /):
    length = len(self.inventory)

    digits = len(f'{length}')
    empty_slots = []
    index = 0
    is_empty = True
    while index < length:
        item = self.inventory[index]
        if isinstance(item, Empty):
            while index < length:
                if not isinstance(self.inventory[index], Empty):
                    break
                empty_slots.append(index)
                index += 1
            continue

        is_empty = False
        if empty_slots:
            for empty_index in empty_slots:
                gray(f'{(empty_index + 1):>{digits * 2 + 1}}')
            empty_slots.clear()
        gray(f'{(index + 1):>{digits * 2 + 1}} {item.display()}')
        index += 1

    if is_empty:
        gray('Your inventory is empty.')


def display_location(self, /):
    island = get(ISLANDS, self.island)
    zone = get(island.zones, self.zone)

    gray('Location:')
    gray(f"  You're at {AQUA}{zone}{GRAY} of {AQUA}{island}{GRAY}.")
    gray('\nNearby places:')
    for conn in island.conns:
        if zone not in conn:
            continue
        other = conn[0] if conn[1] == zone else conn[1]
        sx, sz, ox, oz = zone.x, zone.z, other.x, other.z
        dx, dz = ox - sx, oz - sz
        direc = ''
        if dx == 0:
            direc = 'South' if dz > 0 else 'North'
        elif dz == 0:
            direc = 'East' if dx > 0 else 'West'
        else:
            if dx / dz < tan(radians(60)):
                direc += 'South' if dz > 0 else 'North'
            if dz / dx < tan(radians(60)):
                direc += 'East' if dx > 0 else 'West'
        gray(f'  {AQUA}{format_zone(other.name)}{GRAY}'
             f' on the {AQUA}{direc}{GRAY} ({other.name}).')

    if len(zone.resources) > 0:
        gray('\nResources:')
        for resource in zone.resources:
            gray(f'  {GREEN}{format_name(resource.name)}{GRAY}'
                 f' ({resource.name}).')

    if len(zone.mobs) > 0:
        gray('\nMobs:')
        for mob in zone.mobs:
            green(f'  {mob.display()}{GRAY} ({mob.name}).')

    if len(zone.npcs) > 0:
        gray('\nNPCs:')
        for npc in zone.npcs:
            gray(f'  {GREEN}{npc}{GRAY} ({npc.name}).')

    if zone.portal is not None:
        gray(f'\nPortal to {AQUA}{format_zone(zone.portal)}{GRAY}'
             f' ({zone.portal})')

    gray()


def display_money(self, /):
    if self.zone not in {'bank', 'dwarven_village'}:
        white(f'Purse: {GOLD}{format_number(self.purse)} Coins')
        return

    balance_str = format_number(self.balance)
    if '.' not in balance_str:
        balance_str = balance_str + '  '
    purse_str = format_number(self.purse)
    if '.' not in purse_str:
        purse_str = purse_str + '  '
    length = max(len(balance_str), len(purse_str))

    green('Bank Account')
    gray(f'Balance: {GOLD}{balance_str:>{length}} Coins')
    white(f'Purse:   {GOLD}{purse_str:>{length}} Coins')
    gray(f'Bank Level: {GREEN}{format_name(self.bank_level)}')


def display_pets(self, /):
    length = len(self.pets)
    if length == 0:
        gray("You don't have any pets in your pet menu!")
        return

    digits = len(f'{length}')

    gray('Your pets:')

    for index, pet in enumerate(self.pets):
        active = f'{AQUA}*{GRAY}' if pet.active else ' '
        gray(f'{active} {index + 1:>{digits}} {pet.display()}')


def display_playtime(self, /):
    all_mins = self.play_time // 60
    if all_mins == 0:
        red("You don't have enough playtime"
            " to use this command, try again later!")
        return
    hours, mins = divmod(all_mins, 60)
    green(f'You have {hours} hours and {mins:0>2} minutes playtime!')


def display_recipe_info(self, index: int, /):
    if index >= len(RECIPES):
        red('Recipe index out of bound.')
        return

    width, _ = get_terminal_size()
    width = ceil(width * 0.85)
    yellow(f"{BOLD}{'':-^{width}}")

    recipe = RECIPES[index]

    green(f'{format_name(recipe.name)} '
          f'{GRAY}({format_name(recipe.category)} Recipe)')

    gray('\nIngredients:')
    for item, amount in recipe.ingredients:
        count_str = f'{DARK_GRAY} x {amount}'
        gray(f'  {item.display()}{count_str}')
    gray('\nResult:')
    item, amount = recipe.result
    count_str = f'{DARK_GRAY} x {amount}'
    gray(f'  {item.display()}{count_str}')

    requirements = []

    if recipe.collection_req is not None:
        coll_name, coll_lvl = recipe.collection_req
        lvl = self.coll_lvl(coll_name)
        if lvl < coll_lvl:
            requirements.append(
                f'{DARK_RED}❣ {RED}Requires {GREEN}'
                f'{format_name(coll_name)} Collection {format_roman(coll_lvl)}'
            )

    if len(requirements) != 0:
        gray()
        for req in requirements:
            gray(req)

    yellow(f"{BOLD}{'':-^{width}}")


def display_recipe(self, category: Optional[str], /, *,
                   show_all=False, end=True):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)
    yellow(f"{BOLD}{'':-^{width}}")

    green(f'{format_name(category)} Recipes')
    recipes = [recipe for recipe in RECIPES if recipe.category == category]

    if not show_all:
        recipes_copy = [recipe for recipe in recipes]
        recipes = []
        for recipe in recipes_copy:
            if recipe.collection_req is not None:
                coll_name, coll_lvl = recipe.collection_req
                lvl = self.coll_lvl(coll_name)
                if lvl < coll_lvl:
                    continue

            for item, count in recipe.ingredients:
                if not self.has_item(item.name, count):
                    break
            else:
                recipes.append(recipe)

    digits = len(f'{len(RECIPES)}')

    if len(recipes) == 0:
        gray('  none')
    else:
        for recipe in recipes:
            i = index(RECIPES, recipe.name)
            gray(f'  {(i + 1):>{digits}} {AQUA}{format_name(recipe.name)}')

    if end:
        yellow(f"{BOLD}{'':-^{width}}")


def display_recipes(self, /, *, show_all=False):
    for category in ('farming', 'mining', 'combat', 'foraging', 'fishing',
                     'enchanting', 'forging', 'smelting'):
        self.display_recipe(category, show_all=show_all, end=False)

    width, _ = get_terminal_size()
    width = ceil(width * 0.85)
    yellow(f"{BOLD}{'':-^{width}}")


def display_shop(self, npc: Npc, trade_index: Optional[int] = None, /):
    if trade_index is None:
        gray(f"{npc}'s shop:")
        if len(npc.trades) == 0:
            gray('  none')
            return

        digits = len(f'{len(npc.trades)}')
        for index, (cost, item) in enumerate(npc.trades):
            if isinstance(cost, (int, float)):
                gray(f'  {(index + 1):>{digits}} {item.display()}{GRAY}'
                     f' for {GOLD}{format_number(cost)} coins{GRAY}.')
                continue

            gray(f'  {(index + 1):>{digits}} {item.display()}{GRAY}')
            for cost_item in cost:
                if isinstance(cost_item, int):
                    gray(f"  {'':>{digits}}   {GOLD}"
                         f"{format_number(cost_item)} coins{GRAY}")
                    continue

                item, amount = cost_item
                item_type = get_item(item.name)
                color = RARITY_COLORS[item_type.rarity]
                cost_display = f'{color}{format_name(item.name)}{GRAY}'
                count = ('' if amount == 1
                         else f' {GRAY}x {amount}')
                gray(f"  {'':>{digits}}   {cost_display}{count}")
    else:
        self.display_item(npc.trades[trade_index][1])


def display_stats(self, index: Optional[int] = None, /):
    green('Your SkyBlock Profile')
    for stat_name in ALL_STAT:
        value = self.get_stat(stat_name, index)
        if value == 0 and stat_name in HIDDEN_STATS:
            continue
        color = STAT_COLORS[stat_name]
        if stat_name == 'health':
            ext = ' HP'
        else:
            ext = '%' if stat_name in PERC_STATS else ''
        white(f'  {color} {format_name(stat_name)}'
              f' {WHITE}{floor(value)}{ext}')


def display_skill_add(self, name: str, amount: Number, /):
    name_display = format_name(name)

    exp = self.get_skill_exp(name)
    _, exp_left, exp_to_next = calc_skill_lvl_info(name, exp)

    dark_aqua(f'+ {format_number(amount)} {name_display}'
              f' ({format_number(exp_left)}/{format_number(exp_to_next)})')


def display_skill(self, name: str, /, *,
                  reward: bool = True, end: bool = True):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)

    yellow(f"{BOLD}{'':-^{width}}")

    exp = self.get_skill_exp(name)
    lvl, exp_left, exp_to_next = calc_skill_lvl_info(name, exp)
    green(f'{format_name(name)} {format_roman(lvl)}')

    if exp_left < exp_to_next:
        perc = fround(exp_left / exp_to_next * 100, 2)
        gray(f'Progress to level {format_roman(lvl + 1)}: {YELLOW}{perc}%')

    bar = min(floor(exp_left / exp_to_next * 20), 20)
    left, right = '-' * bar, '-' * (20 - bar)
    green(f'{BOLD}{left}{GRAY}{BOLD}{right} {YELLOW}{format_number(exp_left)}'
          f'{GOLD}/{YELLOW}{format_short(exp_to_next)}')

    if reward and exp_left < exp_to_next:
        gray(f'\nLevel {format_roman(lvl + 1)} Rewards:')
        display_skill_reward(name, lvl, lvl + 1)

    if end:
        yellow(f"{BOLD}{'':-^{width}}")


def display_skills(self, /):
    width, _ = get_terminal_size()
    width = ceil(width * 0.85)

    for skill in ('farming', 'mining', 'combat', 'foraging', 'fishing',
                  'enchanting', 'alchemy', 'taming', 'catacombs'):
        self.display_skill(skill, reward=False, end=False)

    yellow(f"{BOLD}{'':-^{width}}")


def display_warp(self, /):
    gray('Unlocked fast travel destinations:')
    if len(self.fast_travel) == 0:
        gray('  none')
        return

    fast_travel = [scroll.copy() for scroll in self.fast_travel]
    fast_travel = sorted(fast_travel, key=lambda item: (
        index(ISLANDS, item[0]),
        index((island := get(ISLANDS, item[0])).zones,
              island.spawn if item[1] is None else item[1]),
    ))

    for island, zone in self.fast_travel:
        i_name = format_zone(island)
        r_name = 'Spawn' if zone is None else format_zone(zone)
        warp_name = island if zone is None else zone
        green(f'  {i_name}{GRAY} - {AQUA}{r_name}')
        dark_gray(f'  /warp {warp_name}')


@staticmethod
def npc_silent(npc: Npc, /):
    yellow(f'[NPC] {format_name(npc.name)}'
           f"{WHITE}: ({format_name(npc.name)} said nothing)")


@staticmethod
def npc_speak(name: str, dialog: Iterable):
    iterator = iter(dialog)
    yellow(f'[NPC] {format_name(name)}{WHITE}: {next(iterator)}')
    for sentence in iterator:
        sleep(1.5)
        yellow(f'[NPC] {format_name(name)}{WHITE}: {sentence}')


display_functions = {
    name: globals()[name] for name in __all__
}
