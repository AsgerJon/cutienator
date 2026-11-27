"""HeldValueExpert says how a value of a type no cute class stands for
crosses: by the address of a C++ copy Python holds."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING

from .. import HeaderReader
from . import CppText, TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]


class HeldValueExpert(TypeExpert):
  """
  Says how a value crosses of a type no other expert claims and no
  cute class stands for: a smart pointer, as
  'QSharedPointer<QGeoTileTexture>' or Qt's 'QQmlJSScope::ConstPtr'; a
  container of numbers, as 'QList<int>'; 'QBindable<qreal>',
  'QQmlListProperty<QObject>', 'std::optional<quint64>', an iterator,
  'std::filesystem::path', and so on. It crosses as a value of a class
  does: the ritual takes the address of one and hands Qt the value
  there, and for one Qt gives back, makes a copy with 'new' and gives
  its address. Python holds that address without knowing the type, and
  can hand it back to Qt. Its word in the sigil is 'address'.

  For each such type a function of the class gives back, the class gets
  a ritual that removes a copy Python holds, named
  'ritual_drop_<class>__<type>'; see '_planDrops'.

  Whether C++ can copy the type where the ritual file stands, nobody
  can say before the compiler: a header may declare a function giving
  a type it never defines. 'ProbeExpert.settle' compiles the ritual
  file, and takes out every ritual the compiler refuses, with what it
  said, so that it never stands in the way of the others.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The header of the C++ library each type of 'std' a held value names
  #  is defined in.
  __std_headers__ = dict(
      optional='optional', pair='utility', tuple='tuple',
      unique_ptr='memory', shared_ptr='memory', weak_ptr='memory',
      function='functional', filesystem='filesystem', string='string',
      u16string='string', string_view='string_view',
      u16string_view='string_view', vector='vector', list='list',
      deque='deque', map='map', set='set', unordered_map='unordered_map',
      unordered_set='unordered_set', array='array', variant='variant',
      chrono='chrono', byte='cstddef', span='span',
  )
  #  A name as C++ writes it inside a type, as 'std::optional' or
  #  'QCborMap::const_iterator'.
  __name_pattern__ = re.compile(r'[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('held value',)

  def getIncludeLines(self) -> Tuple[str, ...]:
    """
    Gives the lines pulling in the header files that define what the
    held values of the rituals of the class name: a header of Qt named
    after a class, as '#include <QtCore/QBindable>' for
    'QBindable<qreal>', and one of the C++ library, as
    '#include <optional>' for 'std::optional<quint64>'. A header of Qt
    may only declare such a type, as 'qobject.h' declares 'QBindable',
    and a copy needs it defined.
    """
    found = []  # type: List[str]
    for plan in self.getGenerator().getWritten():
      if not self._usesHeld(plan):
        continue
      held = [plan.get('held', '')]
      giving = plan.get('giving') or dict()
      held.append(giving.get('className', ''))
      for argument in plan.get('arguments') or ():
        held.append(argument['passing'].get('className', ''))
      for cppType in held:
        for line in self._findIncludes(cppType or ''):
          if line not in found:
            found.append(line)
    return (*found,)

  def _getNamedHeaders(self) -> Dict[str, List[str]]:
    """Gives, for each header of Qt named after a class, as 'QBindable',
    the parts that have one, as the header folder of the reading has
    them; kept on the tree."""
    kept = self.getGenerator().getDependencyTree().getKept('named headers')
    if 'found' in kept:
      return kept['found']
    folder = HeaderReader.getHeaderFolder().getFolder()
    found = dict()  # type: Dict[str, List[str]]
    for partName in sorted(os.listdir(folder)):
      partFolder = os.path.join(folder, partName)
      if not os.path.isdir(partFolder):
        continue
      for name in os.listdir(partFolder):
        if re.fullmatch(r'Q\w+', name):
          found.setdefault(name, []).append(partName)
    kept['found'] = found
    return found

  def _findIncludes(self, cppType: str) -> List[str]:
    """Gives the lines pulling in what one held type names; see
    'getIncludeLines'."""
    named = self._getNamedHeaders()
    partName = self.getGenerator().getPartName()
    lines = []  # type: List[str]
    for name in self.__name_pattern__.findall(cppType):
      parts = name.split('::')
      if parts[0] == 'std' and len(parts) > 1:
        header = self.__std_headers__.get(parts[1])
        if header is not None:
          lines.append('#include <%s>' % header)
        continue
      owners = named.get(parts[0], ())
      if not owners:
        continue
      #  The part of the class first, then QtCore, then any other.
      ordered = sorted(owners, key=lambda one: (
          one != partName, one != 'QtCore', one))
      lines.append('#include <%s/%s>' % (ordered[0], parts[0]))
    return lines

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def claims(self, written: str, plain: str) -> bool:
    """Claims a value of any type no expert before it claimed: no
    address, no reference left to the others, no function, no array and
    not 'void'."""
    bare = CppText.stripReadOnly(plain).strip()
    if not bare or bare == 'void':
      return False
    if bare.endswith(('*', '&', ')', ']')):
      return False
    return True

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the value crosses by the address of a C++ copy, with
    the type as C++ writes it as 'className'."""
    className = CppText.stripReadOnly(written).strip()
    return dict(kind='held value', word='address', className=className)

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """The ritual takes the address of the value and hands Qt the value
    there."""
    return 'const %s *' % passing['className'], '*%s' % name, ()

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The copy is made here, and its address is what goes back."""
    className = giving['className']
    return '%s *' % className, 'return new %s(' % className, '));', ()

  @staticmethod
  def _usesHeld(plan: Record) -> bool:
    """Says whether a ritual takes or gives a held value, or removes
    one."""
    if plan.get('kind') == 'drop':
      return True
    giving = plan.get('giving') or dict()
    if giving.get('kind') == 'held value':
      return True
    arguments = plan.get('arguments') or ()
    return any(a['passing'].get('kind') == 'held value' for a in arguments)

  def _planDrops(self, written: List[Record]) -> List[Record]:
    """Works out, for each held value a ritual gives back, the ritual
    removing a copy Python holds: 'delete self'."""
    from . import RitualFileExpert
    generator = self.getGenerator()
    classTag = generator.getClassName().replace('::', '_')
    fileExpert = generator.getExpert(RitualFileExpert)
    given = []  # type: List[str]
    for plan in written:
      giving = plan.get('giving') or dict()
      if giving.get('kind') == 'held value':
        if giving['className'] not in given:
          given.append(giving['className'])
    plans = []  # type: List[Record]
    for className in given:
      typeTag = re.sub(r'[^A-Za-z0-9]+', '_', className).strip('_')
      plan = dict(
          ritualName='ritual_drop_%s__%s' % (classTag, typeTag),
          function='a %s a ritual of %s gave' % (
              className, generator.getClassName()),
          kind='drop', gives='void', takes=(('self', '%s *' % className),),
          sigil=('nothing', 'address'), needs=(), unknownTypes=(),
          unsureNumbers=(), words=(), variadic=False, name='',
          arguments=(), giving=None, inPlace=False, held=className,
      )
      plan['text'] = fileExpert.writeRitual(plan, ['  delete self;'])
      plans.append(plan)
    return plans

  def settle(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> None:
    """Adds the rituals removing the held values the rituals give back;
    whether the compiler can copy each where the file stands,
    'ProbeExpert.settle' asks it next."""
    written.extend(self._planDrops(written))

  def forgetDrops(self, written: List[Record]) -> None:
    """Takes out each ritual removing a held value that no ritual gives
    back any more, once others were taken out."""
    kept = {
        (plan.get('giving') or dict()).get('className')
        for plan in written
        if (plan.get('giving') or dict()).get('kind') == 'held value'}
    for plan in [*written]:
      if plan.get('kind') == 'drop' and plan['held'] not in kept:
        written.remove(plan)
