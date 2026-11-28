"""
QMimeXMLProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimeprovider_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeXMLProvider to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QMimeProviderBase, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QMimeGlobPattern, QMimeMagicRuleMatcher, QMimeTypeXMLData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeGlobPattern = WAIT['QMimeGlobPattern']
  QMimeMagicRuleMatcher = WAIT['QMimeMagicRuleMatcher']
  QMimeTypeXMLData = WAIT['QMimeTypeXMLData']


class QMimeXMLProvider(QMimeProviderBase):
  """
  The cute side of Qt's QMimeXMLProvider: a plain Python object standing in
  front of one C++ QMimeXMLProvider.

  It is built on the cute 'QMimeProviderBase', as Qt's QMimeXMLProvider is
  built on Qt's QMimeProviderBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMimeXMLProvider that has a ritual and that Python
  can call so far, 13 names in all: 'isValid', 'isInternalDatabase',
  'knowsMimeType', 'resolveAlias', 'hasGlobDeleteAll', 'globPatterns',
  'icon', 'genericIcon', 'addMimeType', 'addGlobPattern', 'addParent',
  'addAlias', 'addMagicMatcher'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMimeXMLProvider::~QMimeXMLProvider()': the destructor: Python
    never removes a C++ QMimeXMLProvider.
  - Qt's 'void QMimeXMLProvider::addFileNameMatches(const QString &fileName,
    QMimeGlobMatchResult &result)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QMimeXMLProvider::addParents(const QString &mime, QStringList
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMimeXMLProvider::addAliases(const QString &name, QStringList
    &result)': takes a type Python has no way to hand over yet.
  - Qt's 'void QMimeXMLProvider::findByMagic(const QByteArray &data,
    QMimeMagicResult &result)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QMimeXMLProvider::addAllMimeTypes(QList<QMimeType> &result)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMimeTypePrivate::LocaleHash QMimeXMLProvider::localeComments(const
    QString &name)': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 26 functions Qt declares: 4 leans on 'QMimeTypeParserBase; 1
  cannot be called and cannot be called through the meta-object and cannot be
  copied; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QMimeXMLProvider is created at the first use, not by
    'QMimeXMLProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMimeXMLProvider.
  - Each name of Qt's QMimeXMLProvider that has no cute function yet,
    '__init__', 'load', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QMimeXMLProvider, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class InternalDatabaseEnum(CuteNum):
    """
    The enum 'QMimeXMLProvider::InternalDatabaseEnum' of Qt, with the 1 names
    Qt gives in it.
    """

    InternalDatabase = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeXMLProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isInternalDatabase(self) -> bool:
    """
    Calls Qt's 'bool QMimeXMLProvider::isInternalDatabase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimexmlprovider.html#isInternalDatabase
    """
    #  bool QMimeXMLProvider::isInternalDatabase() const
    return self.uglySide.call(
        'ritual_ZNK16QMimeXMLProvider18isInternalDatabaseEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate *db,
      InternalDatabaseEnum a1)': cannot be called and cannot be called
      through the meta-object and cannot be copied: no header file has its
      code, Qt's source does not mark it or its class for use from outside Qt
      or writes it 'inline' or nowhere, and it is no signal, slot or
      invokable function giving back nothing, of a class built on QObject,
      and Qt's source has no code for it that could be told from the rest.
    - Qt's 'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate *db,
      const QString &directory)': leans on
      'QMimeTypeParserBase::parse(QIODevice*, QString const&, QString*)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeXMLProvider.__init__' has no cute function yet. Qt's "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate *db, "
        "InternalDatabaseEnum a1)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest. Qt's "
        "'QMimeXMLProvider::QMimeXMLProvider(QMimeDatabasePrivate *db, "
        "const QString &directory)': leans on "
        "'QMimeTypeParserBase::parse(QIODevice*, QString const&, "
        "QString*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")

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

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMimeXMLProvider::isValid()'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#isValid
    """
    #  bool QMimeXMLProvider::isValid()
    return self.uglySide.call('ritual_ZN16QMimeXMLProvider7isValidEv')

  @overload(str)
  def knowsMimeType(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeXMLProvider::knowsMimeType(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimexmlprovider.html#knowsMimeType

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeXMLProvider::knowsMimeType(const QString &name)
    return self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider13knowsMimeTypeERK7QString', name,
    )

  @overload(str)
  def resolveAlias(self, name: str) -> str:
    """
    Calls Qt's 'QString QMimeXMLProvider::resolveAlias(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#resolveAlias

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeXMLProvider::resolveAlias(const QString &name)
    return self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider12resolveAliasERK7QString', name,
    )

  @overload(str)
  def hasGlobDeleteAll(self, name: str) -> bool:
    """
    Calls Qt's 'bool QMimeXMLProvider::hasGlobDeleteAll(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimexmlprovider.html#hasGlobDeleteAll

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QMimeXMLProvider::hasGlobDeleteAll(const QString &name)
    return self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider16hasGlobDeleteAllERK7QString', name,
    )

  @overload(str)
  def globPatterns(self, name: str) -> QStringList:
    """
    Calls Qt's 'QStringList QMimeXMLProvider::globPatterns(const QString
    &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#globPatterns

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QMimeXMLProvider::globPatterns(const QString &name)
    address = self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider12globPatternsERK7QString', name,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def icon(self, name: str) -> str:
    """
    Calls Qt's 'QString QMimeXMLProvider::icon(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#icon

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeXMLProvider::icon(const QString &name)
    return self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider4iconERK7QString', name,
    )

  @overload(str)
  def genericIcon(self, name: str) -> str:
    """
    Calls Qt's 'QString QMimeXMLProvider::genericIcon(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#genericIcon

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMimeXMLProvider::genericIcon(const QString &name)
    return self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider11genericIconERK7QString', name,
    )

  @overload(QMimeTypeXMLData)
  def addMimeType(self, mt: QMimeTypeXMLData) -> None:
    """
    Calls Qt's 'void QMimeXMLProvider::addMimeType(const QMimeTypeXMLData
    &mt)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#addMimeType

    Parameters
    ----------

    mt : QMimeTypeXMLData
      Passed on as a value: Qt reads the C++ QMimeTypeXMLData, which stays
      Python's own.
    """
    #  void QMimeXMLProvider::addMimeType(const QMimeTypeXMLData &mt)
    self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider11addMimeTypeERK16QMimeTypeXMLData',
        self._valueOf(mt),
    )

  @overload(QMimeGlobPattern)
  def addGlobPattern(self, glob: QMimeGlobPattern) -> None:
    """
    Calls Qt's 'void QMimeXMLProvider::addGlobPattern(const QMimeGlobPattern
    &glob)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimexmlprovider.html#addGlobPattern

    Parameters
    ----------

    glob : QMimeGlobPattern
      Passed on as a value: Qt reads the C++ QMimeGlobPattern, which stays
      Python's own.
    """
    #  void QMimeXMLProvider::addGlobPattern(const QMimeGlobPattern &glob)
    self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider14addGlobPatternERK16QMimeGlobPattern',
        self._valueOf(glob),
    )

  @overload(str, str)
  def addParent(self, child: str, parent: str) -> None:
    """
    Calls Qt's 'void QMimeXMLProvider::addParent(const QString &child, const
    QString &parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#addParent

    Parameters
    ----------

    child : str
      Passed on as it is: a QString is made of it for the call.

    parent : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeXMLProvider::addParent(const QString &child, const QString
    #      &parent)
    self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider9addParentERK7QStringS2_', child, parent,
    )

  @overload(str, str)
  def addAlias(self, alias: str, name: str) -> None:
    """
    Calls Qt's 'void QMimeXMLProvider::addAlias(const QString &alias, const
    QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimexmlprovider.html#addAlias

    Parameters
    ----------

    alias : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeXMLProvider::addAlias(const QString &alias, const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider8addAliasERK7QStringS2_', alias, name,
    )

  @overload(QMimeMagicRuleMatcher)
  def addMagicMatcher(self, matcher: QMimeMagicRuleMatcher) -> None:
    """
    Calls Qt's 'void QMimeXMLProvider::addMagicMatcher(const
    QMimeMagicRuleMatcher &matcher)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimexmlprovider.html#addMagicMatcher

    Parameters
    ----------

    matcher : QMimeMagicRuleMatcher
      Passed on as a value: Qt reads the C++ QMimeMagicRuleMatcher, which
      stays Python's own.
    """
    #  void QMimeXMLProvider::addMagicMatcher(const QMimeMagicRuleMatcher
    #      &matcher)
    self.uglySide.call(
        'ritual_ZN16QMimeXMLProvider15addMagicMatcherERK21QMimeMagicRuleMat'
        'cher',
        self._valueOf(matcher),
    )

  @staticmethod
  def load(*__, **_) -> Never:
    """
    - Qt's 'void QMimeXMLProvider::load(const char *data, qsizetype len)':
      Qt's library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'internalMimeFileName'.
    - Qt's 'bool QMimeXMLProvider::load(const QString &fileName, QString
      *errorMessage)': leans on 'QMimeTypeParserBase::parse(QIODevice*,
      QString const&, QString*)', which Qt's source does not mark for use
      from outside Qt and has no code for that could be taken.
    - Qt's 'void QMimeXMLProvider::load(const QString &fileName)': leans on
      'QMimeTypeParserBase::parse(QIODevice*, QString const&, QString*)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QMimeXMLProvider.load' has no cute function yet. Qt's 'void "
        "QMimeXMLProvider::load(const char *data, qsizetype len)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'internalMimeFileName'. Qt's 'bool QMimeXMLProvider::load(const "
        "QString &fileName, QString *errorMessage)': leans on "
        "'QMimeTypeParserBase::parse(QIODevice*, QString const&, "
        "QString*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken. Qt's 'void "
        "QMimeXMLProvider::load(const QString &fileName)': leans on "
        "'QMimeTypeParserBase::parse(QIODevice*, QString const&, "
        "QString*)', which Qt's source does not mark for use from outside "
        "Qt and has no code for that could be taken.")
