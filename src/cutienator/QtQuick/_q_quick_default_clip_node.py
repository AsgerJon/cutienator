"""
QQuickDefaultClipNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickclipnode_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDefaultClipNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGClipNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QQuickDefaultClipNode(QSGClipNode):
  """
  The cute side of Qt's QQuickDefaultClipNode: a plain Python object standing
  in front of one C++ QQuickDefaultClipNode.

  It is built on the cute 'QSGClipNode', as Qt's QQuickDefaultClipNode is
  built on Qt's QSGClipNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDefaultClipNode that has a ritual and that
  Python can call so far, 6 names in all: 'setRect', 'rect', 'setRadius',
  'radius', 'update', 'updateGeometry'. It can be made from Python, in 1 way;
  see '__init__'.

  What to expect
  --------------

  - The C++ QQuickDefaultClipNode is created at the first use, not by
    'QQuickDefaultClipNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDefaultClipNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDefaultClipNode'

  #  The functions Qt calls itself that QQuickDefaultClipNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'update': (
          ('_ZN21QQuickDefaultClipNode6updateEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'QRectF QQuickDefaultClipNode::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdefaultclipnode.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickDefaultClipNode::rect() const
    address = self.uglySide.call('ritual_ZNK21QQuickDefaultClipNode4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QQuickDefaultClipNode::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdefaultclipnode.html#radius
    """
    #  qreal QQuickDefaultClipNode::radius() const
    return self.uglySide.call('ritual_ZNK21QQuickDefaultClipNode6radiusEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, a0: QRectF) -> None:
    """
    Calls Qt's 'void QQuickDefaultClipNode::setRect(const QRectF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdefaultclipnode.html#setRect

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickDefaultClipNode::setRect(const QRectF &a0)
    self.uglySide.call(
        'ritual_ZN21QQuickDefaultClipNode7setRectERK6QRectF',
        self._valueOf(a0),
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickDefaultClipNode::setRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaultclipnode.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickDefaultClipNode::setRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN21QQuickDefaultClipNode9setRadiusEd', radius,
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

  @overload(QRectF)
  def __init__(self, a0: QRectF) -> None:
    """
    Notes what was given, for Qt's
    'QQuickDefaultClipNode::QQuickDefaultClipNode(const QRectF &a0)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaultclipnode.html#QQuickDefaultClipNode

    Parameters
    ----------

    a0 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QQuickDefaultClipNode::QQuickDefaultClipNode(const QRectF &a0)
    self._noteCreation(QQuickDefaultClipNode, lambda: Rituals.call(
        'ritual_ZN21QQuickDefaultClipNodeC1ERK6QRectF', self._valueOf(a0),
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

  def update(self) -> None:
    """
    Calls Qt's 'void QQuickDefaultClipNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdefaultclipnode.html#update
    """
    #  void QQuickDefaultClipNode::update()
    ritual = 'ritual_ZN21QQuickDefaultClipNode6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickDefaultClipNode6updateEv'
    self.uglySide.call(ritual)

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QQuickDefaultClipNode::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdefaultclipnode.html#updateGeometry
    """
    #  void QQuickDefaultClipNode::updateGeometry()
    self.uglySide.call('ritual_ZN21QQuickDefaultClipNode14updateGeometryEv')
