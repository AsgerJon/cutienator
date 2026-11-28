"""
QQuickIOSCursorFlashTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2IOSStyleImpl/6.12.0/QtQuickControls2IOSStyleImpl/private/qquickioscursorflashtimer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickIOSCursorFlashTimer to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

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


class QQuickIOSCursorFlashTimer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickIOSCursorFlashTimer: a plain Python object
  standing in front of one C++ QQuickIOSCursorFlashTimer.

  What exists
  -----------

  Every function of Qt's QQuickIOSCursorFlashTimer that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'visible',
  'cursorPosition', 'running', 'start', 'stop', 'timerEvent',
  'visibleChanged', 'cursorPositionChanged', 'runningChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickIOSCursorFlashTimer::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickIOSCursorFlashTimer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 19 functions Qt declares: 4 leans on 'QQuickIOSCursorFlashTimer; 2
  not a gap; 1 leans on 'vtable for QQuickIOSCursorFlashTimer', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQuickIOSCursorFlashTimer is created at the first use, not by
    'QQuickIOSCursorFlashTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickIOSCursorFlashTimer.
  - Qt tells when it has removed the C++ QQuickIOSCursorFlashTimer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickIOSCursorFlashTimer that has no cute function
    yet, '__init__', 'setCursorPosition', 'setRunning', 'setVisible', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIOSCursorFlashTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickIOSCursorFlashTimer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickIOSCursorFlashTimer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickIOSCursorFlashTimer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def visible(self) -> bool:
    """
    Calls Qt's 'bool QQuickIOSCursorFlashTimer::visible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#visible
    """
    #  bool QQuickIOSCursorFlashTimer::visible() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickIOSCursorFlashTimer7visibleEv',
    )

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QQuickIOSCursorFlashTimer::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#cursorPosition
    """
    #  int QQuickIOSCursorFlashTimer::cursorPosition() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickIOSCursorFlashTimer14cursorPositionEv',
    )

  def running(self) -> bool:
    """
    Calls Qt's 'bool QQuickIOSCursorFlashTimer::running() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#running
    """
    #  bool QQuickIOSCursorFlashTimer::running() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickIOSCursorFlashTimer7runningEv',
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
    Qt's 'QQuickIOSCursorFlashTimer::QQuickIOSCursorFlashTimer(QObject
    *parent)': leans on 'vtable for QQuickIOSCursorFlashTimer', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickIOSCursorFlashTimer.__init__' has no cute function yet. "
        "Qt's 'QQuickIOSCursorFlashTimer::QQuickIOSCursorFlashTimer(QObject "
        "*parent)': leans on 'vtable for QQuickIOSCursorFlashTimer', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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
    Calls Qt's 'void QQuickIOSCursorFlashTimer::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#start
    """
    #  void QQuickIOSCursorFlashTimer::start()
    self.uglySide.call('ritual_ZN25QQuickIOSCursorFlashTimer5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickIOSCursorFlashTimer::stop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#stop
    """
    #  void QQuickIOSCursorFlashTimer::stop()
    self.uglySide.call('ritual_ZN25QQuickIOSCursorFlashTimer4stopEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickIOSCursorFlashTimer::timerEvent(QTimerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIOSCursorFlashTimer::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_ZN25QQuickIOSCursorFlashTimer10timerEventEP11QTimerEvent',
        self._addressOf(event),
    )

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIOSCursorFlashTimer::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#visibleChanged
    """
    #  void QQuickIOSCursorFlashTimer::visibleChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickIOSCursorFlashTimer14visibleChangedEv',
    )

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickIOSCursorFlashTimer::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html
    """
    #  void QQuickIOSCursorFlashTimer::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickIOSCursorFlashTimer21cursorPositionChangedEv',
    )

  @overload(bool)
  def runningChanged(self, running: bool) -> None:
    """
    Calls Qt's 'void QQuickIOSCursorFlashTimer::runningChanged(bool
    running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickioscursorflashtimer.html#runningChanged

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQuickIOSCursorFlashTimer::runningChanged(bool running)
    self.uglySide.call(
        'ritual_ZN25QQuickIOSCursorFlashTimer14runningChangedEb', running,
    )

  @staticmethod
  def setCursorPosition(*__, **_) -> Never:
    """
    Qt's 'void QQuickIOSCursorFlashTimer::setCursorPosition(int
    cursorPosition)': leans on
    'QQuickIOSCursorFlashTimer::cursorPositionChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickIOSCursorFlashTimer.setCursorPosition' has no cute function "
        "yet. Qt's 'void QQuickIOSCursorFlashTimer::setCursorPosition(int "
        "cursorPosition)': leans on "
        "'QQuickIOSCursorFlashTimer::cursorPositionChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setRunning(*__, **_) -> Never:
    """
    Qt's 'void QQuickIOSCursorFlashTimer::setRunning(bool running)': leans on
    'QQuickIOSCursorFlashTimer::runningChanged(bool)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickIOSCursorFlashTimer.setRunning' has no cute function yet. "
        "Qt's 'void QQuickIOSCursorFlashTimer::setRunning(bool running)': "
        "leans on 'QQuickIOSCursorFlashTimer::runningChanged(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setVisible(*__, **_) -> Never:
    """
    Qt's 'void QQuickIOSCursorFlashTimer::setVisible(bool visible)': leans on
    'QQuickIOSCursorFlashTimer::visibleChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickIOSCursorFlashTimer.setVisible' has no cute function yet. "
        "Qt's 'void QQuickIOSCursorFlashTimer::setVisible(bool visible)': "
        "leans on 'QQuickIOSCursorFlashTimer::visibleChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
