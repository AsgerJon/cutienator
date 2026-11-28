"""
QWinOverlappedIoNotifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialPort/6.12.0/QtSerialPort/private/qwinoverlappedionotifier_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QWinOverlappedIoNotifier to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWinOverlappedIoNotifier(QObject):
  """
  The cute side of Qt's QWinOverlappedIoNotifier: a plain Python object
  standing in front of one C++ QWinOverlappedIoNotifier.

  It is built on the cute 'QObject', as Qt's QWinOverlappedIoNotifier is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWinOverlappedIoNotifier that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'setEnabled',
  '_q_notify'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWinOverlappedIoNotifier::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWinOverlappedIoNotifier::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWinOverlappedIoNotifierPrivate
    *QWinOverlappedIoNotifier::d_func()': gives
    'QWinOverlappedIoNotifierPrivate', which has no cute class yet.
  - Qt's 'const QWinOverlappedIoNotifierPrivate
    *QWinOverlappedIoNotifier::d_func() const': gives
    'QWinOverlappedIoNotifierPrivate', which has no cute class yet.
  - Qt's 'QWinOverlappedIoNotifier::~QWinOverlappedIoNotifier()': the
    destructor: Python never removes a C++ QWinOverlappedIoNotifier.
  - Qt's 'void QWinOverlappedIoNotifier::setHandle(Qt::HANDLE h)': names
    'void', which has no cute class yet.
  - Qt's 'Qt::HANDLE QWinOverlappedIoNotifier::handle() const': gives 'void',
    which has no cute class yet.
  - Qt's 'OVERLAPPED
    *QWinOverlappedIoNotifier::waitForAnyNotified(QDeadlineTimer deadline)':
    gives 'struct _OVERLAPPED', which has no cute class yet.
  - Qt's 'bool QWinOverlappedIoNotifier::waitForNotified(QDeadlineTimer
    deadline, OVERLAPPED *overlapped)': names 'OVERLAPPED', which has no cute
    class yet.
  - Qt's 'void QWinOverlappedIoNotifier::notified(quint32 numberOfBytes,
    quint32 errorCode, OVERLAPPED *overlapped)': names 'OVERLAPPED', which
    has no cute class yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWinOverlappedIoNotifier is created at the first use, not by
    'QWinOverlappedIoNotifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWinOverlappedIoNotifier.
  - Qt tells when it has removed the C++ QWinOverlappedIoNotifier. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWinOverlappedIoNotifier that has no cute function yet,
    'handle', 'notified', 'setHandle', 'waitForAnyNotified',
    'waitForNotified', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QWinOverlappedIoNotifier::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwinoverlappedionotifier.html#tr

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
    #  QString QWinOverlappedIoNotifier::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QWinOverlappedIoNotifier2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWinOverlappedIoNotifier'

  #  A C++ QWinOverlappedIoNotifier Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWinOverlappedIoNotifier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWinOverlappedIoNotifier::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwinoverlappedionotifier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWinOverlappedIoNotifier::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QWinOverlappedIoNotifier10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QWinOverlappedIoNotifier::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwinoverlappedionotifier.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWinOverlappedIoNotifier::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN24QWinOverlappedIoNotifier10setEnabledEb', enabled,
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWinOverlappedIoNotifier::QWinOverlappedIoNotifier(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwinoverlappedionotifier.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWinOverlappedIoNotifier::QWinOverlappedIoNotifier(QObject *parent)
    self._noteCreation(QWinOverlappedIoNotifier, lambda: Rituals.call(
        'ritual_ZN24QWinOverlappedIoNotifierC1EP7QObject',
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

  def _q_notify(self) -> None:
    """
    Calls Qt's 'void QWinOverlappedIoNotifier::_q_notify()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwinoverlappedionotifier.html#_q_notify
    """
    #  void QWinOverlappedIoNotifier::_q_notify()
    self.uglySide.call('ritual_ZN24QWinOverlappedIoNotifier9_q_notifyEv')

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'Qt::HANDLE QWinOverlappedIoNotifier::handle() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWinOverlappedIoNotifier.handle' has no cute function yet. Qt's "
        "'Qt::HANDLE QWinOverlappedIoNotifier::handle() const': gives "
        "'void', which has no cute class yet.")

  @staticmethod
  def notified(*__, **_) -> Never:
    """
    Qt's 'void QWinOverlappedIoNotifier::notified(quint32 numberOfBytes,
    quint32 errorCode, OVERLAPPED *overlapped)': names 'OVERLAPPED', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QWinOverlappedIoNotifier.notified' has no cute function yet. Qt's "
        "'void QWinOverlappedIoNotifier::notified(quint32 numberOfBytes, "
        "quint32 errorCode, OVERLAPPED *overlapped)': names 'OVERLAPPED', "
        "which has no cute class yet.")

  @staticmethod
  def setHandle(*__, **_) -> Never:
    """
    Qt's 'void QWinOverlappedIoNotifier::setHandle(Qt::HANDLE h)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWinOverlappedIoNotifier.setHandle' has no cute function yet. "
        "Qt's 'void QWinOverlappedIoNotifier::setHandle(Qt::HANDLE h)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def waitForAnyNotified(*__, **_) -> Never:
    """
    Qt's 'OVERLAPPED
    *QWinOverlappedIoNotifier::waitForAnyNotified(QDeadlineTimer deadline)':
    gives 'struct _OVERLAPPED', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWinOverlappedIoNotifier.waitForAnyNotified' has no cute function "
        "yet. Qt's 'OVERLAPPED "
        "*QWinOverlappedIoNotifier::waitForAnyNotified(QDeadlineTimer "
        "deadline)': gives 'struct _OVERLAPPED', which has no cute class "
        "yet.")

  @staticmethod
  def waitForNotified(*__, **_) -> Never:
    """
    Qt's 'bool QWinOverlappedIoNotifier::waitForNotified(QDeadlineTimer
    deadline, OVERLAPPED *overlapped)': names 'OVERLAPPED', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QWinOverlappedIoNotifier.waitForNotified' has no cute function "
        "yet. Qt's 'bool "
        "QWinOverlappedIoNotifier::waitForNotified(QDeadlineTimer deadline, "
        "OVERLAPPED *overlapped)': names 'OVERLAPPED', which has no cute "
        "class yet.")
