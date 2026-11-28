"""
QBinaryJsonPrivate::Entry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QBinaryJsonPrivate::Entry to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QBinaryJsonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Entry(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBinaryJsonPrivate::Entry: a plain Python object
  standing in front of one C++ QBinaryJsonPrivate::Entry.

  C++ hands a QBinaryJsonPrivate::Entry around as a copy, so every C++
  QBinaryJsonPrivate::Entry behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBinaryJsonPrivate::Entry that has a ritual and that
  Python can call so far, 8 names in all: 'size', 'usedStorage',
  'shallowKey', 'shallowLatin1Key', 'key', 'isValid', '__eq__', '__ge__'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBinaryJsonPrivate::Entry::~Entry()': the destructor: Python
    removes its C++ QBinaryJsonPrivate::Entry by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QBinaryJsonPrivate::Entry is created at the first use, not by
    'QBinaryJsonPrivate::Entry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBinaryJsonPrivate::Entry back gives a copy the
    ritual made for Python, in a new cute QBinaryJsonPrivate::Entry.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBinaryJsonPrivate::Entry'

  #  Qt's '~QBinaryJsonPrivate::Entry()'. Naming it makes this a value class:
  #  Python owns every C++ QBinaryJsonPrivate::Entry behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18QBinaryJsonPrivate5EntryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Entry::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#size
    """
    #  uint QBinaryJsonPrivate::Entry::size() const
    return self.uglySide.call('ritual_ZNK18QBinaryJsonPrivate5Entry4sizeEv')

  @overload(WAIT['QBinaryJsonPrivate.Base'])
  @overload(NoneType)
  def usedStorage(self, b: Optional[QBinaryJsonPrivate.Base]) -> int:
    """
    Calls Qt's 'uint QBinaryJsonPrivate::Entry::usedStorage(Base *b) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#usedStorage

    Parameters
    ----------

    b : Optional[QBinaryJsonPrivate.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  uint QBinaryJsonPrivate::Entry::usedStorage(Base *b) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Entry11usedStorageEPNS_4BaseE',
        self._addressOf(b),
    )

  def shallowKey(self) -> QBinaryJsonPrivate.String:
    """
    Calls Qt's 'String QBinaryJsonPrivate::Entry::shallowKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#shallowKey

    Returns
    -------

    QBinaryJsonPrivate.String
      A new cute QBinaryJsonPrivate::String around the copy Qt gave back.
      Python owns it.
    """
    #  String QBinaryJsonPrivate::Entry::shallowKey() const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Entry10shallowKeyEv',
    )
    return QBinaryJsonPrivate.String._cuteOwning(address)

  def shallowLatin1Key(self) -> QBinaryJsonPrivate.Latin1String:
    """
    Calls Qt's 'Latin1String QBinaryJsonPrivate::Entry::shallowLatin1Key()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#shallowLatin1Key

    Returns
    -------

    QBinaryJsonPrivate.Latin1String
      A new cute QBinaryJsonPrivate::Latin1String around the copy Qt gave
      back. Python owns it.
    """
    #  Latin1String QBinaryJsonPrivate::Entry::shallowLatin1Key() const
    address = self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Entry16shallowLatin1KeyEv',
    )
    return QBinaryJsonPrivate.Latin1String._cuteOwning(address)

  def key(self) -> str:
    """
    Calls Qt's 'QString QBinaryJsonPrivate::Entry::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBinaryJsonPrivate::Entry::key() const
    return self.uglySide.call('ritual_ZNK18QBinaryJsonPrivate5Entry3keyEv')

  @overload(int)
  def isValid(self, maxSize: int) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Entry::isValid(uint maxSize) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#isValid

    Parameters
    ----------

    maxSize : int
      Passed on as it is.
    """
    #  bool QBinaryJsonPrivate::Entry::isValid(uint maxSize) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5Entry7isValidEj', maxSize,
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

  @overload(str)
  def __eq__(self, key: str) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Entry::operator==(QStringView key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#operator==

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QBinaryJsonPrivate::Entry::operator==(QStringView key) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5EntryeqE11QStringView', key,
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(str)
  def __ge__(self, key: str) -> bool:
    """
    Calls Qt's 'bool QBinaryJsonPrivate::Entry::operator>=(QStringView key)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbinaryjsonprivate-entry.html#operator>=

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QBinaryJsonPrivate::Entry::operator>=(QStringView key) const
    return self.uglySide.call(
        'ritual_ZNK18QBinaryJsonPrivate5EntrygeE11QStringView', key,
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

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
