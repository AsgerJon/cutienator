"""
QRemoteObjectPendingCallWatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qremoteobjectpendingcall.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QRemoteObjectPendingCall

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRemoteObjectPendingCallWatcher(QObject, QRemoteObjectPendingCall):
  """
  The cute side of Qt's QRemoteObjectPendingCallWatcher: a plain Python
  object standing in front of one C++ QRemoteObjectPendingCallWatcher.

  It is built on the cute 'QObject', as Qt's QRemoteObjectPendingCallWatcher
  is built on Qt's QObject, and has everything that class has. It is built on
  the cute 'QRemoteObjectPendingCall' as well, as Qt's
  QRemoteObjectPendingCallWatcher is built on Qt's QRemoteObjectPendingCall
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRemoteObjectPendingCallWatcher that has a ritual
  and that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'isFinished', 'waitForFinished', 'finished'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QRemoteObjectPendingCallWatcher::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QRemoteObjectPendingCallWatcher::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QRemoteObjectPendingCallWatcher::~QRemoteObjectPendingCallWatcher()':
    the destructor: Python never removes a C++
    QRemoteObjectPendingCallWatcher.
  - Qt's 'QRemoteObjectPendingCallWatcherPrivate
    *QRemoteObjectPendingCallWatcher::d_func()': gives
    'QRemoteObjectPendingCallWatcherPrivate', which has no cute class yet.
  - Qt's 'const QRemoteObjectPendingCallWatcherPrivate
    *QRemoteObjectPendingCallWatcher::d_func() const': gives
    'QRemoteObjectPendingCallWatcherPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QRemoteObjectPendingCallWatcher is created at the first use, not
    by 'QRemoteObjectPendingCallWatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRemoteObjectPendingCallWatcher.
  - Qt tells when it has removed the C++ QRemoteObjectPendingCallWatcher.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QRemoteObjectPendingCallWatcher::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcher.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QRemoteObjectPendingCallWatcher::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN31QRemoteObjectPendingCallWatcher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRemoteObjectPendingCallWatcher'

  #  Qt's QRemoteObjectPendingCallWatcher is built on more than one class.
  #  The part of a C++ QRemoteObjectPendingCallWatcher that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QRemoteObjectPendingCall':
          'ritual_cast_QRemoteObjectPendingCallWatcher_QRemoteObjectPendingCall',
  }

  #  A C++ QRemoteObjectPendingCallWatcher Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRemoteObjectPendingCallWatcher'

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
    *QRemoteObjectPendingCallWatcher::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QRemoteObjectPendingCallWatcher::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QRemoteObjectPendingCallWatcher10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QRemoteObjectPendingCallWatcher::isFinished() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcher.html#isFinished
    """
    #  bool QRemoteObjectPendingCallWatcher::isFinished() const
    return self.uglySide.call(
        'ritual_ZNK31QRemoteObjectPendingCallWatcher10isFinishedEv',
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

  @overload(QRemoteObjectPendingCall)
  @overload(QRemoteObjectPendingCall, QObject)
  @overload(QRemoteObjectPendingCall, NoneType)
  def __init__(
      self,
      call: QRemoteObjectPendingCall,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRemoteObjectPendingCallWatcher::QRemoteObjectPendingCallWatcher(const
    QRemoteObjectPendingCall &call, QObject *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcher.html

    Parameters
    ----------

    call : QRemoteObjectPendingCall
      Passed on as a value: Qt reads the C++ QRemoteObjectPendingCall, which
      stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QRemoteObjectPendingCallWatcher::QRemoteObjectPendingCallWatcher(const
    #      QRemoteObjectPendingCall &call, QObject *parent)
    self._noteCreation(QRemoteObjectPendingCallWatcher, lambda: Rituals.call(
        'ritual_ZN31QRemoteObjectPendingCallWatcherC1ERK24QRemoteObjectPend'
        'ingCallP7QObject',
        self._valueOf(call, 'QRemoteObjectPendingCall'),
        self._addressOf(parent, 'QObject'),
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

  def waitForFinished(self) -> None:
    """
    Calls Qt's 'void QRemoteObjectPendingCallWatcher::waitForFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcher.html
    """
    #  void QRemoteObjectPendingCallWatcher::waitForFinished()
    self.uglySide.call(
        'ritual_ZN31QRemoteObjectPendingCallWatcher15waitForFinishedEv',
    )

  @overload(THIS)
  @overload(NoneType)
  def finished(
      self,
      self_: Optional[QRemoteObjectPendingCallWatcher],
  ) -> None:
    """
    Calls Qt's 'void
    QRemoteObjectPendingCallWatcher::finished(QRemoteObjectPendingCallWatcher
    *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qremoteobjectpendingcallwatcher.html#finished

    Parameters
    ----------

    self_ : Optional[QRemoteObjectPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRemoteObjectPendingCallWatcher::finished(
    #      QRemoteObjectPendingCallWatcher *self_)
    self.uglySide.call(
        'ritual_ZN31QRemoteObjectPendingCallWatcher8finishedEPS_',
        self._addressOf(self_),
    )
