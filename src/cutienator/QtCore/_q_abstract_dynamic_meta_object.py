"""
QAbstractDynamicMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QAbstractDynamicMetaObject to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QDynamicMetaObjectData, QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractDynamicMetaObject(QDynamicMetaObjectData, QMetaObject):
  """
  The cute side of Qt's QAbstractDynamicMetaObject: a plain Python object
  standing in front of one C++ QAbstractDynamicMetaObject.

  It is built on the cute 'QDynamicMetaObjectData', as Qt's
  QAbstractDynamicMetaObject is built on Qt's QDynamicMetaObjectData, and has
  everything that class has. It is built on the cute 'QMetaObject' as well,
  as Qt's QAbstractDynamicMetaObject is built on Qt's QMetaObject too, and
  has everything that class has.

  C++ hands a QAbstractDynamicMetaObject around as a copy, so every C++
  QAbstractDynamicMetaObject behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QAbstractDynamicMetaObject that has a ritual and
  that Python can call so far, 2 names in all: 'toDynamicMetaObject',
  'createProperty'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractDynamicMetaObject::~QAbstractDynamicMetaObject()': the
    destructor: Python removes its C++ QAbstractDynamicMetaObject by it, and
    has no other use for it.
  - Qt's 'int QAbstractDynamicMetaObject::metaCall(QObject *a0,
    QMetaObject::Call c, int _id, void **a)': takes a type Python has no way
    to hand over yet.
  - Qt's 'int QAbstractDynamicMetaObject::metaCall(QMetaObject::Call a0, int
    _id, void **a2)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QAbstractDynamicMetaObject is created at the first use, not by
    'QAbstractDynamicMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAbstractDynamicMetaObject back gives a copy the
    ritual made for Python, in a new cute QAbstractDynamicMetaObject.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractDynamicMetaObject'

  #  Qt's QAbstractDynamicMetaObject is built on more than one class. The
  #  part of a C++ QAbstractDynamicMetaObject that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QMetaObject': 'ritual_cast_QAbstractDynamicMetaObject_QMetaObject',
  }

  #  A C++ QAbstractDynamicMetaObject Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractDynamicMetaObject'

  #  The functions Qt calls itself that QAbstractDynamicMetaObject is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createProperty': (
          'int QAbstractDynamicMetaObject::createProperty(const char *, '
          'const char *)',
      ),
      'metaCall': (
          'int QAbstractDynamicMetaObject::metaCall(QMetaObject::Call, '
          'int, void **)',
      ),
  }

  #  Qt's '~QAbstractDynamicMetaObject()'. Naming it makes this a value
  #  class: Python owns every C++ QAbstractDynamicMetaObject behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QAbstractDynamicMetaObjectD1Ev'

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

  @overload(QObject)
  @overload(NoneType)
  def toDynamicMetaObject(
      self,
      a0: Optional[QObject],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'QMetaObject
    *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdynamicmetaobject.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetaObject *QAbstractDynamicMetaObject::toDynamicMetaObject(QObject
    #      *a0)
    ritual = (
        'ritual_ZN26QAbstractDynamicMetaObject19toDynamicMetaObjectEP7QObje'
        'ct')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QAbstractDynamicMetaObject19toDynamicMetaObjectEP'
          '7QObject')
    address = self._callAs(
        'QAbstractDynamicMetaObject', ritual, self._addressOf(a0, 'QObject'),
    )
    return QMetaObject._cuteAt(address)

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def createProperty(self, a0: Optional[str], a1: Optional[str]) -> int:
    """
    Calls Qt's 'int QAbstractDynamicMetaObject::createProperty(const char
    *a0, const char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdynamicmetaobject.html#createProperty

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QAbstractDynamicMetaObject::createProperty(const char *a0, const
    #      char *a1)
    return self._callAs(
        'QAbstractDynamicMetaObject',
        'ritual_ZN26QAbstractDynamicMetaObject14createPropertyEPKcS1_',
        self._bytesOf(a0), self._bytesOf(a1),
    )
