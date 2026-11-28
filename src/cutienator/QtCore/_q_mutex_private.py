"""
QMutexPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmutex_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QMutexPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMutexPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMutexPrivate: a plain Python object standing in
  front of one C++ QMutexPrivate.

  C++ hands a QMutexPrivate around as a copy, so every C++ QMutexPrivate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMutexPrivate that has a ritual and that Python can
  call so far, 1 name in all: 'ref'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMutexPrivate::~QMutexPrivate()': the destructor: Python removes
    its C++ QMutexPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 9 functions Qt declares: 4 leans on 'QMutexPrivate; 3 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file.

  What to expect
  --------------

  - The C++ QMutexPrivate is created at the first use, not by
    'QMutexPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMutexPrivate back gives a copy the ritual made for
    Python, in a new cute QMutexPrivate.
  - Each name of Qt's QMutexPrivate that has no cute function yet,
    '__init__', 'allocate', 'deref', 'derefWaiters', 'release', 'wait',
    'wakeUp', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QMutexPrivate'

  #  Qt's '~QMutexPrivate()'. Naming it makes this a value class: Python owns
  #  every C++ QMutexPrivate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QMutexPrivateD1Ev'

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
    Qt's 'QMutexPrivate::QMutexPrivate()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qt_report_error'.
    """
    raise NotImplementedError(
        "'QMutexPrivate.__init__' has no cute function yet. Qt's "
        "'QMutexPrivate::QMutexPrivate()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'qt_report_error'.")

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

  def ref(self) -> bool:
    """
    Calls Qt's 'bool QMutexPrivate::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qmutexprivate.html#ref
    """
    #  bool QMutexPrivate::ref()
    return self.uglySide.call('ritual_ZN13QMutexPrivate3refEv')

  @staticmethod
  def allocate(*__, **_) -> Never:
    """
    Qt's 'QMutexPrivate *QMutexPrivate::allocate()': leans on
    'QMutexPrivate::allocate()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMutexPrivate.allocate' has no cute function yet. Qt's "
        "'QMutexPrivate *QMutexPrivate::allocate()': leans on "
        "'QMutexPrivate::allocate()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def deref(*__, **_) -> Never:
    """
    Qt's 'void QMutexPrivate::deref()': leans on 'QMutexPrivate::release()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QMutexPrivate.deref' has no cute function yet. Qt's 'void "
        "QMutexPrivate::deref()': leans on 'QMutexPrivate::release()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def derefWaiters(*__, **_) -> Never:
    """
    Qt's 'void QMutexPrivate::derefWaiters(int value)': leans on
    'QMutexPrivate::derefWaiters(int)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMutexPrivate.derefWaiters' has no cute function yet. Qt's 'void "
        "QMutexPrivate::derefWaiters(int value)': leans on "
        "'QMutexPrivate::derefWaiters(int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'void QMutexPrivate::release()': leans on
    'QMutexPrivate::release()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMutexPrivate.release' has no cute function yet. Qt's 'void "
        "QMutexPrivate::release()': leans on 'QMutexPrivate::release()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def wait(*__, **_) -> Never:
    """
    Qt's 'bool QMutexPrivate::wait(QDeadlineTimer timeout)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'qt_report_error'.
    """
    raise NotImplementedError(
        "'QMutexPrivate.wait' has no cute function yet. Qt's 'bool "
        "QMutexPrivate::wait(QDeadlineTimer timeout)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'qt_report_error'.")

  @staticmethod
  def wakeUp(*__, **_) -> Never:
    """
    Qt's 'void QMutexPrivate::wakeUp()': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'qt_report_error'.
    """
    raise NotImplementedError(
        "'QMutexPrivate.wakeUp' has no cute function yet. Qt's 'void "
        "QMutexPrivate::wakeUp()': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qt_report_error'.")
