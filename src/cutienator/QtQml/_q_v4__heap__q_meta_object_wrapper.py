"""
QV4::Heap::QMetaObjectWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4qmetaobjectwrapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::Heap::QMetaObjectWrapper to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaObjectWrapper(QV4.Heap.FunctionObject):
  """
  The cute side of Qt's QV4::Heap::QMetaObjectWrapper: a plain Python object
  standing in front of one C++ QV4::Heap::QMetaObjectWrapper.

  It is built on the cute 'QV4::Heap::FunctionObject', as Qt's
  QV4::Heap::QMetaObjectWrapper is built on Qt's QV4::Heap::FunctionObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QMetaObjectWrapper that has a ritual and
  that Python can call so far, 4 names in all: 'init', 'destroy',
  'metaObject', 'metaType'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 leans on 'QQmlPropertyData.

  What to expect
  --------------

  - The C++ QV4::Heap::QMetaObjectWrapper is created at the first use, not by
    'QV4::Heap::QMetaObjectWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QMetaObjectWrapper.
  - Each name of Qt's QV4::Heap::QMetaObjectWrapper that has no cute function
    yet, 'createConstructors', 'ensureConstructorsCache', holds a function
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
  __qt_class__ = 'QV4::Heap::QMetaObjectWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QV4::Heap::QMetaObjectWrapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmetaobjectwrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::Heap::QMetaObjectWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap18QMetaObjectWrapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::QMetaObjectWrapper::metaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmetaobjectwrapper.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::QMetaObjectWrapper::metaType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap18QMetaObjectWrapper8metaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

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

  @overload(QMetaObject)
  @overload(NoneType)
  def init(self, metaObject: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QV4::Heap::QMetaObjectWrapper::init(const QMetaObject
    *metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmetaobjectwrapper.html#init

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QMetaObjectWrapper::init(const QMetaObject
    #      *metaObject)
    self.uglySide.call(
        'ritual_ZN3QV44Heap18QMetaObjectWrapper4initEPK11QMetaObject',
        self._addressOf(metaObject, 'QMetaObject'),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QMetaObjectWrapper::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmetaobjectwrapper.html#destroy
    """
    #  void QV4::Heap::QMetaObjectWrapper::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap18QMetaObjectWrapper7destroyEv')

  @staticmethod
  def createConstructors(*__, **_) -> Never:
    """
    Qt's 'const QQmlPropertyData
    *QV4::Heap::QMetaObjectWrapper::createConstructors(const QMetaObject
    *metaObject, QMetaType metaType)': leans on
    'QQmlPropertyData::load(QMetaMethod const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.QMetaObjectWrapper.createConstructors' has no cute "
        "function yet. Qt's 'const QQmlPropertyData "
        "*QV4::Heap::QMetaObjectWrapper::createConstructors(const "
        "QMetaObject *metaObject, QMetaType metaType)': leans on "
        "'QQmlPropertyData::load(QMetaMethod const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def ensureConstructorsCache(*__, **_) -> Never:
    """
    Qt's 'const QQmlPropertyData
    *QV4::Heap::QMetaObjectWrapper::ensureConstructorsCache(const QMetaObject
    *metaObject, QMetaType metaType)': leans on
    'QQmlPropertyData::load(QMetaMethod const&)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Heap.QMetaObjectWrapper.ensureConstructorsCache' has no cute "
        "function yet. Qt's 'const QQmlPropertyData "
        "*QV4::Heap::QMetaObjectWrapper::ensureConstructorsCache(const "
        "QMetaObject *metaObject, QMetaType metaType)': leans on "
        "'QQmlPropertyData::load(QMetaMethod const&)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
