//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#include <QtCore/QString>
#include <QtCore/QDateTime>

//  Only a class built on QV4::Compiler::Codegen may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQV4_Compiler_Codegen : QV4::Compiler::Codegen {
  using QV4::Compiler::Codegen::visit;
  using QV4::Compiler::Codegen::endVisit;
  using QV4::Compiler::Codegen::throwSyntaxError;
  using QV4::Compiler::Codegen::throwReferenceError;
  using QV4::Compiler::Codegen::throwRecursionDepthError;
};

//  QV4::Compiler::Codegen::Codegen(QV4::Compiler::JSUnitGenerator
//      *jsUnitGenerator, bool strict, CodegenWarningInterface *iface, bool
//      storeSourceLocations)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen *ritual_ZN3QV48Compiler7CodegenC1EPNS0_15JSUnitGeneratorEbPNS0_23CodegenWarningInterfaceEb(
    QV4::Compiler::JSUnitGenerator *jsUnitGenerator,
    bool strict,
    QV4::Compiler::CodegenWarningInterface *iface,
    bool storeSourceLocations) {
  return new QV4::Compiler::Codegen(
      jsUnitGenerator,
      strict,
      iface,
      storeSourceLocations);
}

//  bool QV4::Compiler::Codegen::isNameGlobal(QAnyStringView name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen12isNameGlobalE14QAnyStringView(
    const QString *name) {
  return QV4::Compiler::Codegen::isNameGlobal(QAnyStringView(*name));
}

//  void QV4::Compiler::Codegen::forEachGlobalName(qxp::function_ref<void
//      (QLatin1StringView)> &&handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen17forEachGlobalNameEON3qxp12function_refIJFv13QLatin1StringEEEE(
    qxp::function_ref<void (QLatin1StringView)> *handler) {
  QV4::Compiler::Codegen::forEachGlobalName(std::move(*handler));
}

//  void QV4::Compiler::Codegen::generateFromProgram(const QString
//      &sourceCode, QQmlJS::AST::Program *ast, Module *module, ContextType
//      contextType)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen19generateFromProgramERK7QStringPN6QQmlJS3AST7ProgramEPNS0_6ModuleENS0_11ContextTypeE(
    QV4::Compiler::Codegen *self,
    const QString *sourceCode,
    QQmlJS::AST::Program *ast,
    QV4::Compiler::Module *module,
    QV4::Compiler::ContextType contextType) {
  self->generateFromProgram(*sourceCode, ast, module, contextType);
}

//  void QV4::Compiler::Codegen::generateFromModule(const QString
//      &sourceCode, QQmlJS::AST::ESModule *ast, Module *module)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen18generateFromModuleERK7QStringPN6QQmlJS3AST8ESModuleEPNS0_6ModuleE(
    QV4::Compiler::Codegen *self,
    const QString *sourceCode,
    QQmlJS::AST::ESModule *ast,
    QV4::Compiler::Module *module) {
  self->generateFromModule(*sourceCode, ast, module);
}

//  void QV4::Compiler::Codegen::generateFromModule(const Value &value,
//      Module *module)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen18generateFromModuleERKNS_5ValueEPNS0_6ModuleE(
    QV4::Compiler::Codegen *self,
    const QV4::Value *value,
    QV4::Compiler::Module *module) {
  self->generateFromModule(*value, module);
}

//  void QV4::Compiler::Codegen::enterContext(QQmlJS::AST::Node *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen12enterContextEPN6QQmlJS3AST4NodeE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Node *node) {
  self->enterContext(node);
}

//  int QV4::Compiler::Codegen::leaveContext()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen12leaveContextEv(
    QV4::Compiler::Codegen *self) {
  return self->leaveContext();
}

//  Context *QV4::Compiler::Codegen::enterBlock(QQmlJS::AST::Node *node)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context *ritual_ZN3QV48Compiler7Codegen10enterBlockEPN6QQmlJS3AST4NodeE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Node *node) {
  return self->enterBlock(node);
}

//  int QV4::Compiler::Codegen::leaveBlock()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen10leaveBlockEv(
    QV4::Compiler::Codegen *self) {
  return self->leaveBlock();
}

//  Reference QV4::Compiler::Codegen::unop(UnaryOperation op, const Reference
//      &expr)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen4unopENS1_14UnaryOperationERKNS1_9ReferenceE(
    QV4::Compiler::Codegen *self,
    QV4::Compiler::Codegen::UnaryOperation op,
    const QV4::Compiler::Codegen::Reference *expr) {
  return new QV4::Compiler::Codegen::Reference(self->unop(op, *expr));
}

//  void QV4::Compiler::Codegen::addCJump()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8addCJumpEv(
    QV4::Compiler::Codegen *self) {
  self->addCJump();
}

//  int QV4::Compiler::Codegen::registerString(const QString &name)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen14registerStringERK7QString(
    QV4::Compiler::Codegen *self,
    const QString *name) {
  return self->registerString(*name);
}

