"""
QFileInfoPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfileinfo_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QFileInfoPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractFileEngine, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QFileInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileInfoPrivate(QSharedData):
  """
  The cute side of Qt's QFileInfoPrivate: a plain Python object standing in
  front of one C++ QFileInfoPrivate.

  It is built on the cute 'QSharedData', as Qt's QFileInfoPrivate is built on
  Qt's QSharedData, and has everything that class has.

  C++ hands a QFileInfoPrivate around as a copy, so every C++
  QFileInfoPrivate behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFileInfoPrivate that has a ritual and that Python
  can call so far, 6 names in all: 'get', 'clearFlags', 'clear',
  'getFileFlags', 'getCachedFlag', 'setCachedFlag'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTime &QFileInfoPrivate::getFileTime(QFile::FileTime a0)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QFileInfoPrivate::~QFileInfoPrivate()': the destructor: Python
    removes its C++ QFileInfoPrivate by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 4 leans on 'QFileSystemEngine; 2 a
  template; 1 the compiler refuses its ritual as it would be written here; 1
  leans on 'QFileSystemEntry.

  What to expect
  --------------

  - The C++ QFileInfoPrivate is created at the first use, not by
    'QFileInfoPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFileInfoPrivate back gives a copy the ritual made
    for Python, in a new cute QFileInfoPrivate.
  - Each name of Qt's QFileInfoPrivate that has no cute function yet,
    'checkAttribute', 'getFileName', 'getFileOwner', 'getFileTime', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QFileInfo)
  @overload(NoneType)
  def get(fi: Optional[QFileInfo]) -> Optional[QFileInfoPrivate]:
    """
    Calls Qt's 'QFileInfoPrivate *QFileInfoPrivate::get(QFileInfo *fi)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfoprivate.html#get

    Parameters
    ----------

    fi : Optional[QFileInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QFileInfoPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileInfoPrivate *QFileInfoPrivate::get(QFileInfo *fi)
    address = Rituals.call(
        'ritual_ZN16QFileInfoPrivate3getEP9QFileInfo',
        CuteMixin._addressOf(fi),
    )
    return QFileInfoPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileInfoPrivate'

  #  Qt's '~QFileInfoPrivate()'. Naming it makes this a value class: Python
  #  owns every C++ QFileInfoPrivate behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QFileInfoPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractFileEngine.FileFlags)
  def getFileFlags(self, a0: QAbstractFileEngine.FileFlags) -> int:
    """
    Calls Qt's 'uint
    QFileInfoPrivate::getFileFlags(QAbstractFileEngine::FileFlags a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfoprivate.html#getFileFlags

    Parameters
    ----------

    a0 : QAbstractFileEngine.FileFlags
      Passed on as its number.
    """
    #  uint QFileInfoPrivate::getFileFlags(QAbstractFileEngine::FileFlags a0)
    #      const
    return self.uglySide.call(
        'ritual_ZNK16QFileInfoPrivate12getFileFlagsE6QFlagsIN19QAbstractFil'
        'eEngine8FileFlagEE',
        a0.value,
    )

  @overload(int)
  def getCachedFlag(self, c: int) -> bool:
    """
    Calls Qt's 'bool QFileInfoPrivate::getCachedFlag(uint c) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfoprivate.html#getCachedFlag

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  bool QFileInfoPrivate::getCachedFlag(uint c) const
    return self.uglySide.call(
        'ritual_ZNK16QFileInfoPrivate13getCachedFlagEj', c,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCachedFlag(self, c: int) -> None:
    """
    Calls Qt's 'void QFileInfoPrivate::setCachedFlag(uint c) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfoprivate.html#setCachedFlag

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QFileInfoPrivate::setCachedFlag(uint c) const
    self.uglySide.call('ritual_ZNK16QFileInfoPrivate13setCachedFlagEj', c)

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
    Notes what was given, for Qt's 'QFileInfoPrivate::QFileInfoPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileinfoprivate.html#QFileInfoPrivate
    """
    #  QFileInfoPrivate::QFileInfoPrivate()
    self._noteCreation(QFileInfoPrivate, lambda: Rituals.call(
        'ritual_ZN16QFileInfoPrivateC1Ev',
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

  def clearFlags(self) -> None:
    """
    Calls Qt's 'void QFileInfoPrivate::clearFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfoprivate.html#clearFlags
    """
    #  void QFileInfoPrivate::clearFlags() const
    self.uglySide.call('ritual_ZNK16QFileInfoPrivate10clearFlagsEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QFileInfoPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfoprivate.html#clear
    """
    #  void QFileInfoPrivate::clear()
    self.uglySide.call('ritual_ZN16QFileInfoPrivate5clearEv')

  @staticmethod
  def checkAttribute(*__, **_) -> Never:
    """
    Qt's 'QFileInfoPrivate::checkAttribute': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QFileInfoPrivate.checkAttribute' has no cute function yet. Qt's "
        "'QFileInfoPrivate::checkAttribute': a template: a pattern and no "
        "single function.")

  @staticmethod
  def getFileName(*__, **_) -> Never:
    """
    Qt's 'QString QFileInfoPrivate::getFileName(QAbstractFileEngine::FileName
    a0) const': leans on 'QFileSystemEngine::absoluteName(QFileSystemEntry
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFileInfoPrivate.getFileName' has no cute function yet. Qt's "
        "'QString "
        "QFileInfoPrivate::getFileName(QAbstractFileEngine::FileName a0) "
        "const': leans on 'QFileSystemEngine::absoluteName(QFileSystemEntry "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def getFileOwner(*__, **_) -> Never:
    """
    Qt's 'QString
    QFileInfoPrivate::getFileOwner(QAbstractFileEngine::FileOwner own)
    const': leans on 'QFileSystemEngine::fillMetaData(QFileSystemEntry
    const&, QFileSystemMetaData&,
    QFlags<QFileSystemMetaData::MetaDataFlag>)', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QFileInfoPrivate.getFileOwner' has no cute function yet. Qt's "
        "'QString "
        "QFileInfoPrivate::getFileOwner(QAbstractFileEngine::FileOwner own) "
        "const': leans on 'QFileSystemEngine::fillMetaData(QFileSystemEntry "
        "const&, QFileSystemMetaData&, "
        "QFlags<QFileSystemMetaData::MetaDataFlag>)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def getFileTime(*__, **_) -> Never:
    """
    Qt's 'QDateTime &QFileInfoPrivate::getFileTime(QFile::FileTime a0)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileInfoPrivate.getFileTime' has no cute function yet. Qt's "
        "'QDateTime &QFileInfoPrivate::getFileTime(QFile::FileTime a0) "
        "const': takes a type Python has no way to hand over yet.")
