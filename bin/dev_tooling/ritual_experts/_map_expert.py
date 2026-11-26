"""MapExpert says how a map of Qt crosses, and writes the rituals of
each kind of map."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert, ValueExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]


class MapExpert(TypeExpert):
  """
  Says how a map of Qt crosses: as a value does, by the address of the
  C++ map. Qt has one class of map for each kind of key and value:
  'QMap<int, QVariant>', 'QHash<int, QByteArray>', and 'QVariantMap',
  its second name for 'QMap<QString, QVariant>'.

  A map needs rituals of its own, which the class of its values
  writes; see 'planMaps'. The kinds of map the functions of the tree
  hand around are found in the same going through the tree as those of
  the lists; see 'ListExpert.getListKinds'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isUsedBy(plan: Record) -> bool:
    """Says whether a ritual takes or gives a map, or is one of the
    rituals of a map itself."""
    if plan['kind'] == 'map':
      return True
    giving = plan.get('giving') or dict()
    if giving.get('kind') == 'map':
      return True
    arguments = plan.get('arguments') or ()
    return any(a['passing'].get('kind') == 'map' for a in arguments)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the one kind of record this expert gives."""
    return ('map',)

  def getOwnMapKinds(self) -> List[Record]:
    """Gives the kinds of map whose values are of the class, as
    'QMap<int, QVariant>' for QVariant: most classes none. They are
    found in the same going through the tree as the lists."""
    generator = self.getGenerator()
    className, partName = generator.getClassName(), generator.getPartName()
    return [
        mapped for (holder, _), mapped in generator.getListKinds().items()
        if 'mapType' in mapped and mapped['holds'] == className
        and holder == partName
    ]

  def getMapNames(self, mapped: Record) -> List[str]:
    """Gives the names Qt itself has for one kind of map, as
    'QVariantMap' for 'QMap<QString, QVariant>': for most kinds none."""
    aliases = self.getGenerator()._getTypeTables()['aliases']
    return sorted(
        name for name, meant in aliases.items()
        if meant == mapped['mapType'] and name.isidentifier()
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def findMapKind(self, cppType: str) -> Optional[Record]:
    """
    Says which kind of map a type hands around as a value. Qt has one
    class of map for each kind of key and value: 'QMap<int, QVariant>',
    'QHash<int, QByteArray>', and 'QVariantMap', its second name for
    'QMap<QString, QVariant>'.

    Parameters
    ----------

    cppType : str
      A type with every name in full.

    Returns
    -------

    Optional[Record]
      None for a type that is no map handed around as a value, and for
      a map that cannot be passed yet: its keys are neither 'int' nor
      text, or its values are no class written inside no other. Else
      'mapType': the map as C++ writes it; 'pattern': 'QMap' or
      'QHash'; 'key': the keys, as C++ writes them; 'keyWord': their
      word in a row, 'int' or 'text'; 'value': the values, as C++
      writes them; 'crossing': how one value crosses, 'value' or
      'address'; 'holds': the class of the values; 'tag': the kind as
      the names of its rituals have it, as 'QMap_int_QVariant'.
    """
    if cppType.endswith(' &'):
      if not cppType.startswith('const '):
        return None
      cppType = cppType[:-2]
    if cppType.startswith('const '):
      cppType = cppType[6:]
    generator = self.getGenerator()
    cppType = generator._followAliases(cppType.strip())
    pattern = cppType.partition('<')[0]
    if pattern not in ('QMap', 'QHash') or not cppType.endswith('>'):
      return None
    key, comma, value = cppType[len(pattern) + 1:-1].partition(',')
    key, value = key.strip(), value.strip()
    if not comma:
      return None
    tables = generator._getTypeTables()
    textName = ValueExpert.getTextName()
    if generator._followAliases(key) == 'int':
      keyWord, keyTag = 'int', 'int'
    elif key == textName:
      keyWord, keyTag = 'text', key
    else:
      return None
    if value.endswith(' *') and value[:-2] in tables['classes']:
      crossing, holds = 'address', value[:-2]
    elif value in tables['copyable'] and value != textName:
      crossing, holds = 'value', value
    else:
      return None
    if '::' in holds:
      return None
    ending = '_ptr' if crossing == 'address' else ''
    return dict(
        mapType='%s<%s, %s>' % (pattern, key, value), pattern=pattern,
        key=key, keyWord=keyWord, value=value, crossing=crossing,
        holds=holds, tag='%s_%s_%s%s' % (pattern, keyTag, holds, ending),
    )

  def claims(self, written: str, plain: str) -> bool:
    """Claims a map handed around as a value; see 'findMapKind'."""
    return True if self.findMapKind(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says that the map crosses as a value does too. The kind is under
    'mapped'."""
    mapped = self.findMapKind(plain)
    return dict(
        kind='map', word='address', className=mapped['mapType'],
        mapped=mapped,
    )

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """Qt reads the map at the address, and the header of what it holds
    has to be known for that."""
    taken = 'const %s *' % passing['className']
    return taken, '*%s' % name, (passing['mapped']['holds'],)

  def writeGiven(self, given: str, giving: Record) -> Given:
    """A copy of the map is made here, and its address goes back."""
    className = giving['className']
    opening = 'return new %s(' % className
    return '%s *' % className, opening, '));', (giving['mapped']['holds'],)

  def planMaps(self) -> List[Record]:
    """
    Works out the eight rituals of each kind of map whose values are
    of the class: the one making an empty map, the one putting a value
    at a key, the one giving how many keys it has, the ones giving the
    key and the value at a place, the one saying whether it has a key,
    the one giving the value at a key, and the one removing the map.
    """
    from . import RitualFileExpert
    fileExpert = self.getGenerator().getExpert(RitualFileExpert)
    plans = []  # type: List[Record]
    for mapped in self.getOwnMapKinds():
      mapType, value = mapped['mapType'], mapped['value']
      byValue = mapped['crossing'] == 'value'
      byText = mapped['keyWord'] == 'text'
      keyTaken = 'const %s *' % mapped['key'] if byText else 'int'
      keyGiven = '%s *' % mapped['key'] if byText else 'int'
      keyHanded = '*key' if byText else 'key'
      keyBack = '*std::next(self->keyBegin(), index)'
      if byText:
        keyBack = 'new %s(%s)' % (mapped['key'], keyBack)
      taken = 'const %s *' % value if byValue else value
      given = '%s *' % value if byValue else value
      handed = '*value' if byValue else 'value'
      word = mapped['keyWord']
      own, read = '%s *' % mapType, 'const %s *' % mapType

      def back(found: str) -> str:
        """What goes back for a value found in the map."""
        return 'new %s(%s)' % (value, found) if byValue else found

      shapes = (
          ('make', '%s()' % mapType, own, (), ('address',),
           'return new %s();' % mapType),
          ('put', 'insert(const Key &key, const T &value)', 'void',
           (('self', own), ('key', keyTaken), ('value', taken)),
           ('nothing', 'address', word, 'address'),
           'self->insert(%s, %s);' % (keyHanded, handed)),
          ('size', 'size() const', 'long long', (('self', read),),
           ('long long', 'address'), 'return self->size();'),
          ('key', 'the key at a place', keyGiven,
           (('self', read), ('index', 'long long')),
           (word, 'address', 'long long'), 'return %s;' % keyBack),
          ('value', 'the value at a place', given,
           (('self', read), ('index', 'long long')),
           ('address', 'address', 'long long'),
           'return %s;' % back('*std::next(self->constBegin(), index)')),
          ('has', 'contains(const Key &key) const', 'bool',
           (('self', read), ('key', keyTaken)), ('bool', 'address', word),
           'return self->contains(%s);' % keyHanded),
          ('get', 'value(const Key &key) const', given,
           (('self', read), ('key', keyTaken)),
           ('address', 'address', word),
           'return %s;' % back('self->value(%s)' % keyHanded)),
          ('drop', '~%s()' % mapped['pattern'], 'void', (('self', own),),
           ('nothing', 'address'), 'delete self;'),
      )
      for role, shown, gives, takes, row, line in shapes:
        plan = dict(
            ritualName='ritual_map_%s_%s' % (role, mapped['tag']),
            function='%s: %s' % (mapType, shown), kind='map',
            gives=gives, takes=takes, row=row, needs=(),
            unknownTypes=(), unsureNumbers=(), words=(), variadic=False,
            name='', arguments=(), giving=None, inPlace=False,
            mapped=mapped, mapRole=role,
        )
        plan['text'] = fileExpert.writeRitual(plan, ['  %s' % line])
        plans.append(plan)
    return plans
