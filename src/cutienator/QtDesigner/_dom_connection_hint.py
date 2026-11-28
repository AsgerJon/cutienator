"""
DomConnectionHint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomConnectionHint to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomConnectionHint(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomConnectionHint: a plain Python object standing in
  front of one C++ DomConnectionHint.

  What exists
  -----------

  Every function of Qt's DomConnectionHint that has a ritual and that Python
  can call so far, 12 names in all: 'hasAttributeType', 'attributeType',
  'setAttributeType', 'clearAttributeType', 'elementX', 'setElementX',
  'hasElementX', 'clearElementX', 'elementY', 'setElementY', 'hasElementY',
  'clearElementY'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomConnectionHint::~DomConnectionHint()': the destructor: Python
    never removes a C++ DomConnectionHint.
  - Qt's 'void DomConnectionHint::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomConnectionHint::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomConnectionHint is created at the first use, not by
    'DomConnectionHint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomConnectionHint.
  - Each name of Qt's DomConnectionHint that has no cute function yet,
    'read', 'write', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomConnectionHint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeType(self) -> bool:
    """
    Calls Qt's 'bool DomConnectionHint::hasAttributeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#hasAttributeType
    """
    #  bool DomConnectionHint::hasAttributeType() const
    return self.uglySide.call(
        'ritual_ZNK17DomConnectionHint16hasAttributeTypeEv',
    )

  def attributeType(self) -> str:
    """
    Calls Qt's 'QString DomConnectionHint::attributeType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#attributeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomConnectionHint::attributeType() const
    return self.uglySide.call(
        'ritual_ZNK17DomConnectionHint13attributeTypeEv',
    )

  def elementX(self) -> int:
    """
    Calls Qt's 'int DomConnectionHint::elementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnectionhint.html#elementX
    """
    #  int DomConnectionHint::elementX() const
    return self.uglySide.call('ritual_ZNK17DomConnectionHint8elementXEv')

  def hasElementX(self) -> bool:
    """
    Calls Qt's 'bool DomConnectionHint::hasElementX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnectionhint.html#hasElementX
    """
    #  bool DomConnectionHint::hasElementX() const
    return self.uglySide.call('ritual_ZNK17DomConnectionHint11hasElementXEv')

  def elementY(self) -> int:
    """
    Calls Qt's 'int DomConnectionHint::elementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnectionhint.html#elementY
    """
    #  int DomConnectionHint::elementY() const
    return self.uglySide.call('ritual_ZNK17DomConnectionHint8elementYEv')

  def hasElementY(self) -> bool:
    """
    Calls Qt's 'bool DomConnectionHint::hasElementY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnectionhint.html#hasElementY
    """
    #  bool DomConnectionHint::hasElementY() const
    return self.uglySide.call('ritual_ZNK17DomConnectionHint11hasElementYEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeType(self, a: str) -> None:
    """
    Calls Qt's 'void DomConnectionHint::setAttributeType(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#setAttributeType

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomConnectionHint::setAttributeType(const QString &a)
    self.uglySide.call(
        'ritual_ZN17DomConnectionHint16setAttributeTypeERK7QString', a,
    )

  @overload(int)
  def setElementX(self, a: int) -> None:
    """
    Calls Qt's 'void DomConnectionHint::setElementX(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domconnectionhint.html#setElementX

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomConnectionHint::setElementX(int a)
    self.uglySide.call('ritual_ZN17DomConnectionHint11setElementXEi', a)

  @overload(int)
  def setElementY(self, a: int) -> None:
    """
    Calls Qt's 'void DomConnectionHint::setElementY(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domconnectionhint.html#setElementY

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomConnectionHint::setElementY(int a)
    self.uglySide.call('ritual_ZN17DomConnectionHint11setElementYEi', a)

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
    Notes what was given, for Qt's 'DomConnectionHint::DomConnectionHint()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#DomConnectionHint
    """
    #  DomConnectionHint::DomConnectionHint()
    self._noteCreation(DomConnectionHint, lambda: Rituals.call(
        'ritual_ZN17DomConnectionHintC1Ev',
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

  def clearAttributeType(self) -> None:
    """
    Calls Qt's 'void DomConnectionHint::clearAttributeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#clearAttributeType
    """
    #  void DomConnectionHint::clearAttributeType()
    self.uglySide.call('ritual_ZN17DomConnectionHint18clearAttributeTypeEv')

  def clearElementX(self) -> None:
    """
    Calls Qt's 'void DomConnectionHint::clearElementX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#clearElementX
    """
    #  void DomConnectionHint::clearElementX()
    self.uglySide.call('ritual_ZN17DomConnectionHint13clearElementXEv')

  def clearElementY(self) -> None:
    """
    Calls Qt's 'void DomConnectionHint::clearElementY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnectionhint.html#clearElementY
    """
    #  void DomConnectionHint::clearElementY()
    self.uglySide.call('ritual_ZN17DomConnectionHint13clearElementYEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomConnectionHint::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomConnectionHint.read' has no cute function yet. Qt's 'void "
        "DomConnectionHint::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomConnectionHint::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomConnectionHint.write' has no cute function yet. Qt's 'void "
        "DomConnectionHint::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomConnectionHint *>': the list of DomConnectionHint, which
#  'QList[DomConnectionHint]' gives. It is made here, so that there is one as
#  soon as there can be a DomConnectionHint.
QList.createKind(
    DomConnectionHint, 'address',
    make='ritual_list_make_DomConnectionHint_ptr',
    add='ritual_list_add_DomConnectionHint_ptr',
    size='ritual_list_size_DomConnectionHint_ptr',
    at='ritual_list_at_DomConnectionHint_ptr',
    drop='ritual_list_drop_DomConnectionHint_ptr',
)
