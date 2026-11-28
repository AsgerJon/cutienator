"""
QRemoteObjectPendingCallWatcherHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectpendingcall_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QRemoteObjectPendingCallWatcherHelper to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QRemoteObjectPendingCallWatcherHelper(QObject):
  """
  The cute side of Qt's QRemoteObjectPendingCallWatcherHelper: a plain Python
  object standing in front of one C++ QRemoteObjectPendingCallWatcherHelper.

  It is built on the cute 'QObject', as Qt's
  QRemoteObjectPendingCallWatcherHelper is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectPendingCallWatcherHelper that has a
  ritual and that Python can call so far, 2 names in all: 'metaObject',
  'finished'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectPendingCallWatcherHelper::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QRemoteObjectPendingCallWatcherHelper::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 3 leans on
  'QRemoteObjectPendingCallWatcherHelper; 2 not a gap.

  What to expect
  --------------

  - The C++ QRemoteObjectPendingCallWatcherHelper is created at the first
    use, not by 'QRemoteObjectPendingCallWatcherHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectPendingCallWatcherHelper.
  - Qt tells when it has removed the C++
    QRemoteObjectPendingCallWatcherHelper. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's QRemoteObjectPendingCallWatcherHelper that has no cute
    function yet, 'add', 'emitSignals', holds a function that raises
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
  __qt_class__ = 'QRemoteObjectPendingCallWatcherHelper'

  #  A C++ QRemoteObjectPendingCallWatcherHelper Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectPendingCallWatcherHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QRemoteObjectPendingCallWatcherHelper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcherhelper.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectPendingCallWatcherHelper::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37QRemoteObjectPendingCallWatcherHelper10metaObjectEv',
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

  def finished(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectPendingCallWatcherHelper::finished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcherhelper.html
    """
    #  void QRemoteObjectPendingCallWatcherHelper::finished()
    self.uglySide.call(
        'ritual_ZN37QRemoteObjectPendingCallWatcherHelper8finishedEv',
    )

  @staticmethod
  def add(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectPendingCallWatcherHelper::add(
    QRemoteObjectPendingCallWatcher *watcher)': leans on
    'QRemoteObjectPendingCallWatcherHelper::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectPendingCallWatcherHelper.add' has no cute function "
        "yet. Qt's 'void "
        "QRemoteObjectPendingCallWatcherHelper::add(QRemoteObjectPendingCall"
        "Watcher *watcher)': leans on "
        "'QRemoteObjectPendingCallWatcherHelper::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def emitSignals(*__, **_) -> Never:
    """
    Qt's 'void QRemoteObjectPendingCallWatcherHelper::emitSignals()': leans
    on 'QRemoteObjectPendingCallWatcherHelper::finished()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QRemoteObjectPendingCallWatcherHelper.emitSignals' has no cute "
        "function yet. Qt's 'void "
        "QRemoteObjectPendingCallWatcherHelper::emitSignals()': leans on "
        "'QRemoteObjectPendingCallWatcherHelper::finished()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
