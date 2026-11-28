"""
QQuickGrabGestureEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickGrabGestureEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickGrabGestureEvent(QObject):
  """
  The cute side of Qt's QQuickGrabGestureEvent: a plain Python object
  standing in front of one C++ QQuickGrabGestureEvent.

  It is built on the cute 'QObject', as Qt's QQuickGrabGestureEvent is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGrabGestureEvent that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'grab', 'wantsGrab',
  'dragThreshold'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGrabGestureEvent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGrabGestureEvent::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickGrabGestureEvent::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QQmlListProperty<QObject> QQuickGrabGestureEvent::touchPoints()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickGrabGestureEvent; 1 leans on 'vtable for QQuickGrabGestureEvent',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QQuickGrabGestureEvent is created at the first use, not by
    'QQuickGrabGestureEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGrabGestureEvent.
  - Qt tells when it has removed the C++ QQuickGrabGestureEvent. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGrabGestureEvent that has no cute function yet,
    '__init__', 'touchPoints', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGrabGestureEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGrabGestureEvent::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrabgestureevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGrabGestureEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickGrabGestureEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def wantsGrab(self) -> bool:
    """
    Calls Qt's 'bool QQuickGrabGestureEvent::wantsGrab() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrabgestureevent.html#wantsGrab
    """
    #  bool QQuickGrabGestureEvent::wantsGrab() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickGrabGestureEvent9wantsGrabEv',
    )

  def dragThreshold(self) -> float:
    """
    Calls Qt's 'qreal QQuickGrabGestureEvent::dragThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgrabgestureevent.html#dragThreshold
    """
    #  qreal QQuickGrabGestureEvent::dragThreshold() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickGrabGestureEvent13dragThresholdEv',
    )

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
    Qt's 'QQuickGrabGestureEvent::QQuickGrabGestureEvent()': leans on 'vtable
    for QQuickGrabGestureEvent', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGrabGestureEvent.__init__' has no cute function yet. Qt's "
        "'QQuickGrabGestureEvent::QQuickGrabGestureEvent()': leans on "
        "'vtable for QQuickGrabGestureEvent', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def grab(self) -> None:
    """
    Calls Qt's 'void QQuickGrabGestureEvent::grab()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgrabgestureevent.html#grab
    """
    #  void QQuickGrabGestureEvent::grab()
    self.uglySide.call('ritual_ZN22QQuickGrabGestureEvent4grabEv')

  @staticmethod
  def touchPoints(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickGrabGestureEvent::touchPoints()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickGrabGestureEvent.touchPoints' has no cute function yet. "
        "Qt's 'QQmlListProperty<QObject> "
        "QQuickGrabGestureEvent::touchPoints()': gives a type Python has no "
        "way to take yet.")
