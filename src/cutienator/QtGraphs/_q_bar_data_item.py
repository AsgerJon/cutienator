"""
QBarDataItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qbardataitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QBarDataItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBarDataItem: a plain Python object standing in front
  of one C++ QBarDataItem.

  C++ hands a QBarDataItem around as a copy, so every C++ QBarDataItem behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBarDataItem that has a ritual and that Python can
  call so far, 4 names in all: 'setValue', 'value', 'setRotation',
  'rotation'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBarDataItem::~QBarDataItem()': the destructor: Python removes its
    C++ QBarDataItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QBarDataItem is created at the first use, not by
    'QBarDataItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBarDataItem back gives a copy the ritual made for
    Python, in a new cute QBarDataItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBarDataItem'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  Qt's '~QBarDataItem()'. Naming it makes this a value class: Python owns
  #  every C++ QBarDataItem behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QBarDataItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> float:
    """
    Calls Qt's 'float QBarDataItem::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#value
    """
    #  float QBarDataItem::value() const
    return self.uglySide.call('ritual_ZNK12QBarDataItem5valueEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'float QBarDataItem::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#rotation
    """
    #  float QBarDataItem::rotation() const
    return self.uglySide.call('ritual_ZNK12QBarDataItem8rotationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setValue(self, val: float) -> None:
    """
    Calls Qt's 'void QBarDataItem::setValue(float val)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#setValue

    Parameters
    ----------

    val : float
      Passed on as it is.
    """
    #  void QBarDataItem::setValue(float val)
    self.uglySide.call('ritual_ZN12QBarDataItem8setValueEf', val)

  @overload(float)
  def setRotation(self, angle: float) -> None:
    """
    Calls Qt's 'void QBarDataItem::setRotation(float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#setRotation

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QBarDataItem::setRotation(float angle)
    self.uglySide.call('ritual_ZN12QBarDataItem11setRotationEf', angle)

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
    Notes what was given, for Qt's 'QBarDataItem::QBarDataItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#QBarDataItem
    """
    #  QBarDataItem::QBarDataItem()
    self._noteCreation(QBarDataItem, lambda: Rituals.call(
        'ritual_ZN12QBarDataItemC1Ev',
    ))

  @overload(float)
  def __init__(self, value: float) -> None:
    """
    Notes what was given, for Qt's 'QBarDataItem::QBarDataItem(float value)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#QBarDataItem

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  QBarDataItem::QBarDataItem(float value)
    self._noteCreation(QBarDataItem, lambda: Rituals.call(
        'ritual_ZN12QBarDataItemC1Ef', value,
    ))

  @overload(float, float)
  def __init__(self, value: float, angle: float) -> None:
    """
    Notes what was given, for Qt's 'QBarDataItem::QBarDataItem(float value,
    float angle)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbardataitem.html#QBarDataItem

    Parameters
    ----------

    value : float
      Passed on as it is.

    angle : float
      Passed on as it is.
    """
    #  QBarDataItem::QBarDataItem(float value, float angle)
    self._noteCreation(QBarDataItem, lambda: Rituals.call(
        'ritual_ZN12QBarDataItemC1Eff', value, angle,
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


#  Qt's 'QList<QBarDataItem>': the list of QBarDataItem, which
#  'QList[QBarDataItem]' gives. It is made here, so that there is one as soon
#  as there can be a QBarDataItem. Qt has a name of its own for it.
QBarDataRow = QList.createKind(
    QBarDataItem, 'value',
    name='QBarDataRow',
    make='ritual_list_make_QBarDataItem',
    add='ritual_list_add_QBarDataItem',
    size='ritual_list_size_QBarDataItem',
    at='ritual_list_at_QBarDataItem',
    drop='ritual_list_drop_QBarDataItem',
)
