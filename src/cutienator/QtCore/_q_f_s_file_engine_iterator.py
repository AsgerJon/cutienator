"""
QFSFileEngineIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfsfileengine_iterator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QFSFileEngineIterator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QAbstractFileEngineIterator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QFileInfo


class QFSFileEngineIterator(QAbstractFileEngineIterator):
  """
  The cute side of Qt's QFSFileEngineIterator: a plain Python object standing
  in front of one C++ QFSFileEngineIterator.

  It is built on the cute 'QAbstractFileEngineIterator', as Qt's
  QFSFileEngineIterator is built on Qt's QAbstractFileEngineIterator, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QFSFileEngineIterator that has a ritual and that
  Python can call so far, 3 names in all: 'advance', 'currentFileName',
  'currentFileInfo'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFSFileEngineIterator::~QFSFileEngineIterator()': the destructor:
    Python never removes a C++ QFSFileEngineIterator.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 leans on 'QFileSystemIterator.

  What to expect
  --------------

  - The C++ QFSFileEngineIterator is created at the first use, not by
    'QFSFileEngineIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFSFileEngineIterator.
  - Each name of Qt's QFSFileEngineIterator that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFSFileEngineIterator'

  #  A C++ QFSFileEngineIterator Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFSFileEngineIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentFileName(self) -> str:
    """
    Calls Qt's 'QString QFSFileEngineIterator::currentFileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengineiterator.html#currentFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFSFileEngineIterator::currentFileName() const
    ritual = 'ritual_ZNK21QFSFileEngineIterator15currentFileNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QFSFileEngineIterator15currentFileNameEv'
    return self.uglySide.call(ritual)

  def currentFileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QFSFileEngineIterator::currentFileInfo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfsfileengineiterator.html#currentFileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QFSFileEngineIterator::currentFileInfo() const
    ritual = 'ritual_ZNK21QFSFileEngineIterator15currentFileInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QFSFileEngineIterator15currentFileInfoEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QFSFileEngineIterator::QFSFileEngineIterator(const QString &path,
      QDir::Filters filters, const QStringList &filterNames)': leans on
      'QFileSystemIterator::QFileSystemIterator(QFileSystemEntry const&,
      QFlags<QDir::Filter>)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QFSFileEngineIterator::QFSFileEngineIterator(const QString &path,
      QDirListing::IteratorFlags filters, const QStringList &filterNames)':
      leans on 'QFileSystemIterator::QFileSystemIterator(QFileSystemEntry
      const&, QFlags<QDirListing::IteratorFlag>)', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFSFileEngineIterator.__init__' has no cute function yet. Qt's "
        "'QFSFileEngineIterator::QFSFileEngineIterator(const QString &path, "
        "QDir::Filters filters, const QStringList &filterNames)': leans on "
        "'QFileSystemIterator::QFileSystemIterator(QFileSystemEntry const&, "
        "QFlags<QDir::Filter>)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken. Qt's "
        "'QFSFileEngineIterator::QFSFileEngineIterator(const QString &path, "
        "QDirListing::IteratorFlags filters, const QStringList "
        "&filterNames)': leans on "
        "'QFileSystemIterator::QFileSystemIterator(QFileSystemEntry const&, "
        "QFlags<QDirListing::IteratorFlag>)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
    Calls Qt's 'bool QFSFileEngineIterator::advance()'.

    Qt's own words: https://doc.qt.io/qt-6/qfsfileengineiterator.html#advance
    """
    #  bool QFSFileEngineIterator::advance()
    return self.uglySide.call('ritual_ZN21QFSFileEngineIterator7advanceEv')
