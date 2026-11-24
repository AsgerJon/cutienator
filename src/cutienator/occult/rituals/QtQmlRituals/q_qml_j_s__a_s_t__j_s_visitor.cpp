//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::JSVisitor that Python can take functions over in. Every QQmlJS::AST::JSVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlJS_AST_JSVisitorCall0)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall1)(const void *, QQmlJS::AST::Node *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall2)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall3)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall4)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall5)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall6)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall7)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall8)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall9)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall10)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall11)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall12)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall13)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall14)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall15)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall16)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall17)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall18)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall19)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall20)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall21)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall22)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall23)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall24)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall25)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall26)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall27)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall28)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall29)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall30)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall31)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall32)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall33)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall34)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall35)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall36)(const void *, QQmlJS::AST::Elision *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall37)(const void *, QQmlJS::AST::Elision *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall38)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall39)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall40)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall41)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall42)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall43)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall44)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall45)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall46)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall47)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall48)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall49)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall50)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall51)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall52)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall53)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall54)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall55)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall56)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall57)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall58)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall59)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall60)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall61)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall62)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall63)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall64)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall65)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall66)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall67)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall68)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall69)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall70)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall71)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall72)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall73)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall74)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall75)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall76)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall77)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall78)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall79)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall80)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall81)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall82)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall83)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall84)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall85)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall86)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall87)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall88)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall89)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall90)(const void *, QQmlJS::AST::Block *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall91)(const void *, QQmlJS::AST::Block *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall92)(const void *, QQmlJS::AST::StatementList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall93)(const void *, QQmlJS::AST::StatementList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall94)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall95)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall96)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall97)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall98)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall99)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall100)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall101)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall102)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall103)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall104)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall105)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall106)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall107)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall108)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall109)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall110)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall111)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall112)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall113)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall114)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall115)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall116)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall117)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall118)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall119)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall120)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall121)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall122)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall123)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall124)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall125)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall126)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall127)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall128)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall129)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall130)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall131)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall132)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall133)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall134)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall135)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall136)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall137)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall138)(const void *, QQmlJS::AST::Catch *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall139)(const void *, QQmlJS::AST::Catch *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall140)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall141)(const void *, QQmlJS::AST::Finally *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall142)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall143)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall144)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall145)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall146)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall147)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall148)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall149)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall150)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall151)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall152)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall153)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall154)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall155)(const void *, QQmlJS::AST::Program *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall156)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall157)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall158)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall159)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall160)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall161)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall162)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall163)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall164)(const void *, QQmlJS::AST::FromClause *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall165)(const void *, QQmlJS::AST::FromClause *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall166)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall167)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall168)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall169)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall170)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall171)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall172)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall173)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall174)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall175)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall176)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall177)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall178)(const void *, QQmlJS::AST::ESModule *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall179)(const void *, QQmlJS::AST::ESModule *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall180)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall181)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall182)(const void *, QQmlJS::AST::Type *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall183)(const void *, QQmlJS::AST::Type *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall184)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall185)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall186)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall187)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall188)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall189)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall190)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall191)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall192)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall193)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall194)(const void *, QQmlJS::AST::UiImport *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall195)(const void *, QQmlJS::AST::UiImport *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall196)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall197)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall198)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall199)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall200)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall201)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall202)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall203)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall204)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall205)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall206)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall207)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall208)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall209)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall210)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall211)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall212)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall213)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall214)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall215)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall216)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall217)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall218)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall219)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall220)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall221)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall222)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall223)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall224)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall225)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall226)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall227)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall228)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall229)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef bool (*CuteQQmlJS_AST_JSVisitorCall230)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall231)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef void (*CuteQQmlJS_AST_JSVisitorCall232)(const void *, int *);
class CuteQQmlJS_AST_JSVisitor : public QQmlJS::AST::JSVisitor {
public:
  using QQmlJS::AST::JSVisitor::JSVisitor;
  void *taken[233] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8preVisitEPNS0_4NodeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor9postVisitEPNS0_4NodeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeExpressionE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeExpressionE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThisExpressionE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThisExpressionE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20IdentifierExpressionE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20IdentifierExpressionE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NullExpressionE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NullExpressionE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11TrueLiteralE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11TrueLiteralE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12FalseLiteralE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12FalseLiteralE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12SuperLiteralE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12SuperLiteralE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StringLiteralE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StringLiteralE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TemplateLiteralE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TemplateLiteralE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NumericLiteralE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NumericLiteralE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13RegExpLiteralE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13RegExpLiteralE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArrayPatternE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArrayPatternE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13ObjectPatternE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13ObjectPatternE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18PatternElementListE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18PatternElementListE")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19PatternPropertyListE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19PatternPropertyListE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14PatternElementE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14PatternElementE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15PatternPropertyE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15PatternPropertyE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ElisionE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ElisionE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16NestedExpressionE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16NestedExpressionE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22IdentifierPropertyNameE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22IdentifierPropertyNameE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_25StringLiteralPropertyNameE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_25StringLiteralPropertyNameE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20ComputedPropertyNameE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20ComputedPropertyNameE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ArrayMemberExpressionE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ArrayMemberExpressionE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21FieldMemberExpressionE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21FieldMemberExpressionE")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TaggedTemplateE")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TaggedTemplateE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19NewMemberExpressionE")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19NewMemberExpressionE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NewExpressionE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NewExpressionE")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14CallExpressionE")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14CallExpressionE")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArgumentListE")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArgumentListE")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostIncrementExpressionE")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostIncrementExpressionE")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostDecrementExpressionE")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostDecrementExpressionE")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DeleteExpressionE")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DeleteExpressionE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14VoidExpressionE")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14VoidExpressionE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16TypeOfExpressionE")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16TypeOfExpressionE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreIncrementExpressionE")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreIncrementExpressionE")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreDecrementExpressionE")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreDecrementExpressionE")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UnaryPlusExpressionE")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UnaryPlusExpressionE")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20UnaryMinusExpressionE")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20UnaryMinusExpressionE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TildeExpressionE")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TildeExpressionE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NotExpressionE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NotExpressionE")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16BinaryExpressionE")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16BinaryExpressionE")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ConditionalExpressionE")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ConditionalExpressionE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15CommaExpressionE")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15CommaExpressionE")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5BlockE")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5BlockE")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StatementListE")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StatementListE")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17VariableStatementE")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17VariableStatementE")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23VariableDeclarationListE")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23VariableDeclarationListE")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14EmptyStatementE")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14EmptyStatementE")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19ExpressionStatementE")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19ExpressionStatementE")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11IfStatementE")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11IfStatementE")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DoWhileStatementE")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DoWhileStatementE")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14WhileStatementE")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14WhileStatementE")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ForStatementE")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ForStatementE")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ForEachStatementE")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ForEachStatementE")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ContinueStatementE")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ContinueStatementE")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14BreakStatementE")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14BreakStatementE")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ReturnStatementE")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ReturnStatementE")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15YieldExpressionE")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15YieldExpressionE")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13WithStatementE")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13WithStatementE")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15SwitchStatementE")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15SwitchStatementE")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9CaseBlockE")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9CaseBlockE")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11CaseClausesE")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11CaseClausesE")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10CaseClauseE")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10CaseClauseE")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13DefaultClauseE")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13DefaultClauseE")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17LabelledStatementE")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17LabelledStatementE")) {
      taken[133] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThrowStatementE")) {
      taken[134] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThrowStatementE")) {
      taken[135] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12TryStatementE")) {
      taken[136] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12TryStatementE")) {
      taken[137] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5CatchE")) {
      taken[138] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5CatchE")) {
      taken[139] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7FinallyE")) {
      taken[140] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7FinallyE")) {
      taken[141] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FunctionDeclarationE")) {
      taken[142] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FunctionDeclarationE")) {
      taken[143] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18FunctionExpressionE")) {
      taken[144] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18FunctionExpressionE")) {
      taken[145] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FormalParameterListE")) {
      taken[146] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FormalParameterListE")) {
      taken[147] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ClassExpressionE")) {
      taken[148] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ClassExpressionE")) {
      taken[149] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassDeclarationE")) {
      taken[150] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassDeclarationE")) {
      taken[151] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassElementListE")) {
      taken[152] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassElementListE")) {
      taken[153] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ProgramE")) {
      taken[154] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ProgramE")) {
      taken[155] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15NameSpaceImportE")) {
      taken[156] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15NameSpaceImportE")) {
      taken[157] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ImportSpecifierE")) {
      taken[158] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ImportSpecifierE")) {
      taken[159] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ImportsListE")) {
      taken[160] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ImportsListE")) {
      taken[161] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12NamedImportsE")) {
      taken[162] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12NamedImportsE")) {
      taken[163] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10FromClauseE")) {
      taken[164] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10FromClauseE")) {
      taken[165] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ImportClauseE")) {
      taken[166] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ImportClauseE")) {
      taken[167] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ImportDeclarationE")) {
      taken[168] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ImportDeclarationE")) {
      taken[169] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ExportSpecifierE")) {
      taken[170] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ExportSpecifierE")) {
      taken[171] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ExportsListE")) {
      taken[172] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ExportsListE")) {
      taken[173] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ExportClauseE")) {
      taken[174] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ExportClauseE")) {
      taken[175] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ExportDeclarationE")) {
      taken[176] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ExportDeclarationE")) {
      taken[177] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8ESModuleE")) {
      taken[178] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8ESModuleE")) {
      taken[179] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17DebuggerStatementE")) {
      taken[180] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17DebuggerStatementE")) {
      taken[181] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_4TypeE")) {
      taken[182] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_4TypeE")) {
      taken[183] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeAnnotationE")) {
      taken[184] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeAnnotationE")) {
      taken[185] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9UiProgramE")) {
      taken[186] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9UiProgramE")) {
      taken[187] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiHeaderItemListE")) {
      taken[188] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiHeaderItemListE")) {
      taken[189] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiPragmaValueListE")) {
      taken[190] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiPragmaValueListE")) {
      taken[191] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiPragmaE")) {
      taken[192] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiPragmaE")) {
      taken[193] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiImportE")) {
      taken[194] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiImportE")) {
      taken[195] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiPublicMemberE")) {
      taken[196] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiPublicMemberE")) {
      taken[197] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiSourceElementE")) {
      taken[198] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiSourceElementE")) {
      taken[199] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectDefinitionE")) {
      taken[200] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectDefinitionE")) {
      taken[201] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UiObjectInitializerE")) {
      taken[202] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UiObjectInitializerE")) {
      taken[203] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiObjectBindingE")) {
      taken[204] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiObjectBindingE")) {
      taken[205] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiScriptBindingE")) {
      taken[206] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiScriptBindingE")) {
      taken[207] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiArrayBindingE")) {
      taken[208] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiArrayBindingE")) {
      taken[209] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiParameterListE")) {
      taken[210] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiParameterListE")) {
      taken[211] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectMemberListE")) {
      taken[212] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectMemberListE")) {
      taken[213] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiArrayMemberListE")) {
      taken[214] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiArrayMemberListE")) {
      taken[215] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13UiQualifiedIdE")) {
      taken[216] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13UiQualifiedIdE")) {
      taken[217] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiEnumDeclarationE")) {
      taken[218] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiEnumDeclarationE")) {
      taken[219] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiEnumMemberListE")) {
      taken[220] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiEnumMemberListE")) {
      taken[221] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiVersionSpecifierE")) {
      taken[222] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiVersionSpecifierE")) {
      taken[223] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiInlineComponentE")) {
      taken[224] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiInlineComponentE")) {
      taken[225] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12UiAnnotationE")) {
      taken[226] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12UiAnnotationE")) {
      taken[227] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiAnnotationListE")) {
      taken[228] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiAnnotationListE")) {
      taken[229] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10UiRequiredE")) {
      taken[230] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10UiRequiredE")) {
      taken[231] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor24throwRecursionDepthErrorEv")) {
      taken[232] = call;
      return true;
    }
    return false;
  }

  //  bool QQmlJS::AST::JSVisitor::preVisit(Node *a0)
  bool preVisit(QQmlJS::AST::Node *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall0 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::preVisit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::postVisit(Node *a0)
  void postVisit(QQmlJS::AST::Node *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall1 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::postVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TypeExpression *a0)
  bool visit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall2 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TypeExpression *a0)
  void endVisit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall3 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ThisExpression *a0)
  bool visit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall4 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ThisExpression *a0)
  void endVisit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall5 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(IdentifierExpression *a0)
  bool visit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall6 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(IdentifierExpression *a0)
  void endVisit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall7 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NullExpression *a0)
  bool visit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall8 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NullExpression *a0)
  void endVisit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall9 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TrueLiteral *a0)
  bool visit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall10 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TrueLiteral *a0)
  void endVisit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall11 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(FalseLiteral *a0)
  bool visit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall12 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(FalseLiteral *a0)
  void endVisit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall13 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(SuperLiteral *a0)
  bool visit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall14 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(SuperLiteral *a0)
  void endVisit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall15 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(StringLiteral *a0)
  bool visit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall16 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall16>(taken[16]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(StringLiteral *a0)
  void endVisit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall17 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TemplateLiteral *a0)
  bool visit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall18 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TemplateLiteral *a0)
  void endVisit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall19 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NumericLiteral *a0)
  bool visit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall20 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NumericLiteral *a0)
  void endVisit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall21 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(RegExpLiteral *a0)
  bool visit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall22 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall22>(taken[22]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(RegExpLiteral *a0)
  void endVisit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall23 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ArrayPattern *a0)
  bool visit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall24 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall24>(taken[24]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ArrayPattern *a0)
  void endVisit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall25 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ObjectPattern *a0)
  bool visit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall26 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall26>(taken[26]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ObjectPattern *a0)
  void endVisit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall27 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PatternElementList *a0)
  bool visit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall28 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall28>(taken[28]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PatternElementList *a0)
  void endVisit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall29 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PatternPropertyList *a0)
  bool visit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall30 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall30>(taken[30]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PatternPropertyList *a0)
  void endVisit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall31 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PatternElement *a0)
  bool visit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall32 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall32>(taken[32]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PatternElement *a0)
  void endVisit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall33 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PatternProperty *a0)
  bool visit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall34 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall34>(taken[34]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PatternProperty *a0)
  void endVisit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall35 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(Elision *a0)
  bool visit(QQmlJS::AST::Elision *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall36 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(Elision *a0)
  void endVisit(QQmlJS::AST::Elision *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall37 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NestedExpression *a0)
  bool visit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall38 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NestedExpression *a0)
  void endVisit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall39 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(IdentifierPropertyName *a0)
  bool visit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall40 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall40>(taken[40]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(IdentifierPropertyName *a0)
  void endVisit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall41 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(StringLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall42 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall42>(taken[42]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(StringLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall43 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NumericLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall44 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall44>(taken[44]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NumericLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall45 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ComputedPropertyName *a0)
  bool visit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall46 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall46>(taken[46]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ComputedPropertyName *a0)
  void endVisit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall47 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ArrayMemberExpression *a0)
  bool visit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall48 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall48>(taken[48]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ArrayMemberExpression *a0)
  void endVisit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall49 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(FieldMemberExpression *a0)
  bool visit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall50 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall50>(taken[50]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(FieldMemberExpression *a0)
  void endVisit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall51 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TaggedTemplate *a0)
  bool visit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall52 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall52>(taken[52]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TaggedTemplate *a0)
  void endVisit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall53 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall53>(taken[53]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NewMemberExpression *a0)
  bool visit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall54 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall54>(taken[54]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NewMemberExpression *a0)
  void endVisit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall55 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall55>(taken[55]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NewExpression *a0)
  bool visit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall56 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall56>(taken[56]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NewExpression *a0)
  void endVisit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall57 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall57>(taken[57]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(CallExpression *a0)
  bool visit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall58 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall58>(taken[58]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(CallExpression *a0)
  void endVisit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall59 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall59>(taken[59]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ArgumentList *a0)
  bool visit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall60 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall60>(taken[60]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ArgumentList *a0)
  void endVisit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall61 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PostIncrementExpression *a0)
  bool visit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall62 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall62>(taken[62]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PostIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall63 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PostDecrementExpression *a0)
  bool visit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall64 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall64>(taken[64]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PostDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall65 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(DeleteExpression *a0)
  bool visit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall66 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall66>(taken[66]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(DeleteExpression *a0)
  void endVisit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall67 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(VoidExpression *a0)
  bool visit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall68 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall68>(taken[68]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(VoidExpression *a0)
  void endVisit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall69 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TypeOfExpression *a0)
  bool visit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall70 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall70>(taken[70]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TypeOfExpression *a0)
  void endVisit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall71 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall71>(taken[71]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PreIncrementExpression *a0)
  bool visit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall72 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall72>(taken[72]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PreIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall73 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(PreDecrementExpression *a0)
  bool visit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall74 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall74>(taken[74]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(PreDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall75 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall75>(taken[75]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UnaryPlusExpression *a0)
  bool visit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall76 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall76>(taken[76]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UnaryPlusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall77 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall77>(taken[77]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UnaryMinusExpression *a0)
  bool visit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall78 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall78>(taken[78]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UnaryMinusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall79 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall79>(taken[79]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TildeExpression *a0)
  bool visit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall80 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall80>(taken[80]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TildeExpression *a0)
  void endVisit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall81 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall81>(taken[81]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NotExpression *a0)
  bool visit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall82 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall82>(taken[82]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NotExpression *a0)
  void endVisit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall83 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall83>(taken[83]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(BinaryExpression *a0)
  bool visit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall84 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall84>(taken[84]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(BinaryExpression *a0)
  void endVisit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall85 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall85>(taken[85]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ConditionalExpression *a0)
  bool visit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall86 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall86>(taken[86]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ConditionalExpression *a0)
  void endVisit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall87 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall87>(taken[87]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(CommaExpression *a0)
  bool visit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall88 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall88>(taken[88]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(CommaExpression *a0)
  void endVisit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall89 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall89>(taken[89]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(Block *a0)
  bool visit(QQmlJS::AST::Block *a0) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall90 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall90>(taken[90]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(Block *a0)
  void endVisit(QQmlJS::AST::Block *a0) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall91 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall91>(taken[91]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(StatementList *a0)
  bool visit(QQmlJS::AST::StatementList *a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall92 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall92>(taken[92]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(StatementList *a0)
  void endVisit(QQmlJS::AST::StatementList *a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall93 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall93>(taken[93]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(VariableStatement *a0)
  bool visit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall94 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall94>(taken[94]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(VariableStatement *a0)
  void endVisit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall95 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(VariableDeclarationList *a0)
  bool visit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall96 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall96>(taken[96]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(VariableDeclarationList *a0)
  void endVisit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall97 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall97>(taken[97]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(EmptyStatement *a0)
  bool visit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall98 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall98>(taken[98]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(EmptyStatement *a0)
  void endVisit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall99 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall99>(taken[99]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ExpressionStatement *a0)
  bool visit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall100 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall100>(taken[100]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ExpressionStatement *a0)
  void endVisit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall101 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall101>(taken[101]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(IfStatement *a0)
  bool visit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall102 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall102>(taken[102]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(IfStatement *a0)
  void endVisit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall103 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall103>(taken[103]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(DoWhileStatement *a0)
  bool visit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall104 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall104>(taken[104]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(DoWhileStatement *a0)
  void endVisit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall105 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall105>(taken[105]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(WhileStatement *a0)
  bool visit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall106 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall106>(taken[106]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(WhileStatement *a0)
  void endVisit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall107 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall107>(taken[107]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ForStatement *a0)
  bool visit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall108 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall108>(taken[108]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ForStatement *a0)
  void endVisit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall109 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall109>(taken[109]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ForEachStatement *a0)
  bool visit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall110 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall110>(taken[110]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ForEachStatement *a0)
  void endVisit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall111 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ContinueStatement *a0)
  bool visit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall112 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall112>(taken[112]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ContinueStatement *a0)
  void endVisit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall113 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall113>(taken[113]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(BreakStatement *a0)
  bool visit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall114 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall114>(taken[114]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(BreakStatement *a0)
  void endVisit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall115 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall115>(taken[115]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ReturnStatement *a0)
  bool visit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall116 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall116>(taken[116]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ReturnStatement *a0)
  void endVisit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall117 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall117>(taken[117]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(YieldExpression *a0)
  bool visit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall118 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall118>(taken[118]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(YieldExpression *a0)
  void endVisit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall119 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall119>(taken[119]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(WithStatement *a0)
  bool visit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall120 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall120>(taken[120]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(WithStatement *a0)
  void endVisit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall121 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall121>(taken[121]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(SwitchStatement *a0)
  bool visit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall122 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall122>(taken[122]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(SwitchStatement *a0)
  void endVisit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall123 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall123>(taken[123]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(CaseBlock *a0)
  bool visit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall124 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall124>(taken[124]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(CaseBlock *a0)
  void endVisit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall125 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall125>(taken[125]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(CaseClauses *a0)
  bool visit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall126 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall126>(taken[126]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(CaseClauses *a0)
  void endVisit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall127 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall127>(taken[127]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(CaseClause *a0)
  bool visit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall128 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall128>(taken[128]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(CaseClause *a0)
  void endVisit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall129 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall129>(taken[129]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(DefaultClause *a0)
  bool visit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall130 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall130>(taken[130]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(DefaultClause *a0)
  void endVisit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall131 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall131>(taken[131]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(LabelledStatement *a0)
  bool visit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall132 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall132>(taken[132]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(LabelledStatement *a0)
  void endVisit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall133 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall133>(taken[133]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ThrowStatement *a0)
  bool visit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[134]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall134 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall134>(taken[134]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ThrowStatement *a0)
  void endVisit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[135]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall135 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall135>(taken[135]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TryStatement *a0)
  bool visit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[136]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall136 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall136>(taken[136]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TryStatement *a0)
  void endVisit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[137]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall137 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall137>(taken[137]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(Catch *a0)
  bool visit(QQmlJS::AST::Catch *a0) override {
    if (taken[138]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall138 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall138>(taken[138]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(Catch *a0)
  void endVisit(QQmlJS::AST::Catch *a0) override {
    if (taken[139]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall139 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall139>(taken[139]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(Finally *a0)
  bool visit(QQmlJS::AST::Finally *a0) override {
    if (taken[140]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall140 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall140>(taken[140]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(Finally *a0)
  void endVisit(QQmlJS::AST::Finally *a0) override {
    if (taken[141]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall141 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall141>(taken[141]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(FunctionDeclaration *a0)
  bool visit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[142]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall142 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall142>(taken[142]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(FunctionDeclaration *a0)
  void endVisit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[143]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall143 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall143>(taken[143]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(FunctionExpression *a0)
  bool visit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[144]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall144 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall144>(taken[144]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(FunctionExpression *a0)
  void endVisit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[145]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall145 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall145>(taken[145]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(FormalParameterList *a0)
  bool visit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[146]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall146 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall146>(taken[146]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(FormalParameterList *a0)
  void endVisit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[147]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall147 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall147>(taken[147]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ClassExpression *a0)
  bool visit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[148]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall148 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall148>(taken[148]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ClassExpression *a0)
  void endVisit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[149]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall149 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall149>(taken[149]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ClassDeclaration *a0)
  bool visit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[150]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall150 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall150>(taken[150]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ClassDeclaration *a0)
  void endVisit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[151]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall151 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall151>(taken[151]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ClassElementList *a0)
  bool visit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[152]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall152 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall152>(taken[152]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ClassElementList *a0)
  void endVisit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[153]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall153 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall153>(taken[153]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(Program *a0)
  bool visit(QQmlJS::AST::Program *a0) override {
    if (taken[154]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall154 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall154>(taken[154]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(Program *a0)
  void endVisit(QQmlJS::AST::Program *a0) override {
    if (taken[155]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall155 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall155>(taken[155]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NameSpaceImport *a0)
  bool visit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[156]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall156 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall156>(taken[156]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NameSpaceImport *a0)
  void endVisit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[157]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall157 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall157>(taken[157]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ImportSpecifier *a0)
  bool visit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[158]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall158 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall158>(taken[158]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ImportSpecifier *a0)
  void endVisit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[159]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall159 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall159>(taken[159]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ImportsList *a0)
  bool visit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[160]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall160 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall160>(taken[160]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ImportsList *a0)
  void endVisit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[161]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall161 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall161>(taken[161]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(NamedImports *a0)
  bool visit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[162]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall162 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall162>(taken[162]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(NamedImports *a0)
  void endVisit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[163]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall163 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall163>(taken[163]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(FromClause *a0)
  bool visit(QQmlJS::AST::FromClause *a0) override {
    if (taken[164]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall164 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall164>(taken[164]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(FromClause *a0)
  void endVisit(QQmlJS::AST::FromClause *a0) override {
    if (taken[165]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall165 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall165>(taken[165]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ImportClause *a0)
  bool visit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[166]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall166 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall166>(taken[166]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ImportClause *a0)
  void endVisit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[167]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall167 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall167>(taken[167]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ImportDeclaration *a0)
  bool visit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[168]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall168 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall168>(taken[168]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ImportDeclaration *a0)
  void endVisit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[169]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall169 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall169>(taken[169]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ExportSpecifier *a0)
  bool visit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[170]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall170 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall170>(taken[170]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ExportSpecifier *a0)
  void endVisit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[171]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall171 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall171>(taken[171]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ExportsList *a0)
  bool visit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[172]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall172 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall172>(taken[172]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ExportsList *a0)
  void endVisit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[173]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall173 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall173>(taken[173]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ExportClause *a0)
  bool visit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[174]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall174 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall174>(taken[174]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ExportClause *a0)
  void endVisit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[175]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall175 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall175>(taken[175]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ExportDeclaration *a0)
  bool visit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[176]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall176 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall176>(taken[176]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ExportDeclaration *a0)
  void endVisit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[177]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall177 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall177>(taken[177]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(ESModule *a0)
  bool visit(QQmlJS::AST::ESModule *a0) override {
    if (taken[178]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall178 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall178>(taken[178]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(ESModule *a0)
  void endVisit(QQmlJS::AST::ESModule *a0) override {
    if (taken[179]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall179 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall179>(taken[179]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(DebuggerStatement *a0)
  bool visit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[180]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall180 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall180>(taken[180]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(DebuggerStatement *a0)
  void endVisit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[181]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall181 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall181>(taken[181]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(Type *a0)
  bool visit(QQmlJS::AST::Type *a0) override {
    if (taken[182]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall182 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall182>(taken[182]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(Type *a0)
  void endVisit(QQmlJS::AST::Type *a0) override {
    if (taken[183]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall183 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall183>(taken[183]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(TypeAnnotation *a0)
  bool visit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[184]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall184 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall184>(taken[184]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(TypeAnnotation *a0)
  void endVisit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[185]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall185 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall185>(taken[185]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiProgram *a0)
  bool visit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[186]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall186 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall186>(taken[186]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiProgram *a0)
  void endVisit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[187]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall187 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall187>(taken[187]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiHeaderItemList *a0)
  bool visit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[188]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall188 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall188>(taken[188]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiHeaderItemList *a0)
  void endVisit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[189]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall189 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall189>(taken[189]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiPragmaValueList *a0)
  bool visit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[190]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall190 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall190>(taken[190]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiPragmaValueList *a0)
  void endVisit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[191]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall191 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall191>(taken[191]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiPragma *a0)
  bool visit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[192]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall192 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall192>(taken[192]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiPragma *a0)
  void endVisit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[193]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall193 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall193>(taken[193]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiImport *a0)
  bool visit(QQmlJS::AST::UiImport *a0) override {
    if (taken[194]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall194 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall194>(taken[194]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiImport *a0)
  void endVisit(QQmlJS::AST::UiImport *a0) override {
    if (taken[195]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall195 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall195>(taken[195]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiPublicMember *a0)
  bool visit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[196]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall196 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall196>(taken[196]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiPublicMember *a0)
  void endVisit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[197]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall197 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall197>(taken[197]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiSourceElement *a0)
  bool visit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[198]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall198 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall198>(taken[198]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiSourceElement *a0)
  void endVisit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[199]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall199 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall199>(taken[199]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiObjectDefinition *a0)
  bool visit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[200]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall200 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall200>(taken[200]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiObjectDefinition *a0)
  void endVisit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[201]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall201 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall201>(taken[201]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiObjectInitializer *a0)
  bool visit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[202]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall202 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall202>(taken[202]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiObjectInitializer *a0)
  void endVisit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[203]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall203 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall203>(taken[203]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiObjectBinding *a0)
  bool visit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[204]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall204 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall204>(taken[204]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiObjectBinding *a0)
  void endVisit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[205]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall205 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall205>(taken[205]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiScriptBinding *a0)
  bool visit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[206]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall206 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall206>(taken[206]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiScriptBinding *a0)
  void endVisit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[207]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall207 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall207>(taken[207]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiArrayBinding *a0)
  bool visit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[208]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall208 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall208>(taken[208]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiArrayBinding *a0)
  void endVisit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[209]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall209 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall209>(taken[209]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiParameterList *a0)
  bool visit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[210]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall210 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall210>(taken[210]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiParameterList *a0)
  void endVisit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[211]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall211 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall211>(taken[211]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiObjectMemberList *a0)
  bool visit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[212]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall212 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall212>(taken[212]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiObjectMemberList *a0)
  void endVisit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[213]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall213 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall213>(taken[213]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiArrayMemberList *a0)
  bool visit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[214]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall214 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall214>(taken[214]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiArrayMemberList *a0)
  void endVisit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[215]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall215 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall215>(taken[215]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiQualifiedId *a0)
  bool visit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[216]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall216 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall216>(taken[216]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiQualifiedId *a0)
  void endVisit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[217]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall217 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall217>(taken[217]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiEnumDeclaration *a0)
  bool visit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[218]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall218 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall218>(taken[218]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiEnumDeclaration *a0)
  void endVisit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[219]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall219 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall219>(taken[219]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiEnumMemberList *a0)
  bool visit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[220]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall220 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall220>(taken[220]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiEnumMemberList *a0)
  void endVisit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[221]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall221 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall221>(taken[221]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiVersionSpecifier *a0)
  bool visit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[222]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall222 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall222>(taken[222]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiVersionSpecifier *a0)
  void endVisit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[223]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall223 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall223>(taken[223]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiInlineComponent *a0)
  bool visit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[224]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall224 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall224>(taken[224]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiInlineComponent *a0)
  void endVisit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[225]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall225 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall225>(taken[225]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiAnnotation *a0)
  bool visit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[226]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall226 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall226>(taken[226]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiAnnotation *a0)
  void endVisit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[227]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall227 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall227>(taken[227]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiAnnotationList *a0)
  bool visit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[228]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall228 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall228>(taken[228]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiAnnotationList *a0)
  void endVisit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[229]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall229 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall229>(taken[229]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::JSVisitor::visit(UiRequired *a0)
  bool visit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[230]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall230 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall230>(taken[230]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::JSVisitor::visit(a0);
  }

  //  void QQmlJS::AST::JSVisitor::endVisit(UiRequired *a0)
  void endVisit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[231]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall231 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall231>(taken[231]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::JSVisitor::endVisit(a0);
  }

  //  void QQmlJS::AST::BaseVisitor::throwRecursionDepthError()
  void throwRecursionDepthError() override {
    if (taken[232]) {
      int handled = 0;
      CuteQQmlJS_AST_JSVisitorCall232 call = reinterpret_cast<CuteQQmlJS_AST_JSVisitorCall232>(taken[232]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  bool QQmlJS::AST::JSVisitor::preVisit(Node *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor8preVisitEPNS0_4NodeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Node *a0) {
  return self->preVisit(a0);
}

//  void QQmlJS::AST::JSVisitor::postVisit(Node *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor9postVisitEPNS0_4NodeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Node *a0) {
  self->postVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14TypeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14TypeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14ThisExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14ThisExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14NullExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NullExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14NullExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NullExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11TrueLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11TrueLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12FalseLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12FalseLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12SuperLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12SuperLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13StringLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13StringLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14NumericLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14NumericLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ArrayPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ArrayPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13ObjectPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13ObjectPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18PatternElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18PatternElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14PatternElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14PatternElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15PatternPropertyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15PatternPropertyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Elision *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_7ElisionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Elision *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Elision *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_7ElisionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Elision *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16NestedExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16NestedExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13NewExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13NewExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14CallExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CallExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14CallExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CallExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ArgumentListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ArgumentListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14VoidExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14VoidExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15TildeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15TildeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13NotExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NotExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13NotExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NotExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15CommaExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15CommaExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Block *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_5BlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Block *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Block *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_5BlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Block *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(StatementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13StatementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StatementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(StatementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13StatementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StatementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17VariableStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17VariableStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14EmptyStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14EmptyStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11IfStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11IfStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14WhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14WhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ForStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ForStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16ForEachStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16ForEachStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17ContinueStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17ContinueStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14BreakStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14BreakStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ReturnStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ReturnStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15YieldExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15YieldExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13WithStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WithStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13WithStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WithStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15SwitchStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15SwitchStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_9CaseBlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_9CaseBlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11CaseClausesE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11CaseClausesE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_10CaseClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_10CaseClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13DefaultClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13DefaultClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17LabelledStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17LabelledStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14ThrowStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14ThrowStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12TryStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TryStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12TryStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TryStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Catch *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_5CatchE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Catch *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Catch *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_5CatchE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Catch *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Finally *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_7FinallyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Finally *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Finally *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_7FinallyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Finally *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19FormalParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19FormalParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ClassExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ClassExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16ClassElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16ClassElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Program *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_7ProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Program *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_7ProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Program *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11ImportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportsList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11ImportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportsList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12NamedImportsE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NamedImports *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12NamedImportsE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NamedImports *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FromClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_10FromClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FromClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FromClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_10FromClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FromClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ImportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ImportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11ExportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportsList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11ExportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportsList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ExportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ExportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ESModule *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_8ESModuleE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ESModule *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_8ESModuleE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ESModule *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Type *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_4TypeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Type *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Type *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_4TypeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Type *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_9UiProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_9UiProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_8UiPragmaE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragma *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_8UiPragmaE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragma *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_8UiImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiImport *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_8UiImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiImport *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiSourceElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiSourceElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12UiAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12UiAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_10UiRequiredE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiRequired *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_10UiRequiredE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiRequired *a0) {
  self->endVisit(a0);
}

//  a Python function taken by a CuteQQmlJS_AST_JSVisitor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_JSVisitor(
    QQmlJS::AST::JSVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_JSVisitor *>(self)->take(key, call);
}

//  bool QQmlJS::AST::JSVisitor::preVisit(Node *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor8preVisitEPNS0_4NodeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Node *a0) {
  return self->QQmlJS::AST::JSVisitor::preVisit(a0);
}

//  void QQmlJS::AST::JSVisitor::postVisit(Node *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor9postVisitEPNS0_4NodeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Node *a0) {
  self->QQmlJS::AST::JSVisitor::postVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14TypeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14TypeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14ThisExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14ThisExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14NullExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NullExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14NullExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NullExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11TrueLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11TrueLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12FalseLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12FalseLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12SuperLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12SuperLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13StringLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13StringLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14NumericLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14NumericLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ArrayPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ArrayPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13ObjectPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13ObjectPatternE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18PatternElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18PatternElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14PatternElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14PatternElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15PatternPropertyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15PatternPropertyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Elision *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_7ElisionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Elision *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Elision *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_7ElisionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Elision *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16NestedExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16NestedExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13NewExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13NewExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NewExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14CallExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CallExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14CallExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CallExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ArgumentListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ArgumentListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14VoidExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14VoidExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15TildeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15TildeExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13NotExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NotExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13NotExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NotExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15CommaExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15CommaExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Block *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_5BlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Block *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Block *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_5BlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Block *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(StatementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13StatementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StatementList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(StatementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13StatementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::StatementList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17VariableStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17VariableStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14EmptyStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14EmptyStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11IfStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11IfStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14WhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14WhileStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ForStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ForStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16ForEachStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16ForEachStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17ContinueStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17ContinueStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14BreakStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14BreakStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ReturnStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ReturnStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15YieldExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15YieldExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13WithStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WithStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13WithStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::WithStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15SwitchStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15SwitchStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_9CaseBlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_9CaseBlockE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11CaseClausesE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11CaseClausesE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_10CaseClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClause *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_10CaseClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::CaseClause *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13DefaultClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13DefaultClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17LabelledStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17LabelledStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14ThrowStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14ThrowStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12TryStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TryStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12TryStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TryStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Catch *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_5CatchE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Catch *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Catch *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_5CatchE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Catch *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Finally *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_7FinallyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Finally *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Finally *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_7FinallyE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Finally *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19FormalParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19FormalParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ClassExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ClassExpressionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16ClassElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16ClassElementListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Program *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_7ProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Program *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_7ProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Program *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11ImportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportsList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11ImportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportsList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12NamedImportsE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NamedImports *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12NamedImportsE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::NamedImports *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(FromClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_10FromClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FromClause *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(FromClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_10FromClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::FromClause *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ImportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportClause *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ImportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportClause *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_11ExportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportsList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_11ExportsListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportsList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12ExportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportClause *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12ExportClauseE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportClause *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(ESModule *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_8ESModuleE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ESModule *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_8ESModuleE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::ESModule *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(Type *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_4TypeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Type *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(Type *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_4TypeE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::Type *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_9UiProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_9UiProgramE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_8UiPragmaE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragma *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_8UiPragmaE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPragma *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_8UiImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiImport *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_8UiImportE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiImport *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiSourceElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiSourceElementE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_15UiParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_15UiParameterListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_12UiAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_12UiAnnotationE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}

//  bool QQmlJS::AST::JSVisitor::visit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST9JSVisitor5visitEPNS0_10UiRequiredE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiRequired *a0) {
  return self->QQmlJS::AST::JSVisitor::visit(a0);
}

//  void QQmlJS::AST::JSVisitor::endVisit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST9JSVisitor8endVisitEPNS0_10UiRequiredE(
    QQmlJS::AST::JSVisitor *self,
    QQmlJS::AST::UiRequired *a0) {
  self->QQmlJS::AST::JSVisitor::endVisit(a0);
}
