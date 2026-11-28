"""
QV4::CompiledData::Unit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Unit to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Unit(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Unit: a plain Python object
  standing in front of one C++ QV4::CompiledData::Unit.

  C++ hands a QV4::CompiledData::Unit around as a copy, so every C++
  QV4::CompiledData::Unit behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Unit that has a ritual and that
  Python can call so far, 17 names in all: 'qmlUnit', 'isSingleton',
  'isListPropertyAssignReplace', 'isListPropertyAssignReplaceIfNotDefault',
  'stringAtInternal', 'functionAt', 'classAt', 'templateObjectAt', 'blockAt',
  'lookupTable', 'regexpAt', 'translations', 'importEntryTable',
  'localExportEntryTable', 'indirectExportEntryTable',
  'starExportEntryTable', 'verifyHeader'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlUnit *QV4::CompiledData::Unit::qmlUnit()': takes in Python what
    'const QmlUnit *QV4::CompiledData::Unit::qmlUnit() const' takes.
  - Qt's 'const quint32_le *QV4::CompiledData::Unit::functionOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'const quint32_le *QV4::CompiledData::Unit::classOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'const quint32_le
    *QV4::CompiledData::Unit::templateObjectOffsetTable() const': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
  - Qt's 'const quint32_le *QV4::CompiledData::Unit::blockOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'const quint64_le *QV4::CompiledData::Unit::constants() const':
    gives 'QSpecialInteger<QLittleEndianStorageType<unsigned long long>>',
    which has no cute class yet.
  - Qt's 'const JSClassMember *QV4::CompiledData::Unit::jsClassAt(int idx,
    int *nMembers) const': takes a number to change where it is.
  - Qt's 'const quint32_le
    *QV4::CompiledData::Unit::translationContextIndex() const': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
  - Qt's 'quint32_le *QV4::CompiledData::Unit::translationContextIndex()':
    gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which
    has no cute class yet.
  - Qt's 'const quint32_le *QV4::CompiledData::Unit::moduleRequestTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'QV4::CompiledData::Unit::~Unit()': the destructor: Python removes
    its C++ QV4::CompiledData::Unit by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Unit is created at the first use, not by
    'QV4::CompiledData::Unit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Unit back gives a copy the ritual
    made for Python, in a new cute QV4::CompiledData::Unit.
  - Each name of Qt's QV4::CompiledData::Unit that has no cute function yet,
    'blockOffsetTable', 'classOffsetTable', 'constants',
    'functionOffsetTable', 'jsClassAt', 'moduleRequestTable',
    'templateObjectOffsetTable', 'translationContextIndex', holds a function
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
  __qt_class__ = 'QV4::CompiledData::Unit'

  #  Qt's '~QV4::CompiledData::Unit()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::Unit behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData4UnitD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def qmlUnit(self) -> Optional[QV4.CompiledData.QmlUnit]:
    """
    Calls Qt's 'const QmlUnit *QV4::CompiledData::Unit::qmlUnit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-unit.html#qmlUnit

    Returns
    -------

    Optional[QV4.CompiledData.QmlUnit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QmlUnit *QV4::CompiledData::Unit::qmlUnit() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit7qmlUnitEv',
    )
    return QV4.CompiledData.QmlUnit._cuteAt(address)

  def isSingleton(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Unit::isSingleton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#isSingleton
    """
    #  bool QV4::CompiledData::Unit::isSingleton() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit11isSingletonEv',
    )

  def isListPropertyAssignReplace(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Unit::isListPropertyAssignReplace()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html
    """
    #  bool QV4::CompiledData::Unit::isListPropertyAssignReplace() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit27isListPropertyAssignReplaceEv',
    )

  def isListPropertyAssignReplaceIfNotDefault(self) -> bool:
    """
    Calls Qt's 'bool
    QV4::CompiledData::Unit::isListPropertyAssignReplaceIfNotDefault()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html
    """
    #  bool
    #      QV4::CompiledData::Unit::isListPropertyAssignReplaceIfNotDefault()
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit39isListPropertyAssignReplaceIfNo'
        'tDefaultEv',
    )

  @overload(int)
  def stringAtInternal(self, idx: int) -> str:
    """
    Calls Qt's 'QString QV4::CompiledData::Unit::stringAtInternal(uint idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#stringAtInternal

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CompiledData::Unit::stringAtInternal(uint idx) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit16stringAtInternalEj', idx,
    )

  @overload(int)
  def functionAt(self, idx: int) -> Optional[QV4.CompiledData.Function]:
    """
    Calls Qt's 'const Function *QV4::CompiledData::Unit::functionAt(int idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#functionAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Function *QV4::CompiledData::Unit::functionAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit10functionAtEi', idx,
    )
    return QV4.CompiledData.Function._cuteAt(address)

  @overload(int)
  def classAt(self, idx: int) -> Optional[QV4.CompiledData.Class]:
    """
    Calls Qt's 'const Class *QV4::CompiledData::Unit::classAt(int idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-unit.html#classAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Class]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Class *QV4::CompiledData::Unit::classAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit7classAtEi', idx,
    )
    return QV4.CompiledData.Class._cuteAt(address)

  @overload(int)
  def templateObjectAt(
      self,
      idx: int,
  ) -> Optional[QV4.CompiledData.TemplateObject]:
    """
    Calls Qt's 'const TemplateObject
    *QV4::CompiledData::Unit::templateObjectAt(int idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#templateObjectAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.TemplateObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const TemplateObject *QV4::CompiledData::Unit::templateObjectAt(int
    #      idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit16templateObjectAtEi', idx,
    )
    return QV4.CompiledData.TemplateObject._cuteAt(address)

  @overload(int)
  def blockAt(self, idx: int) -> Optional[QV4.CompiledData.Block]:
    """
    Calls Qt's 'const Block *QV4::CompiledData::Unit::blockAt(int idx)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-unit.html#blockAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Block]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Block *QV4::CompiledData::Unit::blockAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit7blockAtEi', idx,
    )
    return QV4.CompiledData.Block._cuteAt(address)

  def lookupTable(self) -> Optional[QV4.CompiledData.Lookup]:
    """
    Calls Qt's 'const Lookup *QV4::CompiledData::Unit::lookupTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#lookupTable

    Returns
    -------

    Optional[QV4.CompiledData.Lookup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Lookup *QV4::CompiledData::Unit::lookupTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit11lookupTableEv',
    )
    return QV4.CompiledData.Lookup._cuteAt(address)

  @overload(int)
  def regexpAt(self, index: int) -> Optional[QV4.CompiledData.RegExp]:
    """
    Calls Qt's 'const RegExp *QV4::CompiledData::Unit::regexpAt(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#regexpAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.RegExp]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const RegExp *QV4::CompiledData::Unit::regexpAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit8regexpAtEi', index,
    )
    return QV4.CompiledData.RegExp._cuteAt(address)

  def translations(self) -> Optional[QV4.CompiledData.TranslationData]:
    """
    Calls Qt's 'const TranslationData
    *QV4::CompiledData::Unit::translations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#translations

    Returns
    -------

    Optional[QV4.CompiledData.TranslationData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const TranslationData *QV4::CompiledData::Unit::translations() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit12translationsEv',
    )
    return QV4.CompiledData.TranslationData._cuteAt(address)

  def importEntryTable(self) -> Optional[QV4.CompiledData.ImportEntry]:
    """
    Calls Qt's 'const ImportEntry
    *QV4::CompiledData::Unit::importEntryTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#importEntryTable

    Returns
    -------

    Optional[QV4.CompiledData.ImportEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ImportEntry *QV4::CompiledData::Unit::importEntryTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit16importEntryTableEv',
    )
    return QV4.CompiledData.ImportEntry._cuteAt(address)

  def localExportEntryTable(self) -> Optional[QV4.CompiledData.ExportEntry]:
    """
    Calls Qt's 'const ExportEntry
    *QV4::CompiledData::Unit::localExportEntryTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#localExportEntryTable

    Returns
    -------

    Optional[QV4.CompiledData.ExportEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ExportEntry *QV4::CompiledData::Unit::localExportEntryTable()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit21localExportEntryTableEv',
    )
    return QV4.CompiledData.ExportEntry._cuteAt(address)

  def indirectExportEntryTable(
      self,
  ) -> Optional[QV4.CompiledData.ExportEntry]:
    """
    Calls Qt's 'const ExportEntry
    *QV4::CompiledData::Unit::indirectExportEntryTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html

    Returns
    -------

    Optional[QV4.CompiledData.ExportEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ExportEntry *QV4::CompiledData::Unit::indirectExportEntryTable()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit24indirectExportEntryTableEv',
    )
    return QV4.CompiledData.ExportEntry._cuteAt(address)

  def starExportEntryTable(self) -> Optional[QV4.CompiledData.ExportEntry]:
    """
    Calls Qt's 'const ExportEntry
    *QV4::CompiledData::Unit::starExportEntryTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#starExportEntryTable

    Returns
    -------

    Optional[QV4.CompiledData.ExportEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ExportEntry *QV4::CompiledData::Unit::starExportEntryTable()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit20starExportEntryTableEv',
    )
    return QV4.CompiledData.ExportEntry._cuteAt(address)

  @overload(QDateTime, QString)
  @overload(QDateTime, NoneType)
  def verifyHeader(
      self,
      expectedSourceTimeStamp: QDateTime,
      errorString: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Unit::verifyHeader(QDateTime
    expectedSourceTimeStamp, QString *errorString) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-unit.html#verifyHeader

    Parameters
    ----------

    expectedSourceTimeStamp : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    errorString : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::CompiledData::Unit::verifyHeader(QDateTime
    #      expectedSourceTimeStamp, QString *errorString) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData4Unit12verifyHeaderE9QDateTimeP7QStrin'
        'g',
        self._valueOf(expectedSourceTimeStamp), self._addressOf(errorString),
    )

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

  @staticmethod
  def blockOffsetTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Unit::blockOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.blockOffsetTable' has no cute function yet. "
        "Qt's 'const quint32_le "
        "*QV4::CompiledData::Unit::blockOffsetTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")

  @staticmethod
  def classOffsetTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Unit::classOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.classOffsetTable' has no cute function yet. "
        "Qt's 'const quint32_le "
        "*QV4::CompiledData::Unit::classOffsetTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")

  @staticmethod
  def constants(*__, **_) -> Never:
    """
    Qt's 'const quint64_le *QV4::CompiledData::Unit::constants() const':
    gives 'QSpecialInteger<QLittleEndianStorageType<unsigned long long>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.constants' has no cute function yet. Qt's "
        "'const quint64_le *QV4::CompiledData::Unit::constants() const': "
        "gives 'QSpecialInteger<QLittleEndianStorageType<unsigned long "
        "long>>', which has no cute class yet.")

  @staticmethod
  def functionOffsetTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Unit::functionOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.functionOffsetTable' has no cute function "
        "yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Unit::functionOffsetTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")

  @staticmethod
  def jsClassAt(*__, **_) -> Never:
    """
    Qt's 'const JSClassMember *QV4::CompiledData::Unit::jsClassAt(int idx,
    int *nMembers) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.jsClassAt' has no cute function yet. Qt's "
        "'const JSClassMember *QV4::CompiledData::Unit::jsClassAt(int idx, "
        "int *nMembers) const': takes a number to change where it is.")

  @staticmethod
  def moduleRequestTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Unit::moduleRequestTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.moduleRequestTable' has no cute function "
        "yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Unit::moduleRequestTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")

  @staticmethod
  def templateObjectOffsetTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le
    *QV4::CompiledData::Unit::templateObjectOffsetTable() const': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.templateObjectOffsetTable' has no cute "
        "function yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Unit::templateObjectOffsetTable() const': "
        "gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', "
        "which has no cute class yet.")

  @staticmethod
  def translationContextIndex(*__, **_) -> Never:
    """
    - Qt's 'const quint32_le
      *QV4::CompiledData::Unit::translationContextIndex() const': gives
      'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
      cute class yet.
    - Qt's 'quint32_le *QV4::CompiledData::Unit::translationContextIndex()':
      gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Unit.translationContextIndex' has no cute "
        "function yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Unit::translationContextIndex() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet. Qt's 'quint32_le "
        "*QV4::CompiledData::Unit::translationContextIndex()': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")