//  int QV4::Compiler::Codegen::registerConstant(QV4::ReturnedValue v)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen16registerConstantEy(
    QV4::Compiler::Codegen *self,
    QV4::ReturnedValue v) {
  return self->registerConstant(v);
}

//  int QV4::Compiler::Codegen::registerGetterLookup(int nameIndex,
//      JSUnitGenerator::LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen20registerGetterLookupEiNS0_15JSUnitGenerator10LookupModeE(
    QV4::Compiler::Codegen *self,
    int nameIndex,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerGetterLookup(nameIndex, mode);
}

//  int QV4::Compiler::Codegen::registerSetterLookup(int nameIndex)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen20registerSetterLookupEi(
    QV4::Compiler::Codegen *self,
    int nameIndex) {
  return self->registerSetterLookup(nameIndex);
}

//  int QV4::Compiler::Codegen::registerGlobalGetterLookup(int nameIndex,
//      JSUnitGenerator::LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen26registerGlobalGetterLookupEiNS0_15JSUnitGenerator10LookupModeE(
    QV4::Compiler::Codegen *self,
    int nameIndex,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerGlobalGetterLookup(nameIndex, mode);
}

//  int QV4::Compiler::Codegen::registerQmlContextPropertyGetterLookup(int
//      nameIndex, JSUnitGenerator::LookupMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen38registerQmlContextPropertyGetterLookupEiNS0_15JSUnitGenerator10LookupModeE(
    QV4::Compiler::Codegen *self,
    int nameIndex,
    QV4::Compiler::JSUnitGenerator::LookupMode mode) {
  return self->registerQmlContextPropertyGetterLookup(nameIndex, mode);
}

//  int QV4::Compiler::Codegen::defineFunction(const QString &name,
//      QQmlJS::AST::Node *ast, QQmlJS::AST::FormalParameterList *formals,
//      QQmlJS::AST::StatementList *body)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48Compiler7Codegen14defineFunctionERK7QStringPN6QQmlJS3AST4NodeEPNS6_19FormalParameterListEPNS6_13StatementListE(
    QV4::Compiler::Codegen *self,
    const QString *name,
    QQmlJS::AST::Node *ast,
    QQmlJS::AST::FormalParameterList *formals,
    QQmlJS::AST::StatementList *body) {
  return self->defineFunction(*name, ast, formals, body);
}

//  void QV4::Compiler::Codegen::statement(QQmlJS::AST::Statement *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen9statementEPN6QQmlJS3AST9StatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Statement *ast) {
  self->statement(ast);
}

//  void QV4::Compiler::Codegen::statement(QQmlJS::AST::ExpressionNode *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen9statementEPN6QQmlJS3AST14ExpressionNodeE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ExpressionNode *ast) {
  self->statement(ast);
}

//  Reference QV4::Compiler::Codegen::expression(QQmlJS::AST::ExpressionNode
//      *ast, const QString &name)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen10expressionEPN6QQmlJS3AST14ExpressionNodeERK7QString(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ExpressionNode *ast,
    const QString *name) {
  return new QV4::Compiler::Codegen::Reference(self->expression(ast, *name));
}

//  void QV4::Compiler::Codegen::accept(QQmlJS::AST::Node *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen6acceptEPN6QQmlJS3AST4NodeE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Node *node) {
  self->accept(node);
}

//  void QV4::Compiler::Codegen::program(QQmlJS::AST::Program *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen7programEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Program *ast) {
  self->program(ast);
}

//  void QV4::Compiler::Codegen::statementList(QQmlJS::AST::StatementList
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen13statementListEPN6QQmlJS3AST13StatementListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::StatementList *ast) {
  self->statementList(ast);
}

//  void
//      QV4::Compiler::Codegen::variableDeclaration(QQmlJS::AST::PatternEleme
//      nt *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen19variableDeclarationEPN6QQmlJS3AST14PatternElementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElement *ast) {
  self->variableDeclaration(ast);
}

//  void QV4::Compiler::Codegen::variableDeclarationList(QQmlJS::AST::Variabl
//      eDeclarationList *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen23variableDeclarationListEPN6QQmlJS3AST23VariableDeclarationListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VariableDeclarationList *ast) {
  self->variableDeclarationList(ast);
}

//  Reference QV4::Compiler::Codegen::targetForPatternElement(QQmlJS::AST::Pa
//      tternElement *p)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen23targetForPatternElementEPN6QQmlJS3AST14PatternElementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElement *p) {
  return new QV4::Compiler::Codegen::Reference(
      self->targetForPatternElement(
          p));
}

//  void QV4::Compiler::Codegen::initializeAndDestructureBindingElement(QQmlJ
//      S::AST::PatternElement *e, const Reference &baseRef, bool
//      isDefinition)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen38initializeAndDestructureBindingElementEPN6QQmlJS3AST14PatternElementERKNS1_9ReferenceEb(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElement *e,
    const QV4::Compiler::Codegen::Reference *baseRef,
    bool isDefinition) {
  self->initializeAndDestructureBindingElement(e, *baseRef, isDefinition);
}

