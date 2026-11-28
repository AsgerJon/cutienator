"""
QQuickTableViewResizeHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTableViewResizeHandler to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtGui import QPointingDevice
from . import QQuickTableViewPointerHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickTableViewResizeHandler(QQuickTableViewPointerHandler):
  """
  The cute side of Qt's QQuickTableViewResizeHandler: a plain Python object
  standing in front of one C++ QQuickTableViewResizeHandler.

  It is built on the cute 'QQuickTableViewPointerHandler', as Qt's
  QQuickTableViewResizeHandler is built on Qt's
  QQuickTableViewPointerHandler, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTableViewResizeHandler that has a ritual and
  that Python can call so far, 1 name in all: 'metaObject'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTableViewResizeHandler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickTableViewResizeHandler::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTableViewResizeHandler::updateState(QEventPoint
    &point)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTableViewResizeHandler::updateDrag(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickTableViewResizeHandler::handleEventPoint(QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void
    QQuickTableViewResizeHandler::onGrabChanged(QQuickPointerHandler
    *grabber, QPointingDevice::GrabTransition transition, QPointerEvent *ev,
    QEventPoint &point)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickTableViewResizeHandler.

  What to expect
  --------------

  - The C++ QQuickTableViewResizeHandler is created at the first use, not by
    'QQuickTableViewResizeHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTableViewResizeHandler.
  - Qt tells when it has removed the C++ QQuickTableViewResizeHandler. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTableViewResizeHandler that has no cute function
    yet, '__init__', 'updateDrag', 'updateState', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTableViewResizeHandler'

  #  A C++ QQuickTableViewResizeHandler Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTableViewResizeHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTableViewResizeHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktableviewresizehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTableViewResizeHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickTableViewResizeHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickTableViewResizeHandler::QQuickTableViewResizeHandler(
    QQuickTableView *view)': leans on
    'QQuickTableViewResizeHandler::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTableViewResizeHandler.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickTableViewResizeHandler::QQuickTableViewResizeHandler(QQuickT"
        "ableView *view)': leans on "
        "'QQuickTableViewResizeHandler::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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
  def updateDrag(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewResizeHandler::updateDrag(QPointerEvent *event,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewResizeHandler.updateDrag' has no cute function "
        "yet. Qt's 'void "
        "QQuickTableViewResizeHandler::updateDrag(QPointerEvent *event, "
        "QEventPoint &point)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def updateState(*__, **_) -> Never:
    """
    Qt's 'void QQuickTableViewResizeHandler::updateState(QEventPoint
    &point)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTableViewResizeHandler.updateState' has no cute function "
        "yet. Qt's 'void "
        "QQuickTableViewResizeHandler::updateState(QEventPoint &point)': "
        "takes a type Python has no way to hand over yet.")
