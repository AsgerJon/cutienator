"""
QBinaryJsonObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjsonobject_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QBinaryJsonObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QBinaryJsonObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonObject: a plain Python object standing in
  front of one C++ QBinaryJsonObject.

  What exists
  -----------

  Every function of Qt's QBinaryJsonObject that has a ritual and that Python
  can call so far, 2 names in all: 'detach', 'compact'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBinaryJsonObject::~QBinaryJsonObject()': the destructor: Python
    never removes a C++ QBinaryJsonObject.
  - Qt's 'QBinaryJsonObject::QBinaryJsonObject(QBinaryJsonObject &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QBinaryJsonObject &QBinaryJsonObject::operator=(QBinaryJsonObject
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'char *QBinaryJsonObject::takeRawData(uint *size) const': takes a
    number to change where it is.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 forbidden; 2 leans on
  'QBinaryJsonPrivate.

  What to expect
  --------------

  - The C++ QBinaryJsonObject is created at the first use, not by
    'QBinaryJsonObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBinaryJsonObject.
  - Each name of Qt's QBinaryJsonObject that has no cute function yet,
    'fromJsonObject', 'insert', 'takeRawData', holds a function that raises
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
  __qt_class__ = 'QBinaryJsonObject'

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
    Notes what was given, for Qt's 'QBinaryJsonObject::QBinaryJsonObject()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonobject.html#QBinaryJsonObject
    """
    #  QBinaryJsonObject::QBinaryJsonObject()
    self._noteCreation(QBinaryJsonObject, lambda: Rituals.call(
        'ritual_ZN17QBinaryJsonObjectC1Ev',
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

  @overload()
  @overload(int)
  def detach(self, reserve: int = 0) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonObject::detach(uint reserve)'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonobject.html#detach

    Parameters
    ----------

    reserve : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QBinaryJsonObject::detach(uint reserve)
    return self.uglySide.call(
        'ritual_ZN17QBinaryJsonObject6detachEj', reserve,
    )

  def compact(self) -> None:
    """
    Calls Qt's 'void QBinaryJsonObject::compact()'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonobject.html#compact
    """
    #  void QBinaryJsonObject::compact()
    self.uglySide.call('ritual_ZN17QBinaryJsonObject7compactEv')

  @staticmethod
  def fromJsonObject(*__, **_) -> Never:
    """
    Qt's 'QBinaryJsonObject QBinaryJsonObject::fromJsonObject(const
    QJsonObject &object)': leans on
    'QBinaryJsonPrivate::Value::copyData(QBinaryJsonValue const&, char*,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBinaryJsonObject.fromJsonObject' has no cute function yet. Qt's "
        "'QBinaryJsonObject QBinaryJsonObject::fromJsonObject(const "
        "QJsonObject &object)': leans on "
        "'QBinaryJsonPrivate::Value::copyData(QBinaryJsonValue const&, "
        "char*, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def insert(*__, **_) -> Never:
    """
    Qt's 'void QBinaryJsonObject::insert(const QString &key, const
    QBinaryJsonValue &value)': leans on
    'QBinaryJsonPrivate::Value::copyData(QBinaryJsonValue const&, char*,
    bool)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBinaryJsonObject.insert' has no cute function yet. Qt's 'void "
        "QBinaryJsonObject::insert(const QString &key, const "
        "QBinaryJsonValue &value)': leans on "
        "'QBinaryJsonPrivate::Value::copyData(QBinaryJsonValue const&, "
        "char*, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def takeRawData(*__, **_) -> Never:
    """
    Qt's 'char *QBinaryJsonObject::takeRawData(uint *size) const': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QBinaryJsonObject.takeRawData' has no cute function yet. Qt's "
        "'char *QBinaryJsonObject::takeRawData(uint *size) const': takes a "
        "number to change where it is.")
