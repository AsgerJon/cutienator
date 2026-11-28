"""
DomItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomItem to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomProperty = WAIT['DomProperty']


class DomItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomItem: a plain Python object standing in front of
  one C++ DomItem.

  What exists
  -----------

  Every function of Qt's DomItem that has a ritual and that Python can call
  so far, 12 names in all: 'hasAttributeRow', 'attributeRow',
  'setAttributeRow', 'clearAttributeRow', 'hasAttributeColumn',
  'attributeColumn', 'setAttributeColumn', 'clearAttributeColumn',
  'elementProperty', 'setElementProperty', 'elementItem', 'setElementItem'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomItem::~DomItem()': the destructor: Python never removes a C++
    DomItem.
  - Qt's 'void DomItem::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void DomItem::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomItem is created at the first use, not by 'DomItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomItem.
  - Each name of Qt's DomItem that has no cute function yet, 'read', 'write',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeRow(self) -> bool:
    """
    Calls Qt's 'bool DomItem::hasAttributeRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#hasAttributeRow
    """
    #  bool DomItem::hasAttributeRow() const
    return self.uglySide.call('ritual_ZNK7DomItem15hasAttributeRowEv')

  def attributeRow(self) -> int:
    """
    Calls Qt's 'int DomItem::attributeRow() const'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#attributeRow
    """
    #  int DomItem::attributeRow() const
    return self.uglySide.call('ritual_ZNK7DomItem12attributeRowEv')

  def hasAttributeColumn(self) -> bool:
    """
    Calls Qt's 'bool DomItem::hasAttributeColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#hasAttributeColumn
    """
    #  bool DomItem::hasAttributeColumn() const
    return self.uglySide.call('ritual_ZNK7DomItem18hasAttributeColumnEv')

  def attributeColumn(self) -> int:
    """
    Calls Qt's 'int DomItem::attributeColumn() const'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#attributeColumn
    """
    #  int DomItem::attributeColumn() const
    return self.uglySide.call('ritual_ZNK7DomItem15attributeColumnEv')

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomItem::elementProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomItem::elementProperty() const
    address = self.uglySide.call('ritual_ZNK7DomItem15elementPropertyEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementItem(self) -> QList[DomItem]:
    """
    Calls Qt's 'QList<DomItem *> DomItem::elementItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#elementItem

    Returns
    -------

    QList[DomItem]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomItem *> DomItem::elementItem() const
    address = self.uglySide.call('ritual_ZNK7DomItem11elementItemEv')
    return QList[DomItem]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAttributeRow(self, a: int) -> None:
    """
    Calls Qt's 'void DomItem::setAttributeRow(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#setAttributeRow

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomItem::setAttributeRow(int a)
    self.uglySide.call('ritual_ZN7DomItem15setAttributeRowEi', a)

  @overload(int)
  def setAttributeColumn(self, a: int) -> None:
    """
    Calls Qt's 'void DomItem::setAttributeColumn(int a)'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#setAttributeColumn

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomItem::setAttributeColumn(int a)
    self.uglySide.call('ritual_ZN7DomItem18setAttributeColumnEi', a)

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomItem::setElementProperty(const QList<DomProperty *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomItem::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN7DomItem18setElementPropertyERK5QListIP11DomPropertyE',
        self._valueOf(a),
    )

  @overload(QList[WAIT['DomItem']])
  def setElementItem(self, a: QList[DomItem]) -> None:
    """
    Calls Qt's 'void DomItem::setElementItem(const QList<DomItem *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#setElementItem

    Parameters
    ----------

    a : QList[DomItem]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomItem::setElementItem(const QList<DomItem *> &a)
    self.uglySide.call(
        'ritual_ZN7DomItem14setElementItemERK5QListIPS_E', self._valueOf(a),
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
    Notes what was given, for Qt's 'DomItem::DomItem()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#DomItem
    """
    #  DomItem::DomItem()
    self._noteCreation(DomItem, lambda: Rituals.call(
        'ritual_ZN7DomItemC1Ev',
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

  def clearAttributeRow(self) -> None:
    """
    Calls Qt's 'void DomItem::clearAttributeRow()'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#clearAttributeRow
    """
    #  void DomItem::clearAttributeRow()
    self.uglySide.call('ritual_ZN7DomItem17clearAttributeRowEv')

  def clearAttributeColumn(self) -> None:
    """
    Calls Qt's 'void DomItem::clearAttributeColumn()'.

    Qt's own words: https://doc.qt.io/qt-6/domitem.html#clearAttributeColumn
    """
    #  void DomItem::clearAttributeColumn()
    self.uglySide.call('ritual_ZN7DomItem20clearAttributeColumnEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomItem::read(QXmlStreamReader &reader)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomItem.read' has no cute function yet. Qt's 'void "
        "DomItem::read(QXmlStreamReader &reader)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomItem::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomItem.write' has no cute function yet. Qt's 'void "
        "DomItem::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomItem *>': the list of DomItem, which 'QList[DomItem]'
#  gives. It is made here, so that there is one as soon as there can be a
#  DomItem.
QList.createKind(
    DomItem, 'address',
    make='ritual_list_make_DomItem_ptr',
    add='ritual_list_add_DomItem_ptr',
    size='ritual_list_size_DomItem_ptr',
    at='ritual_list_at_DomItem_ptr',
    drop='ritual_list_drop_DomItem_ptr',
)
