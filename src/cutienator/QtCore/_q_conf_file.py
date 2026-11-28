"""
QConfFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QConfFile to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute
from . import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QConfFile(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QConfFile: a plain Python object standing in front of
  one C++ QConfFile.

  What exists
  -----------

  Every function of Qt's QConfFile that has a ritual and that Python can call
  so far, 1 name in all: 'isWritable'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ParsedSettingsMap QConfFile::mergedKeyMap() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 8 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied; 1
  not a gap.

  What to expect
  --------------

  - The C++ QConfFile is created at the first use, not by 'QConfFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QConfFile.
  - Each name of Qt's QConfFile that has no cute function yet, '__init__',
    'clearCache', 'fromName', 'mergedKeyMap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QConfFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QConfFile::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qconffile.html#isWritable
    """
    #  bool QConfFile::isWritable() const
    return self.uglySide.call('ritual_ZNK9QConfFile10isWritableEv')

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
    - Qt's 'QConfFile::QConfFile(const QConfFile &a0)': cannot be called and
      cannot be called through the meta-object and cannot be copied: no
      header file has its code, Qt's source does not mark it or its class for
      use from outside Qt or writes it 'inline' or nowhere, and it is no
      signal, slot or invokable function giving back nothing, of a class
      built on QObject, and Qt's source has no code for it that could be told
      from the rest.
    - Qt's 'QConfFile::QConfFile(const QString &name, bool _userPerms)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'usedHashFunc'.
    """
    raise NotImplementedError(
        "'QConfFile.__init__' has no cute function yet. Qt's "
        "'QConfFile::QConfFile(const QConfFile &a0)': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest. Qt's "
        "'QConfFile::QConfFile(const QString &name, bool _userPerms)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'usedHashFunc'.")

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
  def clearCache(*__, **_) -> Never:
    """
    Qt's 'void QConfFile::clearCache()': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'settingsGlobalMutex'.
    """
    raise NotImplementedError(
        "'QConfFile.clearCache' has no cute function yet. Qt's 'void "
        "QConfFile::clearCache()': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'settingsGlobalMutex'.")

  @staticmethod
  def fromName(*__, **_) -> Never:
    """
    Qt's 'QConfFile *QConfFile::fromName(const QString &name, bool
    _userPerms)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'settingsGlobalMutex'.
    """
    raise NotImplementedError(
        "'QConfFile.fromName' has no cute function yet. Qt's 'QConfFile "
        "*QConfFile::fromName(const QString &name, bool _userPerms)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'settingsGlobalMutex'.")

  @staticmethod
  def mergedKeyMap(*__, **_) -> Never:
    """
    Qt's 'ParsedSettingsMap QConfFile::mergedKeyMap() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QConfFile.mergedKeyMap' has no cute function yet. Qt's "
        "'ParsedSettingsMap QConfFile::mergedKeyMap() const': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QConfFile *>': the list of QConfFile, which 'QList[QConfFile]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QConfFile.
QList.createKind(
    QConfFile, 'address',
    make='ritual_list_make_QConfFile_ptr',
    add='ritual_list_add_QConfFile_ptr',
    size='ritual_list_size_QConfFile_ptr',
    at='ritual_list_at_QConfFile_ptr',
    drop='ritual_list_drop_QConfFile_ptr',
)
