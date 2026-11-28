"""
QQmlJS::MemoryPool binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsmemorypool_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlJS::MemoryPool to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class MemoryPool(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::MemoryPool: a plain Python object standing in
  front of one C++ QQmlJS::MemoryPool.

  What exists
  -----------

  Every function of Qt's QQmlJS::MemoryPool that has a ritual and that Python
  can call so far, 2 names in all: 'reset', 'newString'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::MemoryPool::~MemoryPool()': the destructor: Python never
    removes a C++ QQmlJS::MemoryPool.
  - Qt's 'void *QQmlJS::MemoryPool::allocate(size_t size)': gives 'void',
    which has no cute class yet.
  - Qt's 'void *QQmlJS::MemoryPool::allocate_helper(size_t size)': gives
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 4 forbidden; 2 a template.

  What to expect
  --------------

  - The C++ QQmlJS::MemoryPool is created at the first use, not by
    'QQmlJS::MemoryPool(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::MemoryPool.
  - Each name of Qt's QQmlJS::MemoryPool that has no cute function yet,
    'New', 'allocate', 'allocate_helper', holds a function that raises
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
  __qt_class__ = 'QQmlJS::MemoryPool'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::MemoryPool::MemoryPool()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-memorypool.html#MemoryPool
    """
    #  QQmlJS::MemoryPool::MemoryPool()
    self._noteCreation(MemoryPool, lambda: Rituals.call(
        'ritual_ZN6QQmlJS10MemoryPoolC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QQmlJS::MemoryPool::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-memorypool.html#reset
    """
    #  void QQmlJS::MemoryPool::reset()
    self.uglySide.call('ritual_ZN6QQmlJS10MemoryPool5resetEv')

  @overload(str)
  def newString(self, string: str) -> str:
    """
    Calls Qt's 'QStringView QQmlJS::MemoryPool::newString(QString string)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-memorypool.html#newString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QQmlJS::MemoryPool::newString(QString string)
    return self.uglySide.call(
        'ritual_ZN6QQmlJS10MemoryPool9newStringE7QString', string,
    )

  @staticmethod
  def New(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::MemoryPool::New': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlJS.MemoryPool.New' has no cute function yet. Qt's "
        "'QQmlJS::MemoryPool::New': a template: a pattern and no single "
        "function.")

  @staticmethod
  def allocate(*__, **_) -> Never:
    """
    Qt's 'void *QQmlJS::MemoryPool::allocate(size_t size)': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.MemoryPool.allocate' has no cute function yet. Qt's 'void "
        "*QQmlJS::MemoryPool::allocate(size_t size)': gives 'void', which "
        "has no cute class yet.")

  @staticmethod
  def allocate_helper(*__, **_) -> Never:
    """
    Qt's 'void *QQmlJS::MemoryPool::allocate_helper(size_t size)': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.MemoryPool.allocate_helper' has no cute function yet. Qt's "
        "'void *QQmlJS::MemoryPool::allocate_helper(size_t size)': gives "
        "'void', which has no cute class yet.")
