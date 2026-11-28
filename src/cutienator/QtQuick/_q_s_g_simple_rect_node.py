"""
QSGSimpleRectNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgsimplerectnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']


class QSGSimpleRectNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGSimpleRectNode: a plain Python object standing in
  front of one C++ QSGSimpleRectNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGSimpleRectNode is
  built on Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSimpleRectNode that has a ritual and that Python
  can call so far, 4 names in all: 'setRect', 'rect', 'setColor', 'color'. It
  can be made from Python, in 2 ways; see '__init__'.

  What to expect
  --------------

  - The C++ QSGSimpleRectNode is created at the first use, not by
    'QSGSimpleRectNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSimpleRectNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSimpleRectNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSimpleRectNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimplerectnode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSimpleRectNode::rect() const
    address = self.uglySide.call('ritual_ZNK17QSGSimpleRectNode4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QSGSimpleRectNode::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimplerectnode.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGSimpleRectNode::color() const
    address = self.uglySide.call('ritual_ZNK17QSGSimpleRectNode5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSimpleRectNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimplerectnode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSimpleRectNode::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN17QSGSimpleRectNode7setRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QSGSimpleRectNode::setRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimplerectnode.html#setRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QSGSimpleRectNode::setRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN17QSGSimpleRectNode7setRectEdddd', x, y, w, h,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGSimpleRectNode::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsimplerectnode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSimpleRectNode::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QSGSimpleRectNode8setColorERK6QColor',
        self._valueOf(color),
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

  @overload(QRectF, QColor)
  def __init__(self, rect: QRectF, color: QColor) -> None:
    """
    Notes what was given, for Qt's
    'QSGSimpleRectNode::QSGSimpleRectNode(const QRectF &rect, const QColor
    &color)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimplerectnode.html#QSGSimpleRectNode

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QSGSimpleRectNode::QSGSimpleRectNode(const QRectF &rect, const QColor
    #      &color)
    self._noteCreation(QSGSimpleRectNode, lambda: Rituals.call(
        'ritual_ZN17QSGSimpleRectNodeC1ERK6QRectFRK6QColor',
        self._valueOf(rect), self._valueOf(color),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSGSimpleRectNode::QSGSimpleRectNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsimplerectnode.html#QSGSimpleRectNode
    """
    #  QSGSimpleRectNode::QSGSimpleRectNode()
    self._noteCreation(QSGSimpleRectNode, lambda: Rituals.call(
        'ritual_ZN17QSGSimpleRectNodeC1Ev',
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
