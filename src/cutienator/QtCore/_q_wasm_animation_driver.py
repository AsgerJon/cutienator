"""
QWasmAnimationDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qwasmanimationdriver_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QWasmAnimationDriver to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAnimationDriver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaObject, QUnifiedTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUnifiedTimer = WAIT['QUnifiedTimer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWasmAnimationDriver(QAnimationDriver):
  """
  The cute side of Qt's QWasmAnimationDriver: a plain Python object standing
  in front of one C++ QWasmAnimationDriver.

  It is built on the cute 'QAnimationDriver', as Qt's QWasmAnimationDriver is
  built on Qt's QAnimationDriver, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWasmAnimationDriver that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'elapsed',
  'start', 'stop', 'handleAnimationFrame', 'handleFallbackTimeout',
  'getCurrentTimeFromTimeline'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWasmAnimationDriver::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWasmAnimationDriver::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWasmAnimationDriver::~QWasmAnimationDriver()': the destructor:
    Python never removes a C++ QWasmAnimationDriver.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWasmAnimationDriver is created at the first use, not by
    'QWasmAnimationDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWasmAnimationDriver.
  - Qt tells when it has removed the C++ QWasmAnimationDriver. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QWasmAnimationDriver::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwasmanimationdriver.html#tr

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
    #  QString QWasmAnimationDriver::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QWasmAnimationDriver2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWasmAnimationDriver'

  #  A C++ QWasmAnimationDriver Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWasmAnimationDriver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWasmAnimationDriver::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwasmanimationdriver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWasmAnimationDriver::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QWasmAnimationDriver10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def elapsed(self) -> int:
    """
    Calls Qt's 'qint64 QWasmAnimationDriver::elapsed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwasmanimationdriver.html#elapsed
    """
    #  qint64 QWasmAnimationDriver::elapsed() const
    ritual = 'ritual_ZNK20QWasmAnimationDriver7elapsedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QWasmAnimationDriver7elapsedEv'
    return self.uglySide.call(ritual)

  def getCurrentTimeFromTimeline(self) -> float:
    """
    Calls Qt's 'double QWasmAnimationDriver::getCurrentTimeFromTimeline()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwasmanimationdriver.html
    """
    #  double QWasmAnimationDriver::getCurrentTimeFromTimeline() const
    return self.uglySide.call(
        'ritual_ZNK20QWasmAnimationDriver26getCurrentTimeFromTimelineEv',
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

  @overload(QUnifiedTimer)
  @overload(NoneType)
  def __init__(self, unifiedTimer: Optional[QUnifiedTimer]) -> None:
    """
    Notes what was given, for Qt's
    'QWasmAnimationDriver::QWasmAnimationDriver(QUnifiedTimer
    *unifiedTimer)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwasmanimationdriver.html#QWasmAnimationDriver

    Parameters
    ----------

    unifiedTimer : Optional[QUnifiedTimer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWasmAnimationDriver::QWasmAnimationDriver(QUnifiedTimer
    #      *unifiedTimer)
    self._noteCreation(QWasmAnimationDriver, lambda: Rituals.call(
        'ritual_ZN20QWasmAnimationDriverC1EP13QUnifiedTimer',
        self._addressOf(unifiedTimer),
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

  def start(self) -> None:
    """
    Calls Qt's 'void QWasmAnimationDriver::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qwasmanimationdriver.html#start
    """
    #  void QWasmAnimationDriver::start()
    ritual = 'ritual_ZN20QWasmAnimationDriver5startEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QWasmAnimationDriver5startEv'
    self.uglySide.call(ritual)

  def stop(self) -> None:
    """
    Calls Qt's 'void QWasmAnimationDriver::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qwasmanimationdriver.html#stop
    """
    #  void QWasmAnimationDriver::stop()
    ritual = 'ritual_ZN20QWasmAnimationDriver4stopEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QWasmAnimationDriver4stopEv'
    self.uglySide.call(ritual)

  @overload(float)
  def handleAnimationFrame(self, timestamp: float) -> None:
    """
    Calls Qt's 'void QWasmAnimationDriver::handleAnimationFrame(double
    timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwasmanimationdriver.html#handleAnimationFrame

    Parameters
    ----------

    timestamp : float
      Passed on as it is.
    """
    #  void QWasmAnimationDriver::handleAnimationFrame(double timestamp)
    self.uglySide.call(
        'ritual_ZN20QWasmAnimationDriver20handleAnimationFrameEd', timestamp,
    )

  def handleFallbackTimeout(self) -> None:
    """
    Calls Qt's 'void QWasmAnimationDriver::handleFallbackTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwasmanimationdriver.html#handleFallbackTimeout
    """
    #  void QWasmAnimationDriver::handleFallbackTimeout()
    self.uglySide.call(
        'ritual_ZN20QWasmAnimationDriver21handleFallbackTimeoutEv',
    )
