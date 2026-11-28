"""
DomSizePolicy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomSizePolicy to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomSizePolicy(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomSizePolicy: a plain Python object standing in
  front of one C++ DomSizePolicy.

  What exists
  -----------

  Every function of Qt's DomSizePolicy that has a ritual and that Python can
  call so far, 24 names in all: 'hasAttributeHSizeType',
  'attributeHSizeType', 'setAttributeHSizeType', 'clearAttributeHSizeType',
  'hasAttributeVSizeType', 'attributeVSizeType', 'setAttributeVSizeType',
  'clearAttributeVSizeType', 'elementHSizeType', 'setElementHSizeType',
  'hasElementHSizeType', 'clearElementHSizeType', 'elementVSizeType',
  'setElementVSizeType', 'hasElementVSizeType', 'clearElementVSizeType',
  'elementHorStretch', 'setElementHorStretch', 'hasElementHorStretch',
  'clearElementHorStretch', 'elementVerStretch', 'setElementVerStretch',
  'hasElementVerStretch', 'clearElementVerStretch'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomSizePolicy::~DomSizePolicy()': the destructor: Python never
    removes a C++ DomSizePolicy.
  - Qt's 'void DomSizePolicy::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomSizePolicy::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 32 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomSizePolicy is created at the first use, not by
    'DomSizePolicy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomSizePolicy.
  - Each name of Qt's DomSizePolicy that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomSizePolicy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeHSizeType(self) -> bool:
    """
    Calls Qt's 'bool DomSizePolicy::hasAttributeHSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#hasAttributeHSizeType
    """
    #  bool DomSizePolicy::hasAttributeHSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy21hasAttributeHSizeTypeEv',
    )

  def attributeHSizeType(self) -> str:
    """
    Calls Qt's 'QString DomSizePolicy::attributeHSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#attributeHSizeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomSizePolicy::attributeHSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy18attributeHSizeTypeEv',
    )

  def hasAttributeVSizeType(self) -> bool:
    """
    Calls Qt's 'bool DomSizePolicy::hasAttributeVSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#hasAttributeVSizeType
    """
    #  bool DomSizePolicy::hasAttributeVSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy21hasAttributeVSizeTypeEv',
    )

  def attributeVSizeType(self) -> str:
    """
    Calls Qt's 'QString DomSizePolicy::attributeVSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#attributeVSizeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomSizePolicy::attributeVSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy18attributeVSizeTypeEv',
    )

  def elementHSizeType(self) -> int:
    """
    Calls Qt's 'int DomSizePolicy::elementHSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#elementHSizeType
    """
    #  int DomSizePolicy::elementHSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy16elementHSizeTypeEv',
    )

  def hasElementHSizeType(self) -> bool:
    """
    Calls Qt's 'bool DomSizePolicy::hasElementHSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#hasElementHSizeType
    """
    #  bool DomSizePolicy::hasElementHSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy19hasElementHSizeTypeEv',
    )

  def elementVSizeType(self) -> int:
    """
    Calls Qt's 'int DomSizePolicy::elementVSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#elementVSizeType
    """
    #  int DomSizePolicy::elementVSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy16elementVSizeTypeEv',
    )

  def hasElementVSizeType(self) -> bool:
    """
    Calls Qt's 'bool DomSizePolicy::hasElementVSizeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#hasElementVSizeType
    """
    #  bool DomSizePolicy::hasElementVSizeType() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy19hasElementVSizeTypeEv',
    )

  def elementHorStretch(self) -> int:
    """
    Calls Qt's 'int DomSizePolicy::elementHorStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#elementHorStretch
    """
    #  int DomSizePolicy::elementHorStretch() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy17elementHorStretchEv',
    )

  def hasElementHorStretch(self) -> bool:
    """
    Calls Qt's 'bool DomSizePolicy::hasElementHorStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#hasElementHorStretch
    """
    #  bool DomSizePolicy::hasElementHorStretch() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy20hasElementHorStretchEv',
    )

  def elementVerStretch(self) -> int:
    """
    Calls Qt's 'int DomSizePolicy::elementVerStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#elementVerStretch
    """
    #  int DomSizePolicy::elementVerStretch() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy17elementVerStretchEv',
    )

  def hasElementVerStretch(self) -> bool:
    """
    Calls Qt's 'bool DomSizePolicy::hasElementVerStretch() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#hasElementVerStretch
    """
    #  bool DomSizePolicy::hasElementVerStretch() const
    return self.uglySide.call(
        'ritual_ZNK13DomSizePolicy20hasElementVerStretchEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeHSizeType(self, a: str) -> None:
    """
    Calls Qt's 'void DomSizePolicy::setAttributeHSizeType(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#setAttributeHSizeType

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomSizePolicy::setAttributeHSizeType(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomSizePolicy21setAttributeHSizeTypeERK7QString', a,
    )

  @overload(str)
  def setAttributeVSizeType(self, a: str) -> None:
    """
    Calls Qt's 'void DomSizePolicy::setAttributeVSizeType(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#setAttributeVSizeType

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomSizePolicy::setAttributeVSizeType(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomSizePolicy21setAttributeVSizeTypeERK7QString', a,
    )

  @overload(int)
  def setElementHSizeType(self, a: int) -> None:
    """
    Calls Qt's 'void DomSizePolicy::setElementHSizeType(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#setElementHSizeType

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomSizePolicy::setElementHSizeType(int a)
    self.uglySide.call('ritual_ZN13DomSizePolicy19setElementHSizeTypeEi', a)

  @overload(int)
  def setElementVSizeType(self, a: int) -> None:
    """
    Calls Qt's 'void DomSizePolicy::setElementVSizeType(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#setElementVSizeType

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomSizePolicy::setElementVSizeType(int a)
    self.uglySide.call('ritual_ZN13DomSizePolicy19setElementVSizeTypeEi', a)

  @overload(int)
  def setElementHorStretch(self, a: int) -> None:
    """
    Calls Qt's 'void DomSizePolicy::setElementHorStretch(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#setElementHorStretch

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomSizePolicy::setElementHorStretch(int a)
    self.uglySide.call('ritual_ZN13DomSizePolicy20setElementHorStretchEi', a)

  @overload(int)
  def setElementVerStretch(self, a: int) -> None:
    """
    Calls Qt's 'void DomSizePolicy::setElementVerStretch(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#setElementVerStretch

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomSizePolicy::setElementVerStretch(int a)
    self.uglySide.call('ritual_ZN13DomSizePolicy20setElementVerStretchEi', a)

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
    Notes what was given, for Qt's 'DomSizePolicy::DomSizePolicy()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domsizepolicy.html#DomSizePolicy
    """
    #  DomSizePolicy::DomSizePolicy()
    self._noteCreation(DomSizePolicy, lambda: Rituals.call(
        'ritual_ZN13DomSizePolicyC1Ev',
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

  def clearAttributeHSizeType(self) -> None:
    """
    Calls Qt's 'void DomSizePolicy::clearAttributeHSizeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#clearAttributeHSizeType
    """
    #  void DomSizePolicy::clearAttributeHSizeType()
    self.uglySide.call('ritual_ZN13DomSizePolicy23clearAttributeHSizeTypeEv')

  def clearAttributeVSizeType(self) -> None:
    """
    Calls Qt's 'void DomSizePolicy::clearAttributeVSizeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#clearAttributeVSizeType
    """
    #  void DomSizePolicy::clearAttributeVSizeType()
    self.uglySide.call('ritual_ZN13DomSizePolicy23clearAttributeVSizeTypeEv')

  def clearElementHSizeType(self) -> None:
    """
    Calls Qt's 'void DomSizePolicy::clearElementHSizeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#clearElementHSizeType
    """
    #  void DomSizePolicy::clearElementHSizeType()
    self.uglySide.call('ritual_ZN13DomSizePolicy21clearElementHSizeTypeEv')

  def clearElementVSizeType(self) -> None:
    """
    Calls Qt's 'void DomSizePolicy::clearElementVSizeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#clearElementVSizeType
    """
    #  void DomSizePolicy::clearElementVSizeType()
    self.uglySide.call('ritual_ZN13DomSizePolicy21clearElementVSizeTypeEv')

  def clearElementHorStretch(self) -> None:
    """
    Calls Qt's 'void DomSizePolicy::clearElementHorStretch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#clearElementHorStretch
    """
    #  void DomSizePolicy::clearElementHorStretch()
    self.uglySide.call('ritual_ZN13DomSizePolicy22clearElementHorStretchEv')

  def clearElementVerStretch(self) -> None:
    """
    Calls Qt's 'void DomSizePolicy::clearElementVerStretch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domsizepolicy.html#clearElementVerStretch
    """
    #  void DomSizePolicy::clearElementVerStretch()
    self.uglySide.call('ritual_ZN13DomSizePolicy22clearElementVerStretchEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomSizePolicy::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSizePolicy.read' has no cute function yet. Qt's 'void "
        "DomSizePolicy::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomSizePolicy::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSizePolicy.write' has no cute function yet. Qt's 'void "
        "DomSizePolicy::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
