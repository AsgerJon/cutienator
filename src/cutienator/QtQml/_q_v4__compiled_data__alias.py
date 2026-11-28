"""
QV4::CompiledData::Alias binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Alias to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QV4


class Alias(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Alias: a plain Python object
  standing in front of one C++ QV4::CompiledData::Alias.

  C++ hands a QV4::CompiledData::Alias around as a copy, so every C++
  QV4::CompiledData::Alias behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Alias that has a ritual and that
  Python can call so far, 12 names in all: 'isReadOnly', 'setIsReadOnly',
  'nameIndex', 'setNameIndex', 'idIndex', 'setIdIndex', 'propertyNameIndex',
  'setPropertyNameIndex', 'location', 'setLocation', 'referenceLocation',
  'setReferenceLocation'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::Alias::~Alias()': the destructor: Python removes
    its C++ QV4::CompiledData::Alias by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Alias is created at the first use, not by
    'QV4::CompiledData::Alias(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Alias back gives a copy the ritual
    made for Python, in a new cute QV4::CompiledData::Alias.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Alias'

  #  Qt's '~QV4::CompiledData::Alias()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::Alias behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData5AliasD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Alias::isReadOnly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#isReadOnly
    """
    #  bool QV4::CompiledData::Alias::isReadOnly() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData5Alias10isReadOnlyEv',
    )

  def nameIndex(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Alias::nameIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#nameIndex
    """
    #  quint32 QV4::CompiledData::Alias::nameIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData5Alias9nameIndexEv',
    )

  def idIndex(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Alias::idIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#idIndex
    """
    #  quint32 QV4::CompiledData::Alias::idIndex() const
    return self.uglySide.call('ritual_ZNK3QV412CompiledData5Alias7idIndexEv')

  def propertyNameIndex(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Alias::propertyNameIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#propertyNameIndex
    """
    #  quint32 QV4::CompiledData::Alias::propertyNameIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData5Alias17propertyNameIndexEv',
    )

  def location(self) -> QV4.CompiledData.Location:
    """
    Calls Qt's 'Location QV4::CompiledData::Alias::location() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#location

    Returns
    -------

    QV4.CompiledData.Location
      A new cute QV4::CompiledData::Location around the copy Qt gave back.
      Python owns it.
    """
    #  Location QV4::CompiledData::Alias::location() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData5Alias8locationEv',
    )
    return QV4.CompiledData.Location._cuteOwning(address)

  def referenceLocation(self) -> QV4.CompiledData.Location:
    """
    Calls Qt's 'Location QV4::CompiledData::Alias::referenceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#referenceLocation

    Returns
    -------

    QV4.CompiledData.Location
      A new cute QV4::CompiledData::Location around the copy Qt gave back.
      Python owns it.
    """
    #  Location QV4::CompiledData::Alias::referenceLocation() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData5Alias17referenceLocationEv',
    )
    return QV4.CompiledData.Location._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsReadOnly(self, isReadOnly: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Alias::setIsReadOnly(bool
    isReadOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#setIsReadOnly

    Parameters
    ----------

    isReadOnly : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Alias::setIsReadOnly(bool isReadOnly)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData5Alias13setIsReadOnlyEb', isReadOnly,
    )

  @overload(int)
  def setNameIndex(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Alias::setNameIndex(quint32
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#setNameIndex

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Alias::setNameIndex(quint32 nameIndex)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData5Alias12setNameIndexEj', nameIndex,
    )

  @overload(int)
  def setIdIndex(self, idIndex: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Alias::setIdIndex(quint32 idIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#setIdIndex

    Parameters
    ----------

    idIndex : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Alias::setIdIndex(quint32 idIndex)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData5Alias10setIdIndexEj', idIndex,
    )

  @overload(int)
  def setPropertyNameIndex(self, propertyNameIndex: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Alias::setPropertyNameIndex(quint32
    propertyNameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#setPropertyNameIndex

    Parameters
    ----------

    propertyNameIndex : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Alias::setPropertyNameIndex(quint32
    #      propertyNameIndex)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData5Alias20setPropertyNameIndexEj',
        propertyNameIndex,
    )

  @overload(WAIT['QV4.CompiledData.Location'])
  def setLocation(self, location: QV4.CompiledData.Location) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Alias::setLocation(Location
    location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#setLocation

    Parameters
    ----------

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.
    """
    #  void QV4::CompiledData::Alias::setLocation(Location location)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData5Alias11setLocationENS0_8LocationE',
        self._valueOf(location),
    )

  @overload(WAIT['QV4.CompiledData.Location'])
  def setReferenceLocation(
      self,
      referenceLocation: QV4.CompiledData.Location,
  ) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Alias::setReferenceLocation(Location
    referenceLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-alias.html#setReferenceLocation

    Parameters
    ----------

    referenceLocation : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.
    """
    #  void QV4::CompiledData::Alias::setReferenceLocation(Location
    #      referenceLocation)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData5Alias20setReferenceLocationENS0_8Locat'
        'ionE',
        self._valueOf(referenceLocation),
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