//  void QV4::Compiler::Codegen::destructurePropertyList(const Reference
//      &object, QQmlJS::AST::PatternPropertyList *bindingList, bool
//      isDefinition)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen23destructurePropertyListERKNS1_9ReferenceEPN6QQmlJS3AST19PatternPropertyListEb(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *object,
    QQmlJS::AST::PatternPropertyList *bindingList,
    bool isDefinition) {
  self->destructurePropertyList(*object, bindingList, isDefinition);
}

//  void QV4::Compiler::Codegen::destructureElementList(const Reference
//      &array, QQmlJS::AST::PatternElementList *bindingList, bool
//      isDefinition)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen22destructureElementListERKNS1_9ReferenceEPN6QQmlJS3AST18PatternElementListEb(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *array,
    QQmlJS::AST::PatternElementList *bindingList,
    bool isDefinition) {
  self->destructureElementList(*array, bindingList, isDefinition);
}

//  void QV4::Compiler::Codegen::destructurePattern(QQmlJS::AST::Pattern *p,
//      const Reference &rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen18destructurePatternEPN6QQmlJS3AST7PatternERKNS1_9ReferenceE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Pattern *p,
    const QV4::Compiler::Codegen::Reference *rhs) {
  self->destructurePattern(p, *rhs);
}

//  Reference QV4::Compiler::Codegen::referenceForPropertyName(const
//      Codegen::Reference &object, QQmlJS::AST::PropertyName *name)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen24referenceForPropertyNameERKNS1_9ReferenceEPN6QQmlJS3AST12PropertyNameE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *object,
    QQmlJS::AST::PropertyName *name) {
  return new QV4::Compiler::Codegen::Reference(
      self->referenceForPropertyName(
          *object,
          name));
}

//  void QV4::Compiler::Codegen::emitReturn(const Reference &expr)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen10emitReturnERKNS1_9ReferenceE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *expr) {
  self->emitReturn(*expr);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ArgumentList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12ArgumentListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArgumentList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST9CaseBlockE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CaseBlock *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CaseClause *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST10CaseClauseE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CaseClause *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CaseClauses *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST11CaseClausesE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CaseClauses *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST5CatchE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Catch *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DefaultClause *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13DefaultClauseE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DefaultClause *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Elision *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST7ElisionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Elision *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Finally *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST7FinallyE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Finally *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FormalParameterList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19FormalParameterListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FormalParameterList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Program *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Program *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::StatementList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13StatementListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::StatementList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiArrayMemberList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17UiArrayMemberListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiArrayMemberList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiImport *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST8UiImportE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiImport *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiHeaderItemList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16UiHeaderItemListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiHeaderItemList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiPragmaValueList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17UiPragmaValueListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiPragmaValueList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiPragma *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST8UiPragmaE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiPragma *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectInitializer *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19UiObjectInitializerE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectInitializer *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectMemberList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18UiObjectMemberListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectMemberList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiParameterList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiParameterListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiParameterList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiProgram *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST9UiProgramE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiProgram *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiQualifiedId *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13UiQualifiedIdE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiQualifiedId *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::VariableDeclarationList
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST23VariableDeclarationListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VariableDeclarationList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternElement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14PatternElementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternElementList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18PatternElementListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElementList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternProperty *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15PatternPropertyE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternProperty *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternPropertyList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19PatternPropertyListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternPropertyList *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ExportDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17ExportDeclarationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ExportDeclaration *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TypeAnnotation *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14TypeAnnotationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TypeAnnotation *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ArrayPattern *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12ArrayPatternE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArrayPattern *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ArrayMemberExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST21ArrayMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArrayMemberExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::BinaryExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16BinaryExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::BinaryExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CallExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14CallExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CallExpression *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::Codegen::endVisit(QQmlJS::AST::CallExpression *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8endVisitEPN6QQmlJS3AST14CallExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CallExpression *ast) {
  self->endVisit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CommaExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15CommaExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CommaExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ConditionalExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST21ConditionalExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ConditionalExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DeleteExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16DeleteExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DeleteExpression *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::Codegen::endVisit(QQmlJS::AST::DeleteExpression *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8endVisitEPN6QQmlJS3AST16DeleteExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DeleteExpression *ast) {
  self->endVisit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FalseLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12FalseLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FalseLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::SuperLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12SuperLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::SuperLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FieldMemberExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FieldMemberExpression *ast) {
  return self->visit(ast);
}

//  void QV4::Compiler::Codegen::endVisit(QQmlJS::AST::FieldMemberExpression
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8endVisitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FieldMemberExpression *ast) {
  self->endVisit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TaggedTemplate *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14TaggedTemplateE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TaggedTemplate *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FunctionExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FunctionExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::IdentifierExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST20IdentifierExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::IdentifierExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NestedExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16NestedExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NestedExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NewExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13NewExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NewExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NewMemberExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19NewMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NewMemberExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NotExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13NotExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NotExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NullExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14NullExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NullExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NumericLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14NumericLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NumericLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ObjectPattern *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13ObjectPatternE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ObjectPattern *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PostDecrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST23PostDecrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PostDecrementExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PostIncrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST23PostIncrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PostIncrementExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PreDecrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST22PreDecrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PreDecrementExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PreIncrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST22PreIncrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PreIncrementExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::RegExpLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13RegExpLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::RegExpLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::StringLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13StringLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::StringLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TemplateLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15TemplateLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TemplateLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ThisExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14ThisExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ThisExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TildeExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15TildeExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TildeExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TrueLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST11TrueLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TrueLiteral *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TypeOfExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16TypeOfExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TypeOfExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UnaryMinusExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST20UnaryMinusExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UnaryMinusExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UnaryPlusExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19UnaryPlusExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UnaryPlusExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::VoidExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14VoidExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VoidExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FunctionDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FunctionDeclaration *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::YieldExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15YieldExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::YieldExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ClassExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15ClassExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ClassExpression *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ClassDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16ClassDeclarationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST5BlockE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Block *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::BreakStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14BreakStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::BreakStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ContinueStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17ContinueStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ContinueStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DebuggerStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17DebuggerStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DebuggerStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DoWhileStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16DoWhileStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DoWhileStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::EmptyStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14EmptyStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::EmptyStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ExpressionStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19ExpressionStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ForEachStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16ForEachStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ForEachStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12ForStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ForStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::IfStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST11IfStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::IfStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::LabelledStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17LabelledStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::LabelledStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ReturnStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15ReturnStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ReturnStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::SwitchStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15SwitchStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::SwitchStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ThrowStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14ThrowStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ThrowStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TryStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12TryStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TryStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::VariableStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17VariableStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VariableStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::WhileStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14WhileStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::WhileStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::WithStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13WithStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::WithStatement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiArrayBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14UiArrayBindingE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiArrayBinding *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiObjectBindingE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectBinding *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectDefinition *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectDefinition *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiPublicMember *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14UiPublicMemberE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiPublicMember *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiScriptBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiScriptBindingE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiSourceElement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiSourceElementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiSourceElement *ast) {
  return self->visit(ast);
}

