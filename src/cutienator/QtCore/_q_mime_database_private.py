"""
QMimeDatabasePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimedatabase_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeDatabasePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QMimeDatabasePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeDatabasePrivate: a plain Python object standing
  in front of one C++ QMimeDatabasePrivate.

  What exists
  -----------

  Every function of Qt's QMimeDatabasePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'defaultMimeType', 'shouldCheck',
  'fallbackParent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMimeDatabasePrivate::~QMimeDatabasePrivate()': the destructor:
    Python never removes a C++ QMimeDatabasePrivate.

  What has no ritual
  ------------------

  26 of the 31 functions Qt declares: 17 leans on 'QMimeXMLProvider; 5 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 4 forbidden.

  What to expect
  --------------

  - The C++ QMimeDatabasePrivate is created at the first use, not by
    'QMimeDatabasePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeDatabasePrivate.
  - Each name of Qt's QMimeDatabasePrivate that has no cute function yet,
    'allMimeTypes', 'findByData', 'findByFileName', 'genericIcon',
    'globPatterns', 'icon', 'inherits', 'instance', 'listAliases',
    'loadProviders', 'localeComments', 'mimeInherits', 'mimeParents',
    'mimeTypeForData', 'mimeTypeForFile', 'mimeTypeForFileExtension',
    'mimeTypeForFileName', 'mimeTypeForFileNameAndData', 'mimeTypeForName',
    'parents', 'providers', 'resolveAlias', holds a function that raises
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
  __qt_class__ = 'QMimeDatabasePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultMimeType(self) -> str:
    """
    Calls Qt's 'const QString &QMimeDatabasePrivate::defaultMimeType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabaseprivate.html#defaultMimeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QMimeDatabasePrivate::defaultMimeType() const
    return self.uglySide.call(
        'ritual_ZNK20QMimeDatabasePrivate15defaultMimeTypeEv',
    )

  @overload(str)
  def fallbackParent(self, mimeTypeName: str) -> str:
    """
    Calls Qt's 'QString QMimeDatabasePrivate::fallbackParent(const QString
    &mimeTypeName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabaseprivate.html#fallbackParent

    Parameters
    ----------

    mimeTypeName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeDatabasePrivate::fallbackParent(const QString
    #      &mimeTypeName) const
    return self.uglySide.call(
        'ritual_ZNK20QMimeDatabasePrivate14fallbackParentERK7QString',
        mimeTypeName,
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QMimeDatabasePrivate::QMimeDatabasePrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabaseprivate.html#QMimeDatabasePrivate
    """
    #  QMimeDatabasePrivate::QMimeDatabasePrivate()
    self._noteCreation(QMimeDatabasePrivate, lambda: Rituals.call(
        'ritual_ZN20QMimeDatabasePrivateC1Ev',
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

  def shouldCheck(self) -> bool:
    """
    Calls Qt's 'bool QMimeDatabasePrivate::shouldCheck()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimedatabaseprivate.html#shouldCheck
    """
    #  bool QMimeDatabasePrivate::shouldCheck()
    return self.uglySide.call(
        'ritual_ZN20QMimeDatabasePrivate11shouldCheckEv',
    )

  @staticmethod
  def allMimeTypes(*__, **_) -> Never:
    """
    Qt's 'QList<QMimeType> QMimeDatabasePrivate::allMimeTypes()': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.allMimeTypes' has no cute function yet. Qt's "
        "'QList<QMimeType> QMimeDatabasePrivate::allMimeTypes()': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def findByData(*__, **_) -> Never:
    """
    Qt's 'QMimeType QMimeDatabasePrivate::findByData(const QByteArray &data,
    int *priorityPtr)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'plainTextMimeType'.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.findByData' has no cute function yet. Qt's "
        "'QMimeType QMimeDatabasePrivate::findByData(const QByteArray "
        "&data, int *priorityPtr)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'plainTextMimeType'.")

  @staticmethod
  def findByFileName(*__, **_) -> Never:
    """
    Qt's 'QMimeGlobMatchResult QMimeDatabasePrivate::findByFileName(const
    QString &fileName)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.findByFileName' has no cute function yet. "
        "Qt's 'QMimeGlobMatchResult "
        "QMimeDatabasePrivate::findByFileName(const QString &fileName)': "
        "leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def genericIcon(*__, **_) -> Never:
    """
    Qt's 'QString QMimeDatabasePrivate::genericIcon(const QString &name)':
    leans on 'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.genericIcon' has no cute function yet. Qt's "
        "'QString QMimeDatabasePrivate::genericIcon(const QString &name)': "
        "leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def globPatterns(*__, **_) -> Never:
    """
    Qt's 'QStringList QMimeDatabasePrivate::globPatterns(const QString
    &name)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.globPatterns' has no cute function yet. Qt's "
        "'QStringList QMimeDatabasePrivate::globPatterns(const QString "
        "&name)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def icon(*__, **_) -> Never:
    """
    Qt's 'QString QMimeDatabasePrivate::icon(const QString &name)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.icon' has no cute function yet. Qt's "
        "'QString QMimeDatabasePrivate::icon(const QString &name)': leans "
        "on 'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def inherits(*__, **_) -> Never:
    """
    Qt's 'bool QMimeDatabasePrivate::inherits(const QString &mime, const
    QString &parent)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.inherits' has no cute function yet. Qt's "
        "'bool QMimeDatabasePrivate::inherits(const QString &mime, const "
        "QString &parent)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def instance(*__, **_) -> Never:
    """
    Qt's 'QMimeDatabasePrivate *QMimeDatabasePrivate::instance()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'staticQMimeDatabase';
    did you mean 'QMimeDatabase'?.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.instance' has no cute function yet. Qt's "
        "'QMimeDatabasePrivate *QMimeDatabasePrivate::instance()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'staticQMimeDatabase'; did you mean 'QMimeDatabase'?.")

  @staticmethod
  def listAliases(*__, **_) -> Never:
    """
    Qt's 'QStringList QMimeDatabasePrivate::listAliases(const QString
    &mimeName)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.listAliases' has no cute function yet. Qt's "
        "'QStringList QMimeDatabasePrivate::listAliases(const QString "
        "&mimeName)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def loadProviders(*__, **_) -> Never:
    """
    Qt's 'void QMimeDatabasePrivate::loadProviders()': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.loadProviders' has no cute function yet. "
        "Qt's 'void QMimeDatabasePrivate::loadProviders()': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def localeComments(*__, **_) -> Never:
    """
    Qt's 'QMimeTypePrivate::LocaleHash
    QMimeDatabasePrivate::localeComments(const QString &name)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.localeComments' has no cute function yet. "
        "Qt's 'QMimeTypePrivate::LocaleHash "
        "QMimeDatabasePrivate::localeComments(const QString &name)': leans "
        "on 'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mimeInherits(*__, **_) -> Never:
    """
    Qt's 'bool QMimeDatabasePrivate::mimeInherits(const QString &mime, const
    QString &parent)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeInherits' has no cute function yet. Qt's "
        "'bool QMimeDatabasePrivate::mimeInherits(const QString &mime, "
        "const QString &parent)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mimeParents(*__, **_) -> Never:
    """
    Qt's 'QStringList QMimeDatabasePrivate::mimeParents(const QString
    &mimeName)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeParents' has no cute function yet. Qt's "
        "'QStringList QMimeDatabasePrivate::mimeParents(const QString "
        "&mimeName)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mimeTypeForData(*__, **_) -> Never:
    """
    Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForData(QIODevice
    *device)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeTypeForData' has no cute function yet. "
        "Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForData(QIODevice "
        "*device)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mimeTypeForFile(*__, **_) -> Never:
    """
    Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForFile(const QString
    &fileName, const QFileInfo &fileInfo, QMimeDatabase::MatchMode mode)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'directoryMimeType'.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeTypeForFile' has no cute function yet. "
        "Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForFile(const "
        "QString &fileName, const QFileInfo &fileInfo, "
        "QMimeDatabase::MatchMode mode)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'directoryMimeType'.")

  @staticmethod
  def mimeTypeForFileExtension(*__, **_) -> Never:
    """
    Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForFileExtension(const
    QString &fileName)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeTypeForFileExtension' has no cute "
        "function yet. Qt's 'QMimeType "
        "QMimeDatabasePrivate::mimeTypeForFileExtension(const QString "
        "&fileName)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mimeTypeForFileName(*__, **_) -> Never:
    """
    Qt's 'QStringList QMimeDatabasePrivate::mimeTypeForFileName(const QString
    &fileName)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'directoryMimeType'.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeTypeForFileName' has no cute function "
        "yet. Qt's 'QStringList "
        "QMimeDatabasePrivate::mimeTypeForFileName(const QString "
        "&fileName)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'directoryMimeType'.")

  @staticmethod
  def mimeTypeForFileNameAndData(*__, **_) -> Never:
    """
    Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForFileNameAndData(const
    QString &fileName, QIODevice *device)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeTypeForFileNameAndData' has no cute "
        "function yet. Qt's 'QMimeType "
        "QMimeDatabasePrivate::mimeTypeForFileNameAndData(const QString "
        "&fileName, QIODevice *device)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def mimeTypeForName(*__, **_) -> Never:
    """
    Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForName(const QString
    &nameOrAlias)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.mimeTypeForName' has no cute function yet. "
        "Qt's 'QMimeType QMimeDatabasePrivate::mimeTypeForName(const "
        "QString &nameOrAlias)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def parents(*__, **_) -> Never:
    """
    Qt's 'QStringList QMimeDatabasePrivate::parents(const QString
    &mimeName)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'plainTextMimeType'.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.parents' has no cute function yet. Qt's "
        "'QStringList QMimeDatabasePrivate::parents(const QString "
        "&mimeName)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'plainTextMimeType'.")

  @staticmethod
  def providers(*__, **_) -> Never:
    """
    Qt's 'const Providers &QMimeDatabasePrivate::providers()': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.providers' has no cute function yet. Qt's "
        "'const Providers &QMimeDatabasePrivate::providers()': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def resolveAlias(*__, **_) -> Never:
    """
    Qt's 'QString QMimeDatabasePrivate::resolveAlias(const QString
    &nameOrAlias)': leans on
    'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*,
    QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeDatabasePrivate.resolveAlias' has no cute function yet. Qt's "
        "'QString QMimeDatabasePrivate::resolveAlias(const QString "
        "&nameOrAlias)': leans on "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate*, "
        "QMimeXMLProvider::InternalDatabaseEnum)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
