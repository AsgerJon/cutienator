"""
QQmlJSImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSImporter to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision
  from . import QQmlJSResourceFileMapper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSResourceFileMapper = WAIT['QQmlJSResourceFileMapper']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSImporter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSImporter: a plain Python object standing in
  front of one C++ QQmlJSImporter.

  C++ hands a QQmlJSImporter around as a copy, so every C++ QQmlJSImporter
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJSImporter that has a ritual and that Python can
  call so far, 13 names in all: 'resourceFileMapper',
  'setResourceFileMapper', 'metaDataMapper', 'setMetaDataMapper',
  'importHardCodedBuiltins', 'importDirectory', 'builtinInternalNames',
  'importPaths', 'setImportPaths', 'clearCache', 'pathOfModule',
  'useOptionalImports', 'preferQmlFilesFromSourceFolder'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSImporter::QQmlJSImporter(const QStringList &importPaths,
    QQmlJSResourceFileMapper *mapper, QQmlJSImporterFlags flags)': names the
    enum 'QQmlJSImporterFlag', whose class cannot be named here.
  - Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImporter::importQmldirs(const QStringList &qmltypesFiles)': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlJSScope::Ptr QQmlJSImporter::importFile(const QString &file)':
    gives a type Python has no way to take yet.
  - Qt's 'QHash<QString, QQmlJSScope::Ptr> QQmlJSImporter::importedFiles()
    const': gives a type Python has no way to take yet.
  - Qt's 'ImportedTypes QQmlJSImporter::importModule(const QString &module,
    quint8 precedence, const QString &prefix, QTypeRevision version,
    QStringList *staticModuleList)': names 'QStringList', which has no cute
    class yet.
  - Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImporter::takeGlobalWarnings()': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlJSScope::ConstPtr QQmlJSImporter::jsGlobalObject()': gives a
    type Python has no way to take yet.
  - Qt's 'void QQmlJSImporter::runImportVisitor(QQmlJS::AST::Node *rootNode,
    const ImportVisitorPrerequisites &prerequisites)': names
    'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'void QQmlJSImporter::setImportVisitor(ImportVisitor visitor)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSImporter::setFlags(const QQmlJSImporterFlags &flags)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSImporterFlags QQmlJSImporter::flags() const': gives the enum
    'QQmlJSImporterFlag', whose class cannot be named here.
  - Qt's 'AvailableTypes QQmlJSImporter::builtinImportHelper()': gives a type
    Python has no way to take yet.
  - Qt's 'bool QQmlJSImporter::importHelper(const QString &module,
    AvailableTypes *types, quint8 precedence, const QString &prefix,
    QTypeRevision version, bool isDependency, bool isFile)': names
    'QQmlJSImporter::AvailableTypes', which has no cute class yet.
  - Qt's 'void QQmlJSImporter::processImport(const QQmlJS::Import
    &importDescription, const Import &import, quint8 precedence,
    AvailableTypes *types)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSImporter::insertAliases(const QQmlJS::ContextualType
    &type, QQmlJSImporter::AvailableTypes *types)': names
    'QQmlJSImporter::AvailableTypes', which has no cute class yet.
  - Qt's 'void QQmlJSImporter::insertExport(const QQmlJS::ContextualType
    &type, const QQmlJS::Export &valExport, const QString &qmlName,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types) const': names 'QHash<QString,
    QList<QQmlJSScope::Export>>', which has no cute class yet.
  - Qt's 'QQmlJSScope::Export QQmlJSImporter::resolveConflictingExports(const
    QQmlJS::Import &importDescription, const QQmlJSExportedScope &val, quint8
    precedence, QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QQmlJSImporter::insertExportWithConflictingVersion(const
    QQmlJSExportedScope &val, quint8 precedence, const QString &qmlName,
    const QQmlJSScope::Export &valExport, const QQmlJSScope::ConstPtr &scope,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types, SeenVersion seenVersion) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'SeenVersion QQmlJSImporter::computeSeenVersion(const QQmlJS::Import
    &importDescription, const QList<QQmlJS::Export> &existingExports,
    QTypeRevision valExportVersion) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlJSImporter::insertExports(const QQmlJS::Import
    &importDescription, const QQmlJSExportedScope &val, const QString
    &cppName, quint8 precedence, QHash<QString, QList<QQmlJSScope::Export>>
    *seenExports, QQmlJSImporter::AvailableTypes *types)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlJSImporter::importDependencies(const Import &import,
    quint8 precedence, AvailableTypes *types, const QString &prefix,
    QTypeRevision version, bool isDependency)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlDirParser QQmlJSImporter::createQmldirParserForFile(const
    QString &filename, Import *import)': names 'QQmlJSImporter::Import',
    which has no cute class yet.
  - Qt's 'void QQmlJSImporter::readQmltypes(const QString &filename, Import
    *result)': names 'QQmlJSImporter::Import', which has no cute class yet.
  - Qt's 'Import QQmlJSImporter::readQmldir(const QString &dirname)': gives a
    type Python has no way to take yet.
  - Qt's 'Import QQmlJSImporter::readDirectory(const QString &directory)':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlJSScope::Ptr QQmlJSImporter::localFile2QQmlJSScope(const
    QString &filePath)': gives a type Python has no way to take yet.
  - Qt's 'void QQmlJSImporter::setQualifiedNamesOn(const Import &import)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSImporter::~QQmlJSImporter()': the destructor: Python removes
    its C++ QQmlJSImporter by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSImporter is created at the first use, not by
    'QQmlJSImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSImporter back gives a copy the ritual made for
    Python, in a new cute QQmlJSImporter.
  - Each name of Qt's QQmlJSImporter that has no cute function yet,
    '__init__', 'builtinImportHelper', 'computeSeenVersion',
    'createQmldirParserForFile', 'flags', 'importDependencies', 'importFile',
    'importHelper', 'importModule', 'importQmldirs', 'importedFiles',
    'insertAliases', 'insertExport', 'insertExportWithConflictingVersion',
    'insertExports', 'jsGlobalObject', 'localFile2QQmlJSScope',
    'processImport', 'readDirectory', 'readQmldir', 'readQmltypes',
    'resolveConflictingExports', 'runImportVisitor', 'setFlags',
    'setImportVisitor', 'setQualifiedNamesOn', 'takeGlobalWarnings', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlJSImporter, each a class in here as in
  #  C++.

  class ImportVisitorPrerequisites(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSImporter::ImportVisitorPrerequisites: a plain
    Python object standing in front of one C++
    QQmlJSImporter::ImportVisitorPrerequisites.

    C++ hands a QQmlJSImporter::ImportVisitorPrerequisites around as a copy,
    so every C++ QQmlJSImporter::ImportVisitorPrerequisites behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSImporter::ImportVisitorPrerequisites yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSImporter::ImportVisitorPrerequisites::
      ImportVisitorPrerequisites(QQmlJSScope::Ptr target, QQmlJSLogger
      *logger, const QString &implicitImportDirectory, const QStringList
      &qmldirFiles)': takes a type Python has no way to hand over yet.
    - Qt's 'QQmlJSImporter::ImportVisitorPrerequisites::
      ~ImportVisitorPrerequisites()': the destructor: Python removes its C++
      QQmlJSImporter::ImportVisitorPrerequisites by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlJSImporter::ImportVisitorPrerequisites is created at the
      first use, not by 'QQmlJSImporter::ImportVisitorPrerequisites(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSImporter::ImportVisitorPrerequisites back
      gives a copy the ritual made for Python, in a new cute
      QQmlJSImporter::ImportVisitorPrerequisites.
    - Each name of Qt's QQmlJSImporter::ImportVisitorPrerequisites that has
      no cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSImporter::ImportVisitorPrerequisites'

    #  Qt's '~QQmlJSImporter::ImportVisitorPrerequisites()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QQmlJSImporter::ImportVisitorPrerequisites behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN14QQmlJSImporter26ImportVisitorPrerequisitesD1Ev')

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QQmlJSImporter::ImportVisitorPrerequisites::
      ImportVisitorPrerequisites(QQmlJSScope::Ptr target, QQmlJSLogger
      *logger, const QString &implicitImportDirectory, const QStringList
      &qmldirFiles)': takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportVisitorPrerequisites.__init__' has no cute "
          "function yet. Qt's "
          "'QQmlJSImporter::ImportVisitorPrerequisites::ImportVisitorPrerequ"
          "isites(QQmlJSScope::Ptr target, QQmlJSLogger *logger, const "
          "QString &implicitImportDirectory, const QStringList "
          "&qmldirFiles)': takes a type Python has no way to hand over yet.")

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

  class ImportedTypes(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSImporter::ImportedTypes: a plain Python
    object standing in front of one C++ QQmlJSImporter::ImportedTypes.

    C++ hands a QQmlJSImporter::ImportedTypes around as a copy, so every C++
    QQmlJSImporter::ImportedTypes behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlJSImporter::ImportedTypes that has a ritual
    and that Python can call so far, 7 names in all: 'clear',
    'contextualTypes', 'setCurrentFileSelector', 'isEmpty', 'hasType',
    'setType', 'isNullType'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QQmlJSImporter::ImportedTypes::ImportedTypes(QQmlJS::ContextualTypes
      &&types, QList<QQmlJS::DiagnosticMessage> &&warnings)': takes a type
      Python has no way to hand over yet.
    - Qt's 'QQmlJSImporter::ImportedTypes::ImportedTypes(ImportedTypes
      &&a0)': takes a type Python has no way to hand over yet.
    - Qt's 'ImportedTypes &QQmlJSImporter::ImportedTypes::operator=(const
      ImportedTypes &a0)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'ImportedTypes
      &QQmlJSImporter::ImportedTypes::operator=(ImportedTypes &&a0)':
      assignment: Python binds a name and has no operator for it.
    - Qt's 'QQmlJSImporter::ImportedTypes::~ImportedTypes()': the destructor:
      Python removes its C++ QQmlJSImporter::ImportedTypes by it, and has no
      other use for it.
    - Qt's 'const QList<QQmlJS::DiagnosticMessage>
      &QQmlJSImporter::ImportedTypes::warnings() const': gives a type Python
      has no way to take yet.
    - Qt's 'QQmlJS::ImportedScope<QQmlJSScope::ConstPtr>
      QQmlJSImporter::ImportedTypes::type(const QString &name) const': gives
      a type Python has no way to take yet.
    - Qt's 'QString QQmlJSImporter::ImportedTypes::name(const
      QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
      hand over yet.
    - Qt's 'const QHash<QString, QQmlJS::ContextualType>
      &QQmlJSImporter::ImportedTypes::types() const': gives a type Python has
      no way to take yet.
    - Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString>
      &QQmlJSImporter::ImportedTypes::names() const': gives a type Python has
      no way to take yet.
    - Qt's 'void QQmlJSImporter::ImportedTypes::add(ImportedTypes &&other)':
      takes a type Python has no way to hand over yet.
    - Qt's 'void QQmlJSImporter::ImportedTypes::addWarnings(QList<QQmlJS::
      DiagnosticMessage> &&warnings)': takes a type Python has no way to hand
      over yet.

    What to expect
    --------------

    - The C++ QQmlJSImporter::ImportedTypes is created at the first use, not
      by 'QQmlJSImporter::ImportedTypes(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSImporter::ImportedTypes back gives a copy the
      ritual made for Python, in a new cute QQmlJSImporter::ImportedTypes.
    - Each name of Qt's QQmlJSImporter::ImportedTypes that has no cute
      function yet, 'add', 'addWarnings', 'name', 'names', 'type', 'types',
      'warnings', holds a function that raises 'NotImplementedError', and its
      docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSImporter::ImportedTypes'

    #  Qt's '~QQmlJSImporter::ImportedTypes()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlJSImporter::ImportedTypes behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QQmlJSImporter13ImportedTypesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def contextualTypes(self) -> QQmlJS.ContextualTypes:
      """
      Calls Qt's 'const QQmlJS::ContextualTypes
      &QQmlJSImporter::ImportedTypes::contextualTypes() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html

      Returns
      -------

      QQmlJS.ContextualTypes
        A new cute QQmlJS::ContextualTypes around the copy Qt gave back.
        Python owns it.
      """
      #  const QQmlJS::ContextualTypes
      #      &QQmlJSImporter::ImportedTypes::contextualTypes() const
      address = self.uglySide.call(
          'ritual_ZNK14QQmlJSImporter13ImportedTypes15contextualTypesEv',
      )
      return QQmlJS.ContextualTypes._cuteOwning(address)

    def isEmpty(self) -> bool:
      """
      Calls Qt's 'bool QQmlJSImporter::ImportedTypes::isEmpty() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html#isEmpty
      """
      #  bool QQmlJSImporter::ImportedTypes::isEmpty() const
      return self.uglySide.call(
          'ritual_ZNK14QQmlJSImporter13ImportedTypes7isEmptyEv',
      )

    @overload(str)
    def hasType(self, name: str) -> bool:
      """
      Calls Qt's 'bool QQmlJSImporter::ImportedTypes::hasType(const QString
      &name) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html#hasType

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QQmlJSImporter::ImportedTypes::hasType(const QString &name)
      #      const
      return self.uglySide.call(
          'ritual_ZNK14QQmlJSImporter13ImportedTypes7hasTypeERK7QString',
          name,
      )

    @overload(str)
    def isNullType(self, name: str) -> bool:
      """
      Calls Qt's 'bool QQmlJSImporter::ImportedTypes::isNullType(const
      QString &name) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html#isNullType

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  bool QQmlJSImporter::ImportedTypes::isNullType(const QString &name)
      #      const
      return self.uglySide.call(
          'ritual_ZNK14QQmlJSImporter13ImportedTypes10isNullTypeERK7QString',
          name,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def setCurrentFileSelector(self, selector: str) -> None:
      """
      Calls Qt's 'void
      QQmlJSImporter::ImportedTypes::setCurrentFileSelector(const QString
      &selector)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html

      Parameters
      ----------

      selector : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  void QQmlJSImporter::ImportedTypes::setCurrentFileSelector(const
      #      QString &selector)
      self.uglySide.call(
          'ritual_ZN14QQmlJSImporter13ImportedTypes22setCurrentFileSelector'
          'ERK7QString',
          selector,
      )

    @overload(str, WAIT['QQmlJS.ContextualType'])
    def setType(self, name: str, type: QQmlJS.ContextualType) -> None:
      """
      Calls Qt's 'void QQmlJSImporter::ImportedTypes::setType(const QString
      &name, const QQmlJS::ContextualType &type)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html#setType

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.

      type : QQmlJS.ContextualType
        Passed on as a value: Qt reads the C++ QQmlJS::ContextualType, which
        stays Python's own.
      """
      #  void QQmlJSImporter::ImportedTypes::setType(const QString &name,
      #      const QQmlJS::ContextualType &type)
      self.uglySide.call(
          'ritual_ZN14QQmlJSImporter13ImportedTypes7setTypeERK7QStringRKN6Q'
          'QmlJS14ContextualTypeE',
          name, self._valueOf(type),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __init__(self, a0: QQmlJSImporter.ImportedTypes) -> None:
      """
      Notes what was given, for Qt's
      'QQmlJSImporter::ImportedTypes::ImportedTypes(const ImportedTypes
      &a0)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html#ImportedTypes

      Parameters
      ----------

      a0 : QQmlJSImporter.ImportedTypes
        Passed on as a value: Qt reads the C++ QQmlJSImporter::ImportedTypes,
        which stays Python's own.
      """
      #  QQmlJSImporter::ImportedTypes::ImportedTypes(const ImportedTypes
      #      &a0)
      self._noteCreation(QQmlJSImporter.ImportedTypes, lambda: Rituals.call(
          'ritual_ZN14QQmlJSImporter13ImportedTypesC1ERKS0_',
          self._valueOf(a0),
      ))

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

    def clear(self) -> None:
      """
      Calls Qt's 'void QQmlJSImporter::ImportedTypes::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmljsimporter-importedtypes.html#clear
      """
      #  void QQmlJSImporter::ImportedTypes::clear()
      self.uglySide.call('ritual_ZN14QQmlJSImporter13ImportedTypes5clearEv')

    @staticmethod
    def add(*__, **_) -> Never:
      """
      Qt's 'void QQmlJSImporter::ImportedTypes::add(ImportedTypes &&other)':
      takes a type Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.add' has no cute function yet. "
          "Qt's 'void QQmlJSImporter::ImportedTypes::add(ImportedTypes "
          "&&other)': takes a type Python has no way to hand over yet.")

    @staticmethod
    def addWarnings(*__, **_) -> Never:
      """
      Qt's 'void QQmlJSImporter::ImportedTypes::addWarnings(QList<QQmlJS::
      DiagnosticMessage> &&warnings)': takes a type Python has no way to hand
      over yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.addWarnings' has no cute function "
          "yet. Qt's 'void "
          "QQmlJSImporter::ImportedTypes::addWarnings(QList<QQmlJS::Diagnost"
          "icMessage> &&warnings)': takes a type Python has no way to hand "
          "over yet.")

    @staticmethod
    def name(*__, **_) -> Never:
      """
      Qt's 'QString QQmlJSImporter::ImportedTypes::name(const
      QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
      hand over yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.name' has no cute function yet. "
          "Qt's 'QString QQmlJSImporter::ImportedTypes::name(const "
          "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
          "way to hand over yet.")

    @staticmethod
    def names(*__, **_) -> Never:
      """
      Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString>
      &QQmlJSImporter::ImportedTypes::names() const': gives a type Python has
      no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.names' has no cute function yet. "
          "Qt's 'const QMultiHash<QQmlJSScope::ConstPtr, QString> "
          "&QQmlJSImporter::ImportedTypes::names() const': gives a type "
          "Python has no way to take yet.")

    @staticmethod
    def type(*__, **_) -> Never:
      """
      Qt's 'QQmlJS::ImportedScope<QQmlJSScope::ConstPtr>
      QQmlJSImporter::ImportedTypes::type(const QString &name) const': gives
      a type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.type' has no cute function yet. "
          "Qt's 'QQmlJS::ImportedScope<QQmlJSScope::ConstPtr> "
          "QQmlJSImporter::ImportedTypes::type(const QString &name) const': "
          "gives a type Python has no way to take yet.")

    @staticmethod
    def types(*__, **_) -> Never:
      """
      Qt's 'const QHash<QString, QQmlJS::ContextualType>
      &QQmlJSImporter::ImportedTypes::types() const': gives a type Python has
      no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.types' has no cute function yet. "
          "Qt's 'const QHash<QString, QQmlJS::ContextualType> "
          "&QQmlJSImporter::ImportedTypes::types() const': gives a type "
          "Python has no way to take yet.")

    @staticmethod
    def warnings(*__, **_) -> Never:
      """
      Qt's 'const QList<QQmlJS::DiagnosticMessage>
      &QQmlJSImporter::ImportedTypes::warnings() const': gives a type Python
      has no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlJSImporter.ImportedTypes.warnings' has no cute function "
          "yet. Qt's 'const QList<QQmlJS::DiagnosticMessage> "
          "&QQmlJSImporter::ImportedTypes::warnings() const': gives a type "
          "Python has no way to take yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSImporter'

  #  Qt's '~QQmlJSImporter()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJSImporter behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QQmlJSImporterD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resourceFileMapper(self) -> Optional[QQmlJSResourceFileMapper]:
    """
    Calls Qt's 'const QQmlJSResourceFileMapper
    *QQmlJSImporter::resourceFileMapper() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#resourceFileMapper

    Returns
    -------

    Optional[QQmlJSResourceFileMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlJSResourceFileMapper *QQmlJSImporter::resourceFileMapper()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlJSImporter18resourceFileMapperEv',
    )
    from . import QQmlJSResourceFileMapper
    return QQmlJSResourceFileMapper._cuteAt(address)

  def metaDataMapper(self) -> Optional[QQmlJSResourceFileMapper]:
    """
    Calls Qt's 'QQmlJSResourceFileMapper *QQmlJSImporter::metaDataMapper()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimporter.html#metaDataMapper

    Returns
    -------

    Optional[QQmlJSResourceFileMapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJSResourceFileMapper *QQmlJSImporter::metaDataMapper() const
    address = self.uglySide.call(
        'ritual_ZNK14QQmlJSImporter14metaDataMapperEv',
    )
    from . import QQmlJSResourceFileMapper
    return QQmlJSResourceFileMapper._cuteAt(address)

  def importPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSImporter::importPaths() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimporter.html#importPaths

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSImporter::importPaths() const
    address = self.uglySide.call('ritual_ZNK14QQmlJSImporter11importPathsEv')
    return QStringList._cuteOwning(address)

  @overload(str, QTypeRevision)
  def pathOfModule(self, moduleName: str, revision: QTypeRevision) -> str:
    """
    Calls Qt's 'QString QQmlJSImporter::pathOfModule(const QString
    &moduleName, QTypeRevision revision) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimporter.html#pathOfModule

    Parameters
    ----------

    moduleName : str
      Passed on as it is: a QString is made of it for the call.

    revision : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSImporter::pathOfModule(const QString &moduleName,
    #      QTypeRevision revision) const
    return self.uglySide.call(
        'ritual_ZNK14QQmlJSImporter12pathOfModuleERK7QString13QTypeRevision',
        moduleName, self._valueOf(revision),
    )

  def useOptionalImports(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSImporter::useOptionalImports() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#useOptionalImports
    """
    #  bool QQmlJSImporter::useOptionalImports() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlJSImporter18useOptionalImportsEv',
    )

  def preferQmlFilesFromSourceFolder(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSImporter::preferQmlFilesFromSourceFolder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#preferQmlFilesFromSourceFolder
    """
    #  bool QQmlJSImporter::preferQmlFilesFromSourceFolder() const
    return self.uglySide.call(
        'ritual_ZNK14QQmlJSImporter30preferQmlFilesFromSourceFolderEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlJSResourceFileMapper)
  @overload(NoneType)
  def setResourceFileMapper(
      self,
      mapper: Optional[QQmlJSResourceFileMapper],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSImporter::setResourceFileMapper(const
    QQmlJSResourceFileMapper *mapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#setResourceFileMapper

    Parameters
    ----------

    mapper : Optional[QQmlJSResourceFileMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImporter::setResourceFileMapper(const
    #      QQmlJSResourceFileMapper *mapper)
    self.uglySide.call(
        'ritual_ZN14QQmlJSImporter21setResourceFileMapperEPK24QQmlJSResourc'
        'eFileMapper',
        self._addressOf(mapper),
    )

  @overload(QQmlJSResourceFileMapper)
  @overload(NoneType)
  def setMetaDataMapper(
      self,
      mapper: Optional[QQmlJSResourceFileMapper],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImporter::setMetaDataMapper(QQmlJSResourceFileMapper *mapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#setMetaDataMapper

    Parameters
    ----------

    mapper : Optional[QQmlJSResourceFileMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImporter::setMetaDataMapper(QQmlJSResourceFileMapper
    #      *mapper)
    self.uglySide.call(
        'ritual_ZN14QQmlJSImporter17setMetaDataMapperEP24QQmlJSResourceFile'
        'Mapper',
        self._addressOf(mapper),
    )

  @overload(QStringList)
  def setImportPaths(self, importPaths: QStringList) -> None:
    """
    Calls Qt's 'void QQmlJSImporter::setImportPaths(const QStringList
    &importPaths)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimporter.html#setImportPaths

    Parameters
    ----------

    importPaths : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlJSImporter::setImportPaths(const QStringList &importPaths)
    self.uglySide.call(
        'ritual_ZN14QQmlJSImporter14setImportPathsERK5QListI7QStringE',
        self._valueOf(importPaths),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlJSImporter::QQmlJSImporter(const QStringList &importPaths,
    QQmlJSResourceFileMapper *mapper, QQmlJSImporterFlags flags)': names the
    enum 'QQmlJSImporterFlag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.__init__' has no cute function yet. Qt's "
        "'QQmlJSImporter::QQmlJSImporter(const QStringList &importPaths, "
        "QQmlJSResourceFileMapper *mapper, QQmlJSImporterFlags flags)': "
        "names the enum 'QQmlJSImporterFlag', whose class cannot be named "
        "here.")

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

  def importHardCodedBuiltins(self) -> ImportedTypes:
    """
    Calls Qt's 'ImportedTypes QQmlJSImporter::importHardCodedBuiltins()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#importHardCodedBuiltins

    Returns
    -------

    ImportedTypes
      A new cute QQmlJSImporter::ImportedTypes around the copy Qt gave back.
      Python owns it.
    """
    #  ImportedTypes QQmlJSImporter::importHardCodedBuiltins()
    address = self.uglySide.call(
        'ritual_ZN14QQmlJSImporter23importHardCodedBuiltinsEv',
    )
    return QQmlJSImporter.ImportedTypes._cuteOwning(address)

  @overload(str, int)
  @overload(str, int, str)
  def importDirectory(
      self,
      directory: str,
      precedence: int,
      prefix: str = '',
  ) -> ImportedTypes:
    """
    Calls Qt's 'ImportedTypes QQmlJSImporter::importDirectory(const QString
    &directory, quint8 precedence, const QString &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#importDirectory

    Parameters
    ----------

    directory : str
      Passed on as it is: a QString is made of it for the call.

    precedence : int
      Passed on as it is.

    prefix : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    ImportedTypes
      A new cute QQmlJSImporter::ImportedTypes around the copy Qt gave back.
      Python owns it.
    """
    #  ImportedTypes QQmlJSImporter::importDirectory(const QString
    #      &directory, quint8 precedence, const QString &prefix)
    address = self.uglySide.call(
        'ritual_ZN14QQmlJSImporter15importDirectoryERK7QStringhS2_',
        directory, precedence, prefix,
    )
    return QQmlJSImporter.ImportedTypes._cuteOwning(address)

  def builtinInternalNames(self) -> ImportedTypes:
    """
    Calls Qt's 'ImportedTypes QQmlJSImporter::builtinInternalNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimporter.html#builtinInternalNames

    Returns
    -------

    ImportedTypes
      A new cute QQmlJSImporter::ImportedTypes around the copy Qt gave back.
      Python owns it.
    """
    #  ImportedTypes QQmlJSImporter::builtinInternalNames()
    address = self.uglySide.call(
        'ritual_ZN14QQmlJSImporter20builtinInternalNamesEv',
    )
    return QQmlJSImporter.ImportedTypes._cuteOwning(address)

  def clearCache(self) -> None:
    """
    Calls Qt's 'void QQmlJSImporter::clearCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimporter.html#clearCache
    """
    #  void QQmlJSImporter::clearCache()
    self.uglySide.call('ritual_ZN14QQmlJSImporter10clearCacheEv')

  @staticmethod
  def builtinImportHelper(*__, **_) -> Never:
    """
    Qt's 'AvailableTypes QQmlJSImporter::builtinImportHelper()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.builtinImportHelper' has no cute function yet. "
        "Qt's 'AvailableTypes QQmlJSImporter::builtinImportHelper()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def computeSeenVersion(*__, **_) -> Never:
    """
    Qt's 'SeenVersion QQmlJSImporter::computeSeenVersion(const QQmlJS::Import
    &importDescription, const QList<QQmlJS::Export> &existingExports,
    QTypeRevision valExportVersion) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.computeSeenVersion' has no cute function yet. Qt's "
        "'SeenVersion QQmlJSImporter::computeSeenVersion(const "
        "QQmlJS::Import &importDescription, const QList<QQmlJS::Export> "
        "&existingExports, QTypeRevision valExportVersion) const': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def createQmldirParserForFile(*__, **_) -> Never:
    """
    Qt's 'QQmlDirParser QQmlJSImporter::createQmldirParserForFile(const
    QString &filename, Import *import)': names 'QQmlJSImporter::Import',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.createQmldirParserForFile' has no cute function "
        "yet. Qt's 'QQmlDirParser "
        "QQmlJSImporter::createQmldirParserForFile(const QString &filename, "
        "Import *import)': names 'QQmlJSImporter::Import', which has no "
        "cute class yet.")

  @staticmethod
  def flags(*__, **_) -> Never:
    """
    Qt's 'QQmlJSImporterFlags QQmlJSImporter::flags() const': gives the enum
    'QQmlJSImporterFlag', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.flags' has no cute function yet. Qt's "
        "'QQmlJSImporterFlags QQmlJSImporter::flags() const': gives the "
        "enum 'QQmlJSImporterFlag', whose class cannot be named here.")

  @staticmethod
  def importDependencies(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::importDependencies(const Import &import,
    quint8 precedence, AvailableTypes *types, const QString &prefix,
    QTypeRevision version, bool isDependency)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.importDependencies' has no cute function yet. Qt's "
        "'void QQmlJSImporter::importDependencies(const Import &import, "
        "quint8 precedence, AvailableTypes *types, const QString &prefix, "
        "QTypeRevision version, bool isDependency)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def importFile(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::Ptr QQmlJSImporter::importFile(const QString &file)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.importFile' has no cute function yet. Qt's "
        "'QQmlJSScope::Ptr QQmlJSImporter::importFile(const QString "
        "&file)': gives a type Python has no way to take yet.")

  @staticmethod
  def importHelper(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSImporter::importHelper(const QString &module,
    AvailableTypes *types, quint8 precedence, const QString &prefix,
    QTypeRevision version, bool isDependency, bool isFile)': names
    'QQmlJSImporter::AvailableTypes', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.importHelper' has no cute function yet. Qt's 'bool "
        "QQmlJSImporter::importHelper(const QString &module, AvailableTypes "
        "*types, quint8 precedence, const QString &prefix, QTypeRevision "
        "version, bool isDependency, bool isFile)': names "
        "'QQmlJSImporter::AvailableTypes', which has no cute class yet.")

  @staticmethod
  def importModule(*__, **_) -> Never:
    """
    Qt's 'ImportedTypes QQmlJSImporter::importModule(const QString &module,
    quint8 precedence, const QString &prefix, QTypeRevision version,
    QStringList *staticModuleList)': names 'QStringList', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.importModule' has no cute function yet. Qt's "
        "'ImportedTypes QQmlJSImporter::importModule(const QString &module, "
        "quint8 precedence, const QString &prefix, QTypeRevision version, "
        "QStringList *staticModuleList)': names 'QStringList', which has no "
        "cute class yet.")

  @staticmethod
  def importQmldirs(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImporter::importQmldirs(const QStringList &qmltypesFiles)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.importQmldirs' has no cute function yet. Qt's "
        "'QList<QQmlJS::DiagnosticMessage> "
        "QQmlJSImporter::importQmldirs(const QStringList &qmltypesFiles)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def importedFiles(*__, **_) -> Never:
    """
    Qt's 'QHash<QString, QQmlJSScope::Ptr> QQmlJSImporter::importedFiles()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.importedFiles' has no cute function yet. Qt's "
        "'QHash<QString, QQmlJSScope::Ptr> QQmlJSImporter::importedFiles() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def insertAliases(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::insertAliases(const QQmlJS::ContextualType
    &type, QQmlJSImporter::AvailableTypes *types)': names
    'QQmlJSImporter::AvailableTypes', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.insertAliases' has no cute function yet. Qt's "
        "'void QQmlJSImporter::insertAliases(const QQmlJS::ContextualType "
        "&type, QQmlJSImporter::AvailableTypes *types)': names "
        "'QQmlJSImporter::AvailableTypes', which has no cute class yet.")

  @staticmethod
  def insertExport(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::insertExport(const QQmlJS::ContextualType
    &type, const QQmlJS::Export &valExport, const QString &qmlName,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types) const': names 'QHash<QString,
    QList<QQmlJSScope::Export>>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.insertExport' has no cute function yet. Qt's 'void "
        "QQmlJSImporter::insertExport(const QQmlJS::ContextualType &type, "
        "const QQmlJS::Export &valExport, const QString &qmlName, "
        "QHash<QString, QList<QQmlJSScope::Export>> *seenExports, "
        "QQmlJSImporter::AvailableTypes *types) const': names "
        "'QHash<QString, QList<QQmlJSScope::Export>>', which has no cute "
        "class yet.")

  @staticmethod
  def insertExportWithConflictingVersion(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::insertExportWithConflictingVersion(const
    QQmlJSExportedScope &val, quint8 precedence, const QString &qmlName,
    const QQmlJSScope::Export &valExport, const QQmlJSScope::ConstPtr &scope,
    QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types, SeenVersion seenVersion) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.insertExportWithConflictingVersion' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSImporter::insertExportWithConflictingVersion(const "
        "QQmlJSExportedScope &val, quint8 precedence, const QString "
        "&qmlName, const QQmlJSScope::Export &valExport, const "
        "QQmlJSScope::ConstPtr &scope, QHash<QString, "
        "QList<QQmlJSScope::Export>> *seenExports, "
        "QQmlJSImporter::AvailableTypes *types, SeenVersion seenVersion) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def insertExports(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::insertExports(const QQmlJS::Import
    &importDescription, const QQmlJSExportedScope &val, const QString
    &cppName, quint8 precedence, QHash<QString, QList<QQmlJSScope::Export>>
    *seenExports, QQmlJSImporter::AvailableTypes *types)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.insertExports' has no cute function yet. Qt's "
        "'void QQmlJSImporter::insertExports(const QQmlJS::Import "
        "&importDescription, const QQmlJSExportedScope &val, const QString "
        "&cppName, quint8 precedence, QHash<QString, "
        "QList<QQmlJSScope::Export>> *seenExports, "
        "QQmlJSImporter::AvailableTypes *types)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def jsGlobalObject(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::ConstPtr QQmlJSImporter::jsGlobalObject()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.jsGlobalObject' has no cute function yet. Qt's "
        "'QQmlJSScope::ConstPtr QQmlJSImporter::jsGlobalObject()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def localFile2QQmlJSScope(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::Ptr QQmlJSImporter::localFile2QQmlJSScope(const
    QString &filePath)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.localFile2QQmlJSScope' has no cute function yet. "
        "Qt's 'QQmlJSScope::Ptr QQmlJSImporter::localFile2QQmlJSScope(const "
        "QString &filePath)': gives a type Python has no way to take yet.")

  @staticmethod
  def processImport(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::processImport(const QQmlJS::Import
    &importDescription, const Import &import, quint8 precedence,
    AvailableTypes *types)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.processImport' has no cute function yet. Qt's "
        "'void QQmlJSImporter::processImport(const QQmlJS::Import "
        "&importDescription, const Import &import, quint8 precedence, "
        "AvailableTypes *types)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def readDirectory(*__, **_) -> Never:
    """
    Qt's 'Import QQmlJSImporter::readDirectory(const QString &directory)':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.readDirectory' has no cute function yet. Qt's "
        "'Import QQmlJSImporter::readDirectory(const QString &directory)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def readQmldir(*__, **_) -> Never:
    """
    Qt's 'Import QQmlJSImporter::readQmldir(const QString &dirname)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.readQmldir' has no cute function yet. Qt's 'Import "
        "QQmlJSImporter::readQmldir(const QString &dirname)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def readQmltypes(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::readQmltypes(const QString &filename, Import
    *result)': names 'QQmlJSImporter::Import', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.readQmltypes' has no cute function yet. Qt's 'void "
        "QQmlJSImporter::readQmltypes(const QString &filename, Import "
        "*result)': names 'QQmlJSImporter::Import', which has no cute class "
        "yet.")

  @staticmethod
  def resolveConflictingExports(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::Export QQmlJSImporter::resolveConflictingExports(const
    QQmlJS::Import &importDescription, const QQmlJSExportedScope &val, quint8
    precedence, QHash<QString, QList<QQmlJSScope::Export>> *seenExports,
    QQmlJSImporter::AvailableTypes *types)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.resolveConflictingExports' has no cute function "
        "yet. Qt's 'QQmlJSScope::Export "
        "QQmlJSImporter::resolveConflictingExports(const QQmlJS::Import "
        "&importDescription, const QQmlJSExportedScope &val, quint8 "
        "precedence, QHash<QString, QList<QQmlJSScope::Export>> "
        "*seenExports, QQmlJSImporter::AvailableTypes *types)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def runImportVisitor(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::runImportVisitor(QQmlJS::AST::Node *rootNode,
    const ImportVisitorPrerequisites &prerequisites)': names
    'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.runImportVisitor' has no cute function yet. Qt's "
        "'void QQmlJSImporter::runImportVisitor(QQmlJS::AST::Node "
        "*rootNode, const ImportVisitorPrerequisites &prerequisites)': "
        "names 'QQmlJS::AST::Node', which has no cute class yet.")

  @staticmethod
  def setFlags(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::setFlags(const QQmlJSImporterFlags &flags)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.setFlags' has no cute function yet. Qt's 'void "
        "QQmlJSImporter::setFlags(const QQmlJSImporterFlags &flags)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def setImportVisitor(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::setImportVisitor(ImportVisitor visitor)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.setImportVisitor' has no cute function yet. Qt's "
        "'void QQmlJSImporter::setImportVisitor(ImportVisitor visitor)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setQualifiedNamesOn(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImporter::setQualifiedNamesOn(const Import &import)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.setQualifiedNamesOn' has no cute function yet. "
        "Qt's 'void QQmlJSImporter::setQualifiedNamesOn(const Import "
        "&import)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def takeGlobalWarnings(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImporter::takeGlobalWarnings()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImporter.takeGlobalWarnings' has no cute function yet. Qt's "
        "'QList<QQmlJS::DiagnosticMessage> "
        "QQmlJSImporter::takeGlobalWarnings()': gives a type Python has no "
        "way to take yet.")
