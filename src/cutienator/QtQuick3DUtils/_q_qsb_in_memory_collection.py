"""
QQsbInMemoryCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQsbInMemoryCollection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQsbCollection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QQsbInMemoryCollection(QQsbCollection):
  """
  The cute side of Qt's QQsbInMemoryCollection: a plain Python object
  standing in front of one C++ QQsbInMemoryCollection.

  It is built on the cute 'QQsbCollection', as Qt's QQsbInMemoryCollection is
  built on Qt's QQsbCollection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQsbInMemoryCollection that has a ritual and that
  Python can call so far, 4 names in all: 'addEntry', 'clear', 'load',
  'save'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'EntryMap QQsbInMemoryCollection::availableEntries() const': gives a
    type Python has no way to take yet.
  - Qt's 'bool QQsbInMemoryCollection::extractEntry(Entry entry, EntryDesc
    &entryDesc)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQsbInMemoryCollection is created at the first use, not by
    'QQsbInMemoryCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQsbInMemoryCollection.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQsbInMemoryCollection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'QQsbInMemoryCollection::QQsbInMemoryCollection()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqsbinmemorycollection.html#QQsbInMemoryCollection
    """
    #  QQsbInMemoryCollection::QQsbInMemoryCollection()
    self._noteCreation(QQsbInMemoryCollection, lambda: Rituals.call(
        'ritual_ZN22QQsbInMemoryCollectionC1Ev',
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

  @overload(QByteArray, QQsbCollection.EntryDesc)
  def addEntry(
      self,
      key: QByteArray,
      entryDesc: QQsbCollection.EntryDesc,
  ) -> QQsbCollection.Entry:
    """
    Calls Qt's 'Entry QQsbInMemoryCollection::addEntry(const QByteArray &key,
    const EntryDesc &entryDesc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqsbinmemorycollection.html#addEntry

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    entryDesc : QQsbCollection.EntryDesc
      Passed on as a value: Qt reads the C++ QQsbCollection::EntryDesc, which
      stays Python's own.

    Returns
    -------

    QQsbCollection.Entry
      A new cute QQsbCollection::Entry around the copy Qt gave back. Python
      owns it.
    """
    #  Entry QQsbInMemoryCollection::addEntry(const QByteArray &key, const
    #      EntryDesc &entryDesc)
    ritual = (
        'ritual_ZN22QQsbInMemoryCollection8addEntryERK10QByteArrayRKN14QQsb'
        'Collection9EntryDescE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQsbInMemoryCollection8addEntryERK10QByteArrayRKN'
          '14QQsbCollection9EntryDescE')
    address = self.uglySide.call(
        ritual, self._valueOf(key), self._valueOf(entryDesc),
    )
    return QQsbCollection.Entry._cuteOwning(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QQsbInMemoryCollection::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qqsbinmemorycollection.html#clear
    """
    #  void QQsbInMemoryCollection::clear()
    self.uglySide.call('ritual_ZN22QQsbInMemoryCollection5clearEv')

  @overload(str)
  def load(self, filename: str) -> bool:
    """
    Calls Qt's 'bool QQsbInMemoryCollection::load(const QString &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qqsbinmemorycollection.html#load

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQsbInMemoryCollection::load(const QString &filename)
    return self.uglySide.call(
        'ritual_ZN22QQsbInMemoryCollection4loadERK7QString', filename,
    )

  @overload(str)
  def save(self, filename: str) -> bool:
    """
    Calls Qt's 'bool QQsbInMemoryCollection::save(const QString &filename)'.

    Qt's own words: https://doc.qt.io/qt-6/qqsbinmemorycollection.html#save

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQsbInMemoryCollection::save(const QString &filename)
    return self.uglySide.call(
        'ritual_ZN22QQsbInMemoryCollection4saveERK7QString', filename,
    )
