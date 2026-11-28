"""
QSGRectangleNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgrectanglenode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
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


class QSGRectangleNode(QSGGeometryNode):
  """
  The cute side of Qt's QSGRectangleNode: a plain Python object standing in
  front of one C++ QSGRectangleNode.

  It is built on the cute 'QSGGeometryNode', as Qt's QSGRectangleNode is
  built on Qt's QSGGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRectangleNode that has a ritual and that Python
  can call so far, 4 names in all: 'setRect', 'rect', 'setColor', 'color'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGRectangleNode::~QSGRectangleNode()': the destructor: Python
    never removes a C++ QSGRectangleNode.

  What to expect
  --------------

  - The C++ QSGRectangleNode is created at the first use, not by
    'QSGRectangleNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRectangleNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGRectangleNode'

  #  A C++ QSGRectangleNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRectangleNode'

  #  The functions Qt calls itself that QSGRectangleNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setRect': (
          ('_ZN16QSGRectangleNode7setRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'rect': (
          ('_ZNK16QSGRectangleNode4rectEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
      'setColor': (
          ('_ZN16QSGRectangleNode8setColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'color': (
          ('_ZNK16QSGRectangleNode5colorEv',
           ('address', 'value', 'QtGui:QColor'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGRectangleNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrectanglenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGRectangleNode::rect() const
    address = self.uglySide.call('ritual_ZNK16QSGRectangleNode4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QSGRectangleNode::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrectanglenode.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGRectangleNode::color() const
    address = self.uglySide.call('ritual_ZNK16QSGRectangleNode5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGRectangleNode::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrectanglenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGRectangleNode::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN16QSGRectangleNode7setRectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QSGRectangleNode::setRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrectanglenode.html#setRect

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
    #  void QSGRectangleNode::setRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN16QSGRectangleNode7setRectEdddd', x, y, w, h,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGRectangleNode::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgrectanglenode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGRectangleNode::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QSGRectangleNode8setColorERK6QColor',
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
