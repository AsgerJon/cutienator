"""
QDefaultAnimationDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDefaultAnimationDriver to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAnimationDriver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDefaultAnimationDriver(QAnimationDriver):
  """
  The cute side of Qt's QDefaultAnimationDriver: a plain Python object
  standing in front of one C++ QDefaultAnimationDriver.

  It is built on the cute 'QAnimationDriver', as Qt's QDefaultAnimationDriver
  is built on Qt's QAnimationDriver, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDefaultAnimationDriver that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'timerEvent',
  'startTimer', 'stopTimer'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDefaultAnimationDriver::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDefaultAnimationDriver::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDefaultAnimationDriver::~QDefaultAnimationDriver()': the
    destructor: Python never removes a C++ QDefaultAnimationDriver.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 leans on
  'QDefaultAnimationDriver.

  What to expect
  --------------

  - The C++ QDefaultAnimationDriver is created at the first use, not by
    'QDefaultAnimationDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDefaultAnimationDriver.
  - Qt tells when it has removed the C++ QDefaultAnimationDriver. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDefaultAnimationDriver that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDefaultAnimationDriver'

  #  A C++ QDefaultAnimationDriver Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDefaultAnimationDriver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDefaultAnimationDriver::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdefaultanimationdriver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDefaultAnimationDriver::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QDefaultAnimationDriver10metaObjectEv',
    )
    from . import QMetaObject
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
    Qt's 'QDefaultAnimationDriver::QDefaultAnimationDriver(QUnifiedTimer
    *timer)': leans on
    'QDefaultAnimationDriver::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDefaultAnimationDriver.__init__' has no cute function yet. Qt's "
        "'QDefaultAnimationDriver::QDefaultAnimationDriver(QUnifiedTimer "
        "*timer)': leans on "
        "'QDefaultAnimationDriver::qt_metacall(QMetaObject::Call, int, "
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

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QDefaultAnimationDriver::timerEvent(QTimerEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdefaultanimationdriver.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDefaultAnimationDriver::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN23QDefaultAnimationDriver10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QDefaultAnimationDriver10timerEventEP11QTimerEven'
          't')
    self.uglySide.call(ritual, self._addressOf(e))

  def startTimer(self) -> None:
    """
    Calls Qt's 'void QDefaultAnimationDriver::startTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdefaultanimationdriver.html#startTimer
    """
    #  void QDefaultAnimationDriver::startTimer()
    self.uglySide.call('ritual_ZN23QDefaultAnimationDriver10startTimerEv')

  def stopTimer(self) -> None:
    """
    Calls Qt's 'void QDefaultAnimationDriver::stopTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdefaultanimationdriver.html#stopTimer
    """
    #  void QDefaultAnimationDriver::stopTimer()
    self.uglySide.call('ritual_ZN23QDefaultAnimationDriver9stopTimerEv')
