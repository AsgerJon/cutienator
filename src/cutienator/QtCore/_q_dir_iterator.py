"""
QDirIterator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdiriterator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QDir

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFileInfo


class QDirIterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDirIterator: a plain Python object standing in front
  of one C++ QDirIterator.

  What exists
  -----------

  Every function of Qt's QDirIterator that has a ritual and that Python can
  call so far, 7 names in all: 'next', 'nextFileInfo', 'hasNext', 'fileName',
  'filePath', 'fileInfo', 'path'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDirIterator::~QDirIterator()': the destructor: Python never
    removes a C++ QDirIterator.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 2 forbidden; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QDirIterator is created at the first use, not by
    'QDirIterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDirIterator.
  """

  #  The enums Qt writes inside QDirIterator, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class IteratorFlag(CuteFlags):
    """
    The flags enum 'QDirIterator::IteratorFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QDirIterator::IteratorFlags'.
    """

    NoIteratorFlags = 0x0
    FollowSymlinks = 0x1
    Subdirectories = 0x2

  IteratorFlags = IteratorFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDirIterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasNext(self) -> bool:
    """
    Calls Qt's 'bool QDirIterator::hasNext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#hasNext
    """
    #  bool QDirIterator::hasNext() const
    return self.uglySide.call('ritual_ZNK12QDirIterator7hasNextEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QDirIterator::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirIterator::fileName() const
    return self.uglySide.call('ritual_ZNK12QDirIterator8fileNameEv')

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QDirIterator::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirIterator::filePath() const
    return self.uglySide.call('ritual_ZNK12QDirIterator8filePathEv')

  def fileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QDirIterator::fileInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#fileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QDirIterator::fileInfo() const
    address = self.uglySide.call('ritual_ZNK12QDirIterator8fileInfoEv')
    from . import QFileInfo
    return QFileInfo._cuteOwning(address)

  def path(self) -> str:
    """
    Calls Qt's 'QString QDirIterator::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirIterator::path() const
    return self.uglySide.call('ritual_ZNK12QDirIterator4pathEv')

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

  @overload(QDir)
  @overload(QDir, IteratorFlags)
  def __init__(
      self,
      dir: QDir,
      flags: IteratorFlags = IteratorFlags.NoIteratorFlags,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDirIterator::QDirIterator(const QDir
    &dir, IteratorFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#QDirIterator

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    flags : IteratorFlags
      Passed on as its number. May be left out, as in Qt: it is then
      IteratorFlags.NoIteratorFlags.
    """
    #  QDirIterator::QDirIterator(const QDir &dir, IteratorFlags flags)
    self._noteCreation(QDirIterator, lambda: Rituals.call(
        'ritual_ZN12QDirIteratorC1ERK4QDir6QFlagsINS_12IteratorFlagEE',
        self._valueOf(dir), flags.value,
    ))

  @overload(str)
  @overload(str, IteratorFlags)
  def __init__(
      self,
      path: str,
      flags: IteratorFlags = IteratorFlags.NoIteratorFlags,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDirIterator::QDirIterator(const QString
    &path, IteratorFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#QDirIterator

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    flags : IteratorFlags
      Passed on as its number. May be left out, as in Qt: it is then
      IteratorFlags.NoIteratorFlags.
    """
    #  QDirIterator::QDirIterator(const QString &path, IteratorFlags flags)
    self._noteCreation(QDirIterator, lambda: Rituals.call(
        'ritual_ZN12QDirIteratorC1ERK7QString6QFlagsINS_12IteratorFlagEE',
        path, flags.value,
    ))

  @overload(str, QDir.Filters)
  @overload(str, QDir.Filters, IteratorFlags)
  def __init__(
      self,
      path: str,
      filter: QDir.Filters,
      flags: IteratorFlags = IteratorFlags.NoIteratorFlags,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDirIterator::QDirIterator(const QString
    &path, QDir::Filters filter, IteratorFlags flags)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#QDirIterator

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    filter : QDir.Filters
      Passed on as its number.

    flags : IteratorFlags
      Passed on as its number. May be left out, as in Qt: it is then
      IteratorFlags.NoIteratorFlags.
    """
    #  QDirIterator::QDirIterator(const QString &path, QDir::Filters filter,
    #      IteratorFlags flags)
    self._noteCreation(QDirIterator, lambda: Rituals.call(
        'ritual_ZN12QDirIteratorC1ERK7QString6QFlagsIN4QDir6FilterEES3_INS_'
        '12IteratorFlagEE',
        path, filter.value, flags.value,
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

  def next(self) -> str:
    """
    Calls Qt's 'QString QDirIterator::next()'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#next

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDirIterator::next()
    return self.uglySide.call('ritual_ZN12QDirIterator4nextEv')

  def nextFileInfo(self) -> QFileInfo:
    """
    Calls Qt's 'QFileInfo QDirIterator::nextFileInfo()'.

    Qt's own words: https://doc.qt.io/qt-6/qdiriterator.html#nextFileInfo

    Returns
    -------

    QFileInfo
      A new cute QFileInfo around the copy Qt gave back. Python owns it.
    """
    #  QFileInfo QDirIterator::nextFileInfo()
    address = self.uglySide.call('ritual_ZN12QDirIterator12nextFileInfoEv')
    from . import QFileInfo
    return QFileInfo._cuteOwning(address)
