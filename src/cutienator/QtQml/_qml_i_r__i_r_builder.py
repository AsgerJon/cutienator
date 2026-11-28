"""
QmlIR::IRBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::IRBuilder to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQmlJS, QV4, QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTypeRevision

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class IRBuilder(QQmlJS.AST.Visitor):
  """
  The cute side of Qt's QmlIR::IRBuilder: a plain Python object standing in
  front of one C++ QmlIR::IRBuilder.

  It is built on the cute 'QQmlJS::AST::Visitor', as Qt's QmlIR::IRBuilder is
  built on Qt's QQmlJS::AST::Visitor, and has everything that class has.

  C++ hands a QmlIR::IRBuilder around as a copy, so every C++
  QmlIR::IRBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QmlIR::IRBuilder that has a ritual and that Python
  can call so far, 16 names in all: 'tr', 'generateFromQml', 'visit',
  'throwRecursionDepthError', 'asString', 'extractVersion', 'textRefAt',
  'tryGeneratingTranslationBinding', 'appendBinding', 'appendAlias',
  'registerFunctionExpr', 'bindingsTarget', 'recordError', 'registerString',
  'stringAt', 'sanityCheckFunctionNames'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QmlIR::IRBuilder::accept(QQmlJS::AST::Node *node)': names
    'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex,
    QQmlJS::AST::UiQualifiedId *qualifiedTypeNameId, const
    QV4::CompiledData::Location &location, QQmlJS::AST::UiObjectInitializer
    *initializer, Object *declarationsOverride)': takes a number to change
    where it is.
  - Qt's 'bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex,
    QQmlJS::AST::UiObjectDefinition *node, Object *declarationsOverride)':
    takes a number to change where it is.
  - Qt's 'QStringView QmlIR::IRBuilder::asStringRef(QQmlJS::AST::Node
    *node)': names 'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'void QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding
    *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
    *parentNode)': names 'QQmlJS::AST::Statement', which has no cute class
    yet.
  - Qt's 'void QmlIR::IRBuilder::appendBinding(QQmlJS::AST::UiQualifiedId
    *name, QQmlJS::AST::Statement *value, QQmlJS::AST::Node *parentNode)':
    names 'QQmlJS::AST::Statement', which has no cute class yet.
  - Qt's 'void QmlIR::IRBuilder::appendBinding(const QQmlJS::SourceLocation
    &qualifiedNameLocation, const QQmlJS::SourceLocation &nameLocation,
    quint32 propertyNameIndex, QQmlJS::AST::Statement *value,
    QQmlJS::AST::Node *parentNode)': names 'QQmlJS::AST::Statement', which
    has no cute class yet.
  - Qt's 'bool QmlIR::IRBuilder::setId(const QQmlJS::SourceLocation
    &idLocation, QQmlJS::AST::Statement *value)': names
    'QQmlJS::AST::Statement', which has no cute class yet.
  - Qt's 'bool
    QmlIR::IRBuilder::resolveQualifiedId(QQmlJS::AST::UiQualifiedId
    **nameToResolve, Object **object, bool onAssignment)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QmlIR::IRBuilder::isStatementNodeScript(QQmlJS::AST::Statement
    *statement)': names 'QQmlJS::AST::Statement', which has no cute class
    yet.
  - Qt's 'bool
    QmlIR::IRBuilder::isRedundantNullInitializerForPropertyDeclaration(
    Property *property, QQmlJS::AST::Statement *statement)': names
    'QQmlJS::AST::Statement', which has no cute class yet.
  - Qt's 'QmlIR::IRBuilder::~IRBuilder()': the destructor: Python removes its
    C++ QmlIR::IRBuilder by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 43 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QmlIR::IRBuilder is created at the first use, not by
    'QmlIR::IRBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::IRBuilder back gives a copy the ritual made
    for Python, in a new cute QmlIR::IRBuilder.
  - Each name of Qt's QmlIR::IRBuilder that has no cute function yet, 'New',
    'accept', 'asStringRef', 'defineQMLObject',
    'isRedundantNullInitializerForPropertyDeclaration',
    'isStatementNodeScript', 'resolveQualifiedId', 'setBindingValue',
    'setId', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QmlIR::IRBuilder, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class IsQmlFunction(CuteNum, scoped=True):
    """
    The enum 'QmlIR::IRBuilder::IsQmlFunction' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Yes = Kee[int](0)
    No = Kee[int](1)

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
    Calls Qt's 'QString QmlIR::IRBuilder::tr(const char *sourceText, const
    char *disambiguation, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#tr

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
    #  QString QmlIR::IRBuilder::tr(const char *sourceText, const char
    #      *disambiguation, int n)
    return Rituals.call(
        'ritual_ZN5QmlIR9IRBuilder2trEPKcS2_i',
        CuteMixin._bytesOf(sourceText), CuteMixin._bytesOf(disambiguation),
        n,
    )

  @staticmethod
  @overload(WAIT['QQmlJS.AST.UiQualifiedId'])
  @overload(NoneType)
  def asString(node: Optional[QQmlJS.AST.UiQualifiedId]) -> str:
    """
    Calls Qt's 'QString QmlIR::IRBuilder::asString(QQmlJS::AST::UiQualifiedId
    *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#asString

    Parameters
    ----------

    node : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::IRBuilder::asString(QQmlJS::AST::UiQualifiedId *node)
    return Rituals.call(
        'ritual_ZN5QmlIR9IRBuilder8asStringEPN6QQmlJS3AST13UiQualifiedIdE',
        CuteMixin._addressOf(node),
    )

  @staticmethod
  @overload(str)
  def extractVersion(string: str) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QmlIR::IRBuilder::extractVersion(QStringView
    string)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#extractVersion

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QmlIR::IRBuilder::extractVersion(QStringView string)
    address = Rituals.call(
        'ritual_ZN5QmlIR9IRBuilder14extractVersionE11QStringView', string,
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::IRBuilder'

  #  A C++ QmlIR::IRBuilder Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlIR_IRBuilder'

  #  The functions Qt calls itself that QmlIR::IRBuilder is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setBindingValue': (
          'void '
          'QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding *, '
          'QQmlJS::AST::Statement *, QQmlJS::AST::Node *)',
      ),
  }

  #  The functions Qt calls itself that QmlIR::IRBuilder is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'registerFunctionExpr': (
          ('_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AST18Functi'
           'onExpressionENS0_13IsQmlFunctionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QQmlJS.AST.FunctionExpression'),
               ('int', 'enum', 'QtQml:QmlIR.IRBuilder.IsQmlFunction'),
           )),
      ),
  }

  #  Qt's '~QmlIR::IRBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QmlIR::IRBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR9IRBuilderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QQmlJS.SourceLocation'])
  def textRefAt(self, loc: QQmlJS.SourceLocation) -> str:
    """
    Calls Qt's 'QStringView QmlIR::IRBuilder::textRefAt(const
    QQmlJS::SourceLocation &loc) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#textRefAt

    Parameters
    ----------

    loc : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QmlIR::IRBuilder::textRefAt(const QQmlJS::SourceLocation
    #      &loc) const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR9IRBuilder9textRefAtERKN6QQmlJS14SourceLocationE',
        self._valueOf(loc),
    )

  @overload(WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.SourceLocation'])
  def textRefAt(
      self,
      first: QQmlJS.SourceLocation,
      last: QQmlJS.SourceLocation,
  ) -> str:
    """
    Calls Qt's 'QStringView QmlIR::IRBuilder::textRefAt(const
    QQmlJS::SourceLocation &first, const QQmlJS::SourceLocation &last)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#textRefAt

    Parameters
    ----------

    first : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    last : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QmlIR::IRBuilder::textRefAt(const QQmlJS::SourceLocation
    #      &first, const QQmlJS::SourceLocation &last) const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR9IRBuilder9textRefAtERKN6QQmlJS14SourceLocationES4'
        '_',
        self._valueOf(first), self._valueOf(last),
    )

  def bindingsTarget(self) -> Optional[QmlIR.Object]:
    """
    Calls Qt's 'Object *QmlIR::IRBuilder::bindingsTarget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#bindingsTarget

    Returns
    -------

    Optional[QmlIR.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QmlIR::IRBuilder::bindingsTarget() const
    address = self.uglySide.call(
        'ritual_ZNK5QmlIR9IRBuilder14bindingsTargetEv',
    )
    return QmlIR.Object._cuteAt(address)

  @overload(str)
  def registerString(self, str: str) -> int:
    """
    Calls Qt's 'quint32 QmlIR::IRBuilder::registerString(const QString &str)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#registerString

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  quint32 QmlIR::IRBuilder::registerString(const QString &str) const
    return self.uglySide.call(
        'ritual_ZNK5QmlIR9IRBuilder14registerStringERK7QString', str,
    )

  @overload(int)
  def stringAt(self, index: int) -> str:
    """
    Calls Qt's 'QString QmlIR::IRBuilder::stringAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#stringAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::IRBuilder::stringAt(int index) const
    return self.uglySide.call('ritual_ZNK5QmlIR9IRBuilder8stringAtEi', index)

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
    Notes what was given, for Qt's 'QmlIR::IRBuilder::IRBuilder()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#IRBuilder
    """
    #  QmlIR::IRBuilder::IRBuilder()
    self._noteCreation(IRBuilder, lambda: Rituals.call(
        'ritual_ZN5QmlIR9IRBuilderC1Ev',
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

  @overload(str, str, WAIT['QmlIR.Document'])
  @overload(str, str, NoneType)
  def generateFromQml(
      self,
      code: str,
      url: str,
      output: Optional[QmlIR.Document],
  ) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::generateFromQml(const QString &code,
    const QString &url, Document *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#generateFromQml

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.

    url : str
      Passed on as it is: a QString is made of it for the call.

    output : Optional[QmlIR.Document]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::generateFromQml(const QString &code, const
    #      QString &url, Document *output)
    return self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder15generateFromQmlERK7QStringS3_PNS_8Docum'
        'entE',
        code, url, self._addressOf(output),
    )

  @overload(WAIT['QQmlJS.AST.UiImport'])
  @overload(NoneType)
  def visit(self, ast: Optional[QQmlJS.AST.UiImport]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiImport *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiImport *ast)
    ritual = 'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST8UiImportE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST8UiImportE'
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiPragma'])
  def visit(self, ast: Optional[QQmlJS.AST.UiPragma]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPragma *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiPragma]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPragma *ast)
    ritual = 'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST8UiPragmaE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST8UiPragmaE'
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiProgram'])
  def visit(self, a0: Optional[QQmlJS.AST.UiProgram]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiProgram *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    a0 : Optional[QQmlJS.AST.UiProgram]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiProgram *a0)
    ritual = 'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST9UiProgramE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST9UiProgramE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['QQmlJS.AST.UiArrayBinding'])
  def visit(self, ast: Optional[QQmlJS.AST.UiArrayBinding]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiArrayBinding
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiArrayBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiArrayBinding *ast)
    ritual = 'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST14UiArrayBindingE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST14UiArrayBindin'
          'gE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiObjectBinding'])
  def visit(self, ast: Optional[QQmlJS.AST.UiObjectBinding]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectBinding
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiObjectBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectBinding *ast)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiObjectBindingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiObjectBindi'
          'ngE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiObjectDefinition'])
  def visit(self, ast: Optional[QQmlJS.AST.UiObjectDefinition]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectDefinition
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiObjectDefinition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectDefinition *ast)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST18UiObjectDefinitionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST18UiObjectDefin'
          'itionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiInlineComponent'])
  def visit(self, ast: Optional[QQmlJS.AST.UiInlineComponent]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiInlineComponent
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiInlineComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiInlineComponent *ast)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST17UiInlineComponentE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST17UiInlineCompo'
          'nentE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiEnumDeclaration'])
  def visit(self, ast: Optional[QQmlJS.AST.UiEnumDeclaration]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiEnumDeclaration
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiEnumDeclaration]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiEnumDeclaration *ast)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST17UiEnumDeclarationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST17UiEnumDeclara'
          'tionE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiPublicMember'])
  def visit(self, ast: Optional[QQmlJS.AST.UiPublicMember]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPublicMember
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPublicMember *ast)
    ritual = 'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST14UiPublicMemberE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST14UiPublicMembe'
          'rE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiScriptBinding'])
  def visit(self, ast: Optional[QQmlJS.AST.UiScriptBinding]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiScriptBinding
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiScriptBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiScriptBinding *ast)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiScriptBindingE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiScriptBindi'
          'ngE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiSourceElement'])
  def visit(self, ast: Optional[QQmlJS.AST.UiSourceElement]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiSourceElement
    *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiSourceElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiSourceElement *ast)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiSourceElementE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiSourceEleme'
          'ntE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  @overload(WAIT['QQmlJS.AST.UiRequired'])
  def visit(self, ast: Optional[QQmlJS.AST.UiRequired]) -> bool:
    """
    Calls Qt's 'bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiRequired *ast)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#visit

    Parameters
    ----------

    ast : Optional[QQmlJS.AST.UiRequired]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiRequired *ast)
    ritual = 'ritual_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST10UiRequiredE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST10UiRequiredE')
    return self.uglySide.call(ritual, self._addressOf(ast))

  def throwRecursionDepthError(self) -> None:
    """
    Calls Qt's 'void QmlIR::IRBuilder::throwRecursionDepthError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#throwRecursionDepthError
    """
    #  void QmlIR::IRBuilder::throwRecursionDepthError()
    ritual = 'ritual_ZN5QmlIR9IRBuilder24throwRecursionDepthErrorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QmlIR9IRBuilder24throwRecursionDepthErrorEv'
    self.uglySide.call(ritual)

  @overload(
      str, WAIT['QQmlJS.AST.ArgumentList'], WAIT['QV4.CompiledData.Binding'],
  )
  @overload(str, WAIT['QQmlJS.AST.ArgumentList'], NoneType)
  @overload(str, NoneType, WAIT['QV4.CompiledData.Binding'])
  @overload(str, NoneType, NoneType)
  def tryGeneratingTranslationBinding(
      self,
      base: str,
      args: Optional[QQmlJS.AST.ArgumentList],
      binding: Optional[QV4.CompiledData.Binding],
  ) -> None:
    """
    Calls Qt's 'void
    QmlIR::IRBuilder::tryGeneratingTranslationBinding(QStringView base,
    QQmlJS::AST::ArgumentList *args, QV4::CompiledData::Binding *binding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html

    Parameters
    ----------

    base : str
      Passed on as it is: a QString is made of it for the call.

    args : Optional[QQmlJS.AST.ArgumentList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QmlIR::IRBuilder::tryGeneratingTranslationBinding(QStringView
    #      base, QQmlJS::AST::ArgumentList *args, QV4::CompiledData::Binding
    #      *binding)
    self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder31tryGeneratingTranslationBindingE11QStri'
        'ngViewPN6QQmlJS3AST12ArgumentListEPN3QV412CompiledData7BindingE',
        base, self._addressOf(args), self._addressOf(binding),
    )

  @overload(WAIT['QQmlJS.AST.UiQualifiedId'], int)
  @overload(NoneType, int)
  @overload(WAIT['QQmlJS.AST.UiQualifiedId'], int, bool)
  @overload(NoneType, int, bool)
  def appendBinding(
      self,
      name: Optional[QQmlJS.AST.UiQualifiedId],
      objectIndex: int,
      isOnAssignment: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QmlIR::IRBuilder::appendBinding(QQmlJS::AST::UiQualifiedId *name, int
    objectIndex, bool isOnAssignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#appendBinding

    Parameters
    ----------

    name : Optional[QQmlJS.AST.UiQualifiedId]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectIndex : int
      Passed on as it is.

    isOnAssignment : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QmlIR::IRBuilder::appendBinding(QQmlJS::AST::UiQualifiedId *name,
    #      int objectIndex, bool isOnAssignment)
    self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder13appendBindingEPN6QQmlJS3AST13UiQualifie'
        'dIdEib',
        self._addressOf(name), objectIndex, isOnAssignment,
    )

  @overload(
      WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.SourceLocation'], int, int,
  )
  @overload(
      WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.SourceLocation'], int, int,
      bool,
  )
  @overload(
      WAIT['QQmlJS.SourceLocation'], WAIT['QQmlJS.SourceLocation'], int, int,
      bool, bool,
  )
  def appendBinding(
      self,
      qualifiedNameLocation: QQmlJS.SourceLocation,
      nameLocation: QQmlJS.SourceLocation,
      propertyNameIndex: int,
      objectIndex: int,
      isListItem: bool = False,
      isOnAssignment: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QmlIR::IRBuilder::appendBinding(const
    QQmlJS::SourceLocation &qualifiedNameLocation, const
    QQmlJS::SourceLocation &nameLocation, quint32 propertyNameIndex, int
    objectIndex, bool isListItem, bool isOnAssignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#appendBinding

    Parameters
    ----------

    qualifiedNameLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    nameLocation : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    propertyNameIndex : int
      Passed on as it is.

    objectIndex : int
      Passed on as it is.

    isListItem : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    isOnAssignment : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QmlIR::IRBuilder::appendBinding(const QQmlJS::SourceLocation
    #      &qualifiedNameLocation, const QQmlJS::SourceLocation
    #      &nameLocation, quint32 propertyNameIndex, int objectIndex, bool
    #      isListItem, bool isOnAssignment)
    self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder13appendBindingERKN6QQmlJS14SourceLocatio'
        'nES4_jibb',
        self._valueOf(qualifiedNameLocation), self._valueOf(nameLocation),
        propertyNameIndex, objectIndex, isListItem, isOnAssignment,
    )

  @overload(WAIT['QQmlJS.AST.UiPublicMember'])
  @overload(NoneType)
  def appendAlias(self, node: Optional[QQmlJS.AST.UiPublicMember]) -> bool:
    """
    Calls Qt's 'bool
    QmlIR::IRBuilder::appendAlias(QQmlJS::AST::UiPublicMember *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#appendAlias

    Parameters
    ----------

    node : Optional[QQmlJS.AST.UiPublicMember]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QmlIR::IRBuilder::appendAlias(QQmlJS::AST::UiPublicMember *node)
    return self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder11appendAliasEPN6QQmlJS3AST14UiPublicMemb'
        'erE',
        self._addressOf(node),
    )

  @overload(WAIT['QQmlJS.AST.FunctionExpression'], IsQmlFunction)
  @overload(NoneType, IsQmlFunction)
  def registerFunctionExpr(
      self,
      fexp: Optional[QQmlJS.AST.FunctionExpression],
      a1: IsQmlFunction,
  ) -> None:
    """
    Calls Qt's 'void
    QmlIR::IRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpression
    *fexp, IsQmlFunction a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#registerFunctionExpr

    Parameters
    ----------

    fexp : Optional[QQmlJS.AST.FunctionExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : IsQmlFunction
      Passed on as its number.
    """
    #  void QmlIR::IRBuilder::registerFunctionExpr(QQmlJS::AST::
    #      FunctionExpression *fexp, IsQmlFunction a1)
    ritual = (
        'ritual_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AST18Fun'
        'ctionExpressionENS0_13IsQmlFunctionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AS'
          'T18FunctionExpressionENS0_13IsQmlFunctionE')
    self.uglySide.call(ritual, self._addressOf(fexp), a1.value)

  @overload(WAIT['QQmlJS.SourceLocation'], str)
  def recordError(
      self,
      location: QQmlJS.SourceLocation,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QmlIR::IRBuilder::recordError(const
    QQmlJS::SourceLocation &location, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-irbuilder.html#recordError

    Parameters
    ----------

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QmlIR::IRBuilder::recordError(const QQmlJS::SourceLocation
    #      &location, const QString &description)
    self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder11recordErrorERKN6QQmlJS14SourceLocationE'
        'RK7QString',
        self._valueOf(location), description,
    )

  @overload(WAIT['QmlIR.Object'], WAIT['QQmlJS.SourceLocation'])
  @overload(WAIT['QmlIR.Object'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.SourceLocation'])
  @overload(NoneType, NoneType)
  def sanityCheckFunctionNames(
      self,
      obj: Optional[QmlIR.Object],
      errorLocation: Optional[QQmlJS.SourceLocation],
  ) -> str:
    """
    Calls Qt's 'QString QmlIR::IRBuilder::sanityCheckFunctionNames(Object
    *obj, QQmlJS::SourceLocation *errorLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlir-irbuilder.html#sanityCheckFunctionNames

    Parameters
    ----------

    obj : Optional[QmlIR.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlIR::IRBuilder::sanityCheckFunctionNames(Object *obj,
    #      QQmlJS::SourceLocation *errorLocation)
    return self.uglySide.call(
        'ritual_ZN5QmlIR9IRBuilder24sanityCheckFunctionNamesEPNS_6ObjectEPN'
        '6QQmlJS14SourceLocationE',
        self._addressOf(obj), self._addressOf(errorLocation),
    )

  @staticmethod
  def New(*__, **_) -> Never:
    """
    Qt's 'QmlIR::IRBuilder::New': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.New' has no cute function yet. Qt's "
        "'QmlIR::IRBuilder::New': a template: a pattern and no single "
        "function.")

  @staticmethod
  def accept(*__, **_) -> Never:
    """
    Qt's 'void QmlIR::IRBuilder::accept(QQmlJS::AST::Node *node)': names
    'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.accept' has no cute function yet. Qt's 'void "
        "QmlIR::IRBuilder::accept(QQmlJS::AST::Node *node)': names "
        "'QQmlJS::AST::Node', which has no cute class yet.")

  @staticmethod
  def asStringRef(*__, **_) -> Never:
    """
    Qt's 'QStringView QmlIR::IRBuilder::asStringRef(QQmlJS::AST::Node
    *node)': names 'QQmlJS::AST::Node', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.asStringRef' has no cute function yet. Qt's "
        "'QStringView QmlIR::IRBuilder::asStringRef(QQmlJS::AST::Node "
        "*node)': names 'QQmlJS::AST::Node', which has no cute class yet.")

  @staticmethod
  def defineQMLObject(*__, **_) -> Never:
    """
    - Qt's 'bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex,
      QQmlJS::AST::UiQualifiedId *qualifiedTypeNameId, const
      QV4::CompiledData::Location &location, QQmlJS::AST::UiObjectInitializer
      *initializer, Object *declarationsOverride)': takes a number to change
      where it is.
    - Qt's 'bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex,
      QQmlJS::AST::UiObjectDefinition *node, Object *declarationsOverride)':
      takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.defineQMLObject' has no cute function yet. Qt's "
        "'bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex, "
        "QQmlJS::AST::UiQualifiedId *qualifiedTypeNameId, const "
        "QV4::CompiledData::Location &location, "
        "QQmlJS::AST::UiObjectInitializer *initializer, Object "
        "*declarationsOverride)': takes a number to change where it is. "
        "Qt's 'bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex, "
        "QQmlJS::AST::UiObjectDefinition *node, Object "
        "*declarationsOverride)': takes a number to change where it is.")

  @staticmethod
  def isRedundantNullInitializerForPropertyDeclaration(*__, **_) -> Never:
    """
    Qt's 'bool
    QmlIR::IRBuilder::isRedundantNullInitializerForPropertyDeclaration(
    Property *property, QQmlJS::AST::Statement *statement)': names
    'QQmlJS::AST::Statement', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.isRedundantNullInitializerForPropertyDeclaration' "
        "has no cute function yet. Qt's 'bool "
        "QmlIR::IRBuilder::isRedundantNullInitializerForPropertyDeclaration("
        "Property *property, QQmlJS::AST::Statement *statement)': names "
        "'QQmlJS::AST::Statement', which has no cute class yet.")

  @staticmethod
  def isStatementNodeScript(*__, **_) -> Never:
    """
    Qt's 'bool QmlIR::IRBuilder::isStatementNodeScript(QQmlJS::AST::Statement
    *statement)': names 'QQmlJS::AST::Statement', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.isStatementNodeScript' has no cute function yet. "
        "Qt's 'bool "
        "QmlIR::IRBuilder::isStatementNodeScript(QQmlJS::AST::Statement "
        "*statement)': names 'QQmlJS::AST::Statement', which has no cute "
        "class yet.")

  @staticmethod
  def resolveQualifiedId(*__, **_) -> Never:
    """
    Qt's 'bool
    QmlIR::IRBuilder::resolveQualifiedId(QQmlJS::AST::UiQualifiedId
    **nameToResolve, Object **object, bool onAssignment)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.resolveQualifiedId' has no cute function yet. "
        "Qt's 'bool "
        "QmlIR::IRBuilder::resolveQualifiedId(QQmlJS::AST::UiQualifiedId "
        "**nameToResolve, Object **object, bool onAssignment)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def setBindingValue(*__, **_) -> Never:
    """
    Qt's 'void QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding
    *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
    *parentNode)': names 'QQmlJS::AST::Statement', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.setBindingValue' has no cute function yet. Qt's "
        "'void QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding "
        "*binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node "
        "*parentNode)': names 'QQmlJS::AST::Statement', which has no cute "
        "class yet.")

  @staticmethod
  def setId(*__, **_) -> Never:
    """
    Qt's 'bool QmlIR::IRBuilder::setId(const QQmlJS::SourceLocation
    &idLocation, QQmlJS::AST::Statement *value)': names
    'QQmlJS::AST::Statement', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QmlIR.IRBuilder.setId' has no cute function yet. Qt's 'bool "
        "QmlIR::IRBuilder::setId(const QQmlJS::SourceLocation &idLocation, "
        "QQmlJS::AST::Statement *value)': names 'QQmlJS::AST::Statement', "
        "which has no cute class yet.")
