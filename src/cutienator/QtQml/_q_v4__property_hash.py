"""
QV4::PropertyHash binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::PropertyHash to be private: it declares the class in a
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
  from typing import Optional


class PropertyHash(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::PropertyHash: a plain Python object standing in
  front of one C++ QV4::PropertyHash.

  C++ hands a QV4::PropertyHash around as a copy, so every C++
  QV4::PropertyHash behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::PropertyHash that has a ritual and that Python
  can call so far, 3 names in all: 'addEntry', 'lookup', 'detach'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::PropertyHash::~PropertyHash()': the destructor: Python removes
    its C++ QV4::PropertyHash by it, and has no other use for it.
  - Qt's 'PropertyHash &QV4::PropertyHash::operator=(const PropertyHash
    &other)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QV4::PropertyHash is created at the first use, not by
    'QV4::PropertyHash(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::PropertyHash back gives a copy the ritual made
    for Python, in a new cute QV4::PropertyHash.
  """

  #  The classes Qt writes inside QV4::PropertyHash, each a class in here as
  #  in C++.

  class Entry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::PropertyHash::Entry: a plain Python object
    standing in front of one C++ QV4::PropertyHash::Entry.

    C++ hands a QV4::PropertyHash::Entry around as a copy, so every C++
    QV4::PropertyHash::Entry behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QV4::PropertyHash::Entry yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::PropertyHash::Entry::~Entry()': the destructor: Python
      removes its C++ QV4::PropertyHash::Entry by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QV4::PropertyHash::Entry is created at the first use, not by
      'QV4::PropertyHash::Entry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::PropertyHash::Entry back gives a copy the
      ritual made for Python, in a new cute QV4::PropertyHash::Entry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::PropertyHash::Entry'

    #  Qt's '~QV4::PropertyHash::Entry()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::PropertyHash::Entry behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV412PropertyHash5EntryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::PropertyHash'

  #  Qt's '~QV4::PropertyHash()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::PropertyHash behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV412PropertyHashD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.PropertyKey'])
  def lookup(self, identifier: QV4.PropertyKey) -> Optional[Entry]:
    """
    Calls Qt's 'Entry *QV4::PropertyHash::lookup(PropertyKey identifier)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyhash.html#lookup

    Parameters
    ----------

    identifier : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    Returns
    -------

    Optional[Entry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Entry *QV4::PropertyHash::lookup(PropertyKey identifier) const
    address = self.uglySide.call(
        'ritual_ZNK3QV412PropertyHash6lookupENS_11PropertyKeyE',
        self._valueOf(identifier),
    )
    return QV4.PropertyHash.Entry._cuteAt(address)

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
    Notes what was given, for Qt's 'QV4::PropertyHash::PropertyHash()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyhash.html#PropertyHash
    """
    #  QV4::PropertyHash::PropertyHash()
    self._noteCreation(PropertyHash, lambda: Rituals.call(
        'ritual_ZN3QV412PropertyHashC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: PropertyHash) -> None:
    """
    Notes what was given, for Qt's 'QV4::PropertyHash::PropertyHash(const
    PropertyHash &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyhash.html#PropertyHash

    Parameters
    ----------

    other : PropertyHash
      Passed on as a value: Qt reads the C++ QV4::PropertyHash, which stays
      Python's own.
    """
    #  QV4::PropertyHash::PropertyHash(const PropertyHash &other)
    self._noteCreation(PropertyHash, lambda: Rituals.call(
        'ritual_ZN3QV412PropertyHashC1ERKS0_', self._valueOf(other),
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

  @overload(Entry, int)
  def addEntry(self, entry: Entry, classSize: int) -> None:
    """
    Calls Qt's 'void QV4::PropertyHash::addEntry(const Entry &entry, int
    classSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyhash.html#addEntry

    Parameters
    ----------

    entry : Entry
      Passed on as a value: Qt reads the C++ QV4::PropertyHash::Entry, which
      stays Python's own.

    classSize : int
      Passed on as it is.
    """
    #  void QV4::PropertyHash::addEntry(const Entry &entry, int classSize)
    self.uglySide.call(
        'ritual_ZN3QV412PropertyHash8addEntryERKNS0_5EntryEi',
        self._valueOf(entry), classSize,
    )

  @overload(bool, int)
  def detach(self, grow: bool, classSize: int) -> None:
    """
    Calls Qt's 'void QV4::PropertyHash::detach(bool grow, int classSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-propertyhash.html#detach

    Parameters
    ----------

    grow : bool
      Passed on as it is.

    classSize : int
      Passed on as it is.
    """
    #  void QV4::PropertyHash::detach(bool grow, int classSize)
    self.uglySide.call(
        'ritual_ZN3QV412PropertyHash6detachEbi', grow, classSize,
    )
