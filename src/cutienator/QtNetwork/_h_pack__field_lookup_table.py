"""
HPack::FieldLookupTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/hpacktable_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means HPack::FieldLookupTable to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import HPack

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FieldLookupTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's HPack::FieldLookupTable: a plain Python object
  standing in front of one C++ HPack::FieldLookupTable.

  What exists
  -----------

  Every function of Qt's HPack::FieldLookupTable that has a ritual and that
  Python can call so far, 15 names in all: 'numberOfEntries',
  'numberOfStaticEntries', 'numberOfDynamicEntries', 'dynamicDataSize',
  'dynamicDataCapacity', 'maxDynamicDataCapacity', 'clearDynamicTable',
  'indexIsValid', 'indexOf', 'field', 'fieldName', 'fieldValue',
  'setMaxDynamicTableSize', 'front', 'back'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const std::vector<HeaderField>
    &HPack::FieldLookupTable::staticPart()': gives a type Python has no way
    to take yet.
  - Qt's 'SearchEntry HPack::FieldLookupTable::frontKey() const': gives a
    type Python has no way to take yet.
  - Qt's 'SearchEntry HPack::FieldLookupTable::backKey() const': gives a type
    Python has no way to take yet.
  - Qt's 'HeaderField &HPack::FieldLookupTable::front()': gives a type Python
    has no way to take yet.
  - Qt's 'quint32 HPack::FieldLookupTable::indexOfChunk(const Chunk *chunk)
    const': names 'HPack::FieldLookupTable::Chunk', which has no cute class
    yet.
  - Qt's 'quint32 HPack::FieldLookupTable::keyToIndex(const SearchEntry &key)
    const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 32 functions Qt declares: 4 forbidden; 3 leans on 'HPack; 1 not a
  gap; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ HPack::FieldLookupTable is created at the first use, not by
    'HPack::FieldLookupTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ HPack::FieldLookupTable.
  - Each name of Qt's HPack::FieldLookupTable that has no cute function yet,
    'backKey', 'evictEntry', 'findInStaticPart', 'frontKey', 'indexOfChunk',
    'keyToIndex', 'prependField', 'staticPart', 'updateDynamicTableSize',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'HPack::FieldLookupTable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def numberOfEntries(self) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::numberOfEntries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#numberOfEntries
    """
    #  quint32 HPack::FieldLookupTable::numberOfEntries() const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable15numberOfEntriesEv',
    )

  def numberOfStaticEntries(self) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::numberOfStaticEntries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#numberOfStaticEntries
    """
    #  quint32 HPack::FieldLookupTable::numberOfStaticEntries() const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable21numberOfStaticEntriesEv',
    )

  def numberOfDynamicEntries(self) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::numberOfDynamicEntries()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#numberOfDynamicEntries
    """
    #  quint32 HPack::FieldLookupTable::numberOfDynamicEntries() const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable22numberOfDynamicEntriesEv',
    )

  def dynamicDataSize(self) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::dynamicDataSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#dynamicDataSize
    """
    #  quint32 HPack::FieldLookupTable::dynamicDataSize() const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable15dynamicDataSizeEv',
    )

  def dynamicDataCapacity(self) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::dynamicDataCapacity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#dynamicDataCapacity
    """
    #  quint32 HPack::FieldLookupTable::dynamicDataCapacity() const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable19dynamicDataCapacityEv',
    )

  def maxDynamicDataCapacity(self) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::maxDynamicDataCapacity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#maxDynamicDataCapacity
    """
    #  quint32 HPack::FieldLookupTable::maxDynamicDataCapacity() const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable22maxDynamicDataCapacityEv',
    )

  @overload(int)
  def indexIsValid(self, index: int) -> bool:
    """
    Calls Qt's 'bool HPack::FieldLookupTable::indexIsValid(quint32 index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#indexIsValid

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool HPack::FieldLookupTable::indexIsValid(quint32 index) const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable12indexIsValidEj', index,
    )

  @overload(QByteArray, QByteArray)
  def indexOf(self, name: QByteArray, value: QByteArray) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::indexOf(const QByteArray
    &name, const QByteArray &value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#indexOf

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  quint32 HPack::FieldLookupTable::indexOf(const QByteArray &name, const
    #      QByteArray &value) const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable7indexOfERK10QByteArrayS3_',
        self._valueOf(name), self._valueOf(value),
    )

  @overload(QByteArray)
  def indexOf(self, name: QByteArray) -> int:
    """
    Calls Qt's 'quint32 HPack::FieldLookupTable::indexOf(const QByteArray
    &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#indexOf

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  quint32 HPack::FieldLookupTable::indexOf(const QByteArray &name) const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable7indexOfERK10QByteArray',
        self._valueOf(name),
    )

  @overload(int, QByteArray, QByteArray)
  @overload(int, QByteArray, NoneType)
  @overload(int, NoneType, QByteArray)
  @overload(int, NoneType, NoneType)
  def field(
      self,
      index: int,
      name: Optional[QByteArray],
      value: Optional[QByteArray],
  ) -> bool:
    """
    Calls Qt's 'bool HPack::FieldLookupTable::field(quint32 index, QByteArray
    *name, QByteArray *value) const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#field

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool HPack::FieldLookupTable::field(quint32 index, QByteArray *name,
    #      QByteArray *value) const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable5fieldEjP10QByteArrayS2_',
        index, self._addressOf(name), self._addressOf(value),
    )

  @overload(int, QByteArray)
  @overload(int, NoneType)
  def fieldName(self, index: int, dst: Optional[QByteArray]) -> bool:
    """
    Calls Qt's 'bool HPack::FieldLookupTable::fieldName(quint32 index,
    QByteArray *dst) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#fieldName

    Parameters
    ----------

    index : int
      Passed on as it is.

    dst : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool HPack::FieldLookupTable::fieldName(quint32 index, QByteArray
    #      *dst) const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable9fieldNameEjP10QByteArray',
        index, self._addressOf(dst),
    )

  @overload(int, QByteArray)
  @overload(int, NoneType)
  def fieldValue(self, index: int, dst: Optional[QByteArray]) -> bool:
    """
    Calls Qt's 'bool HPack::FieldLookupTable::fieldValue(quint32 index,
    QByteArray *dst) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#fieldValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    dst : Optional[QByteArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool HPack::FieldLookupTable::fieldValue(quint32 index, QByteArray
    #      *dst) const
    return self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable10fieldValueEjP10QByteArray',
        index, self._addressOf(dst),
    )

  def front(self) -> HPack.HeaderField:
    """
    Calls Qt's 'const HeaderField &HPack::FieldLookupTable::front() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#front

    Returns
    -------

    HPack.HeaderField
      A new cute HPack::HeaderField around the copy Qt gave back. Python owns
      it.
    """
    #  const HeaderField &HPack::FieldLookupTable::front() const
    address = self.uglySide.call(
        'ritual_ZNK5HPack16FieldLookupTable5frontEv',
    )
    return HPack.HeaderField._cuteOwning(address)

  def back(self) -> HPack.HeaderField:
    """
    Calls Qt's 'const HeaderField &HPack::FieldLookupTable::back() const'.

    Qt's own words: https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#back

    Returns
    -------

    HPack.HeaderField
      A new cute HPack::HeaderField around the copy Qt gave back. Python owns
      it.
    """
    #  const HeaderField &HPack::FieldLookupTable::back() const
    address = self.uglySide.call('ritual_ZNK5HPack16FieldLookupTable4backEv')
    return HPack.HeaderField._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMaxDynamicTableSize(self, size: int) -> None:
    """
    Calls Qt's 'void HPack::FieldLookupTable::setMaxDynamicTableSize(quint32
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#setMaxDynamicTableSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void HPack::FieldLookupTable::setMaxDynamicTableSize(quint32 size)
    self.uglySide.call(
        'ritual_ZN5HPack16FieldLookupTable22setMaxDynamicTableSizeEj', size,
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

  @overload(int, bool)
  def __init__(self, maxTableSize: int, useIndex: bool) -> None:
    """
    Notes what was given, for Qt's
    'HPack::FieldLookupTable::FieldLookupTable(quint32 maxTableSize, bool
    useIndex)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#FieldLookupTable

    Parameters
    ----------

    maxTableSize : int
      Passed on as it is.

    useIndex : bool
      Passed on as it is.
    """
    #  HPack::FieldLookupTable::FieldLookupTable(quint32 maxTableSize, bool
    #      useIndex)
    self._noteCreation(FieldLookupTable, lambda: Rituals.call(
        'ritual_ZN5HPack16FieldLookupTableC1Ejb', maxTableSize, useIndex,
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

  def clearDynamicTable(self) -> None:
    """
    Calls Qt's 'void HPack::FieldLookupTable::clearDynamicTable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/hpack-fieldlookuptable.html#clearDynamicTable
    """
    #  void HPack::FieldLookupTable::clearDynamicTable()
    self.uglySide.call(
        'ritual_ZN5HPack16FieldLookupTable17clearDynamicTableEv',
    )

  @staticmethod
  def backKey(*__, **_) -> Never:
    """
    Qt's 'SearchEntry HPack::FieldLookupTable::backKey() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.backKey' has no cute function yet. Qt's "
        "'SearchEntry HPack::FieldLookupTable::backKey() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def evictEntry(*__, **_) -> Never:
    """
    Qt's 'void HPack::FieldLookupTable::evictEntry()': leans on
    'HPack::entry_size(QByteArrayView, QByteArrayView)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.evictEntry' has no cute function yet. Qt's "
        "'void HPack::FieldLookupTable::evictEntry()': leans on "
        "'HPack::entry_size(QByteArrayView, QByteArrayView)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def findInStaticPart(*__, **_) -> Never:
    """
    Qt's 'std::vector<HeaderField>::const_iterator
    HPack::FieldLookupTable::findInStaticPart(const HeaderField &field,
    CompareMode mode)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'compare'; did you mean 'QOperatingSystemVersionBase::compare'?.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.findInStaticPart' has no cute function "
        "yet. Qt's 'std::vector<HeaderField>::const_iterator "
        "HPack::FieldLookupTable::findInStaticPart(const HeaderField "
        "&field, CompareMode mode)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'compare'; did you mean "
        "'QOperatingSystemVersionBase::compare'?.")

  @staticmethod
  def frontKey(*__, **_) -> Never:
    """
    Qt's 'SearchEntry HPack::FieldLookupTable::frontKey() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.frontKey' has no cute function yet. Qt's "
        "'SearchEntry HPack::FieldLookupTable::frontKey() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def indexOfChunk(*__, **_) -> Never:
    """
    Qt's 'quint32 HPack::FieldLookupTable::indexOfChunk(const Chunk *chunk)
    const': names 'HPack::FieldLookupTable::Chunk', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.indexOfChunk' has no cute function yet. "
        "Qt's 'quint32 HPack::FieldLookupTable::indexOfChunk(const Chunk "
        "*chunk) const': names 'HPack::FieldLookupTable::Chunk', which has "
        "no cute class yet.")

  @staticmethod
  def keyToIndex(*__, **_) -> Never:
    """
    Qt's 'quint32 HPack::FieldLookupTable::keyToIndex(const SearchEntry &key)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.keyToIndex' has no cute function yet. Qt's "
        "'quint32 HPack::FieldLookupTable::keyToIndex(const SearchEntry "
        "&key) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def prependField(*__, **_) -> Never:
    """
    Qt's 'bool HPack::FieldLookupTable::prependField(const QByteArray &name,
    const QByteArray &value)': leans on 'HPack::entry_size(QByteArrayView,
    QByteArrayView)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.prependField' has no cute function yet. "
        "Qt's 'bool HPack::FieldLookupTable::prependField(const QByteArray "
        "&name, const QByteArray &value)': leans on "
        "'HPack::entry_size(QByteArrayView, QByteArrayView)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def staticPart(*__, **_) -> Never:
    """
    Qt's 'const std::vector<HeaderField>
    &HPack::FieldLookupTable::staticPart()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.staticPart' has no cute function yet. Qt's "
        "'const std::vector<HeaderField> "
        "&HPack::FieldLookupTable::staticPart()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def updateDynamicTableSize(*__, **_) -> Never:
    """
    Qt's 'bool HPack::FieldLookupTable::updateDynamicTableSize(quint32
    size)': leans on 'HPack::entry_size(QByteArrayView, QByteArrayView)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'HPack.FieldLookupTable.updateDynamicTableSize' has no cute "
        "function yet. Qt's 'bool "
        "HPack::FieldLookupTable::updateDynamicTableSize(quint32 size)': "
        "leans on 'HPack::entry_size(QByteArrayView, QByteArrayView)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
