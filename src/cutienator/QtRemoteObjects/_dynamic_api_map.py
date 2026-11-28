"""
DynamicApiMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectsource_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DynamicApiMap to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QList, QMetaMethod
from . import SourceApiMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class DynamicApiMap(SourceApiMap):
  """
  The cute side of Qt's DynamicApiMap: a plain Python object standing in
  front of one C++ DynamicApiMap.

  It is built on the cute 'SourceApiMap', as Qt's DynamicApiMap is built on
  Qt's SourceApiMap, and has everything that class has.

  C++ hands a DynamicApiMap around as a copy, so every C++ DynamicApiMap
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's DynamicApiMap that has a ritual and that Python can
  call so far, 28 names in all: 'name', 'typeName', 'className', 'enumCount',
  'propertyCount', 'signalCount', 'methodCount', 'sourceEnumIndex',
  'sourcePropertyIndex', 'sourceSignalIndex', 'sourceMethodIndex',
  'signalParameterCount', 'signalParameterType', 'signalSignature',
  'signalParameterNames', 'methodParameterCount', 'methodParameterType',
  'methodSignature', 'methodType', 'methodParameterNames',
  'propertyIndexFromSignal', 'propertyRawIndexFromSignal', 'objectSignature',
  'isDynamic', 'parameterCount', 'parameterType', 'signature', 'checkCache'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DynamicApiMap::~DynamicApiMap()': the destructor: Python removes
    its C++ DynamicApiMap by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 31 functions Qt declares: 1 leans on 'QtPrivate.

  What to expect
  --------------

  - The C++ DynamicApiMap is created at the first use, not by
    'DynamicApiMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a DynamicApiMap back gives a copy the ritual made for
    Python, in a new cute DynamicApiMap.
  - Each name of Qt's DynamicApiMap that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'DynamicApiMap'

  #  Qt's '~DynamicApiMap()'. Naming it makes this a value class: Python owns
  #  every C++ DynamicApiMap behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13DynamicApiMapD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString DynamicApiMap::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DynamicApiMap::name() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap4nameEv')

  @overload()
  def typeName(self) -> str:
    """
    Calls Qt's 'QString DynamicApiMap::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#typeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DynamicApiMap::typeName() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap8typeNameEv')

  @overload(int)
  def typeName(self, index: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray DynamicApiMap::typeName(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#typeName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray DynamicApiMap::typeName(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap8typeNameEi', index,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def className(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray DynamicApiMap::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#className

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray DynamicApiMap::className() const
    address = self.uglySide.call('ritual_ZNK13DynamicApiMap9classNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def enumCount(self) -> int:
    """
    Calls Qt's 'int DynamicApiMap::enumCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#enumCount
    """
    #  int DynamicApiMap::enumCount() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap9enumCountEv')

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int DynamicApiMap::propertyCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#propertyCount
    """
    #  int DynamicApiMap::propertyCount() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap13propertyCountEv')

  def signalCount(self) -> int:
    """
    Calls Qt's 'int DynamicApiMap::signalCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#signalCount
    """
    #  int DynamicApiMap::signalCount() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap11signalCountEv')

  def methodCount(self) -> int:
    """
    Calls Qt's 'int DynamicApiMap::methodCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#methodCount
    """
    #  int DynamicApiMap::methodCount() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap11methodCountEv')

  @overload(int)
  def sourceEnumIndex(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::sourceEnumIndex(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#sourceEnumIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::sourceEnumIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap15sourceEnumIndexEi', index,
    )

  @overload(int)
  def sourcePropertyIndex(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::sourcePropertyIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#sourcePropertyIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::sourcePropertyIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap19sourcePropertyIndexEi', index,
    )

  @overload(int)
  def sourceSignalIndex(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::sourceSignalIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#sourceSignalIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::sourceSignalIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap17sourceSignalIndexEi', index,
    )

  @overload(int)
  def sourceMethodIndex(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::sourceMethodIndex(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#sourceMethodIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::sourceMethodIndex(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap17sourceMethodIndexEi', index,
    )

  @overload(int)
  def signalParameterCount(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::signalParameterCount(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#signalParameterCount

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::signalParameterCount(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap20signalParameterCountEi', index,
    )

  @overload(int, int)
  def signalParameterType(self, sigIndex: int, paramIndex: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::signalParameterType(int sigIndex, int
    paramIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#signalParameterType

    Parameters
    ----------

    sigIndex : int
      Passed on as it is.

    paramIndex : int
      Passed on as it is.
    """
    #  int DynamicApiMap::signalParameterType(int sigIndex, int paramIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap19signalParameterTypeEii',
        sigIndex, paramIndex,
    )

  @overload(int)
  def signalSignature(self, index: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray DynamicApiMap::signalSignature(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#signalSignature

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray DynamicApiMap::signalSignature(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap15signalSignatureEi', index,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def signalParameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList DynamicApiMap::signalParameterNames(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#signalParameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList DynamicApiMap::signalParameterNames(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap20signalParameterNamesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def methodParameterCount(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::methodParameterCount(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#methodParameterCount

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::methodParameterCount(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap20methodParameterCountEi', index,
    )

  @overload(int, int)
  def methodParameterType(self, methodIndex: int, paramIndex: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::methodParameterType(int methodIndex, int
    paramIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#methodParameterType

    Parameters
    ----------

    methodIndex : int
      Passed on as it is.

    paramIndex : int
      Passed on as it is.
    """
    #  int DynamicApiMap::methodParameterType(int methodIndex, int
    #      paramIndex) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap19methodParameterTypeEii',
        methodIndex, paramIndex,
    )

  @overload(int)
  def methodSignature(self, index: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray DynamicApiMap::methodSignature(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#methodSignature

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray DynamicApiMap::methodSignature(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap15methodSignatureEi', index,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def methodType(self, index: int) -> QMetaMethod.MethodType:
    """
    Calls Qt's 'QMetaMethod::MethodType DynamicApiMap::methodType(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#methodType

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMetaMethod.MethodType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QMetaMethod.MethodType(number)' gives.
    """
    #  QMetaMethod::MethodType DynamicApiMap::methodType(int index) const
    return QMetaMethod.MethodType(self.uglySide.call(
        'ritual_ZNK13DynamicApiMap10methodTypeEi', index,
    ))

  @overload(int)
  def methodParameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QByteArrayList DynamicApiMap::methodParameterNames(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#methodParameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QByteArrayList DynamicApiMap::methodParameterNames(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap20methodParameterNamesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(int)
  def propertyIndexFromSignal(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::propertyIndexFromSignal(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#propertyIndexFromSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::propertyIndexFromSignal(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap23propertyIndexFromSignalEi', index,
    )

  @overload(int)
  def propertyRawIndexFromSignal(self, index: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::propertyRawIndexFromSignal(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dynamicapimap.html#propertyRawIndexFromSignal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int DynamicApiMap::propertyRawIndexFromSignal(int index) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap26propertyRawIndexFromSignalEi', index,
    )

  def objectSignature(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray DynamicApiMap::objectSignature() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#objectSignature

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray DynamicApiMap::objectSignature() const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap15objectSignatureEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isDynamic(self) -> bool:
    """
    Calls Qt's 'bool DynamicApiMap::isDynamic() const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#isDynamic
    """
    #  bool DynamicApiMap::isDynamic() const
    return self.uglySide.call('ritual_ZNK13DynamicApiMap9isDynamicEv')

  @overload(int)
  def parameterCount(self, objectIndex: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::parameterCount(int objectIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#parameterCount

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.
    """
    #  int DynamicApiMap::parameterCount(int objectIndex) const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap14parameterCountEi', objectIndex,
    )

  @overload(int, int)
  def parameterType(self, objectIndex: int, paramIndex: int) -> int:
    """
    Calls Qt's 'int DynamicApiMap::parameterType(int objectIndex, int
    paramIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#parameterType

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    paramIndex : int
      Passed on as it is.
    """
    #  int DynamicApiMap::parameterType(int objectIndex, int paramIndex)
    #      const
    return self.uglySide.call(
        'ritual_ZNK13DynamicApiMap13parameterTypeEii',
        objectIndex, paramIndex,
    )

  @overload(int)
  def signature(self, objectIndex: int) -> QByteArray:
    """
    Calls Qt's 'const QByteArray DynamicApiMap::signature(int objectIndex)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#signature

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray DynamicApiMap::signature(int objectIndex) const
    address = self.uglySide.call(
        'ritual_ZNK13DynamicApiMap9signatureEi', objectIndex,
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
    Qt's 'DynamicApiMap::DynamicApiMap(QObject *object, const QMetaObject
    *metaObject, const QString &name, const QString &typeName)': leans on
    'QtPrivate::qtro_classinfo_signature(QMetaObject const*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'DynamicApiMap.__init__' has no cute function yet. Qt's "
        "'DynamicApiMap::DynamicApiMap(QObject *object, const QMetaObject "
        "*metaObject, const QString &name, const QString &typeName)': leans "
        "on 'QtPrivate::qtro_classinfo_signature(QMetaObject const*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
  def checkCache(self, objectIndex: int) -> None:
    """
    Calls Qt's 'void DynamicApiMap::checkCache(int objectIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/dynamicapimap.html#checkCache

    Parameters
    ----------

    objectIndex : int
      Passed on as it is.
    """
    #  void DynamicApiMap::checkCache(int objectIndex) const
    self.uglySide.call(
        'ritual_ZNK13DynamicApiMap10checkCacheEi', objectIndex,
    )
