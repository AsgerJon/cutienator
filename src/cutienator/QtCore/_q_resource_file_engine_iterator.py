"""
QResourceFileEngineIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qresource_iterator_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QResourceFileEngineIterator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QAbstractFileEngineIterator, QDir, QDirListing, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFileInfo


class QResourceFileEngineIterator(QAbstractFileEngineIterator):
  """
  The cute side of Qt's QResourceFileEngineIterator: a plain Python object
  standing in front of one C++ QResourceFileEngineIterator.

  It is built on the cute 'QAbstractFileEngineIterator', as Qt's
  QResourceFileEngineIterator is built on Qt's QAbstractFileEngineIterator,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QResourceFileEngineIterator that has a ritual and
  that Python can call so far, 3 names in all: 'advance', 'currentFileName',
  'currentFileInfo'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QResourceFileEngineIterator::~QResourceFileEngineIterator()': the
    destructor: Python never removes a C++ QResourceFileEngineIterator.

  What to expect
  --------------

  - The C++ QResourceFileEngineIterator is created at the first use, not by
    'QResourceFileEngineIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QResourceFileEngineIterator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QResourceFileEngineIterator'

  #  A C++ QResourceFileEngineIterator Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QResourceFileEngineIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentFileName(self) -> str:
    """
    Calls Qt's 'QString QResourceFileEngineIterator::currentFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengineiterator.html#currentFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QResourceFileEngineIterator::currentFileName() const
    ritual = 'ritual_ZNK27QResourceFileEngineIterator15currentFileNameEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QResourceFileEngineIterator15currentFileNameEv')
    return self.uglySide.call(ritual)

  def currentFileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QResourceFileEngineIterator::currentFileInfo()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengineiterator.html#currentFileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QResourceFileEngineIterator::currentFileInfo() const
    ritual = 'ritual_ZNK27QResourceFileEngineIterator15currentFileInfoEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QResourceFileEngineIterator15currentFileInfoEv')
    address = self.uglySide.call(ritual)
    from . import QFileInfo
    return QFileInfo._cuteOwning(address)

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
      filterNames: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QResourceFileEngineIterator::QResourceFileEngineIterator(const QString
    &path, QDir::Filters filters, const QStringList &filterNames)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengineiterator.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    filters : QDir.Filters
      Passed on as its number.

    filterNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QResourceFileEngineIterator::QResourceFileEngineIterator(const QString
    #      &path, QDir::Filters filters, const QStringList &filterNames)
    self._noteCreation(QResourceFileEngineIterator, lambda: Rituals.call(
        'ritual_ZN27QResourceFileEngineIteratorC1ERK7QString6QFlagsIN4QDir6'
        'FilterEERK5QListIS0_E',
        path, filters.value, self._valueOf(filterNames),
    ))

  @overload(str, QDirListing.IteratorFlags, QStringList)
  def __init__(
      self,
      path: str,
      filters: QDirListing.IteratorFlags,
      filterNames: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QResourceFileEngineIterator::QResourceFileEngineIterator(const QString
    &path, QDirListing::IteratorFlags filters, const QStringList
    &filterNames)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengineiterator.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    filters : QDirListing.IteratorFlags
      Passed on as its number.

    filterNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QResourceFileEngineIterator::QResourceFileEngineIterator(const QString
    #      &path, QDirListing::IteratorFlags filters, const QStringList
    #      &filterNames)
    self._noteCreation(QResourceFileEngineIterator, lambda: Rituals.call(
        'ritual_ZN27QResourceFileEngineIteratorC1ERK7QString6QFlagsIN11QDir'
        'Listing12IteratorFlagEERK5QListIS0_E',
        path, filters.value, self._valueOf(filterNames),
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
    Calls Qt's 'bool QResourceFileEngineIterator::advance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qresourcefileengineiterator.html#advance
    """
    #  bool QResourceFileEngineIterator::advance()
    ritual = 'ritual_ZN27QResourceFileEngineIterator7advanceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QResourceFileEngineIterator7advanceEv'
    return self.uglySide.call(ritual)
