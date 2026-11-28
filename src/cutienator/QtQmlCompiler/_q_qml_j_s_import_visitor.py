"""
QQmlJSImportVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimportvisitor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSImportVisitor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from ..QtQml import QQmlJS
from . import QQmlSA, QQmlJSImporter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSAnnotation, QQmlJSLogger, QQmlJSMetaPropertyBinding
  from . import QQmlJSResourceFileMapper, QQmlJSScopesById
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSLogger = WAIT['QQmlJSLogger']
  QQmlJSMetaPropertyBinding = WAIT['QQmlJSMetaPropertyBinding']
  QQmlJSResourceFileMapper = WAIT['QQmlJSResourceFileMapper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSImportVisitor(QQmlJS.AST.Visitor):
  """
  The cute side of Qt's QQmlJSImportVisitor: a plain Python object standing
  in front of one C++ QQmlJSImportVisitor.

  It is built on the cute 'QQmlJS::AST::Visitor', as Qt's QQmlJSImportVisitor
  is built on Qt's QQmlJS::AST::Visitor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJSImportVisitor that has a ritual and that
  Python can call so far, 38 names in all: 'logger', 'imports',
  'addressableScopes', 'implicitImportDirectory', 'importer',
  'seenModuleQualifiers', 'visit', 'endVisit', 'throwRecursionDepthError',
  'createAttachedAndGroupedScopes', 'openAttachedAndGroupedScopes',
  'forgetFunctionExpression', 'populateRuntimeFunctionIndicesForDocument',
  'enterEnvironment', 'enterEnvironmentNonUnique', 'leaveEnvironment',
  'parseAnnotations', 'setAllBindings', 'addDefaultProperties',
  'processDefaultProperties', 'processPropertyBindings',
  'checkRequiredProperties', 'processPropertyTypes', 'processMethodTypes',
  'processPropertyBindingObjects', 'flushPendingSignalParameters',
  'rootScopeIsValid', 'isImportPrefix', 'importBaseModules',
  'resolveAliases', 'populatePropertyAliases', 'resolveGroupProperties',
  'handleIdDeclaration', 'handleLiteralBinding',
  'visitFunctionExpressionHelper', 'addImportWithLocation',
  'populateCurrentScope', 'enterRootScope'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSImportVisitor::~QQmlJSImportVisitor()': the destructor:
    Python never removes a C++ QQmlJSImportVisitor.
  - Qt's 'QQmlJSScope::Ptr QQmlJSImportVisitor::result() const': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlJSLogger *QQmlJSImportVisitor::logger()': takes in Python what
    'const QQmlJSLogger *QQmlJSImportVisitor::logger() const' takes.
  - Qt's 'QDuplicateTracker<QQmlJSScope::ConstPtr>
    *QQmlJSImportVisitor::knownUnresolvedTypes()': gives
    'QDuplicateTracker<QQmlJSScope::ConstPtr>', which has no cute class yet.
  - Qt's 'QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler>
    QQmlJSImportVisitor::signalHandlers() const': gives a type Python has no
    way to take yet.
  - Qt's 'QList<QQmlJSScope::ConstPtr> QQmlJSImportVisitor::qmlTypes()
    const': gives a type Python has no way to take yet.
  - Qt's 'QHash<QV4::CompiledData::Location, QQmlJSScope::ConstPtr>
    QQmlJSImportVisitor::scopesBylocation() const': gives a type Python has
    no way to take yet.
  - Qt's 'const QQmlJSImporter *QQmlJSImportVisitor::importer() const': takes
    in Python what 'QQmlJSImporter *QQmlJSImportVisitor::importer()' takes.
  - Qt's 'bool QQmlJSImportVisitor::checkCustomParser(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlJSImportVisitor::setScopeName(QQmlJSScope::Ptr &scope,
    QQmlJSScope::ScopeType type, const QString &name)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool QQmlJSImportVisitor::safeInsertJSIdentifier(QQmlJSScope::Ptr
    &scope, const QString &name, const QQmlJSScope::JavaScriptIdentifier
    &identifier)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSMetaMethod::RelativeFunctionIndex
    QQmlJSImportVisitor::addFunctionOrExpression(const QQmlJSScope::ConstPtr
    &scope, const QString &name)': takes a type Python has no way to hand
    over yet.
  - Qt's 'int
    QQmlJSImportVisitor::synthesizeCompilationUnitRuntimeFunctionIndices(
    const QQmlJSScope::Ptr &scope, int count) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QQmlJSImportVisitor::checkTypeResolved(const
    QQmlJSScope::ConstPtr &type)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlJSImportVisitor::warnUnresolvedType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlJSImportVisitor::warnMissingPropertyForBinding(const
    QString &property, const QQmlJS::SourceLocation &location, const
    std::optional<QQmlJSFixSuggestion> &fixSuggestion)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QQmlJSImportVisitor::breakInheritanceCycles(const
    QQmlJSScope::Ptr &scope)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQmlJSImportVisitor::checkDeprecation(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void
    QQmlJSImportVisitor::checkGroupedAndAttachedScopes(QQmlJSScope::ConstPtr
    scope)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlJSImportVisitor::checkForComponentTypeWithProperties(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
  - Qt's 'BindingExpressionParseResult
    QQmlJSImportVisitor::parseBindingExpression(const QString &name, const
    QQmlJS::AST::Statement *statement, const QQmlJS::AST::UiPublicMember
    *associatedPropertyDefinition)': gives the enum
    'QQmlJSImportVisitor::BindingExpressionParseResult', whose class cannot
    be named here.
  - Qt's 'void QQmlJSImportVisitor::checkSignal(const QQmlJSScope::ConstPtr
    &signalScope, const QQmlJS::SourceLocation &location, const QString
    &handlerName, const QStringList &handlerParameters)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QQmlJSImportVisitor::processImportWarnings(const QString
    &what, const QList<QQmlJS::DiagnosticMessage> &warnings, const
    QQmlJS::SourceLocation &srcLocation)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImportVisitor::importFromHost(const QString &path, const QString
    &prefix, const QQmlJS::SourceLocation &location)': gives a type Python
    has no way to take yet.
  - Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImportVisitor::importFromQrc(const QString &path, const QString
    &prefix, const QQmlJS::SourceLocation &location)': gives a type Python
    has no way to take yet.

  What has no ritual
  ------------------

  2 of the 116 functions Qt declares: 1 a template; 1 not a gap.

  What to expect
  --------------

  - The C++ QQmlJSImportVisitor is created at the first use, not by
    'QQmlJSImportVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSImportVisitor.
  - Each name of Qt's QQmlJSImportVisitor that has no cute function yet,
    'addFunctionOrExpression', 'breakInheritanceCycles', 'checkCustomParser',
    'checkDeprecation', 'checkForComponentTypeWithProperties',
    'checkGroupedAndAttachedScopes', 'checkSignal', 'checkTypeResolved',
    'importFromHost', 'importFromQrc', 'knownUnresolvedTypes',
    'parseBindingExpression', 'processImportWarnings', 'qmlTypes', 'result',
    'safeInsertJSIdentifier', 'scopesBylocation', 'setScopeName',
    'signalHandlers', 'synthesizeCompilationUnitRuntimeFunctionIndices',
    'warnMissingPropertyForBinding', 'warnUnresolvedType', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlJSImportVisitor, each a class in here
  #  as in C++.

  class UnfinishedBinding(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlJSImportVisitor::UnfinishedBinding: a plain
    Python object standing in front of one C++
    QQmlJSImportVisitor::UnfinishedBinding.

    C++ hands a QQmlJSImportVisitor::UnfinishedBinding around as a copy, so
    every C++ QQmlJSImportVisitor::UnfinishedBinding behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlJSImportVisitor::UnfinishedBinding yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlJSImportVisitor::UnfinishedBinding::~UnfinishedBinding()':
      the destructor: Python removes its C++
      QQmlJSImportVisitor::UnfinishedBinding by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlJSImportVisitor::UnfinishedBinding is created at the first
      use, not by 'QQmlJSImportVisitor::UnfinishedBinding(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlJSImportVisitor::UnfinishedBinding back gives a
      copy the ritual made for Python, in a new cute
      QQmlJSImportVisitor::UnfinishedBinding.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlJSImportVisitor::UnfinishedBinding'

    #  Qt's '~QQmlJSImportVisitor::UnfinishedBinding()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QQmlJSImportVisitor::UnfinishedBinding behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QQmlJSImportVisitor17UnfinishedBindingD1Ev')

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
  @overload(str, QQmlJSResourceFileMapper)
  @overload(str, NoneType)
  def implicitImportDirectory(
      localFile: str,
      mapper: Optional[QQmlJSResourceFileMapper],
  ) -> str:
    """
    Calls Qt's 'QString QQmlJSImportVisitor::implicitImportDirectory(const
    QString &localFile, const QQmlJSResourceFileMapper *mapper)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#implicitImportDirectory

    Parameters
    ----------

    localFile : str
      Passed on as it is: a QString is made of it for the call.

    mapper : Optional[QQmlJSResourceFileMapper]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSImportVisitor::implicitImportDirectory(const QString
    #      &localFile, const QQmlJSResourceFileMapper *mapper)
    return Rituals.call(
        'ritual_ZN19QQmlJSImportVisitor23implicitImportDirectoryERK7QString'
        'PK24QQmlJSResourceFileMapper',
        localFile, CuteMixin._addressOf(mapper),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSImportVisitor'

  #  A C++ QQmlJSImportVisitor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSImportVisitor'

  #  The functions Qt calls itself that QQmlJSImportVisitor is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'checkCustomParser': (
          'bool QQmlJSImportVisitor::checkCustomParser(const '
          'QQmlJSScope::ConstPtr &)',
      ),
      'safeInsertJSIdentifier': (
          'bool '
          'QQmlJSImportVisitor::safeInsertJSIdentifier(QQmlJSScope::Ptr &, '
          'const QString &, const QQmlJSScope::JavaScriptIdentifier &)',
      ),
      'parseBindingExpression': (
          'BindingExpressionParseResult '
          'QQmlJSImportVisitor::parseBindingExpression(const QString &, '
          'const QQmlJS::AST::Statement *, const '
          'QQmlJS::AST::UiPublicMember *)',
      ),
  }

  #  The functions Qt calls itself that QQmlJSImportVisitor is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'leaveEnvironment': (
          ('_ZN19QQmlJSImportVisitor16leaveEnvironmentEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'handleLiteralBinding': (
          ('_ZN19QQmlJSImportVisitor20handleLiteralBindingERK25QQmlJSMetaPr'
           'opertyBindingPKN6QQmlJS3AST14UiPublicMemberE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value',
                'QtQmlCompiler:QQmlJSMetaPropertyBinding'),
               ('address', 'address', 'QtQml:QQmlJS.AST.UiPublicMember'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def logger(self) -> Optional[QQmlJSLogger]:
    """
    Calls Qt's 'const QQmlJSLogger *QQmlJSImportVisitor::logger() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#logger

    Returns
    -------

    Optional[QQmlJSLogger]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlJSLogger *QQmlJSImportVisitor::logger() const
    address = self.uglySide.call('ritual_ZNK19QQmlJSImportVisitor6loggerEv')
    from . import QQmlJSLogger
    return QQmlJSLogger._cuteAt(address)

  def imports(self) -> QQmlJSImporter.ImportedTypes:
    """
    Calls Qt's 'QQmlJSImporter::ImportedTypes QQmlJSImportVisitor::imports()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#imports

    Returns
    -------

    QQmlJSImporter.ImportedTypes
      A new cute QQmlJSImporter::ImportedTypes around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlJSImporter::ImportedTypes QQmlJSImportVisitor::imports() const
    address = self.uglySide.call('ritual_ZNK19QQmlJSImportVisitor7importsEv')
    return QQmlJSImporter.ImportedTypes._cuteOwning(address)

  def addressableScopes(self) -> QQmlJSScopesById:
    """
    Calls Qt's 'QQmlJSScopesById QQmlJSImportVisitor::addressableScopes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#addressableScopes

    Returns
    -------

    QQmlJSScopesById
      A new cute QQmlJSScopesById around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSScopesById QQmlJSImportVisitor::addressableScopes() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSImportVisitor17addressableScopesEv',
    )
    from . import QQmlJSScopesById
    return QQmlJSScopesById._cuteOwning(address)

  def seenModuleQualifiers(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQmlJSImportVisitor::seenModuleQualifiers()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#seenModuleQualifiers

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlJSImportVisitor::seenModuleQualifiers() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlJSImportVisitor20seenModuleQualifiersEv',
    )
    return QStringList._cuteOwning(address)

  def rootScopeIsValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::rootScopeIsValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#rootScopeIsValid
    """
    #  bool QQmlJSImportVisitor::rootScopeIsValid() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSImportVisitor16rootScopeIsValidEv',
    )

  @overload(str)
  def isImportPrefix(self, prefix: str) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::isImportPrefix(QString prefix)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#isImportPrefix

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJSImportVisitor::isImportPrefix(QString prefix) const
    return self.uglySide.call(
        'ritual_ZNK19QQmlJSImportVisitor14isImportPrefixE7QString', prefix,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setAllBindings(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::setAllBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#setAllBindings
    """
    #  void QQmlJSImportVisitor::setAllBindings()
    self.uglySide.call('ritual_ZN19QQmlJSImportVisitor14setAllBindingsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlJSImporter, QQmlJSLogger, str, QStringList)
  @overload(QQmlJSImporter, NoneType, str, QStringList)
  @overload(NoneType, QQmlJSLogger, str, QStringList)
  @overload(NoneType, NoneType, str, QStringList)
  def __init__(
      self,
      importer: Optional[QQmlJSImporter],
      logger: Optional[QQmlJSLogger],
      implicitImportDirectory: str,
      qmldirFiles: QStringList,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSImportVisitor::QQmlJSImportVisitor(QQmlJSImporter *importer,
    QQmlJSLogger *logger, const QString &implicitImportDirectory, const
    QStringList &qmldirFiles)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#QQmlJSImportVisitor

    Parameters
    ----------

    importer : Optional[QQmlJSImporter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    logger : Optional[QQmlJSLogger]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    implicitImportDirectory : str
      Passed on as it is: a QString is made of it for the call.

    qmldirFiles : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  QQmlJSImportVisitor::QQmlJSImportVisitor(QQmlJSImporter *importer,
    #      QQmlJSLogger *logger, const QString &implicitImportDirectory,
    #      const QStringList &qmldirFiles)
    self._noteCreation(QQmlJSImportVisitor, lambda: Rituals.call(
        'ritual_ZN19QQmlJSImportVisitorC1EP14QQmlJSImporterP12QQmlJSLoggerR'
        'K7QStringRK5QListIS4_E',
        self._addressOf(importer), self._addressOf(logger),
        implicitImportDirectory, self._valueOf(qmldirFiles),
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

  def importer(self) -> Optional[QQmlJSImporter]:
    """
    Calls Qt's 'QQmlJSImporter *QQmlJSImportVisitor::importer()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#importer

    Returns
    -------

    Optional[QQmlJSImporter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJSImporter *QQmlJSImportVisitor::importer()
    address = self.uglySide.call('ritual_ZN19QQmlJSImportVisitor8importerEv')
    return QQmlJSImporter._cuteAt(address)

  @overload(WAIT['QQmlJS.AST.ExpressionStatement'])
  @overload(NoneType)
  def visit(self, ast: Optional[QQmlJS.AST.ExpressionStatement]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::ExpressionStatement *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ExpressionStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExpressionStatement *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19ExpressionStat'
        'ementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19Expressi'
          'onStatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiProgram'])
  def visit(self, a0: Optional[QQmlJS.AST.UiProgram]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiProgram *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiProgram *a0)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9UiProgramE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9UiProgram'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  def visit(self, a0: Optional[QQmlJS.AST.UiObjectDefinition]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectDefinition *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectDefinition *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18UiObjectDefini'
        'tionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18UiObject'
          'DefinitionE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiInlineComponent'])
  def visit(self, a0: Optional[QQmlJS.AST.UiInlineComponent]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::UiInlineComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiInlineComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiInlineComponent *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiInlineCompon'
        'entE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiInline'
          'ComponentE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPublicMember'])
  def visit(self, a0: Optional[QQmlJS.AST.UiPublicMember]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPublicMember
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPublicMember *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiPublicMember'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiPublic'
          'MemberE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiRequired'])
  def visit(self, required: Optional[QQmlJS.AST.UiRequired]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiRequired
    *required)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    required : Optional[QQmlJS.AST.UiRequired]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiRequired *required)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST10UiRequiredE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST10UiRequir'
          'edE')
    return self.uglySide.call(ritual, self._addressOf(required))

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  def visit(self, a0: Optional[QQmlJS.AST.UiScriptBinding]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiScriptBinding
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiScriptBinding *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiScriptBindin'
        'gE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiScript'
          'BindingE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayBinding'])
  def visit(self, a0: Optional[QQmlJS.AST.UiArrayBinding]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiArrayBinding
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiArrayBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiArrayBinding *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiArrayBinding'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiArrayB'
          'indingE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiEnumDeclaration'])
  def visit(self, uied: Optional[QQmlJS.AST.UiEnumDeclaration]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::UiEnumDeclaration *uied)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    uied : Optional[QQmlJS.AST.UiEnumDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiEnumDeclaration *uied)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiEnumDeclarat'
        'ionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiEnumDe'
          'clarationE')
    return self.uglySide.call(ritual, self._addressOf(uied))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  def visit(self, fexpr: Optional[QQmlJS.AST.FunctionExpression]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionExpression *fexpr)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    fexpr : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionExpression
    #      *fexpr)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18FunctionExpres'
        'sionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18Function'
          'ExpressionE')
    return self.uglySide.call(ritual, self._addressOf(fexpr))

  @overload(WAIT['QQmlJS.AST.UiSourceElement'])
  def visit(self, a0: Optional[QQmlJS.AST.UiSourceElement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiSourceElement
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiSourceElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiSourceElement *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiSourceElemen'
        'tE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiSource'
          'ElementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def visit(self, fdecl: Optional[QQmlJS.AST.FunctionDeclaration]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionDeclaration *fdecl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    fdecl : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionDeclaration
    #      *fdecl)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FunctionDeclar'
        'ationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19Function'
          'DeclarationE')
    return self.uglySide.call(ritual, self._addressOf(fdecl))

  @overload(WAIT['QQmlJS.AST.ClassExpression'])
  def visit(self, ast: Optional[QQmlJS.AST.ClassExpression]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassExpression
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ClassExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassExpression *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15ClassExpressio'
        'nE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15ClassExp'
          'ressionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiImport'])
  def visit(self, import_: Optional[QQmlJS.AST.UiImport]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiImport
    *import)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    import_ : Optional[QQmlJS.AST.UiImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiImport *import)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiImportE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiImportE')
    return self.uglySide.call(ritual, self._addressOf(import_))

  @overload(WAIT['QQmlJS.AST.UiPragma'])
  def visit(self, pragma: Optional[QQmlJS.AST.UiPragma]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPragma
    *pragma)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    pragma : Optional[QQmlJS.AST.UiPragma]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPragma *pragma)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiPragmaE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiPragmaE')
    return self.uglySide.call(ritual, self._addressOf(pragma))

  @overload(WAIT['QQmlJS.AST.ClassDeclaration'])
  def visit(self, ast: Optional[QQmlJS.AST.ClassDeclaration]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassDeclaration
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ClassDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassDeclaration *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ClassDeclarati'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ClassDec'
          'larationE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ForStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.ForStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForStatement
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ForStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForStatement *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST12ForStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST12ForState'
          'mentE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ForEachStatement'])
  def visit(self, ast: Optional[QQmlJS.AST.ForEachStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForEachStatement
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ForEachStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForEachStatement *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ForEachStateme'
        'ntE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ForEachS'
          'tatementE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Block'])
  def visit(self, ast: Optional[QQmlJS.AST.Block]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::Block *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Block *ast)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5BlockE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5BlockE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.CaseBlock'])
  def visit(self, ast: Optional[QQmlJS.AST.CaseBlock]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::CaseBlock
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.CaseBlock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::CaseBlock *ast)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9CaseBlockE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9CaseBlock'
          'E')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Catch'])
  def visit(self, ast: Optional[QQmlJS.AST.Catch]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::Catch *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Catch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Catch *ast)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5CatchE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5CatchE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.WithStatement'])
  def visit(self, withStatement: Optional[QQmlJS.AST.WithStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::WithStatement
    *withStatement)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    withStatement : Optional[QQmlJS.AST.WithStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::WithStatement
    #      *withStatement)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST13WithStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST13WithStat'
          'ementE')
    return self.uglySide.call(ritual, self._addressOf(withStatement))

  @overload(WAIT['QQmlJS.AST.FormalParameterList'])
  def visit(self, fpl: Optional[QQmlJS.AST.FormalParameterList]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::FormalParameterList *fpl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    fpl : Optional[QQmlJS.AST.FormalParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FormalParameterList *fpl)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FormalParamete'
        'rListE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FormalPa'
          'rameterListE')
    return self.uglySide.call(ritual, self._addressOf(fpl))

  @overload(WAIT['QQmlJS.AST.UiObjectBinding'])
  def visit(self, uiob: Optional[QQmlJS.AST.UiObjectBinding]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectBinding
    *uiob)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    uiob : Optional[QQmlJS.AST.UiObjectBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectBinding *uiob)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiObjectBindin'
        'gE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiObject'
          'BindingE')
    return self.uglySide.call(ritual, self._addressOf(uiob))

  @overload(WAIT['QQmlJS.AST.ExportDeclaration'])
  def visit(self, exp: Optional[QQmlJS.AST.ExportDeclaration]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::ExportDeclaration *exp)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    exp : Optional[QQmlJS.AST.ExportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExportDeclaration *exp)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17ExportDeclarat'
        'ionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17ExportDe'
          'clarationE')
    return self.uglySide.call(ritual, self._addressOf(exp))

  @overload(WAIT['QQmlJS.AST.ESModule'])
  def visit(self, module: Optional[QQmlJS.AST.ESModule]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::ESModule
    *module)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    module : Optional[QQmlJS.AST.ESModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ESModule *module)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8ESModuleE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8ESModuleE')
    return self.uglySide.call(ritual, self._addressOf(module))

  @overload(WAIT['QQmlJS.AST.Program'])
  def visit(self, program: Optional[QQmlJS.AST.Program]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::Program
    *program)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    program : Optional[QQmlJS.AST.Program]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Program *program)
    ritual = 'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST7ProgramE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST7ProgramE')
    return self.uglySide.call(ritual, self._addressOf(program))

  @overload(WAIT['QQmlJS.AST.IdentifierExpression'])
  def visit(self, idexp: Optional[QQmlJS.AST.IdentifierExpression]) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::visit(QQmlJS::AST::IdentifierExpression *idexp)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    idexp : Optional[QQmlJS.AST.IdentifierExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IdentifierExpression
    #      *idexp)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST20IdentifierExpr'
        'essionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST20Identifi'
          'erExpressionE')
    return self.uglySide.call(ritual, self._addressOf(idexp))

  @overload(WAIT['QQmlJS.AST.PatternElement'])
  def visit(self, a0: Optional[QQmlJS.AST.PatternElement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::PatternElement
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::PatternElement *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14PatternElement'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14PatternE'
          'lementE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.IfStatement'])
  def visit(self, a0: Optional[QQmlJS.AST.IfStatement]) -> bool:
    """
    Calls Qt's 'bool QQmlJSImportVisitor::visit(QQmlJS::AST::IfStatement
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.IfStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IfStatement *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST11IfStatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST11IfStatem'
          'entE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ExpressionStatement'])
  @overload(NoneType)
  def endVisit(self, ast: Optional[QQmlJS.AST.ExpressionStatement]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExpressionStatement *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ExpressionStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExpressionStatement
    #      *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19ExpressionS'
        'tatementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19Expre'
          'ssionStatementE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiProgram'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiProgram]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiProgram
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiProgram *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9UiProgramE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9UiProg'
          'ramE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiObjectDefinition]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectDefinition *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectDefinition
    #      *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18UiObjectDef'
        'initionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18UiObj'
          'ectDefinitionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiInlineComponent'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiInlineComponent]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiInlineComponent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiInlineComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiInlineComponent *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17UiInlineCom'
        'ponentE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17UiInl'
          'ineComponentE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiPublicMember'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiPublicMember]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiPublicMember *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiPublicMember *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiPublicMem'
        'berE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiPub'
          'licMemberE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiScriptBinding]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiScriptBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiScriptBinding *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiScriptBin'
        'dingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiScr'
          'iptBindingE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayBinding'])
  def endVisit(self, a0: Optional[QQmlJS.AST.UiArrayBinding]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiArrayBinding *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiArrayBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiArrayBinding *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiArrayBind'
        'ingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiArr'
          'ayBindingE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FunctionExpression]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionExpression
    #      *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18FunctionExp'
        'ressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18Funct'
          'ionExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.FunctionDeclaration'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FunctionDeclaration]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionDeclaration *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FunctionDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionDeclaration
    #      *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19FunctionDec'
        'larationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19Funct'
          'ionDeclarationE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.ClassExpression]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.ClassExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassExpression *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15ClassExpres'
        'sionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15Class'
          'ExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.ClassDeclaration'])
  def endVisit(self, ast: Optional[QQmlJS.AST.ClassDeclaration]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassDeclaration *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ClassDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassDeclaration *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ClassDeclar'
        'ationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16Class'
          'DeclarationE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ForStatement'])
  def endVisit(self, ast: Optional[QQmlJS.AST.ForStatement]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForStatement
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ForStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForStatement *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST12ForStatemen'
        'tE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST12ForSt'
          'atementE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.ForEachStatement'])
  def endVisit(self, ast: Optional[QQmlJS.AST.ForEachStatement]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForEachStatement *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.ForEachStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForEachStatement *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ForEachStat'
        'ementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ForEa'
          'chStatementE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Block'])
  def endVisit(self, ast: Optional[QQmlJS.AST.Block]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Block *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Block *ast)
    ritual = 'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5BlockE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5BlockE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.CaseBlock'])
  def endVisit(self, ast: Optional[QQmlJS.AST.CaseBlock]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::CaseBlock
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.CaseBlock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::CaseBlock *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9CaseBlockE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9CaseBl'
          'ockE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.Catch'])
  def endVisit(self, ast: Optional[QQmlJS.AST.Catch]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Catch *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.Catch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Catch *ast)
    ritual = 'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5CatchE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5CatchE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.WithStatement'])
  def endVisit(self, ast: Optional[QQmlJS.AST.WithStatement]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::WithStatement
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.WithStatement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::WithStatement *ast)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST13WithStateme'
        'ntE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST13WithS'
          'tatementE')
    self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiObjectBinding'])
  def endVisit(self, uiob: Optional[QQmlJS.AST.UiObjectBinding]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectBinding *uiob)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    uiob : Optional[QQmlJS.AST.UiObjectBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectBinding *uiob)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiObjectBin'
        'dingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiObj'
          'ectBindingE')
    self.uglySide.call(ritual, self._addressOf(uiob))

  @overload(WAIT['QQmlJS.AST.ExportDeclaration'])
  def endVisit(self, exp: Optional[QQmlJS.AST.ExportDeclaration]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExportDeclaration *exp)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    exp : Optional[QQmlJS.AST.ExportDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExportDeclaration
    #      *exp)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17ExportDecla'
        'rationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17Expor'
          'tDeclarationE')
    self.uglySide.call(ritual, self._addressOf(exp))

  @overload(WAIT['QQmlJS.AST.ESModule'])
  def endVisit(self, module: Optional[QQmlJS.AST.ESModule]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ESModule
    *module)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    module : Optional[QQmlJS.AST.ESModule]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ESModule *module)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST8ESModuleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST8ESModu'
          'leE')
    self.uglySide.call(ritual, self._addressOf(module))

  @overload(WAIT['QQmlJS.AST.Program'])
  def endVisit(self, program: Optional[QQmlJS.AST.Program]) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Program
    *program)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    program : Optional[QQmlJS.AST.Program]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Program *program)
    ritual = 'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST7ProgramE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST7Progra'
          'mE')
    self.uglySide.call(ritual, self._addressOf(program))

  @overload(WAIT['QQmlJS.AST.FieldMemberExpression'])
  def endVisit(self, a0: Optional[QQmlJS.AST.FieldMemberExpression]) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::endVisit(QQmlJS::AST::FieldMemberExpression *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsimportvisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.FieldMemberExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FieldMemberExpression
    #      *a0)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST21FieldMember'
        'ExpressionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST21Field'
          'MemberExpressionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  def throwRecursionDepthError(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::throwRecursionDepthError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#throwRecursionDepthError
    """
    #  void QQmlJSImportVisitor::throwRecursionDepthError()
    ritual = 'ritual_ZN19QQmlJSImportVisitor24throwRecursionDepthErrorEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor24throwRecursionDepthErrorEv')
    self.uglySide.call(ritual)

  @overload(WAIT['QQmlJS.AST.UiQualifiedId'])
  @overload(NoneType)
  def createAttachedAndGroupedScopes(
      self,
      propertyName: Optional[QQmlJS.AST.UiQualifiedId],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::createAttachedAndGroupedScopes(QQmlJS::AST::
    UiQualifiedId *propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html

    Parameters
    ----------

    propertyName : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::createAttachedAndGroupedScopes(QQmlJS::AST::
    #      UiQualifiedId *propertyName)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor30createAttachedAndGroupedScopesEPN6'
        'QQmlJS3AST13UiQualifiedIdE',
        self._addressOf(propertyName),
    )

  @overload(WAIT['QQmlJS.AST.UiQualifiedId'])
  @overload(NoneType)
  def openAttachedAndGroupedScopes(
      self,
      propertyName: Optional[QQmlJS.AST.UiQualifiedId],
  ) -> int:
    """
    Calls Qt's 'int
    QQmlJSImportVisitor::openAttachedAndGroupedScopes(QQmlJS::AST::
    UiQualifiedId *propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html

    Parameters
    ----------

    propertyName : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlJSImportVisitor::openAttachedAndGroupedScopes(QQmlJS::AST::
    #      UiQualifiedId *propertyName)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor28openAttachedAndGroupedScopesEPN6QQ'
        'mlJS3AST13UiQualifiedIdE',
        self._addressOf(propertyName),
    )

  @overload(str)
  def forgetFunctionExpression(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::forgetFunctionExpression(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#forgetFunctionExpression

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlJSImportVisitor::forgetFunctionExpression(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor24forgetFunctionExpressionERK7QStrin'
        'g',
        name,
    )

  def populateRuntimeFunctionIndicesForDocument(self) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::populateRuntimeFunctionIndicesForDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html
    """
    #  void QQmlJSImportVisitor::populateRuntimeFunctionIndicesForDocument()
    #      const
    self.uglySide.call(
        'ritual_ZNK19QQmlJSImportVisitor41populateRuntimeFunctionIndicesFor'
        'DocumentEv',
    )

  @overload(QQmlSA.ScopeType, str, WAIT['QQmlJS.SourceLocation'])
  def enterEnvironment(
      self,
      type: QQmlSA.ScopeType,
      name: str,
      location: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::enterEnvironment(QQmlJSScope::ScopeType type, const
    QString &name, const QQmlJS::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#enterEnvironment

    Parameters
    ----------

    type : QQmlSA.ScopeType
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSImportVisitor::enterEnvironment(QQmlJSScope::ScopeType
    #      type, const QString &name, const QQmlJS::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor16enterEnvironmentEN6QQmlSA9ScopeTyp'
        'eERK7QStringRKN6QQmlJS14SourceLocationE',
        type.value, name, self._valueOf(location),
    )

  @overload(QQmlSA.ScopeType, str, WAIT['QQmlJS.SourceLocation'])
  def enterEnvironmentNonUnique(
      self,
      type: QQmlSA.ScopeType,
      name: str,
      location: QQmlJS.SourceLocation,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJSImportVisitor::enterEnvironmentNonUnique(QQmlJSScope::ScopeType
    type, const QString &name, const QQmlJS::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#enterEnvironmentNonUnique

    Parameters
    ----------

    type : QQmlSA.ScopeType
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  bool QQmlJSImportVisitor::enterEnvironmentNonUnique(QQmlJSScope::
    #      ScopeType type, const QString &name, const QQmlJS::SourceLocation
    #      &location)
    return self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor25enterEnvironmentNonUniqueEN6QQmlSA'
        '9ScopeTypeERK7QStringRKN6QQmlJS14SourceLocationE',
        type.value, name, self._valueOf(location),
    )

  def leaveEnvironment(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::leaveEnvironment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#leaveEnvironment
    """
    #  void QQmlJSImportVisitor::leaveEnvironment()
    ritual = 'ritual_ZN19QQmlJSImportVisitor16leaveEnvironmentEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlJSImportVisitor16leaveEnvironmentEv'
    self.uglySide.call(ritual)

  @overload(WAIT['QQmlJS.AST.UiAnnotationList'])
  @overload(NoneType)
  def parseAnnotations(
      self,
      list: Optional[QQmlJS.AST.UiAnnotationList],
  ) -> QList[QQmlJSAnnotation]:
    """
    Calls Qt's 'QList<QQmlJSAnnotation>
    QQmlJSImportVisitor::parseAnnotations(QQmlJS::AST::UiAnnotationList
    *list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#parseAnnotations

    Parameters
    ----------

    list : Optional[QQmlJS.AST.UiAnnotationList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QQmlJSAnnotation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlJSAnnotation>
    #      QQmlJSImportVisitor::parseAnnotations(QQmlJS::AST::
    #      UiAnnotationList *list)
    address = self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor16parseAnnotationsEPN6QQmlJS3AST16Ui'
        'AnnotationListE',
        self._addressOf(list),
    )
    from . import QQmlJSAnnotation
    return QList[QQmlJSAnnotation]._cuteOwning(address)

  def addDefaultProperties(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::addDefaultProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#addDefaultProperties
    """
    #  void QQmlJSImportVisitor::addDefaultProperties()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor20addDefaultPropertiesEv',
    )

  def processDefaultProperties(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::processDefaultProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#processDefaultProperties
    """
    #  void QQmlJSImportVisitor::processDefaultProperties()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor24processDefaultPropertiesEv',
    )

  def processPropertyBindings(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::processPropertyBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#processPropertyBindings
    """
    #  void QQmlJSImportVisitor::processPropertyBindings()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor23processPropertyBindingsEv',
    )

  def checkRequiredProperties(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::checkRequiredProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#checkRequiredProperties
    """
    #  void QQmlJSImportVisitor::checkRequiredProperties()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor23checkRequiredPropertiesEv',
    )

  def processPropertyTypes(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::processPropertyTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#processPropertyTypes
    """
    #  void QQmlJSImportVisitor::processPropertyTypes()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor20processPropertyTypesEv',
    )

  def processMethodTypes(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::processMethodTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#processMethodTypes
    """
    #  void QQmlJSImportVisitor::processMethodTypes()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor18processMethodTypesEv',
    )

  def processPropertyBindingObjects(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::processPropertyBindingObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html
    """
    #  void QQmlJSImportVisitor::processPropertyBindingObjects()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor29processPropertyBindingObjectsEv',
    )

  def flushPendingSignalParameters(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::flushPendingSignalParameters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html
    """
    #  void QQmlJSImportVisitor::flushPendingSignalParameters()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor28flushPendingSignalParametersEv',
    )

  def importBaseModules(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::importBaseModules()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#importBaseModules
    """
    #  void QQmlJSImportVisitor::importBaseModules()
    self.uglySide.call('ritual_ZN19QQmlJSImportVisitor17importBaseModulesEv')

  def resolveAliases(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::resolveAliases()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#resolveAliases
    """
    #  void QQmlJSImportVisitor::resolveAliases()
    self.uglySide.call('ritual_ZN19QQmlJSImportVisitor14resolveAliasesEv')

  def populatePropertyAliases(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::populatePropertyAliases()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#populatePropertyAliases
    """
    #  void QQmlJSImportVisitor::populatePropertyAliases()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor23populatePropertyAliasesEv',
    )

  def resolveGroupProperties(self) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::resolveGroupProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#resolveGroupProperties
    """
    #  void QQmlJSImportVisitor::resolveGroupProperties()
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor22resolveGroupPropertiesEv',
    )

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  @overload(NoneType)
  def handleIdDeclaration(
      self,
      scriptBinding: Optional[QQmlJS.AST.UiScriptBinding],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::handleIdDeclaration(QQmlJS::AST::UiScriptBinding
    *scriptBinding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#handleIdDeclaration

    Parameters
    ----------

    scriptBinding : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::handleIdDeclaration(QQmlJS::AST::
    #      UiScriptBinding *scriptBinding)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor19handleIdDeclarationEPN6QQmlJS3AST1'
        '5UiScriptBindingE',
        self._addressOf(scriptBinding),
    )

  @overload(QQmlJSMetaPropertyBinding, WAIT['QQmlJS.AST.UiPublicMember'])
  @overload(QQmlJSMetaPropertyBinding, NoneType)
  def handleLiteralBinding(
      self,
      a0: QQmlJSMetaPropertyBinding,
      a1: Optional[QQmlJS.AST.UiPublicMember],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::handleLiteralBinding(const
    QQmlJSMetaPropertyBinding &a0, const QQmlJS::AST::UiPublicMember *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#handleLiteralBinding

    Parameters
    ----------

    a0 : QQmlJSMetaPropertyBinding
      Passed on as a value: Qt reads the C++ QQmlJSMetaPropertyBinding, which
      stays Python's own.

    a1 : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::handleLiteralBinding(const
    #      QQmlJSMetaPropertyBinding &a0, const QQmlJS::AST::UiPublicMember
    #      *a1)
    ritual = (
        'ritual_ZN19QQmlJSImportVisitor20handleLiteralBindingERK25QQmlJSMet'
        'aPropertyBindingPKN6QQmlJS3AST14UiPublicMemberE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlJSImportVisitor20handleLiteralBindingERK25QQm'
          'lJSMetaPropertyBindingPKN6QQmlJS3AST14UiPublicMemberE')
    self.uglySide.call(ritual, self._valueOf(a0), self._addressOf(a1))

  @overload(WAIT['QQmlJS.AST.FunctionExpression'])
  @overload(NoneType)
  def visitFunctionExpressionHelper(
      self,
      fexpr: Optional[QQmlJS.AST.FunctionExpression],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::visitFunctionExpressionHelper(QQmlJS::AST::
    FunctionExpression *fexpr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html

    Parameters
    ----------

    fexpr : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSImportVisitor::visitFunctionExpressionHelper(QQmlJS::AST::
    #      FunctionExpression *fexpr)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor29visitFunctionExpressionHelperEPN6Q'
        'QmlJS3AST18FunctionExpressionE',
        self._addressOf(fexpr),
    )

  @overload(str, WAIT['QQmlJS.SourceLocation'], bool)
  def addImportWithLocation(
      self,
      name: str,
      loc: QQmlJS.SourceLocation,
      hadWarnings: bool,
  ) -> None:
    """
    Calls Qt's 'void QQmlJSImportVisitor::addImportWithLocation(const QString
    &name, const QQmlJS::SourceLocation &loc, bool hadWarnings)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#addImportWithLocation

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    hadWarnings : bool
      Passed on as it is.
    """
    #  void QQmlJSImportVisitor::addImportWithLocation(const QString &name,
    #      const QQmlJS::SourceLocation &loc, bool hadWarnings)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor21addImportWithLocationERK7QStringRK'
        'N6QQmlJS14SourceLocationEb',
        name, self._valueOf(loc), hadWarnings,
    )

  @overload(QQmlSA.ScopeType, str, WAIT['QQmlJS.SourceLocation'])
  def populateCurrentScope(
      self,
      type: QQmlSA.ScopeType,
      name: str,
      location: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::populateCurrentScope(QQmlJSScope::ScopeType type,
    const QString &name, const QQmlJS::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#populateCurrentScope

    Parameters
    ----------

    type : QQmlSA.ScopeType
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSImportVisitor::populateCurrentScope(QQmlJSScope::ScopeType
    #      type, const QString &name, const QQmlJS::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor20populateCurrentScopeEN6QQmlSA9Scop'
        'eTypeERK7QStringRKN6QQmlJS14SourceLocationE',
        type.value, name, self._valueOf(location),
    )

  @overload(QQmlSA.ScopeType, str, WAIT['QQmlJS.SourceLocation'])
  def enterRootScope(
      self,
      type: QQmlSA.ScopeType,
      name: str,
      location: QQmlJS.SourceLocation,
  ) -> None:
    """
    Calls Qt's 'void
    QQmlJSImportVisitor::enterRootScope(QQmlJSScope::ScopeType type, const
    QString &name, const QQmlJS::SourceLocation &location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsimportvisitor.html#enterRootScope

    Parameters
    ----------

    type : QQmlSA.ScopeType
      Passed on as its number.

    name : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  void QQmlJSImportVisitor::enterRootScope(QQmlJSScope::ScopeType type,
    #      const QString &name, const QQmlJS::SourceLocation &location)
    self.uglySide.call(
        'ritual_ZN19QQmlJSImportVisitor14enterRootScopeEN6QQmlSA9ScopeTypeE'
        'RK7QStringRKN6QQmlJS14SourceLocationE',
        type.value, name, self._valueOf(location),
    )

  @staticmethod
  def addFunctionOrExpression(*__, **_) -> Never:
    """
    Qt's 'QQmlJSMetaMethod::RelativeFunctionIndex
    QQmlJSImportVisitor::addFunctionOrExpression(const QQmlJSScope::ConstPtr
    &scope, const QString &name)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.addFunctionOrExpression' has no cute function "
        "yet. Qt's 'QQmlJSMetaMethod::RelativeFunctionIndex "
        "QQmlJSImportVisitor::addFunctionOrExpression(const "
        "QQmlJSScope::ConstPtr &scope, const QString &name)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def breakInheritanceCycles(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::breakInheritanceCycles(const
    QQmlJSScope::Ptr &scope)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.breakInheritanceCycles' has no cute function "
        "yet. Qt's 'void QQmlJSImportVisitor::breakInheritanceCycles(const "
        "QQmlJSScope::Ptr &scope)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def checkCustomParser(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSImportVisitor::checkCustomParser(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.checkCustomParser' has no cute function yet. "
        "Qt's 'bool QQmlJSImportVisitor::checkCustomParser(const "
        "QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def checkDeprecation(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::checkDeprecation(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.checkDeprecation' has no cute function yet. "
        "Qt's 'void QQmlJSImportVisitor::checkDeprecation(const "
        "QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def checkForComponentTypeWithProperties(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::checkForComponentTypeWithProperties(const
    QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.checkForComponentTypeWithProperties' has no "
        "cute function yet. Qt's 'void "
        "QQmlJSImportVisitor::checkForComponentTypeWithProperties(const "
        "QQmlJSScope::ConstPtr &scope)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def checkGroupedAndAttachedScopes(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlJSImportVisitor::checkGroupedAndAttachedScopes(QQmlJSScope::ConstPtr
    scope)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.checkGroupedAndAttachedScopes' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSImportVisitor::checkGroupedAndAttachedScopes(QQmlJSScope::Con"
        "stPtr scope)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def checkSignal(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::checkSignal(const QQmlJSScope::ConstPtr
    &signalScope, const QQmlJS::SourceLocation &location, const QString
    &handlerName, const QStringList &handlerParameters)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.checkSignal' has no cute function yet. Qt's "
        "'void QQmlJSImportVisitor::checkSignal(const QQmlJSScope::ConstPtr "
        "&signalScope, const QQmlJS::SourceLocation &location, const "
        "QString &handlerName, const QStringList &handlerParameters)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def checkTypeResolved(*__, **_) -> Never:
    """
    - Qt's 'bool QQmlJSImportVisitor::checkTypeResolved(const
      QQmlJSScope::ConstPtr &type)': takes a type Python has no way to hand
      over yet.
    - Qt's 'QQmlJSImportVisitor::checkTypeResolved': a template: a pattern
      and no single function.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.checkTypeResolved' has no cute function yet. "
        "Qt's 'bool QQmlJSImportVisitor::checkTypeResolved(const "
        "QQmlJSScope::ConstPtr &type)': takes a type Python has no way to "
        "hand over yet. Qt's 'QQmlJSImportVisitor::checkTypeResolved': a "
        "template: a pattern and no single function.")

  @staticmethod
  def importFromHost(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImportVisitor::importFromHost(const QString &path, const QString
    &prefix, const QQmlJS::SourceLocation &location)': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.importFromHost' has no cute function yet. "
        "Qt's 'QList<QQmlJS::DiagnosticMessage> "
        "QQmlJSImportVisitor::importFromHost(const QString &path, const "
        "QString &prefix, const QQmlJS::SourceLocation &location)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def importFromQrc(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJS::DiagnosticMessage>
    QQmlJSImportVisitor::importFromQrc(const QString &path, const QString
    &prefix, const QQmlJS::SourceLocation &location)': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.importFromQrc' has no cute function yet. Qt's "
        "'QList<QQmlJS::DiagnosticMessage> "
        "QQmlJSImportVisitor::importFromQrc(const QString &path, const "
        "QString &prefix, const QQmlJS::SourceLocation &location)': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def knownUnresolvedTypes(*__, **_) -> Never:
    """
    Qt's 'QDuplicateTracker<QQmlJSScope::ConstPtr>
    *QQmlJSImportVisitor::knownUnresolvedTypes()': gives
    'QDuplicateTracker<QQmlJSScope::ConstPtr>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.knownUnresolvedTypes' has no cute function "
        "yet. Qt's 'QDuplicateTracker<QQmlJSScope::ConstPtr> "
        "*QQmlJSImportVisitor::knownUnresolvedTypes()': gives "
        "'QDuplicateTracker<QQmlJSScope::ConstPtr>', which has no cute "
        "class yet.")

  @staticmethod
  def parseBindingExpression(*__, **_) -> Never:
    """
    Qt's 'BindingExpressionParseResult
    QQmlJSImportVisitor::parseBindingExpression(const QString &name, const
    QQmlJS::AST::Statement *statement, const QQmlJS::AST::UiPublicMember
    *associatedPropertyDefinition)': gives the enum
    'QQmlJSImportVisitor::BindingExpressionParseResult', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.parseBindingExpression' has no cute function "
        "yet. Qt's 'BindingExpressionParseResult "
        "QQmlJSImportVisitor::parseBindingExpression(const QString &name, "
        "const QQmlJS::AST::Statement *statement, const "
        "QQmlJS::AST::UiPublicMember *associatedPropertyDefinition)': gives "
        "the enum 'QQmlJSImportVisitor::BindingExpressionParseResult', "
        "whose class cannot be named here.")

  @staticmethod
  def processImportWarnings(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::processImportWarnings(const QString
    &what, const QList<QQmlJS::DiagnosticMessage> &warnings, const
    QQmlJS::SourceLocation &srcLocation)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.processImportWarnings' has no cute function "
        "yet. Qt's 'void QQmlJSImportVisitor::processImportWarnings(const "
        "QString &what, const QList<QQmlJS::DiagnosticMessage> &warnings, "
        "const QQmlJS::SourceLocation &srcLocation)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def qmlTypes(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlJSScope::ConstPtr> QQmlJSImportVisitor::qmlTypes()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.qmlTypes' has no cute function yet. Qt's "
        "'QList<QQmlJSScope::ConstPtr> QQmlJSImportVisitor::qmlTypes() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def result(*__, **_) -> Never:
    """
    Qt's 'QQmlJSScope::Ptr QQmlJSImportVisitor::result() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.result' has no cute function yet. Qt's "
        "'QQmlJSScope::Ptr QQmlJSImportVisitor::result() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def safeInsertJSIdentifier(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSImportVisitor::safeInsertJSIdentifier(QQmlJSScope::Ptr
    &scope, const QString &name, const QQmlJSScope::JavaScriptIdentifier
    &identifier)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.safeInsertJSIdentifier' has no cute function "
        "yet. Qt's 'bool "
        "QQmlJSImportVisitor::safeInsertJSIdentifier(QQmlJSScope::Ptr "
        "&scope, const QString &name, const "
        "QQmlJSScope::JavaScriptIdentifier &identifier)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def scopesBylocation(*__, **_) -> Never:
    """
    Qt's 'QHash<QV4::CompiledData::Location, QQmlJSScope::ConstPtr>
    QQmlJSImportVisitor::scopesBylocation() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.scopesBylocation' has no cute function yet. "
        "Qt's 'QHash<QV4::CompiledData::Location, QQmlJSScope::ConstPtr> "
        "QQmlJSImportVisitor::scopesBylocation() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setScopeName(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::setScopeName(QQmlJSScope::Ptr &scope,
    QQmlJSScope::ScopeType type, const QString &name)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.setScopeName' has no cute function yet. Qt's "
        "'void QQmlJSImportVisitor::setScopeName(QQmlJSScope::Ptr &scope, "
        "QQmlJSScope::ScopeType type, const QString &name)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def signalHandlers(*__, **_) -> Never:
    """
    Qt's 'QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler>
    QQmlJSImportVisitor::signalHandlers() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.signalHandlers' has no cute function yet. "
        "Qt's 'QHash<QQmlJS::SourceLocation, QQmlJSMetaSignalHandler> "
        "QQmlJSImportVisitor::signalHandlers() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def synthesizeCompilationUnitRuntimeFunctionIndices(*__, **_) -> Never:
    """
    Qt's 'int
    QQmlJSImportVisitor::synthesizeCompilationUnitRuntimeFunctionIndices(
    const QQmlJSScope::Ptr &scope, int count) const': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.synthesizeCompilationUnitRuntimeFunctionIndice"
        "s' has no cute function yet. Qt's 'int "
        "QQmlJSImportVisitor::synthesizeCompilationUnitRuntimeFunctionIndice"
        "s(const QQmlJSScope::Ptr &scope, int count) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def warnMissingPropertyForBinding(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::warnMissingPropertyForBinding(const
    QString &property, const QQmlJS::SourceLocation &location, const
    std::optional<QQmlJSFixSuggestion> &fixSuggestion)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.warnMissingPropertyForBinding' has no cute "
        "function yet. Qt's 'void "
        "QQmlJSImportVisitor::warnMissingPropertyForBinding(const QString "
        "&property, const QQmlJS::SourceLocation &location, const "
        "std::optional<QQmlJSFixSuggestion> &fixSuggestion)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def warnUnresolvedType(*__, **_) -> Never:
    """
    Qt's 'void QQmlJSImportVisitor::warnUnresolvedType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSImportVisitor.warnUnresolvedType' has no cute function yet. "
        "Qt's 'void QQmlJSImportVisitor::warnUnresolvedType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")
