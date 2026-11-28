"""
QDBusMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/6.12.0/QtDBus/private/qdbusmetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QDBusMetaObject to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QDBusMetaObject(QMetaObject):
  """
  The cute side of Qt's QDBusMetaObject: a plain Python object standing in
  front of one C++ QDBusMetaObject.

  It is built on the cute 'QMetaObject', as Qt's QDBusMetaObject is built on
  Qt's QMetaObject, and has everything that class has.

  C++ hands a QDBusMetaObject around as a copy, so every C++ QDBusMetaObject
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusMetaObject that has a ritual and that Python
  can call so far, 1 name in all: 'propertyMetaType'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusMetaObject *QDBusMetaObject::createMetaObject(const QString
    &interface, const QString &xml, QHash<QString, QDBusMetaObject *> &map,
    QDBusError &error)': takes a type Python has no way to hand over yet.
  - Qt's 'QDBusMetaObject::~QDBusMetaObject()': the destructor: Python
    removes its C++ QDBusMetaObject by it, and has no other use for it.
  - Qt's 'const int *QDBusMetaObject::inputTypesForMethod(int id) const':
    gives 'int', which has no cute class yet.
  - Qt's 'const int *QDBusMetaObject::outputTypesForMethod(int id) const':
    gives 'int', which has no cute class yet.

  What to expect
  --------------

  - The C++ QDBusMetaObject is created at the first use, not by
    'QDBusMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusMetaObject back gives a copy the ritual made for
    Python, in a new cute QDBusMetaObject.
  - Each name of Qt's QDBusMetaObject that has no cute function yet,
    'createMetaObject', 'inputTypesForMethod', 'outputTypesForMethod', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusMetaObject'

  #  Qt's '~QDBusMetaObject()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusMetaObject behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QDBusMetaObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def propertyMetaType(self, id: int) -> int:
    """
    Calls Qt's 'int QDBusMetaObject::propertyMetaType(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmetaobject.html#propertyMetaType

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  int QDBusMetaObject::propertyMetaType(int id) const
    return self.uglySide.call(
        'ritual_ZNK15QDBusMetaObject16propertyMetaTypeEi', id,
    )

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
    Notes what was given, for Qt's 'QDBusMetaObject::QDBusMetaObject()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusmetaobject.html#QDBusMetaObject
    """
    #  QDBusMetaObject::QDBusMetaObject()
    self._noteCreation(QDBusMetaObject, lambda: Rituals.call(
        'ritual_ZN15QDBusMetaObjectC1Ev',
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

  @staticmethod
  def createMetaObject(*__, **_) -> Never:
    """
    Qt's 'QDBusMetaObject *QDBusMetaObject::createMetaObject(const QString
    &interface, const QString &xml, QHash<QString, QDBusMetaObject *> &map,
    QDBusError &error)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusMetaObject.createMetaObject' has no cute function yet. Qt's "
        "'QDBusMetaObject *QDBusMetaObject::createMetaObject(const QString "
        "&interface, const QString &xml, QHash<QString, QDBusMetaObject *> "
        "&map, QDBusError &error)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def inputTypesForMethod(*__, **_) -> Never:
    """
    Qt's 'const int *QDBusMetaObject::inputTypesForMethod(int id) const':
    gives 'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDBusMetaObject.inputTypesForMethod' has no cute function yet. "
        "Qt's 'const int *QDBusMetaObject::inputTypesForMethod(int id) "
        "const': gives 'int', which has no cute class yet.")

  @staticmethod
  def outputTypesForMethod(*__, **_) -> Never:
    """
    Qt's 'const int *QDBusMetaObject::outputTypesForMethod(int id) const':
    gives 'int', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QDBusMetaObject.outputTypesForMethod' has no cute function yet. "
        "Qt's 'const int *QDBusMetaObject::outputTypesForMethod(int id) "
        "const': gives 'int', which has no cute class yet.")
