"""
QV4::ResolvedTypeReference binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4resolvedtypereference_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QV4::ResolvedTypeReference to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QTypeRevision
  from . import QQmlType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlType = WAIT['QQmlType']
  QTypeRevision = WAIT['QTypeRevision']


class ResolvedTypeReference(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ResolvedTypeReference: a plain Python object
  standing in front of one C++ QV4::ResolvedTypeReference.

  What exists
  -----------

  Every function of Qt's QV4::ResolvedTypeReference that has a ritual and
  that Python can call so far, 12 names in all: 'createPropertyCache',
  'doDynamicTypeCheck', 'type', 'setType', 'typePropertyCache',
  'setTypePropertyCache', 'version', 'setVersion', 'isFullyDynamicType',
  'setFullyDynamicType', 'isSelfReference', 'setIsSelfReference'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QV4::ResolvedTypeReference::addToHash(QCryptographicHash
    *hash, QHash<quintptr, QByteArray> *checksums)': names 'QHash<quintptr,
    QByteArray>', which has no cute class yet.
  - Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QV4::ResolvedTypeReference::compilationUnit() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QV4::ResolvedTypeReference::setCompilationUnit(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QV4::ResolvedTypeReference is created at the first use, not by
    'QV4::ResolvedTypeReference(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ResolvedTypeReference.
  - Each name of Qt's QV4::ResolvedTypeReference that has no cute function
    yet, 'addToHash', 'compilationUnit', 'setCompilationUnit', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ResolvedTypeReference'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> QQmlType:
    """
    Calls Qt's 'QQmlType QV4::ResolvedTypeReference::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#type

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QV4::ResolvedTypeReference::type() const
    address = self.uglySide.call(
        'ritual_ZNK3QV421ResolvedTypeReference4typeEv',
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  def typePropertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QV4::ResolvedTypeReference::typePropertyCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#typePropertyCache

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QV4::ResolvedTypeReference::typePropertyCache() const
    address = self.uglySide.call(
        'ritual_ZNK3QV421ResolvedTypeReference17typePropertyCacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  def version(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QV4::ResolvedTypeReference::version() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#version

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QV4::ResolvedTypeReference::version() const
    address = self.uglySide.call(
        'ritual_ZNK3QV421ResolvedTypeReference7versionEv',
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def isFullyDynamicType(self) -> bool:
    """
    Calls Qt's 'bool QV4::ResolvedTypeReference::isFullyDynamicType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#isFullyDynamicType
    """
    #  bool QV4::ResolvedTypeReference::isFullyDynamicType() const
    return self.uglySide.call(
        'ritual_ZNK3QV421ResolvedTypeReference18isFullyDynamicTypeEv',
    )

  def isSelfReference(self) -> bool:
    """
    Calls Qt's 'bool QV4::ResolvedTypeReference::isSelfReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#isSelfReference
    """
    #  bool QV4::ResolvedTypeReference::isSelfReference() const
    return self.uglySide.call(
        'ritual_ZNK3QV421ResolvedTypeReference15isSelfReferenceEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlType)
  def setType(self, type: QQmlType) -> None:
    """
    Calls Qt's 'void QV4::ResolvedTypeReference::setType(QQmlType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#setType

    Parameters
    ----------

    type : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.
    """
    #  void QV4::ResolvedTypeReference::setType(QQmlType type)
    self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference7setTypeE8QQmlType',
        self._valueOf(type),
    )

  @overload(QQmlPropertyCache.ConstPtr)
  def setTypePropertyCache(self, cache: QQmlPropertyCache.ConstPtr) -> None:
    """
    Calls Qt's 'void
    QV4::ResolvedTypeReference::setTypePropertyCache(QQmlPropertyCache::
    ConstPtr cache)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html

    Parameters
    ----------

    cache : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QV4::ResolvedTypeReference::setTypePropertyCache(
    #      QQmlPropertyCache::ConstPtr cache)
    self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference20setTypePropertyCacheEN17QQml'
        'PropertyCache8ConstPtrE',
        self._valueOf(cache),
    )

  @overload(QTypeRevision)
  def setVersion(self, version: QTypeRevision) -> None:
    """
    Calls Qt's 'void QV4::ResolvedTypeReference::setVersion(QTypeRevision
    version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#setVersion

    Parameters
    ----------

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QV4::ResolvedTypeReference::setVersion(QTypeRevision version)
    self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference10setVersionE13QTypeRevision',
        self._valueOf(version),
    )

  @overload(bool)
  def setFullyDynamicType(self, fullyDynamic: bool) -> None:
    """
    Calls Qt's 'void QV4::ResolvedTypeReference::setFullyDynamicType(bool
    fullyDynamic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#setFullyDynamicType

    Parameters
    ----------

    fullyDynamic : bool
      Passed on as it is.
    """
    #  void QV4::ResolvedTypeReference::setFullyDynamicType(bool
    #      fullyDynamic)
    self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference19setFullyDynamicTypeEb',
        fullyDynamic,
    )

  @overload(bool)
  def setIsSelfReference(self, selfReference: bool) -> None:
    """
    Calls Qt's 'void QV4::ResolvedTypeReference::setIsSelfReference(bool
    selfReference)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#setIsSelfReference

    Parameters
    ----------

    selfReference : bool
      Passed on as it is.
    """
    #  void QV4::ResolvedTypeReference::setIsSelfReference(bool
    #      selfReference)
    self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference18setIsSelfReferenceEb',
        selfReference,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QV4::ResolvedTypeReference::ResolvedTypeReference()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html
    """
    #  QV4::ResolvedTypeReference::ResolvedTypeReference()
    self._noteCreation(ResolvedTypeReference, lambda: Rituals.call(
        'ritual_ZN3QV421ResolvedTypeReferenceC1Ev',
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

  def createPropertyCache(self) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QV4::ResolvedTypeReference::createPropertyCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#createPropertyCache

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QV4::ResolvedTypeReference::createPropertyCache()
    address = self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference19createPropertyCacheEv',
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  def doDynamicTypeCheck(self) -> None:
    """
    Calls Qt's 'void QV4::ResolvedTypeReference::doDynamicTypeCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-resolvedtypereference.html#doDynamicTypeCheck
    """
    #  void QV4::ResolvedTypeReference::doDynamicTypeCheck()
    self.uglySide.call(
        'ritual_ZN3QV421ResolvedTypeReference18doDynamicTypeCheckEv',
    )

  @staticmethod
  def addToHash(*__, **_) -> Never:
    """
    Qt's 'bool QV4::ResolvedTypeReference::addToHash(QCryptographicHash
    *hash, QHash<quintptr, QByteArray> *checksums)': names 'QHash<quintptr,
    QByteArray>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.ResolvedTypeReference.addToHash' has no cute function yet. "
        "Qt's 'bool "
        "QV4::ResolvedTypeReference::addToHash(QCryptographicHash *hash, "
        "QHash<quintptr, QByteArray> *checksums)': names 'QHash<quintptr, "
        "QByteArray>', which has no cute class yet.")

  @staticmethod
  def compilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    QV4::ResolvedTypeReference::compilationUnit() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.ResolvedTypeReference.compilationUnit' has no cute function "
        "yet. Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QV4::ResolvedTypeReference::compilationUnit() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void QV4::ResolvedTypeReference::setCompilationUnit(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ResolvedTypeReference.setCompilationUnit' has no cute "
        "function yet. Qt's 'void "
        "QV4::ResolvedTypeReference::setCompilationUnit(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> &unit)': takes "
        "a type Python has no way to hand over yet.")
