"""
QV4::CompiledData::Object binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::CompiledData::Object to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class Object(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::CompiledData::Object: a plain Python object
  standing in front of one C++ QV4::CompiledData::Object.

  C++ hands a QV4::CompiledData::Object around as a copy, so every C++
  QV4::CompiledData::Object behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CompiledData::Object that has a ritual and that
  Python can call so far, 32 names in all: 'flags', 'hasFlag', 'setFlag',
  'setFlags', 'hasAliasAsDefaultProperty', 'setHasAliasAsDefaultProperty',
  'objectId', 'setObjectId', 'calculateSizeExcludingSignalsAndEnums',
  'propertyTable', 'aliasTable', 'bindingTable', 'enumAt', 'signalAt',
  'inlineComponentAt', 'inlineComponentTable', 'requiredPropertyExtraDataAt',
  'requiredPropertyExtraDataTable', 'propertyCount', 'aliasCount',
  'enumCount', 'signalCount', 'functionCount', 'inlineComponentCount',
  'bindingsBegin', 'bindingsEnd', 'bindingCount', 'propertiesBegin',
  'propertiesEnd', 'aliasesBegin', 'aliasesEnd',
  'namedObjectsInComponentCount'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const quint32_le *QV4::CompiledData::Object::functionOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
  - Qt's 'const quint32_le
    *QV4::CompiledData::Object::namedObjectsInComponentTable() const': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
  - Qt's 'EnumIterator QV4::CompiledData::Object::enumsBegin() const': gives
    a type Python has no way to take yet.
  - Qt's 'EnumIterator QV4::CompiledData::Object::enumsEnd() const': gives a
    type Python has no way to take yet.
  - Qt's 'SignalIterator QV4::CompiledData::Object::signalsBegin() const':
    gives a type Python has no way to take yet.
  - Qt's 'SignalIterator QV4::CompiledData::Object::signalsEnd() const':
    gives a type Python has no way to take yet.
  - Qt's 'InlineComponentIterator
    QV4::CompiledData::Object::inlineComponentsBegin() const': gives a type
    Python has no way to take yet.
  - Qt's 'InlineComponentIterator
    QV4::CompiledData::Object::inlineComponentsEnd() const': gives a type
    Python has no way to take yet.
  - Qt's 'RequiredPropertyExtraDataIterator
    QV4::CompiledData::Object::requiredPropertyExtraDataBegin() const': gives
    a type Python has no way to take yet.
  - Qt's 'RequiredPropertyExtraDataIterator
    QV4::CompiledData::Object::requiredPropertyExtraDataEnd() const': gives a
    type Python has no way to take yet.
  - Qt's 'QV4::CompiledData::Object::~Object()': the destructor: Python
    removes its C++ QV4::CompiledData::Object by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QV4::CompiledData::Object is created at the first use, not by
    'QV4::CompiledData::Object(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CompiledData::Object back gives a copy the
    ritual made for Python, in a new cute QV4::CompiledData::Object.
  - Each name of Qt's QV4::CompiledData::Object that has no cute function
    yet, 'enumsBegin', 'enumsEnd', 'functionOffsetTable',
    'inlineComponentsBegin', 'inlineComponentsEnd',
    'namedObjectsInComponentTable', 'requiredPropertyExtraDataBegin',
    'requiredPropertyExtraDataEnd', 'signalsBegin', 'signalsEnd', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QV4::CompiledData::Object, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QV4::CompiledData::Object::Flag' of Qt, with the 6 names
    Qt gives in it. Qt names the type of its combinations
    'QV4::CompiledData::Object::Flags'.
    """

    NoFlag = 0x0
    IsComponent = 0x1
    HasDeferredBindings = 0x2
    HasCustomParserBindings = 0x4
    IsInlineComponentRoot = 0x8
    IsPartOfInlineComponent = 0x10

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int, int, int, int, int, int, int, int, int)
  def calculateSizeExcludingSignalsAndEnums(
      nFunctions: int,
      nProperties: int,
      nAliases: int,
      nEnums: int,
      nSignals: int,
      nBindings: int,
      nNamedObjectsInComponent: int,
      nInlineComponents: int,
      nRequiredPropertyExtraData: int,
  ) -> int:
    """
    Calls Qt's 'int
    QV4::CompiledData::Object::calculateSizeExcludingSignalsAndEnums(int
    nFunctions, int nProperties, int nAliases, int nEnums, int nSignals, int
    nBindings, int nNamedObjectsInComponent, int nInlineComponents, int
    nRequiredPropertyExtraData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html

    Parameters
    ----------

    nFunctions : int
      Passed on as it is.

    nProperties : int
      Passed on as it is.

    nAliases : int
      Passed on as it is.

    nEnums : int
      Passed on as it is.

    nSignals : int
      Passed on as it is.

    nBindings : int
      Passed on as it is.

    nNamedObjectsInComponent : int
      Passed on as it is.

    nInlineComponents : int
      Passed on as it is.

    nRequiredPropertyExtraData : int
      Passed on as it is.
    """
    #  int QV4::CompiledData::Object::calculateSizeExcludingSignalsAndEnums(
    #      int nFunctions, int nProperties, int nAliases, int nEnums, int
    #      nSignals, int nBindings, int nNamedObjectsInComponent, int
    #      nInlineComponents, int nRequiredPropertyExtraData)
    return Rituals.call(
        'ritual_ZN3QV412CompiledData6Object37calculateSizeExcludingSignalsA'
        'ndEnumsEiiiiiiiii',
        nFunctions, nProperties, nAliases, nEnums, nSignals, nBindings,
        nNamedObjectsInComponent, nInlineComponents,
        nRequiredPropertyExtraData,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CompiledData::Object'

  #  Qt's '~QV4::CompiledData::Object()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::CompiledData::Object behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412CompiledData6ObjectD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QV4::CompiledData::Object::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-compileddata-object.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QV4::CompiledData::Object::flags() const
    return Object.Flags(self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object5flagsEv',
    ))

  @overload(Flag)
  def hasFlag(self, flag: Flag) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Object::hasFlag(Flag flag) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#hasFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.
    """
    #  bool QV4::CompiledData::Object::hasFlag(Flag flag) const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object7hasFlagENS1_4FlagE', flag.value,
    )

  def hasAliasAsDefaultProperty(self) -> bool:
    """
    Calls Qt's 'bool QV4::CompiledData::Object::hasAliasAsDefaultProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html
    """
    #  bool QV4::CompiledData::Object::hasAliasAsDefaultProperty() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object25hasAliasAsDefaultPropertyEv',
    )

  def objectId(self) -> int:
    """
    Calls Qt's 'qint32 QV4::CompiledData::Object::objectId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#objectId
    """
    #  qint32 QV4::CompiledData::Object::objectId() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object8objectIdEv',
    )

  def propertyTable(self) -> Optional[QV4.CompiledData.Property]:
    """
    Calls Qt's 'const Property *QV4::CompiledData::Object::propertyTable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#propertyTable

    Returns
    -------

    Optional[QV4.CompiledData.Property]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Property *QV4::CompiledData::Object::propertyTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object13propertyTableEv',
    )
    return QV4.CompiledData.Property._cuteAt(address)

  def aliasTable(self) -> Optional[QV4.CompiledData.Alias]:
    """
    Calls Qt's 'const Alias *QV4::CompiledData::Object::aliasTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#aliasTable

    Returns
    -------

    Optional[QV4.CompiledData.Alias]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Alias *QV4::CompiledData::Object::aliasTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object10aliasTableEv',
    )
    return QV4.CompiledData.Alias._cuteAt(address)

  def bindingTable(self) -> Optional[QV4.CompiledData.Binding]:
    """
    Calls Qt's 'const Binding *QV4::CompiledData::Object::bindingTable()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#bindingTable

    Returns
    -------

    Optional[QV4.CompiledData.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Binding *QV4::CompiledData::Object::bindingTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object12bindingTableEv',
    )
    return QV4.CompiledData.Binding._cuteAt(address)

  @overload(int)
  def enumAt(self, idx: int) -> Optional[QV4.CompiledData.Enum]:
    """
    Calls Qt's 'const Enum *QV4::CompiledData::Object::enumAt(int idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#enumAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Enum]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Enum *QV4::CompiledData::Object::enumAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object6enumAtEi', idx,
    )
    return QV4.CompiledData.Enum._cuteAt(address)

  @overload(int)
  def signalAt(self, idx: int) -> Optional[QV4.CompiledData.Signal]:
    """
    Calls Qt's 'const Signal *QV4::CompiledData::Object::signalAt(int idx)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#signalAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.Signal]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Signal *QV4::CompiledData::Object::signalAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object8signalAtEi', idx,
    )
    return QV4.CompiledData.Signal._cuteAt(address)

  @overload(int)
  def inlineComponentAt(
      self,
      idx: int,
  ) -> Optional[QV4.CompiledData.InlineComponent]:
    """
    Calls Qt's 'const InlineComponent
    *QV4::CompiledData::Object::inlineComponentAt(int idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#inlineComponentAt

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.InlineComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const InlineComponent
    #      *QV4::CompiledData::Object::inlineComponentAt(int idx) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object17inlineComponentAtEi', idx,
    )
    return QV4.CompiledData.InlineComponent._cuteAt(address)

  def inlineComponentTable(
      self,
  ) -> Optional[QV4.CompiledData.InlineComponent]:
    """
    Calls Qt's 'const InlineComponent
    *QV4::CompiledData::Object::inlineComponentTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#inlineComponentTable

    Returns
    -------

    Optional[QV4.CompiledData.InlineComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const InlineComponent
    #      *QV4::CompiledData::Object::inlineComponentTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object20inlineComponentTableEv',
    )
    return QV4.CompiledData.InlineComponent._cuteAt(address)

  @overload(int)
  def requiredPropertyExtraDataAt(
      self,
      idx: int,
  ) -> Optional[QV4.CompiledData.RequiredPropertyExtraData]:
    """
    Calls Qt's 'const RequiredPropertyExtraData
    *QV4::CompiledData::Object::requiredPropertyExtraDataAt(int idx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html

    Parameters
    ----------

    idx : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.CompiledData.RequiredPropertyExtraData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const RequiredPropertyExtraData
    #      *QV4::CompiledData::Object::requiredPropertyExtraDataAt(int idx)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object27requiredPropertyExtraDataAtEi',
        idx,
    )
    return QV4.CompiledData.RequiredPropertyExtraData._cuteAt(address)

  def requiredPropertyExtraDataTable(
      self,
  ) -> Optional[QV4.CompiledData.RequiredPropertyExtraData]:
    """
    Calls Qt's 'const RequiredPropertyExtraData
    *QV4::CompiledData::Object::requiredPropertyExtraDataTable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html

    Returns
    -------

    Optional[QV4.CompiledData.RequiredPropertyExtraData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const RequiredPropertyExtraData
    #      *QV4::CompiledData::Object::requiredPropertyExtraDataTable() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object30requiredPropertyExtraDataTabl'
        'eEv',
    )
    return QV4.CompiledData.RequiredPropertyExtraData._cuteAt(address)

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::propertyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#propertyCount
    """
    #  int QV4::CompiledData::Object::propertyCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object13propertyCountEv',
    )

  def aliasCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::aliasCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#aliasCount
    """
    #  int QV4::CompiledData::Object::aliasCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object10aliasCountEv',
    )

  def enumCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::enumCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#enumCount
    """
    #  int QV4::CompiledData::Object::enumCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object9enumCountEv',
    )

  def signalCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::signalCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#signalCount
    """
    #  int QV4::CompiledData::Object::signalCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object11signalCountEv',
    )

  def functionCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::functionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#functionCount
    """
    #  int QV4::CompiledData::Object::functionCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object13functionCountEv',
    )

  def inlineComponentCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::inlineComponentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#inlineComponentCount
    """
    #  int QV4::CompiledData::Object::inlineComponentCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object20inlineComponentCountEv',
    )

  def bindingsBegin(self) -> Optional[QV4.CompiledData.Binding]:
    """
    Calls Qt's 'const Binding *QV4::CompiledData::Object::bindingsBegin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#bindingsBegin

    Returns
    -------

    Optional[QV4.CompiledData.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Binding *QV4::CompiledData::Object::bindingsBegin() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object13bindingsBeginEv',
    )
    return QV4.CompiledData.Binding._cuteAt(address)

  def bindingsEnd(self) -> Optional[QV4.CompiledData.Binding]:
    """
    Calls Qt's 'const Binding *QV4::CompiledData::Object::bindingsEnd()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#bindingsEnd

    Returns
    -------

    Optional[QV4.CompiledData.Binding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Binding *QV4::CompiledData::Object::bindingsEnd() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object11bindingsEndEv',
    )
    return QV4.CompiledData.Binding._cuteAt(address)

  def bindingCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::bindingCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#bindingCount
    """
    #  int QV4::CompiledData::Object::bindingCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object12bindingCountEv',
    )

  def propertiesBegin(self) -> Optional[QV4.CompiledData.Property]:
    """
    Calls Qt's 'const Property *QV4::CompiledData::Object::propertiesBegin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#propertiesBegin

    Returns
    -------

    Optional[QV4.CompiledData.Property]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Property *QV4::CompiledData::Object::propertiesBegin() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object15propertiesBeginEv',
    )
    return QV4.CompiledData.Property._cuteAt(address)

  def propertiesEnd(self) -> Optional[QV4.CompiledData.Property]:
    """
    Calls Qt's 'const Property *QV4::CompiledData::Object::propertiesEnd()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#propertiesEnd

    Returns
    -------

    Optional[QV4.CompiledData.Property]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Property *QV4::CompiledData::Object::propertiesEnd() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object13propertiesEndEv',
    )
    return QV4.CompiledData.Property._cuteAt(address)

  def aliasesBegin(self) -> Optional[QV4.CompiledData.Alias]:
    """
    Calls Qt's 'const Alias *QV4::CompiledData::Object::aliasesBegin()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#aliasesBegin

    Returns
    -------

    Optional[QV4.CompiledData.Alias]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Alias *QV4::CompiledData::Object::aliasesBegin() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object12aliasesBeginEv',
    )
    return QV4.CompiledData.Alias._cuteAt(address)

  def aliasesEnd(self) -> Optional[QV4.CompiledData.Alias]:
    """
    Calls Qt's 'const Alias *QV4::CompiledData::Object::aliasesEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#aliasesEnd

    Returns
    -------

    Optional[QV4.CompiledData.Alias]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Alias *QV4::CompiledData::Object::aliasesEnd() const
    address = self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object10aliasesEndEv',
    )
    return QV4.CompiledData.Alias._cuteAt(address)

  def namedObjectsInComponentCount(self) -> int:
    """
    Calls Qt's 'int QV4::CompiledData::Object::namedObjectsInComponentCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html
    """
    #  int QV4::CompiledData::Object::namedObjectsInComponentCount() const
    return self.uglySide.call(
        'ritual_ZNK3QV412CompiledData6Object28namedObjectsInComponentCountE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flag)
  def setFlag(self, flag: Flag) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Object::setFlag(Flag flag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#setFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.
    """
    #  void QV4::CompiledData::Object::setFlag(Flag flag)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData6Object7setFlagENS1_4FlagE', flag.value,
    )

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Object::setFlags(Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QV4::CompiledData::Object::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData6Object8setFlagsE6QFlagsINS1_4FlagEE',
        flags.value,
    )

  @overload(bool)
  def setHasAliasAsDefaultProperty(self, defaultAlias: bool) -> None:
    """
    Calls Qt's 'void
    QV4::CompiledData::Object::setHasAliasAsDefaultProperty(bool
    defaultAlias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html

    Parameters
    ----------

    defaultAlias : bool
      Passed on as it is.
    """
    #  void QV4::CompiledData::Object::setHasAliasAsDefaultProperty(bool
    #      defaultAlias)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData6Object28setHasAliasAsDefaultPropertyEb',
        defaultAlias,
    )

  @overload(int)
  def setObjectId(self, id: int) -> None:
    """
    Calls Qt's 'void QV4::CompiledData::Object::setObjectId(qint32 id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-compileddata-object.html#setObjectId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QV4::CompiledData::Object::setObjectId(qint32 id)
    self.uglySide.call(
        'ritual_ZN3QV412CompiledData6Object11setObjectIdEi', id,
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

  @staticmethod
  def enumsBegin(*__, **_) -> Never:
    """
    Qt's 'EnumIterator QV4::CompiledData::Object::enumsBegin() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.enumsBegin' has no cute function yet. "
        "Qt's 'EnumIterator QV4::CompiledData::Object::enumsBegin() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def enumsEnd(*__, **_) -> Never:
    """
    Qt's 'EnumIterator QV4::CompiledData::Object::enumsEnd() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.enumsEnd' has no cute function yet. Qt's "
        "'EnumIterator QV4::CompiledData::Object::enumsEnd() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def functionOffsetTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le *QV4::CompiledData::Object::functionOffsetTable()
    const': gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.functionOffsetTable' has no cute function "
        "yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Object::functionOffsetTable() const': gives "
        "'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which "
        "has no cute class yet.")

  @staticmethod
  def inlineComponentsBegin(*__, **_) -> Never:
    """
    Qt's 'InlineComponentIterator
    QV4::CompiledData::Object::inlineComponentsBegin() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.inlineComponentsBegin' has no cute "
        "function yet. Qt's 'InlineComponentIterator "
        "QV4::CompiledData::Object::inlineComponentsBegin() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def inlineComponentsEnd(*__, **_) -> Never:
    """
    Qt's 'InlineComponentIterator
    QV4::CompiledData::Object::inlineComponentsEnd() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.inlineComponentsEnd' has no cute function "
        "yet. Qt's 'InlineComponentIterator "
        "QV4::CompiledData::Object::inlineComponentsEnd() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def namedObjectsInComponentTable(*__, **_) -> Never:
    """
    Qt's 'const quint32_le
    *QV4::CompiledData::Object::namedObjectsInComponentTable() const': gives
    'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.namedObjectsInComponentTable' has no cute "
        "function yet. Qt's 'const quint32_le "
        "*QV4::CompiledData::Object::namedObjectsInComponentTable() const': "
        "gives 'QSpecialInteger<QLittleEndianStorageType<unsigned int>>', "
        "which has no cute class yet.")

  @staticmethod
  def requiredPropertyExtraDataBegin(*__, **_) -> Never:
    """
    Qt's 'RequiredPropertyExtraDataIterator
    QV4::CompiledData::Object::requiredPropertyExtraDataBegin() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.requiredPropertyExtraDataBegin' has no "
        "cute function yet. Qt's 'RequiredPropertyExtraDataIterator "
        "QV4::CompiledData::Object::requiredPropertyExtraDataBegin() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def requiredPropertyExtraDataEnd(*__, **_) -> Never:
    """
    Qt's 'RequiredPropertyExtraDataIterator
    QV4::CompiledData::Object::requiredPropertyExtraDataEnd() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.requiredPropertyExtraDataEnd' has no cute "
        "function yet. Qt's 'RequiredPropertyExtraDataIterator "
        "QV4::CompiledData::Object::requiredPropertyExtraDataEnd() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def signalsBegin(*__, **_) -> Never:
    """
    Qt's 'SignalIterator QV4::CompiledData::Object::signalsBegin() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.signalsBegin' has no cute function yet. "
        "Qt's 'SignalIterator QV4::CompiledData::Object::signalsBegin() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def signalsEnd(*__, **_) -> Never:
    """
    Qt's 'SignalIterator QV4::CompiledData::Object::signalsEnd() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.CompiledData.Object.signalsEnd' has no cute function yet. "
        "Qt's 'SignalIterator QV4::CompiledData::Object::signalsEnd() "
        "const': gives a type Python has no way to take yet.")
