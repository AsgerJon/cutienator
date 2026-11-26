"""ListExpert says how a list of Qt crosses, and writes the rituals of
each kind of list."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import threading
from typing import TYPE_CHECKING

from . import CppText, TypeExpert, ValueExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]


class ListExpert(TypeExpert):
  """
  Says how a list of Qt crosses: as a value does, by the address of the
  C++ list. Qt has one class of list for each thing a list can hold:
  'QList<QUrl>', 'QList<QAction *>', and 'QStringList', its second
  name for 'QList<QString>'.

  A list needs rituals of its own, which the class it holds writes:
  making an empty one, adding an element, how many it holds, the
  element at a place, and removing the list; see 'planLists'. So each
  class has to know whether some function somewhere hands a list of it
  around: 'getListKinds' goes through the whole tree once for that,
  for the maps as well, and keeps what it found on the tree.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isUsedBy(plan: Record) -> bool:
    """Says whether a ritual takes or gives a list, or is one of the
    rituals of a list itself."""
    if plan['kind'] == 'list':
      return True
    giving = plan.get('giving') or dict()
    if giving.get('kind') == 'list':
      return True
    arguments = plan.get('arguments') or ()
    return any(a['passing'].get('kind') == 'list' for a in arguments)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The kinds of list the functions of the tree hand around are kept
  #  in a dict the tree gives for them, 'DependencyTree.getKept'. The
  #  lock keeps two threads from both going through the tree for them.
  __list_kinds_lock__ = threading.Lock()

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('list',)

  def getListKinds(self) -> Dict[Tuple[str, str], Record]:
    """
    Gives every kind of list the functions of Qt take or give, as
    'findListKind' describes it, under the part of the class it holds
    and its tag, as ('QtCore', 'QUrl'); and every kind of map, as
    'MapExpert.findMapKind' describes it, the same way.

    Found for you by going through every class the tree knows, once
    for each tree. The class a kind holds writes the rituals of that
    kind, and its cute class collects the kind, so each has to know
    whether some function somewhere hands such a list around.
    """
    kept = self.getGenerator().getDependencyTree().getKept('list kinds')
    with self.__list_kinds_lock__:
      if 'found' not in kept:
        kept['found'] = self._findListKinds()
      return kept['found']

  def getOwnListKinds(self) -> List[Record]:
    """Gives the kinds of list that hold the class, as 'QList<QUrl>'
    for QUrl and 'QList<QAction *>' for QAction: most classes none."""
    generator = self.getGenerator()
    className, partName = generator.getClassName(), generator.getPartName()
    return [
        listed for (holder, _), listed in self.getListKinds().items()
        if 'listType' in listed and listed['holds'] == className
        and holder == partName and listed['crossing'] != 'text'
    ]

  def getListNames(self, listed: Record) -> List[str]:
    """Gives the names Qt itself has for one kind of list, as
    'QModelIndexList' for 'QList<QModelIndex>': for most kinds none."""
    aliases = self.getGenerator()._getTypeTables()['aliases']
    return sorted(
        name for name, meant in aliases.items()
        if meant == listed['listType'] and name.isidentifier()
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _findListKinds(self) -> Dict[Tuple[str, str], Record]:
    """Does the going through the tree for 'getListKinds', which keeps
    the answer."""
    generator = self.getGenerator()
    tree = generator.getDependencyTree()
    kinds = dict()  # type: Dict[Tuple[str, str], Record]
    wanted = ('CXXMethodDecl', 'CXXConstructorDecl')
    cute = tree.getCuteNames()
    for classKey in tree.getClasses():
      if classKey not in cute:
        #  No function of Python hands its lists around.
        continue
      other = generator._getGenerator(classKey)
      aliases = other._getTypeTables()['aliases']
      for member in other._readRecord(classKey[1]).get('inner', ()):
        if member.get('kind') not in wanted:
          continue
        given = CppText.splitFunctionType(member['type']['qualType'])[0]
        types = [given, *(
            child['type']['qualType']
            for child in member.get('inner', ())
            if isinstance(child, dict) and child.get('kind') == 'ParmVarDecl'
        )]
        for cppType in types:
          bare = cppType.replace('const ', '').replace(' &', '').strip()
          templated = any(
              mark in cppType for mark in ('QList<', 'QMap<', 'QHash<'))
          if not templated and bare not in aliases:
            #  A list is written 'QList<...>', or by a second name Qt
            #  has for one, as 'QStringList'. Anything else is spared
            #  the spelling out.
            continue
          spelled = other._spellOutside(cppType)
          for found in (
              other._findListKind(spelled), other._findMapKind(spelled)):
            if found is None:
              continue
            #  The kind is under the part of the class it holds, as
            #  that class sees it: a list of QtGraphs' 'QBarSet *' is
            #  another kind than one of QtCharts' 'QBarSet *'.
            try:
              holder = other._keyOf(found['holds'])[0]
            except LookupError:
              holder = ''
            kinds.setdefault((holder, found['tag']), found)
    return kinds

  def findListKind(self, cppType: str) -> Optional[Record]:
    """
    Says which kind of list a type hands around as a value. Qt has one
    class of list for each thing a list can hold: 'QList<QUrl>',
    'QList<QAction *>', and 'QStringList', its second name for
    'QList<QString>'.

    Parameters
    ----------

    cppType : str
      A type with every name in full, as 'QList<QUrl>', 'const
      QList<QUrl> &' or 'QStringList'.

    Returns
    -------

    Optional[Record]
      None for a type that is no list handed around as a value, and for
      a list of something that cannot be an element yet: a number, an
      enum, a pair, a class Qt writes inside another. Else 'listType':
      the list as C++ writes it;
      'element': what it holds, as C++ writes it; 'crossing': how one
      element crosses, 'value', 'address' or 'text'; 'holds': the class
      of the element; 'tag': the kind as the names of its rituals have
      it, as 'QUrl' and 'QAction_ptr'.
    """
    if cppType.endswith(' &'):
      if not cppType.startswith('const '):
        return None
      cppType = cppType[:-2]
    if cppType.startswith('const '):
      cppType = cppType[6:]
    generator = self.getGenerator()
    cppType = generator._followAliases(cppType.strip())
    if not cppType.startswith('QList<') or not cppType.endswith('>'):
      return None
    element = cppType[len('QList<'):-1].strip()
    tables = generator._getTypeTables()
    if element == ValueExpert.getTextName():
      crossing, holds, tag = 'text', element, element
    elif element.endswith(' *') and element[:-2] in tables['classes']:
      crossing, holds = 'address', element[:-2]
      tag = '%s_ptr' % holds
    elif element in tables['copyable']:
      crossing, holds, tag = 'value', element, element
    else:
      return None
    if '::' in holds:
      #  A class Qt writes inside another: not as an element yet.
      return None
    return dict(
        listType='QList<%s>' % element, element=element,
        crossing=crossing, holds=holds, tag=tag,
    )

  def claims(self, written: str, plain: str) -> bool:
    """Claims a list handed around as a value; see 'findListKind'."""
    return True if self.findListKind(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the list crosses as a value does: by the address of
    the C++ list. The kind is under 'listed'."""
    listed = self.findListKind(plain)
    return dict(
        kind='list', word='address', className=listed['listType'],
        listed=listed,
    )

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """Qt reads the list at the address, and the header of what it
    holds has to be known for that."""
    taken = 'const %s *' % passing['className']
    return taken, '*%s' % name, (passing['listed']['holds'],)

  def writeGiven(self, given: str, giving: Record) -> Given:
    """A copy of the list is made here, and its address goes back."""
    className = giving['className']
    opening = 'return new %s(' % className
    return '%s *' % className, opening, '));', (giving['listed']['holds'],)

  def planLists(self) -> List[Record]:
    """
    Works out the five rituals of each kind of list that holds the
    class: the one making an empty list, the one adding an element, the
    one giving how many it holds, the one giving the element at a
    place, and the one removing the list.
    """
    from . import RitualFileExpert
    fileExpert = self.getGenerator().getExpert(RitualFileExpert)
    plans = []  # type: List[Record]
    for listed in self.getOwnListKinds():
      listType, element = listed['listType'], listed['element']
      byValue = listed['crossing'] == 'value'
      handed = 'const %s *' % element if byValue else element
      back = '%s *' % element if byValue else element
      shapes = (
          ('make', '%s::QList()' % listType, '%s *' % listType, (),
           ('address',), 'return new %s();' % listType),
          ('add', 'void %s::append(const %s &value)' % (listType, element),
           'void', (('self', '%s *' % listType), ('element', handed)),
           ('nothing', 'address', 'address'),
           'self->append(%selement);' % ('*' if byValue else '')),
          ('size', 'qsizetype %s::size() const' % listType, 'long long',
           (('self', 'const %s *' % listType),), ('long long', 'address'),
           'return self->size();'),
          ('at', 'const %s &%s::at(qsizetype i) const' % (element, listType),
           back, (('self', 'const %s *' % listType), ('index', 'long long')),
           ('address', 'address', 'long long'),
           'return new %s(self->at(index));' % element if byValue
           else 'return self->at(index);'),
          ('drop', '%s::~QList()' % listType, 'void',
           (('self', '%s *' % listType),), ('nothing', 'address'),
           'delete self;'),
      )
      for role, shown, gives, takes, row, line in shapes:
        plan = dict(
            ritualName='ritual_list_%s_%s' % (role, listed['tag']),
            function=shown, kind='list', gives=gives, takes=takes,
            row=row, needs=(), unknownTypes=(), unsureNumbers=(),
            words=(), variadic=False, name='', arguments=(), giving=None,
            inPlace=False, listed=listed, listRole=role,
        )
        plan['text'] = fileExpert.writeRitual(plan, ['  %s' % line])
        plans.append(plan)
    return plans