//  bool QV4::Compiler::Codegen::throwSyntaxErrorOnEvalOrArgumentsInStrictMod
//      e(const Reference &r, const QQmlJS::SourceLocation &loc)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen45throwSyntaxErrorOnEvalOrArgumentsInStrictModeERKNS1_9ReferenceERKN6QQmlJS14SourceLocationE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *r,
    const QQmlJS::SourceLocation *loc) {
  return self->throwSyntaxErrorOnEvalOrArgumentsInStrictMode(*r, *loc);
}

//  void QV4::Compiler::Codegen::throwSyntaxError(const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen16throwSyntaxErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::Compiler::Codegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->throwSyntaxError(*loc, *detail);
}

//  void QV4::Compiler::Codegen::throwReferenceError(const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen19throwReferenceErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::Compiler::Codegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->throwReferenceError(*loc, *detail);
}

//  void QV4::Compiler::Codegen::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen24throwRecursionDepthErrorEv(
    QV4::Compiler::Codegen *self) {
  self->throwRecursionDepthError();
}

//  ErrorType QV4::Compiler::Codegen::errorType() const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::ErrorType ritual_ZNK3QV48Compiler7Codegen9errorTypeEv(
    const QV4::Compiler::Codegen *self) {
  return self->errorType();
}

//  bool QV4::Compiler::Codegen::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen8hasErrorEv(
    const QV4::Compiler::Codegen *self) {
  return self->hasError();
}

//  QQmlJS::DiagnosticMessage QV4::Compiler::Codegen::error() const
extern "C" Q_DECL_EXPORT
QQmlJS::DiagnosticMessage *ritual_ZNK3QV48Compiler7Codegen5errorEv(
    const QV4::Compiler::Codegen *self) {
  return new QQmlJS::DiagnosticMessage(self->error());
}

//  QUrl QV4::Compiler::Codegen::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK3QV48Compiler7Codegen3urlEv(
    const QV4::Compiler::Codegen *self) {
  return new QUrl(self->url());
}

