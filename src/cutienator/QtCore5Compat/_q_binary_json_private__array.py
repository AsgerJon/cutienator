"""
QBinaryJsonPrivate::Array binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::Array to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QBinaryJsonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class Array(QBinaryJsonPrivate.Base):
  """
  The cute side of Qt's QBinaryJsonPrivate::Array: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::Array.

  It is built on the cute 'QBinaryJsonPrivate::Base', as Qt's
  QBinaryJsonPrivate::Array is built on Qt's QBinaryJsonPrivate::Base, and
  has everything that class has.

  C++ hands a QBinaryJsonPrivate::Array around as a copy, so every C++
  QBinaryJsonPrivate::Array behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::Array that has a ritual and that
  Python can call so far, 1 name in all: 'at'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Value *QBinaryJsonPrivate::Array::at(uint i)': takes in Python what
    'const Value *QBinaryJsonPrivate::Array::at(uint i) const' takes.
  - Qt's 'QBinaryJsonPrivate::Array::~Array()': the destructor: Python
    removes its C++ QBinaryJsonPrivate::Array by it, and has no other use for
    it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'QBinaryJsonPrivate.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::Array is created at the first use, not by
    'QBinaryJsonPrivate::Array(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::Array back gives a copy the
    ritual made for Python, in a new cute QBinaryJsonPrivate::Array.
  - Each name of Qt's QBinaryJsonPrivate::Array that has no cute function
    yet, 'isValidHelper', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::Array'

  #  Qt's '~QBinaryJsonPrivate::Array()'. Naming it makes this a value class:
  #  Python owns every C++ QBinaryJsonPrivate::Array behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate5ArrayD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def at(self, i: int) -> Optional[QBinaryJsonPrivate.Value]:
    """
    Calls Qt's 'const Value *QBinaryJsonPrivate::Array::at(uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonprivate-array.html#at

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QBinaryJsonPrivate.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QBinaryJsonPrivate::Array::at(uint i) const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Array2atEj', i,
    )
    return QBinaryJsonPrivate.Value._cuteAt(address)

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

  @staticmethod
  def isValidHelper(*__, **_) -> Never:
    """
    Qt's 'bool QBinaryJsonPrivate::Array::isValidHelper(uint maxSize,
    IsValidStack &stack) const': leans on
    'QBinaryJsonPrivate::Value::isValidHelper(QBinaryJsonPrivate::Base
    const*, QVarLengthArray<QBinaryJsonPrivate::IsValidFrame, 16ll>&) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Array.isValidHelper' has no cute function yet. "
        "Qt's 'bool QBinaryJsonPrivate::Array::isValidHelper(uint maxSize, "
        "IsValidStack &stack) const': leans on "
        "'QBinaryJsonPrivate::Value::isValidHelper(QBinaryJsonPrivate::Base "
        "const*, QVarLengthArray<QBinaryJsonPrivate::IsValidFrame, 16ll>&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
