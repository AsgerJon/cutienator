"""
ScatterRenderItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/scatterrenderitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ScatterRenderItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import AbstractRenderItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class ScatterRenderItem(AbstractRenderItem):
  """
  The cute side of Qt's ScatterRenderItem: a plain Python object standing in
  front of one C++ ScatterRenderItem.

  It is built on the cute 'AbstractRenderItem', as Qt's ScatterRenderItem is
  built on Qt's AbstractRenderItem, and has everything that class has.

  C++ hands a ScatterRenderItem around as a copy, so every C++
  ScatterRenderItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ScatterRenderItem that has a ritual and that Python
  can call so far, 4 names in all: 'position', 'setPosition', 'isVisible',
  'setVisible'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ScatterRenderItem &ScatterRenderItem::operator=(const
    ScatterRenderItem &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'ScatterRenderItem::~ScatterRenderItem()': the destructor: Python
    removes its C++ ScatterRenderItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ ScatterRenderItem is created at the first use, not by
    'ScatterRenderItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ScatterRenderItem back gives a copy the ritual made
    for Python, in a new cute ScatterRenderItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterRenderItem'

  #  Qt's '~ScatterRenderItem()'. Naming it makes this a value class: Python
  #  owns every C++ ScatterRenderItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17ScatterRenderItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def position(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &ScatterRenderItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterrenderitem.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &ScatterRenderItem::position() const
    address = self.uglySide.call('ritual_ZNK17ScatterRenderItem8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool ScatterRenderItem::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/scatterrenderitem.html#isVisible
    """
    #  bool ScatterRenderItem::isVisible() const
    return self.uglySide.call('ritual_ZNK17ScatterRenderItem9isVisibleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setPosition(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void ScatterRenderItem::setPosition(const QVector3D &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterrenderitem.html#setPosition

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void ScatterRenderItem::setPosition(const QVector3D &pos)
    self.uglySide.call(
        'ritual_ZN17ScatterRenderItem11setPositionERK9QVector3D',
        self._valueOf(pos),
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void ScatterRenderItem::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/scatterrenderitem.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void ScatterRenderItem::setVisible(bool visible)
    self.uglySide.call('ritual_ZN17ScatterRenderItem10setVisibleEb', visible)

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
    Notes what was given, for Qt's 'ScatterRenderItem::ScatterRenderItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterrenderitem.html#ScatterRenderItem
    """
    #  ScatterRenderItem::ScatterRenderItem()
    self._noteCreation(ScatterRenderItem, lambda: Rituals.call(
        'ritual_ZN17ScatterRenderItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: ScatterRenderItem) -> None:
    """
    Notes what was given, for Qt's
    'ScatterRenderItem::ScatterRenderItem(const ScatterRenderItem &other)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/scatterrenderitem.html#ScatterRenderItem

    Parameters
    ----------

    other : ScatterRenderItem
      Passed on as a value: Qt reads the C++ ScatterRenderItem, which stays
      Python's own.
    """
    #  ScatterRenderItem::ScatterRenderItem(const ScatterRenderItem &other)
    self._noteCreation(ScatterRenderItem, lambda: Rituals.call(
        'ritual_ZN17ScatterRenderItemC1ERKS_', self._valueOf(other),
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
