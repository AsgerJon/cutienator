"""
QQmlOpenMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlopenmetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlOpenMetaObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QAbstractDynamicMetaObject, QDynamicMetaObjectData
from ..QtCore import QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QObject, QVariant
  from . import QQmlOpenMetaObjectType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlOpenMetaObject(QAbstractDynamicMetaObject):
  """
  The cute side of Qt's QQmlOpenMetaObject: a plain Python object standing in
  front of one C++ QQmlOpenMetaObject.

  It is built on the cute 'QAbstractDynamicMetaObject', as Qt's
  QQmlOpenMetaObject is built on Qt's QAbstractDynamicMetaObject, and has
  everything that class has.

  C++ hands a QQmlOpenMetaObject around as a copy, so every C++
  QQmlOpenMetaObject behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlOpenMetaObject that has a ritual and that Python
  can call so far, 20 names in all: 'value', 'setValue', 'hasValue', 'count',
  'name', 'object', 'initialValue', 'setCached', 'autoCreatesProperties',
  'setAutoCreatesProperties', 'type', 'parent', 'emitPropertyNotification',
  'unparent', 'createProperty', 'propertyRead', 'propertyWrite',
  'propertyWriteValue', 'propertyWritten', 'checkedSetValue'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlOpenMetaObject::QQmlOpenMetaObject(QObject *a0, const
    QQmlRefPointer<QQmlOpenMetaObjectType> &a1)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlOpenMetaObject::~QQmlOpenMetaObject()': the destructor: Python
    removes its C++ QQmlOpenMetaObject by it, and has no other use for it.
  - Qt's 'void QQmlOpenMetaObject::setValues(const QHash<QByteArray,
    QVariant> &a0, bool force)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QVariant &QQmlOpenMetaObject::valueRef(const QByteArray &a0)':
    gives a type Python has no way to take yet.
  - Qt's 'int QQmlOpenMetaObject::metaCall(QObject *o, QMetaObject::Call _c,
    int _id, void **_a)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlOpenMetaObject::propertyCreated(int a0,
    QMetaPropertyBuilder &a1)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QQmlOpenMetaObject is created at the first use, not by
    'QQmlOpenMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlOpenMetaObject back gives a copy the ritual made
    for Python, in a new cute QQmlOpenMetaObject.
  - Each name of Qt's QQmlOpenMetaObject that has no cute function yet,
    'propertyCreated', 'setValues', 'valueRef', holds a function that raises
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
  __qt_class__ = 'QQmlOpenMetaObject'

  #  A C++ QQmlOpenMetaObject Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlOpenMetaObject'

  #  The functions Qt calls itself that QQmlOpenMetaObject is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'propertyCreated': (
          'void QQmlOpenMetaObject::propertyCreated(int, '
          'QMetaPropertyBuilder &)',
      ),
  }

  #  The functions Qt calls itself that QQmlOpenMetaObject is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialValue': (
          ('_ZN18QQmlOpenMetaObject12initialValueEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyRead': (
          ('_ZN18QQmlOpenMetaObject12propertyReadEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyWrite': (
          ('_ZN18QQmlOpenMetaObject13propertyWriteEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'propertyWriteValue': (
          ('_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'propertyWritten': (
          ('_ZN18QQmlOpenMetaObject15propertyWrittenEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QQmlOpenMetaObject()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlOpenMetaObject behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlOpenMetaObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def value(self, a0: QByteArray) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlOpenMetaObject::value(const QByteArray &a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#value

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlOpenMetaObject::value(const QByteArray &a0) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlOpenMetaObject5valueERK10QByteArray',
        self._valueOf(a0),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def value(self, a0: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlOpenMetaObject::value(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#value

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlOpenMetaObject::value(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK18QQmlOpenMetaObject5valueEi', a0,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def hasValue(self, a0: int) -> bool:
    """
    Calls Qt's 'bool QQmlOpenMetaObject::hasValue(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#hasValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  bool QQmlOpenMetaObject::hasValue(int a0) const
    return self.uglySide.call(
        'ritual_ZNK18QQmlOpenMetaObject8hasValueEi', a0,
    )

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlOpenMetaObject::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#count
    """
    #  int QQmlOpenMetaObject::count() const
    return self.uglySide.call('ritual_ZNK18QQmlOpenMetaObject5countEv')

  @overload(int)
  def name(self, a0: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlOpenMetaObject::name(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#name

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlOpenMetaObject::name(int a0) const
    address = self.uglySide.call('ritual_ZNK18QQmlOpenMetaObject4nameEi', a0)
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlOpenMetaObject::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlOpenMetaObject::object() const
    address = self.uglySide.call('ritual_ZNK18QQmlOpenMetaObject6objectEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def autoCreatesProperties(self) -> bool:
    """
    Calls Qt's 'bool QQmlOpenMetaObject::autoCreatesProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#autoCreatesProperties
    """
    #  bool QQmlOpenMetaObject::autoCreatesProperties() const
    return self.uglySide.call(
        'ritual_ZNK18QQmlOpenMetaObject21autoCreatesPropertiesEv',
    )

  def type(self) -> Optional[QQmlOpenMetaObjectType]:
    """
    Calls Qt's 'QQmlOpenMetaObjectType *QQmlOpenMetaObject::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#type

    Returns
    -------

    Optional[QQmlOpenMetaObjectType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlOpenMetaObjectType *QQmlOpenMetaObject::type() const
    address = self.uglySide.call('ritual_ZNK18QQmlOpenMetaObject4typeEv')
    from . import QQmlOpenMetaObjectType
    return QQmlOpenMetaObjectType._cuteAt(address)

  def parent(self) -> Optional[QDynamicMetaObjectData]:
    """
    Calls Qt's 'QDynamicMetaObjectData *QQmlOpenMetaObject::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#parent

    Returns
    -------

    Optional[QDynamicMetaObjectData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDynamicMetaObjectData *QQmlOpenMetaObject::parent() const
    address = self.uglySide.call('ritual_ZNK18QQmlOpenMetaObject6parentEv')
    return QDynamicMetaObjectData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray, QVariant)
  @overload(QByteArray, QVariant, bool)
  def setValue(
      self,
      a0: QByteArray,
      a1: QVariant,
      force: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlOpenMetaObject::setValue(const QByteArray &a0, const
    QVariant &a1, bool force)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#setValue

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    force : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQmlOpenMetaObject::setValue(const QByteArray &a0, const QVariant
    #      &a1, bool force)
    return self.uglySide.call(
        'ritual_ZN18QQmlOpenMetaObject8setValueERK10QByteArrayRK8QVariantb',
        self._valueOf(a0), self._valueOf(a1), force,
    )

  @overload(int, QVariant)
  def setValue(self, a0: int, a1: QVariant) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::setValue(int a0, const QVariant
    &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#setValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlOpenMetaObject::setValue(int a0, const QVariant &a1)
    self.uglySide.call(
        'ritual_ZN18QQmlOpenMetaObject8setValueEiRK8QVariant',
        a0, self._valueOf(a1),
    )

  @overload(bool)
  def setCached(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::setCached(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#setCached

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQmlOpenMetaObject::setCached(bool a0)
    self.uglySide.call('ritual_ZN18QQmlOpenMetaObject9setCachedEb', a0)

  @overload(bool)
  def setAutoCreatesProperties(self, autoCreate: bool) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::setAutoCreatesProperties(bool
    autoCreate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#setAutoCreatesProperties

    Parameters
    ----------

    autoCreate : bool
      Passed on as it is.
    """
    #  void QQmlOpenMetaObject::setAutoCreatesProperties(bool autoCreate)
    self.uglySide.call(
        'ritual_ZN18QQmlOpenMetaObject24setAutoCreatesPropertiesEb',
        autoCreate,
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

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QMetaObject)
  @overload(QObject, NoneType)
  @overload(NoneType, QMetaObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      a0: Optional[QObject],
      a1: Optional[QMetaObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlOpenMetaObject::QQmlOpenMetaObject(QObject *a0, const QMetaObject
    *a1)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#QQmlOpenMetaObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlOpenMetaObject::QQmlOpenMetaObject(QObject *a0, const QMetaObject
    #      *a1)
    self._noteCreation(QQmlOpenMetaObject, lambda: Rituals.call(
        'ritual_ZN18QQmlOpenMetaObjectC1EP7QObjectPK11QMetaObject',
        self._addressOf(a0, 'QObject'), self._addressOf(a1, 'QMetaObject'),
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

  @overload(int)
  def initialValue(self, a0: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlOpenMetaObject::initialValue(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#initialValue

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlOpenMetaObject::initialValue(int a0)
    ritual = 'ritual_ZN18QQmlOpenMetaObject12initialValueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlOpenMetaObject12initialValueEi'
    address = self.uglySide.call(ritual, a0)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QByteArray)
  def emitPropertyNotification(self, propertyName: QByteArray) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::emitPropertyNotification(const
    QByteArray &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#emitPropertyNotification

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQmlOpenMetaObject::emitPropertyNotification(const QByteArray
    #      &propertyName)
    self.uglySide.call(
        'ritual_ZN18QQmlOpenMetaObject24emitPropertyNotificationERK10QByteA'
        'rray',
        self._valueOf(propertyName),
    )

  def unparent(self) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::unparent()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlopenmetaobject.html#unparent
    """
    #  void QQmlOpenMetaObject::unparent()
    self.uglySide.call('ritual_ZN18QQmlOpenMetaObject8unparentEv')

  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def createProperty(self, a0: Optional[str], a1: Optional[str]) -> int:
    """
    Calls Qt's 'int QQmlOpenMetaObject::createProperty(const char *a0, const
    char *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#createProperty

    Parameters
    ----------

    a0 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    a1 : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QQmlOpenMetaObject::createProperty(const char *a0, const char *a1)
    return self.uglySide.call(
        'ritual_ZN18QQmlOpenMetaObject14createPropertyEPKcS1_',
        self._bytesOf(a0), self._bytesOf(a1),
    )

  @overload(int)
  def propertyRead(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::propertyRead(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#propertyRead

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlOpenMetaObject::propertyRead(int a0)
    ritual = 'ritual_ZN18QQmlOpenMetaObject12propertyReadEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlOpenMetaObject12propertyReadEi'
    self.uglySide.call(ritual, a0)

  @overload(int)
  def propertyWrite(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::propertyWrite(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#propertyWrite

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlOpenMetaObject::propertyWrite(int a0)
    ritual = 'ritual_ZN18QQmlOpenMetaObject13propertyWriteEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlOpenMetaObject13propertyWriteEi'
    self.uglySide.call(ritual, a0)

  @overload(int, QVariant)
  def propertyWriteValue(self, a0: int, a1: QVariant) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlOpenMetaObject::propertyWriteValue(int a0, const
    QVariant &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#propertyWriteValue

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
    #  QVariant QQmlOpenMetaObject::propertyWriteValue(int a0, const QVariant
    #      &a1)
    ritual = 'ritual_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQmlOpenMetaObject18propertyWriteValueEiRK8QVaria'
          'nt')
    address = self.uglySide.call(ritual, a0, self._valueOf(a1))
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def propertyWritten(self, a0: int) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObject::propertyWritten(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#propertyWritten

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQmlOpenMetaObject::propertyWritten(int a0)
    ritual = 'ritual_ZN18QQmlOpenMetaObject15propertyWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQmlOpenMetaObject15propertyWrittenEi'
    self.uglySide.call(ritual, a0)

  @overload(int, QVariant, bool)
  def checkedSetValue(
      self,
      index: int,
      value: QVariant,
      force: bool,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlOpenMetaObject::checkedSetValue(int index, const
    QVariant &value, bool force)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobject.html#checkedSetValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    force : bool
      Passed on as it is.
    """
    #  bool QQmlOpenMetaObject::checkedSetValue(int index, const QVariant
    #      &value, bool force)
    return self.uglySide.call(
        'ritual_ZN18QQmlOpenMetaObject15checkedSetValueEiRK8QVariantb',
        index, self._valueOf(value), force,
    )

  @staticmethod
  def propertyCreated(*__, **_) -> Never:
    """
    Qt's 'void QQmlOpenMetaObject::propertyCreated(int a0,
    QMetaPropertyBuilder &a1)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlOpenMetaObject.propertyCreated' has no cute function yet. "
        "Qt's 'void QQmlOpenMetaObject::propertyCreated(int a0, "
        "QMetaPropertyBuilder &a1)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setValues(*__, **_) -> Never:
    """
    Qt's 'void QQmlOpenMetaObject::setValues(const QHash<QByteArray,
    QVariant> &a0, bool force)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlOpenMetaObject.setValues' has no cute function yet. Qt's "
        "'void QQmlOpenMetaObject::setValues(const QHash<QByteArray, "
        "QVariant> &a0, bool force)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def valueRef(*__, **_) -> Never:
    """
    Qt's 'QVariant &QQmlOpenMetaObject::valueRef(const QByteArray &a0)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlOpenMetaObject.valueRef' has no cute function yet. Qt's "
        "'QVariant &QQmlOpenMetaObject::valueRef(const QByteArray &a0)': "
        "gives a type Python has no way to take yet.")
