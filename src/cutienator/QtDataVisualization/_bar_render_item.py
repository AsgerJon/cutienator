"""
BarRenderItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/barrenderitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means BarRenderItem to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import AbstractRenderItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']


class BarRenderItem(AbstractRenderItem):
  """
  The cute side of Qt's BarRenderItem: a plain Python object standing in
  front of one C++ BarRenderItem.

  It is built on the cute 'AbstractRenderItem', as Qt's BarRenderItem is
  built on Qt's AbstractRenderItem, and has everything that class has.

  C++ hands a BarRenderItem around as a copy, so every C++ BarRenderItem
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's BarRenderItem that has a ritual and that Python can
  call so far, 6 names in all: 'setPosition', 'position', 'setValue',
  'value', 'setHeight', 'height'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'BarRenderItem &BarRenderItem::operator=(const BarRenderItem &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'BarRenderItem::~BarRenderItem()': the destructor: Python removes
    its C++ BarRenderItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ BarRenderItem is created at the first use, not by
    'BarRenderItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a BarRenderItem back gives a copy the ritual made for
    Python, in a new cute BarRenderItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BarRenderItem'

  #  Qt's '~BarRenderItem()'. Naming it makes this a value class: Python owns
  #  every C++ BarRenderItem behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13BarRenderItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> QPoint:
    """
    Calls Qt's 'const QPoint &BarRenderItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#position

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint &BarRenderItem::position() const
    address = self.uglySide.call('ritual_ZNK13BarRenderItem8positionEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def value(self) -> float:
    """
    Calls Qt's 'float BarRenderItem::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#value
    """
    #  float BarRenderItem::value() const
    return self.uglySide.call('ritual_ZNK13BarRenderItem5valueEv')

  def height(self) -> float:
    """
    Calls Qt's 'GLfloat BarRenderItem::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#height
    """
    #  GLfloat BarRenderItem::height() const
    return self.uglySide.call('ritual_ZNK13BarRenderItem6heightEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def setPosition(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void BarRenderItem::setPosition(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#setPosition

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void BarRenderItem::setPosition(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN13BarRenderItem11setPositionERK6QPoint',
        self._valueOf(pos),
    )

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void BarRenderItem::setValue(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void BarRenderItem::setValue(float value)
    self.uglySide.call('ritual_ZN13BarRenderItem8setValueEf', value)

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void BarRenderItem::setHeight(GLfloat height)'.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void BarRenderItem::setHeight(GLfloat height)
    self.uglySide.call('ritual_ZN13BarRenderItem9setHeightEf', height)

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
    Notes what was given, for Qt's 'BarRenderItem::BarRenderItem()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#BarRenderItem
    """
    #  BarRenderItem::BarRenderItem()
    self._noteCreation(BarRenderItem, lambda: Rituals.call(
        'ritual_ZN13BarRenderItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: BarRenderItem) -> None:
    """
    Notes what was given, for Qt's 'BarRenderItem::BarRenderItem(const
    BarRenderItem &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/barrenderitem.html#BarRenderItem

    Parameters
    ----------

    other : BarRenderItem
      Passed on as a value: Qt reads the C++ BarRenderItem, which stays
      Python's own.
    """
    #  BarRenderItem::BarRenderItem(const BarRenderItem &other)
    self._noteCreation(BarRenderItem, lambda: Rituals.call(
        'ritual_ZN13BarRenderItemC1ERKS_', self._valueOf(other),
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
