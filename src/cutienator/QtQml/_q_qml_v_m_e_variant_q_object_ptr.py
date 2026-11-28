"""
QQmlVMEVariantQObjectPtr binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlVMEVariantQObjectPtr to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQmlVMEMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlVMEMetaObject = WAIT['QQmlVMEMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlVMEVariantQObjectPtr(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlVMEVariantQObjectPtr: a plain Python object
  standing in front of one C++ QQmlVMEVariantQObjectPtr.

  C++ hands a QQmlVMEVariantQObjectPtr around as a copy, so every C++
  QQmlVMEVariantQObjectPtr behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlVMEVariantQObjectPtr that has a ritual and that
  Python can call so far, 1 name in all: 'setGuardedValue'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlVMEVariantQObjectPtr::~QQmlVMEVariantQObjectPtr()': the
    destructor: Python removes its C++ QQmlVMEVariantQObjectPtr by it, and
    has no other use for it.

  What has no ritual
  ------------------

  2 of the 4 functions Qt declares: 2 leans on 'QV4.

  What to expect
  --------------

  - The C++ QQmlVMEVariantQObjectPtr is created at the first use, not by
    'QQmlVMEVariantQObjectPtr(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlVMEVariantQObjectPtr back gives a copy the ritual
    made for Python, in a new cute QQmlVMEVariantQObjectPtr.
  - Each name of Qt's QQmlVMEVariantQObjectPtr that has no cute function yet,
    '__init__', 'objectDestroyedImpl', holds a function that raises
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
  __qt_class__ = 'QQmlVMEVariantQObjectPtr'

  #  Qt's '~QQmlVMEVariantQObjectPtr()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlVMEVariantQObjectPtr behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQmlVMEVariantQObjectPtrD1Ev'

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

  @overload(QObject, QQmlVMEMetaObject, int)
  @overload(QObject, NoneType, int)
  @overload(NoneType, QQmlVMEMetaObject, int)
  @overload(NoneType, NoneType, int)
  def setGuardedValue(
      self,
      obj: Optional[QObject],
      target: Optional[QQmlVMEMetaObject],
      index: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlVMEVariantQObjectPtr::setGuardedValue(QObject *obj,
    QQmlVMEMetaObject *target, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmevariantqobjectptr.html#setGuardedValue

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    target : Optional[QQmlVMEMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  void QQmlVMEVariantQObjectPtr::setGuardedValue(QObject *obj,
    #      QQmlVMEMetaObject *target, int index)
    self.uglySide.call(
        'ritual_ZN24QQmlVMEVariantQObjectPtr15setGuardedValueEP7QObjectP17Q'
        'QmlVMEMetaObjecti',
        self._addressOf(obj, 'QObject'), self._addressOf(target), index,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlVMEVariantQObjectPtr::QQmlVMEVariantQObjectPtr()': leans on
    'QV4::MemberData::static_vtbl', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlVMEVariantQObjectPtr.__init__' has no cute function yet. Qt's "
        "'QQmlVMEVariantQObjectPtr::QQmlVMEVariantQObjectPtr()': leans on "
        "'QV4::MemberData::static_vtbl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
  def objectDestroyedImpl(*__, **_) -> Never:
    """
    Qt's 'void QQmlVMEVariantQObjectPtr::objectDestroyedImpl(QQmlGuardImpl
    *guard)': leans on 'QV4::MemberData::static_vtbl', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlVMEVariantQObjectPtr.objectDestroyedImpl' has no cute "
        "function yet. Qt's 'void "
        "QQmlVMEVariantQObjectPtr::objectDestroyedImpl(QQmlGuardImpl "
        "*guard)': leans on 'QV4::MemberData::static_vtbl', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
