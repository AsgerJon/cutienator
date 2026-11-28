"""
QQmlJSAotCompiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJSAotCompiler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtQml import QQmlJS, QV4, QmlIR
from . import QQmlJSCompilePass

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSAotFunction, QQmlJSImporter, QQmlJSLogger
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSImporter = WAIT['QQmlJSImporter']
  QQmlJSLogger = WAIT['QQmlJSLogger']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSAotCompiler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSAotCompiler: a plain Python object standing in
  front of one C++ QQmlJSAotCompiler.

  What exists
  -----------

  Every function of Qt's QQmlJSAotCompiler that has a ritual and that Python
  can call so far, 7 names in all: 'setDocument', 'setScope', 'globalCode',
  'isLintCompiler', 'noAotValidation', 'doCompile',
  'doCompileAndRecordAotStats'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJSAotCompiler::~QQmlJSAotCompiler()': the destructor: Python
    never removes a C++ QQmlJSAotCompiler.
  - Qt's 'std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>
    QQmlJSAotCompiler::compileBinding(const QV4::Compiler::Context *context,
    const QmlIR::Binding &irBinding, QQmlJS::AST::Node *astNode)': gives a
    type Python has no way to take yet.
  - Qt's 'std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>
    QQmlJSAotCompiler::compileFunction(const QV4::Compiler::Context *context,
    const QString &name, QQmlJS::AST::Node *astNode)': gives a type Python
    has no way to take yet.
  - Qt's 'LookupSignatures QQmlJSAotCompiler::lookupSignatures() const':
    gives a type Python has no way to take yet.
  - Qt's 'std::optional<QList<QQmlJS::DiagnosticMessage>>
    QQmlJSAotCompiler::finalizeBindingOrFunction()': gives a type Python has
    no way to take yet.
  - Qt's 'QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const QString
    &message, QtMsgType type, const QQmlJS::SourceLocation &location) const':
    names the enum 'QtMsgType', whose class cannot be named here.

  What to expect
  --------------

  - The C++ QQmlJSAotCompiler is created at the first use, not by
    'QQmlJSAotCompiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJSAotCompiler.
  - Each name of Qt's QQmlJSAotCompiler that has no cute function yet,
    'compileBinding', 'compileFunction', 'diagnose',
    'finalizeBindingOrFunction', 'lookupSignatures', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJSAotCompiler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QQmlJSAotCompiler::Flag' of Qt, with the 4 names Qt gives
    in it. Qt names the type of its combinations 'QQmlJSAotCompiler::Flags'.
    """

    NoFlags = 0x0
    ValidateBasicBlocks = 0x1
    IsLintCompiler = 0x2
    NoAOTValidation = 0x4

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJSAotCompiler'

  #  A C++ QQmlJSAotCompiler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJSAotCompiler'

  #  The functions Qt calls itself that QQmlJSAotCompiler is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'compileBinding': (
          'std::variant<QQmlJSAotFunction, '
          'QList<QQmlJS::DiagnosticMessage>> '
          'QQmlJSAotCompiler::compileBinding(const QV4::Compiler::Context '
          '*, const QmlIR::Binding &, QQmlJS::AST::Node *)',
      ),
      'compileFunction': (
          'std::variant<QQmlJSAotFunction, '
          'QList<QQmlJS::DiagnosticMessage>> '
          'QQmlJSAotCompiler::compileFunction(const QV4::Compiler::Context '
          '*, const QString &, QQmlJS::AST::Node *)',
      ),
      'diagnose': (
          'QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const '
          'QString &, QtMsgType, const QQmlJS::SourceLocation &) const',
      ),
  }

  #  The functions Qt calls itself that QQmlJSAotCompiler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setDocument': (
          ('_ZN17QQmlJSAotCompiler11setDocumentEPKN5QmlIR9JSCodeGenEPKNS0_8'
           'DocumentE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QmlIR.JSCodeGen'),
               ('address', 'address', 'QtQml:QmlIR.Document'),
           )),
      ),
      'setScope': (
          ('_ZN17QQmlJSAotCompiler8setScopeEPKN5QmlIR6ObjectES3_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QmlIR.Object'),
               ('address', 'address', 'QtQml:QmlIR.Object'),
           )),
      ),
      'globalCode': (
          ('_ZNK17QQmlJSAotCompiler10globalCodeEv',
           ('address', 'value', 'QtQmlCompiler:QQmlJSAotFunction'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def globalCode(self) -> QQmlJSAotFunction:
    """
    Calls Qt's 'QQmlJSAotFunction QQmlJSAotCompiler::globalCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotcompiler.html#globalCode

    Returns
    -------

    QQmlJSAotFunction
      A new cute QQmlJSAotFunction around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSAotFunction QQmlJSAotCompiler::globalCode() const
    ritual = 'ritual_ZNK17QQmlJSAotCompiler10globalCodeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQmlJSAotCompiler10globalCodeEv'
    address = self.uglySide.call(ritual)
    from . import QQmlJSAotFunction
    return QQmlJSAotFunction._cuteOwning(address)

  def isLintCompiler(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSAotCompiler::isLintCompiler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsaotcompiler.html#isLintCompiler
    """
    #  bool QQmlJSAotCompiler::isLintCompiler() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlJSAotCompiler14isLintCompilerEv',
    )

  def noAotValidation(self) -> bool:
    """
    Calls Qt's 'bool QQmlJSAotCompiler::noAotValidation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsaotcompiler.html#noAotValidation
    """
    #  bool QQmlJSAotCompiler::noAotValidation() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlJSAotCompiler15noAotValidationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QmlIR.JSCodeGen'], WAIT['QmlIR.Document'])
  @overload(WAIT['QmlIR.JSCodeGen'], NoneType)
  @overload(NoneType, WAIT['QmlIR.Document'])
  @overload(NoneType, NoneType)
  def setDocument(
      self,
      codegen: Optional[QmlIR.JSCodeGen],
      document: Optional[QmlIR.Document],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSAotCompiler::setDocument(const QmlIR::JSCodeGen
    *codegen, const QmlIR::Document *document)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotcompiler.html#setDocument

    Parameters
    ----------

    codegen : Optional[QmlIR.JSCodeGen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    document : Optional[QmlIR.Document]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSAotCompiler::setDocument(const QmlIR::JSCodeGen *codegen,
    #      const QmlIR::Document *document)
    ritual = (
        'ritual_ZN17QQmlJSAotCompiler11setDocumentEPKN5QmlIR9JSCodeGenEPKNS'
        '0_8DocumentE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSAotCompiler11setDocumentEPKN5QmlIR9JSCodeGe'
          'nEPKNS0_8DocumentE')
    self.uglySide.call(
        ritual, self._addressOf(codegen), self._addressOf(document),
    )

  @overload(WAIT['QmlIR.Object'], WAIT['QmlIR.Object'])
  @overload(WAIT['QmlIR.Object'], NoneType)
  @overload(NoneType, WAIT['QmlIR.Object'])
  @overload(NoneType, NoneType)
  def setScope(
      self,
      object: Optional[QmlIR.Object],
      scope: Optional[QmlIR.Object],
  ) -> None:
    """
    Calls Qt's 'void QQmlJSAotCompiler::setScope(const QmlIR::Object *object,
    const QmlIR::Object *scope)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotcompiler.html#setScope

    Parameters
    ----------

    object : Optional[QmlIR.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scope : Optional[QmlIR.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJSAotCompiler::setScope(const QmlIR::Object *object, const
    #      QmlIR::Object *scope)
    ritual = 'ritual_ZN17QQmlJSAotCompiler8setScopeEPKN5QmlIR6ObjectES3_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQmlJSAotCompiler8setScopeEPKN5QmlIR6ObjectES3_')
    self.uglySide.call(
        ritual, self._addressOf(object), self._addressOf(scope),
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

  @overload(QQmlJSImporter, str, QStringList, QQmlJSLogger)
  @overload(QQmlJSImporter, str, QStringList, NoneType)
  @overload(NoneType, str, QStringList, QQmlJSLogger)
  @overload(NoneType, str, QStringList, NoneType)
  def __init__(
      self,
      importer: Optional[QQmlJSImporter],
      resourcePath: str,
      qmldirFiles: QStringList,
      logger: Optional[QQmlJSLogger],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSAotCompiler::QQmlJSAotCompiler(QQmlJSImporter *importer, const
    QString &resourcePath, const QStringList &qmldirFiles, QQmlJSLogger
    *logger)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsaotcompiler.html#QQmlJSAotCompiler

    Parameters
    ----------

    importer : Optional[QQmlJSImporter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resourcePath : str
      Passed on as it is: a QString is made of it for the call.

    qmldirFiles : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    logger : Optional[QQmlJSLogger]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJSAotCompiler::QQmlJSAotCompiler(QQmlJSImporter *importer, const
    #      QString &resourcePath, const QStringList &qmldirFiles,
    #      QQmlJSLogger *logger)
    self._noteCreation(QQmlJSAotCompiler, lambda: Rituals.call(
        'ritual_ZN17QQmlJSAotCompilerC1EP14QQmlJSImporterRK7QStringRK5QList'
        'IS2_EP12QQmlJSLogger',
        self._addressOf(importer), resourcePath, self._valueOf(qmldirFiles),
        self._addressOf(logger),
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

  @overload(WAIT['QV4.Compiler.Context'], QQmlJSCompilePass.Function)
  @overload(WAIT['QV4.Compiler.Context'], NoneType)
  @overload(NoneType, QQmlJSCompilePass.Function)
  @overload(NoneType, NoneType)
  def doCompile(
      self,
      context: Optional[QV4.Compiler.Context],
      function: Optional[QQmlJSCompilePass.Function],
  ) -> QQmlJSAotFunction:
    """
    Calls Qt's 'QQmlJSAotFunction QQmlJSAotCompiler::doCompile(const
    QV4::Compiler::Context *context, const QQmlJSCompilePass::Function
    *function)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljsaotcompiler.html#doCompile

    Parameters
    ----------

    context : Optional[QV4.Compiler.Context]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QQmlJSCompilePass.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlJSAotFunction
      A new cute QQmlJSAotFunction around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSAotFunction QQmlJSAotCompiler::doCompile(const
    #      QV4::Compiler::Context *context, const QQmlJSCompilePass::Function
    #      *function)
    address = self.uglySide.call(
        'ritual_ZN17QQmlJSAotCompiler9doCompileEPKN3QV48Compiler7ContextEPK'
        'N17QQmlJSCompilePass8FunctionE',
        self._addressOf(context), self._addressOf(function),
    )
    from . import QQmlJSAotFunction
    return QQmlJSAotFunction._cuteOwning(address)

  @overload(
      WAIT['QV4.Compiler.Context'], QQmlJSCompilePass.Function, str,
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(
      WAIT['QV4.Compiler.Context'], NoneType, str,
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(
      NoneType, QQmlJSCompilePass.Function, str,
      WAIT['QQmlJS.SourceLocation'],
  )
  @overload(NoneType, NoneType, str, WAIT['QQmlJS.SourceLocation'])
  def doCompileAndRecordAotStats(
      self,
      context: Optional[QV4.Compiler.Context],
      function: Optional[QQmlJSCompilePass.Function],
      name: str,
      location: QQmlJS.SourceLocation,
  ) -> QQmlJSAotFunction:
    """
    Calls Qt's 'QQmlJSAotFunction
    QQmlJSAotCompiler::doCompileAndRecordAotStats(const
    QV4::Compiler::Context *context, const QQmlJSCompilePass::Function
    *function, const QString &name, QQmlJS::SourceLocation location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljsaotcompiler.html#doCompileAndRecordAotStats

    Parameters
    ----------

    context : Optional[QV4.Compiler.Context]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QQmlJSCompilePass.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.

    Returns
    -------

    QQmlJSAotFunction
      A new cute QQmlJSAotFunction around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlJSAotFunction QQmlJSAotCompiler::doCompileAndRecordAotStats(const
    #      QV4::Compiler::Context *context, const QQmlJSCompilePass::Function
    #      *function, const QString &name, QQmlJS::SourceLocation location)
    address = self.uglySide.call(
        'ritual_ZN17QQmlJSAotCompiler26doCompileAndRecordAotStatsEPKN3QV48C'
        'ompiler7ContextEPKN17QQmlJSCompilePass8FunctionERK7QStringN6QQmlJS'
        '14SourceLocationE',
        self._addressOf(context), self._addressOf(function), name,
        self._valueOf(location),
    )
    from . import QQmlJSAotFunction
    return QQmlJSAotFunction._cuteOwning(address)

  @staticmethod
  def compileBinding(*__, **_) -> Never:
    """
    Qt's 'std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>
    QQmlJSAotCompiler::compileBinding(const QV4::Compiler::Context *context,
    const QmlIR::Binding &irBinding, QQmlJS::AST::Node *astNode)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSAotCompiler.compileBinding' has no cute function yet. Qt's "
        "'std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>> "
        "QQmlJSAotCompiler::compileBinding(const QV4::Compiler::Context "
        "*context, const QmlIR::Binding &irBinding, QQmlJS::AST::Node "
        "*astNode)': gives a type Python has no way to take yet.")

  @staticmethod
  def compileFunction(*__, **_) -> Never:
    """
    Qt's 'std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>>
    QQmlJSAotCompiler::compileFunction(const QV4::Compiler::Context *context,
    const QString &name, QQmlJS::AST::Node *astNode)': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSAotCompiler.compileFunction' has no cute function yet. Qt's "
        "'std::variant<QQmlJSAotFunction, QList<QQmlJS::DiagnosticMessage>> "
        "QQmlJSAotCompiler::compileFunction(const QV4::Compiler::Context "
        "*context, const QString &name, QQmlJS::AST::Node *astNode)': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def diagnose(*__, **_) -> Never:
    """
    Qt's 'QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const QString
    &message, QtMsgType type, const QQmlJS::SourceLocation &location) const':
    names the enum 'QtMsgType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlJSAotCompiler.diagnose' has no cute function yet. Qt's "
        "'QQmlJS::DiagnosticMessage QQmlJSAotCompiler::diagnose(const "
        "QString &message, QtMsgType type, const QQmlJS::SourceLocation "
        "&location) const': names the enum 'QtMsgType', whose class cannot "
        "be named here.")

  @staticmethod
  def finalizeBindingOrFunction(*__, **_) -> Never:
    """
    Qt's 'std::optional<QList<QQmlJS::DiagnosticMessage>>
    QQmlJSAotCompiler::finalizeBindingOrFunction()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSAotCompiler.finalizeBindingOrFunction' has no cute function "
        "yet. Qt's 'std::optional<QList<QQmlJS::DiagnosticMessage>> "
        "QQmlJSAotCompiler::finalizeBindingOrFunction()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def lookupSignatures(*__, **_) -> Never:
    """
    Qt's 'LookupSignatures QQmlJSAotCompiler::lookupSignatures() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSAotCompiler.lookupSignatures' has no cute function yet. "
        "Qt's 'LookupSignatures QQmlJSAotCompiler::lookupSignatures() "
        "const': gives a type Python has no way to take yet.")