//  Reference
//      QV4::Compiler::Codegen::binopHelper(QQmlJS::AST::BinaryExpression
//      *ast, QSOperator::Op oper, Reference &left, Reference &right)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen11binopHelperEPN6QQmlJS3AST16BinaryExpressionEN10QSOperator2OpERNS1_9ReferenceES9_(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::BinaryExpression *ast,
    QSOperator::Op oper,
    QV4::Compiler::Codegen::Reference *left,
    QV4::Compiler::Codegen::Reference *right) {
  return new QV4::Compiler::Codegen::Reference(
      self->binopHelper(
          ast,
          oper,
          *left,
          *right));
}

//  Reference QV4::Compiler::Codegen::jumpBinop(QSOperator::Op oper,
//      Reference &left, Reference &right)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9jumpBinopEN10QSOperator2OpERNS1_9ReferenceES5_(
    QV4::Compiler::Codegen *self,
    QSOperator::Op oper,
    QV4::Compiler::Codegen::Reference *left,
    QV4::Compiler::Codegen::Reference *right) {
  return new QV4::Compiler::Codegen::Reference(
      self->jumpBinop(
          oper,
          *left,
          *right));
}

//  Arguments QV4::Compiler::Codegen::pushArgs(QQmlJS::AST::ArgumentList
//      *args)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Arguments *ritual_ZN3QV48Compiler7Codegen8pushArgsEPN6QQmlJS3AST12ArgumentListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArgumentList *args) {
  return new QV4::Compiler::Codegen::Arguments(self->pushArgs(args));
}

//  void QV4::Compiler::Codegen::handleCall(Reference &base, Arguments
//      calldata, int slotForFunction, int slotForThisObject, bool optional)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen10handleCallERNS1_9ReferenceENS1_9ArgumentsEiib(
    QV4::Compiler::Codegen *self,
    QV4::Compiler::Codegen::Reference *base,
    const QV4::Compiler::Codegen::Arguments *calldata,
    int slotForFunction,
    int slotForThisObject,
    bool optional) {
  self->handleCall(
      *base,
      *calldata,
      slotForFunction,
      slotForThisObject,
      optional);
}

//  Arguments
//      QV4::Compiler::Codegen::pushTemplateArgs(QQmlJS::AST::TemplateLiteral
//      *args)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Arguments *ritual_ZN3QV48Compiler7Codegen16pushTemplateArgsEPN6QQmlJS3AST15TemplateLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TemplateLiteral *args) {
  return new QV4::Compiler::Codegen::Arguments(self->pushTemplateArgs(args));
}

//  bool QV4::Compiler::Codegen::handleTaggedTemplate(Reference base,
//      QQmlJS::AST::TaggedTemplate *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen20handleTaggedTemplateENS1_9ReferenceEPN6QQmlJS3AST14TaggedTemplateE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *base,
    QQmlJS::AST::TaggedTemplate *ast) {
  return self->handleTaggedTemplate(*base, ast);
}

//  void
//      QV4::Compiler::Codegen::createTemplateObject(QQmlJS::AST::TemplateLit
//      eral *t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen20createTemplateObjectEPN6QQmlJS3AST15TemplateLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TemplateLiteral *t) {
  self->createTemplateObject(t);
}

//  void QV4::Compiler::Codegen::setUseFastLookups(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen17setUseFastLookupsEb(
    QV4::Compiler::Codegen *self,
    bool b) {
  self->setUseFastLookups(b);
}

//  void QV4::Compiler::Codegen::handleTryCatch(QQmlJS::AST::TryStatement
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen14handleTryCatchEPN6QQmlJS3AST12TryStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TryStatement *ast) {
  self->handleTryCatch(ast);
}

//  void QV4::Compiler::Codegen::handleTryFinally(QQmlJS::AST::TryStatement
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen16handleTryFinallyEPN6QQmlJS3AST12TryStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TryStatement *ast) {
  self->handleTryFinally(ast);
}

//  Reference QV4::Compiler::Codegen::referenceForName(const QString &name,
//      bool lhs, const QQmlJS::SourceLocation &accessLocation)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen16referenceForNameERK7QStringbRKN6QQmlJS14SourceLocationE(
    QV4::Compiler::Codegen *self,
    const QString *name,
    bool lhs,
    const QQmlJS::SourceLocation *accessLocation) {
  return new QV4::Compiler::Codegen::Reference(
      self->referenceForName(
          *name,
          lhs,
          *accessLocation));
}

//  QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      QV4::Compiler::Codegen::generateCompilationUnit(bool
//      generateUnitData)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZN3QV48Compiler7Codegen23generateCompilationUnitEb(
    QV4::Compiler::Codegen *self,
    bool generateUnitData) {
  return new QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
      self->generateCompilationUnit(
          generateUnitData));
}

