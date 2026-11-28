"""
QV4::IdentifierTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4identifiertable_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::IdentifierTable to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class IdentifierTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::IdentifierTable: a plain Python object standing
  in front of one C++ QV4::IdentifierTable.

  C++ hands a QV4::IdentifierTable around as a copy, so every C++
  QV4::IdentifierTable behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::IdentifierTable that has a ritual and that
  Python can call so far, 13 names in all: 'addEntry', 'insertString',
  'insertSymbol', 'asPropertyKey', 'asPropertyKeyImpl', 'resolveId',
  'stringForId', 'symbolForId', 'markObjects', 'sweep', 'addIdentifierHash',
  'removeIdentifierHash', 'resolveStringEntry'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::IdentifierTable::~IdentifierTable()': the destructor: Python
    removes its C++ QV4::IdentifierTable by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::IdentifierTable is created at the first use, not by
    'QV4::IdentifierTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::IdentifierTable back gives a copy the ritual
    made for Python, in a new cute QV4::IdentifierTable.
  """

  #  The enums Qt writes inside QV4::IdentifierTable, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class KeyConversionBehavior(CuteNum):
    """
    The enum 'QV4::IdentifierTable::KeyConversionBehavior' of Qt, with the 2
    names Qt gives in it.
    """

    Default = Kee[int](0)
    ForceConversionToId = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::IdentifierTable'

  #  Qt's '~QV4::IdentifierTable()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::IdentifierTable behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV415IdentifierTableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.PropertyKey'])
  def resolveId(
      self,
      i: QV4.PropertyKey,
  ) -> Optional[QV4.Heap.StringOrSymbol]:
    """
    Calls Qt's 'Heap::StringOrSymbol
    *QV4::IdentifierTable::resolveId(PropertyKey i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifiertable.html#resolveId

    Parameters
    ----------

    i : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.Heap.StringOrSymbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::StringOrSymbol *QV4::IdentifierTable::resolveId(PropertyKey i)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV415IdentifierTable9resolveIdENS_11PropertyKeyE',
        self._valueOf(i),
    )
    return QV4.Heap.StringOrSymbol._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  def stringForId(self, i: QV4.PropertyKey) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::IdentifierTable::stringForId(PropertyKey
    i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#stringForId

    Parameters
    ----------

    i : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::IdentifierTable::stringForId(PropertyKey i) const
    address = self.uglySide.call(
        'ritual_ZNK3QV415IdentifierTable11stringForIdENS_11PropertyKeyE',
        self._valueOf(i),
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(WAIT['QV4.PropertyKey'])
  def symbolForId(self, i: QV4.PropertyKey) -> Optional[QV4.Heap.Symbol]:
    """
    Calls Qt's 'Heap::Symbol *QV4::IdentifierTable::symbolForId(PropertyKey
    i) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#symbolForId

    Parameters
    ----------

    i : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[QV4.Heap.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Symbol *QV4::IdentifierTable::symbolForId(PropertyKey i) const
    address = self.uglySide.call(
        'ritual_ZNK3QV415IdentifierTable11symbolForIdENS_11PropertyKeyE',
        self._valueOf(i),
    )
    return QV4.Heap.Symbol._cuteAt(address)

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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  @overload(WAIT['QV4.ExecutionEngine'], int)
  @overload(NoneType, int)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      numBits: int = 8,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QV4::IdentifierTable::IdentifierTable(ExecutionEngine *engine, int
    numBits)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#IdentifierTable

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    numBits : int
      Passed on as it is. May be left out, as in Qt: it is then 8.
    """
    #  QV4::IdentifierTable::IdentifierTable(ExecutionEngine *engine, int
    #      numBits)
    self._noteCreation(IdentifierTable, lambda: Rituals.call(
        'ritual_ZN3QV415IdentifierTableC1EPNS_15ExecutionEngineEi',
        self._addressOf(engine), numBits,
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

  @overload(WAIT['QV4.Heap.StringOrSymbol'])
  @overload(NoneType)
  def addEntry(self, str: Optional[QV4.Heap.StringOrSymbol]) -> None:
    """
    Calls Qt's 'void QV4::IdentifierTable::addEntry(Heap::StringOrSymbol
    *str)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifiertable.html#addEntry

    Parameters
    ----------

    str : Optional[QV4.Heap.StringOrSymbol]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::IdentifierTable::addEntry(Heap::StringOrSymbol *str)
    self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable8addEntryEPNS_4Heap14StringOrSymbolE',
        self._addressOf(str),
    )

  @overload(str)
  def insertString(self, s: str) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::IdentifierTable::insertString(const
    QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#insertString

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::IdentifierTable::insertString(const QString &s)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable12insertStringERK7QString', s,
    )
    return QV4.Heap.String._cuteAt(address)

  @overload(str)
  def insertSymbol(self, s: str) -> Optional[QV4.Heap.Symbol]:
    """
    Calls Qt's 'Heap::Symbol *QV4::IdentifierTable::insertSymbol(const
    QString &s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#insertSymbol

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QV4.Heap.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Symbol *QV4::IdentifierTable::insertSymbol(const QString &s)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable12insertSymbolERK7QString', s,
    )
    return QV4.Heap.Symbol._cuteAt(address)

  @overload(WAIT['QV4.Heap.String'])
  @overload(NoneType)
  def asPropertyKey(self, str: Optional[QV4.Heap.String]) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierTable::asPropertyKey(const
    Heap::String *str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#asPropertyKey

    Parameters
    ----------

    str : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::IdentifierTable::asPropertyKey(const Heap::String
    #      *str)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable13asPropertyKeyEPKNS_4Heap6StringE',
        self._addressOf(str),
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(WAIT['QV4.String'])
  def asPropertyKey(self, str: Optional[QV4.String]) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierTable::asPropertyKey(const
    QV4::String *str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#asPropertyKey

    Parameters
    ----------

    str : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::IdentifierTable::asPropertyKey(const QV4::String
    #      *str)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable13asPropertyKeyEPKNS_6StringE',
        self._addressOf(str),
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(str)
  @overload(str, KeyConversionBehavior)
  def asPropertyKey(
      self,
      s: str,
      conversionBehavior: KeyConversionBehavior = (
          KeyConversionBehavior.Default),
  ) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierTable::asPropertyKey(const QString
    &s, KeyConversionBehavior conversionBehavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#asPropertyKey

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    conversionBehavior : KeyConversionBehavior
      Passed on as its number. May be left out, as in Qt: it is then
      KeyConversionBehavior.Default.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::IdentifierTable::asPropertyKey(const QString &s,
    #      KeyConversionBehavior conversionBehavior)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable13asPropertyKeyERK7QStringNS0_21KeyC'
        'onversionBehaviorE',
        s, conversionBehavior.value,
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(WAIT['QV4.Heap.String'])
  @overload(NoneType)
  def asPropertyKeyImpl(
      self,
      str: Optional[QV4.Heap.String],
  ) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierTable::asPropertyKeyImpl(const
    Heap::String *str)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#asPropertyKeyImpl

    Parameters
    ----------

    str : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::IdentifierTable::asPropertyKeyImpl(const Heap::String
    #      *str)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable17asPropertyKeyImplEPKNS_4Heap6Strin'
        'gE',
        self._addressOf(str),
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def markObjects(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::IdentifierTable::markObjects(MarkStack *markStack)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#markObjects

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::IdentifierTable::markObjects(MarkStack *markStack) const
    self.uglySide.call(
        'ritual_ZNK3QV415IdentifierTable11markObjectsEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  def sweep(self) -> None:
    """
    Calls Qt's 'void QV4::IdentifierTable::sweep()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifiertable.html#sweep
    """
    #  void QV4::IdentifierTable::sweep()
    self.uglySide.call('ritual_ZN3QV415IdentifierTable5sweepEv')

  @overload(WAIT['QV4.IdentifierHashData'])
  @overload(NoneType)
  def addIdentifierHash(self, h: Optional[QV4.IdentifierHashData]) -> None:
    """
    Calls Qt's 'void
    QV4::IdentifierTable::addIdentifierHash(IdentifierHashData *h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#addIdentifierHash

    Parameters
    ----------

    h : Optional[QV4.IdentifierHashData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::IdentifierTable::addIdentifierHash(IdentifierHashData *h)
    self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable17addIdentifierHashEPNS_18Identifier'
        'HashDataE',
        self._addressOf(h),
    )

  @overload(WAIT['QV4.IdentifierHashData'])
  @overload(NoneType)
  def removeIdentifierHash(
      self,
      h: Optional[QV4.IdentifierHashData],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::IdentifierTable::removeIdentifierHash(IdentifierHashData *h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#removeIdentifierHash

    Parameters
    ----------

    h : Optional[QV4.IdentifierHashData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::IdentifierTable::removeIdentifierHash(IdentifierHashData *h)
    self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable20removeIdentifierHashEPNS_18Identif'
        'ierHashDataE',
        self._addressOf(h),
    )

  @overload(str, int, int)
  def resolveStringEntry(
      self,
      s: str,
      hash: int,
      subtype: int,
  ) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::IdentifierTable::resolveStringEntry(const
    QString &s, uint hash, uint subtype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifiertable.html#resolveStringEntry

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    hash : int
      Passed on as it is.

    subtype : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::IdentifierTable::resolveStringEntry(const QString
    #      &s, uint hash, uint subtype)
    address = self.uglySide.call(
        'ritual_ZN3QV415IdentifierTable18resolveStringEntryERK7QStringjj',
        s, hash, subtype,
    )
    return QV4.Heap.String._cuteAt(address)
