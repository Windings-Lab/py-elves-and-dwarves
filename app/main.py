from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum([player.get_rating() for player in team])


def elves_concert(team: list[Elf]) -> None:
    (elf.play_elf_song() for elf in team)


def feast_of_the_dwarves(team: list[Dwarf]) -> None:
    (dwarf.eat_favourite_dish() for dwarf in team)
