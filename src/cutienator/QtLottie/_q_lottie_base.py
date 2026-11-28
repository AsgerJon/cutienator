"""
QLottieBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiebase_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieBase to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QLottieLiteral
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QJsonObject, QSize, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieBase: a plain Python object standing in front
  of one C++ QLottieBase.

  C++ hands a QLottieBase around as a copy, so every C++ QLottieBase behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieBase that has a ritual and that Python can
  call so far, 25 names in all: 'clone', 'setProperty', 'name', 'setName',
  'type', 'setType', 'isShapeElement', 'isPathElement', 'parse',
  'definition', 'active', 'hidden', 'parent', 'setParent', 'children',
  'prependChild', 'insertChildBeforeLast', 'appendChild', 'findChild',
  'updateProperties', 'layerSize', 'isStructureDumping', 'resolveTopRoot',
  'topRoot', 'resolveExpression'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieBase::~QLottieBase()': the destructor: Python removes its
    C++ QLottieBase by it, and has no other use for it.
  - Qt's 'void QLottieBase::render(QLottieRenderer &renderer) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QLottieBase::renderChildren(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'bool QLottieBase::checkRequiredKeys(const QJsonObject &definition,
    const QLatin1StringView type, const QList<QLatin1StringView> &keys, const
    QString &name) const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLottieBase is created at the first use, not by
    'QLottieBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieBase back gives a copy the ritual made for
    Python, in a new cute QLottieBase.
  - Each name of Qt's QLottieBase that has no cute function yet,
    'checkRequiredKeys', 'render', 'renderChildren', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieBase'

  #  A C++ QLottieBase Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieBase'

  #  The functions Qt calls itself that QLottieBase is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'render': (
          'void QLottieBase::render(QLottieRenderer &) const',
      ),
  }

  #  The functions Qt calls itself that QLottieBase is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZNK11QLottieBase5cloneEv',
           ('address', 'address', 'QtLottie:QLottieBase'),
           ()),
      ),
      'setProperty': (
          ('_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8'
           'QVariant',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtLottie:QLottieLiteral.PropertyType'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'parse': (
          ('_ZN11QLottieBase5parseERK11QJsonObject',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QJsonObject'),
           )),
      ),
      'active': (
          ('_ZNK11QLottieBase6activeEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'findChild': (
          ('_ZN11QLottieBase9findChildERK7QString',
           ('address', 'address', 'QtLottie:QLottieBase'),
           (
               ('address', 'text', ''),
           )),
      ),
      'updateProperties': (
          ('_ZN11QLottieBase16updatePropertiesEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'layerSize': (
          ('_ZNK11QLottieBase9layerSizeEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
      ),
  }

  #  Qt's '~QLottieBase()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieBase behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QLottieBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieBase::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieBase::clone() const
    ritual = 'ritual_ZNK11QLottieBase5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieBase5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QLottieBase::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLottieBase::name() const
    return self.uglySide.call('ritual_ZNK11QLottieBase4nameEv')

  def type(self) -> int:
    """
    Calls Qt's 'int QLottieBase::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#type
    """
    #  int QLottieBase::type() const
    return self.uglySide.call('ritual_ZNK11QLottieBase4typeEv')

  def isShapeElement(self) -> bool:
    """
    Calls Qt's 'bool QLottieBase::isShapeElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#isShapeElement
    """
    #  bool QLottieBase::isShapeElement() const
    return self.uglySide.call('ritual_ZNK11QLottieBase14isShapeElementEv')

  def isPathElement(self) -> bool:
    """
    Calls Qt's 'bool QLottieBase::isPathElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#isPathElement
    """
    #  bool QLottieBase::isPathElement() const
    return self.uglySide.call('ritual_ZNK11QLottieBase13isPathElementEv')

  def definition(self) -> QJsonObject:
    """
    Calls Qt's 'const QJsonObject &QLottieBase::definition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#definition

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  const QJsonObject &QLottieBase::definition() const
    address = self.uglySide.call('ritual_ZNK11QLottieBase10definitionEv')
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @overload(int)
  def active(self, frame: int) -> bool:
    """
    Calls Qt's 'bool QLottieBase::active(int frame) const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#active

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  bool QLottieBase::active(int frame) const
    ritual = 'ritual_ZNK11QLottieBase6activeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieBase6activeEi'
    return self.uglySide.call(ritual, frame)

  def hidden(self) -> bool:
    """
    Calls Qt's 'bool QLottieBase::hidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#hidden
    """
    #  bool QLottieBase::hidden() const
    return self.uglySide.call('ritual_ZNK11QLottieBase6hiddenEv')

  def parent(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieBase::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#parent

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieBase::parent() const
    address = self.uglySide.call('ritual_ZNK11QLottieBase6parentEv')
    return QLottieBase._cuteAt(address)

  def children(self) -> QList[QLottieBase]:
    """
    Calls Qt's 'const QList<QLottieBase *> &QLottieBase::children() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#children

    Returns
    -------

    QList[QLottieBase]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QLottieBase *> &QLottieBase::children() const
    address = self.uglySide.call('ritual_ZNK11QLottieBase8childrenEv')
    return QList[QLottieBase]._cuteOwning(address)

  def layerSize(self) -> QSize:
    """
    Calls Qt's 'QSize QLottieBase::layerSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#layerSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QLottieBase::layerSize() const
    ritual = 'ritual_ZNK11QLottieBase9layerSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QLottieBase9layerSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isStructureDumping(self) -> bool:
    """
    Calls Qt's 'bool QLottieBase::isStructureDumping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebase.html#isStructureDumping
    """
    #  bool QLottieBase::isStructureDumping() const
    return self.uglySide.call(
        'ritual_ZNK11QLottieBase18isStructureDumpingEv',
    )

  def topRoot(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieBase::topRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#topRoot

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieBase::topRoot() const
    address = self.uglySide.call('ritual_ZNK11QLottieBase7topRootEv')
    return QLottieBase._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLottieLiteral.PropertyType, QVariant)
  def setProperty(
      self,
      propertyType: QLottieLiteral.PropertyType,
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QLottieBase::setProperty(QLottieLiteral::PropertyType
    propertyType, QVariant value)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#setProperty

    Parameters
    ----------

    propertyType : QLottieLiteral.PropertyType
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
    #      propertyType, QVariant value)
    ritual = (
        'ritual_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTyp'
        'eE8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QLottieBase11setPropertyEN14QLottieLiteral12Prope'
          'rtyTypeE8QVariant')
    return self.uglySide.call(
        ritual, propertyType.value, self._valueOf(value),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QLottieBase::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QLottieBase::setName(const QString &name)
    self.uglySide.call('ritual_ZN11QLottieBase7setNameERK7QString', name)

  @overload(int)
  def setType(self, type: int) -> None:
    """
    Calls Qt's 'void QLottieBase::setType(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#setType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QLottieBase::setType(int type)
    self.uglySide.call('ritual_ZN11QLottieBase7setTypeEi', type)

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, parent: Optional[QLottieBase]) -> None:
    """
    Calls Qt's 'void QLottieBase::setParent(QLottieBase *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#setParent

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLottieBase::setParent(QLottieBase *parent)
    self.uglySide.call(
        'ritual_ZN11QLottieBase9setParentEPS_', self._addressOf(parent),
    )

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
    Notes what was given, for Qt's 'QLottieBase::QLottieBase()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#QLottieBase
    """
    #  QLottieBase::QLottieBase()
    self._noteCreation(QLottieBase, lambda: Rituals.call(
        'ritual_ZN11QLottieBaseC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieBase) -> None:
    """
    Notes what was given, for Qt's 'QLottieBase::QLottieBase(const
    QLottieBase &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#QLottieBase

    Parameters
    ----------

    other : QLottieBase
      Passed on as a value: Qt reads the C++ QLottieBase, which stays
      Python's own.
    """
    #  QLottieBase::QLottieBase(const QLottieBase &other)
    self._noteCreation(QLottieBase, lambda: Rituals.call(
        'ritual_ZN11QLottieBaseC1ERKS_', self._valueOf(other),
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieBase::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieBase::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN11QLottieBase5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieBase5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @overload(THIS)
  @overload(NoneType)
  def prependChild(self, child: Optional[QLottieBase]) -> None:
    """
    Calls Qt's 'void QLottieBase::prependChild(QLottieBase *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#prependChild

    Parameters
    ----------

    child : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLottieBase::prependChild(QLottieBase *child)
    self.uglySide.call(
        'ritual_ZN11QLottieBase12prependChildEPS_', self._addressOf(child),
    )

  @overload(THIS)
  @overload(NoneType)
  def insertChildBeforeLast(self, child: Optional[QLottieBase]) -> None:
    """
    Calls Qt's 'void QLottieBase::insertChildBeforeLast(QLottieBase *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiebase.html#insertChildBeforeLast

    Parameters
    ----------

    child : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLottieBase::insertChildBeforeLast(QLottieBase *child)
    self.uglySide.call(
        'ritual_ZN11QLottieBase21insertChildBeforeLastEPS_',
        self._addressOf(child),
    )

  @overload(THIS)
  @overload(NoneType)
  def appendChild(self, child: Optional[QLottieBase]) -> None:
    """
    Calls Qt's 'void QLottieBase::appendChild(QLottieBase *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#appendChild

    Parameters
    ----------

    child : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLottieBase::appendChild(QLottieBase *child)
    self.uglySide.call(
        'ritual_ZN11QLottieBase11appendChildEPS_', self._addressOf(child),
    )

  @overload(str)
  def findChild(self, childName: str) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieBase::findChild(const QString
    &childName)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#findChild

    Parameters
    ----------

    childName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieBase::findChild(const QString &childName)
    ritual = 'ritual_ZN11QLottieBase9findChildERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieBase9findChildERK7QString'
    address = self.uglySide.call(ritual, childName)
    return QLottieBase._cuteAt(address)

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieBase::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieBase::updateProperties(int frame)
    ritual = 'ritual_ZN11QLottieBase16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QLottieBase16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  def resolveTopRoot(self) -> None:
    """
    Calls Qt's 'void QLottieBase::resolveTopRoot()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#resolveTopRoot
    """
    #  void QLottieBase::resolveTopRoot()
    self.uglySide.call('ritual_ZN11QLottieBase14resolveTopRootEv')

  @overload(QJsonObject)
  def resolveExpression(self, definition: QJsonObject) -> QJsonObject:
    """
    Calls Qt's 'const QJsonObject QLottieBase::resolveExpression(const
    QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiebase.html#resolveExpression

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  const QJsonObject QLottieBase::resolveExpression(const QJsonObject
    #      &definition)
    address = self.uglySide.call(
        'ritual_ZN11QLottieBase17resolveExpressionERK11QJsonObject',
        self._valueOf(definition),
    )
    from ..QtCore import QJsonObject
    return QJsonObject._cuteOwning(address)

  @staticmethod
  def checkRequiredKeys(*__, **_) -> Never:
    """
    Qt's 'bool QLottieBase::checkRequiredKeys(const QJsonObject &definition,
    const QLatin1StringView type, const QList<QLatin1StringView> &keys, const
    QString &name) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieBase.checkRequiredKeys' has no cute function yet. Qt's "
        "'bool QLottieBase::checkRequiredKeys(const QJsonObject "
        "&definition, const QLatin1StringView type, const "
        "QList<QLatin1StringView> &keys, const QString &name) const': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void QLottieBase::render(QLottieRenderer &renderer) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieBase.render' has no cute function yet. Qt's 'void "
        "QLottieBase::render(QLottieRenderer &renderer) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def renderChildren(*__, **_) -> Never:
    """
    Qt's 'void QLottieBase::renderChildren(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieBase.renderChildren' has no cute function yet. Qt's 'void "
        "QLottieBase::renderChildren(QLottieRenderer &renderer) const': "
        "takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QLottieBase *>': the list of QLottieBase, which
#  'QList[QLottieBase]' gives. It is made here, so that there is one as soon
#  as there can be a QLottieBase.
QList.createKind(
    QLottieBase, 'address',
    make='ritual_list_make_QLottieBase_ptr',
    add='ritual_list_add_QLottieBase_ptr',
    size='ritual_list_size_QLottieBase_ptr',
    at='ritual_list_at_QLottieBase_ptr',
    drop='ritual_list_drop_QLottieBase_ptr',
)