//  QQmlRefPointer<QV4::CompiledData::CompilationUnit>
//      QV4::Compiler::Codegen::compileModule(bool debugMode, const QString
//      &url, const QString &sourceCode, const QDateTime &sourceTimeStamp,
//      QList<QQmlJS::DiagnosticMessage> *diagnostics)
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QV4::CompiledData::CompilationUnit> *ritual_ZN3QV48Compiler7Codegen13compileModuleEbRK7QStringS4_RK9QDateTimeP5QListIN6QQmlJS17DiagnosticMessageEE(
    bool debugMode,
    const QString *url,
    const QString *sourceCode,
    const QDateTime *sourceTimeStamp,
    QList<QQmlJS::DiagnosticMessage> *diagnostics) {
  return new QQmlRefPointer<QV4::CompiledData::CompilationUnit>(
      QV4::Compiler::Codegen::compileModule(
          debugMode,
          *url,
          *sourceCode,
          *sourceTimeStamp,
          diagnostics));
}

//  const QV4::CompiledData::Unit
//      *QV4::Compiler::Codegen::generateNativeModuleUnitData(bool debugMode,
//      const QString &url, const QV4::Value &value)
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Unit *ritual_ZN3QV48Compiler7Codegen28generateNativeModuleUnitDataEbRK7QStringRKNS_5ValueE(
    bool debugMode,
    const QString *url,
    const QV4::Value *value) {
  return QV4::Compiler::Codegen::generateNativeModuleUnitData(
      debugMode,
      *url,
      *value);
}

//  Context *QV4::Compiler::Codegen::currentContext() const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context *ritual_ZNK3QV48Compiler7Codegen14currentContextEv(
    const QV4::Compiler::Codegen *self) {
  return self->currentContext();
}

//  BytecodeGenerator *QV4::Compiler::Codegen::generator() const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::BytecodeGenerator *ritual_ZNK3QV48Compiler7Codegen9generatorEv(
    const QV4::Compiler::Codegen *self) {
  return self->generator();
}

//  void QV4::Compiler::Codegen::loadClosure(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen11loadClosureEi(
    QV4::Compiler::Codegen *self,
    int index) {
  self->loadClosure(index);
}

//  Module *QV4::Compiler::Codegen::module() const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Module *ritual_ZNK3QV48Compiler7Codegen6moduleEv(
    const QV4::Compiler::Codegen *self) {
  return self->module();
}

//  void QV4::Compiler::Codegen::setExprResult(const Reference &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen13setExprResultERKNS1_9ReferenceE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *result) {
  self->setExprResult(*result);
}

//  void QV4::Compiler::Codegen::setExprResult(Reference &&result)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen13setExprResultEONS1_9ReferenceE(
    QV4::Compiler::Codegen *self,
    QV4::Compiler::Codegen::Reference *result) {
  self->setExprResult(std::move(*result));
}

//  Reference QV4::Compiler::Codegen::exprResult() const
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZNK3QV48Compiler7Codegen10exprResultEv(
    const QV4::Compiler::Codegen *self) {
  return new QV4::Compiler::Codegen::Reference(self->exprResult());
}

//  void QV4::Compiler::Codegen::clearExprResultName()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen19clearExprResultNameEv(
    QV4::Compiler::Codegen *self) {
  self->clearExprResultName();
}

//  bool QV4::Compiler::Codegen::exprAccept(Format f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen10exprAcceptENS1_6FormatE(
    QV4::Compiler::Codegen *self,
    QV4::Compiler::Codegen::Format f) {
  return self->exprAccept(f);
}

//  const Result &QV4::Compiler::Codegen::currentExpr() const
extern "C" Q_DECL_EXPORT
const QV4::Compiler::Codegen::Result *ritual_ZNK3QV48Compiler7Codegen11currentExprEv(
    const QV4::Compiler::Codegen *self) {
  return &(self->currentExpr());
}

//  void QV4::Compiler::Codegen::pushExpr(Result &&expr)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8pushExprEONS1_6ResultE(
    QV4::Compiler::Codegen *self,
    QV4::Compiler::Codegen::Result *expr) {
  self->pushExpr(std::move(*expr));
}

//  void QV4::Compiler::Codegen::pushExpr(const Result &expr)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8pushExprERKNS1_6ResultE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Result *expr) {
  self->pushExpr(*expr);
}

//  void QV4::Compiler::Codegen::pushExpr(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen8pushExprERK7QString(
    QV4::Compiler::Codegen *self,
    const QString *name) {
  self->pushExpr(*name);
}

//  Result QV4::Compiler::Codegen::popExpr()
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Result *ritual_ZN3QV48Compiler7Codegen7popExprEv(
    QV4::Compiler::Codegen *self) {
  return new QV4::Compiler::Codegen::Result(self->popExpr());
}

//  Reference QV4::Compiler::Codegen::popResult()
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9popResultEv(
    QV4::Compiler::Codegen *self) {
  return new QV4::Compiler::Codegen::Reference(self->popResult());
}

