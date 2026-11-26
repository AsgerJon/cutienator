"""DurationExpert says how a span of time of C++ crosses: as the number
of its steps."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from . import CppText, NumberExpert, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]


class DurationExpert(TypeExpert):
  """
  Says how a span of time of C++ crosses, 'std::chrono::milliseconds'
  and every other 'std::chrono::duration': as the number of its steps,
  each step as long as the type says, a millisecond for
  'std::chrono::milliseconds'. The ritual takes the number as a
  'long long', or a 'double' for a span counted in fractions, makes the
  span of it for Qt, and gives back the number of a span Qt gives, by
  'count()'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  A span of time as the compiler reads it, with the number type it
  #  counts in: 'std::chrono::duration<long, std::ratio<1, 1000>>'.
  __duration_pattern__ = re.compile(
      r'^std::chrono::duration<\s*([A-Za-z_][\w ]*?)\s*'
      r'(?:,\s*std::ratio<[^<>]*>\s*)?>$')
  #  The number types a span counts in fractions with.
  __fraction_types__ = ('float', 'double', 'long double')
  #  The spans C++ names, each counting in whole steps, where the
  #  compiler reports the name alone.
  __duration_names__ = (
      'nanoseconds', 'microseconds', 'milliseconds', 'seconds',
      'minutes', 'hours', 'days', 'weeks', 'months', 'years',
  )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('duration',)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findSteps(self, plain: str) -> str:
    """Gives the number type a span of time counts in, as 'long', or ''
    for a type that is no span of time handed around as a value."""
    bare = CppText.stripReadOnly(plain)
    named = bare[len('std::chrono::'):]
    if bare.startswith('std::chrono::') and named in self.__duration_names__:
      return 'long long'
    match = self.__duration_pattern__.match(bare)
    if match is None:
      return ''
    steps = self.getGenerator()._followAliases(match.group(1).strip())
    if steps not in NumberExpert.getNumberTypes():
      if steps not in self.__fraction_types__:
        return ''
    return steps

  def claims(self, written: str, plain: str) -> bool:
    """Claims a span of time handed around as a value."""
    return True if self._findSteps(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says how the span crosses, with the span as C++ writes it as
    'className', as 'std::chrono::milliseconds'."""
    steps = self._findSteps(plain)
    word = 'double' if steps in self.__fraction_types__ else 'long long'
    className = CppText.stripReadOnly(written)
    return dict(kind='duration', word=word, className=className)

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """The span is made of the number for the call."""
    handed = '%s(%s)' % (passing['className'], name)
    return passing['word'], handed, ()

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The number of steps of the span Qt gives goes back."""
    word = giving['word']
    return word, 'return static_cast<%s>(' % word, ').count());', ()
