"""
QScxmlInternal::EventLoopHook binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScxmlInternal::EventLoopHook to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
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


class EventLoopHook(QObject):
  """
  The cute side of Qt's QScxmlInternal::EventLoopHook: a plain Python object
  standing in front of one C++ QScxmlInternal::EventLoopHook.

  It is built on the cute 'QObject', as Qt's QScxmlInternal::EventLoopHook is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlInternal::EventLoopHook that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject',
  'queueProcessEvents', 'doProcessEvents', 'timerEvent'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlInternal::EventLoopHook::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QScxmlInternal::EventLoopHook::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 not a gap; 2 leans on 'QScxmlInternal.

  What to expect
  --------------

  - The C++ QScxmlInternal::EventLoopHook is created at the first use, not by
    'QScxmlInternal::EventLoopHook(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlInternal::EventLoopHook.
  - Qt tells when it has removed the C++ QScxmlInternal::EventLoopHook. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlInternal::EventLoopHook that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInternal::EventLoopHook'

  #  A C++ QScxmlInternal::EventLoopHook Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScxmlInternal_EventLoopHook'

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
    *QScxmlInternal::EventLoopHook::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-eventloophook.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlInternal::EventLoopHook::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK14QScxmlInternal13EventLoopHook10metaObjectEv',
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
    'QScxmlInternal::EventLoopHook::EventLoopHook(QScxmlStateMachinePrivate
    *smp)': leans on
    'QScxmlInternal::EventLoopHook::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScxmlInternal.EventLoopHook.__init__' has no cute function yet. "
        "Qt's "
        "'QScxmlInternal::EventLoopHook::EventLoopHook(QScxmlStateMachinePri"
        "vate *smp)': leans on "
        "'QScxmlInternal::EventLoopHook::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def queueProcessEvents(self) -> None:
    """
    Calls Qt's 'void QScxmlInternal::EventLoopHook::queueProcessEvents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-eventloophook.html
    """
    #  void QScxmlInternal::EventLoopHook::queueProcessEvents()
    self.uglySide.call(
        'ritual_ZN14QScxmlInternal13EventLoopHook18queueProcessEventsEv',
    )

  def doProcessEvents(self) -> None:
    """
    Calls Qt's 'void QScxmlInternal::EventLoopHook::doProcessEvents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-eventloophook.html#doProcessEvents
    """
    #  void QScxmlInternal::EventLoopHook::doProcessEvents()
    self.uglySide.call(
        'ritual_ZN14QScxmlInternal13EventLoopHook15doProcessEventsEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, timerEvent: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QScxmlInternal::EventLoopHook::timerEvent(QTimerEvent
    *timerEvent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-eventloophook.html#timerEvent

    Parameters
    ----------

    timerEvent : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlInternal::EventLoopHook::timerEvent(QTimerEvent
    #      *timerEvent)
    ritual = (
        'ritual_ZN14QScxmlInternal13EventLoopHook10timerEventEP11QTimerEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QScxmlInternal13EventLoopHook10timerEventEP11QTim'
          'erEvent')
    self.uglySide.call(ritual, self._addressOf(timerEvent))
