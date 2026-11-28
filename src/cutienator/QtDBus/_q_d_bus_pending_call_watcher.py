"""
QDBusPendingCallWatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbuspendingcall.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QDBusPendingCall

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusPendingCallWatcher(QObject, QDBusPendingCall):
  """
  The cute side of Qt's QDBusPendingCallWatcher: a plain Python object
  standing in front of one C++ QDBusPendingCallWatcher.

  It is built on the cute 'QObject', as Qt's QDBusPendingCallWatcher is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QDBusPendingCall' as well, as Qt's QDBusPendingCallWatcher is built on
  Qt's QDBusPendingCall too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusPendingCallWatcher that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr',
  'waitForFinished', 'finished'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusPendingCallWatcher::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusPendingCallWatcher::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusPendingCallWatcher::~QDBusPendingCallWatcher()': the
    destructor: Python never removes a C++ QDBusPendingCallWatcher.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDBusPendingCallWatcher is created at the first use, not by
    'QDBusPendingCallWatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusPendingCallWatcher.
  - Qt tells when it has removed the C++ QDBusPendingCallWatcher. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDBusPendingCallWatcher::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcallwatcher.html#tr

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
    #  QString QDBusPendingCallWatcher::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QDBusPendingCallWatcher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusPendingCallWatcher'

  #  Qt's QDBusPendingCallWatcher is built on more than one class. The part
  #  of a C++ QDBusPendingCallWatcher that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QDBusPendingCall':
          'ritual_cast_QDBusPendingCallWatcher_QDBusPendingCall',
  }

  #  A C++ QDBusPendingCallWatcher Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusPendingCallWatcher'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusPendingCallWatcher::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallwatcher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusPendingCallWatcher::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QDBusPendingCallWatcher10metaObjectEv',
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

  @overload(QDBusPendingCall)
  @overload(QDBusPendingCall, QObject)
  @overload(QDBusPendingCall, NoneType)
  def __init__(
      self,
      call: QDBusPendingCall,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDBusPendingCallWatcher::QDBusPendingCallWatcher(const QDBusPendingCall
    &call, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallwatcher.html

    Parameters
    ----------

    call : QDBusPendingCall
      Passed on as a value: Qt reads the C++ QDBusPendingCall, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusPendingCallWatcher::QDBusPendingCallWatcher(const
    #      QDBusPendingCall &call, QObject *parent)
    self._noteCreation(QDBusPendingCallWatcher, lambda: Rituals.call(
        'ritual_ZN23QDBusPendingCallWatcherC1ERK16QDBusPendingCallP7QObject',
        self._valueOf(call, 'QDBusPendingCall'), self._addressOf(parent,
        'QObject'),
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
    Calls Qt's 'void QDBusPendingCallWatcher::waitForFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallwatcher.html#waitForFinished
    """
    #  void QDBusPendingCallWatcher::waitForFinished()
    self.uglySide.call(
        'ritual_ZN23QDBusPendingCallWatcher15waitForFinishedEv',
    )

  @overload()
  @overload(THIS)
  @overload(NoneType)
  def finished(
      self,
      self_: Optional[QDBusPendingCallWatcher] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QDBusPendingCallWatcher::finished(QDBusPendingCallWatcher *self_)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcallwatcher.html#finished

    Parameters
    ----------

    self_ : Optional[QDBusPendingCallWatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QDBusPendingCallWatcher::finished(QDBusPendingCallWatcher *self_)
    self.uglySide.call(
        'ritual_ZN23QDBusPendingCallWatcher8finishedEPS_',
        self._addressOf(self_),
    )
