"""
QQuickSelectionRectanglePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSelectionRectanglePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickControlPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QPointF
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem
  from . import QQuickSelectionRectangle, QQuickSelectionRectangleAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSelectionRectanglePrivate(QQuickControlPrivate):
  """
  The cute side of Qt's QQuickSelectionRectanglePrivate: a plain Python
  object standing in front of one C++ QQuickSelectionRectanglePrivate.

  It is built on the cute 'QQuickControlPrivate', as Qt's
  QQuickSelectionRectanglePrivate is built on Qt's QQuickControlPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSelectionRectanglePrivate that has a ritual
  and that Python can call so far, 10 names in all: 'q_func',
  'updateDraggingState', 'updateActiveState', 'updateHandles',
  'updateSelectionMode', 'connectToTarget', 'scrollTowardsPos',
  'handleUnderPos', 'createHandle', 'getAttachedObject'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickSelectionRectangle
    *QQuickSelectionRectanglePrivate::q_func() const': takes in Python what
    'QQuickSelectionRectangle *QQuickSelectionRectanglePrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickSelectionRectanglePrivate is created at the first use, not
    by 'QQuickSelectionRectanglePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSelectionRectanglePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSelectionRectanglePrivate'

  #  A C++ QQuickSelectionRectanglePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSelectionRectanglePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def getAttachedObject(
      self,
      object: Optional[QObject],
  ) -> Optional[QQuickSelectionRectangleAttached]:
    """
    Calls Qt's 'QQuickSelectionRectangleAttached
    *QQuickSelectionRectanglePrivate::getAttachedObject(const QObject
    *object) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSelectionRectangleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSelectionRectangleAttached
    #      *QQuickSelectionRectanglePrivate::getAttachedObject(const QObject
    #      *object) const
    address = self.uglySide.call(
        'ritual_ZNK31QQuickSelectionRectanglePrivate17getAttachedObjectEPK7'
        'QObject',
        self._addressOf(object, 'QObject'),
    )
    from . import QQuickSelectionRectangleAttached
    return QQuickSelectionRectangleAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickSelectionRectanglePrivate::QQuickSelectionRectanglePrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html
    """
    #  QQuickSelectionRectanglePrivate::QQuickSelectionRectanglePrivate()
    self._noteCreation(QQuickSelectionRectanglePrivate, lambda: Rituals.call(
        'ritual_ZN31QQuickSelectionRectanglePrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickSelectionRectangle]:
    """
    Calls Qt's 'QQuickSelectionRectangle
    *QQuickSelectionRectanglePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html#q_func

    Returns
    -------

    Optional[QQuickSelectionRectangle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSelectionRectangle *QQuickSelectionRectanglePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate6q_funcEv',
    )
    from . import QQuickSelectionRectangle
    return QQuickSelectionRectangle._cuteAt(address)

  @overload(bool)
  def updateDraggingState(self, isDragging: bool) -> None:
    """
    Calls Qt's 'void
    QQuickSelectionRectanglePrivate::updateDraggingState(bool isDragging)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html

    Parameters
    ----------

    isDragging : bool
      Passed on as it is.
    """
    #  void QQuickSelectionRectanglePrivate::updateDraggingState(bool
    #      isDragging)
    self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate19updateDraggingStateEb',
        isDragging,
    )

  @overload(bool)
  def updateActiveState(self, isActive: bool) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectanglePrivate::updateActiveState(bool
    isActive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html

    Parameters
    ----------

    isActive : bool
      Passed on as it is.
    """
    #  void QQuickSelectionRectanglePrivate::updateActiveState(bool isActive)
    self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate17updateActiveStateEb',
        isActive,
    )

  def updateHandles(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectanglePrivate::updateHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html#updateHandles
    """
    #  void QQuickSelectionRectanglePrivate::updateHandles()
    self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate13updateHandlesEv',
    )

  def updateSelectionMode(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectanglePrivate::updateSelectionMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html
    """
    #  void QQuickSelectionRectanglePrivate::updateSelectionMode()
    self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate19updateSelectionModeEv',
    )

  def connectToTarget(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectanglePrivate::connectToTarget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html
    """
    #  void QQuickSelectionRectanglePrivate::connectToTarget()
    self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate15connectToTargetEv',
    )

  @overload(QPointF)
  def scrollTowardsPos(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectanglePrivate::scrollTowardsPos(const
    QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickSelectionRectanglePrivate::scrollTowardsPos(const QPointF
    #      &pos)
    self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate16scrollTowardsPosERK7QP'
        'ointF',
        self._valueOf(pos, 'QPointF'),
    )

  @overload(QPointF)
  def handleUnderPos(self, pos: QPointF) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickSelectionRectanglePrivate::handleUnderPos(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSelectionRectanglePrivate::handleUnderPos(const
    #      QPointF &pos)
    address = self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate14handleUnderPosERK7QPoi'
        'ntF',
        self._valueOf(pos, 'QPointF'),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQmlComponent, Qt.Corner)
  @overload(NoneType, Qt.Corner)
  def createHandle(
      self,
      delegate: Optional[QQmlComponent],
      corner: Qt.Corner,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickSelectionRectanglePrivate::createHandle(QQmlComponent *delegate,
    Qt::Corner corner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangleprivate.html#createHandle

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    corner : Qt.Corner
      Passed on as its number.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem
    #      *QQuickSelectionRectanglePrivate::createHandle(QQmlComponent
    #      *delegate, Qt::Corner corner)
    address = self.uglySide.call(
        'ritual_ZN31QQuickSelectionRectanglePrivate12createHandleEP13QQmlCo'
        'mponentN2Qt6CornerE',
        self._addressOf(delegate), corner.value,
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)