//  VolatileMemoryLocations
//      QV4::Compiler::Codegen::scanVolatileMemoryLocations(QQmlJS::AST::Node
//      *ast)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::VolatileMemoryLocations *ritual_ZN3QV48Compiler7Codegen27scanVolatileMemoryLocationsEPN6QQmlJS3AST4NodeE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Node *ast) {
  return new QV4::Compiler::Codegen::VolatileMemoryLocations(
      self->scanVolatileMemoryLocations(
          ast));
}

//  void QV4::Compiler::Codegen::handleConstruct(const Reference &base,
//      QQmlJS::AST::ArgumentList *args)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen15handleConstructERKNS1_9ReferenceEPN6QQmlJS3AST12ArgumentListE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *base,
    QQmlJS::AST::ArgumentList *args) {
  self->handleConstruct(*base, args);
}

//  void QV4::Compiler::Codegen::throwError(ErrorType errorType, const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen10throwErrorENS1_9ErrorTypeERKN6QQmlJS14SourceLocationERK7QString(
    QV4::Compiler::Codegen *self,
    QV4::Compiler::Codegen::ErrorType errorType,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  self->throwError(errorType, *loc, *detail);
}

//  bool QV4::Compiler::Codegen::traverseOptionalChain(QQmlJS::AST::Node
//      *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen21traverseOptionalChainEPN6QQmlJS3AST4NodeE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Node *node) {
  return self->traverseOptionalChain(node);
}

//  void QV4::Compiler::Codegen::optionalChainFinalizer(const Reference
//      &expressionResult, bool tailOfChain, bool isDeleteExpression)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen22optionalChainFinalizerERKNS1_9ReferenceEbb(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *expressionResult,
    bool tailOfChain,
    bool isDeleteExpression) {
  self->optionalChainFinalizer(
      *expressionResult,
      tailOfChain,
      isDeleteExpression);
}

//  Reference QV4::Compiler::Codegen::loadSubscriptForCall(const Reference
//      &base)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen20loadSubscriptForCallERKNS1_9ReferenceE(
    QV4::Compiler::Codegen *self,
    const QV4::Compiler::Codegen::Reference *base) {
  return new QV4::Compiler::Codegen::Reference(
      self->loadSubscriptForCall(
          *base));
}

