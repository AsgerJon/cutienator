"""ValueExpert says how a value class crosses, text included: by the
address of the object."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from typing import TYPE_CHECKING

from . import TypeExpert

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, Optional, Tuple

  Record = Dict[str, Any]
  Taken = Tuple[str, str, Tuple[str, ...]]
  Given = Tuple[str, str, str, Tuple[str, ...]]
  Handed = Tuple[str, str, Tuple[str, str, str]]
  HandedBack = Tuple[str, Tuple[str, str, str], str]


class ValueExpert(TypeExpert):
  """
  Says how a value class crosses: a class C++ can copy, as 'QSize', in
  'QSize', 'const QSize' and 'const QSize &'. The ritual takes the
  address of one and hands Qt the object there, which Qt copies if it
  keeps it. For one given back, the ritual makes a copy with 'new' and
  gives its address: that copy is known to nobody else, and whoever
  called the ritual has to remove it.

  Text is a value class as well: Qt's 'QString', and the two classes
  that look at text held elsewhere, 'QStringView' and
  'QAnyStringView'. It is passed as a value of 'QString', and its word
  in the row is 'text', so Python passes a plain 'str'. Three kinds:
  'value', 'text' and 'view'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getTextName() -> str:
    """Gives the class of Qt that is text, 'QString'."""
    return ValueExpert.__text_name__

  @staticmethod
  def getViewNames() -> Tuple[str, ...]:
    """Gives the classes of Qt that look at text held elsewhere."""
    return ValueExpert.__view_names__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt that is text, and the classes of Qt that look at
  #  text held elsewhere. A ritual takes a 'QString' for each of them.
  __text_name__ = 'QString'
  __view_names__ = ('QAnyStringView', 'QStringView')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getKinds(self) -> Tuple[str, ...]:
    """Gives the three kinds of record this expert gives."""
    return ('value', 'text', 'view')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def findValueName(self, cppType: str) -> str:
    """
    Gives the class a type hands around as a value: 'QSize' for
    'QSize', 'const QSize' and 'const QSize &'. Gives '' for any other
    type, as 'QSize &' and 'QSize *', and for a class C++ cannot copy.
    """
    if cppType.endswith(' &'):
      if not cppType.startswith('const '):
        return ''
      cppType = cppType[:-2]
    if cppType.startswith('const '):
      cppType = cppType[6:]
    generator = self.getGenerator()
    cppType = generator._followAliases(cppType)
    if cppType in generator._getTypeTables()['copyable']:
      return cppType
    return ''

  def claims(self, written: str, plain: str) -> bool:
    """Claims a type handed around as a value; see 'findValueName'."""
    return True if self.findValueName(plain) else False

  def findPassing(self, written: str, plain: str) -> Optional[Record]:
    """Says how the value crosses, with its class as 'className'."""
    valueName = self.findValueName(plain)
    if valueName == self.__text_name__:
      return dict(kind='text', word='text', className=valueName)
    if valueName in self.__view_names__:
      return dict(kind='view', word='text', className=valueName)
    return dict(kind='value', word='address', className=valueName)

  def writeTaken(self, name: str, written: str, passing: Record) -> Taken:
    """The ritual takes the address of the object and hands Qt the
    object there. A look at text is made from the text for the call."""
    valueName = passing['className']
    if passing['kind'] == 'view':
      taken = 'const %s *' % self.__text_name__
      handed = '%s(*%s)' % (valueName, name)
      return taken, handed, (valueName, self.__text_name__)
    return 'const %s *' % valueName, '*%s' % name, (valueName,)

  def writeGiven(self, given: str, giving: Record) -> Given:
    """The copy is made here, and its address is what goes back. Of a
    look at text, the text is copied."""
    valueName = giving['className']
    needs = (valueName,)
    if giving['kind'] == 'view':
      needs = (valueName, self.__text_name__)
      valueName = self.__text_name__
      closing = ').toString());'
    else:
      closing = '));'
    return '%s *' % valueName, 'return new %s(' % valueName, closing, needs

  def handOver(
      self,
      name: str,
      written: str,
      passing: Record,
  ) -> Optional[Handed]:
    """The address of the object goes to Python. Of text, Python reads
    the letters off Qt's own text. A look at text is not handed over
    yet."""
    className = passing['className']
    if passing['kind'] == 'value':
      taken = 'const %s *' % className
      return taken, '&%s' % name, ('address', 'value', className)
    if passing['kind'] == 'text':
      taken = 'const %s *' % className
      return taken, '&%s' % name, ('address', 'text', '')
    return None

  def handBack(self, written: str, giving: Record) -> Optional[HandedBack]:
    """
    Python gives the address of an object, and the function gives a
    copy of it. Python makes a text of Qt for what it gives, and the
    C++ class of ours copies it and removes it. A function that gives
    the text it keeps, as 'const QString &', cannot give one made for
    the call; a look at text is not taken back yet.
    """
    className = giving['className']
    if giving['kind'] == 'text' and '&' not in written:
      return '%s *' % className, ('address', 'text', ''), '*given'
    if giving['kind'] == 'value':
      given = 'const %s *' % className
      return given, ('address', 'value', className), '*given'
    return None
