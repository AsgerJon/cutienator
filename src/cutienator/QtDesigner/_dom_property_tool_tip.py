"""
DomPropertyToolTip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomPropertyToolTip to be private: it declares the class in a
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


class DomPropertyToolTip(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomPropertyToolTip: a plain Python object standing in
  front of one C++ DomPropertyToolTip.

  What exists
  -----------

  Every function of Qt's DomPropertyToolTip that has a ritual and that Python
  can call so far, 4 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomPropertyToolTip::~DomPropertyToolTip()': the destructor: Python
    never removes a C++ DomPropertyToolTip.
  - Qt's 'void DomPropertyToolTip::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomPropertyToolTip::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomPropertyToolTip is created at the first use, not by
    'DomPropertyToolTip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomPropertyToolTip.
  - Each name of Qt's DomPropertyToolTip that has no cute function yet,
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
  __qt_class__ = 'DomPropertyToolTip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomPropertyToolTip::hasAttributeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertytooltip.html#hasAttributeName
    """
    #  bool DomPropertyToolTip::hasAttributeName() const
    return self.uglySide.call(
        'ritual_ZNK18DomPropertyToolTip16hasAttributeNameEv',
    )

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomPropertyToolTip::attributeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertytooltip.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomPropertyToolTip::attributeName() const
    return self.uglySide.call(
        'ritual_ZNK18DomPropertyToolTip13attributeNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomPropertyToolTip::setAttributeName(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertytooltip.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomPropertyToolTip::setAttributeName(const QString &a)
    self.uglySide.call(
        'ritual_ZN18DomPropertyToolTip16setAttributeNameERK7QString', a,
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
    Notes what was given, for Qt's
    'DomPropertyToolTip::DomPropertyToolTip()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertytooltip.html#DomPropertyToolTip
    """
    #  DomPropertyToolTip::DomPropertyToolTip()
    self._noteCreation(DomPropertyToolTip, lambda: Rituals.call(
        'ritual_ZN18DomPropertyToolTipC1Ev',
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

  def clearAttributeName(self) -> None:
    """
    Calls Qt's 'void DomPropertyToolTip::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertytooltip.html#clearAttributeName
    """
    #  void DomPropertyToolTip::clearAttributeName()
    self.uglySide.call('ritual_ZN18DomPropertyToolTip18clearAttributeNameEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomPropertyToolTip::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPropertyToolTip.read' has no cute function yet. Qt's 'void "
        "DomPropertyToolTip::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomPropertyToolTip::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomPropertyToolTip.write' has no cute function yet. Qt's 'void "
        "DomPropertyToolTip::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomPropertyToolTip *>': the list of DomPropertyToolTip, which
#  'QList[DomPropertyToolTip]' gives. It is made here, so that there is one
#  as soon as there can be a DomPropertyToolTip.
QList.createKind(
    DomPropertyToolTip, 'address',
    make='ritual_list_make_DomPropertyToolTip_ptr',
    add='ritual_list_add_DomPropertyToolTip_ptr',
    size='ritual_list_size_DomPropertyToolTip_ptr',
    at='ritual_list_at_DomPropertyToolTip_ptr',
    drop='ritual_list_drop_DomPropertyToolTip_ptr',
)
