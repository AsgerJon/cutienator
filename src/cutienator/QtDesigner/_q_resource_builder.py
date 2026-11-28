"""
QResourceBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/resourcebuilder_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QResourceBuilder to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDir, QVariant
  from . import DomProperty, DomResourceIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomProperty = WAIT['DomProperty']
  DomResourceIcon = WAIT['DomResourceIcon']
  QDir = WAIT['QDir']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QResourceBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QResourceBuilder: a plain Python object standing in
  front of one C++ QResourceBuilder.

  C++ hands a QResourceBuilder around as a copy, so every C++
  QResourceBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QResourceBuilder that has a ritual and that Python
  can call so far, 9 names in all: 'themeIconNames', 'themeIconIndex',
  'fullyQualifiedThemeIconName', 'loadResource', 'toNativeValue',
  'saveResource', 'isResourceProperty', 'isResourceType', 'iconStateFlags'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QResourceBuilder::~QResourceBuilder()': the destructor: Python
    removes its C++ QResourceBuilder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QResourceBuilder is created at the first use, not by
    'QResourceBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QResourceBuilder back gives a copy the ritual made
    for Python, in a new cute QResourceBuilder.
  """

  #  The enums Qt writes inside QResourceBuilder, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class IconStateFlags(CuteNum):
    """
    The enum 'QResourceBuilder::IconStateFlags' of Qt, with the 8 names Qt
    gives in it.
    """

    NormalOff = Kee[int](1)
    NormalOn = Kee[int](2)
    DisabledOff = Kee[int](4)
    DisabledOn = Kee[int](8)
    ActiveOff = Kee[int](16)
    ActiveOn = Kee[int](32)
    SelectedOff = Kee[int](64)
    SelectedOn = Kee[int](128)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def themeIconNames() -> QStringList:
    """
    Calls Qt's 'const QStringList &QResourceBuilder::themeIconNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#themeIconNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList &QResourceBuilder::themeIconNames()
    address = Rituals.call('ritual_ZN16QResourceBuilder14themeIconNamesEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  def themeIconIndex(name: str) -> int:
    """
    Calls Qt's 'int QResourceBuilder::themeIconIndex(QStringView name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#themeIconIndex

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QResourceBuilder::themeIconIndex(QStringView name)
    return Rituals.call(
        'ritual_ZN16QResourceBuilder14themeIconIndexE11QStringView', name,
    )

  @staticmethod
  @overload(int)
  def fullyQualifiedThemeIconName(i: int) -> str:
    """
    Calls Qt's 'QString QResourceBuilder::fullyQualifiedThemeIconName(int
    i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#fullyQualifiedThemeIconName

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QResourceBuilder::fullyQualifiedThemeIconName(int i)
    return Rituals.call(
        'ritual_ZN16QResourceBuilder27fullyQualifiedThemeIconNameEi', i,
    )

  @staticmethod
  @overload(DomResourceIcon)
  @overload(NoneType)
  def iconStateFlags(resIcon: Optional[DomResourceIcon]) -> int:
    """
    Calls Qt's 'int QResourceBuilder::iconStateFlags(const DomResourceIcon
    *resIcon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#iconStateFlags

    Parameters
    ----------

    resIcon : Optional[DomResourceIcon]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QResourceBuilder::iconStateFlags(const DomResourceIcon *resIcon)
    return Rituals.call(
        'ritual_ZN16QResourceBuilder14iconStateFlagsEPK15DomResourceIcon',
        CuteMixin._addressOf(resIcon),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QResourceBuilder'

  #  A C++ QResourceBuilder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QResourceBuilder'

  #  The functions Qt calls itself that QResourceBuilder is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'loadResource': (
          ('_ZNK16QResourceBuilder12loadResourceERK4QDirPK11DomProperty',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QDir'),
               ('address', 'address', 'QtDesigner:DomProperty'),
           )),
      ),
      'toNativeValue': (
          ('_ZNK16QResourceBuilder13toNativeValueERK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'saveResource': (
          ('_ZNK16QResourceBuilder12saveResourceERK4QDirRK8QVariant',
           ('address', 'address', 'QtDesigner:DomProperty'),
           (
               ('address', 'value', 'QtCore:QDir'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'isResourceProperty': (
          ('_ZNK16QResourceBuilder18isResourcePropertyEPK11DomProperty',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtDesigner:DomProperty'),
           )),
      ),
      'isResourceType': (
          ('_ZNK16QResourceBuilder14isResourceTypeERK8QVariant',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Qt's '~QResourceBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QResourceBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QResourceBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDir, DomProperty)
  @overload(QDir, NoneType)
  def loadResource(
      self,
      workingDirectory: QDir,
      property: Optional[DomProperty],
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QResourceBuilder::loadResource(const QDir
    &workingDirectory, const DomProperty *property) const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcebuilder.html#loadResource

    Parameters
    ----------

    workingDirectory : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    property : Optional[DomProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QResourceBuilder::loadResource(const QDir &workingDirectory,
    #      const DomProperty *property) const
    ritual = (
        'ritual_ZNK16QResourceBuilder12loadResourceERK4QDirPK11DomProperty')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QResourceBuilder12loadResourceERK4QDirPK11DomPro'
          'perty')
    address = self.uglySide.call(
        ritual, self._valueOf(workingDirectory), self._addressOf(property),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def toNativeValue(self, value: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QResourceBuilder::toNativeValue(const QVariant
    &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#toNativeValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QResourceBuilder::toNativeValue(const QVariant &value) const
    ritual = 'ritual_ZNK16QResourceBuilder13toNativeValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QResourceBuilder13toNativeValueERK8QVariant'
    address = self.uglySide.call(ritual, self._valueOf(value))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QDir, QVariant)
  def saveResource(
      self,
      workingDirectory: QDir,
      value: QVariant,
  ) -> Optional[DomProperty]:
    """
    Calls Qt's 'DomProperty *QResourceBuilder::saveResource(const QDir
    &workingDirectory, const QVariant &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qresourcebuilder.html#saveResource

    Parameters
    ----------

    workingDirectory : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    Optional[DomProperty]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomProperty *QResourceBuilder::saveResource(const QDir
    #      &workingDirectory, const QVariant &value) const
    ritual = 'ritual_ZNK16QResourceBuilder12saveResourceERK4QDirRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QResourceBuilder12saveResourceERK4QDirRK8QVarian'
          't')
    address = self.uglySide.call(
        ritual, self._valueOf(workingDirectory), self._valueOf(value),
    )
    from . import DomProperty
    return DomProperty._cuteAt(address)

  @overload(DomProperty)
  @overload(NoneType)
  def isResourceProperty(self, p: Optional[DomProperty]) -> bool:
    """
    Calls Qt's 'bool QResourceBuilder::isResourceProperty(const DomProperty
    *p) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#isResourceProperty

    Parameters
    ----------

    p : Optional[DomProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QResourceBuilder::isResourceProperty(const DomProperty *p) const
    ritual = (
        'ritual_ZNK16QResourceBuilder18isResourcePropertyEPK11DomProperty')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QResourceBuilder18isResourcePropertyEPK11DomProp'
          'erty')
    return self.uglySide.call(ritual, self._addressOf(p))

  @overload(QVariant)
  def isResourceType(self, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QResourceBuilder::isResourceType(const QVariant &value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#isResourceType

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QResourceBuilder::isResourceType(const QVariant &value) const
    ritual = 'ritual_ZNK16QResourceBuilder14isResourceTypeERK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QResourceBuilder14isResourceTypeERK8QVariant'
    return self.uglySide.call(ritual, self._valueOf(value))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QResourceBuilder::QResourceBuilder()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcebuilder.html#QResourceBuilder
    """
    #  QResourceBuilder::QResourceBuilder()
    self._noteCreation(QResourceBuilder, lambda: Rituals.call(
        'ritual_ZN16QResourceBuilderC1Ev',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
