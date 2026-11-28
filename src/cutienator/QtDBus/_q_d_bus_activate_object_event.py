"""
QDBusActivateObjectEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusintegrator_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusActivateObjectEvent to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class QDBusActivateObjectEvent(QAbstractMetaCallEvent):
  """
  The cute side of Qt's QDBusActivateObjectEvent: a plain Python object
  standing in front of one C++ QDBusActivateObjectEvent.

  It is built on the cute 'QAbstractMetaCallEvent', as Qt's
  QDBusActivateObjectEvent is built on Qt's QAbstractMetaCallEvent, and has
  everything that class has.

  C++ hands a QDBusActivateObjectEvent around as a copy, so every C++
  QDBusActivateObjectEvent behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusActivateObjectEvent that has a ritual and that
  Python can call so far, 1 name in all: 'placeMetaCall'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusActivateObjectEvent::~QDBusActivateObjectEvent()': the
    destructor: Python removes its C++ QDBusActivateObjectEvent by it, and
    has no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 leans on
  'qDBusInterfaceInObject(QObject*, QString const&)', which Qt's source does
  not mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QDBusActivateObjectEvent is created at the first use, not by
    'QDBusActivateObjectEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusActivateObjectEvent back gives a copy the ritual
    made for Python, in a new cute QDBusActivateObjectEvent.
  - Each name of Qt's QDBusActivateObjectEvent that has no cute function yet,
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
  __qt_class__ = 'QDBusActivateObjectEvent'

  #  A C++ QDBusActivateObjectEvent Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusActivateObjectEvent'

  #  Qt's '~QDBusActivateObjectEvent()'. Naming it makes this a value class:
  #  Python owns every C++ QDBusActivateObjectEvent behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QDBusActivateObjectEventD1Ev'

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
    Qt's 'QDBusActivateObjectEvent::QDBusActivateObjectEvent(const
    QDBusConnection &c, QObject *sender, const
    QDBusConnectionPrivate::ObjectTreeNode &n, int p, const QDBusMessage &m,
    QLatch *l)': leans on 'qDBusInterfaceInObject(QObject*, QString const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDBusActivateObjectEvent.__init__' has no cute function yet. Qt's "
        "'QDBusActivateObjectEvent::QDBusActivateObjectEvent(const "
        "QDBusConnection &c, QObject *sender, const "
        "QDBusConnectionPrivate::ObjectTreeNode &n, int p, const "
        "QDBusMessage &m, QLatch *l)': leans on "
        "'qDBusInterfaceInObject(QObject*, QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Calls Qt's 'void QDBusActivateObjectEvent::placeMetaCall(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusactivateobjectevent.html#placeMetaCall

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusActivateObjectEvent::placeMetaCall(QObject *a0)
    self.uglySide.call(
        'ritual_ZN24QDBusActivateObjectEvent13placeMetaCallEP7QObject',
        self._addressOf(a0, 'QObject'),
    )
