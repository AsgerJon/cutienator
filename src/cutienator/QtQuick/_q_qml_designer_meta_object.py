"""
QQmlDesignerMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qqmldesignermetaobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDesignerMetaObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QDynamicMetaObjectData, QMetaObject
from ..QtQml import QQmlOpenMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDesignerMetaObject(QQmlOpenMetaObject):
  """
  The cute side of Qt's QQmlDesignerMetaObject: a plain Python object
  standing in front of one C++ QQmlDesignerMetaObject.

  It is built on the cute 'QQmlOpenMetaObject', as Qt's
  QQmlDesignerMetaObject is built on Qt's QQmlOpenMetaObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlDesignerMetaObject that has a ritual and that
  Python can call so far, 8 names in all: 'createNewDynamicProperty',
  'createProperty', 'propertyWriteValue', 'myObject',
  'dynamicMetaObjectParent', 'propertyOffset', 'count', 'name'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QQmlDesignerMetaObject::metaCall(QObject *o, QMetaObject::Call
    _c, int _id, void **_a)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QQmlPropertyCache::Ptr QQmlDesignerMetaObject::cache() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  8 of the 18 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQmlDesignerMetaObject is created at the first use, not by
    'QQmlDesignerMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDesignerMetaObject.
  - Each name of Qt's QQmlDesignerMetaObject that has no cute function yet,
    '__init__', 'cache', 'getNodeInstanceMetaObject', 'init',
    'notifyPropertyChange', 'openMetaCall',
    'registerNotifyPropertyChangeCallBack', holds a function that raises
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
  __qt_class__ = 'QQmlDesignerMetaObject'

  #  A C++ QQmlDesignerMetaObject Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDesignerMetaObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def myObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlDesignerMetaObject::myObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldesignermetaobject.html#myObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlDesignerMetaObject::myObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlDesignerMetaObject8myObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def dynamicMetaObjectParent(self) -> Optional[QDynamicMetaObjectData]:
    """
    Calls Qt's 'QDynamicMetaObjectData
    *QQmlDesignerMetaObject::dynamicMetaObjectParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldesignermetaobject.html

    Returns
    -------

    Optional[QDynamicMetaObjectData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDynamicMetaObjectData
    #      *QQmlDesignerMetaObject::dynamicMetaObjectParent() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlDesignerMetaObject23dynamicMetaObjectParentEv',
    )
    return QDynamicMetaObjectData._cuteAt(address)

  def propertyOffset(self) -> int:
    """
    Calls Qt's 'int QQmlDesignerMetaObject::propertyOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldesignermetaobject.html#propertyOffset
    """
    #  int QQmlDesignerMetaObject::propertyOffset() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlDesignerMetaObject14propertyOffsetEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlDesignerMetaObject::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldesignermetaobject.html#count
    """
    #  int QQmlDesignerMetaObject::count() const
    return self.uglySide.call('ritual_ZNK22QQmlDesignerMetaObject5countEv')

  @overload(int)
  def name(self, a0: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlDesignerMetaObject::name(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldesignermetaobject.html#name

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlDesignerMetaObject::name(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlDesignerMetaObject4nameEi', a0,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
    Qt's 'QQmlDesignerMetaObject::QQmlDesignerMetaObject(QObject *object,
    QQmlEngine *engine)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: allocation of
    incomplete type 'MetaPropertyData'.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.__init__' has no cute function yet. Qt's "
        "'QQmlDesignerMetaObject::QQmlDesignerMetaObject(QObject *object, "
        "QQmlEngine *engine)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: "
        "allocation of incomplete type 'MetaPropertyData'.")

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

  @overload(str)
  def createNewDynamicProperty(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlDesignerMetaObject::createNewDynamicProperty(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldesignermetaobject.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDesignerMetaObject::createNewDynamicProperty(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN22QQmlDesignerMetaObject24createNewDynamicPropertyERK7QSt'
        'ring',
        name,
    )

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def createProperty(
      self,
      name: Optional[str],
      passAlong: Optional[str],
  ) -> int:
    """
    Calls Qt's 'int QQmlDesignerMetaObject::createProperty(const char *name,
    const char *passAlong)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldesignermetaobject.html#createProperty

    Parameters
    ----------

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    passAlong : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QQmlDesignerMetaObject::createProperty(const char *name, const
    #      char *passAlong)
    return self.uglySide.call(
        'ritual_ZN22QQmlDesignerMetaObject14createPropertyEPKcS1_',
        self._bytesOf(name), self._bytesOf(passAlong),
    )

  @overload(int, QVariant)
  def propertyWriteValue(self, a0: int, a1: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlDesignerMetaObject::propertyWriteValue(int a0,
    const QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldesignermetaobject.html#propertyWriteValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlDesignerMetaObject::propertyWriteValue(int a0, const
    #      QVariant &a1)
    ritual = (
        'ritual_ZN22QQmlDesignerMetaObject18propertyWriteValueEiRK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQmlDesignerMetaObject18propertyWriteValueEiRK8QV'
          'ariant')
    address = self.uglySide.call(ritual, a0, self._valueOf(a1))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  def cache(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::Ptr QQmlDesignerMetaObject::cache() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.cache' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlDesignerMetaObject::cache() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def getNodeInstanceMetaObject(*__, **_) -> Never:
    """
    Qt's 'QQmlDesignerMetaObject
    *QQmlDesignerMetaObject::getNodeInstanceMetaObject(QObject *object,
    QQmlEngine *engine)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'nodeInstanceMetaObjectList'; did you mean
    'getNodeInstanceMetaObject'?.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.getNodeInstanceMetaObject' has no cute "
        "function yet. Qt's 'QQmlDesignerMetaObject "
        "*QQmlDesignerMetaObject::getNodeInstanceMetaObject(QObject "
        "*object, QQmlEngine *engine)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'nodeInstanceMetaObjectList'; did you "
        "mean 'getNodeInstanceMetaObject'?.")

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QQmlDesignerMetaObject::init(QObject *a0)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'nodeInstanceMetaObjectList'; did
    you mean 'getNodeInstanceMetaObject'?.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.init' has no cute function yet. Qt's 'void "
        "QQmlDesignerMetaObject::init(QObject *a0)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'nodeInstanceMetaObjectList'; did you mean "
        "'getNodeInstanceMetaObject'?.")

  @staticmethod
  def notifyPropertyChange(*__, **_) -> Never:
    """
    Qt's 'void QQmlDesignerMetaObject::notifyPropertyChange(int id)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'notifyPropertyChangeCallBack'; did you mean
    'registerNotifyPropertyChangeCallBack'?.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.notifyPropertyChange' has no cute function "
        "yet. Qt's 'void QQmlDesignerMetaObject::notifyPropertyChange(int "
        "id)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'notifyPropertyChangeCallBack'; did you mean "
        "'registerNotifyPropertyChangeCallBack'?.")

  @staticmethod
  def openMetaCall(*__, **_) -> Never:
    """
    Qt's 'int QQmlDesignerMetaObject::openMetaCall(QObject *o,
    QMetaObject::Call _c, int _id, void **_a)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'MetaPropertyData'.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.openMetaCall' has no cute function yet. "
        "Qt's 'int QQmlDesignerMetaObject::openMetaCall(QObject *o, "
        "QMetaObject::Call _c, int _id, void **_a)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'MetaPropertyData'.")

  @staticmethod
  def registerNotifyPropertyChangeCallBack(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlDesignerMetaObject::registerNotifyPropertyChangeCallBack(void
    (*)(QObject *, const QQuickDesignerSupport::PropertyName &) callback)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'notifyPropertyChangeCallBack'.
    """
    raise NotImplementedError(
        "'QQmlDesignerMetaObject.registerNotifyPropertyChangeCallBack' has "
        "no cute function yet. Qt's 'void "
        "QQmlDesignerMetaObject::registerNotifyPropertyChangeCallBack(void "
        "(*)(QObject *, const QQuickDesignerSupport::PropertyName &) "
        "callback)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'notifyPropertyChangeCallBack'.")
