"""
QtPrivate::ExceptionStore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QException
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QException = WAIT['QException']


class ExceptionStore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::ExceptionStore: a plain Python object
  standing in front of one C++ QtPrivate::ExceptionStore.

  C++ hands a QtPrivate::ExceptionStore around as a copy, so every C++
  QtPrivate::ExceptionStore behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::ExceptionStore that has a ritual and that
  Python can call so far, 4 names in all: 'setException', 'hasException',
  'throwPossibleException', 'rethrowException'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QtPrivate::ExceptionStore::setException(std::exception_ptr
    e)': takes a type Python has no way to hand over yet.
  - Qt's 'std::exception_ptr QtPrivate::ExceptionStore::exception() const':
    gives a type Python has no way to take yet.
  - Qt's 'QtPrivate::ExceptionStore::~ExceptionStore()': the destructor:
    Python removes its C++ QtPrivate::ExceptionStore by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtPrivate::ExceptionStore is created at the first use, not by
    'QtPrivate::ExceptionStore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::ExceptionStore back gives a copy the
    ritual made for Python, in a new cute QtPrivate::ExceptionStore.
  - Each name of Qt's QtPrivate::ExceptionStore that has no cute function
    yet, 'exception', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QtPrivate::ExceptionStore'

  #  Qt's '~QtPrivate::ExceptionStore()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::ExceptionStore behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate14ExceptionStoreD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasException(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ExceptionStore::hasException() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-exceptionstore.html#hasException
    """
    #  bool QtPrivate::ExceptionStore::hasException() const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate14ExceptionStore12hasExceptionEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QException)
  def setException(self, e: QException) -> None:
    """
    Calls Qt's 'void QtPrivate::ExceptionStore::setException(const QException
    &e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-exceptionstore.html#setException

    Parameters
    ----------

    e : QException
      Passed on as a value: Qt reads the C++ QException, which stays Python's
      own.
    """
    #  void QtPrivate::ExceptionStore::setException(const QException &e)
    self.uglySide.call(
        'ritual_ZN9QtPrivate14ExceptionStore12setExceptionERK10QException',
        self._valueOf(e),
    )

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

  def throwPossibleException(self) -> None:
    """
    Calls Qt's 'void QtPrivate::ExceptionStore::throwPossibleException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-exceptionstore.html
    """
    #  void QtPrivate::ExceptionStore::throwPossibleException()
    self.uglySide.call(
        'ritual_ZN9QtPrivate14ExceptionStore22throwPossibleExceptionEv',
    )

  def rethrowException(self) -> None:
    """
    Calls Qt's 'void QtPrivate::ExceptionStore::rethrowException() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-exceptionstore.html#rethrowException
    """
    #  void QtPrivate::ExceptionStore::rethrowException() const
    self.uglySide.call(
        'ritual_ZNK9QtPrivate14ExceptionStore16rethrowExceptionEv',
    )

  @staticmethod
  def exception(*__, **_) -> Never:
    """
    Qt's 'std::exception_ptr QtPrivate::ExceptionStore::exception() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.ExceptionStore.exception' has no cute function yet. "
        "Qt's 'std::exception_ptr QtPrivate::ExceptionStore::exception() "
        "const': gives a type Python has no way to take yet.")
