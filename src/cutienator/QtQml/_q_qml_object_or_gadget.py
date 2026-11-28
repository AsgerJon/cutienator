"""
QQmlObjectOrGadget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlobjectorgadget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlObjectOrGadget to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QQmlMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlObjectOrGadget(QQmlMetaObject):
  """
  The cute side of Qt's QQmlObjectOrGadget: a plain Python object standing in
  front of one C++ QQmlObjectOrGadget.

  It is built on the cute 'QQmlMetaObject', as Qt's QQmlObjectOrGadget is
  built on Qt's QQmlMetaObject, and has everything that class has.

  C++ hands a QQmlObjectOrGadget around as a copy, so every C++
  QQmlObjectOrGadget behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlObjectOrGadget that has a ritual and that Python
  can call so far, 2 names in all: 'isNull', 'qObject'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlObjectOrGadget::QQmlObjectOrGadget(const QMetaObject
    *metaObject, void *gadget)': names 'void', which has no cute class yet.
  - Qt's 'void QQmlObjectOrGadget::metacall(QMetaObject::Call type, int
    index, void **argv) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlObjectOrGadget::~QQmlObjectOrGadget()': the destructor: Python
    removes its C++ QQmlObjectOrGadget by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlObjectOrGadget is created at the first use, not by
    'QQmlObjectOrGadget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlObjectOrGadget back gives a copy the ritual made
    for Python, in a new cute QQmlObjectOrGadget.
  - Each name of Qt's QQmlObjectOrGadget that has no cute function yet,
    'metacall', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQmlObjectOrGadget'

  #  Qt's '~QQmlObjectOrGadget()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlObjectOrGadget behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlObjectOrGadgetD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlObjectOrGadget::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectorgadget.html#isNull
    """
    #  bool QQmlObjectOrGadget::isNull() const
    return self.uglySide.call('ritual_ZNK18QQmlObjectOrGadget6isNullEv')

  def qObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlObjectOrGadget::qObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlobjectorgadget.html#qObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlObjectOrGadget::qObject() const
    address = self.uglySide.call('ritual_ZNK18QQmlObjectOrGadget7qObjectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, obj: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlObjectOrGadget::QQmlObjectOrGadget(QObject *obj)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectorgadget.html#QQmlObjectOrGadget

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlObjectOrGadget::QQmlObjectOrGadget(QObject *obj)
    self._noteCreation(QQmlObjectOrGadget, lambda: Rituals.call(
        'ritual_ZN18QQmlObjectOrGadgetC1EP7QObject',
        self._addressOf(obj, 'QObject'),
    ))

  @overload(QMetaObject)
  def __init__(self, metaObject: Optional[QMetaObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlObjectOrGadget::QQmlObjectOrGadget(const QMetaObject *metaObject)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlobjectorgadget.html#QQmlObjectOrGadget

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlObjectOrGadget::QQmlObjectOrGadget(const QMetaObject *metaObject)
    self._noteCreation(QQmlObjectOrGadget, lambda: Rituals.call(
        'ritual_ZN18QQmlObjectOrGadgetC1EPK11QMetaObject',
        self._addressOf(metaObject, 'QMetaObject'),
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
  def metacall(*__, **_) -> Never:
    """
    Qt's 'void QQmlObjectOrGadget::metacall(QMetaObject::Call type, int
    index, void **argv) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlObjectOrGadget.metacall' has no cute function yet. Qt's 'void "
        "QQmlObjectOrGadget::metacall(QMetaObject::Call type, int index, "
        "void **argv) const': takes a type Python has no way to hand over "
        "yet.")
