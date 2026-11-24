//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimportvisitor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimportvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsscopesbyid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsannotation_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlJSImportVisitor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlJSImportVisitor : QQmlJSImportVisitor {
  using QQmlJSImportVisitor::visit;
  using QQmlJSImportVisitor::endVisit;
  using QQmlJSImportVisitor::throwRecursionDepthError;
  using QQmlJSImportVisitor::leaveEnvironment;
};

//  A QQmlJSImportVisitor that Python can take functions over in. Every QQmlJSImportVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlJSImportVisitorCall0)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall1)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall2)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef void (*CuteQQmlJSImportVisitorCall3)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall4)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef void (*CuteQQmlJSImportVisitorCall5)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall6)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef void (*CuteQQmlJSImportVisitorCall7)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall8)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef void (*CuteQQmlJSImportVisitorCall9)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall10)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall11)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef void (*CuteQQmlJSImportVisitorCall12)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall13)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef void (*CuteQQmlJSImportVisitorCall14)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall15)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall16)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall17)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall18)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall19)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef void (*CuteQQmlJSImportVisitorCall20)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall21)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall22)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall23)(const void *, QQmlJS::AST::UiImport *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall24)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall25)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef void (*CuteQQmlJSImportVisitorCall26)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall27)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall28)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall29)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall30)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall31)(const void *, QQmlJS::AST::Block *, int *);
typedef void (*CuteQQmlJSImportVisitorCall32)(const void *, QQmlJS::AST::Block *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall33)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef void (*CuteQQmlJSImportVisitorCall34)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall35)(const void *, QQmlJS::AST::Catch *, int *);
typedef void (*CuteQQmlJSImportVisitorCall36)(const void *, QQmlJS::AST::Catch *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall37)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall38)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall39)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall40)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef void (*CuteQQmlJSImportVisitorCall41)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall42)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef void (*CuteQQmlJSImportVisitorCall43)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall44)(const void *, QQmlJS::AST::ESModule *, int *);
typedef void (*CuteQQmlJSImportVisitorCall45)(const void *, QQmlJS::AST::ESModule *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall46)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQQmlJSImportVisitorCall47)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQQmlJSImportVisitorCall48)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall49)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall50)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall51)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall52)(const void *, int *);
typedef void (*CuteQQmlJSImportVisitorCall53)(const void *, int *);
typedef void (*CuteQQmlJSImportVisitorCall54)(const void *, const QQmlJSMetaPropertyBinding *, const QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall55)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQQmlJSImportVisitorCall56)(const void *, QQmlJS::AST::Node *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall57)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall58)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall59)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall60)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall61)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef void (*CuteQQmlJSImportVisitorCall62)(const void *, QQmlJS::AST::UiImport *, int *);
typedef void (*CuteQQmlJSImportVisitorCall63)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall64)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQQmlJSImportVisitorCall65)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall66)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall67)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall68)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall69)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall70)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall71)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall72)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJSImportVisitorCall73)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJSImportVisitorCall74)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall75)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall76)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall77)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQQmlJSImportVisitorCall78)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall79)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef void (*CuteQQmlJSImportVisitorCall80)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall81)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall82)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall83)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall84)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall85)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall86)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall87)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall88)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall89)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall90)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall91)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall92)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall93)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall94)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall95)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall96)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall97)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall98)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall99)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall100)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall101)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall102)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall103)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef void (*CuteQQmlJSImportVisitorCall104)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall105)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef void (*CuteQQmlJSImportVisitorCall106)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall107)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef void (*CuteQQmlJSImportVisitorCall108)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall109)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall110)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall111)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall112)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall113)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall114)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef void (*CuteQQmlJSImportVisitorCall115)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall116)(const void *, QQmlJS::AST::Elision *, int *);
typedef void (*CuteQQmlJSImportVisitorCall117)(const void *, QQmlJS::AST::Elision *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall118)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall119)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall120)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef void (*CuteQQmlJSImportVisitorCall121)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall122)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef void (*CuteQQmlJSImportVisitorCall123)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall124)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef void (*CuteQQmlJSImportVisitorCall125)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall126)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef void (*CuteQQmlJSImportVisitorCall127)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall128)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall129)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall130)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall131)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef void (*CuteQQmlJSImportVisitorCall132)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall133)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall134)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall135)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall136)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall137)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall138)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall139)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall140)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall141)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall142)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall143)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall144)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall145)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall146)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall147)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall148)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall149)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall150)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall151)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall152)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall153)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall154)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall155)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall156)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall157)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall158)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall159)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall160)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall161)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall162)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall163)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall164)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall165)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall166)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall167)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall168)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall169)(const void *, QQmlJS::AST::StatementList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall170)(const void *, QQmlJS::AST::StatementList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall171)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall172)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall173)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall174)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall175)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall176)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall177)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall178)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall179)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall180)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall181)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall182)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall183)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall184)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall185)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall186)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall187)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall188)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef void (*CuteQQmlJSImportVisitorCall189)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall190)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall191)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall192)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef void (*CuteQQmlJSImportVisitorCall193)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall194)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef void (*CuteQQmlJSImportVisitorCall195)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall196)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef void (*CuteQQmlJSImportVisitorCall197)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall198)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall199)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall200)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall201)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall202)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall203)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall204)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJSImportVisitorCall205)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJSImportVisitorCall206)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall207)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall208)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall209)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef void (*CuteQQmlJSImportVisitorCall210)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall211)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef void (*CuteQQmlJSImportVisitorCall212)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall213)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall214)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall215)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef void (*CuteQQmlJSImportVisitorCall216)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall217)(const void *, QQmlJS::AST::FromClause *, int *);
typedef void (*CuteQQmlJSImportVisitorCall218)(const void *, QQmlJS::AST::FromClause *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall219)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef void (*CuteQQmlJSImportVisitorCall220)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall221)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef void (*CuteQQmlJSImportVisitorCall222)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall223)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef void (*CuteQQmlJSImportVisitorCall224)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall225)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef void (*CuteQQmlJSImportVisitorCall226)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall227)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef void (*CuteQQmlJSImportVisitorCall228)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall229)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef void (*CuteQQmlJSImportVisitorCall230)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall231)(const void *, QQmlJS::AST::Type *, int *);
typedef void (*CuteQQmlJSImportVisitorCall232)(const void *, QQmlJS::AST::Type *, int *);
typedef bool (*CuteQQmlJSImportVisitorCall233)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJSImportVisitorCall234)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
class CuteQQmlJSImportVisitor : public QQmlJSImportVisitor {
public:
  using QQmlJSImportVisitor::QQmlJSImportVisitor;
  void *taken[235] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19ExpressionStatementE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19ExpressionStatementE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9UiProgramE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9UiProgramE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectDefinitionE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectDefinitionE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiInlineComponentE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiInlineComponentE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiPublicMemberE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiPublicMemberE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10UiRequiredE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiScriptBindingE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiScriptBindingE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiArrayBindingE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiArrayBindingE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiEnumDeclarationE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18FunctionExpressionE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18FunctionExpressionE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiSourceElementE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FunctionDeclarationE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FunctionDeclarationE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ClassExpressionE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ClassExpressionE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiImportE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiPragmaE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassDeclarationE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassDeclarationE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ForStatementE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ForStatementE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ForEachStatementE")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ForEachStatementE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5BlockE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5BlockE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9CaseBlockE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9CaseBlockE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5CatchE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5CatchE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13WithStatementE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13WithStatementE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FormalParameterListE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiObjectBindingE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiObjectBindingE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ExportDeclarationE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ExportDeclarationE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8ESModuleE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8ESModuleE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ProgramE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ProgramE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21FieldMemberExpressionE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20IdentifierExpressionE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14PatternElementE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11IfStatementE")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor24throwRecursionDepthErrorEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlJSImportVisitor16leaveEnvironmentEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQmlJSImportVisitor20handleLiteralBindingERK25QQmlJSMetaPropertyBindingPKN6QQmlJS3AST14UiPublicMemberE")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8preVisitEPNS0_4NodeE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor9postVisitEPNS0_4NodeE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiHeaderItemListE")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiHeaderItemListE")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiPragmaValueListE")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiPragmaValueListE")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiPragmaE")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiImportE")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiSourceElementE")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UiObjectInitializerE")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UiObjectInitializerE")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiParameterListE")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiParameterListE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectMemberListE")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectMemberListE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiArrayMemberListE")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiArrayMemberListE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13UiQualifiedIdE")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13UiQualifiedIdE")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiEnumDeclarationE")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiEnumMemberListE")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiEnumMemberListE")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiVersionSpecifierE")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiVersionSpecifierE")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12UiAnnotationE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12UiAnnotationE")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiAnnotationListE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiAnnotationListE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10UiRequiredE")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeExpressionE")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeExpressionE")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThisExpressionE")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThisExpressionE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20IdentifierExpressionE")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NullExpressionE")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NullExpressionE")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11TrueLiteralE")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11TrueLiteralE")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12FalseLiteralE")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12FalseLiteralE")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12SuperLiteralE")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12SuperLiteralE")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StringLiteralE")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StringLiteralE")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TemplateLiteralE")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TemplateLiteralE")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NumericLiteralE")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NumericLiteralE")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13RegExpLiteralE")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13RegExpLiteralE")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArrayPatternE")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArrayPatternE")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13ObjectPatternE")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13ObjectPatternE")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18PatternElementListE")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18PatternElementListE")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19PatternPropertyListE")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19PatternPropertyListE")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14PatternElementE")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15PatternPropertyE")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15PatternPropertyE")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ElisionE")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ElisionE")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16NestedExpressionE")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16NestedExpressionE")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22IdentifierPropertyNameE")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22IdentifierPropertyNameE")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_25StringLiteralPropertyNameE")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_25StringLiteralPropertyNameE")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20ComputedPropertyNameE")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20ComputedPropertyNameE")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ArrayMemberExpressionE")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ArrayMemberExpressionE")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21FieldMemberExpressionE")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TaggedTemplateE")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TaggedTemplateE")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19NewMemberExpressionE")) {
      taken[133] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19NewMemberExpressionE")) {
      taken[134] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NewExpressionE")) {
      taken[135] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NewExpressionE")) {
      taken[136] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14CallExpressionE")) {
      taken[137] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14CallExpressionE")) {
      taken[138] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArgumentListE")) {
      taken[139] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArgumentListE")) {
      taken[140] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostIncrementExpressionE")) {
      taken[141] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostIncrementExpressionE")) {
      taken[142] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostDecrementExpressionE")) {
      taken[143] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostDecrementExpressionE")) {
      taken[144] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DeleteExpressionE")) {
      taken[145] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DeleteExpressionE")) {
      taken[146] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14VoidExpressionE")) {
      taken[147] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14VoidExpressionE")) {
      taken[148] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16TypeOfExpressionE")) {
      taken[149] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16TypeOfExpressionE")) {
      taken[150] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreIncrementExpressionE")) {
      taken[151] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreIncrementExpressionE")) {
      taken[152] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreDecrementExpressionE")) {
      taken[153] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreDecrementExpressionE")) {
      taken[154] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UnaryPlusExpressionE")) {
      taken[155] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UnaryPlusExpressionE")) {
      taken[156] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20UnaryMinusExpressionE")) {
      taken[157] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20UnaryMinusExpressionE")) {
      taken[158] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TildeExpressionE")) {
      taken[159] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TildeExpressionE")) {
      taken[160] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NotExpressionE")) {
      taken[161] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NotExpressionE")) {
      taken[162] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16BinaryExpressionE")) {
      taken[163] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16BinaryExpressionE")) {
      taken[164] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ConditionalExpressionE")) {
      taken[165] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ConditionalExpressionE")) {
      taken[166] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15CommaExpressionE")) {
      taken[167] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15CommaExpressionE")) {
      taken[168] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StatementListE")) {
      taken[169] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StatementListE")) {
      taken[170] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17VariableStatementE")) {
      taken[171] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17VariableStatementE")) {
      taken[172] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23VariableDeclarationListE")) {
      taken[173] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23VariableDeclarationListE")) {
      taken[174] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14EmptyStatementE")) {
      taken[175] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14EmptyStatementE")) {
      taken[176] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11IfStatementE")) {
      taken[177] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DoWhileStatementE")) {
      taken[178] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DoWhileStatementE")) {
      taken[179] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14WhileStatementE")) {
      taken[180] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14WhileStatementE")) {
      taken[181] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ContinueStatementE")) {
      taken[182] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ContinueStatementE")) {
      taken[183] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14BreakStatementE")) {
      taken[184] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14BreakStatementE")) {
      taken[185] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ReturnStatementE")) {
      taken[186] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ReturnStatementE")) {
      taken[187] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15YieldExpressionE")) {
      taken[188] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15YieldExpressionE")) {
      taken[189] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15SwitchStatementE")) {
      taken[190] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15SwitchStatementE")) {
      taken[191] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11CaseClausesE")) {
      taken[192] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11CaseClausesE")) {
      taken[193] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10CaseClauseE")) {
      taken[194] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10CaseClauseE")) {
      taken[195] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13DefaultClauseE")) {
      taken[196] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13DefaultClauseE")) {
      taken[197] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17LabelledStatementE")) {
      taken[198] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17LabelledStatementE")) {
      taken[199] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThrowStatementE")) {
      taken[200] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThrowStatementE")) {
      taken[201] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12TryStatementE")) {
      taken[202] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12TryStatementE")) {
      taken[203] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7FinallyE")) {
      taken[204] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7FinallyE")) {
      taken[205] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FormalParameterListE")) {
      taken[206] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassElementListE")) {
      taken[207] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassElementListE")) {
      taken[208] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15NameSpaceImportE")) {
      taken[209] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15NameSpaceImportE")) {
      taken[210] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ImportSpecifierE")) {
      taken[211] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ImportSpecifierE")) {
      taken[212] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ImportsListE")) {
      taken[213] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ImportsListE")) {
      taken[214] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12NamedImportsE")) {
      taken[215] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12NamedImportsE")) {
      taken[216] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10FromClauseE")) {
      taken[217] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10FromClauseE")) {
      taken[218] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ImportClauseE")) {
      taken[219] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ImportClauseE")) {
      taken[220] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ImportDeclarationE")) {
      taken[221] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ImportDeclarationE")) {
      taken[222] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ExportSpecifierE")) {
      taken[223] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ExportSpecifierE")) {
      taken[224] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ExportsListE")) {
      taken[225] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ExportsListE")) {
      taken[226] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ExportClauseE")) {
      taken[227] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ExportClauseE")) {
      taken[228] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17DebuggerStatementE")) {
      taken[229] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17DebuggerStatementE")) {
      taken[230] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_4TypeE")) {
      taken[231] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_4TypeE")) {
      taken[232] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeAnnotationE")) {
      taken[233] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeAnnotationE")) {
      taken[234] = call;
      return true;
    }
    return false;
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExpressionStatement
  //      *ast)
  bool visit(QQmlJS::AST::ExpressionStatement *ast) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall0 call = reinterpret_cast<CuteQQmlJSImportVisitorCall0>(taken[0]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExpressionStatement
  //      *ast)
  void endVisit(QQmlJS::AST::ExpressionStatement *ast) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall1 call = reinterpret_cast<CuteQQmlJSImportVisitorCall1>(taken[1]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiProgram *a0)
  bool visit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall2 call = reinterpret_cast<CuteQQmlJSImportVisitorCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiProgram *a0)
  void endVisit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall3 call = reinterpret_cast<CuteQQmlJSImportVisitorCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectDefinition *a0)
  bool visit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall4 call = reinterpret_cast<CuteQQmlJSImportVisitorCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectDefinition
  //      *a0)
  void endVisit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall5 call = reinterpret_cast<CuteQQmlJSImportVisitorCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiInlineComponent *a0)
  bool visit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall6 call = reinterpret_cast<CuteQQmlJSImportVisitorCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiInlineComponent
  //      *a0)
  void endVisit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall7 call = reinterpret_cast<CuteQQmlJSImportVisitorCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPublicMember *a0)
  bool visit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall8 call = reinterpret_cast<CuteQQmlJSImportVisitorCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiPublicMember *a0)
  void endVisit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall9 call = reinterpret_cast<CuteQQmlJSImportVisitorCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiRequired *required)
  bool visit(QQmlJS::AST::UiRequired *required) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall10 call = reinterpret_cast<CuteQQmlJSImportVisitorCall10>(taken[10]);
      bool given = call(this, required, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(required);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiScriptBinding *a0)
  bool visit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall11 call = reinterpret_cast<CuteQQmlJSImportVisitorCall11>(taken[11]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiScriptBinding *a0)
  void endVisit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall12 call = reinterpret_cast<CuteQQmlJSImportVisitorCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiArrayBinding *a0)
  bool visit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall13 call = reinterpret_cast<CuteQQmlJSImportVisitorCall13>(taken[13]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiArrayBinding *a0)
  void endVisit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall14 call = reinterpret_cast<CuteQQmlJSImportVisitorCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiEnumDeclaration *uied)
  bool visit(QQmlJS::AST::UiEnumDeclaration *uied) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall15 call = reinterpret_cast<CuteQQmlJSImportVisitorCall15>(taken[15]);
      bool given = call(this, uied, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(uied);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionExpression
  //      *fexpr)
  bool visit(QQmlJS::AST::FunctionExpression *fexpr) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall16 call = reinterpret_cast<CuteQQmlJSImportVisitorCall16>(taken[16]);
      bool given = call(this, fexpr, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(fexpr);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionExpression
  //      *a0)
  void endVisit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall17 call = reinterpret_cast<CuteQQmlJSImportVisitorCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiSourceElement *a0)
  bool visit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall18 call = reinterpret_cast<CuteQQmlJSImportVisitorCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionDeclaration
  //      *fdecl)
  bool visit(QQmlJS::AST::FunctionDeclaration *fdecl) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall19 call = reinterpret_cast<CuteQQmlJSImportVisitorCall19>(taken[19]);
      bool given = call(this, fdecl, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(fdecl);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionDeclaration
  //      *a0)
  void endVisit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall20 call = reinterpret_cast<CuteQQmlJSImportVisitorCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassExpression *ast)
  bool visit(QQmlJS::AST::ClassExpression *ast) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall21 call = reinterpret_cast<CuteQQmlJSImportVisitorCall21>(taken[21]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassExpression *a0)
  void endVisit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall22 call = reinterpret_cast<CuteQQmlJSImportVisitorCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiImport *import)
  bool visit(QQmlJS::AST::UiImport *import) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall23 call = reinterpret_cast<CuteQQmlJSImportVisitorCall23>(taken[23]);
      bool given = call(this, import, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(import);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPragma *pragma)
  bool visit(QQmlJS::AST::UiPragma *pragma) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall24 call = reinterpret_cast<CuteQQmlJSImportVisitorCall24>(taken[24]);
      bool given = call(this, pragma, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(pragma);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassDeclaration *ast)
  bool visit(QQmlJS::AST::ClassDeclaration *ast) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall25 call = reinterpret_cast<CuteQQmlJSImportVisitorCall25>(taken[25]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassDeclaration
  //      *ast)
  void endVisit(QQmlJS::AST::ClassDeclaration *ast) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall26 call = reinterpret_cast<CuteQQmlJSImportVisitorCall26>(taken[26]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForStatement *ast)
  bool visit(QQmlJS::AST::ForStatement *ast) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall27 call = reinterpret_cast<CuteQQmlJSImportVisitorCall27>(taken[27]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForStatement *ast)
  void endVisit(QQmlJS::AST::ForStatement *ast) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall28 call = reinterpret_cast<CuteQQmlJSImportVisitorCall28>(taken[28]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForEachStatement *ast)
  bool visit(QQmlJS::AST::ForEachStatement *ast) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall29 call = reinterpret_cast<CuteQQmlJSImportVisitorCall29>(taken[29]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForEachStatement
  //      *ast)
  void endVisit(QQmlJS::AST::ForEachStatement *ast) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall30 call = reinterpret_cast<CuteQQmlJSImportVisitorCall30>(taken[30]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Block *ast)
  bool visit(QQmlJS::AST::Block *ast) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall31 call = reinterpret_cast<CuteQQmlJSImportVisitorCall31>(taken[31]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Block *ast)
  void endVisit(QQmlJS::AST::Block *ast) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall32 call = reinterpret_cast<CuteQQmlJSImportVisitorCall32>(taken[32]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::CaseBlock *ast)
  bool visit(QQmlJS::AST::CaseBlock *ast) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall33 call = reinterpret_cast<CuteQQmlJSImportVisitorCall33>(taken[33]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::CaseBlock *ast)
  void endVisit(QQmlJS::AST::CaseBlock *ast) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall34 call = reinterpret_cast<CuteQQmlJSImportVisitorCall34>(taken[34]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Catch *ast)
  bool visit(QQmlJS::AST::Catch *ast) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall35 call = reinterpret_cast<CuteQQmlJSImportVisitorCall35>(taken[35]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(ast);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Catch *ast)
  void endVisit(QQmlJS::AST::Catch *ast) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall36 call = reinterpret_cast<CuteQQmlJSImportVisitorCall36>(taken[36]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::WithStatement
  //      *withStatement)
  bool visit(QQmlJS::AST::WithStatement *withStatement) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall37 call = reinterpret_cast<CuteQQmlJSImportVisitorCall37>(taken[37]);
      bool given = call(this, withStatement, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(withStatement);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::WithStatement *ast)
  void endVisit(QQmlJS::AST::WithStatement *ast) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall38 call = reinterpret_cast<CuteQQmlJSImportVisitorCall38>(taken[38]);
      call(this, ast, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(ast);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FormalParameterList
  //      *fpl)
  bool visit(QQmlJS::AST::FormalParameterList *fpl) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall39 call = reinterpret_cast<CuteQQmlJSImportVisitorCall39>(taken[39]);
      bool given = call(this, fpl, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(fpl);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectBinding *uiob)
  bool visit(QQmlJS::AST::UiObjectBinding *uiob) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall40 call = reinterpret_cast<CuteQQmlJSImportVisitorCall40>(taken[40]);
      bool given = call(this, uiob, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(uiob);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectBinding
  //      *uiob)
  void endVisit(QQmlJS::AST::UiObjectBinding *uiob) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall41 call = reinterpret_cast<CuteQQmlJSImportVisitorCall41>(taken[41]);
      call(this, uiob, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(uiob);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExportDeclaration *exp)
  bool visit(QQmlJS::AST::ExportDeclaration *exp) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall42 call = reinterpret_cast<CuteQQmlJSImportVisitorCall42>(taken[42]);
      bool given = call(this, exp, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(exp);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExportDeclaration
  //      *exp)
  void endVisit(QQmlJS::AST::ExportDeclaration *exp) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall43 call = reinterpret_cast<CuteQQmlJSImportVisitorCall43>(taken[43]);
      call(this, exp, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(exp);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ESModule *module)
  bool visit(QQmlJS::AST::ESModule *module) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall44 call = reinterpret_cast<CuteQQmlJSImportVisitorCall44>(taken[44]);
      bool given = call(this, module, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(module);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ESModule *module)
  void endVisit(QQmlJS::AST::ESModule *module) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall45 call = reinterpret_cast<CuteQQmlJSImportVisitorCall45>(taken[45]);
      call(this, module, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(module);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Program *program)
  bool visit(QQmlJS::AST::Program *program) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall46 call = reinterpret_cast<CuteQQmlJSImportVisitorCall46>(taken[46]);
      bool given = call(this, program, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(program);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Program *program)
  void endVisit(QQmlJS::AST::Program *program) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall47 call = reinterpret_cast<CuteQQmlJSImportVisitorCall47>(taken[47]);
      call(this, program, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(program);
  }

  //  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FieldMemberExpression
  //      *a0)
  void endVisit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall48 call = reinterpret_cast<CuteQQmlJSImportVisitorCall48>(taken[48]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::endVisit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IdentifierExpression
  //      *idexp)
  bool visit(QQmlJS::AST::IdentifierExpression *idexp) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall49 call = reinterpret_cast<CuteQQmlJSImportVisitorCall49>(taken[49]);
      bool given = call(this, idexp, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(idexp);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::PatternElement *a0)
  bool visit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall50 call = reinterpret_cast<CuteQQmlJSImportVisitorCall50>(taken[50]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IfStatement *a0)
  bool visit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall51 call = reinterpret_cast<CuteQQmlJSImportVisitorCall51>(taken[51]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJSImportVisitor::visit(a0);
  }

  //  void QQmlJSImportVisitor::throwRecursionDepthError()
  void throwRecursionDepthError() override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall52 call = reinterpret_cast<CuteQQmlJSImportVisitorCall52>(taken[52]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::throwRecursionDepthError();
  }

  //  void QQmlJSImportVisitor::leaveEnvironment()
  void leaveEnvironment() override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall53 call = reinterpret_cast<CuteQQmlJSImportVisitorCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::leaveEnvironment();
  }

  //  void QQmlJSImportVisitor::handleLiteralBinding(const
  //      QQmlJSMetaPropertyBinding &a0, const QQmlJS::AST::UiPublicMember
  //      *a1)
  void handleLiteralBinding(
      const QQmlJSMetaPropertyBinding &a0,
      const QQmlJS::AST::UiPublicMember *a1) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall54 call = reinterpret_cast<CuteQQmlJSImportVisitorCall54>(taken[54]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSImportVisitor::handleLiteralBinding(a0, a1);
  }

  //  bool QQmlJS::AST::Visitor::preVisit(Node *a0)
  bool preVisit(QQmlJS::AST::Node *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall55 call = reinterpret_cast<CuteQQmlJSImportVisitorCall55>(taken[55]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::preVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::postVisit(Node *a0)
  void postVisit(QQmlJS::AST::Node *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall56 call = reinterpret_cast<CuteQQmlJSImportVisitorCall56>(taken[56]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::postVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
  bool visit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall57 call = reinterpret_cast<CuteQQmlJSImportVisitorCall57>(taken[57]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
  void endVisit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall58 call = reinterpret_cast<CuteQQmlJSImportVisitorCall58>(taken[58]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
  bool visit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall59 call = reinterpret_cast<CuteQQmlJSImportVisitorCall59>(taken[59]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
  void endVisit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall60 call = reinterpret_cast<CuteQQmlJSImportVisitorCall60>(taken[60]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
  void endVisit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall61 call = reinterpret_cast<CuteQQmlJSImportVisitorCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
  void endVisit(QQmlJS::AST::UiImport *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall62 call = reinterpret_cast<CuteQQmlJSImportVisitorCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
  void endVisit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall63 call = reinterpret_cast<CuteQQmlJSImportVisitorCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
  bool visit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall64 call = reinterpret_cast<CuteQQmlJSImportVisitorCall64>(taken[64]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
  void endVisit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall65 call = reinterpret_cast<CuteQQmlJSImportVisitorCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
  bool visit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall66 call = reinterpret_cast<CuteQQmlJSImportVisitorCall66>(taken[66]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
  void endVisit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall67 call = reinterpret_cast<CuteQQmlJSImportVisitorCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
  bool visit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall68 call = reinterpret_cast<CuteQQmlJSImportVisitorCall68>(taken[68]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
  void endVisit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall69 call = reinterpret_cast<CuteQQmlJSImportVisitorCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
  bool visit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall70 call = reinterpret_cast<CuteQQmlJSImportVisitorCall70>(taken[70]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
  void endVisit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall71 call = reinterpret_cast<CuteQQmlJSImportVisitorCall71>(taken[71]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
  bool visit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall72 call = reinterpret_cast<CuteQQmlJSImportVisitorCall72>(taken[72]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
  void endVisit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall73 call = reinterpret_cast<CuteQQmlJSImportVisitorCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
  void endVisit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall74 call = reinterpret_cast<CuteQQmlJSImportVisitorCall74>(taken[74]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
  bool visit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall75 call = reinterpret_cast<CuteQQmlJSImportVisitorCall75>(taken[75]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
  void endVisit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall76 call = reinterpret_cast<CuteQQmlJSImportVisitorCall76>(taken[76]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
  bool visit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall77 call = reinterpret_cast<CuteQQmlJSImportVisitorCall77>(taken[77]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
  void endVisit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall78 call = reinterpret_cast<CuteQQmlJSImportVisitorCall78>(taken[78]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
  bool visit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall79 call = reinterpret_cast<CuteQQmlJSImportVisitorCall79>(taken[79]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
  void endVisit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall80 call = reinterpret_cast<CuteQQmlJSImportVisitorCall80>(taken[80]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
  bool visit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall81 call = reinterpret_cast<CuteQQmlJSImportVisitorCall81>(taken[81]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
  void endVisit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall82 call = reinterpret_cast<CuteQQmlJSImportVisitorCall82>(taken[82]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
  void endVisit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall83 call = reinterpret_cast<CuteQQmlJSImportVisitorCall83>(taken[83]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
  bool visit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall84 call = reinterpret_cast<CuteQQmlJSImportVisitorCall84>(taken[84]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
  void endVisit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall85 call = reinterpret_cast<CuteQQmlJSImportVisitorCall85>(taken[85]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
  bool visit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall86 call = reinterpret_cast<CuteQQmlJSImportVisitorCall86>(taken[86]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
  void endVisit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall87 call = reinterpret_cast<CuteQQmlJSImportVisitorCall87>(taken[87]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
  void endVisit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall88 call = reinterpret_cast<CuteQQmlJSImportVisitorCall88>(taken[88]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
  bool visit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall89 call = reinterpret_cast<CuteQQmlJSImportVisitorCall89>(taken[89]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
  void endVisit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall90 call = reinterpret_cast<CuteQQmlJSImportVisitorCall90>(taken[90]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
  bool visit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall91 call = reinterpret_cast<CuteQQmlJSImportVisitorCall91>(taken[91]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
  void endVisit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall92 call = reinterpret_cast<CuteQQmlJSImportVisitorCall92>(taken[92]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
  bool visit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall93 call = reinterpret_cast<CuteQQmlJSImportVisitorCall93>(taken[93]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
  void endVisit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall94 call = reinterpret_cast<CuteQQmlJSImportVisitorCall94>(taken[94]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
  bool visit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall95 call = reinterpret_cast<CuteQQmlJSImportVisitorCall95>(taken[95]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
  void endVisit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall96 call = reinterpret_cast<CuteQQmlJSImportVisitorCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
  bool visit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall97 call = reinterpret_cast<CuteQQmlJSImportVisitorCall97>(taken[97]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
  void endVisit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall98 call = reinterpret_cast<CuteQQmlJSImportVisitorCall98>(taken[98]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
  bool visit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall99 call = reinterpret_cast<CuteQQmlJSImportVisitorCall99>(taken[99]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
  void endVisit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall100 call = reinterpret_cast<CuteQQmlJSImportVisitorCall100>(taken[100]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
  bool visit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall101 call = reinterpret_cast<CuteQQmlJSImportVisitorCall101>(taken[101]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
  void endVisit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall102 call = reinterpret_cast<CuteQQmlJSImportVisitorCall102>(taken[102]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
  bool visit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall103 call = reinterpret_cast<CuteQQmlJSImportVisitorCall103>(taken[103]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
  void endVisit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall104 call = reinterpret_cast<CuteQQmlJSImportVisitorCall104>(taken[104]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
  bool visit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall105 call = reinterpret_cast<CuteQQmlJSImportVisitorCall105>(taken[105]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
  void endVisit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall106 call = reinterpret_cast<CuteQQmlJSImportVisitorCall106>(taken[106]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
  bool visit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall107 call = reinterpret_cast<CuteQQmlJSImportVisitorCall107>(taken[107]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
  void endVisit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall108 call = reinterpret_cast<CuteQQmlJSImportVisitorCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
  bool visit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall109 call = reinterpret_cast<CuteQQmlJSImportVisitorCall109>(taken[109]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
  void endVisit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall110 call = reinterpret_cast<CuteQQmlJSImportVisitorCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
  bool visit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall111 call = reinterpret_cast<CuteQQmlJSImportVisitorCall111>(taken[111]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
  void endVisit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall112 call = reinterpret_cast<CuteQQmlJSImportVisitorCall112>(taken[112]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
  void endVisit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall113 call = reinterpret_cast<CuteQQmlJSImportVisitorCall113>(taken[113]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
  bool visit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall114 call = reinterpret_cast<CuteQQmlJSImportVisitorCall114>(taken[114]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
  void endVisit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall115 call = reinterpret_cast<CuteQQmlJSImportVisitorCall115>(taken[115]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Elision *a0)
  bool visit(QQmlJS::AST::Elision *a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall116 call = reinterpret_cast<CuteQQmlJSImportVisitorCall116>(taken[116]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
  void endVisit(QQmlJS::AST::Elision *a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall117 call = reinterpret_cast<CuteQQmlJSImportVisitorCall117>(taken[117]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
  bool visit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall118 call = reinterpret_cast<CuteQQmlJSImportVisitorCall118>(taken[118]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
  void endVisit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall119 call = reinterpret_cast<CuteQQmlJSImportVisitorCall119>(taken[119]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
  bool visit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall120 call = reinterpret_cast<CuteQQmlJSImportVisitorCall120>(taken[120]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
  void endVisit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall121 call = reinterpret_cast<CuteQQmlJSImportVisitorCall121>(taken[121]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall122 call = reinterpret_cast<CuteQQmlJSImportVisitorCall122>(taken[122]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall123 call = reinterpret_cast<CuteQQmlJSImportVisitorCall123>(taken[123]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall124 call = reinterpret_cast<CuteQQmlJSImportVisitorCall124>(taken[124]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall125 call = reinterpret_cast<CuteQQmlJSImportVisitorCall125>(taken[125]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
  bool visit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall126 call = reinterpret_cast<CuteQQmlJSImportVisitorCall126>(taken[126]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
  void endVisit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall127 call = reinterpret_cast<CuteQQmlJSImportVisitorCall127>(taken[127]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
  bool visit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall128 call = reinterpret_cast<CuteQQmlJSImportVisitorCall128>(taken[128]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
  void endVisit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall129 call = reinterpret_cast<CuteQQmlJSImportVisitorCall129>(taken[129]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
  bool visit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall130 call = reinterpret_cast<CuteQQmlJSImportVisitorCall130>(taken[130]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
  bool visit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall131 call = reinterpret_cast<CuteQQmlJSImportVisitorCall131>(taken[131]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
  void endVisit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall132 call = reinterpret_cast<CuteQQmlJSImportVisitorCall132>(taken[132]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
  bool visit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall133 call = reinterpret_cast<CuteQQmlJSImportVisitorCall133>(taken[133]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
  void endVisit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[134]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall134 call = reinterpret_cast<CuteQQmlJSImportVisitorCall134>(taken[134]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
  bool visit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[135]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall135 call = reinterpret_cast<CuteQQmlJSImportVisitorCall135>(taken[135]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
  void endVisit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[136]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall136 call = reinterpret_cast<CuteQQmlJSImportVisitorCall136>(taken[136]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
  bool visit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[137]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall137 call = reinterpret_cast<CuteQQmlJSImportVisitorCall137>(taken[137]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
  void endVisit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[138]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall138 call = reinterpret_cast<CuteQQmlJSImportVisitorCall138>(taken[138]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
  bool visit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[139]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall139 call = reinterpret_cast<CuteQQmlJSImportVisitorCall139>(taken[139]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
  void endVisit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[140]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall140 call = reinterpret_cast<CuteQQmlJSImportVisitorCall140>(taken[140]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
  bool visit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[141]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall141 call = reinterpret_cast<CuteQQmlJSImportVisitorCall141>(taken[141]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[142]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall142 call = reinterpret_cast<CuteQQmlJSImportVisitorCall142>(taken[142]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
  bool visit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[143]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall143 call = reinterpret_cast<CuteQQmlJSImportVisitorCall143>(taken[143]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[144]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall144 call = reinterpret_cast<CuteQQmlJSImportVisitorCall144>(taken[144]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
  bool visit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[145]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall145 call = reinterpret_cast<CuteQQmlJSImportVisitorCall145>(taken[145]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
  void endVisit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[146]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall146 call = reinterpret_cast<CuteQQmlJSImportVisitorCall146>(taken[146]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
  bool visit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[147]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall147 call = reinterpret_cast<CuteQQmlJSImportVisitorCall147>(taken[147]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
  void endVisit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[148]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall148 call = reinterpret_cast<CuteQQmlJSImportVisitorCall148>(taken[148]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
  bool visit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[149]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall149 call = reinterpret_cast<CuteQQmlJSImportVisitorCall149>(taken[149]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
  void endVisit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[150]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall150 call = reinterpret_cast<CuteQQmlJSImportVisitorCall150>(taken[150]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
  bool visit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[151]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall151 call = reinterpret_cast<CuteQQmlJSImportVisitorCall151>(taken[151]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[152]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall152 call = reinterpret_cast<CuteQQmlJSImportVisitorCall152>(taken[152]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
  bool visit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[153]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall153 call = reinterpret_cast<CuteQQmlJSImportVisitorCall153>(taken[153]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[154]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall154 call = reinterpret_cast<CuteQQmlJSImportVisitorCall154>(taken[154]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
  bool visit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[155]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall155 call = reinterpret_cast<CuteQQmlJSImportVisitorCall155>(taken[155]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[156]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall156 call = reinterpret_cast<CuteQQmlJSImportVisitorCall156>(taken[156]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
  bool visit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[157]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall157 call = reinterpret_cast<CuteQQmlJSImportVisitorCall157>(taken[157]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[158]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall158 call = reinterpret_cast<CuteQQmlJSImportVisitorCall158>(taken[158]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
  bool visit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[159]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall159 call = reinterpret_cast<CuteQQmlJSImportVisitorCall159>(taken[159]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
  void endVisit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[160]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall160 call = reinterpret_cast<CuteQQmlJSImportVisitorCall160>(taken[160]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
  bool visit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[161]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall161 call = reinterpret_cast<CuteQQmlJSImportVisitorCall161>(taken[161]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
  void endVisit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[162]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall162 call = reinterpret_cast<CuteQQmlJSImportVisitorCall162>(taken[162]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
  bool visit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[163]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall163 call = reinterpret_cast<CuteQQmlJSImportVisitorCall163>(taken[163]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
  void endVisit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[164]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall164 call = reinterpret_cast<CuteQQmlJSImportVisitorCall164>(taken[164]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
  bool visit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[165]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall165 call = reinterpret_cast<CuteQQmlJSImportVisitorCall165>(taken[165]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
  void endVisit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[166]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall166 call = reinterpret_cast<CuteQQmlJSImportVisitorCall166>(taken[166]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
  bool visit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[167]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall167 call = reinterpret_cast<CuteQQmlJSImportVisitorCall167>(taken[167]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
  void endVisit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[168]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall168 call = reinterpret_cast<CuteQQmlJSImportVisitorCall168>(taken[168]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
  bool visit(QQmlJS::AST::StatementList *a0) override {
    if (taken[169]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall169 call = reinterpret_cast<CuteQQmlJSImportVisitorCall169>(taken[169]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
  void endVisit(QQmlJS::AST::StatementList *a0) override {
    if (taken[170]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall170 call = reinterpret_cast<CuteQQmlJSImportVisitorCall170>(taken[170]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
  bool visit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[171]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall171 call = reinterpret_cast<CuteQQmlJSImportVisitorCall171>(taken[171]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
  void endVisit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[172]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall172 call = reinterpret_cast<CuteQQmlJSImportVisitorCall172>(taken[172]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
  bool visit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[173]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall173 call = reinterpret_cast<CuteQQmlJSImportVisitorCall173>(taken[173]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
  void endVisit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[174]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall174 call = reinterpret_cast<CuteQQmlJSImportVisitorCall174>(taken[174]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
  bool visit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[175]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall175 call = reinterpret_cast<CuteQQmlJSImportVisitorCall175>(taken[175]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
  void endVisit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[176]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall176 call = reinterpret_cast<CuteQQmlJSImportVisitorCall176>(taken[176]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
  void endVisit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[177]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall177 call = reinterpret_cast<CuteQQmlJSImportVisitorCall177>(taken[177]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
  bool visit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[178]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall178 call = reinterpret_cast<CuteQQmlJSImportVisitorCall178>(taken[178]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
  void endVisit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[179]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall179 call = reinterpret_cast<CuteQQmlJSImportVisitorCall179>(taken[179]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
  bool visit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[180]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall180 call = reinterpret_cast<CuteQQmlJSImportVisitorCall180>(taken[180]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
  void endVisit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[181]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall181 call = reinterpret_cast<CuteQQmlJSImportVisitorCall181>(taken[181]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
  bool visit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[182]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall182 call = reinterpret_cast<CuteQQmlJSImportVisitorCall182>(taken[182]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
  void endVisit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[183]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall183 call = reinterpret_cast<CuteQQmlJSImportVisitorCall183>(taken[183]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
  bool visit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[184]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall184 call = reinterpret_cast<CuteQQmlJSImportVisitorCall184>(taken[184]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
  void endVisit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[185]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall185 call = reinterpret_cast<CuteQQmlJSImportVisitorCall185>(taken[185]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
  bool visit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[186]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall186 call = reinterpret_cast<CuteQQmlJSImportVisitorCall186>(taken[186]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
  void endVisit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[187]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall187 call = reinterpret_cast<CuteQQmlJSImportVisitorCall187>(taken[187]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
  bool visit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[188]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall188 call = reinterpret_cast<CuteQQmlJSImportVisitorCall188>(taken[188]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
  void endVisit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[189]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall189 call = reinterpret_cast<CuteQQmlJSImportVisitorCall189>(taken[189]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
  bool visit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[190]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall190 call = reinterpret_cast<CuteQQmlJSImportVisitorCall190>(taken[190]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
  void endVisit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[191]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall191 call = reinterpret_cast<CuteQQmlJSImportVisitorCall191>(taken[191]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
  bool visit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[192]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall192 call = reinterpret_cast<CuteQQmlJSImportVisitorCall192>(taken[192]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
  void endVisit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[193]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall193 call = reinterpret_cast<CuteQQmlJSImportVisitorCall193>(taken[193]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
  bool visit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[194]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall194 call = reinterpret_cast<CuteQQmlJSImportVisitorCall194>(taken[194]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
  void endVisit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[195]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall195 call = reinterpret_cast<CuteQQmlJSImportVisitorCall195>(taken[195]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
  bool visit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[196]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall196 call = reinterpret_cast<CuteQQmlJSImportVisitorCall196>(taken[196]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
  void endVisit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[197]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall197 call = reinterpret_cast<CuteQQmlJSImportVisitorCall197>(taken[197]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
  bool visit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[198]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall198 call = reinterpret_cast<CuteQQmlJSImportVisitorCall198>(taken[198]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
  void endVisit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[199]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall199 call = reinterpret_cast<CuteQQmlJSImportVisitorCall199>(taken[199]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
  bool visit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[200]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall200 call = reinterpret_cast<CuteQQmlJSImportVisitorCall200>(taken[200]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
  void endVisit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[201]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall201 call = reinterpret_cast<CuteQQmlJSImportVisitorCall201>(taken[201]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
  bool visit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[202]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall202 call = reinterpret_cast<CuteQQmlJSImportVisitorCall202>(taken[202]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
  void endVisit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[203]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall203 call = reinterpret_cast<CuteQQmlJSImportVisitorCall203>(taken[203]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Finally *a0)
  bool visit(QQmlJS::AST::Finally *a0) override {
    if (taken[204]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall204 call = reinterpret_cast<CuteQQmlJSImportVisitorCall204>(taken[204]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
  void endVisit(QQmlJS::AST::Finally *a0) override {
    if (taken[205]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall205 call = reinterpret_cast<CuteQQmlJSImportVisitorCall205>(taken[205]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
  void endVisit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[206]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall206 call = reinterpret_cast<CuteQQmlJSImportVisitorCall206>(taken[206]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
  bool visit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[207]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall207 call = reinterpret_cast<CuteQQmlJSImportVisitorCall207>(taken[207]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
  void endVisit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[208]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall208 call = reinterpret_cast<CuteQQmlJSImportVisitorCall208>(taken[208]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
  bool visit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[209]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall209 call = reinterpret_cast<CuteQQmlJSImportVisitorCall209>(taken[209]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
  void endVisit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[210]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall210 call = reinterpret_cast<CuteQQmlJSImportVisitorCall210>(taken[210]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
  bool visit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[211]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall211 call = reinterpret_cast<CuteQQmlJSImportVisitorCall211>(taken[211]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
  void endVisit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[212]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall212 call = reinterpret_cast<CuteQQmlJSImportVisitorCall212>(taken[212]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
  bool visit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[213]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall213 call = reinterpret_cast<CuteQQmlJSImportVisitorCall213>(taken[213]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
  void endVisit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[214]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall214 call = reinterpret_cast<CuteQQmlJSImportVisitorCall214>(taken[214]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
  bool visit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[215]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall215 call = reinterpret_cast<CuteQQmlJSImportVisitorCall215>(taken[215]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
  void endVisit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[216]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall216 call = reinterpret_cast<CuteQQmlJSImportVisitorCall216>(taken[216]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
  bool visit(QQmlJS::AST::FromClause *a0) override {
    if (taken[217]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall217 call = reinterpret_cast<CuteQQmlJSImportVisitorCall217>(taken[217]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
  void endVisit(QQmlJS::AST::FromClause *a0) override {
    if (taken[218]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall218 call = reinterpret_cast<CuteQQmlJSImportVisitorCall218>(taken[218]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
  bool visit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[219]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall219 call = reinterpret_cast<CuteQQmlJSImportVisitorCall219>(taken[219]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
  void endVisit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[220]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall220 call = reinterpret_cast<CuteQQmlJSImportVisitorCall220>(taken[220]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
  bool visit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[221]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall221 call = reinterpret_cast<CuteQQmlJSImportVisitorCall221>(taken[221]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
  void endVisit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[222]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall222 call = reinterpret_cast<CuteQQmlJSImportVisitorCall222>(taken[222]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
  bool visit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[223]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall223 call = reinterpret_cast<CuteQQmlJSImportVisitorCall223>(taken[223]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
  void endVisit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[224]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall224 call = reinterpret_cast<CuteQQmlJSImportVisitorCall224>(taken[224]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
  bool visit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[225]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall225 call = reinterpret_cast<CuteQQmlJSImportVisitorCall225>(taken[225]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
  void endVisit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[226]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall226 call = reinterpret_cast<CuteQQmlJSImportVisitorCall226>(taken[226]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
  bool visit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[227]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall227 call = reinterpret_cast<CuteQQmlJSImportVisitorCall227>(taken[227]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
  void endVisit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[228]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall228 call = reinterpret_cast<CuteQQmlJSImportVisitorCall228>(taken[228]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
  bool visit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[229]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall229 call = reinterpret_cast<CuteQQmlJSImportVisitorCall229>(taken[229]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
  void endVisit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[230]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall230 call = reinterpret_cast<CuteQQmlJSImportVisitorCall230>(taken[230]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Type *a0)
  bool visit(QQmlJS::AST::Type *a0) override {
    if (taken[231]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall231 call = reinterpret_cast<CuteQQmlJSImportVisitorCall231>(taken[231]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Type *a0)
  void endVisit(QQmlJS::AST::Type *a0) override {
    if (taken[232]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall232 call = reinterpret_cast<CuteQQmlJSImportVisitorCall232>(taken[232]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
  bool visit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[233]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall233 call = reinterpret_cast<CuteQQmlJSImportVisitorCall233>(taken[233]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
  void endVisit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[234]) {
      int handled = 0;
      CuteQQmlJSImportVisitorCall234 call = reinterpret_cast<CuteQQmlJSImportVisitorCall234>(taken[234]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }
};

//  QQmlJSImportVisitor::QQmlJSImportVisitor(QQmlJSImporter *importer,
//      QQmlJSLogger *logger, const QString &implicitImportDirectory, const
//      QStringList &qmldirFiles)
extern "C" Q_DECL_EXPORT
QQmlJSImportVisitor *ritual_ZN19QQmlJSImportVisitorC1EP14QQmlJSImporterP12QQmlJSLoggerRK7QStringRK5QListIS4_E(
    QQmlJSImporter *importer,
    QQmlJSLogger *logger,
    const QString *implicitImportDirectory,
    const QList<QString> *qmldirFiles) {
  return new CuteQQmlJSImportVisitor(
      importer,
      logger,
      *implicitImportDirectory,
      *qmldirFiles);
}

//  QQmlJSImportVisitor::~QQmlJSImportVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitorD1Ev(QQmlJSImportVisitor *self) {
  delete self;
}

//  const QQmlJSLogger *QQmlJSImportVisitor::logger() const
extern "C" Q_DECL_EXPORT
const QQmlJSLogger *ritual_ZNK19QQmlJSImportVisitor6loggerEv(
    const QQmlJSImportVisitor *self) {
  return self->logger();
}

//  QQmlJSLogger *QQmlJSImportVisitor::logger()
extern "C" Q_DECL_EXPORT
QQmlJSLogger *ritual_ZN19QQmlJSImportVisitor6loggerEv(
    QQmlJSImportVisitor *self) {
  return self->logger();
}

//  QQmlJSImporter::ImportedTypes QQmlJSImportVisitor::imports() const
extern "C" Q_DECL_EXPORT
QQmlJSImporter::ImportedTypes *ritual_ZNK19QQmlJSImportVisitor7importsEv(
    const QQmlJSImportVisitor *self) {
  return new QQmlJSImporter::ImportedTypes(self->imports());
}

//  QQmlJSScopesById QQmlJSImportVisitor::addressableScopes() const
extern "C" Q_DECL_EXPORT
QQmlJSScopesById *ritual_ZNK19QQmlJSImportVisitor17addressableScopesEv(
    const QQmlJSImportVisitor *self) {
  return new QQmlJSScopesById(self->addressableScopes());
}

//  QString QQmlJSImportVisitor::implicitImportDirectory(const QString
//      &localFile, const QQmlJSResourceFileMapper *mapper)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSImportVisitor23implicitImportDirectoryERK7QStringPK24QQmlJSResourceFileMapper(
    const QString *localFile,
    const QQmlJSResourceFileMapper *mapper) {
  return new QString(
      QQmlJSImportVisitor::implicitImportDirectory(
          *localFile,
          mapper));
}

//  QQmlJSImporter *QQmlJSImportVisitor::importer()
extern "C" Q_DECL_EXPORT
QQmlJSImporter *ritual_ZN19QQmlJSImportVisitor8importerEv(
    QQmlJSImportVisitor *self) {
  return self->importer();
}

//  const QQmlJSImporter *QQmlJSImportVisitor::importer() const
extern "C" Q_DECL_EXPORT
const QQmlJSImporter *ritual_ZNK19QQmlJSImportVisitor8importerEv(
    const QQmlJSImportVisitor *self) {
  return self->importer();
}

//  QStringList QQmlJSImportVisitor::seenModuleQualifiers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QQmlJSImportVisitor20seenModuleQualifiersEv(
    const QQmlJSImportVisitor *self) {
  return new QList<QString>(self->seenModuleQualifiers());
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExpressionStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19ExpressionStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExpressionStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19ExpressionStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9UiProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9UiProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiInlineComponentE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17UiInlineComponentE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiRequired *required)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST10UiRequiredE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiRequired *required) {
  return self->visit(required);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiArrayBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiArrayBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiEnumDeclaration *uied)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiEnumDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *uied) {
  return self->visit(uied);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionExpression *fexpr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionExpression *fexpr) {
  return self->visit(fexpr);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiSourceElementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return self->visit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionDeclaration *fdecl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionDeclaration *fdecl) {
  return self->visit(fdecl);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19FunctionDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15ClassExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassExpression *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15ClassExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiImport *import)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiImportE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiImport *import) {
  return self->visit(import);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPragma *pragma)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiPragmaE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiPragma *pragma) {
  return self->visit(pragma);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ClassDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassDeclaration *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ClassDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST12ForStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForStatement *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST12ForStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForStatement *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForEachStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ForEachStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForEachStatement *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForEachStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ForEachStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForEachStatement *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5BlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Block *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5BlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Block *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9CaseBlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::CaseBlock *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9CaseBlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::CaseBlock *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5CatchE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Catch *ast) {
  return self->visit(ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5CatchE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Catch *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::WithStatement
//      *withStatement)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST13WithStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::WithStatement *withStatement) {
  return self->visit(withStatement);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::WithStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST13WithStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::WithStatement *ast) {
  self->endVisit(ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FormalParameterList *fpl)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FormalParameterListE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FormalParameterList *fpl) {
  return self->visit(fpl);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectBinding *uiob)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiObjectBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectBinding *uiob) {
  return self->visit(uiob);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectBinding *uiob)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiObjectBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectBinding *uiob) {
  self->endVisit(uiob);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExportDeclaration *exp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17ExportDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExportDeclaration *exp) {
  return self->visit(exp);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExportDeclaration *exp)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17ExportDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExportDeclaration *exp) {
  self->endVisit(exp);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ESModule *module)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8ESModuleE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ESModule *module) {
  return self->visit(module);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ESModule *module)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST8ESModuleE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ESModule *module) {
  self->endVisit(module);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Program *program)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST7ProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Program *program) {
  return self->visit(program);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Program *program)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST7ProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Program *program) {
  self->endVisit(program);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FieldMemberExpression
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IdentifierExpression *idexp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST20IdentifierExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::IdentifierExpression *idexp) {
  return self->visit(idexp);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14PatternElementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return self->visit(a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST11IfStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJSImportVisitor::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor24throwRecursionDepthErrorEv(
    QQmlJSImportVisitor *self) {
  self->throwRecursionDepthError();
}

//  void QQmlJSImportVisitor::createAttachedAndGroupedScopes(QQmlJS::AST::UiQ
//      ualifiedId *propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor30createAttachedAndGroupedScopesEPN6QQmlJS3AST13UiQualifiedIdE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiQualifiedId *propertyName) {
  self->createAttachedAndGroupedScopes(propertyName);
}

//  int QQmlJSImportVisitor::openAttachedAndGroupedScopes(QQmlJS::AST::UiQual
//      ifiedId *propertyName)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlJSImportVisitor28openAttachedAndGroupedScopesEPN6QQmlJS3AST13UiQualifiedIdE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiQualifiedId *propertyName) {
  return self->openAttachedAndGroupedScopes(propertyName);
}

//  void QQmlJSImportVisitor::forgetFunctionExpression(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor24forgetFunctionExpressionERK7QString(
    QQmlJSImportVisitor *self,
    const QString *name) {
  self->forgetFunctionExpression(*name);
}

//  void QQmlJSImportVisitor::populateRuntimeFunctionIndicesForDocument()
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQmlJSImportVisitor41populateRuntimeFunctionIndicesForDocumentEv(
    const QQmlJSImportVisitor *self) {
  self->populateRuntimeFunctionIndicesForDocument();
}

//  void QQmlJSImportVisitor::enterEnvironment(QQmlJSScope::ScopeType type,
//      const QString &name, const QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor16enterEnvironmentEN6QQmlSA9ScopeTypeERK7QStringRKN6QQmlJS14SourceLocationE(
    QQmlJSImportVisitor *self,
    QQmlJSScope::ScopeType type,
    const QString *name,
    const QQmlJS::SourceLocation *location) {
  self->enterEnvironment(type, *name, *location);
}

//  bool
//      QQmlJSImportVisitor::enterEnvironmentNonUnique(QQmlJSScope::ScopeType
//      type, const QString &name, const QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSImportVisitor25enterEnvironmentNonUniqueEN6QQmlSA9ScopeTypeERK7QStringRKN6QQmlJS14SourceLocationE(
    QQmlJSImportVisitor *self,
    QQmlJSScope::ScopeType type,
    const QString *name,
    const QQmlJS::SourceLocation *location) {
  return self->enterEnvironmentNonUnique(type, *name, *location);
}

//  void QQmlJSImportVisitor::leaveEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor16leaveEnvironmentEv(
    QQmlJSImportVisitor *self) {
  self->leaveEnvironment();
}

//  QList<QQmlJSAnnotation>
//      QQmlJSImportVisitor::parseAnnotations(QQmlJS::AST::UiAnnotationList
//      *list)
extern "C" Q_DECL_EXPORT
QList<QQmlJSAnnotation> *ritual_ZN19QQmlJSImportVisitor16parseAnnotationsEPN6QQmlJS3AST16UiAnnotationListE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiAnnotationList *list) {
  return new QList<QQmlJSAnnotation>(self->parseAnnotations(list));
}

//  void QQmlJSImportVisitor::setAllBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor14setAllBindingsEv(
    QQmlJSImportVisitor *self) {
  self->setAllBindings();
}

//  void QQmlJSImportVisitor::addDefaultProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor20addDefaultPropertiesEv(
    QQmlJSImportVisitor *self) {
  self->addDefaultProperties();
}

//  void QQmlJSImportVisitor::processDefaultProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor24processDefaultPropertiesEv(
    QQmlJSImportVisitor *self) {
  self->processDefaultProperties();
}

//  void QQmlJSImportVisitor::processPropertyBindings()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor23processPropertyBindingsEv(
    QQmlJSImportVisitor *self) {
  self->processPropertyBindings();
}

//  void QQmlJSImportVisitor::checkRequiredProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor23checkRequiredPropertiesEv(
    QQmlJSImportVisitor *self) {
  self->checkRequiredProperties();
}

//  void QQmlJSImportVisitor::processPropertyTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor20processPropertyTypesEv(
    QQmlJSImportVisitor *self) {
  self->processPropertyTypes();
}

//  void QQmlJSImportVisitor::processMethodTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor18processMethodTypesEv(
    QQmlJSImportVisitor *self) {
  self->processMethodTypes();
}

//  void QQmlJSImportVisitor::processPropertyBindingObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor29processPropertyBindingObjectsEv(
    QQmlJSImportVisitor *self) {
  self->processPropertyBindingObjects();
}

//  void QQmlJSImportVisitor::flushPendingSignalParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor28flushPendingSignalParametersEv(
    QQmlJSImportVisitor *self) {
  self->flushPendingSignalParameters();
}

//  bool QQmlJSImportVisitor::rootScopeIsValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSImportVisitor16rootScopeIsValidEv(
    const QQmlJSImportVisitor *self) {
  return self->rootScopeIsValid();
}

//  BindingExpressionParseResult
//      QQmlJSImportVisitor::parseBindingExpression(const QString &name,
//      const QQmlJS::AST::Statement *statement, const
//      QQmlJS::AST::UiPublicMember *associatedPropertyDefinition)
extern "C" Q_DECL_EXPORT
QQmlJSImportVisitor::BindingExpressionParseResult ritual_ZN19QQmlJSImportVisitor22parseBindingExpressionERK7QStringPKN6QQmlJS3AST9StatementEPKNS4_14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    const QString *name,
    const QQmlJS::AST::Statement *statement,
    const QQmlJS::AST::UiPublicMember *associatedPropertyDefinition) {
  return self->parseBindingExpression(
      *name,
      statement,
      associatedPropertyDefinition);
}

//  bool QQmlJSImportVisitor::isImportPrefix(QString prefix) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSImportVisitor14isImportPrefixE7QString(
    const QQmlJSImportVisitor *self,
    const QString *prefix) {
  return self->isImportPrefix(*prefix);
}

//  void QQmlJSImportVisitor::importBaseModules()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor17importBaseModulesEv(
    QQmlJSImportVisitor *self) {
  self->importBaseModules();
}

//  void QQmlJSImportVisitor::resolveAliases()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor14resolveAliasesEv(
    QQmlJSImportVisitor *self) {
  self->resolveAliases();
}

//  void QQmlJSImportVisitor::populatePropertyAliases()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor23populatePropertyAliasesEv(
    QQmlJSImportVisitor *self) {
  self->populatePropertyAliases();
}

//  void QQmlJSImportVisitor::resolveGroupProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor22resolveGroupPropertiesEv(
    QQmlJSImportVisitor *self) {
  self->resolveGroupProperties();
}

//  void
//      QQmlJSImportVisitor::handleIdDeclaration(QQmlJS::AST::UiScriptBinding
//      *scriptBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor19handleIdDeclarationEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiScriptBinding *scriptBinding) {
  self->handleIdDeclaration(scriptBinding);
}

//  void QQmlJSImportVisitor::handleLiteralBinding(const
//      QQmlJSMetaPropertyBinding &a0, const QQmlJS::AST::UiPublicMember *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor20handleLiteralBindingERK25QQmlJSMetaPropertyBindingPKN6QQmlJS3AST14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    const QQmlJSMetaPropertyBinding *a0,
    const QQmlJS::AST::UiPublicMember *a1) {
  self->handleLiteralBinding(*a0, a1);
}

//  void QQmlJSImportVisitor::visitFunctionExpressionHelper(QQmlJS::AST::Func
//      tionExpression *fexpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor29visitFunctionExpressionHelperEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionExpression *fexpr) {
  self->visitFunctionExpressionHelper(fexpr);
}

//  void QQmlJSImportVisitor::addImportWithLocation(const QString &name,
//      const QQmlJS::SourceLocation &loc, bool hadWarnings)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor21addImportWithLocationERK7QStringRKN6QQmlJS14SourceLocationEb(
    QQmlJSImportVisitor *self,
    const QString *name,
    const QQmlJS::SourceLocation *loc,
    bool hadWarnings) {
  self->addImportWithLocation(*name, *loc, hadWarnings);
}

//  void QQmlJSImportVisitor::populateCurrentScope(QQmlJSScope::ScopeType
//      type, const QString &name, const QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor20populateCurrentScopeEN6QQmlSA9ScopeTypeERK7QStringRKN6QQmlJS14SourceLocationE(
    QQmlJSImportVisitor *self,
    QQmlJSScope::ScopeType type,
    const QString *name,
    const QQmlJS::SourceLocation *location) {
  self->populateCurrentScope(type, *name, *location);
}

//  void QQmlJSImportVisitor::enterRootScope(QQmlJSScope::ScopeType type,
//      const QString &name, const QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSImportVisitor14enterRootScopeEN6QQmlSA9ScopeTypeERK7QStringRKN6QQmlJS14SourceLocationE(
    QQmlJSImportVisitor *self,
    QQmlJSScope::ScopeType type,
    const QString *name,
    const QQmlJS::SourceLocation *location) {
  self->enterRootScope(type, *name, *location);
}

//  a Python function taken by a CuteQQmlJSImportVisitor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSImportVisitor(
    QQmlJSImportVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSImportVisitor *>(self)->take(key, call);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExpressionStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19ExpressionStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExpressionStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19ExpressionStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExpressionStatement *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9UiProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9UiProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiInlineComponentE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17UiInlineComponentE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiRequired *required)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST10UiRequiredE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiRequired *required) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      required);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiScriptBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14UiArrayBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST14UiArrayBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiEnumDeclaration *uied)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17UiEnumDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *uied) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      uied);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionExpression *fexpr)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionExpression *fexpr) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      fexpr);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiSourceElementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FunctionDeclaration *fdecl)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionDeclaration *fdecl) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      fdecl);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST19FunctionDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15ClassExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassExpression *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15ClassExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiImport *import)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiImportE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiImport *import) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      import);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiPragma *pragma)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8UiPragmaE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiPragma *pragma) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      pragma);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ClassDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ClassDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ClassDeclaration *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ClassDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ClassDeclaration *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST12ForStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForStatement *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST12ForStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForStatement *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ForEachStatement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST16ForEachStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForEachStatement *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ForEachStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST16ForEachStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ForEachStatement *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5BlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Block *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Block *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5BlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Block *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST9CaseBlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::CaseBlock *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::CaseBlock *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST9CaseBlockE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::CaseBlock *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST5CatchE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Catch *ast) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      ast);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Catch *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST5CatchE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Catch *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::WithStatement
//      *withStatement)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST13WithStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::WithStatement *withStatement) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      withStatement);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::WithStatement *ast)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST13WithStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::WithStatement *ast) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      ast);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::FormalParameterList *fpl)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST19FormalParameterListE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FormalParameterList *fpl) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      fpl);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::UiObjectBinding *uiob)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST15UiObjectBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectBinding *uiob) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      uiob);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::UiObjectBinding *uiob)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST15UiObjectBindingE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::UiObjectBinding *uiob) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      uiob);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ExportDeclaration *exp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST17ExportDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExportDeclaration *exp) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      exp);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ExportDeclaration *exp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST17ExportDeclarationE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ExportDeclaration *exp) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      exp);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::ESModule *module)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST8ESModuleE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ESModule *module) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      module);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::ESModule *module)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST8ESModuleE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::ESModule *module) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      module);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::Program *program)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST7ProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Program *program) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      program);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::Program *program)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST7ProgramE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::Program *program) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      program);
}

//  void QQmlJSImportVisitor::endVisit(QQmlJS::AST::FieldMemberExpression
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor8endVisitEPN6QQmlJS3AST21FieldMemberExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::endVisit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IdentifierExpression *idexp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST20IdentifierExpressionE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::IdentifierExpression *idexp) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      idexp);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST14PatternElementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  bool QQmlJSImportVisitor::visit(QQmlJS::AST::IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQmlJSImportVisitor5visitEPN6QQmlJS3AST11IfStatementE(
    QQmlJSImportVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::visit(
      a0);
}

//  void QQmlJSImportVisitor::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor24throwRecursionDepthErrorEv(
    QQmlJSImportVisitor *self) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::throwRecursionDepthError();
}

//  void QQmlJSImportVisitor::leaveEnvironment()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor16leaveEnvironmentEv(
    QQmlJSImportVisitor *self) {
  static_cast<OwnQQmlJSImportVisitor *>(self)->OwnQQmlJSImportVisitor::leaveEnvironment();
}

//  void QQmlJSImportVisitor::handleLiteralBinding(const
//      QQmlJSMetaPropertyBinding &a0, const QQmlJS::AST::UiPublicMember *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSImportVisitor20handleLiteralBindingERK25QQmlJSMetaPropertyBindingPKN6QQmlJS3AST14UiPublicMemberE(
    QQmlJSImportVisitor *self,
    const QQmlJSMetaPropertyBinding *a0,
    const QQmlJS::AST::UiPublicMember *a1) {
  self->QQmlJSImportVisitor::handleLiteralBinding(*a0, a1);
}
