"""
QV4::UrlSearchParamsObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4urlobject_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::UrlSearchParamsObject to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class UrlSearchParamsObject(QV4.Object):
  """
  The cute side of Qt's QV4::UrlSearchParamsObject: a plain Python object
  standing in front of one C++ QV4::UrlSearchParamsObject.

  It is built on the cute 'QV4::Object', as Qt's QV4::UrlSearchParamsObject
  is built on Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::UrlSearchParamsObject that has a ritual and
  that Python can call so far, 18 names in all: '__dataTest', 'd_unchecked',
  'd', 'defaultPrototype', 'initializeParams', 'urlObject', 'setUrlObject',
  'searchString', 'nameAt', 'nameAtRaw', 'valueAt', 'valueAtRaw', 'append',
  'indexOf', 'length', 'virtualGetOwnProperty', 'stringAt', 'stringAtRaw'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::UrlSearchParamsObject::initializeParams(ScopedArrayObject
    &params)': takes a type Python has no way to hand over yet.
  - Qt's 'void QV4::UrlSearchParamsObject::initializeParams(ScopedObject
    &params)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<QStringList> QV4::UrlSearchParamsObject::params() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QV4::UrlSearchParamsObject::setParams(const QList<QStringList>
    &params)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 29 functions Qt declares: 3 forbidden; 1 not a gap; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file; 1 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::UrlSearchParamsObject is created at the first use, not by
    'QV4::UrlSearchParamsObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::UrlSearchParamsObject.
  - Each name of Qt's QV4::UrlSearchParamsObject that has no cute function
    yet, 'params', 'setParams', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def defaultPrototype(
      e: Optional[QV4.ExecutionEngine],
  ) -> Optional[QV4.Object]:
    """
    Calls Qt's 'QV4::Object
    *QV4::UrlSearchParamsObject::defaultPrototype(QV4::ExecutionEngine *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#defaultPrototype

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Object
    #      *QV4::UrlSearchParamsObject::defaultPrototype(QV4::ExecutionEngine
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV421UrlSearchParamsObject16defaultPrototypeEPNS_15Execu'
        'tionEngineE',
        CuteMixin._addressOf(e),
    )
    return QV4.Object._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(NoneType, WAIT['QV4.PropertyKey'], NoneType)
  def virtualGetOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
  ) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes
    QV4::UrlSearchParamsObject::virtualGetOwnProperty(const Managed *m,
    PropertyKey id, Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes
    #      QV4::UrlSearchParamsObject::virtualGetOwnProperty(const Managed
    #      *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV421UrlSearchParamsObject21virtualGetOwnPropertyEPKNS_7'
        'ManagedENS_11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::UrlSearchParamsObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.UrlSearchParamsObject]:
    """
    Calls Qt's 'QV4::Heap::UrlSearchParamsObject
    *QV4::UrlSearchParamsObject::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.UrlSearchParamsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::UrlSearchParamsObject
    #      *QV4::UrlSearchParamsObject::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject11d_uncheckedEv',
    )
    return QV4.Heap.UrlSearchParamsObject._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.UrlSearchParamsObject]:
    """
    Calls Qt's 'QV4::Heap::UrlSearchParamsObject
    *QV4::UrlSearchParamsObject::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#d

    Returns
    -------

    Optional[QV4.Heap.UrlSearchParamsObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::UrlSearchParamsObject *QV4::UrlSearchParamsObject::d()
    #      const
    address = self.uglySide.call('ritual_ZNK3QV421UrlSearchParamsObject1dEv')
    return QV4.Heap.UrlSearchParamsObject._cuteAt(address)

  def urlObject(self) -> Optional[QV4.Heap.UrlObject]:
    """
    Calls Qt's 'Heap::UrlObject *QV4::UrlSearchParamsObject::urlObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#urlObject

    Returns
    -------

    Optional[QV4.Heap.UrlObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::UrlObject *QV4::UrlSearchParamsObject::urlObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject9urlObjectEv',
    )
    return QV4.Heap.UrlObject._cuteAt(address)

  def searchString(self) -> str:
    """
    Calls Qt's 'QString QV4::UrlSearchParamsObject::searchString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#searchString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlSearchParamsObject::searchString() const
    return self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject12searchStringEv',
    )

  @overload(int)
  def nameAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QV4::UrlSearchParamsObject::nameAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#nameAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlSearchParamsObject::nameAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject6nameAtEi', index,
    )

  @overload(int)
  def nameAtRaw(self, index: int) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::UrlSearchParamsObject::nameAtRaw(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#nameAtRaw

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::UrlSearchParamsObject::nameAtRaw(int index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject9nameAtRawEi', index,
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(int)
  def valueAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QV4::UrlSearchParamsObject::valueAt(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#valueAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlSearchParamsObject::valueAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject7valueAtEi', index,
    )

  @overload(int)
  def valueAtRaw(self, index: int) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::UrlSearchParamsObject::valueAtRaw(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#valueAtRaw

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::UrlSearchParamsObject::valueAtRaw(int index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject10valueAtRawEi', index,
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(str)
  @overload(str, int)
  def indexOf(self, name: str, last: int = -1) -> int:
    """
    Calls Qt's 'int QV4::UrlSearchParamsObject::indexOf(QString name, int
    last) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#indexOf

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    last : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QV4::UrlSearchParamsObject::indexOf(QString name, int last) const
    return self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject7indexOfE7QStringi',
        name, last,
    )

  def length(self) -> int:
    """
    Calls Qt's 'int QV4::UrlSearchParamsObject::length() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#length
    """
    #  int QV4::UrlSearchParamsObject::length() const
    return self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject6lengthEv',
    )

  @overload(int, int)
  def stringAt(self, index: int, pairIndex: int) -> str:
    """
    Calls Qt's 'QString QV4::UrlSearchParamsObject::stringAt(int index, int
    pairIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    pairIndex : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::UrlSearchParamsObject::stringAt(int index, int pairIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject8stringAtEii',
        index, pairIndex,
    )

  @overload(int, int)
  def stringAtRaw(
      self,
      index: int,
      pairIndex: int,
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::UrlSearchParamsObject::stringAtRaw(int
    index, int pairIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#stringAtRaw

    Parameters
    ----------

    index : int
      Passed on as it is.

    pairIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::UrlSearchParamsObject::stringAtRaw(int index, int
    #      pairIndex) const
    address = self.uglySide.call(
        'ritual_ZNK3QV421UrlSearchParamsObject11stringAtRawEii',
        index, pairIndex,
    )
    return QV4.Heap.String._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.UrlObject'])
  @overload(NoneType)
  def setUrlObject(self, url: Optional[QV4.UrlObject]) -> None:
    """
    Calls Qt's 'void QV4::UrlSearchParamsObject::setUrlObject(const UrlObject
    *url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#setUrlObject

    Parameters
    ----------

    url : Optional[QV4.UrlObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::UrlSearchParamsObject::setUrlObject(const UrlObject *url)
    self.uglySide.call(
        'ritual_ZN3QV421UrlSearchParamsObject12setUrlObjectEPKNS_9UrlObject'
        'E',
        self._addressOf(url),
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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::UrlSearchParamsObject::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#__dataTest
    """
    #  void QV4::UrlSearchParamsObject::__dataTest()
    self.uglySide.call('ritual_ZN3QV421UrlSearchParamsObject10__dataTestEv')

  @overload()
  def initializeParams(self) -> None:
    """
    Calls Qt's 'void QV4::UrlSearchParamsObject::initializeParams()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#initializeParams
    """
    #  void QV4::UrlSearchParamsObject::initializeParams()
    self.uglySide.call(
        'ritual_ZN3QV421UrlSearchParamsObject16initializeParamsEv',
    )

  @overload(str)
  def initializeParams(self, params: str) -> None:
    """
    Calls Qt's 'void QV4::UrlSearchParamsObject::initializeParams(QString
    params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#initializeParams

    Parameters
    ----------

    params : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QV4::UrlSearchParamsObject::initializeParams(QString params)
    self.uglySide.call(
        'ritual_ZN3QV421UrlSearchParamsObject16initializeParamsE7QString',
        params,
    )

  @overload(WAIT['QV4.Heap.String'], WAIT['QV4.Heap.String'])
  @overload(WAIT['QV4.Heap.String'], NoneType)
  @overload(NoneType, WAIT['QV4.Heap.String'])
  @overload(NoneType, NoneType)
  def append(
      self,
      name: Optional[QV4.Heap.String],
      value: Optional[QV4.Heap.String],
  ) -> None:
    """
    Calls Qt's 'void QV4::UrlSearchParamsObject::append(Heap::String *name,
    Heap::String *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-urlsearchparamsobject.html#append

    Parameters
    ----------

    name : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::UrlSearchParamsObject::append(Heap::String *name,
    #      Heap::String *value)
    self.uglySide.call(
        'ritual_ZN3QV421UrlSearchParamsObject6appendEPNS_4Heap6StringES3_',
        self._addressOf(name), self._addressOf(value),
    )

  @staticmethod
  def params(*__, **_) -> Never:
    """
    Qt's 'QList<QStringList> QV4::UrlSearchParamsObject::params() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsObject.params' has no cute function yet. Qt's "
        "'QList<QStringList> QV4::UrlSearchParamsObject::params() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setParams(*__, **_) -> Never:
    """
    Qt's 'void QV4::UrlSearchParamsObject::setParams(const QList<QStringList>
    &params)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.UrlSearchParamsObject.setParams' has no cute function yet. "
        "Qt's 'void QV4::UrlSearchParamsObject::setParams(const "
        "QList<QStringList> &params)': takes a type Python has no way to "
        "hand over yet.")
