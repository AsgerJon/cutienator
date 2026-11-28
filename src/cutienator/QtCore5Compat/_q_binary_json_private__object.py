"""
QBinaryJsonPrivate::Object binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::Object to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QBinaryJsonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class Object(QBinaryJsonPrivate.Base):
  """
  The cute side of Qt's QBinaryJsonPrivate::Object: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::Object.

  It is built on the cute 'QBinaryJsonPrivate::Base', as Qt's
  QBinaryJsonPrivate::Object is built on Qt's QBinaryJsonPrivate::Base, and
  has everything that class has.

  C++ hands a QBinaryJsonPrivate::Object around as a copy, so every C++
  QBinaryJsonPrivate::Object behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::Object that has a ritual and
  that Python can call so far, 1 name in all: 'entryAt'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Entry *QBinaryJsonPrivate::Object::entryAt(uint i)': takes in
    Python what 'const Entry *QBinaryJsonPrivate::Object::entryAt(uint i)
    const' takes.
  - Qt's 'uint QBinaryJsonPrivate::Object::indexOf(QStringView key, bool
    *exists) const': takes a number to change where it is.
  - Qt's 'QBinaryJsonPrivate::Object::~Object()': the destructor: Python
    removes its C++ QBinaryJsonPrivate::Object by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QBinaryJsonPrivate.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::Object is created at the first use, not by
    'QBinaryJsonPrivate::Object(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::Object back gives a copy the
    ritual made for Python, in a new cute QBinaryJsonPrivate::Object.
  - Each name of Qt's QBinaryJsonPrivate::Object that has no cute function
    yet, 'indexOf', 'isValidHelper', holds a function that raises
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
  __qt_class__ = 'QBinaryJsonPrivate::Object'

  #  Qt's '~QBinaryJsonPrivate::Object()'. Naming it makes this a value
  #  class: Python owns every C++ QBinaryJsonPrivate::Object behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate6ObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def entryAt(self, i: int) -> Optional[QBinaryJsonPrivate.Entry]:
    """
    Calls Qt's 'const Entry *QBinaryJsonPrivate::Object::entryAt(uint i)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-object.html#entryAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QBinaryJsonPrivate.Entry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Entry *QBinaryJsonPrivate::Object::entryAt(uint i) const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate6Object7entryAtEj', i,
    )
    return QBinaryJsonPrivate.Entry._cuteAt(address)

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
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'uint QBinaryJsonPrivate::Object::indexOf(QStringView key, bool
    *exists) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Object.indexOf' has no cute function yet. Qt's "
        "'uint QBinaryJsonPrivate::Object::indexOf(QStringView key, bool "
        "*exists) const': takes a number to change where it is.")

  @staticmethod
  def isValidHelper(*__, **_) -> Never:
    """
    Qt's 'bool QBinaryJsonPrivate::Object::isValidHelper(uint maxSize,
    IsValidStack &stack) const': leans on
    'QBinaryJsonPrivate::Value::isValidHelper(QBinaryJsonPrivate::Base
    const*, QVarLengthArray<QBinaryJsonPrivate::IsValidFrame, 16ll>&) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBinaryJsonPrivate.Object.isValidHelper' has no cute function "
        "yet. Qt's 'bool QBinaryJsonPrivate::Object::isValidHelper(uint "
        "maxSize, IsValidStack &stack) const': leans on "
        "'QBinaryJsonPrivate::Value::isValidHelper(QBinaryJsonPrivate::Base "
        "const*, QVarLengthArray<QBinaryJsonPrivate::IsValidFrame, 16ll>&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
