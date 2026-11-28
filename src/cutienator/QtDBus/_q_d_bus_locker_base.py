"""
QDBusLockerBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusthreaddebug_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusLockerBase to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDBusConnectionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnectionPrivate = WAIT['QDBusConnectionPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusLockerBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusLockerBase: a plain Python object standing in
  front of one C++ QDBusLockerBase.

  C++ hands a QDBusLockerBase around as a copy, so every C++ QDBusLockerBase
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusLockerBase that has a ritual and that Python
  can call so far, 1 name in all: 'reportThreadAction'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusLockerBase::~QDBusLockerBase()': the destructor: Python
    removes its C++ QDBusLockerBase by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDBusLockerBase is created at the first use, not by
    'QDBusLockerBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusLockerBase back gives a copy the ritual made for
    Python, in a new cute QDBusLockerBase.
  """

  #  The enums Qt writes inside QDBusLockerBase, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Condition(CuteNum):
    """
    The enum 'QDBusLockerBase::Condition' of Qt, with the 12 names Qt gives
    in it.
    """

    BeforeLock = Kee[int](0)
    AfterLock = Kee[int](1)
    BeforeUnlock = Kee[int](2)
    AfterUnlock = Kee[int](3)
    BeforePost = Kee[int](4)
    AfterPost = Kee[int](5)
    BeforeDeliver = Kee[int](6)
    AfterDeliver = Kee[int](7)
    BeforeAcquire = Kee[int](8)
    AfterAcquire = Kee[int](9)
    BeforeRelease = Kee[int](10)
    AfterRelease = Kee[int](11)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int, QDBusConnectionPrivate)
  @overload(int, int, NoneType)
  def reportThreadAction(
      a0: int,
      a1: int,
      a2: Optional[QDBusConnectionPrivate],
  ) -> None:
    """
    Calls Qt's 'void QDBusLockerBase::reportThreadAction(int a0, int a1,
    QDBusConnectionPrivate *a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuslockerbase.html#reportThreadAction

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.

    a2 : Optional[QDBusConnectionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDBusLockerBase::reportThreadAction(int a0, int a1,
    #      QDBusConnectionPrivate *a2)
    Rituals.call(
        'ritual_ZN15QDBusLockerBase18reportThreadActionEiiP22QDBusConnectio'
        'nPrivate',
        a0, a1, CuteMixin._addressOf(a2),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusLockerBase'

  #  Qt's '~QDBusLockerBase()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusLockerBase behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDBusLockerBaseD1Ev'

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
