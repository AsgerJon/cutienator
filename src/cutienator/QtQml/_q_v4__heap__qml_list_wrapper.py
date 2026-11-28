"""
QV4::Heap::QmlListWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmllistwrapper_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::QmlListWrapper to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlListWrapper(QV4.Heap.Object):
  """
  The cute side of Qt's QV4::Heap::QmlListWrapper: a plain Python object
  standing in front of one C++ QV4::Heap::QmlListWrapper.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::QmlListWrapper is built on Qt's QV4::Heap::Object, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QmlListWrapper that has a ritual and that
  Python can call so far, 5 names in all: 'init', 'destroy', 'object',
  'propertyType', 'elementType'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Heap::QmlListWrapper::init(QObject *object, const
    QQmlListProperty<QObject> &list, QMetaType propertyType)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QQmlListProperty<QObject>
    *QV4::Heap::QmlListWrapper::property() const': gives
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QQmlListProperty<QObject> *QV4::Heap::QmlListWrapper::property()':
    gives 'QQmlListProperty<QObject>', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::Heap::QmlListWrapper is created at the first use, not by
    'QV4::Heap::QmlListWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QmlListWrapper.
  - Each name of Qt's QV4::Heap::QmlListWrapper that has no cute function
    yet, 'property', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QV4::Heap::QmlListWrapper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::Heap::QmlListWrapper::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmllistwrapper.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::Heap::QmlListWrapper::object() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap14QmlListWrapper6objectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def propertyType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::QmlListWrapper::propertyType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmllistwrapper.html#propertyType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::QmlListWrapper::propertyType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap14QmlListWrapper12propertyTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def elementType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::QmlListWrapper::elementType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmllistwrapper.html#elementType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::QmlListWrapper::elementType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap14QmlListWrapper11elementTypeEv',
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

  @overload(QObject, int, QMetaType)
  @overload(NoneType, int, QMetaType)
  def init(
      self,
      object: Optional[QObject],
      propertyId: int,
      propertyType: QMetaType,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::QmlListWrapper::init(QObject *object, int
    propertyId, QMetaType propertyType)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-qmllistwrapper.html#init

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyId : int
      Passed on as it is.

    propertyType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QV4::Heap::QmlListWrapper::init(QObject *object, int propertyId,
    #      QMetaType propertyType)
    self.uglySide.call(
        'ritual_ZN3QV44Heap14QmlListWrapper4initEP7QObjecti9QMetaType',
        self._addressOf(object, 'QObject'), propertyId,
        self._valueOf(propertyType),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QmlListWrapper::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qmllistwrapper.html#destroy
    """
    #  void QV4::Heap::QmlListWrapper::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap14QmlListWrapper7destroyEv')

  @staticmethod
  def property(*__, **_) -> Never:
    """
    - Qt's 'const QQmlListProperty<QObject>
      *QV4::Heap::QmlListWrapper::property() const': gives
      'QQmlListProperty<QObject>', which has no cute class yet.
    - Qt's 'QQmlListProperty<QObject>
      *QV4::Heap::QmlListWrapper::property()': gives
      'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.QmlListWrapper.property' has no cute function yet. Qt's "
        "'const QQmlListProperty<QObject> "
        "*QV4::Heap::QmlListWrapper::property() const': gives "
        "'QQmlListProperty<QObject>', which has no cute class yet. Qt's "
        "'QQmlListProperty<QObject> "
        "*QV4::Heap::QmlListWrapper::property()': gives "
        "'QQmlListProperty<QObject>', which has no cute class yet.")
