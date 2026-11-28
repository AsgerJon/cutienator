"""
QTemporaryFilePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtemporaryfile_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTemporaryFilePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..occult import Rituals
from . import QFilePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractFileEngine, QTemporaryFile


class QTemporaryFilePrivate(QFilePrivate):
  """
  The cute side of Qt's QTemporaryFilePrivate: a plain Python object standing
  in front of one C++ QTemporaryFilePrivate.

  It is built on the cute 'QFilePrivate', as Qt's QTemporaryFilePrivate is
  built on Qt's QFilePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTemporaryFilePrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'engine',
  'materializeUnnamedFile', 'defaultTemplateName'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTemporaryFile *QTemporaryFilePrivate::q_func() const': takes
    in Python what 'QTemporaryFile *QTemporaryFilePrivate::q_func()' takes.
  - Qt's 'QTemporaryFilePrivate::~QTemporaryFilePrivate()': the destructor:
    Python never removes a C++ QTemporaryFilePrivate.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 3 leans on 'QFileSystemEntry; 1 leans on
  'QFileDevicePrivate.

  What to expect
  --------------

  - The C++ QTemporaryFilePrivate is created at the first use, not by
    'QTemporaryFilePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTemporaryFilePrivate.
  - Each name of Qt's QTemporaryFilePrivate that has no cute function yet,
    '__init__', 'rename', 'resetFileEngine', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def defaultTemplateName() -> str:
    """
    Calls Qt's 'QString QTemporaryFilePrivate::defaultTemplateName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfileprivate.html#defaultTemplateName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryFilePrivate::defaultTemplateName()
    return Rituals.call(
        'ritual_ZN21QTemporaryFilePrivate19defaultTemplateNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTemporaryFilePrivate'

  #  A C++ QTemporaryFilePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTemporaryFilePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def engine(self) -> Optional[QAbstractFileEngine]:
    """
    Calls Qt's 'QAbstractFileEngine *QTemporaryFilePrivate::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileprivate.html#engine

    Returns
    -------

    Optional[QAbstractFileEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileEngine *QTemporaryFilePrivate::engine() const
    address = self.uglySide.call(
        'ritual_ZNK21QTemporaryFilePrivate6engineEv',
    )
    from . import QAbstractFileEngine
    return QAbstractFileEngine._cuteAt(address)

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
    - Qt's 'QTemporaryFilePrivate::QTemporaryFilePrivate()': leans on
      'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'QTemporaryFilePrivate::QTemporaryFilePrivate(const QString
      &templateNameIn)': leans on 'QFileSystemEntry::QFileSystemEntry(QString
      const&)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTemporaryFilePrivate.__init__' has no cute function yet. Qt's "
        "'QTemporaryFilePrivate::QTemporaryFilePrivate()': leans on "
        "'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken. Qt's "
        "'QTemporaryFilePrivate::QTemporaryFilePrivate(const QString "
        "&templateNameIn)': leans on "
        "'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[QTemporaryFile]:
    """
    Calls Qt's 'QTemporaryFile *QTemporaryFilePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporaryfileprivate.html#q_func

    Returns
    -------

    Optional[QTemporaryFile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTemporaryFile *QTemporaryFilePrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QTemporaryFilePrivate6q_funcEv')
    from . import QTemporaryFile
    return QTemporaryFile._cuteAt(address)

  def materializeUnnamedFile(self) -> None:
    """
    Calls Qt's 'void QTemporaryFilePrivate::materializeUnnamedFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtemporaryfileprivate.html#materializeUnnamedFile
    """
    #  void QTemporaryFilePrivate::materializeUnnamedFile()
    self.uglySide.call(
        'ritual_ZN21QTemporaryFilePrivate22materializeUnnamedFileEv',
    )

  @staticmethod
  def rename(*__, **_) -> Never:
    """
    Qt's 'bool QTemporaryFilePrivate::rename(const QString &newName, bool
    overwrite)': leans on
    'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QTemporaryFilePrivate.rename' has no cute function yet. Qt's "
        "'bool QTemporaryFilePrivate::rename(const QString &newName, bool "
        "overwrite)': leans on "
        "'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def resetFileEngine(*__, **_) -> Never:
    """
    Qt's 'void QTemporaryFilePrivate::resetFileEngine() const': leans on
    'QFileSystemEntry::QFileSystemEntry(QString const&)', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTemporaryFilePrivate.resetFileEngine' has no cute function yet. "
        "Qt's 'void QTemporaryFilePrivate::resetFileEngine() const': leans "
        "on 'QFileSystemEntry::QFileSystemEntry(QString const&)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
