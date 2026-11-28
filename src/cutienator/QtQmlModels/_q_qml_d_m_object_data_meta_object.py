"""
QQmlDMObjectDataMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldmobjectdata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDMObjectDataMetaObject to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QAbstractDynamicMetaObject, QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDMObjectDataMetaObject(QAbstractDynamicMetaObject):
  """
  The cute side of Qt's QQmlDMObjectDataMetaObject: a plain Python object
  standing in front of one C++ QQmlDMObjectDataMetaObject.

  It is built on the cute 'QAbstractDynamicMetaObject', as Qt's
  QQmlDMObjectDataMetaObject is built on Qt's QAbstractDynamicMetaObject, and
  has everything that class has.

  C++ hands a QQmlDMObjectDataMetaObject around as a copy, so every C++
  QQmlDMObjectDataMetaObject behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlDMObjectDataMetaObject that has a ritual and
  that Python can call so far, 1 name in all: 'createProperty'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDMObjectDataMetaObject::~QQmlDMObjectDataMetaObject()': the
    destructor: Python removes its C++ QQmlDMObjectDataMetaObject by it, and
    has no other use for it.
  - Qt's 'int QQmlDMObjectDataMetaObject::metaCall(QObject *o,
    QMetaObject::Call call, int id, void **arguments)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'QQmlDMObjectData.

  What to expect
  --------------

  - The C++ QQmlDMObjectDataMetaObject is created at the first use, not by
    'QQmlDMObjectDataMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDMObjectDataMetaObject back gives a copy the
    ritual made for Python, in a new cute QQmlDMObjectDataMetaObject.
  - Each name of Qt's QQmlDMObjectDataMetaObject that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QQmlDMObjectDataMetaObject'

  #  A C++ QQmlDMObjectDataMetaObject Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDMObjectDataMetaObject'

  #  Qt's '~QQmlDMObjectDataMetaObject()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlDMObjectDataMetaObject behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQmlDMObjectDataMetaObjectD1Ev'

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
    Qt's
    'QQmlDMObjectDataMetaObject::QQmlDMObjectDataMetaObject(QQmlDMObjectData
    *data, VDMObjectDelegateDataType *type)': leans on
    'QQmlDMObjectData::modelDataChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlDMObjectDataMetaObject.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlDMObjectDataMetaObject::QQmlDMObjectDataMetaObject(QQmlDMObjec"
        "tData *data, VDMObjectDelegateDataType *type)': leans on "
        "'QQmlDMObjectData::modelDataChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def createProperty(self, name: Optional[str], a1: Optional[str]) -> int:
    """
    Calls Qt's 'int QQmlDMObjectDataMetaObject::createProperty(const char
    *name, const char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldmobjectdatametaobject.html#createProperty

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QQmlDMObjectDataMetaObject::createProperty(const char *name, const
    #      char *a1)
    return self.uglySide.call(
        'ritual_ZN26QQmlDMObjectDataMetaObject14createPropertyEPKcS1_',
        self._bytesOf(name), self._bytesOf(a1),
    )
