"""
QV4::IdentifierHash binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4identifierhash_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::IdentifierHash to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class IdentifierHash(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::IdentifierHash: a plain Python object standing
  in front of one C++ QV4::IdentifierHash.

  C++ hands a QV4::IdentifierHash around as a copy, so every C++
  QV4::IdentifierHash behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::IdentifierHash that has a ritual and that
  Python can call so far, 8 names in all: 'isValid', 'size', 'add', 'value',
  'addEntry', 'lookup', 'reverseLookup', 'toIdentifier'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::IdentifierHash::IdentifierHash(IdentifierHash &&other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QV4::IdentifierHash::~IdentifierHash()': the destructor: Python
    removes its C++ QV4::IdentifierHash by it, and has no other use for it.
  - Qt's 'void QV4::IdentifierHash::swap(IdentifierHash &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'IdentifierHash &QV4::IdentifierHash::operator=(IdentifierHash
    &&other)': assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  3 of the 21 functions Qt declares: 2 a template; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::IdentifierHash is created at the first use, not by
    'QV4::IdentifierHash(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::IdentifierHash back gives a copy the ritual made
    for Python, in a new cute QV4::IdentifierHash.
  - Each name of Qt's QV4::IdentifierHash that has no cute function yet,
    'key', 'swap', 'toString', holds a function that raises
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
  __qt_class__ = 'QV4::IdentifierHash'

  #  Qt's '~QV4::IdentifierHash()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::IdentifierHash behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV414IdentifierHashD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QV4::IdentifierHash::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#isValid
    """
    #  bool QV4::IdentifierHash::isValid() const
    return self.uglySide.call('ritual_ZNK3QV414IdentifierHash7isValidEv')

  def size(self) -> int:
    """
    Calls Qt's 'int QV4::IdentifierHash::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#size
    """
    #  int QV4::IdentifierHash::size() const
    return self.uglySide.call('ritual_ZNK3QV414IdentifierHash4sizeEv')

  @overload(str)
  def value(self, str: str) -> int:
    """
    Calls Qt's 'int QV4::IdentifierHash::value(const QString &str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#value

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QV4::IdentifierHash::value(const QString &str) const
    return self.uglySide.call(
        'ritual_ZNK3QV414IdentifierHash5valueERK7QString', str,
    )

  @overload(WAIT['QV4.Heap.String'])
  @overload(NoneType)
  def value(self, str: Optional[QV4.Heap.String]) -> int:
    """
    Calls Qt's 'int QV4::IdentifierHash::value(Heap::String *str) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#value

    Parameters
    ----------

    str : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QV4::IdentifierHash::value(Heap::String *str) const
    return self.uglySide.call(
        'ritual_ZNK3QV414IdentifierHash5valueEPNS_4Heap6StringE',
        self._addressOf(str),
    )

  @overload(WAIT['QV4.PropertyKey'])
  def lookup(self, identifier: QV4.PropertyKey) -> int:
    """
    Calls Qt's 'int QV4::IdentifierHash::lookup(PropertyKey identifier)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#lookup

    Parameters
    ----------

    identifier : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  int QV4::IdentifierHash::lookup(PropertyKey identifier) const
    return self.uglySide.call(
        'ritual_ZNK3QV414IdentifierHash6lookupENS_11PropertyKeyE',
        self._valueOf(identifier),
    )

  @overload(int)
  def reverseLookup(self, value: int) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierHash::reverseLookup(int value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhash.html#reverseLookup

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::IdentifierHash::reverseLookup(int value) const
    address = self.uglySide.call(
        'ritual_ZNK3QV414IdentifierHash13reverseLookupEi', value,
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(str)
  def toIdentifier(self, str: str) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierHash::toIdentifier(const QString
    &str) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhash.html#toIdentifier

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::IdentifierHash::toIdentifier(const QString &str)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV414IdentifierHash12toIdentifierERK7QString', str,
    )
    return QV4.PropertyKey._cuteOwning(address)

  @overload(WAIT['QV4.Heap.String'])
  @overload(NoneType)
  def toIdentifier(self, str: Optional[QV4.Heap.String]) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::IdentifierHash::toIdentifier(Heap::String
    *str) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhash.html#toIdentifier

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
    #  PropertyKey QV4::IdentifierHash::toIdentifier(Heap::String *str) const
    address = self.uglySide.call(
        'ritual_ZNK3QV414IdentifierHash12toIdentifierEPNS_4Heap6StringE',
        self._addressOf(str),
    )
    return QV4.PropertyKey._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::IdentifierHash::IdentifierHash()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhash.html#IdentifierHash
    """
    #  QV4::IdentifierHash::IdentifierHash()
    self._noteCreation(IdentifierHash, lambda: Rituals.call(
        'ritual_ZN3QV414IdentifierHashC1Ev',
    ))

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QV4::IdentifierHash::IdentifierHash(ExecutionEngine *engine)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhash.html#IdentifierHash

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::IdentifierHash::IdentifierHash(ExecutionEngine *engine)
    self._noteCreation(IdentifierHash, lambda: Rituals.call(
        'ritual_ZN3QV414IdentifierHashC1EPNS_15ExecutionEngineE',
        self._addressOf(engine),
    ))

  @overload(THIS)
  def __init__(self, other: IdentifierHash) -> None:
    """
    Notes what was given, for Qt's 'QV4::IdentifierHash::IdentifierHash(const
    IdentifierHash &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-identifierhash.html#IdentifierHash

    Parameters
    ----------

    other : IdentifierHash
      Passed on as a value: Qt reads the C++ QV4::IdentifierHash, which stays
      Python's own.
    """
    #  QV4::IdentifierHash::IdentifierHash(const IdentifierHash &other)
    self._noteCreation(IdentifierHash, lambda: Rituals.call(
        'ritual_ZN3QV414IdentifierHashC1ERKS0_', self._valueOf(other),
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

  @overload(str, int)
  def add(self, str: str, value: int) -> None:
    """
    Calls Qt's 'void QV4::IdentifierHash::add(const QString &str, int
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#add

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    value : int
      Passed on as it is.
    """
    #  void QV4::IdentifierHash::add(const QString &str, int value)
    self.uglySide.call(
        'ritual_ZN3QV414IdentifierHash3addERK7QStringi', str, value,
    )

  @overload(WAIT['QV4.Heap.String'], int)
  @overload(NoneType, int)
  def add(self, str: Optional[QV4.Heap.String], value: int) -> None:
    """
    Calls Qt's 'void QV4::IdentifierHash::add(Heap::String *str, int value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#add

    Parameters
    ----------

    str : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : int
      Passed on as it is.
    """
    #  void QV4::IdentifierHash::add(Heap::String *str, int value)
    self.uglySide.call(
        'ritual_ZN3QV414IdentifierHash3addEPNS_4Heap6StringEi',
        self._addressOf(str), value,
    )

  @overload(WAIT['QV4.PropertyKey'], int)
  def addEntry(self, i: QV4.PropertyKey, value: int) -> None:
    """
    Calls Qt's 'void QV4::IdentifierHash::addEntry(PropertyKey i, int
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-identifierhash.html#addEntry

    Parameters
    ----------

    i : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    value : int
      Passed on as it is.
    """
    #  void QV4::IdentifierHash::addEntry(PropertyKey i, int value)
    self.uglySide.call(
        'ritual_ZN3QV414IdentifierHash8addEntryENS_11PropertyKeyEi',
        self._valueOf(i), value,
    )

  @staticmethod
  def key(*__, **_) -> Never:
    """
    Qt's 'QV4::IdentifierHash::key': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.IdentifierHash.key' has no cute function yet. Qt's "
        "'QV4::IdentifierHash::key': a template: a pattern and no single "
        "function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QV4::IdentifierHash::swap(IdentifierHash &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.IdentifierHash.swap' has no cute function yet. Qt's 'void "
        "QV4::IdentifierHash::swap(IdentifierHash &other)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'QV4::IdentifierHash::toString': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QV4.IdentifierHash.toString' has no cute function yet. Qt's "
        "'QV4::IdentifierHash::toString': a template: a pattern and no "
        "single function.")
