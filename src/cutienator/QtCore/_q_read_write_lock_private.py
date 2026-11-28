"""
QReadWriteLockPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qreadwritelock_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QReadWriteLockPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']


class QReadWriteLockPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QReadWriteLockPrivate: a plain Python object standing
  in front of one C++ QReadWriteLockPrivate.

  What exists
  -----------

  Every function of Qt's QReadWriteLockPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'unlock', 'recursiveLockForWrite',
  'recursiveLockForRead'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool
    QReadWriteLockPrivate::lockForWrite(std::unique_lock<std::mutex> &lock,
    QDeadlineTimer timeout)': takes a type Python has no way to hand over
    yet.
  - Qt's 'bool
    QReadWriteLockPrivate::lockForRead(std::unique_lock<std::mutex> &lock,
    QDeadlineTimer timeout)': takes a type Python has no way to hand over
    yet.
  - Qt's 'quintptr QReadWriteLockPrivate::describeState(void *dd)': names
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 a template.

  What to expect
  --------------

  - The C++ QReadWriteLockPrivate is created at the first use, not by
    'QReadWriteLockPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QReadWriteLockPrivate.
  - Each name of Qt's QReadWriteLockPrivate that has no cute function yet,
    'allocate', 'describeState', 'lockForRead', 'lockForWrite',
    'recursiveUnlock', 'release', 'waitConditionWait', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QReadWriteLockPrivate, each a class in here
  #  as in C++.

  class Reader(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QReadWriteLockPrivate::Reader: a plain Python
    object standing in front of one C++ QReadWriteLockPrivate::Reader.

    C++ hands a QReadWriteLockPrivate::Reader around as a copy, so every C++
    QReadWriteLockPrivate::Reader behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QReadWriteLockPrivate::Reader yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QReadWriteLockPrivate::Reader::~Reader()': the destructor: Python
      removes its C++ QReadWriteLockPrivate::Reader by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QReadWriteLockPrivate::Reader is created at the first use, not
      by 'QReadWriteLockPrivate::Reader(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QReadWriteLockPrivate::Reader back gives a copy the
      ritual made for Python, in a new cute QReadWriteLockPrivate::Reader.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QReadWriteLockPrivate::Reader'

    #  Qt's '~QReadWriteLockPrivate::Reader()'. Naming it makes this a value
    #  class: Python owns every C++ QReadWriteLockPrivate::Reader behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QReadWriteLockPrivate6ReaderD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QReadWriteLockPrivate'

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

  @overload()
  @overload(bool)
  def __init__(self, isRecursive: bool = False) -> None:
    """
    Notes what was given, for Qt's
    'QReadWriteLockPrivate::QReadWriteLockPrivate(bool isRecursive)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qreadwritelockprivate.html#QReadWriteLockPrivate

    Parameters
    ----------

    isRecursive : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QReadWriteLockPrivate::QReadWriteLockPrivate(bool isRecursive)
    self._noteCreation(QReadWriteLockPrivate, lambda: Rituals.call(
        'ritual_ZN21QReadWriteLockPrivateC1Eb', isRecursive,
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

  def unlock(self) -> None:
    """
    Calls Qt's 'void QReadWriteLockPrivate::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qreadwritelockprivate.html#unlock
    """
    #  void QReadWriteLockPrivate::unlock()
    self.uglySide.call('ritual_ZN21QReadWriteLockPrivate6unlockEv')

  @overload(QDeadlineTimer)
  def recursiveLockForWrite(self, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool
    QReadWriteLockPrivate::recursiveLockForWrite(QDeadlineTimer timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreadwritelockprivate.html#recursiveLockForWrite

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QReadWriteLockPrivate::recursiveLockForWrite(QDeadlineTimer
    #      timeout)
    return self.uglySide.call(
        'ritual_ZN21QReadWriteLockPrivate21recursiveLockForWriteE14QDeadlin'
        'eTimer',
        self._valueOf(timeout),
    )

  @overload(QDeadlineTimer)
  def recursiveLockForRead(self, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool
    QReadWriteLockPrivate::recursiveLockForRead(QDeadlineTimer timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreadwritelockprivate.html#recursiveLockForRead

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QReadWriteLockPrivate::recursiveLockForRead(QDeadlineTimer
    #      timeout)
    return self.uglySide.call(
        'ritual_ZN21QReadWriteLockPrivate20recursiveLockForReadE14QDeadline'
        'Timer',
        self._valueOf(timeout),
    )

  @staticmethod
  def allocate(*__, **_) -> Never:
    """
    Qt's 'QReadWriteLockPrivate *QReadWriteLockPrivate::allocate()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'qrwl_freelist'.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.allocate' has no cute function yet. Qt's "
        "'QReadWriteLockPrivate *QReadWriteLockPrivate::allocate()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'qrwl_freelist'.")

  @staticmethod
  def describeState(*__, **_) -> Never:
    """
    Qt's 'quintptr QReadWriteLockPrivate::describeState(void *dd)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.describeState' has no cute function yet. "
        "Qt's 'quintptr QReadWriteLockPrivate::describeState(void *dd)': "
        "names 'void', which has no cute class yet.")

  @staticmethod
  def lockForRead(*__, **_) -> Never:
    """
    Qt's 'bool
    QReadWriteLockPrivate::lockForRead(std::unique_lock<std::mutex> &lock,
    QDeadlineTimer timeout)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.lockForRead' has no cute function yet. Qt's "
        "'bool "
        "QReadWriteLockPrivate::lockForRead(std::unique_lock<std::mutex> "
        "&lock, QDeadlineTimer timeout)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def lockForWrite(*__, **_) -> Never:
    """
    Qt's 'bool
    QReadWriteLockPrivate::lockForWrite(std::unique_lock<std::mutex> &lock,
    QDeadlineTimer timeout)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.lockForWrite' has no cute function yet. "
        "Qt's 'bool "
        "QReadWriteLockPrivate::lockForWrite(std::unique_lock<std::mutex> "
        "&lock, QDeadlineTimer timeout)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def recursiveUnlock(*__, **_) -> Never:
    """
    Qt's 'void QReadWriteLockPrivate::recursiveUnlock()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'handleEquals'.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.recursiveUnlock' has no cute function yet. "
        "Qt's 'void QReadWriteLockPrivate::recursiveUnlock()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'handleEquals'.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'void QReadWriteLockPrivate::release()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'qrwl_freelist'.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.release' has no cute function yet. Qt's "
        "'void QReadWriteLockPrivate::release()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'qrwl_freelist'.")

  @staticmethod
  def waitConditionWait(*__, **_) -> Never:
    """
    Qt's 'QReadWriteLockPrivate::waitConditionWait': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QReadWriteLockPrivate.waitConditionWait' has no cute function "
        "yet. Qt's 'QReadWriteLockPrivate::waitConditionWait': a template: "
        "a pattern and no single function.")
