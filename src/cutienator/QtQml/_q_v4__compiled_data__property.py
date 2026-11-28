"""
QV4::CompiledData::Property binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Property to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QV4


class Property(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Property: a plain Python object
  standing in front of one C++ QV4::CompiledData::Property.

  C++ hands a QV4::CompiledData::Property around as a copy, so every C++
  QV4::CompiledData::Property behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Property that has a ritual and
  that Python can call so far, 20 names in all: 'nameIndex', 'setNameIndex',
  'isVirtual', 'setIsVirtual', 'isOverride', 'setIsOverride', 'isFinal',
  'setIsFinal', 'setCommonType', 'commonType', 'setTypeNameIndex',
  'typeNameIndex', 'isCommonType', 'commonTypeOrTypeNameIndex', 'isList',
  'setIsList', 'isRequired', 'setIsRequired', 'isReadOnly', 'setIsReadOnly'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CompiledData::Property::~Property()': the destructor: Python
    removes its C++ QV4::CompiledData::Property by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Property is created at the first use, not by
    'QV4::CompiledData::Property(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Property back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::Property.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Property'

  #  Qt's '~QV4::CompiledData::Property()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::CompiledData::Property behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData8PropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nameIndex(self) -> int:
    """
    Calls Qt's 'quint32 QV4::CompiledData::Property::nameIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#nameIndex
    """
    #  quint32 QV4::CompiledData::Property::nameIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property9nameIndexEv',
    )

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isVirtual() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isVirtual
    """
    #  bool QV4::CompiledData::Property::isVirtual() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property9isVirtualEv',
    )

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isOverride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isOverride
    """
    #  bool QV4::CompiledData::Property::isOverride() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property10isOverrideEv',
    )

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isFinal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isFinal
    """
    #  bool QV4::CompiledData::Property::isFinal() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property7isFinalEv',
    )

  def commonType(self) -> QV4.CompiledData.CommonType:
    """
    Calls Qt's 'CommonType QV4::CompiledData::Property::commonType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#commonType

    Returns
    -------

    QV4.CompiledData.CommonType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QV4.CompiledData.CommonType(number)' gives.
    """
    #  CommonType QV4::CompiledData::Property::commonType() const
    return QV4.CompiledData.CommonType(self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property10commonTypeEv',
    ))

  def typeNameIndex(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Property::typeNameIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#typeNameIndex
    """
    #  int QV4::CompiledData::Property::typeNameIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property13typeNameIndexEv',
    )

  def isCommonType(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isCommonType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isCommonType
    """
    #  bool QV4::CompiledData::Property::isCommonType() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property12isCommonTypeEv',
    )

  def commonTypeOrTypeNameIndex(self) -> int:
    """
    Calls Qt's 'uint QV4::CompiledData::Property::commonTypeOrTypeNameIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html
    """
    #  uint QV4::CompiledData::Property::commonTypeOrTypeNameIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property25commonTypeOrTypeNameIndexEv',
    )

  def isList(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isList
    """
    #  bool QV4::CompiledData::Property::isList() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property6isListEv',
    )

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isRequired
    """
    #  bool QV4::CompiledData::Property::isRequired() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property10isRequiredEv',
    )

  def isReadOnly(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Property::isReadOnly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#isReadOnly
    """
    #  bool QV4::CompiledData::Property::isReadOnly() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData8Property10isReadOnlyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNameIndex(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setNameIndex(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setNameIndex

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setNameIndex(int nameIndex)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property12setNameIndexEi', nameIndex,
    )

  @overload(bool)
  def setIsVirtual(self, isVirtual: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setIsVirtual(bool
    isVirtual)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setIsVirtual

    Parameters
    ----------

    isVirtual : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setIsVirtual(bool isVirtual)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property12setIsVirtualEb', isVirtual,
    )

  @overload(bool)
  def setIsOverride(self, isOverride: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setIsOverride(bool
    isOverride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setIsOverride

    Parameters
    ----------

    isOverride : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setIsOverride(bool isOverride)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property13setIsOverrideEb', isOverride,
    )

  @overload(bool)
  def setIsFinal(self, isFinal: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setIsFinal(bool isFinal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setIsFinal

    Parameters
    ----------

    isFinal : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setIsFinal(bool isFinal)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property10setIsFinalEb', isFinal,
    )

  @overload(QV4.CompiledData.CommonType)
  def setCommonType(self, t: QV4.CompiledData.CommonType) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setCommonType(CommonType
    t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setCommonType

    Parameters
    ----------

    t : QV4.CompiledData.CommonType
      Passed on as its number.
    """
    #  void QV4::CompiledData::Property::setCommonType(CommonType t)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property13setCommonTypeENS0_10CommonTy'
        'peE',
        t.value,
    )

  @overload(int)
  def setTypeNameIndex(self, nameIndex: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setTypeNameIndex(int
    nameIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setTypeNameIndex

    Parameters
    ----------

    nameIndex : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setTypeNameIndex(int nameIndex)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property16setTypeNameIndexEi',
        nameIndex,
    )

  @overload(bool)
  def setIsList(self, isList: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setIsList(bool isList)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setIsList

    Parameters
    ----------

    isList : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setIsList(bool isList)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property9setIsListEb', isList,
    )

  @overload(bool)
  def setIsRequired(self, isRequired: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setIsRequired(bool
    isRequired)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setIsRequired

    Parameters
    ----------

    isRequired : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setIsRequired(bool isRequired)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property13setIsRequiredEb', isRequired,
    )

  @overload(bool)
  def setIsReadOnly(self, isReadOnly: bool) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Property::setIsReadOnly(bool
    isReadOnly)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-property.html#setIsReadOnly

    Parameters
    ----------

    isReadOnly : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Property::setIsReadOnly(bool isReadOnly)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData8Property13setIsReadOnlyEb', isReadOnly,
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
