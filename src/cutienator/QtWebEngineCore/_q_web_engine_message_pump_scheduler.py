"""
QWebEngineMessagePumpScheduler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/6.12.0/QtWebEngineCore/private/qwebenginemessagepumpscheduler_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWebEngineMessagePumpScheduler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineMessagePumpScheduler(QObject):
  """
  The cute side of Qt's QWebEngineMessagePumpScheduler: a plain Python object
  standing in front of one C++ QWebEngineMessagePumpScheduler.

  It is built on the cute 'QObject', as Qt's QWebEngineMessagePumpScheduler
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineMessagePumpScheduler that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'scheduleImmediateWork', 'scheduleDelayedWork', 'timerEvent'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineMessagePumpScheduler::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWebEngineMessagePumpScheduler::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QWebEngineMessagePumpScheduler::QWebEngineMessagePumpScheduler(std::
    function<void ()> callback)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWebEngineMessagePumpScheduler is created at the first use, not
    by 'QWebEngineMessagePumpScheduler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineMessagePumpScheduler.
  - Qt tells when it has removed the C++ QWebEngineMessagePumpScheduler.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWebEngineMessagePumpScheduler that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QWebEngineMessagePumpScheduler::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginemessagepumpscheduler.html#tr

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
    #  QString QWebEngineMessagePumpScheduler::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN30QWebEngineMessagePumpScheduler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineMessagePumpScheduler'

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
    *QWebEngineMessagePumpScheduler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginemessagepumpscheduler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineMessagePumpScheduler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK30QWebEngineMessagePumpScheduler10metaObjectEv',
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
    Qt's
    'QWebEngineMessagePumpScheduler::QWebEngineMessagePumpScheduler(std::
    function<void ()> callback)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QWebEngineMessagePumpScheduler.__init__' has no cute function "
        "yet. Qt's "
        "'QWebEngineMessagePumpScheduler::QWebEngineMessagePumpScheduler(std"
        "::function<void ()> callback)': takes a type Python has no way to "
        "hand over yet.")

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

  def scheduleImmediateWork(self) -> None:
    """
    Calls Qt's 'void
    QWebEngineMessagePumpScheduler::scheduleImmediateWork()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginemessagepumpscheduler.html
    """
    #  void QWebEngineMessagePumpScheduler::scheduleImmediateWork()
    self.uglySide.call(
        'ritual_ZN30QWebEngineMessagePumpScheduler21scheduleImmediateWorkEv',
    )

  @overload(int)
  def scheduleDelayedWork(self, delay: int) -> None:
    """
    Calls Qt's 'void QWebEngineMessagePumpScheduler::scheduleDelayedWork(int
    delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginemessagepumpscheduler.html

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QWebEngineMessagePumpScheduler::scheduleDelayedWork(int delay)
    self.uglySide.call(
        'ritual_ZN30QWebEngineMessagePumpScheduler19scheduleDelayedWorkEi',
        delay,
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, ev: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QWebEngineMessagePumpScheduler::timerEvent(QTimerEvent
    *ev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginemessagepumpscheduler.html#timerEvent

    Parameters
    ----------

    ev : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWebEngineMessagePumpScheduler::timerEvent(QTimerEvent *ev)
    ritual = (
        'ritual_ZN30QWebEngineMessagePumpScheduler10timerEventEP11QTimerEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QWebEngineMessagePumpScheduler10timerEventEP11QTi'
          'merEvent')
    self.uglySide.call(ritual, self._addressOf(ev))
