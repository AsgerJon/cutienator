"""
QQmlJSResourceFileMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsresourcefilemapper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSResourceFileMapper to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQmlJSResourceFileMapper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSResourceFileMapper: a plain Python object
  standing in front of one C++ QQmlJSResourceFileMapper.

  C++ hands a QQmlJSResourceFileMapper around as a copy, so every C++
  QQmlJSResourceFileMapper behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSResourceFileMapper that has a ritual and that
  Python can call so far, 9 names in all: 'allQmlJSFilter',
  'localFileFilter', 'resourceFileFilter', 'resourceQmlDirectoryFilter',
  'isEmpty', 'isFile', 'filePaths', 'resourcePaths', 'entry'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<Entry> QQmlJSResourceFileMapper::filter(const Filter &filter)
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlJSResourceFileMapper::populateFromQrcFile(QFile &file)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSResourceFileMapper::~QQmlJSResourceFileMapper()': the
    destructor: Python removes its C++ QQmlJSResourceFileMapper by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSResourceFileMapper is created at the first use, not by
    'QQmlJSResourceFileMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSResourceFileMapper back gives a copy the ritual
    made for Python, in a new cute QQmlJSResourceFileMapper.
  - Each name of Qt's QQmlJSResourceFileMapper that has no cute function yet,
    'filter', 'populateFromQrcFile', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSResourceFileMapper, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FilterMode(CuteFlags):
    """
    The flags enum 'QQmlJSResourceFileMapper::FilterMode' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QQmlJSResourceFileMapper::FilterFlags'.
    """

    File = 0x0
    Directory = 0x1
    Resource = 0x2
    Recurse = 0x4

  FilterFlags = FilterMode

  #  The classes Qt writes inside QQmlJSResourceFileMapper, each a class in
  #  here as in C++.

  class Entry(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSResourceFileMapper::Entry: a plain Python
    object standing in front of one C++ QQmlJSResourceFileMapper::Entry.

    C++ hands a QQmlJSResourceFileMapper::Entry around as a copy, so every
    C++ QQmlJSResourceFileMapper::Entry behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQmlJSResourceFileMapper::Entry that has a ritual
    and that Python can call so far, 1 name in all: 'isValid'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSResourceFileMapper::Entry::~Entry()': the destructor:
      Python removes its C++ QQmlJSResourceFileMapper::Entry by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQmlJSResourceFileMapper::Entry is created at the first use,
      not by 'QQmlJSResourceFileMapper::Entry(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSResourceFileMapper::Entry back gives a copy
      the ritual made for Python, in a new cute
      QQmlJSResourceFileMapper::Entry.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSResourceFileMapper::Entry'

    #  Qt's '~QQmlJSResourceFileMapper::Entry()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlJSResourceFileMapper::Entry
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QQmlJSResourceFileMapper5EntryD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QQmlJSResourceFileMapper::Entry::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsresourcefilemapper-entry.html#isValid
      """
      #  bool QQmlJSResourceFileMapper::Entry::isValid() const
      return self.uglySide.call(
          'ritual_ZNK24QQmlJSResourceFileMapper5Entry7isValidEv',
      )

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

  class Filter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSResourceFileMapper::Filter: a plain Python
    object standing in front of one C++ QQmlJSResourceFileMapper::Filter.

    C++ hands a QQmlJSResourceFileMapper::Filter around as a copy, so every
    C++ QQmlJSResourceFileMapper::Filter behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQmlJSResourceFileMapper::Filter yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSResourceFileMapper::Filter::~Filter()': the destructor:
      Python removes its C++ QQmlJSResourceFileMapper::Filter by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQmlJSResourceFileMapper::Filter is created at the first use,
      not by 'QQmlJSResourceFileMapper::Filter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSResourceFileMapper::Filter back gives a copy
      the ritual made for Python, in a new cute
      QQmlJSResourceFileMapper::Filter.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSResourceFileMapper::Filter'

    #  Qt's '~QQmlJSResourceFileMapper::Filter()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlJSResourceFileMapper::Filter
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QQmlJSResourceFileMapper6FilterD1Ev'

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

  @staticmethod
  def allQmlJSFilter() -> Filter:
    """
    Calls Qt's 'Filter QQmlJSResourceFileMapper::allQmlJSFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#allQmlJSFilter

    Returns
    -------

    Filter
      A new cute QQmlJSResourceFileMapper::Filter around the copy Qt gave
      back. Python owns it.
    """
    #  Filter QQmlJSResourceFileMapper::allQmlJSFilter()
    address = Rituals.call(
        'ritual_ZN24QQmlJSResourceFileMapper14allQmlJSFilterEv',
    )
    return QQmlJSResourceFileMapper.Filter._cuteOwning(address)

  @staticmethod
  @overload(str)
  def localFileFilter(file: str) -> Filter:
    """
    Calls Qt's 'Filter QQmlJSResourceFileMapper::localFileFilter(const
    QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#localFileFilter

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Filter
      A new cute QQmlJSResourceFileMapper::Filter around the copy Qt gave
      back. Python owns it.
    """
    #  Filter QQmlJSResourceFileMapper::localFileFilter(const QString &file)
    address = Rituals.call(
        'ritual_ZN24QQmlJSResourceFileMapper15localFileFilterERK7QString',
        file,
    )
    return QQmlJSResourceFileMapper.Filter._cuteOwning(address)

  @staticmethod
  @overload(str)
  def resourceFileFilter(file: str) -> Filter:
    """
    Calls Qt's 'Filter QQmlJSResourceFileMapper::resourceFileFilter(const
    QString &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#resourceFileFilter

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Filter
      A new cute QQmlJSResourceFileMapper::Filter around the copy Qt gave
      back. Python owns it.
    """
    #  Filter QQmlJSResourceFileMapper::resourceFileFilter(const QString
    #      &file)
    address = Rituals.call(
        'ritual_ZN24QQmlJSResourceFileMapper18resourceFileFilterERK7QString',
        file,
    )
    return QQmlJSResourceFileMapper.Filter._cuteOwning(address)

  @staticmethod
  @overload(str)
  def resourceQmlDirectoryFilter(directory: str) -> Filter:
    """
    Calls Qt's 'Filter
    QQmlJSResourceFileMapper::resourceQmlDirectoryFilter(const QString
    &directory)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Filter
      A new cute QQmlJSResourceFileMapper::Filter around the copy Qt gave
      back. Python owns it.
    """
    #  Filter QQmlJSResourceFileMapper::resourceQmlDirectoryFilter(const
    #      QString &directory)
    address = Rituals.call(
        'ritual_ZN24QQmlJSResourceFileMapper26resourceQmlDirectoryFilterERK'
        '7QString',
        directory,
    )
    return QQmlJSResourceFileMapper.Filter._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSResourceFileMapper'

  #  Qt's '~QQmlJSResourceFileMapper()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlJSResourceFileMapper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QQmlJSResourceFileMapperD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSResourceFileMapper::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#isEmpty
    """
    #  bool QQmlJSResourceFileMapper::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK24QQmlJSResourceFileMapper7isEmptyEv',
    )

  @overload(str)
  def isFile(self, resourcePath: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSResourceFileMapper::isFile(QStringView
    resourcePath) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#isFile

    Parameters
    ----------

    resourcePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSResourceFileMapper::isFile(QStringView resourcePath) const
    return self.uglySide.call(
        'ritual_ZNK24QQmlJSResourceFileMapper6isFileE11QStringView',
        resourcePath,
    )

  @overload(Filter)
  def filePaths(self, filter: Filter) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSResourceFileMapper::filePaths(const Filter
    &filter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#filePaths

    Parameters
    ----------

    filter : Filter
      Passed on as a value: Qt reads the C++
      QQmlJSResourceFileMapper::Filter, which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSResourceFileMapper::filePaths(const Filter &filter)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlJSResourceFileMapper9filePathsERKNS_6FilterE',
        self._valueOf(filter),
    )
    return QStringList._cuteOwning(address)

  @overload(Filter)
  def resourcePaths(self, filter: Filter) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSResourceFileMapper::resourcePaths(const
    Filter &filter) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#resourcePaths

    Parameters
    ----------

    filter : Filter
      Passed on as a value: Qt reads the C++
      QQmlJSResourceFileMapper::Filter, which stays Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSResourceFileMapper::resourcePaths(const Filter
    #      &filter) const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlJSResourceFileMapper13resourcePathsERKNS_6FilterE',
        self._valueOf(filter),
    )
    return QStringList._cuteOwning(address)

  @overload(Filter)
  def entry(self, filter: Filter) -> Entry:
    """
    Calls Qt's 'Entry QQmlJSResourceFileMapper::entry(const Filter &filter)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html#entry

    Parameters
    ----------

    filter : Filter
      Passed on as a value: Qt reads the C++
      QQmlJSResourceFileMapper::Filter, which stays Python's own.

    Returns
    -------

    Entry
      A new cute QQmlJSResourceFileMapper::Entry around the copy Qt gave
      back. Python owns it.
    """
    #  Entry QQmlJSResourceFileMapper::entry(const Filter &filter) const
    address = self.uglySide.call(
        'ritual_ZNK24QQmlJSResourceFileMapper5entryERKNS_6FilterE',
        self._valueOf(filter),
    )
    return QQmlJSResourceFileMapper.Entry._cuteOwning(address)

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

  @overload(QStringList)
  def __init__(self, resourceFiles: QStringList) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSResourceFileMapper::QQmlJSResourceFileMapper(const QStringList
    &resourceFiles)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsresourcefilemapper.html

    Parameters
    ----------

    resourceFiles : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QQmlJSResourceFileMapper::QQmlJSResourceFileMapper(const QStringList
    #      &resourceFiles)
    self._noteCreation(QQmlJSResourceFileMapper, lambda: Rituals.call(
        'ritual_ZN24QQmlJSResourceFileMapperC1ERK5QListI7QStringE',
        self._valueOf(resourceFiles),
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

  @staticmethod
  def filter(*__, **_) -> Never:
    """
    Qt's 'QList<Entry> QQmlJSResourceFileMapper::filter(const Filter &filter)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSResourceFileMapper.filter' has no cute function yet. Qt's "
        "'QList<Entry> QQmlJSResourceFileMapper::filter(const Filter "
        "&filter) const': gives a type Python has no way to take yet.")

  @staticmethod
  def populateFromQrcFile(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSResourceFileMapper::populateFromQrcFile(QFile &file)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSResourceFileMapper.populateFromQrcFile' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSResourceFileMapper::populateFromQrcFile(QFile &file)': takes "
        "a type Python has no way to hand over yet.")
