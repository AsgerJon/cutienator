"""SpellingExpert writes a type the way it has to be written outside
the class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import re
from typing import TYPE_CHECKING

from . import RitualExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, FrozenSet, List, Optional


class SpellingExpert(RitualExpert):
  """
  Writes a type the way it has to be written outside the class. Inside
  a class a header may shorten the name of anything the class declares
  itself, or a class it is built on declares: the second name 'Id' in
  'QAccessible' is 'QAccessible::Id' anywhere else. A ritual stands
  outside every class, so it needs the full name; see 'spellOutside'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  A name as C++ writes it inside a type, as 'QMetaObject::Connection'.
  __name_pattern__ = re.compile(r'[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*')

  #  Private Variables
  __known_names__ = None  # type: Optional[FrozenSet[str]]
  __spelling_names__ = None  # type: Optional[FrozenSet[str]]
  #  The classes 'spellOutside' looks a shortened name up in, nearest
  #  first, the class of the generator first.
  __spelling_scopes__ = None  # type: Optional[List[str]]

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKnownNames(self, **kwargs) -> FrozenSet[str]:
    """
    Gives the full name of every class, enum and second name for a type
    the dependency tree knows, as 'QAccessible::Id'. Kept after the
    first call.
    """
    if self.__known_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      generator = self.getGenerator()
      tree = generator.getDependencyTree()
      self.__known_names__ = frozenset((
          *(name for _, name in tree.getClasses()),
          *(name for _, name in tree.getEnumNames()),
          *tree.getAliasTypes(generator.getPartName()),
      ))
      return self.getKnownNames(_recursion=True)
    return self.__known_names__

  def getLookupOrder(self) -> List[str]:
    """Gives the class of the generator and every class it is built
    on, nearest first, as C++ looks a name up: the class, the classes it
    is built on, then theirs. Kept for the class."""
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    className = generator.getClassName()
    scopes = self.__spelling_scopes__
    if scopes is None or scopes[0] != className:
      partName = generator.getPartName()
      scopes, waiting = [], [className]  # type: List[str], List[str]
      while waiting:
        name = waiting.pop(0)
        if name in scopes:
          continue
        scopes.append(name)
        for parent in tree.getParents(name, partName):
          parent = parent.split('<')[0].strip()
          if tree.hasClass(parent, partName) and parent not in scopes:
            waiting.append(parent)
      for _, name in reversed(tree.getAncestors(className, partName)):
        if name not in scopes:
          scopes.append(name)
      self.__spelling_scopes__ = scopes
    return scopes

  def getSpellingNames(self, **kwargs) -> FrozenSet[str]:
    """
    Gives the names 'spellOutside' writes in full: those of
    'getKnownNames', and the classes a class declares private or
    protected, as 'QMetaMethod::Data', which no Python class stands
    for but a ritual may name, as it is compiled with
    '-fno-access-control'. Kept after the first call.
    """
    if self.__spelling_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      tree = self.getGenerator().getDependencyTree()
      self.__spelling_names__ = frozenset((
          *self.getKnownNames(),
          *(name for _, name in tree.getLeftOut()),
      ))
      return self.getSpellingNames(_recursion=True)
    return self.__spelling_names__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def spellOutside(self, cppType: str) -> str:
    """
    Writes a type the way it has to be written outside the class.

    Inside a class a header may shorten the name of anything the class
    declares itself, or a class it is built on declares: the second
    name 'Id' in 'QAccessible' is 'QAccessible::Id' anywhere else. A
    ritual stands outside every class, so it needs the full name.

    Parameters
    ----------

    cppType : str
      A type as the header of the class writes it, as 'Id' or
      'const Connection &'.

    Returns
    -------

    str
      The same type with every shortened name written in full. A name
      the dependency tree does not know inside the class, or inside a
      class it is built on, is left as it is.
    """
    known = self.getSpellingNames()
    #  Nearest first, as C++ looks a name up: the class, the classes it
    #  is built on, then theirs. 'Type' in 'QGles2Buffer' is the one of
    #  'QRhiBuffer', not the one of 'QRhiResource' further down.
    scopes = self.getLookupOrder()

    def spell(match: Any) -> str:
      name = match.group(0)
      for scope in scopes:
        while scope:
          fullName = '%s::%s' % (scope, name)
          if fullName in known:
            return fullName
          scope = scope.rpartition('::')[0]
      return name

    return self.__name_pattern__.sub(spell, cppType)
