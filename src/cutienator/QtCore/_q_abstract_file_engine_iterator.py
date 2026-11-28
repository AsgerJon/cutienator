"""
QAbstractFileEngineIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAbstractFileEngineIterator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QDir, QDirListing, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFileInfo


class QAbstractFileEngineIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractFileEngineIterator: a plain Python object
  standing in front of one C++ QAbstractFileEngineIterator.

  What exists
  -----------

  Every function of Qt's QAbstractFileEngineIterator that has a ritual and
  that Python can call so far, 7 names in all: 'advance', 'path',
  'nameFilters', 'filters', 'currentFileName', 'currentFileInfo',
  'currentFilePath'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractFileEngineIterator::~QAbstractFileEngineIterator()': the
    destructor: Python never removes a C++ QAbstractFileEngineIterator.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QAbstractFileEngineIterator is created at the first use, not by
    'QAbstractFileEngineIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFileEngineIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFileEngineIterator'

  #  A C++ QAbstractFileEngineIterator Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractFileEngineIterator'

  #  The functions Qt calls itself that QAbstractFileEngineIterator is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'advance': (
          ('_ZN27QAbstractFileEngineIterator7advanceEv',
           ('bool', 'number', ''),
           ()),
      ),
      'currentFileName': (
          ('_ZNK27QAbstractFileEngineIterator15currentFileNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'currentFileInfo': (
          ('_ZNK27QAbstractFileEngineIterator15currentFileInfoEv',
           ('address', 'value', 'QtCore:QFileInfo'),
           ()),
      ),
      'currentFilePath': (
          ('_ZNK27QAbstractFileEngineIterator15currentFilePathEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def path(self) -> str:
    """
    Calls Qt's 'QString QAbstractFileEngineIterator::path() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileEngineIterator::path() const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractFileEngineIterator4pathEv',
    )

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QAbstractFileEngineIterator::nameFilters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QAbstractFileEngineIterator::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractFileEngineIterator11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  def filters(self) -> QDir.Filters:
    """
    Calls Qt's 'QDir::Filters QAbstractFileEngineIterator::filters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#filters

    Returns
    -------

    QDir.Filters
      The value standing for the combination Qt gave back.
    """
    #  QDir::Filters QAbstractFileEngineIterator::filters() const
    return QDir.Filters(self.uglySide.call(
        'ritual_ZNK27QAbstractFileEngineIterator7filtersEv',
    ))

  def currentFileName(self) -> str:
    """
    Calls Qt's 'QString QAbstractFileEngineIterator::currentFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#currentFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileEngineIterator::currentFileName() const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractFileEngineIterator15currentFileNameEv',
    )

  def currentFileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QAbstractFileEngineIterator::currentFileInfo()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#currentFileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QAbstractFileEngineIterator::currentFileInfo() const
    ritual = 'ritual_ZNK27QAbstractFileEngineIterator15currentFileInfoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QAbstractFileEngineIterator15currentFileInfoEv')
    address = self.uglySide.call(ritual)
    from . import QFileInfo
    return QFileInfo._cuteOwning(address)

  def currentFilePath(self) -> str:
    """
    Calls Qt's 'QString QAbstractFileEngineIterator::currentFilePath()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#currentFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileEngineIterator::currentFilePath() const
    ritual = 'ritual_ZNK27QAbstractFileEngineIterator15currentFilePathEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QAbstractFileEngineIterator15currentFilePathEv')
    return self.uglySide.call(ritual)

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

  @overload(str, QDir.Filters, QStringList)
  def __init__(
      self,
      path: str,
      filters: QDir.Filters,
      nameFilters: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractFileEngineIterator::QAbstractFileEngineIterator(const QString
    &path, QDir::Filters filters, const QStringList &nameFilters)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    filters : QDir.Filters
      Passed on as its number.

    nameFilters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QAbstractFileEngineIterator::QAbstractFileEngineIterator(const QString
    #      &path, QDir::Filters filters, const QStringList &nameFilters)
    self._noteCreation(QAbstractFileEngineIterator, lambda: Rituals.call(
        'ritual_ZN27QAbstractFileEngineIteratorC1ERK7QString6QFlagsIN4QDir6'
        'FilterEERK5QListIS0_E',
        path, filters.value, self._valueOf(nameFilters),
    ))

  @overload(str, QDirListing.IteratorFlags, QStringList)
  def __init__(
      self,
      path: str,
      filters: QDirListing.IteratorFlags,
      nameFilters: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractFileEngineIterator::QAbstractFileEngineIterator(const QString
    &path, QDirListing::IteratorFlags filters, const QStringList
    &nameFilters)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    filters : QDirListing.IteratorFlags
      Passed on as its number.

    nameFilters : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QAbstractFileEngineIterator::QAbstractFileEngineIterator(const QString
    #      &path, QDirListing::IteratorFlags filters, const QStringList
    #      &nameFilters)
    self._noteCreation(QAbstractFileEngineIterator, lambda: Rituals.call(
        'ritual_ZN27QAbstractFileEngineIteratorC1ERK7QString6QFlagsIN11QDir'
        'Listing12IteratorFlagEERK5QListIS0_E',
        path, filters.value, self._valueOf(nameFilters),
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

  def advance(self) -> bool:
    """
    Calls Qt's 'bool QAbstractFileEngineIterator::advance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileengineiterator.html#advance
    """
    #  bool QAbstractFileEngineIterator::advance()
    return self.uglySide.call(
        'ritual_ZN27QAbstractFileEngineIterator7advanceEv',
    )
