"""
QQmlDelegateModelPartsMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDelegateModelPartsMetaObject to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtQml import QQmlOpenMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant


class QQmlDelegateModelPartsMetaObject(QQmlOpenMetaObject):
  """
  The cute side of Qt's QQmlDelegateModelPartsMetaObject: a plain Python
  object standing in front of one C++ QQmlDelegateModelPartsMetaObject.

  It is built on the cute 'QQmlOpenMetaObject', as Qt's
  QQmlDelegateModelPartsMetaObject is built on Qt's QQmlOpenMetaObject, and
  has everything that class has.

  C++ hands a QQmlDelegateModelPartsMetaObject around as a copy, so every C++
  QQmlDelegateModelPartsMetaObject behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlDelegateModelPartsMetaObject that has a ritual
  and that Python can call so far, 1 name in all: 'initialValue'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlDelegateModelPartsMetaObject::propertyCreated(int a0,
    QMetaPropertyBuilder &a1)': takes a type Python has no way to hand over
    yet.
  - Qt's
    'QQmlDelegateModelPartsMetaObject::~QQmlDelegateModelPartsMetaObject()':
    the destructor: Python removes its C++ QQmlDelegateModelPartsMetaObject
    by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'vtable for QQmlPartsModel',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QQmlDelegateModelPartsMetaObject is created at the first use, not
    by 'QQmlDelegateModelPartsMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDelegateModelPartsMetaObject back gives a copy
    the ritual made for Python, in a new cute
    QQmlDelegateModelPartsMetaObject.
  - Each name of Qt's QQmlDelegateModelPartsMetaObject that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QQmlDelegateModelPartsMetaObject'

  #  A C++ QQmlDelegateModelPartsMetaObject Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDelegateModelPartsMetaObject'

  #  Qt's '~QQmlDelegateModelPartsMetaObject()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlDelegateModelPartsMetaObject behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN32QQmlDelegateModelPartsMetaObjectD1Ev'

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
    Qt's 'QQmlDelegateModelPartsMetaObject::QQmlDelegateModelPartsMetaObject(
    QObject *parent)': leans on 'vtable for QQmlPartsModel', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQmlDelegateModelPartsMetaObject.__init__' has no cute function "
        "yet. Qt's "
        "'QQmlDelegateModelPartsMetaObject::QQmlDelegateModelPartsMetaObject"
        "(QObject *parent)': leans on 'vtable for QQmlPartsModel', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  @overload(int)
  def initialValue(self, a0: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDelegateModelPartsMetaObject::initialValue(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldelegatemodelpartsmetaobject.html#initialValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDelegateModelPartsMetaObject::initialValue(int a0)
    address = self.uglySide.call(
        'ritual_ZN32QQmlDelegateModelPartsMetaObject12initialValueEi', a0,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)
