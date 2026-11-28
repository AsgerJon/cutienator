"""
QQsbCollection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qqsbcollection_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQsbCollection to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QQsbCollection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQsbCollection: a plain Python object standing in
  front of one C++ QQsbCollection.

  What exists
  -----------

  Every function of Qt's QQsbCollection that has a ritual and that Python can
  call so far, 1 name in all: 'addEntry'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQsbCollection::~QQsbCollection()': the destructor: Python never
    removes a C++ QQsbCollection.
  - Qt's 'EntryMap QQsbCollection::availableEntries() const': gives a type
    Python has no way to take yet.
  - Qt's 'bool QQsbCollection::extractEntry(Entry entry, EntryDesc
    &entryDesc)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQsbCollection::readEndHeader(QDataStream &ds, qint64
    *startPos, quint8 *version)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQsbCollection::writeEndHeader(QDataStream &ds, qint64
    startPos, quint8 version, quint64 magic)': takes a type Python has no way
    to hand over yet.
  - Qt's 'bool QQsbCollection::readEndHeader(QIODevice *device, EntryMap
    *entries, quint8 *version)': names 'QQsbCollection::EntryMap', which has
    no cute class yet.
  - Qt's 'void QQsbCollection::writeEndHeader(QIODevice *device, const
    EntryMap &entries)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQsbCollection is created at the first use, not by
    'QQsbCollection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQsbCollection.
  - Each name of Qt's QQsbCollection that has no cute function yet,
    'availableEntries', 'extractEntry', 'readEndHeader', 'toFeatureSet',
    'writeEndHeader', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QQsbCollection, each a class in here as in
  #  C++.

  class Entry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQsbCollection::Entry: a plain Python object
    standing in front of one C++ QQsbCollection::Entry.

    C++ hands a QQsbCollection::Entry around as a copy, so every C++
    QQsbCollection::Entry behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQsbCollection::Entry that has a ritual and that
    Python can call so far, 1 name in all: 'isValid'. It can be made from
    Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQsbCollection::Entry::~Entry()': the destructor: Python removes
      its C++ QQsbCollection::Entry by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQsbCollection::Entry is created at the first use, not by
      'QQsbCollection::Entry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQsbCollection::Entry back gives a copy the ritual
      made for Python, in a new cute QQsbCollection::Entry.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQsbCollection::Entry'

    #  Qt's '~QQsbCollection::Entry()'. Naming it makes this a value class:
    #  Python owns every C++ QQsbCollection::Entry behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QQsbCollection5EntryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QQsbCollection::Entry::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqsbcollection-entry.html#isValid
      """
      #  bool QQsbCollection::Entry::isValid() const
      return self.uglySide.call('ritual_ZNK14QQsbCollection5Entry7isValidEv')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQsbCollection::Entry::Entry()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqsbcollection-entry.html#Entry
      """
      #  QQsbCollection::Entry::Entry()
      self._noteCreation(QQsbCollection.Entry, lambda: Rituals.call(
          'ritual_ZN14QQsbCollection5EntryC1Ev',
      ))

    @overload(QByteArray)
    def __init__(self, key: QByteArray) -> None:
      """
      Notes what was given, for Qt's 'QQsbCollection::Entry::Entry(const
      QByteArray &key)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqsbcollection-entry.html#Entry

      Parameters
      ----------

      key : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.
      """
      #  QQsbCollection::Entry::Entry(const QByteArray &key)
      self._noteCreation(QQsbCollection.Entry, lambda: Rituals.call(
          'ritual_ZN14QQsbCollection5EntryC1ERK10QByteArray',
          self._valueOf(key),
      ))

    @overload(QByteArray, int)
    def __init__(self, key: QByteArray, value: int) -> None:
      """
      Notes what was given, for Qt's 'QQsbCollection::Entry::Entry(const
      QByteArray &key, qint64 value)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qqsbcollection-entry.html#Entry

      Parameters
      ----------

      key : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.

      value : int
        Passed on as it is.
      """
      #  QQsbCollection::Entry::Entry(const QByteArray &key, qint64 value)
      self._noteCreation(QQsbCollection.Entry, lambda: Rituals.call(
          'ritual_ZN14QQsbCollection5EntryC1ERK10QByteArrayx',
          self._valueOf(key), value,
      ))

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

  class EntryDesc(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQsbCollection::EntryDesc: a plain Python object
    standing in front of one C++ QQsbCollection::EntryDesc.

    C++ hands a QQsbCollection::EntryDesc around as a copy, so every C++
    QQsbCollection::EntryDesc behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQsbCollection::EntryDesc that has a ritual and
    that Python can call so far, 1 name in all: 'generateSha'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QByteArray QQsbCollection::EntryDesc::generateSha(const
      QByteArray &materialKey, const FeatureSet &featureSet)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QQsbCollection::EntryDesc::~EntryDesc()': the destructor: Python
      removes its C++ QQsbCollection::EntryDesc by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQsbCollection::EntryDesc is created at the first use, not by
      'QQsbCollection::EntryDesc(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQsbCollection::EntryDesc back gives a copy the
      ritual made for Python, in a new cute QQsbCollection::EntryDesc.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQsbCollection::EntryDesc'

    #  Qt's '~QQsbCollection::EntryDesc()'. Naming it makes this a value
    #  class: Python owns every C++ QQsbCollection::EntryDesc behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QQsbCollection9EntryDescD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def generateSha(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QQsbCollection::EntryDesc::generateSha() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqsbcollection-entrydesc.html#generateSha

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QQsbCollection::EntryDesc::generateSha() const
      address = self.uglySide.call(
          'ritual_ZNK14QQsbCollection9EntryDesc11generateShaEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

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
  __qt_class__ = 'QQsbCollection'

  #  A C++ QQsbCollection Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQsbCollection'

  #  The functions Qt calls itself that QQsbCollection is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'availableEntries': (
          'EntryMap QQsbCollection::availableEntries() const',
      ),
      'extractEntry': (
          'bool QQsbCollection::extractEntry(Entry, EntryDesc &)',
      ),
  }

  #  The functions Qt calls itself that QQsbCollection is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'addEntry': (
          ('_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE',
           ('address', 'value', 'QtQuick3DUtils:QQsbCollection.Entry'),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'value',
                'QtQuick3DUtils:QQsbCollection.EntryDesc'),
           )),
      ),
  }

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

  @overload(QByteArray, EntryDesc)
  def addEntry(self, key: QByteArray, entryDesc: EntryDesc) -> Entry:
    """
    Calls Qt's 'Entry QQsbCollection::addEntry(const QByteArray &key, const
    EntryDesc &entryDesc)'.

    Qt's own words: https://doc.qt.io/qt-6/qqsbcollection.html#addEntry

    Parameters
    ----------

    key : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    entryDesc : EntryDesc
      Passed on as a value: Qt reads the C++ QQsbCollection::EntryDesc, which
      stays Python's own.

    Returns
    -------

    Entry
      A new cute QQsbCollection::Entry around the copy Qt gave back. Python
      owns it.
    """
    #  Entry QQsbCollection::addEntry(const QByteArray &key, const EntryDesc
    #      &entryDesc)
    address = self.uglySide.call(
        'ritual_ZN14QQsbCollection8addEntryERK10QByteArrayRKNS_9EntryDescE',
        self._valueOf(key), self._valueOf(entryDesc),
    )
    return QQsbCollection.Entry._cuteOwning(address)

  @staticmethod
  def availableEntries(*__, **_) -> Never:
    """
    Qt's 'EntryMap QQsbCollection::availableEntries() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQsbCollection.availableEntries' has no cute function yet. Qt's "
        "'EntryMap QQsbCollection::availableEntries() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def extractEntry(*__, **_) -> Never:
    """
    Qt's 'bool QQsbCollection::extractEntry(Entry entry, EntryDesc
    &entryDesc)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQsbCollection.extractEntry' has no cute function yet. Qt's 'bool "
        "QQsbCollection::extractEntry(Entry entry, EntryDesc &entryDesc)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def readEndHeader(*__, **_) -> Never:
    """
    - Qt's 'bool QQsbCollection::readEndHeader(QDataStream &ds, qint64
      *startPos, quint8 *version)': takes a type Python has no way to hand
      over yet.
    - Qt's 'bool QQsbCollection::readEndHeader(QIODevice *device, EntryMap
      *entries, quint8 *version)': names 'QQsbCollection::EntryMap', which
      has no cute class yet.
    """
    raise NotImplementedError(
        "'QQsbCollection.readEndHeader' has no cute function yet. Qt's "
        "'bool QQsbCollection::readEndHeader(QDataStream &ds, qint64 "
        "*startPos, quint8 *version)': takes a type Python has no way to "
        "hand over yet. Qt's 'bool QQsbCollection::readEndHeader(QIODevice "
        "*device, EntryMap *entries, quint8 *version)': names "
        "'QQsbCollection::EntryMap', which has no cute class yet.")

  @staticmethod
  def toFeatureSet(*__, **_) -> Never:
    """
    Qt's 'QQsbCollection::toFeatureSet': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQsbCollection.toFeatureSet' has no cute function yet. Qt's "
        "'QQsbCollection::toFeatureSet': a template: a pattern and no "
        "single function.")

  @staticmethod
  def writeEndHeader(*__, **_) -> Never:
    """
    - Qt's 'void QQsbCollection::writeEndHeader(QDataStream &ds, qint64
      startPos, quint8 version, quint64 magic)': takes a type Python has no
      way to hand over yet.
    - Qt's 'void QQsbCollection::writeEndHeader(QIODevice *device, const
      EntryMap &entries)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQsbCollection.writeEndHeader' has no cute function yet. Qt's "
        "'void QQsbCollection::writeEndHeader(QDataStream &ds, qint64 "
        "startPos, quint8 version, quint64 magic)': takes a type Python has "
        "no way to hand over yet. Qt's 'void "
        "QQsbCollection::writeEndHeader(QIODevice *device, const EntryMap "
        "&entries)': takes a type Python has no way to hand over yet.")
