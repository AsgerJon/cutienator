"""
QtPrivate::QPropertyAdaptorSlotObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtPrivate::QPropertyAdaptorSlotObject to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QUntypedPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaProperty, QObject


class QPropertyAdaptorSlotObject(QUntypedPropertyData):
  """
  The cute side of Qt's QtPrivate::QPropertyAdaptorSlotObject: a plain Python
  object standing in front of one C++ QtPrivate::QPropertyAdaptorSlotObject.

  It is built on the cute 'QUntypedPropertyData', as Qt's
  QtPrivate::QPropertyAdaptorSlotObject is built on Qt's
  QUntypedPropertyData, and has everything that class has. Qt's
  QtPrivate::QPropertyAdaptorSlotObject is built on Qt's
  QtPrivate::QSlotObjectBase as well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QtPrivate::QPropertyAdaptorSlotObject that has a
  ritual and that Python can call so far, 2 names in all: 'object',
  'metaProperty'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPropertyBindingData
    &QtPrivate::QPropertyAdaptorSlotObject::bindingData() const': gives a
    type Python has no way to take yet.
  - Qt's 'QPropertyBindingData
    &QtPrivate::QPropertyAdaptorSlotObject::bindingData()': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 2 leans on 'QtPrivate; 1 cannot be called
  and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QtPrivate::QPropertyAdaptorSlotObject is created at the first
    use, not by 'QtPrivate::QPropertyAdaptorSlotObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::QPropertyAdaptorSlotObject.
  - Each name of Qt's QtPrivate::QPropertyAdaptorSlotObject that has no cute
    function yet, '__init__', 'bindingData', 'cast', 'impl', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QPropertyAdaptorSlotObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QtPrivate::QPropertyAdaptorSlotObject::object()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertyadaptorslotobject.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QtPrivate::QPropertyAdaptorSlotObject::object() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate26QPropertyAdaptorSlotObject6objectEv',
    )
    from . import QObject
    return QObject._cuteAt(address)

  def metaProperty(self) -> QMetaProperty:
    """
    Calls Qt's 'const QMetaProperty
    &QtPrivate::QPropertyAdaptorSlotObject::metaProperty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qpropertyadaptorslotobject.html

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  const QMetaProperty
    #      &QtPrivate::QPropertyAdaptorSlotObject::metaProperty() const
    address = self.uglySide.call(
        'ritual_ZNK9QtPrivate26QPropertyAdaptorSlotObject12metaPropertyEv',
    )
    from . import QMetaProperty
    return QMetaProperty._cuteOwning(address)

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
    Qt's 'QtPrivate::QPropertyAdaptorSlotObject::QPropertyAdaptorSlotObject(
    QObject *o, const QMetaProperty &p)': leans on
    'QtPrivate::QPropertyAdaptorSlotObject::impl(int,
    QtPrivate::QSlotObjectBase*, QObject*, void**, bool*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyAdaptorSlotObject.__init__' has no cute "
        "function yet. Qt's "
        "'QtPrivate::QPropertyAdaptorSlotObject::QPropertyAdaptorSlotObject("
        "QObject *o, const QMetaProperty &p)': leans on "
        "'QtPrivate::QPropertyAdaptorSlotObject::impl(int, "
        "QtPrivate::QSlotObjectBase*, QObject*, void**, bool*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
  def bindingData(*__, **_) -> Never:
    """
    - Qt's 'const QPropertyBindingData
      &QtPrivate::QPropertyAdaptorSlotObject::bindingData() const': gives a
      type Python has no way to take yet.
    - Qt's 'QPropertyBindingData
      &QtPrivate::QPropertyAdaptorSlotObject::bindingData()': gives a type
      Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyAdaptorSlotObject.bindingData' has no cute "
        "function yet. Qt's 'const QPropertyBindingData "
        "&QtPrivate::QPropertyAdaptorSlotObject::bindingData() const': "
        "gives a type Python has no way to take yet. Qt's "
        "'QPropertyBindingData "
        "&QtPrivate::QPropertyAdaptorSlotObject::bindingData()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def cast(*__, **_) -> Never:
    """
    Qt's 'QPropertyAdaptorSlotObject
    *QtPrivate::QPropertyAdaptorSlotObject::cast(QSlotObjectBase *ptr, int
    propertyIndex)': leans on
    'QtPrivate::QPropertyAdaptorSlotObject::impl(int,
    QtPrivate::QSlotObjectBase*, QObject*, void**, bool*)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyAdaptorSlotObject.cast' has no cute function "
        "yet. Qt's 'QPropertyAdaptorSlotObject "
        "*QtPrivate::QPropertyAdaptorSlotObject::cast(QSlotObjectBase *ptr, "
        "int propertyIndex)': leans on "
        "'QtPrivate::QPropertyAdaptorSlotObject::impl(int, "
        "QtPrivate::QSlotObjectBase*, QObject*, void**, bool*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def impl(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QPropertyAdaptorSlotObject::impl(int which,
    QSlotObjectBase *this_, QObject *r, void **a, bool *ret)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QtPrivate.QPropertyAdaptorSlotObject.impl' has no cute function "
        "yet. Qt's 'void QtPrivate::QPropertyAdaptorSlotObject::impl(int "
        "which, QSlotObjectBase *this_, QObject *r, void **a, bool *ret)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
