"""
The 'ritual_experts' package holds the experts 'RitualGenerator' hands
its work to, one kind of work each.

- The ways a function of Qt is reached from a ritual, asked in turn,
  the first that can reach a function having it: 'CallExpert' calls it
  where Qt's library offers it, 'MetaExpert' has the class's
  meta-object run a signal, slot or invokable function, 'CopyExpert'
  carries a copy of its code from Qt's source. All are built on
  'ReachExpert'.
- The ways a type crosses between Python and C++, asked in turn, the
  first that claims a type saying how it crosses: 'NothingExpert',
  'NumberExpert', 'CharsExpert', 'TextsAddressExpert',
  'NumberAddressExpert', 'NullExpert', 'EnumExpert', 'FlagsExpert',
  'DurationExpert', 'AddressExpert', 'FunctionAddressExpert',
  'RawAddressExpert', 'ListExpert', 'MapExpert', 'ValueExpert',
  'MovedExpert', 'ReferenceExpert' and, last, 'HeldValueExpert' for a
  value of any type no cute class stands for. All are built on
  'TypeExpert'.
- The rest, one job each: 'ConditionExpert' finds the '#if' lines,
  'SpellingExpert' writes names in full, 'ProbeExpert' asks the
  compiler, 'CuteClassExpert' writes the C++ class of ours through which
  Python takes functions over, and 'RitualFileExpert' writes the text
  of the ritual file and of the rows file.

Every expert is built on 'RitualExpert', which knows the generator it
works for. 'CppText' takes apart and puts together types as C++ writes
them, for all of them.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._ritual_expert import RitualExpert
from ._cpp_text import CppText
from ._reach_expert import ReachExpert
from ._type_expert import TypeExpert
from ._condition_expert import ConditionExpert
from ._spelling_expert import SpellingExpert
from ._probe_expert import ProbeExpert
from ._call_expert import CallExpert
from ._meta_expert import MetaExpert
from ._copy_expert import CopyExpert
from ._nothing_expert import NothingExpert
from ._number_expert import NumberExpert
from ._chars_expert import CharsExpert
from ._texts_address_expert import TextsAddressExpert
from ._number_address_expert import NumberAddressExpert
from ._null_expert import NullExpert
from ._enum_expert import EnumExpert
from ._flags_expert import FlagsExpert
from ._duration_expert import DurationExpert
from ._address_expert import AddressExpert
from ._function_address_expert import FunctionAddressExpert
from ._raw_address_expert import RawAddressExpert
from ._value_expert import ValueExpert
from ._list_expert import ListExpert
from ._map_expert import MapExpert
from ._moved_expert import MovedExpert
from ._reference_expert import ReferenceExpert
from ._held_value_expert import HeldValueExpert
from ._cute_class_expert import CuteClassExpert
from ._ritual_file_expert import RitualFileExpert

__all__ = (
    'RitualExpert', 'CppText',
    'ReachExpert', 'CallExpert', 'MetaExpert', 'CopyExpert',
    'TypeExpert', 'NothingExpert', 'NumberExpert', 'CharsExpert',
    'TextsAddressExpert', 'NumberAddressExpert', 'NullExpert',
    'EnumExpert', 'FlagsExpert', 'DurationExpert', 'AddressExpert',
    'FunctionAddressExpert', 'RawAddressExpert', 'ListExpert',
    'MapExpert', 'ValueExpert', 'MovedExpert', 'ReferenceExpert',
    'HeldValueExpert',
    'ConditionExpert', 'SpellingExpert', 'ProbeExpert',
    'CuteClassExpert', 'RitualFileExpert',
)
