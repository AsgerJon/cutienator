"""
QQmlImports binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlimport_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlImports to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision, QUrl
  from . import QHashedStringRef, QQmlError, QQmlImportInstance
  from . import QQmlImportNamespace, QQmlTypeLoader
  from . import QQmlTypeLoaderQmldirContent, QQmlTypeNameCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedStringRef = WAIT['QHashedStringRef']
  QQmlImportInstance = WAIT['QQmlImportInstance']
  QQmlImportNamespace = WAIT['QQmlImportNamespace']
  QQmlTypeLoader = WAIT['QQmlTypeLoader']
  QQmlTypeLoaderQmldirContent = WAIT['QQmlTypeLoaderQmldirContent']
  QQmlTypeNameCache = WAIT['QQmlTypeNameCache']
  QTypeRevision = WAIT['QTypeRevision']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlImports(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlImports: a plain Python object standing in front
  of one C++ QQmlImports.

  What exists
  -----------

  Every function of Qt's QQmlImports that has a ritual and that Python can
  call so far, 17 names in all: 'tr', 'setBaseUrl', 'baseUrl',
  'populateCache', 'completeQmldirPaths', 'versionString', 'isLocal',
  'urlFromLocalFileOrQrcOrUrl', 'setDesignerSupportRequired', 'validVersion',
  'moduleNotFoundError', 'redirectQmldirContent', 'insertImport',
  'importNamespace', 'findQualifiedNamespace', 'registerBuiltinModuleTypes',
  'resolvedUri'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlImports::~QQmlImports()': the destructor: Python never removes
    a C++ QQmlImports.
  - Qt's 'bool QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const
    QHashedStringRef &type, QQmlType *type_return, QTypeRevision
    *version_return, QQmlImportNamespace **ns_return, QList<QQmlError>
    *errors, QQmlType::RegistrationType registrationType, bool
    *typeRecursionDetected) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'bool QQmlImports::addInlineComponentImport(QQmlImportInstance
    *const importInstance, const QString &name, const QUrl &importUrl)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QTypeRevision QQmlImports::addFileImport(QQmlTypeLoader
    *typeLoader, const QString &uri, const QString &prefix, QTypeRevision
    requestedVersion, ImportFlags flags, quint8 precedence, QString
    *localQmldir, QList<QQmlError> *errors)': names 'QList<QQmlError>', which
    has no cute class yet.
  - Qt's 'QTypeRevision QQmlImports::addLibraryImport(QQmlTypeLoader
    *typeLoader, const QString &uri, const QString &prefix, QTypeRevision
    requestedVersion, const QString &qmldirIdentifier, const QString
    &qmldirUrl, ImportFlags flags, quint8 precedence, QList<QQmlError>
    *errors)': names 'QList<QQmlError>', which has no cute class yet.
  - Qt's 'QTypeRevision QQmlImports::updateQmldirContent(QQmlTypeLoader
    *typeLoader, const QString &uri, QTypeRevision version, const QString
    &prefix, const QString &qmldirIdentifier, const QString &qmldirUrl,
    QList<QQmlError> *errors)': names 'QList<QQmlError>', which has no cute
    class yet.
  - Qt's 'QList<ScriptReference> QQmlImports::resolvedScripts() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<CompositeSingletonReference>
    QQmlImports::resolvedCompositeSingletons() const': gives a type Python
    has no way to take yet.
  - Qt's 'bool QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const
    QHashedStringRef &type, QTypeRevision *version_return, QQmlType
    *type_return, QList<QQmlError> *errors, QQmlType::RegistrationType
    registrationType, bool *typeRecursionDetected) const': names
    'QList<QQmlError>', which has no cute class yet.
  - Qt's 'QTypeRevision QQmlImports::importExtension(QQmlTypeLoader
    *typeLoader, const QString &uri, QTypeRevision version, const
    QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
  - Qt's 'bool QQmlImports::getQmldirContent(QQmlTypeLoader *typeLoader,
    const QString &qmldirIdentifier, const QString &uri,
    QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.

  What has no ritual
  ------------------

  8 of the 38 functions Qt declares: 4 forbidden; 3 a template; 1 leans on
  'lcQmlImport()', which Qt's source does not mark for use from outside Qt
  and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQmlImports is created at the first use, not by
    'QQmlImports(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlImports.
  - Each name of Qt's QQmlImports that has no cute function yet,
    'addFileImport', 'addImplicitImport', 'addImportToNamespace',
    'addInlineComponentImport', 'addLibraryImport', 'finalizeImport',
    'getQmldirContent', 'importExtension', 'resolveType',
    'resolvedCompositeSingletons', 'resolvedScripts', 'updateQmldirContent',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQmlImports, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ImportFlag(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QQmlImports::ImportFlag' of Qt, with the 2 names Qt gives
    in it. Qt names the type of its combinations 'QQmlImports::ImportFlags'.
    """

    ImportNoFlag = 0x0
    ImportIncomplete = 0x1

  ImportFlags = ImportFlag

  class ImportVersion(CuteNum):
    """
    The enum 'QQmlImports::ImportVersion' of Qt, with the 3 names Qt gives in
    it.
    """

    FullyVersioned = Kee[int](0)
    PartiallyVersioned = Kee[int](1)
    Unversioned = Kee[int](2)

  #  The classes Qt writes inside QQmlImports, each a class in here as in
  #  C++.

  class CompositeSingletonReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlImports::CompositeSingletonReference: a plain
    Python object standing in front of one C++
    QQmlImports::CompositeSingletonReference.

    C++ hands a QQmlImports::CompositeSingletonReference around as a copy, so
    every C++ QQmlImports::CompositeSingletonReference behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlImports::CompositeSingletonReference yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlImports::CompositeSingletonReference::
      ~CompositeSingletonReference()': the destructor: Python removes its C++
      QQmlImports::CompositeSingletonReference by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlImports::CompositeSingletonReference is created at the
      first use, not by 'QQmlImports::CompositeSingletonReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlImports::CompositeSingletonReference back gives
      a copy the ritual made for Python, in a new cute
      QQmlImports::CompositeSingletonReference.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlImports::CompositeSingletonReference'

    #  Qt's '~QQmlImports::CompositeSingletonReference()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlImports::CompositeSingletonReference behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN11QQmlImports27CompositeSingletonReferenceD1Ev')

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

  class ScriptReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlImports::ScriptReference: a plain Python object
    standing in front of one C++ QQmlImports::ScriptReference.

    C++ hands a QQmlImports::ScriptReference around as a copy, so every C++
    QQmlImports::ScriptReference behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlImports::ScriptReference yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlImports::ScriptReference::~ScriptReference()': the
      destructor: Python removes its C++ QQmlImports::ScriptReference by it,
      and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlImports::ScriptReference is created at the first use, not
      by 'QQmlImports::ScriptReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlImports::ScriptReference back gives a copy the
      ritual made for Python, in a new cute QQmlImports::ScriptReference.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlImports::ScriptReference'

    #  Qt's '~QQmlImports::ScriptReference()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlImports::ScriptReference behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN11QQmlImports15ScriptReferenceD1Ev'

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
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(
      sourceText: Optional[str],
      disambiguation: Optional[str] = None,
      n: int = -1,
  ) -> str:
    """
    Calls Qt's 'QString QQmlImports::tr(const char *sourceText, const char
    *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#tr

    Parameters
    ----------

    sourceText : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    disambiguation : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlImports::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN11QQmlImports2trEPKcS1_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  @overload(str, QStringList, QTypeRevision)
  def completeQmldirPaths(
      uri: str,
      basePaths: QStringList,
      version: QTypeRevision,
  ) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlImports::completeQmldirPaths(const QString
    &uri, const QStringList &basePaths, QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#completeQmldirPaths

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    basePaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlImports::completeQmldirPaths(const QString &uri, const
    #      QStringList &basePaths, QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN11QQmlImports19completeQmldirPathsERK7QStringRK5QListIS0_'
        'E13QTypeRevision',
        uri, CuteMixin._valueOf(basePaths), CuteMixin._valueOf(version),
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QTypeRevision, ImportVersion)
  def versionString(
      version: QTypeRevision,
      importVersion: ImportVersion,
  ) -> str:
    """
    Calls Qt's 'QString QQmlImports::versionString(QTypeRevision version,
    ImportVersion importVersion)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#versionString

    Parameters
    ----------

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    importVersion : ImportVersion
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlImports::versionString(QTypeRevision version,
    #      ImportVersion importVersion)
    return Rituals.call(
        'ritual_ZN11QQmlImports13versionStringE13QTypeRevisionNS_13ImportVe'
        'rsionE',
        CuteMixin._valueOf(version), importVersion.value,
    )

  @staticmethod
  @overload(str)
  def isLocal(url: str) -> bool:
    """
    Calls Qt's 'bool QQmlImports::isLocal(const QString &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#isLocal

    Parameters
    ----------

    url : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlImports::isLocal(const QString &url)
    return Rituals.call('ritual_ZN11QQmlImports7isLocalERK7QString', url)

  @staticmethod
  @overload(QUrl)
  def isLocal(url: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlImports::isLocal(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#isLocal

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlImports::isLocal(const QUrl &url)
    return Rituals.call(
        'ritual_ZN11QQmlImports7isLocalERK4QUrl', CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(str)
  def urlFromLocalFileOrQrcOrUrl(a0: str) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlImports::urlFromLocalFileOrQrcOrUrl(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#urlFromLocalFileOrQrcOrUrl

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlImports::urlFromLocalFileOrQrcOrUrl(const QString &a0)
    address = Rituals.call(
        'ritual_ZN11QQmlImports26urlFromLocalFileOrQrcOrUrlERK7QString', a0,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(bool)
  def setDesignerSupportRequired(b: bool) -> None:
    """
    Calls Qt's 'void QQmlImports::setDesignerSupportRequired(bool b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#setDesignerSupportRequired

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QQmlImports::setDesignerSupportRequired(bool b)
    Rituals.call('ritual_ZN11QQmlImports26setDesignerSupportRequiredEb', b)

  @staticmethod
  @overload()
  @overload(QTypeRevision)
  def validVersion(version: Optional[QTypeRevision] = None) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlImports::validVersion(QTypeRevision
    version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#validVersion

    Parameters
    ----------

    version : Optional[QTypeRevision]
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own. May be left out, as in Qt: a new 'QTypeRevision()' is
      then passed on.

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlImports::validVersion(QTypeRevision version)
    if version is None:
      from ..QtCore import QTypeRevision
      version = QTypeRevision()
    address = Rituals.call(
        'ritual_ZN11QQmlImports12validVersionE13QTypeRevision',
        CuteMixin._valueOf(version),
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  @staticmethod
  @overload(str, QTypeRevision)
  def moduleNotFoundError(uri: str, version: QTypeRevision) -> QQmlError:
    """
    Calls Qt's 'QQmlError QQmlImports::moduleNotFoundError(const QString
    &uri, QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#moduleNotFoundError

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlError
      A new cute QQmlError around the copy Qt gave back. Python owns it.
    """
    #  QQmlError QQmlImports::moduleNotFoundError(const QString &uri,
    #      QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN11QQmlImports19moduleNotFoundErrorERK7QString13QTypeRevis'
        'ion',
        uri, CuteMixin._valueOf(version),
    )
    from . import QQmlError
    return QQmlError._cuteOwning(address)

  @staticmethod
  @overload(QQmlTypeLoader, QQmlTypeLoaderQmldirContent)
  @overload(QQmlTypeLoader, NoneType)
  @overload(NoneType, QQmlTypeLoaderQmldirContent)
  @overload(NoneType, NoneType)
  def redirectQmldirContent(
      typeLoader: Optional[QQmlTypeLoader],
      qmldir: Optional[QQmlTypeLoaderQmldirContent],
  ) -> str:
    """
    Calls Qt's 'QString QQmlImports::redirectQmldirContent(QQmlTypeLoader
    *typeLoader, QQmlTypeLoaderQmldirContent *qmldir)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#redirectQmldirContent

    Parameters
    ----------

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    qmldir : Optional[QQmlTypeLoaderQmldirContent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlImports::redirectQmldirContent(QQmlTypeLoader *typeLoader,
    #      QQmlTypeLoaderQmldirContent *qmldir)
    return Rituals.call(
        'ritual_ZN11QQmlImports21redirectQmldirContentEP14QQmlTypeLoaderP27'
        'QQmlTypeLoaderQmldirContent',
        CuteMixin._addressOf(typeLoader), CuteMixin._addressOf(qmldir),
    )

  @staticmethod
  @overload(QQmlImportNamespace, QQmlImportInstance)
  @overload(QQmlImportNamespace, NoneType)
  @overload(NoneType, QQmlImportInstance)
  @overload(NoneType, NoneType)
  def insertImport(
      nameSpace: Optional[QQmlImportNamespace],
      import_: Optional[QQmlImportInstance],
  ) -> None:
    """
    Calls Qt's 'void QQmlImports::insertImport(QQmlImportNamespace
    *nameSpace, QQmlImportInstance *import)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#insertImport

    Parameters
    ----------

    nameSpace : Optional[QQmlImportNamespace]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    import_ : Optional[QQmlImportInstance]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlImports::insertImport(QQmlImportNamespace *nameSpace,
    #      QQmlImportInstance *import)
    Rituals.call(
        'ritual_ZN11QQmlImports12insertImportEP19QQmlImportNamespaceP18QQml'
        'ImportInstance',
        CuteMixin._addressOf(nameSpace), CuteMixin._addressOf(import_),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlImports'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlImports::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlImports::baseUrl() const
    address = self.uglySide.call('ritual_ZNK11QQmlImports7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(QHashedStringRef)
  def findQualifiedNamespace(
      self,
      a0: QHashedStringRef,
  ) -> Optional[QQmlImportNamespace]:
    """
    Calls Qt's 'QQmlImportNamespace
    *QQmlImports::findQualifiedNamespace(const QHashedStringRef &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#findQualifiedNamespace

    Parameters
    ----------

    a0 : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlImportNamespace]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlImportNamespace *QQmlImports::findQualifiedNamespace(const
    #      QHashedStringRef &a0) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlImports22findQualifiedNamespaceERK16QHashedStringR'
        'ef',
        self._valueOf(a0),
    )
    from . import QQmlImportNamespace
    return QQmlImportNamespace._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  @overload(QUrl, str)
  def setBaseUrl(self, url: QUrl, urlString: str = '') -> None:
    """
    Calls Qt's 'void QQmlImports::setBaseUrl(const QUrl &url, const QString
    &urlString)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#setBaseUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    urlString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QQmlImports::setBaseUrl(const QUrl &url, const QString
    #      &urlString)
    self.uglySide.call(
        'ritual_ZN11QQmlImports10setBaseUrlERK4QUrlRK7QString',
        self._valueOf(url), urlString,
    )

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
    Notes what was given, for Qt's 'QQmlImports::QQmlImports()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#QQmlImports
    """
    #  QQmlImports::QQmlImports()
    self._noteCreation(QQmlImports, lambda: Rituals.call(
        'ritual_ZN11QQmlImportsC1Ev',
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

  @overload(QQmlTypeNameCache)
  @overload(NoneType)
  def populateCache(self, cache: Optional[QQmlTypeNameCache]) -> None:
    """
    Calls Qt's 'void QQmlImports::populateCache(QQmlTypeNameCache *cache)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#populateCache

    Parameters
    ----------

    cache : Optional[QQmlTypeNameCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlImports::populateCache(QQmlTypeNameCache *cache) const
    self.uglySide.call(
        'ritual_ZNK11QQmlImports13populateCacheEP17QQmlTypeNameCache',
        self._addressOf(cache),
    )

  @overload(str)
  def importNamespace(self, prefix: str) -> Optional[QQmlImportNamespace]:
    """
    Calls Qt's 'QQmlImportNamespace *QQmlImports::importNamespace(const
    QString &prefix)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#importNamespace

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QQmlImportNamespace]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlImportNamespace *QQmlImports::importNamespace(const QString
    #      &prefix)
    address = self.uglySide.call(
        'ritual_ZN11QQmlImports15importNamespaceERK7QString', prefix,
    )
    from . import QQmlImportNamespace
    return QQmlImportNamespace._cuteAt(address)

  @overload(QQmlTypeLoaderQmldirContent, QTypeRevision)
  def registerBuiltinModuleTypes(
      self,
      qmldir: QQmlTypeLoaderQmldirContent,
      version: QTypeRevision,
  ) -> None:
    """
    Calls Qt's 'void QQmlImports::registerBuiltinModuleTypes(const
    QQmlTypeLoaderQmldirContent &qmldir, QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlimports.html#registerBuiltinModuleTypes

    Parameters
    ----------

    qmldir : QQmlTypeLoaderQmldirContent
      Passed on as a value: Qt reads the C++ QQmlTypeLoaderQmldirContent,
      which stays Python's own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlImports::registerBuiltinModuleTypes(const
    #      QQmlTypeLoaderQmldirContent &qmldir, QTypeRevision version)
    self.uglySide.call(
        'ritual_ZN11QQmlImports26registerBuiltinModuleTypesERK27QQmlTypeLoa'
        'derQmldirContent13QTypeRevision',
        self._valueOf(qmldir), self._valueOf(version),
    )

  @overload(str, QQmlTypeLoader)
  @overload(str, NoneType)
  def resolvedUri(
      self,
      dir_arg: str,
      typeLoader: Optional[QQmlTypeLoader],
  ) -> str:
    """
    Calls Qt's 'QString QQmlImports::resolvedUri(const QString &dir_arg,
    QQmlTypeLoader *typeLoader)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlimports.html#resolvedUri

    Parameters
    ----------

    dir_arg : str
      Passed on as it is: a QString is made of it for the call.

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlImports::resolvedUri(const QString &dir_arg,
    #      QQmlTypeLoader *typeLoader)
    return self.uglySide.call(
        'ritual_ZN11QQmlImports11resolvedUriERK7QStringP14QQmlTypeLoader',
        dir_arg, self._addressOf(typeLoader),
    )

  @staticmethod
  def addFileImport(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlImports::addFileImport(QQmlTypeLoader
    *typeLoader, const QString &uri, const QString &prefix, QTypeRevision
    requestedVersion, ImportFlags flags, quint8 precedence, QString
    *localQmldir, QList<QQmlError> *errors)': names 'QList<QQmlError>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlImports.addFileImport' has no cute function yet. Qt's "
        "'QTypeRevision QQmlImports::addFileImport(QQmlTypeLoader "
        "*typeLoader, const QString &uri, const QString &prefix, "
        "QTypeRevision requestedVersion, ImportFlags flags, quint8 "
        "precedence, QString *localQmldir, QList<QQmlError> *errors)': "
        "names 'QList<QQmlError>', which has no cute class yet.")

  @staticmethod
  def addImplicitImport(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlImports::addImplicitImport(QQmlTypeLoader
    *typeLoader, QString *localQmldir, QList<QQmlError> *errors)': leans on
    'lcQmlImport()', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlImports.addImplicitImport' has no cute function yet. Qt's "
        "'QTypeRevision QQmlImports::addImplicitImport(QQmlTypeLoader "
        "*typeLoader, QString *localQmldir, QList<QQmlError> *errors)': "
        "leans on 'lcQmlImport()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def addImportToNamespace(*__, **_) -> Never:
    """
    Qt's 'QQmlImports::addImportToNamespace': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlImports.addImportToNamespace' has no cute function yet. Qt's "
        "'QQmlImports::addImportToNamespace': a template: a pattern and no "
        "single function.")

  @staticmethod
  def addInlineComponentImport(*__, **_) -> Never:
    """
    Qt's 'bool QQmlImports::addInlineComponentImport(QQmlImportInstance
    *const importInstance, const QString &name, const QUrl &importUrl)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlImports.addInlineComponentImport' has no cute function yet. "
        "Qt's 'bool "
        "QQmlImports::addInlineComponentImport(QQmlImportInstance *const "
        "importInstance, const QString &name, const QUrl &importUrl)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def addLibraryImport(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlImports::addLibraryImport(QQmlTypeLoader
    *typeLoader, const QString &uri, const QString &prefix, QTypeRevision
    requestedVersion, const QString &qmldirIdentifier, const QString
    &qmldirUrl, ImportFlags flags, quint8 precedence, QList<QQmlError>
    *errors)': names 'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlImports.addLibraryImport' has no cute function yet. Qt's "
        "'QTypeRevision QQmlImports::addLibraryImport(QQmlTypeLoader "
        "*typeLoader, const QString &uri, const QString &prefix, "
        "QTypeRevision requestedVersion, const QString &qmldirIdentifier, "
        "const QString &qmldirUrl, ImportFlags flags, quint8 precedence, "
        "QList<QQmlError> *errors)': names 'QList<QQmlError>', which has no "
        "cute class yet.")

  @staticmethod
  def finalizeImport(*__, **_) -> Never:
    """
    Qt's 'QQmlImports::finalizeImport': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlImports.finalizeImport' has no cute function yet. Qt's "
        "'QQmlImports::finalizeImport': a template: a pattern and no single "
        "function.")

  @staticmethod
  def getQmldirContent(*__, **_) -> Never:
    """
    Qt's 'bool QQmlImports::getQmldirContent(QQmlTypeLoader *typeLoader,
    const QString &qmldirIdentifier, const QString &uri,
    QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlImports.getQmldirContent' has no cute function yet. Qt's "
        "'bool QQmlImports::getQmldirContent(QQmlTypeLoader *typeLoader, "
        "const QString &qmldirIdentifier, const QString &uri, "
        "QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)': "
        "names 'QList<QQmlError>', which has no cute class yet.")

  @staticmethod
  def importExtension(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlImports::importExtension(QQmlTypeLoader
    *typeLoader, const QString &uri, QTypeRevision version, const
    QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlImports.importExtension' has no cute function yet. Qt's "
        "'QTypeRevision QQmlImports::importExtension(QQmlTypeLoader "
        "*typeLoader, const QString &uri, QTypeRevision version, const "
        "QQmlTypeLoaderQmldirContent *qmldir, QList<QQmlError> *errors)': "
        "names 'QList<QQmlError>', which has no cute class yet.")

  @staticmethod
  def resolveType(*__, **_) -> Never:
    """
    - Qt's 'bool QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const
      QHashedStringRef &type, QQmlType *type_return, QTypeRevision
      *version_return, QQmlImportNamespace **ns_return, QList<QQmlError>
      *errors, QQmlType::RegistrationType registrationType, bool
      *typeRecursionDetected) const': takes a type Python has no way to hand
      over yet.
    - Qt's 'bool QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const
      QHashedStringRef &type, QTypeRevision *version_return, QQmlType
      *type_return, QList<QQmlError> *errors, QQmlType::RegistrationType
      registrationType, bool *typeRecursionDetected) const': names
      'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlImports.resolveType' has no cute function yet. Qt's 'bool "
        "QQmlImports::resolveType(QQmlTypeLoader *typeLoader, const "
        "QHashedStringRef &type, QQmlType *type_return, QTypeRevision "
        "*version_return, QQmlImportNamespace **ns_return, QList<QQmlError> "
        "*errors, QQmlType::RegistrationType registrationType, bool "
        "*typeRecursionDetected) const': takes a type Python has no way to "
        "hand over yet. Qt's 'bool QQmlImports::resolveType(QQmlTypeLoader "
        "*typeLoader, const QHashedStringRef &type, QTypeRevision "
        "*version_return, QQmlType *type_return, QList<QQmlError> *errors, "
        "QQmlType::RegistrationType registrationType, bool "
        "*typeRecursionDetected) const': names 'QList<QQmlError>', which "
        "has no cute class yet.")

  @staticmethod
  def resolvedCompositeSingletons(*__, **_) -> Never:
    """
    Qt's 'QList<CompositeSingletonReference>
    QQmlImports::resolvedCompositeSingletons() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlImports.resolvedCompositeSingletons' has no cute function "
        "yet. Qt's 'QList<CompositeSingletonReference> "
        "QQmlImports::resolvedCompositeSingletons() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def resolvedScripts(*__, **_) -> Never:
    """
    Qt's 'QList<ScriptReference> QQmlImports::resolvedScripts() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlImports.resolvedScripts' has no cute function yet. Qt's "
        "'QList<ScriptReference> QQmlImports::resolvedScripts() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def updateQmldirContent(*__, **_) -> Never:
    """
    Qt's 'QTypeRevision QQmlImports::updateQmldirContent(QQmlTypeLoader
    *typeLoader, const QString &uri, QTypeRevision version, const QString
    &prefix, const QString &qmldirIdentifier, const QString &qmldirUrl,
    QList<QQmlError> *errors)': names 'QList<QQmlError>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlImports.updateQmldirContent' has no cute function yet. Qt's "
        "'QTypeRevision QQmlImports::updateQmldirContent(QQmlTypeLoader "
        "*typeLoader, const QString &uri, QTypeRevision version, const "
        "QString &prefix, const QString &qmldirIdentifier, const QString "
        "&qmldirUrl, QList<QQmlError> *errors)': names 'QList<QQmlError>', "
        "which has no cute class yet.")
