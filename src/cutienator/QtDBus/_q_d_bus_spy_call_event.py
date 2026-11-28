"""
QDBusSpyCallEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusSpyCallEvent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QAbstractMetaCallEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusSpyCallEvent(QAbstractMetaCallEvent):
  """
  The cute side of Qt's QDBusSpyCallEvent: a plain Python object standing in
  front of one C++ QDBusSpyCallEvent.

  It is built on the cute 'QAbstractMetaCallEvent', as Qt's QDBusSpyCallEvent
  is built on Qt's QAbstractMetaCallEvent, and has everything that class has.

  C++ hands a QDBusSpyCallEvent around as a copy, so every C++
  QDBusSpyCallEvent behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusSpyCallEvent that has a ritual and that Python
  can call so far, 1 name in all: 'placeMetaCall'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusSpyCallEvent::~QDBusSpyCallEvent()': the destructor: Python
    removes its C++ QDBusSpyCallEvent by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QDBusSpyCallEvent.

  What to expect
  --------------

  - The C++ QDBusSpyCallEvent is created at the first use, not by
    'QDBusSpyCallEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusSpyCallEvent back gives a copy the ritual made
    for Python, in a new cute QDBusSpyCallEvent.
  - Each name of Qt's QDBusSpyCallEvent that has no cute function yet,
    '__init__', 'invokeSpyHooks', holds a function that raises
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
  __qt_class__ = 'QDBusSpyCallEvent'

  #  A C++ QDBusSpyCallEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusSpyCallEvent'

  #  Qt's '~QDBusSpyCallEvent()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusSpyCallEvent behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QDBusSpyCallEventD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QDBusSpyCallEvent::QDBusSpyCallEvent(QDBusConnectionPrivate *cp,
    const QDBusConnection &c, const QDBusMessage &msg)': leans on
    'QDBusSpyCallEvent::~QDBusSpyCallEvent()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusSpyCallEvent.__init__' has no cute function yet. Qt's "
        "'QDBusSpyCallEvent::QDBusSpyCallEvent(QDBusConnectionPrivate *cp, "
        "const QDBusConnection &c, const QDBusMessage &msg)': leans on "
        "'QDBusSpyCallEvent::~QDBusSpyCallEvent()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
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

  @overload(QObject)
  @overload(NoneType)
  def placeMetaCall(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QDBusSpyCallEvent::placeMetaCall(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusspycallevent.html#placeMetaCall

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusSpyCallEvent::placeMetaCall(QObject *a0)
    self.uglySide.call(
        'ritual_ZN17QDBusSpyCallEvent13placeMetaCallEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @staticmethod
  def invokeSpyHooks(*__, **_) -> Never:
    """
    Qt's 'void QDBusSpyCallEvent::invokeSpyHooks(const QDBusMessage &msg)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'qDBusSpyHookList'.
    """
    raise NotImplementedError(
        "'QDBusSpyCallEvent.invokeSpyHooks' has no cute function yet. Qt's "
        "'void QDBusSpyCallEvent::invokeSpyHooks(const QDBusMessage &msg)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qDBusSpyHookList'.")
