"""
QSGSoftwareRectangleNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGSoftwareRectangleNode to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGRectangleNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from ..QtGui import QColor, QPainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareRectangleNode(QSGRectangleNode):
  """
  The cute side of Qt's QSGSoftwareRectangleNode: a plain Python object
  standing in front of one C++ QSGSoftwareRectangleNode.

  It is built on the cute 'QSGRectangleNode', as Qt's
  QSGSoftwareRectangleNode is built on Qt's QSGRectangleNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareRectangleNode that has a ritual and that
  Python can call so far, 5 names in all: 'setRect', 'rect', 'setColor',
  'color', 'paint'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGSoftwareRectangleNode is created at the first use, not by
    'QSGSoftwareRectangleNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareRectangleNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareRectangleNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QSGSoftwareRectangleNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarerectanglenode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QSGSoftwareRectangleNode::rect() const
    ritual = 'ritual_ZNK24QSGSoftwareRectangleNode4rectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGSoftwareRectangleNode4rectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QSGSoftwareRectangleNode::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerectanglenode.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSGSoftwareRectangleNode::color() const
    ritual = 'ritual_ZNK24QSGSoftwareRectangleNode5colorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QSGSoftwareRectangleNode5colorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGSoftwareRectangleNode::setRect(const QRectF &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerectanglenode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGSoftwareRectangleNode::setRect(const QRectF &rect)
    ritual = 'ritual_ZN24QSGSoftwareRectangleNode7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSGSoftwareRectangleNode7setRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGSoftwareRectangleNode::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerectanglenode.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGSoftwareRectangleNode::setColor(const QColor &color)
    ritual = 'ritual_ZN24QSGSoftwareRectangleNode8setColorERK6QColor'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QSGSoftwareRectangleNode8setColorERK6QColor'
    self.uglySide.call(ritual, self._valueOf(color))

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
    'QSGSoftwareRectangleNode::QSGSoftwareRectangleNode()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerectanglenode.html
    """
    #  QSGSoftwareRectangleNode::QSGSoftwareRectangleNode()
    self._noteCreation(QSGSoftwareRectangleNode, lambda: Rituals.call(
        'ritual_ZN24QSGSoftwareRectangleNodeC1Ev',
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

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRectangleNode::paint(QPainter *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerectanglenode.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRectangleNode::paint(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN24QSGSoftwareRectangleNode5paintEP8QPainter',
        self._addressOf(painter),
    )
