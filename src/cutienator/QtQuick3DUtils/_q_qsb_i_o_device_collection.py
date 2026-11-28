"""
QQsbIODeviceCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQsbIODeviceCollection to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import QQsbCollection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QQsbIODeviceCollection(QQsbCollection):
  """
  The cute side of Qt's QQsbIODeviceCollection: a plain Python object
  standing in front of one C++ QQsbIODeviceCollection.

  It is built on the cute 'QQsbCollection', as Qt's QQsbIODeviceCollection is
  built on Qt's QQsbCollection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQsbIODeviceCollection that has a ritual and that
  Python can call so far, 4 names in all: 'map', 'unmap', 'addEntry',
  'dumpInfo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQsbIODeviceCollection::QQsbIODeviceCollection(QIODevice &dev)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQsbIODeviceCollection::~QQsbIODeviceCollection()': the destructor:
    Python never removes a C++ QQsbIODeviceCollection.
  - Qt's 'EntryMap QQsbIODeviceCollection::availableEntries() const': gives a
    type Python has no way to take yet.
  - Qt's 'bool QQsbIODeviceCollection::extractEntry(Entry entry, EntryDesc
    &entryDesc)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQsbIODeviceCollection::dumpInfo(QIODevice &device)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QQsbIODeviceCollection is created at the first use, not by
    'QQsbIODeviceCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQsbIODeviceCollection.
  """

  #  The enums Qt writes inside QQsbIODeviceCollection, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class MapMode(CuteNum):
    """
    The enum 'QQsbIODeviceCollection::MapMode' of Qt, with the 2 names Qt
    gives in it.
    """

    Read = Kee[int](1)
    Write = Kee[int](10)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQsbIODeviceCollection'

  #  A C++ QQsbIODeviceCollection Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQsbIODeviceCollection'

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

  @overload(str)
  def __init__(self, filePath: str) -> None:
    """
    Notes what was given, for Qt's
    'QQsbIODeviceCollection::QQsbIODeviceCollection(const QString
    &filePath)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqsbiodevicecollection.html#QQsbIODeviceCollection

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQsbIODeviceCollection::QQsbIODeviceCollection(const QString
    #      &filePath)
    self._noteCreation(QQsbIODeviceCollection, lambda: Rituals.call(
        'ritual_ZN22QQsbIODeviceCollectionC1ERK7QString', filePath,
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

  @overload(MapMode)
  def map(self, mode: MapMode) -> bool:
    """
    Calls Qt's 'bool QQsbIODeviceCollection::map(MapMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qqsbiodevicecollection.html#map

    Parameters
    ----------

    mode : MapMode
      Passed on as its number.
    """
    #  bool QQsbIODeviceCollection::map(MapMode mode)
    return self.uglySide.call(
        'ritual_ZN22QQsbIODeviceCollection3mapENS_7MapModeE', mode.value,
    )

  def unmap(self) -> None:
    """
    Calls Qt's 'void QQsbIODeviceCollection::unmap()'.

    Qt's own words: https://doc.qt.io/qt-6/qqsbiodevicecollection.html#unmap
    """
    #  void QQsbIODeviceCollection::unmap()
    self.uglySide.call('ritual_ZN22QQsbIODeviceCollection5unmapEv')

  @overload(QByteArray, QQsbCollection.EntryDesc)
  def addEntry(
      self,
      key: QByteArray,
      entryDesc: QQsbCollection.EntryDesc,
  ) -> QQsbCollection.Entry:
    """
    Calls Qt's 'Entry QQsbIODeviceCollection::addEntry(const QByteArray &key,
    const EntryDesc &entryDesc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqsbiodevicecollection.html#addEntry

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
    #  Entry QQsbIODeviceCollection::addEntry(const QByteArray &key, const
    #      EntryDesc &entryDesc)
    ritual = (
        'ritual_ZN22QQsbIODeviceCollection8addEntryERK10QByteArrayRKN14QQsb'
        'Collection9EntryDescE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQsbIODeviceCollection8addEntryERK10QByteArrayRKN'
          '14QQsbCollection9EntryDescE')
    address = self.uglySide.call(
        ritual, self._valueOf(key), self._valueOf(entryDesc),
    )
    return QQsbCollection.Entry._cuteOwning(address)

  @overload()
  def dumpInfo(self) -> None:
    """
    Calls Qt's 'void QQsbIODeviceCollection::dumpInfo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqsbiodevicecollection.html#dumpInfo
    """
    #  void QQsbIODeviceCollection::dumpInfo()
    self.uglySide.call('ritual_ZN22QQsbIODeviceCollection8dumpInfoEv')

  @staticmethod
  @overload(str)
  def dumpInfo(device: str) -> None:
    """
    Calls Qt's 'void QQsbIODeviceCollection::dumpInfo(const QString
    &device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqsbiodevicecollection.html#dumpInfo

    Parameters
    ----------

    device : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQsbIODeviceCollection::dumpInfo(const QString &device)
    Rituals.call(
        'ritual_ZN22QQsbIODeviceCollection8dumpInfoERK7QString', device,
    )