//  void QV4::Compiler::Codegen::generateThrowException(const QString &type,
//      const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen22generateThrowExceptionERK7QStringS4_(
    QV4::Compiler::Codegen *self,
    const QString *type,
    const QString *text) {
  self->generateThrowException(*type, *text);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ArgumentList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12ArgumentListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArgumentList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST9CaseBlockE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CaseBlock *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CaseClause *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST10CaseClauseE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CaseClause *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CaseClauses *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST11CaseClausesE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CaseClauses *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST5CatchE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Catch *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DefaultClause *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13DefaultClauseE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DefaultClause *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Elision *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST7ElisionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Elision *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Finally *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST7FinallyE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Finally *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FormalParameterList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19FormalParameterListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FormalParameterList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Program *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST7ProgramE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Program *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::StatementList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13StatementListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::StatementList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiArrayMemberList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17UiArrayMemberListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiArrayMemberList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiImport *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST8UiImportE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiImport *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiHeaderItemList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16UiHeaderItemListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiHeaderItemList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiPragmaValueList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17UiPragmaValueListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiPragmaValueList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiPragma *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST8UiPragmaE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiPragma *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectInitializer *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19UiObjectInitializerE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectInitializer *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectMemberList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18UiObjectMemberListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectMemberList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiParameterList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiParameterListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiParameterList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiProgram *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST9UiProgramE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiProgram *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiQualifiedId *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13UiQualifiedIdE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiQualifiedId *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::VariableDeclarationList
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST23VariableDeclarationListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VariableDeclarationList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternElement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14PatternElementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternElementList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18PatternElementListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternElementList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternProperty *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15PatternPropertyE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternProperty *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PatternPropertyList *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19PatternPropertyListE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PatternPropertyList *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ExportDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17ExportDeclarationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ExportDeclaration *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TypeAnnotation *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14TypeAnnotationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TypeAnnotation *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ArrayPattern *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12ArrayPatternE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArrayPattern *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ArrayMemberExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST21ArrayMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ArrayMemberExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::BinaryExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16BinaryExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::BinaryExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CallExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14CallExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CallExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  void QV4::Compiler::Codegen::endVisit(QQmlJS::AST::CallExpression *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler7Codegen8endVisitEPN6QQmlJS3AST14CallExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CallExpression *ast) {
  static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::endVisit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::CommaExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15CommaExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::CommaExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ConditionalExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST21ConditionalExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ConditionalExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DeleteExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16DeleteExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DeleteExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  void QV4::Compiler::Codegen::endVisit(QQmlJS::AST::DeleteExpression *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler7Codegen8endVisitEPN6QQmlJS3AST16DeleteExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DeleteExpression *ast) {
  static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::endVisit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FalseLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12FalseLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FalseLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::SuperLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12SuperLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::SuperLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FieldMemberExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FieldMemberExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  void QV4::Compiler::Codegen::endVisit(QQmlJS::AST::FieldMemberExpression
//      *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler7Codegen8endVisitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FieldMemberExpression *ast) {
  static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::endVisit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TaggedTemplate *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14TaggedTemplateE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TaggedTemplate *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FunctionExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FunctionExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::IdentifierExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST20IdentifierExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::IdentifierExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NestedExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16NestedExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NestedExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NewExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13NewExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NewExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NewMemberExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19NewMemberExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NewMemberExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NotExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13NotExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NotExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NullExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14NullExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NullExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::NumericLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14NumericLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::NumericLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ObjectPattern *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13ObjectPatternE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ObjectPattern *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PostDecrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST23PostDecrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PostDecrementExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PostIncrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST23PostIncrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PostIncrementExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PreDecrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST22PreDecrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PreDecrementExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::PreIncrementExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST22PreIncrementExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::PreIncrementExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::RegExpLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13RegExpLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::RegExpLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::StringLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13StringLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::StringLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TemplateLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15TemplateLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TemplateLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ThisExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14ThisExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ThisExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TildeExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15TildeExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TildeExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TrueLiteral *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST11TrueLiteralE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TrueLiteral *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TypeOfExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16TypeOfExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TypeOfExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UnaryMinusExpression
//      *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST20UnaryMinusExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UnaryMinusExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UnaryPlusExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19UnaryPlusExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UnaryPlusExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::VoidExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14VoidExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VoidExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::FunctionDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::FunctionDeclaration *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::YieldExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15YieldExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::YieldExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ClassExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15ClassExpressionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ClassExpression *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ClassDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16ClassDeclarationE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST5BlockE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::Block *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::BreakStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14BreakStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::BreakStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ContinueStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17ContinueStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ContinueStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DebuggerStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17DebuggerStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DebuggerStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::DoWhileStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16DoWhileStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::DoWhileStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::EmptyStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14EmptyStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::EmptyStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ExpressionStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST19ExpressionStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ForEachStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST16ForEachStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ForEachStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12ForStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ForStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::IfStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST11IfStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::IfStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::LabelledStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17LabelledStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::LabelledStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ReturnStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15ReturnStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ReturnStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::SwitchStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15SwitchStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::SwitchStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::ThrowStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14ThrowStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::ThrowStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::TryStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST12TryStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::TryStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::VariableStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST17VariableStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::VariableStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::WhileStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14WhileStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::WhileStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::WithStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST13WithStatementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::WithStatement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiArrayBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14UiArrayBindingE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiArrayBinding *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiObjectBindingE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectBinding *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiObjectDefinition *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiObjectDefinition *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiPublicMember *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST14UiPublicMemberE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiPublicMember *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiScriptBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiScriptBindingE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  bool QV4::Compiler::Codegen::visit(QQmlJS::AST::UiSourceElement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler7Codegen5visitEPN6QQmlJS3AST15UiSourceElementE(
    QV4::Compiler::Codegen *self,
    QQmlJS::AST::UiSourceElement *ast) {
  return static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::visit(
      ast);
}

//  void QV4::Compiler::Codegen::throwSyntaxError(const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler7Codegen16throwSyntaxErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::Compiler::Codegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::throwSyntaxError(
      *loc,
      *detail);
}

//  void QV4::Compiler::Codegen::throwReferenceError(const
//      QQmlJS::SourceLocation &loc, const QString &detail)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler7Codegen19throwReferenceErrorERKN6QQmlJS14SourceLocationERK7QString(
    QV4::Compiler::Codegen *self,
    const QQmlJS::SourceLocation *loc,
    const QString *detail) {
  static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::throwReferenceError(
      *loc,
      *detail);
}

//  void QV4::Compiler::Codegen::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN3QV48Compiler7Codegen24throwRecursionDepthErrorEv(
    QV4::Compiler::Codegen *self) {
  static_cast<OwnQV4_Compiler_Codegen *>(self)->OwnQV4_Compiler_Codegen::throwRecursionDepthError();
}

//  a QQmlRefPointer<QV4::CompiledData::CompilationUnit> a ritual of
//      QV4::Compiler::Codegen gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_Compiler_Codegen__QQmlRefPointer_QV4_CompiledData_CompilationUnit(
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> *self) {
  delete self;
}

//  a QV4::Compiler::Codegen::Result a ritual of QV4::Compiler::Codegen gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_Compiler_Codegen__QV4_Compiler_Codegen_Result(
    QV4::Compiler::Codegen::Result *self) {
  delete self;
}
