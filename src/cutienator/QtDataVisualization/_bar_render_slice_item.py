"""
BarRenderSliceItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/barrenderitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means BarRenderSliceItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import BarRenderItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class BarRenderSliceItem(BarRenderItem):
  """
  The cute side of Qt's BarRenderSliceItem: a plain Python object standing in
  front of one C++ BarRenderSliceItem.

  It is built on the cute 'BarRenderItem', as Qt's BarRenderSliceItem is
  built on Qt's BarRenderItem, and has everything that class has.

  C++ hands a BarRenderSliceItem around as a copy, so every C++
  BarRenderSliceItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's BarRenderSliceItem that has a ritual and that Python
  can call so far, 3 names in all: 'setItem', 'setSliceLabel', 'sliceLabel'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'BarRenderSliceItem &BarRenderSliceItem::operator=(const
    BarRenderSliceItem &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'BarRenderSliceItem::~BarRenderSliceItem()': the destructor: Python
    removes its C++ BarRenderSliceItem by it, and has no other use for it.
  - Qt's 'LabelItem &BarRenderSliceItem::sliceLabelItem()': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ BarRenderSliceItem is created at the first use, not by
    'BarRenderSliceItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a BarRenderSliceItem back gives a copy the ritual made
    for Python, in a new cute BarRenderSliceItem.
  - Each name of Qt's BarRenderSliceItem that has no cute function yet,
    'sliceLabelItem', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'BarRenderSliceItem'

  #  Qt's '~BarRenderSliceItem()'. Naming it makes this a value class: Python
  #  owns every C++ BarRenderSliceItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18BarRenderSliceItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sliceLabel(self) -> str:
    """
    Calls Qt's 'const QString &BarRenderSliceItem::sliceLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/barrendersliceitem.html#sliceLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &BarRenderSliceItem::sliceLabel() const
    return self.uglySide.call('ritual_ZNK18BarRenderSliceItem10sliceLabelEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(BarRenderItem)
  def setItem(self, renderItem: BarRenderItem) -> None:
    """
    Calls Qt's 'void BarRenderSliceItem::setItem(const BarRenderItem
    &renderItem)'.

    Qt's own words: https://doc.qt.io/qt-6/barrendersliceitem.html#setItem

    Parameters
    ----------

    renderItem : BarRenderItem
      Passed on as a value: Qt reads the C++ BarRenderItem, which stays
      Python's own.
    """
    #  void BarRenderSliceItem::setItem(const BarRenderItem &renderItem)
    self.uglySide.call(
        'ritual_ZN18BarRenderSliceItem7setItemERK13BarRenderItem',
        self._valueOf(renderItem),
    )

  @overload(str)
  def setSliceLabel(self, label: str) -> None:
    """
    Calls Qt's 'void BarRenderSliceItem::setSliceLabel(const QString
    &label)'.

    Qt's own words:
    https://doc.qt.io/qt-6/barrendersliceitem.html#setSliceLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void BarRenderSliceItem::setSliceLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN18BarRenderSliceItem13setSliceLabelERK7QString', label,
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
    'BarRenderSliceItem::BarRenderSliceItem()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/barrendersliceitem.html#BarRenderSliceItem
    """
    #  BarRenderSliceItem::BarRenderSliceItem()
    self._noteCreation(BarRenderSliceItem, lambda: Rituals.call(
        'ritual_ZN18BarRenderSliceItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: BarRenderSliceItem) -> None:
    """
    Notes what was given, for Qt's
    'BarRenderSliceItem::BarRenderSliceItem(const BarRenderSliceItem
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/barrendersliceitem.html#BarRenderSliceItem

    Parameters
    ----------

    other : BarRenderSliceItem
      Passed on as a value: Qt reads the C++ BarRenderSliceItem, which stays
      Python's own.
    """
    #  BarRenderSliceItem::BarRenderSliceItem(const BarRenderSliceItem
    #      &other)
    self._noteCreation(BarRenderSliceItem, lambda: Rituals.call(
        'ritual_ZN18BarRenderSliceItemC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def sliceLabelItem(*__, **_) -> Never:
    """
    Qt's 'LabelItem &BarRenderSliceItem::sliceLabelItem()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'BarRenderSliceItem.sliceLabelItem' has no cute function yet. Qt's "
        "'LabelItem &BarRenderSliceItem::sliceLabelItem()': gives a type "
        "Python has no way to take yet.")
