//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <cstring>

//  A QmlIR::IRBuilder that Python can take functions over in. Every QmlIR::IRBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQmlIR_IRBuilderCall0)(const void *, QQmlJS::AST::UiImport *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall1)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall2)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall3)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall4)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall5)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall6)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall7)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall8)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall9)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall10)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall11)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef void (*CuteQmlIR_IRBuilderCall12)(const void *, int *);
typedef void (*CuteQmlIR_IRBuilderCall13)(const void *, QV4::CompiledData::Binding *, QQmlJS::AST::Statement *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQmlIR_IRBuilderCall14)(const void *, QQmlJS::AST::FunctionExpression *, int, int *);
typedef bool (*CuteQmlIR_IRBuilderCall15)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQmlIR_IRBuilderCall16)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQmlIR_IRBuilderCall17)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall18)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall19)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall20)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall21)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall22)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef void (*CuteQmlIR_IRBuilderCall23)(const void *, QQmlJS::AST::UiImport *, int *);
typedef void (*CuteQmlIR_IRBuilderCall24)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef void (*CuteQmlIR_IRBuilderCall25)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall26)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall27)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQmlIR_IRBuilderCall28)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQmlIR_IRBuilderCall29)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef void (*CuteQmlIR_IRBuilderCall30)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef void (*CuteQmlIR_IRBuilderCall31)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall32)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall33)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall34)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall35)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall36)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall37)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall38)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQmlIR_IRBuilderCall39)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQmlIR_IRBuilderCall40)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall41)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall42)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall43)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQmlIR_IRBuilderCall44)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQmlIR_IRBuilderCall45)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall46)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef void (*CuteQmlIR_IRBuilderCall47)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall48)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall49)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall50)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall51)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall52)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall53)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall54)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall55)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall56)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall57)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall58)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall59)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall60)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall61)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall62)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall63)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall64)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall65)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall66)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall67)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall68)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall69)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall70)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall71)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef void (*CuteQmlIR_IRBuilderCall72)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall73)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef void (*CuteQmlIR_IRBuilderCall74)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall75)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef void (*CuteQmlIR_IRBuilderCall76)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall77)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall78)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall79)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall80)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall81)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall82)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall83)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef void (*CuteQmlIR_IRBuilderCall84)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall85)(const void *, QQmlJS::AST::Elision *, int *);
typedef void (*CuteQmlIR_IRBuilderCall86)(const void *, QQmlJS::AST::Elision *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall87)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall88)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall89)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef void (*CuteQmlIR_IRBuilderCall90)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall91)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef void (*CuteQmlIR_IRBuilderCall92)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall93)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef void (*CuteQmlIR_IRBuilderCall94)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall95)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef void (*CuteQmlIR_IRBuilderCall96)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall97)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall98)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall99)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall100)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall101)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef void (*CuteQmlIR_IRBuilderCall102)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall103)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall104)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall105)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall106)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall107)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall108)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall109)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall110)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall111)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall112)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall113)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall114)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall115)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall116)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall117)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall118)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall119)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall120)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall121)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall122)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall123)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall124)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall125)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall126)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall127)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall128)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall129)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall130)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall131)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall132)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall133)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall134)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall135)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall136)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall137)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall138)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall139)(const void *, QQmlJS::AST::Block *, int *);
typedef void (*CuteQmlIR_IRBuilderCall140)(const void *, QQmlJS::AST::Block *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall141)(const void *, QQmlJS::AST::StatementList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall142)(const void *, QQmlJS::AST::StatementList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall143)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall144)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall145)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall146)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall147)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall148)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall149)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall150)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall151)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall152)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall153)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall154)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall155)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall156)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall157)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall158)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall159)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall160)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall161)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall162)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall163)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall164)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall165)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall166)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall167)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall168)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall169)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall170)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall171)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall172)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall173)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef void (*CuteQmlIR_IRBuilderCall174)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall175)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef void (*CuteQmlIR_IRBuilderCall176)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall177)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef void (*CuteQmlIR_IRBuilderCall178)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall179)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef void (*CuteQmlIR_IRBuilderCall180)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall181)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall182)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall183)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall184)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall185)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall186)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall187)(const void *, QQmlJS::AST::Catch *, int *);
typedef void (*CuteQmlIR_IRBuilderCall188)(const void *, QQmlJS::AST::Catch *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall189)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQmlIR_IRBuilderCall190)(const void *, QQmlJS::AST::Finally *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall191)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef void (*CuteQmlIR_IRBuilderCall192)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall193)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall194)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall195)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall196)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall197)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef void (*CuteQmlIR_IRBuilderCall198)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall199)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef void (*CuteQmlIR_IRBuilderCall200)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall201)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall202)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall203)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQmlIR_IRBuilderCall204)(const void *, QQmlJS::AST::Program *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall205)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef void (*CuteQmlIR_IRBuilderCall206)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall207)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef void (*CuteQmlIR_IRBuilderCall208)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall209)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall210)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall211)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef void (*CuteQmlIR_IRBuilderCall212)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall213)(const void *, QQmlJS::AST::FromClause *, int *);
typedef void (*CuteQmlIR_IRBuilderCall214)(const void *, QQmlJS::AST::FromClause *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall215)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef void (*CuteQmlIR_IRBuilderCall216)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall217)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef void (*CuteQmlIR_IRBuilderCall218)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall219)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef void (*CuteQmlIR_IRBuilderCall220)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall221)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef void (*CuteQmlIR_IRBuilderCall222)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall223)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef void (*CuteQmlIR_IRBuilderCall224)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall225)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef void (*CuteQmlIR_IRBuilderCall226)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall227)(const void *, QQmlJS::AST::ESModule *, int *);
typedef void (*CuteQmlIR_IRBuilderCall228)(const void *, QQmlJS::AST::ESModule *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall229)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef void (*CuteQmlIR_IRBuilderCall230)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall231)(const void *, QQmlJS::AST::Type *, int *);
typedef void (*CuteQmlIR_IRBuilderCall232)(const void *, QQmlJS::AST::Type *, int *);
typedef bool (*CuteQmlIR_IRBuilderCall233)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQmlIR_IRBuilderCall234)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
class CuteQmlIR_IRBuilder : public QmlIR::IRBuilder {
public:
  using QmlIR::IRBuilder::IRBuilder;
  CuteQmlIR_IRBuilder(const QmlIR::IRBuilder &other) : QmlIR::IRBuilder(other) {}
  void *taken[235] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiImportE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiPragmaE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9UiProgramE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiArrayBindingE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiObjectBindingE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectDefinitionE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiInlineComponentE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiEnumDeclarationE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiPublicMemberE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiScriptBindingE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiSourceElementE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10UiRequiredE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor24throwRecursionDepthErrorEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN5QmlIR9IRBuilder15setBindingValueEPN3QV412CompiledData7BindingEPN6QQmlJS3AST9StatementEPNS6_4NodeE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AST18FunctionExpressionENS0_13IsQmlFunctionE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8preVisitEPNS0_4NodeE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor9postVisitEPNS0_4NodeE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9UiProgramE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiHeaderItemListE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiHeaderItemListE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiPragmaValueListE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiPragmaValueListE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiPragmaE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiImportE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiPublicMemberE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiSourceElementE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectDefinitionE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UiObjectInitializerE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UiObjectInitializerE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiObjectBindingE")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiScriptBindingE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiArrayBindingE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiParameterListE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiParameterListE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectMemberListE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectMemberListE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiArrayMemberListE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiArrayMemberListE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13UiQualifiedIdE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13UiQualifiedIdE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiEnumDeclarationE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiEnumMemberListE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiEnumMemberListE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiVersionSpecifierE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiVersionSpecifierE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiInlineComponentE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12UiAnnotationE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12UiAnnotationE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiAnnotationListE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiAnnotationListE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10UiRequiredE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeExpressionE")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeExpressionE")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThisExpressionE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThisExpressionE")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20IdentifierExpressionE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20IdentifierExpressionE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NullExpressionE")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NullExpressionE")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11TrueLiteralE")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11TrueLiteralE")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12FalseLiteralE")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12FalseLiteralE")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12SuperLiteralE")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12SuperLiteralE")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StringLiteralE")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StringLiteralE")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TemplateLiteralE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TemplateLiteralE")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NumericLiteralE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NumericLiteralE")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13RegExpLiteralE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13RegExpLiteralE")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArrayPatternE")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArrayPatternE")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13ObjectPatternE")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13ObjectPatternE")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18PatternElementListE")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18PatternElementListE")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19PatternPropertyListE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19PatternPropertyListE")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14PatternElementE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14PatternElementE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15PatternPropertyE")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15PatternPropertyE")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ElisionE")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ElisionE")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16NestedExpressionE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16NestedExpressionE")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22IdentifierPropertyNameE")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22IdentifierPropertyNameE")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_25StringLiteralPropertyNameE")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_25StringLiteralPropertyNameE")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20ComputedPropertyNameE")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20ComputedPropertyNameE")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ArrayMemberExpressionE")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ArrayMemberExpressionE")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21FieldMemberExpressionE")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21FieldMemberExpressionE")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TaggedTemplateE")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TaggedTemplateE")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19NewMemberExpressionE")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19NewMemberExpressionE")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NewExpressionE")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NewExpressionE")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14CallExpressionE")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14CallExpressionE")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArgumentListE")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArgumentListE")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostIncrementExpressionE")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostIncrementExpressionE")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostDecrementExpressionE")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostDecrementExpressionE")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DeleteExpressionE")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DeleteExpressionE")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14VoidExpressionE")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14VoidExpressionE")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16TypeOfExpressionE")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16TypeOfExpressionE")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreIncrementExpressionE")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreIncrementExpressionE")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreDecrementExpressionE")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreDecrementExpressionE")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UnaryPlusExpressionE")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UnaryPlusExpressionE")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20UnaryMinusExpressionE")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20UnaryMinusExpressionE")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TildeExpressionE")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TildeExpressionE")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NotExpressionE")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NotExpressionE")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16BinaryExpressionE")) {
      taken[133] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16BinaryExpressionE")) {
      taken[134] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ConditionalExpressionE")) {
      taken[135] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ConditionalExpressionE")) {
      taken[136] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15CommaExpressionE")) {
      taken[137] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15CommaExpressionE")) {
      taken[138] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5BlockE")) {
      taken[139] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5BlockE")) {
      taken[140] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StatementListE")) {
      taken[141] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StatementListE")) {
      taken[142] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17VariableStatementE")) {
      taken[143] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17VariableStatementE")) {
      taken[144] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23VariableDeclarationListE")) {
      taken[145] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23VariableDeclarationListE")) {
      taken[146] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14EmptyStatementE")) {
      taken[147] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14EmptyStatementE")) {
      taken[148] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19ExpressionStatementE")) {
      taken[149] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19ExpressionStatementE")) {
      taken[150] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11IfStatementE")) {
      taken[151] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11IfStatementE")) {
      taken[152] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DoWhileStatementE")) {
      taken[153] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DoWhileStatementE")) {
      taken[154] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14WhileStatementE")) {
      taken[155] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14WhileStatementE")) {
      taken[156] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ForStatementE")) {
      taken[157] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ForStatementE")) {
      taken[158] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ForEachStatementE")) {
      taken[159] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ForEachStatementE")) {
      taken[160] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ContinueStatementE")) {
      taken[161] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ContinueStatementE")) {
      taken[162] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14BreakStatementE")) {
      taken[163] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14BreakStatementE")) {
      taken[164] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ReturnStatementE")) {
      taken[165] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ReturnStatementE")) {
      taken[166] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15YieldExpressionE")) {
      taken[167] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15YieldExpressionE")) {
      taken[168] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13WithStatementE")) {
      taken[169] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13WithStatementE")) {
      taken[170] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15SwitchStatementE")) {
      taken[171] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15SwitchStatementE")) {
      taken[172] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9CaseBlockE")) {
      taken[173] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9CaseBlockE")) {
      taken[174] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11CaseClausesE")) {
      taken[175] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11CaseClausesE")) {
      taken[176] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10CaseClauseE")) {
      taken[177] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10CaseClauseE")) {
      taken[178] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13DefaultClauseE")) {
      taken[179] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13DefaultClauseE")) {
      taken[180] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17LabelledStatementE")) {
      taken[181] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17LabelledStatementE")) {
      taken[182] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThrowStatementE")) {
      taken[183] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThrowStatementE")) {
      taken[184] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12TryStatementE")) {
      taken[185] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12TryStatementE")) {
      taken[186] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5CatchE")) {
      taken[187] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5CatchE")) {
      taken[188] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7FinallyE")) {
      taken[189] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7FinallyE")) {
      taken[190] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FunctionDeclarationE")) {
      taken[191] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FunctionDeclarationE")) {
      taken[192] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18FunctionExpressionE")) {
      taken[193] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18FunctionExpressionE")) {
      taken[194] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FormalParameterListE")) {
      taken[195] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FormalParameterListE")) {
      taken[196] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ClassExpressionE")) {
      taken[197] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ClassExpressionE")) {
      taken[198] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassDeclarationE")) {
      taken[199] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassDeclarationE")) {
      taken[200] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassElementListE")) {
      taken[201] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassElementListE")) {
      taken[202] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ProgramE")) {
      taken[203] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ProgramE")) {
      taken[204] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15NameSpaceImportE")) {
      taken[205] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15NameSpaceImportE")) {
      taken[206] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ImportSpecifierE")) {
      taken[207] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ImportSpecifierE")) {
      taken[208] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ImportsListE")) {
      taken[209] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ImportsListE")) {
      taken[210] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12NamedImportsE")) {
      taken[211] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12NamedImportsE")) {
      taken[212] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10FromClauseE")) {
      taken[213] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10FromClauseE")) {
      taken[214] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ImportClauseE")) {
      taken[215] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ImportClauseE")) {
      taken[216] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ImportDeclarationE")) {
      taken[217] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ImportDeclarationE")) {
      taken[218] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ExportSpecifierE")) {
      taken[219] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ExportSpecifierE")) {
      taken[220] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ExportsListE")) {
      taken[221] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ExportsListE")) {
      taken[222] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ExportClauseE")) {
      taken[223] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ExportClauseE")) {
      taken[224] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ExportDeclarationE")) {
      taken[225] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ExportDeclarationE")) {
      taken[226] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8ESModuleE")) {
      taken[227] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8ESModuleE")) {
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

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiImport *ast)
  bool visit(QQmlJS::AST::UiImport *ast) override {
    if (taken[0]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall0 call = reinterpret_cast<CuteQmlIR_IRBuilderCall0>(taken[0]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPragma *ast)
  bool visit(QQmlJS::AST::UiPragma *ast) override {
    if (taken[1]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall1 call = reinterpret_cast<CuteQmlIR_IRBuilderCall1>(taken[1]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiProgram *a0)
  bool visit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall2 call = reinterpret_cast<CuteQmlIR_IRBuilderCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(a0);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiArrayBinding *ast)
  bool visit(QQmlJS::AST::UiArrayBinding *ast) override {
    if (taken[3]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall3 call = reinterpret_cast<CuteQmlIR_IRBuilderCall3>(taken[3]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectBinding *ast)
  bool visit(QQmlJS::AST::UiObjectBinding *ast) override {
    if (taken[4]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall4 call = reinterpret_cast<CuteQmlIR_IRBuilderCall4>(taken[4]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectDefinition *ast)
  bool visit(QQmlJS::AST::UiObjectDefinition *ast) override {
    if (taken[5]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall5 call = reinterpret_cast<CuteQmlIR_IRBuilderCall5>(taken[5]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiInlineComponent *ast)
  bool visit(QQmlJS::AST::UiInlineComponent *ast) override {
    if (taken[6]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall6 call = reinterpret_cast<CuteQmlIR_IRBuilderCall6>(taken[6]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiEnumDeclaration *ast)
  bool visit(QQmlJS::AST::UiEnumDeclaration *ast) override {
    if (taken[7]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall7 call = reinterpret_cast<CuteQmlIR_IRBuilderCall7>(taken[7]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPublicMember *ast)
  bool visit(QQmlJS::AST::UiPublicMember *ast) override {
    if (taken[8]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall8 call = reinterpret_cast<CuteQmlIR_IRBuilderCall8>(taken[8]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiScriptBinding *ast)
  bool visit(QQmlJS::AST::UiScriptBinding *ast) override {
    if (taken[9]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall9 call = reinterpret_cast<CuteQmlIR_IRBuilderCall9>(taken[9]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiSourceElement *ast)
  bool visit(QQmlJS::AST::UiSourceElement *ast) override {
    if (taken[10]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall10 call = reinterpret_cast<CuteQmlIR_IRBuilderCall10>(taken[10]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiRequired *ast)
  bool visit(QQmlJS::AST::UiRequired *ast) override {
    if (taken[11]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall11 call = reinterpret_cast<CuteQmlIR_IRBuilderCall11>(taken[11]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  void QmlIR::IRBuilder::throwRecursionDepthError()
  void throwRecursionDepthError() override {
    if (taken[12]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall12 call = reinterpret_cast<CuteQmlIR_IRBuilderCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QmlIR::IRBuilder::throwRecursionDepthError();
  }

  //  void QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding
  //      *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
  //      *parentNode)
  void setBindingValue(
      QV4::CompiledData::Binding *binding,
      QQmlJS::AST::Statement *statement,
      QQmlJS::AST::Node *parentNode) override {
    if (taken[13]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall13 call = reinterpret_cast<CuteQmlIR_IRBuilderCall13>(taken[13]);
      call(this, binding, statement, parentNode, &handled);
      if (handled) return;
    }
    QmlIR::IRBuilder::setBindingValue(binding, statement, parentNode);
  }

  //  void QmlIR::IRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpr
  //      ession *fexp, IsQmlFunction a1)
  void registerFunctionExpr(
      QQmlJS::AST::FunctionExpression *fexp,
      QmlIR::IRBuilder::IsQmlFunction a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall14 call = reinterpret_cast<CuteQmlIR_IRBuilderCall14>(taken[14]);
      call(this, fexp, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QmlIR::IRBuilder::registerFunctionExpr(fexp, a1);
  }

  //  bool QQmlJS::AST::Visitor::preVisit(Node *a0)
  bool preVisit(QQmlJS::AST::Node *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall15 call = reinterpret_cast<CuteQmlIR_IRBuilderCall15>(taken[15]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::preVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::postVisit(Node *a0)
  void postVisit(QQmlJS::AST::Node *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall16 call = reinterpret_cast<CuteQmlIR_IRBuilderCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::postVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)
  void endVisit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall17 call = reinterpret_cast<CuteQmlIR_IRBuilderCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
  bool visit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall18 call = reinterpret_cast<CuteQmlIR_IRBuilderCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
  void endVisit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall19 call = reinterpret_cast<CuteQmlIR_IRBuilderCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
  bool visit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall20 call = reinterpret_cast<CuteQmlIR_IRBuilderCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
  void endVisit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall21 call = reinterpret_cast<CuteQmlIR_IRBuilderCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
  void endVisit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall22 call = reinterpret_cast<CuteQmlIR_IRBuilderCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
  void endVisit(QQmlJS::AST::UiImport *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall23 call = reinterpret_cast<CuteQmlIR_IRBuilderCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)
  void endVisit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall24 call = reinterpret_cast<CuteQmlIR_IRBuilderCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
  void endVisit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall25 call = reinterpret_cast<CuteQmlIR_IRBuilderCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)
  void endVisit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall26 call = reinterpret_cast<CuteQmlIR_IRBuilderCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
  bool visit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall27 call = reinterpret_cast<CuteQmlIR_IRBuilderCall27>(taken[27]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
  void endVisit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall28 call = reinterpret_cast<CuteQmlIR_IRBuilderCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)
  void endVisit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall29 call = reinterpret_cast<CuteQmlIR_IRBuilderCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)
  void endVisit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall30 call = reinterpret_cast<CuteQmlIR_IRBuilderCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)
  void endVisit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall31 call = reinterpret_cast<CuteQmlIR_IRBuilderCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
  bool visit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall32 call = reinterpret_cast<CuteQmlIR_IRBuilderCall32>(taken[32]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
  void endVisit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall33 call = reinterpret_cast<CuteQmlIR_IRBuilderCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
  bool visit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall34 call = reinterpret_cast<CuteQmlIR_IRBuilderCall34>(taken[34]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
  void endVisit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall35 call = reinterpret_cast<CuteQmlIR_IRBuilderCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
  bool visit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall36 call = reinterpret_cast<CuteQmlIR_IRBuilderCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
  void endVisit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall37 call = reinterpret_cast<CuteQmlIR_IRBuilderCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
  bool visit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall38 call = reinterpret_cast<CuteQmlIR_IRBuilderCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
  void endVisit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall39 call = reinterpret_cast<CuteQmlIR_IRBuilderCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
  void endVisit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall40 call = reinterpret_cast<CuteQmlIR_IRBuilderCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
  bool visit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall41 call = reinterpret_cast<CuteQmlIR_IRBuilderCall41>(taken[41]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
  void endVisit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall42 call = reinterpret_cast<CuteQmlIR_IRBuilderCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
  bool visit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall43 call = reinterpret_cast<CuteQmlIR_IRBuilderCall43>(taken[43]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
  void endVisit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall44 call = reinterpret_cast<CuteQmlIR_IRBuilderCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)
  void endVisit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall45 call = reinterpret_cast<CuteQmlIR_IRBuilderCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
  bool visit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall46 call = reinterpret_cast<CuteQmlIR_IRBuilderCall46>(taken[46]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
  void endVisit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall47 call = reinterpret_cast<CuteQmlIR_IRBuilderCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
  bool visit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall48 call = reinterpret_cast<CuteQmlIR_IRBuilderCall48>(taken[48]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
  void endVisit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall49 call = reinterpret_cast<CuteQmlIR_IRBuilderCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
  void endVisit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall50 call = reinterpret_cast<CuteQmlIR_IRBuilderCall50>(taken[50]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
  bool visit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall51 call = reinterpret_cast<CuteQmlIR_IRBuilderCall51>(taken[51]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
  void endVisit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall52 call = reinterpret_cast<CuteQmlIR_IRBuilderCall52>(taken[52]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
  bool visit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[53]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall53 call = reinterpret_cast<CuteQmlIR_IRBuilderCall53>(taken[53]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
  void endVisit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall54 call = reinterpret_cast<CuteQmlIR_IRBuilderCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)
  bool visit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall55 call = reinterpret_cast<CuteQmlIR_IRBuilderCall55>(taken[55]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
  void endVisit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall56 call = reinterpret_cast<CuteQmlIR_IRBuilderCall56>(taken[56]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
  bool visit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall57 call = reinterpret_cast<CuteQmlIR_IRBuilderCall57>(taken[57]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
  void endVisit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[58]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall58 call = reinterpret_cast<CuteQmlIR_IRBuilderCall58>(taken[58]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
  bool visit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall59 call = reinterpret_cast<CuteQmlIR_IRBuilderCall59>(taken[59]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
  void endVisit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall60 call = reinterpret_cast<CuteQmlIR_IRBuilderCall60>(taken[60]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
  bool visit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall61 call = reinterpret_cast<CuteQmlIR_IRBuilderCall61>(taken[61]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
  void endVisit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall62 call = reinterpret_cast<CuteQmlIR_IRBuilderCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
  bool visit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall63 call = reinterpret_cast<CuteQmlIR_IRBuilderCall63>(taken[63]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
  void endVisit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall64 call = reinterpret_cast<CuteQmlIR_IRBuilderCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
  bool visit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall65 call = reinterpret_cast<CuteQmlIR_IRBuilderCall65>(taken[65]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
  void endVisit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall66 call = reinterpret_cast<CuteQmlIR_IRBuilderCall66>(taken[66]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
  bool visit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall67 call = reinterpret_cast<CuteQmlIR_IRBuilderCall67>(taken[67]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
  void endVisit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall68 call = reinterpret_cast<CuteQmlIR_IRBuilderCall68>(taken[68]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
  bool visit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall69 call = reinterpret_cast<CuteQmlIR_IRBuilderCall69>(taken[69]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
  void endVisit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall70 call = reinterpret_cast<CuteQmlIR_IRBuilderCall70>(taken[70]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
  bool visit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall71 call = reinterpret_cast<CuteQmlIR_IRBuilderCall71>(taken[71]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
  void endVisit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall72 call = reinterpret_cast<CuteQmlIR_IRBuilderCall72>(taken[72]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
  bool visit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall73 call = reinterpret_cast<CuteQmlIR_IRBuilderCall73>(taken[73]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
  void endVisit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall74 call = reinterpret_cast<CuteQmlIR_IRBuilderCall74>(taken[74]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
  bool visit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall75 call = reinterpret_cast<CuteQmlIR_IRBuilderCall75>(taken[75]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
  void endVisit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall76 call = reinterpret_cast<CuteQmlIR_IRBuilderCall76>(taken[76]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
  bool visit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[77]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall77 call = reinterpret_cast<CuteQmlIR_IRBuilderCall77>(taken[77]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
  void endVisit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall78 call = reinterpret_cast<CuteQmlIR_IRBuilderCall78>(taken[78]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
  bool visit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall79 call = reinterpret_cast<CuteQmlIR_IRBuilderCall79>(taken[79]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
  void endVisit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall80 call = reinterpret_cast<CuteQmlIR_IRBuilderCall80>(taken[80]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElement *a0)
  bool visit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall81 call = reinterpret_cast<CuteQmlIR_IRBuilderCall81>(taken[81]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
  void endVisit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall82 call = reinterpret_cast<CuteQmlIR_IRBuilderCall82>(taken[82]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
  bool visit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall83 call = reinterpret_cast<CuteQmlIR_IRBuilderCall83>(taken[83]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
  void endVisit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall84 call = reinterpret_cast<CuteQmlIR_IRBuilderCall84>(taken[84]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Elision *a0)
  bool visit(QQmlJS::AST::Elision *a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall85 call = reinterpret_cast<CuteQmlIR_IRBuilderCall85>(taken[85]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
  void endVisit(QQmlJS::AST::Elision *a0) override {
    if (taken[86]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall86 call = reinterpret_cast<CuteQmlIR_IRBuilderCall86>(taken[86]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
  bool visit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[87]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall87 call = reinterpret_cast<CuteQmlIR_IRBuilderCall87>(taken[87]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
  void endVisit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall88 call = reinterpret_cast<CuteQmlIR_IRBuilderCall88>(taken[88]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
  bool visit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall89 call = reinterpret_cast<CuteQmlIR_IRBuilderCall89>(taken[89]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
  void endVisit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[90]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall90 call = reinterpret_cast<CuteQmlIR_IRBuilderCall90>(taken[90]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[91]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall91 call = reinterpret_cast<CuteQmlIR_IRBuilderCall91>(taken[91]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall92 call = reinterpret_cast<CuteQmlIR_IRBuilderCall92>(taken[92]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall93 call = reinterpret_cast<CuteQmlIR_IRBuilderCall93>(taken[93]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall94 call = reinterpret_cast<CuteQmlIR_IRBuilderCall94>(taken[94]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
  bool visit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall95 call = reinterpret_cast<CuteQmlIR_IRBuilderCall95>(taken[95]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
  void endVisit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall96 call = reinterpret_cast<CuteQmlIR_IRBuilderCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
  bool visit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall97 call = reinterpret_cast<CuteQmlIR_IRBuilderCall97>(taken[97]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
  void endVisit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall98 call = reinterpret_cast<CuteQmlIR_IRBuilderCall98>(taken[98]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
  bool visit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall99 call = reinterpret_cast<CuteQmlIR_IRBuilderCall99>(taken[99]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression *a0)
  void endVisit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall100 call = reinterpret_cast<CuteQmlIR_IRBuilderCall100>(taken[100]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
  bool visit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[101]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall101 call = reinterpret_cast<CuteQmlIR_IRBuilderCall101>(taken[101]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
  void endVisit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[102]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall102 call = reinterpret_cast<CuteQmlIR_IRBuilderCall102>(taken[102]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
  bool visit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall103 call = reinterpret_cast<CuteQmlIR_IRBuilderCall103>(taken[103]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
  void endVisit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall104 call = reinterpret_cast<CuteQmlIR_IRBuilderCall104>(taken[104]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
  bool visit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall105 call = reinterpret_cast<CuteQmlIR_IRBuilderCall105>(taken[105]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
  void endVisit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall106 call = reinterpret_cast<CuteQmlIR_IRBuilderCall106>(taken[106]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
  bool visit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall107 call = reinterpret_cast<CuteQmlIR_IRBuilderCall107>(taken[107]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
  void endVisit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall108 call = reinterpret_cast<CuteQmlIR_IRBuilderCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
  bool visit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall109 call = reinterpret_cast<CuteQmlIR_IRBuilderCall109>(taken[109]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
  void endVisit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall110 call = reinterpret_cast<CuteQmlIR_IRBuilderCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
  bool visit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall111 call = reinterpret_cast<CuteQmlIR_IRBuilderCall111>(taken[111]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall112 call = reinterpret_cast<CuteQmlIR_IRBuilderCall112>(taken[112]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
  bool visit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall113 call = reinterpret_cast<CuteQmlIR_IRBuilderCall113>(taken[113]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall114 call = reinterpret_cast<CuteQmlIR_IRBuilderCall114>(taken[114]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
  bool visit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall115 call = reinterpret_cast<CuteQmlIR_IRBuilderCall115>(taken[115]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
  void endVisit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall116 call = reinterpret_cast<CuteQmlIR_IRBuilderCall116>(taken[116]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
  bool visit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall117 call = reinterpret_cast<CuteQmlIR_IRBuilderCall117>(taken[117]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
  void endVisit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[118]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall118 call = reinterpret_cast<CuteQmlIR_IRBuilderCall118>(taken[118]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
  bool visit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[119]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall119 call = reinterpret_cast<CuteQmlIR_IRBuilderCall119>(taken[119]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
  void endVisit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[120]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall120 call = reinterpret_cast<CuteQmlIR_IRBuilderCall120>(taken[120]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
  bool visit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall121 call = reinterpret_cast<CuteQmlIR_IRBuilderCall121>(taken[121]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall122 call = reinterpret_cast<CuteQmlIR_IRBuilderCall122>(taken[122]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
  bool visit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[123]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall123 call = reinterpret_cast<CuteQmlIR_IRBuilderCall123>(taken[123]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[124]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall124 call = reinterpret_cast<CuteQmlIR_IRBuilderCall124>(taken[124]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
  bool visit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[125]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall125 call = reinterpret_cast<CuteQmlIR_IRBuilderCall125>(taken[125]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[126]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall126 call = reinterpret_cast<CuteQmlIR_IRBuilderCall126>(taken[126]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
  bool visit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall127 call = reinterpret_cast<CuteQmlIR_IRBuilderCall127>(taken[127]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall128 call = reinterpret_cast<CuteQmlIR_IRBuilderCall128>(taken[128]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
  bool visit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall129 call = reinterpret_cast<CuteQmlIR_IRBuilderCall129>(taken[129]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
  void endVisit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[130]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall130 call = reinterpret_cast<CuteQmlIR_IRBuilderCall130>(taken[130]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
  bool visit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[131]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall131 call = reinterpret_cast<CuteQmlIR_IRBuilderCall131>(taken[131]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
  void endVisit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[132]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall132 call = reinterpret_cast<CuteQmlIR_IRBuilderCall132>(taken[132]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
  bool visit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall133 call = reinterpret_cast<CuteQmlIR_IRBuilderCall133>(taken[133]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
  void endVisit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[134]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall134 call = reinterpret_cast<CuteQmlIR_IRBuilderCall134>(taken[134]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
  bool visit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[135]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall135 call = reinterpret_cast<CuteQmlIR_IRBuilderCall135>(taken[135]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
  void endVisit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[136]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall136 call = reinterpret_cast<CuteQmlIR_IRBuilderCall136>(taken[136]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
  bool visit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[137]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall137 call = reinterpret_cast<CuteQmlIR_IRBuilderCall137>(taken[137]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
  void endVisit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[138]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall138 call = reinterpret_cast<CuteQmlIR_IRBuilderCall138>(taken[138]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Block *a0)
  bool visit(QQmlJS::AST::Block *a0) override {
    if (taken[139]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall139 call = reinterpret_cast<CuteQmlIR_IRBuilderCall139>(taken[139]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Block *a0)
  void endVisit(QQmlJS::AST::Block *a0) override {
    if (taken[140]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall140 call = reinterpret_cast<CuteQmlIR_IRBuilderCall140>(taken[140]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
  bool visit(QQmlJS::AST::StatementList *a0) override {
    if (taken[141]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall141 call = reinterpret_cast<CuteQmlIR_IRBuilderCall141>(taken[141]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
  void endVisit(QQmlJS::AST::StatementList *a0) override {
    if (taken[142]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall142 call = reinterpret_cast<CuteQmlIR_IRBuilderCall142>(taken[142]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
  bool visit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[143]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall143 call = reinterpret_cast<CuteQmlIR_IRBuilderCall143>(taken[143]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
  void endVisit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[144]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall144 call = reinterpret_cast<CuteQmlIR_IRBuilderCall144>(taken[144]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
  bool visit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[145]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall145 call = reinterpret_cast<CuteQmlIR_IRBuilderCall145>(taken[145]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
  void endVisit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[146]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall146 call = reinterpret_cast<CuteQmlIR_IRBuilderCall146>(taken[146]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
  bool visit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[147]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall147 call = reinterpret_cast<CuteQmlIR_IRBuilderCall147>(taken[147]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
  void endVisit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[148]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall148 call = reinterpret_cast<CuteQmlIR_IRBuilderCall148>(taken[148]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)
  bool visit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[149]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall149 call = reinterpret_cast<CuteQmlIR_IRBuilderCall149>(taken[149]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExpressionStatement *a0)
  void endVisit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[150]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall150 call = reinterpret_cast<CuteQmlIR_IRBuilderCall150>(taken[150]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IfStatement *a0)
  bool visit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[151]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall151 call = reinterpret_cast<CuteQmlIR_IRBuilderCall151>(taken[151]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
  void endVisit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[152]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall152 call = reinterpret_cast<CuteQmlIR_IRBuilderCall152>(taken[152]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
  bool visit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[153]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall153 call = reinterpret_cast<CuteQmlIR_IRBuilderCall153>(taken[153]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
  void endVisit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[154]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall154 call = reinterpret_cast<CuteQmlIR_IRBuilderCall154>(taken[154]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
  bool visit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[155]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall155 call = reinterpret_cast<CuteQmlIR_IRBuilderCall155>(taken[155]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
  void endVisit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[156]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall156 call = reinterpret_cast<CuteQmlIR_IRBuilderCall156>(taken[156]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ForStatement *a0)
  bool visit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[157]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall157 call = reinterpret_cast<CuteQmlIR_IRBuilderCall157>(taken[157]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)
  void endVisit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[158]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall158 call = reinterpret_cast<CuteQmlIR_IRBuilderCall158>(taken[158]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)
  bool visit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[159]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall159 call = reinterpret_cast<CuteQmlIR_IRBuilderCall159>(taken[159]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)
  void endVisit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[160]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall160 call = reinterpret_cast<CuteQmlIR_IRBuilderCall160>(taken[160]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
  bool visit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[161]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall161 call = reinterpret_cast<CuteQmlIR_IRBuilderCall161>(taken[161]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
  void endVisit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[162]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall162 call = reinterpret_cast<CuteQmlIR_IRBuilderCall162>(taken[162]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
  bool visit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[163]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall163 call = reinterpret_cast<CuteQmlIR_IRBuilderCall163>(taken[163]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
  void endVisit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[164]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall164 call = reinterpret_cast<CuteQmlIR_IRBuilderCall164>(taken[164]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
  bool visit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[165]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall165 call = reinterpret_cast<CuteQmlIR_IRBuilderCall165>(taken[165]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
  void endVisit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[166]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall166 call = reinterpret_cast<CuteQmlIR_IRBuilderCall166>(taken[166]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
  bool visit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[167]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall167 call = reinterpret_cast<CuteQmlIR_IRBuilderCall167>(taken[167]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
  void endVisit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[168]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall168 call = reinterpret_cast<CuteQmlIR_IRBuilderCall168>(taken[168]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WithStatement *a0)
  bool visit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[169]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall169 call = reinterpret_cast<CuteQmlIR_IRBuilderCall169>(taken[169]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)
  void endVisit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[170]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall170 call = reinterpret_cast<CuteQmlIR_IRBuilderCall170>(taken[170]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
  bool visit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[171]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall171 call = reinterpret_cast<CuteQmlIR_IRBuilderCall171>(taken[171]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
  void endVisit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[172]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall172 call = reinterpret_cast<CuteQmlIR_IRBuilderCall172>(taken[172]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)
  bool visit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[173]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall173 call = reinterpret_cast<CuteQmlIR_IRBuilderCall173>(taken[173]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)
  void endVisit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[174]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall174 call = reinterpret_cast<CuteQmlIR_IRBuilderCall174>(taken[174]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
  bool visit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[175]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall175 call = reinterpret_cast<CuteQmlIR_IRBuilderCall175>(taken[175]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
  void endVisit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[176]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall176 call = reinterpret_cast<CuteQmlIR_IRBuilderCall176>(taken[176]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
  bool visit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[177]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall177 call = reinterpret_cast<CuteQmlIR_IRBuilderCall177>(taken[177]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
  void endVisit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[178]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall178 call = reinterpret_cast<CuteQmlIR_IRBuilderCall178>(taken[178]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
  bool visit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[179]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall179 call = reinterpret_cast<CuteQmlIR_IRBuilderCall179>(taken[179]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
  void endVisit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[180]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall180 call = reinterpret_cast<CuteQmlIR_IRBuilderCall180>(taken[180]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
  bool visit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[181]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall181 call = reinterpret_cast<CuteQmlIR_IRBuilderCall181>(taken[181]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
  void endVisit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[182]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall182 call = reinterpret_cast<CuteQmlIR_IRBuilderCall182>(taken[182]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
  bool visit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[183]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall183 call = reinterpret_cast<CuteQmlIR_IRBuilderCall183>(taken[183]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
  void endVisit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[184]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall184 call = reinterpret_cast<CuteQmlIR_IRBuilderCall184>(taken[184]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
  bool visit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[185]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall185 call = reinterpret_cast<CuteQmlIR_IRBuilderCall185>(taken[185]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
  void endVisit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[186]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall186 call = reinterpret_cast<CuteQmlIR_IRBuilderCall186>(taken[186]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Catch *a0)
  bool visit(QQmlJS::AST::Catch *a0) override {
    if (taken[187]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall187 call = reinterpret_cast<CuteQmlIR_IRBuilderCall187>(taken[187]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Catch *a0)
  void endVisit(QQmlJS::AST::Catch *a0) override {
    if (taken[188]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall188 call = reinterpret_cast<CuteQmlIR_IRBuilderCall188>(taken[188]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Finally *a0)
  bool visit(QQmlJS::AST::Finally *a0) override {
    if (taken[189]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall189 call = reinterpret_cast<CuteQmlIR_IRBuilderCall189>(taken[189]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
  void endVisit(QQmlJS::AST::Finally *a0) override {
    if (taken[190]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall190 call = reinterpret_cast<CuteQmlIR_IRBuilderCall190>(taken[190]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FunctionDeclaration *a0)
  bool visit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[191]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall191 call = reinterpret_cast<CuteQmlIR_IRBuilderCall191>(taken[191]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration *a0)
  void endVisit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[192]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall192 call = reinterpret_cast<CuteQmlIR_IRBuilderCall192>(taken[192]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FunctionExpression *a0)
  bool visit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[193]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall193 call = reinterpret_cast<CuteQmlIR_IRBuilderCall193>(taken[193]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)
  void endVisit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[194]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall194 call = reinterpret_cast<CuteQmlIR_IRBuilderCall194>(taken[194]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)
  bool visit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[195]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall195 call = reinterpret_cast<CuteQmlIR_IRBuilderCall195>(taken[195]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
  void endVisit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[196]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall196 call = reinterpret_cast<CuteQmlIR_IRBuilderCall196>(taken[196]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)
  bool visit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[197]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall197 call = reinterpret_cast<CuteQmlIR_IRBuilderCall197>(taken[197]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)
  void endVisit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[198]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall198 call = reinterpret_cast<CuteQmlIR_IRBuilderCall198>(taken[198]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)
  bool visit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[199]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall199 call = reinterpret_cast<CuteQmlIR_IRBuilderCall199>(taken[199]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)
  void endVisit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[200]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall200 call = reinterpret_cast<CuteQmlIR_IRBuilderCall200>(taken[200]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
  bool visit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[201]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall201 call = reinterpret_cast<CuteQmlIR_IRBuilderCall201>(taken[201]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
  void endVisit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[202]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall202 call = reinterpret_cast<CuteQmlIR_IRBuilderCall202>(taken[202]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Program *a0)
  bool visit(QQmlJS::AST::Program *a0) override {
    if (taken[203]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall203 call = reinterpret_cast<CuteQmlIR_IRBuilderCall203>(taken[203]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Program *a0)
  void endVisit(QQmlJS::AST::Program *a0) override {
    if (taken[204]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall204 call = reinterpret_cast<CuteQmlIR_IRBuilderCall204>(taken[204]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
  bool visit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[205]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall205 call = reinterpret_cast<CuteQmlIR_IRBuilderCall205>(taken[205]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
  void endVisit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[206]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall206 call = reinterpret_cast<CuteQmlIR_IRBuilderCall206>(taken[206]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
  bool visit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[207]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall207 call = reinterpret_cast<CuteQmlIR_IRBuilderCall207>(taken[207]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
  void endVisit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[208]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall208 call = reinterpret_cast<CuteQmlIR_IRBuilderCall208>(taken[208]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
  bool visit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[209]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall209 call = reinterpret_cast<CuteQmlIR_IRBuilderCall209>(taken[209]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
  void endVisit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[210]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall210 call = reinterpret_cast<CuteQmlIR_IRBuilderCall210>(taken[210]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
  bool visit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[211]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall211 call = reinterpret_cast<CuteQmlIR_IRBuilderCall211>(taken[211]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
  void endVisit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[212]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall212 call = reinterpret_cast<CuteQmlIR_IRBuilderCall212>(taken[212]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
  bool visit(QQmlJS::AST::FromClause *a0) override {
    if (taken[213]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall213 call = reinterpret_cast<CuteQmlIR_IRBuilderCall213>(taken[213]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
  void endVisit(QQmlJS::AST::FromClause *a0) override {
    if (taken[214]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall214 call = reinterpret_cast<CuteQmlIR_IRBuilderCall214>(taken[214]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
  bool visit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[215]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall215 call = reinterpret_cast<CuteQmlIR_IRBuilderCall215>(taken[215]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
  void endVisit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[216]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall216 call = reinterpret_cast<CuteQmlIR_IRBuilderCall216>(taken[216]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
  bool visit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[217]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall217 call = reinterpret_cast<CuteQmlIR_IRBuilderCall217>(taken[217]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
  void endVisit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[218]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall218 call = reinterpret_cast<CuteQmlIR_IRBuilderCall218>(taken[218]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
  bool visit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[219]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall219 call = reinterpret_cast<CuteQmlIR_IRBuilderCall219>(taken[219]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
  void endVisit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[220]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall220 call = reinterpret_cast<CuteQmlIR_IRBuilderCall220>(taken[220]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
  bool visit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[221]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall221 call = reinterpret_cast<CuteQmlIR_IRBuilderCall221>(taken[221]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
  void endVisit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[222]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall222 call = reinterpret_cast<CuteQmlIR_IRBuilderCall222>(taken[222]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
  bool visit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[223]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall223 call = reinterpret_cast<CuteQmlIR_IRBuilderCall223>(taken[223]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
  void endVisit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[224]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall224 call = reinterpret_cast<CuteQmlIR_IRBuilderCall224>(taken[224]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)
  bool visit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[225]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall225 call = reinterpret_cast<CuteQmlIR_IRBuilderCall225>(taken[225]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)
  void endVisit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[226]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall226 call = reinterpret_cast<CuteQmlIR_IRBuilderCall226>(taken[226]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ESModule *a0)
  bool visit(QQmlJS::AST::ESModule *a0) override {
    if (taken[227]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall227 call = reinterpret_cast<CuteQmlIR_IRBuilderCall227>(taken[227]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ESModule *a0)
  void endVisit(QQmlJS::AST::ESModule *a0) override {
    if (taken[228]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall228 call = reinterpret_cast<CuteQmlIR_IRBuilderCall228>(taken[228]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
  bool visit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[229]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall229 call = reinterpret_cast<CuteQmlIR_IRBuilderCall229>(taken[229]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
  void endVisit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[230]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall230 call = reinterpret_cast<CuteQmlIR_IRBuilderCall230>(taken[230]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Type *a0)
  bool visit(QQmlJS::AST::Type *a0) override {
    if (taken[231]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall231 call = reinterpret_cast<CuteQmlIR_IRBuilderCall231>(taken[231]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Type *a0)
  void endVisit(QQmlJS::AST::Type *a0) override {
    if (taken[232]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall232 call = reinterpret_cast<CuteQmlIR_IRBuilderCall232>(taken[232]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
  bool visit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[233]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall233 call = reinterpret_cast<CuteQmlIR_IRBuilderCall233>(taken[233]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
  void endVisit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[234]) {
      int handled = 0;
      CuteQmlIR_IRBuilderCall234 call = reinterpret_cast<CuteQmlIR_IRBuilderCall234>(taken[234]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }
};

//  QString QmlIR::IRBuilder::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QmlIR9IRBuilder2trEPKcS2_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QmlIR::IRBuilder::tr(sourceText, disambiguation, n));
}

//  void QmlIR::IRBuilder::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR9IRBuilder24throwRecursionDepthErrorEv(
    QmlIR::IRBuilder *self) {
  self->throwRecursionDepthError();
}

//  bool QmlIR::IRBuilder::defineQMLObject(int *objectIndex,
//      QQmlJS::AST::UiObjectDefinition *node, Object *declarationsOverride)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QmlIR9IRBuilder15defineQMLObjectEPiPN6QQmlJS3AST18UiObjectDefinitionEPNS_6ObjectE(
    QmlIR::IRBuilder *self,
    int *objectIndex,
    QQmlJS::AST::UiObjectDefinition *node,
    QmlIR::Object *declarationsOverride) {
  return self->defineQMLObject(objectIndex, node, declarationsOverride);
}

//  QStringView QmlIR::IRBuilder::textRefAt(const QQmlJS::SourceLocation
//      &loc) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QmlIR9IRBuilder9textRefAtERKN6QQmlJS14SourceLocationE(
    const QmlIR::IRBuilder *self,
    const QQmlJS::SourceLocation *loc) {
  return new QString(self->textRefAt(*loc).toString());
}

//  void QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding
//      *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
//      *parentNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR9IRBuilder15setBindingValueEPN3QV412CompiledData7BindingEPN6QQmlJS3AST9StatementEPNS6_4NodeE(
    QmlIR::IRBuilder *self,
    QV4::CompiledData::Binding *binding,
    QQmlJS::AST::Statement *statement,
    QQmlJS::AST::Node *parentNode) {
  self->setBindingValue(binding, statement, parentNode);
}

//  void
//      QmlIR::IRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpressio
//      n *fexp, IsQmlFunction a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AST18FunctionExpressionENS0_13IsQmlFunctionE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::FunctionExpression *fexp,
    QmlIR::IRBuilder::IsQmlFunction a1) {
  self->registerFunctionExpr(fexp, a1);
}

//  quint32 QmlIR::IRBuilder::registerString(const QString &str) const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5QmlIR9IRBuilder14registerStringERK7QString(
    const QmlIR::IRBuilder *self,
    const QString *str) {
  return self->registerString(*str);
}

//  QString QmlIR::IRBuilder::stringAt(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QmlIR9IRBuilder8stringAtEi(
    const QmlIR::IRBuilder *self,
    int index) {
  return new QString(self->stringAt(index));
}

//  QmlIR::IRBuilder::~IRBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR9IRBuilderD1Ev(QmlIR::IRBuilder *self) {
  delete self;
}

//  a Python function taken by a CuteQmlIR_IRBuilder, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QmlIR_IRBuilder(
    QmlIR::IRBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQmlIR_IRBuilder *>(self)->take(key, call);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiImport *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST8UiImportE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiImport *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPragma *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST8UiPragmaE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiPragma *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST9UiProgramE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->QmlIR::IRBuilder::visit(a0);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiArrayBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST14UiArrayBindingE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiArrayBinding *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiObjectBindingE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiObjectBinding *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectDefinition *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST18UiObjectDefinitionE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiObjectDefinition *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiInlineComponent *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST17UiInlineComponentE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiInlineComponent *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiEnumDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST17UiEnumDeclarationE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiEnumDeclaration *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPublicMember *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST14UiPublicMemberE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiPublicMember *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiScriptBinding *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiScriptBindingE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiScriptBinding *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiSourceElement *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST15UiSourceElementE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiSourceElement *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiRequired *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QmlIR9IRBuilder5visitEPN6QQmlJS3AST10UiRequiredE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::UiRequired *ast) {
  return self->QmlIR::IRBuilder::visit(ast);
}

//  void QmlIR::IRBuilder::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QmlIR9IRBuilder24throwRecursionDepthErrorEv(
    QmlIR::IRBuilder *self) {
  self->QmlIR::IRBuilder::throwRecursionDepthError();
}

//  void QmlIR::IRBuilder::setBindingValue(QV4::CompiledData::Binding
//      *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
//      *parentNode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QmlIR9IRBuilder15setBindingValueEPN3QV412CompiledData7BindingEPN6QQmlJS3AST9StatementEPNS6_4NodeE(
    QmlIR::IRBuilder *self,
    QV4::CompiledData::Binding *binding,
    QQmlJS::AST::Statement *statement,
    QQmlJS::AST::Node *parentNode) {
  self->QmlIR::IRBuilder::setBindingValue(binding, statement, parentNode);
}

//  void
//      QmlIR::IRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpressio
//      n *fexp, IsQmlFunction a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AST18FunctionExpressionENS0_13IsQmlFunctionE(
    QmlIR::IRBuilder *self,
    QQmlJS::AST::FunctionExpression *fexp,
    QmlIR::IRBuilder::IsQmlFunction a1) {
  self->QmlIR::IRBuilder::registerFunctionExpr(fexp, a1);
}
