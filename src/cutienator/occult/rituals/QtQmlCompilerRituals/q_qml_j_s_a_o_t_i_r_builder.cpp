//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsaotirbuilder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsaotirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJSAOTIRBuilder that Python can take functions over in. Every QQmlJSAOTIRBuilder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlJSAOTIRBuilderCall0)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall1)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall2)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall3)(const void *, QQmlJS::AST::FunctionExpression *, int, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall4)(const void *, QV4::CompiledData::Binding *, QQmlJS::AST::Statement *, QQmlJS::AST::Node *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall5)(const void *, QQmlJS::AST::UiImport *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall6)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall7)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall8)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall9)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall10)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall11)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall12)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall13)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall14)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall15)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall16)(const void *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall17)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall18)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall19)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall20)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall21)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall22)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall23)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall24)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall25)(const void *, QQmlJS::AST::UiImport *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall26)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall27)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall28)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall29)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall30)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall31)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall32)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall33)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall34)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall35)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall36)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall37)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall38)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall39)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall40)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall41)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall42)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall43)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall44)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall45)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall46)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall47)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall48)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall49)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall50)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall51)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall52)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall53)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall54)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall55)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall56)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall57)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall58)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall59)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall60)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall61)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall62)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall63)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall64)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall65)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall66)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall67)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall68)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall69)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall70)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall71)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall72)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall73)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall74)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall75)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall76)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall77)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall78)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall79)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall80)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall81)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall82)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall83)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall84)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall85)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall86)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall87)(const void *, QQmlJS::AST::Elision *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall88)(const void *, QQmlJS::AST::Elision *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall89)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall90)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall91)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall92)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall93)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall94)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall95)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall96)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall97)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall98)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall99)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall100)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall101)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall102)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall103)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall104)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall105)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall106)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall107)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall108)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall109)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall110)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall111)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall112)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall113)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall114)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall115)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall116)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall117)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall118)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall119)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall120)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall121)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall122)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall123)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall124)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall125)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall126)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall127)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall128)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall129)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall130)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall131)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall132)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall133)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall134)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall135)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall136)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall137)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall138)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall139)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall140)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall141)(const void *, QQmlJS::AST::Block *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall142)(const void *, QQmlJS::AST::Block *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall143)(const void *, QQmlJS::AST::StatementList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall144)(const void *, QQmlJS::AST::StatementList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall145)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall146)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall147)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall148)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall149)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall150)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall151)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall152)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall153)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall154)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall155)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall156)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall157)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall158)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall159)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall160)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall161)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall162)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall163)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall164)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall165)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall166)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall167)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall168)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall169)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall170)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall171)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall172)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall173)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall174)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall175)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall176)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall177)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall178)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall179)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall180)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall181)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall182)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall183)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall184)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall185)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall186)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall187)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall188)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall189)(const void *, QQmlJS::AST::Catch *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall190)(const void *, QQmlJS::AST::Catch *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall191)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall192)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall193)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall194)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall195)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall196)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall197)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall198)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall199)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall200)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall201)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall202)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall203)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall204)(const void *, QQmlJS::AST::Program *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall205)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall206)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall207)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall208)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall209)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall210)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall211)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall212)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall213)(const void *, QQmlJS::AST::FromClause *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall214)(const void *, QQmlJS::AST::FromClause *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall215)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall216)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall217)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall218)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall219)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall220)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall221)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall222)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall223)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall224)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall225)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall226)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall227)(const void *, QQmlJS::AST::ESModule *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall228)(const void *, QQmlJS::AST::ESModule *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall229)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall230)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall231)(const void *, QQmlJS::AST::Type *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall232)(const void *, QQmlJS::AST::Type *, int *);
typedef bool (*CuteQQmlJSAOTIRBuilderCall233)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJSAOTIRBuilderCall234)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
class CuteQQmlJSAOTIRBuilder : public QQmlJSAOTIRBuilder {
public:
  using QQmlJSAOTIRBuilder::QQmlJSAOTIRBuilder;
  CuteQQmlJSAOTIRBuilder(const QQmlJSAOTIRBuilder & other) : QQmlJSAOTIRBuilder(other) {}
  void *taken[235] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18FunctionExpressionE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FunctionDeclarationE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiSourceElementE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN5QmlIR9IRBuilder20registerFunctionExprEPN6QQmlJS3AST18FunctionExpressionENS0_13IsQmlFunctionE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN5QmlIR9IRBuilder15setBindingValueEPN3QV412CompiledData7BindingEPN6QQmlJS3AST9StatementEPNS6_4NodeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiImportE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiPragmaE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9UiProgramE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiArrayBindingE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiObjectBindingE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectDefinitionE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiInlineComponentE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiEnumDeclarationE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiPublicMemberE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiScriptBindingE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10UiRequiredE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor24throwRecursionDepthErrorEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8preVisitEPNS0_4NodeE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor9postVisitEPNS0_4NodeE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9UiProgramE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiHeaderItemListE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiHeaderItemListE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiPragmaValueListE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiPragmaValueListE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiPragmaE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiImportE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiPublicMemberE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiSourceElementE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectDefinitionE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UiObjectInitializerE")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UiObjectInitializerE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiObjectBindingE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiScriptBindingE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiArrayBindingE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiParameterListE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiParameterListE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectMemberListE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectMemberListE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiArrayMemberListE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiArrayMemberListE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13UiQualifiedIdE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13UiQualifiedIdE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiEnumDeclarationE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiEnumMemberListE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiEnumMemberListE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiVersionSpecifierE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiVersionSpecifierE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiInlineComponentE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12UiAnnotationE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12UiAnnotationE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiAnnotationListE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiAnnotationListE")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10UiRequiredE")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeExpressionE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeExpressionE")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThisExpressionE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThisExpressionE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20IdentifierExpressionE")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20IdentifierExpressionE")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NullExpressionE")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NullExpressionE")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11TrueLiteralE")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11TrueLiteralE")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12FalseLiteralE")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12FalseLiteralE")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12SuperLiteralE")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12SuperLiteralE")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StringLiteralE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StringLiteralE")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TemplateLiteralE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TemplateLiteralE")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NumericLiteralE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NumericLiteralE")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13RegExpLiteralE")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13RegExpLiteralE")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArrayPatternE")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArrayPatternE")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13ObjectPatternE")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13ObjectPatternE")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18PatternElementListE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18PatternElementListE")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19PatternPropertyListE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19PatternPropertyListE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14PatternElementE")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14PatternElementE")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15PatternPropertyE")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15PatternPropertyE")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ElisionE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ElisionE")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16NestedExpressionE")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16NestedExpressionE")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22IdentifierPropertyNameE")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22IdentifierPropertyNameE")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_25StringLiteralPropertyNameE")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_25StringLiteralPropertyNameE")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20ComputedPropertyNameE")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20ComputedPropertyNameE")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ArrayMemberExpressionE")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ArrayMemberExpressionE")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21FieldMemberExpressionE")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21FieldMemberExpressionE")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TaggedTemplateE")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TaggedTemplateE")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19NewMemberExpressionE")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19NewMemberExpressionE")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NewExpressionE")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NewExpressionE")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14CallExpressionE")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14CallExpressionE")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArgumentListE")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArgumentListE")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostIncrementExpressionE")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostIncrementExpressionE")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostDecrementExpressionE")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostDecrementExpressionE")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DeleteExpressionE")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DeleteExpressionE")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14VoidExpressionE")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14VoidExpressionE")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16TypeOfExpressionE")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16TypeOfExpressionE")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreIncrementExpressionE")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreIncrementExpressionE")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreDecrementExpressionE")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreDecrementExpressionE")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UnaryPlusExpressionE")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UnaryPlusExpressionE")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20UnaryMinusExpressionE")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20UnaryMinusExpressionE")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TildeExpressionE")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TildeExpressionE")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NotExpressionE")) {
      taken[133] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NotExpressionE")) {
      taken[134] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16BinaryExpressionE")) {
      taken[135] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16BinaryExpressionE")) {
      taken[136] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ConditionalExpressionE")) {
      taken[137] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ConditionalExpressionE")) {
      taken[138] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15CommaExpressionE")) {
      taken[139] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15CommaExpressionE")) {
      taken[140] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5BlockE")) {
      taken[141] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5BlockE")) {
      taken[142] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StatementListE")) {
      taken[143] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StatementListE")) {
      taken[144] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17VariableStatementE")) {
      taken[145] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17VariableStatementE")) {
      taken[146] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23VariableDeclarationListE")) {
      taken[147] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23VariableDeclarationListE")) {
      taken[148] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14EmptyStatementE")) {
      taken[149] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14EmptyStatementE")) {
      taken[150] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19ExpressionStatementE")) {
      taken[151] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19ExpressionStatementE")) {
      taken[152] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11IfStatementE")) {
      taken[153] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11IfStatementE")) {
      taken[154] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DoWhileStatementE")) {
      taken[155] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DoWhileStatementE")) {
      taken[156] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14WhileStatementE")) {
      taken[157] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14WhileStatementE")) {
      taken[158] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ForStatementE")) {
      taken[159] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ForStatementE")) {
      taken[160] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ForEachStatementE")) {
      taken[161] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ForEachStatementE")) {
      taken[162] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ContinueStatementE")) {
      taken[163] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ContinueStatementE")) {
      taken[164] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14BreakStatementE")) {
      taken[165] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14BreakStatementE")) {
      taken[166] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ReturnStatementE")) {
      taken[167] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ReturnStatementE")) {
      taken[168] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15YieldExpressionE")) {
      taken[169] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15YieldExpressionE")) {
      taken[170] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13WithStatementE")) {
      taken[171] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13WithStatementE")) {
      taken[172] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15SwitchStatementE")) {
      taken[173] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15SwitchStatementE")) {
      taken[174] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9CaseBlockE")) {
      taken[175] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9CaseBlockE")) {
      taken[176] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11CaseClausesE")) {
      taken[177] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11CaseClausesE")) {
      taken[178] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10CaseClauseE")) {
      taken[179] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10CaseClauseE")) {
      taken[180] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13DefaultClauseE")) {
      taken[181] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13DefaultClauseE")) {
      taken[182] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17LabelledStatementE")) {
      taken[183] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17LabelledStatementE")) {
      taken[184] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThrowStatementE")) {
      taken[185] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThrowStatementE")) {
      taken[186] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12TryStatementE")) {
      taken[187] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12TryStatementE")) {
      taken[188] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5CatchE")) {
      taken[189] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5CatchE")) {
      taken[190] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7FinallyE")) {
      taken[191] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7FinallyE")) {
      taken[192] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FunctionDeclarationE")) {
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

  //  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionExpression *ast)
  bool visit(QQmlJS::AST::FunctionExpression *ast) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall0 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall0>(taken[0]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSAOTIRBuilder::visit(ast);
  }

  //  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionDeclaration *ast)
  bool visit(QQmlJS::AST::FunctionDeclaration *ast) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall1 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall1>(taken[1]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QQmlJSAOTIRBuilder::visit(ast);
  }

  //  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::UiSourceElement *node)
  bool visit(QQmlJS::AST::UiSourceElement *node) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall2 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall2>(taken[2]);
      bool given = call(this, node, &handled);
      if (handled) return given;
    }
    return QQmlJSAOTIRBuilder::visit(node);
  }

  //  void QQmlJSAOTIRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionEx
  //      pression *fexp, IsQmlFunction a1)
  void registerFunctionExpr(
      QQmlJS::AST::FunctionExpression *fexp,
      QmlIR::IRBuilder::IsQmlFunction a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall3 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall3>(taken[3]);
      call(this, fexp, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQmlJSAOTIRBuilder::registerFunctionExpr(fexp, a1);
  }

  //  void QQmlJSAOTIRBuilder::setBindingValue(QV4::CompiledData::Binding
  //      *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
  //      *parentNode)
  void setBindingValue(
      QV4::CompiledData::Binding *binding,
      QQmlJS::AST::Statement *statement,
      QQmlJS::AST::Node *parentNode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall4 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall4>(taken[4]);
      call(this, binding, statement, parentNode, &handled);
      if (handled) return;
    }
    QQmlJSAOTIRBuilder::setBindingValue(binding, statement, parentNode);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiImport *ast)
  bool visit(QQmlJS::AST::UiImport *ast) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall5 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall5>(taken[5]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPragma *ast)
  bool visit(QQmlJS::AST::UiPragma *ast) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall6 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall6>(taken[6]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiProgram *a0)
  bool visit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall7 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall7>(taken[7]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(a0);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiArrayBinding *ast)
  bool visit(QQmlJS::AST::UiArrayBinding *ast) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall8 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall8>(taken[8]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectBinding *ast)
  bool visit(QQmlJS::AST::UiObjectBinding *ast) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall9 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall9>(taken[9]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiObjectDefinition *ast)
  bool visit(QQmlJS::AST::UiObjectDefinition *ast) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall10 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall10>(taken[10]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiInlineComponent *ast)
  bool visit(QQmlJS::AST::UiInlineComponent *ast) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall11 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall11>(taken[11]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiEnumDeclaration *ast)
  bool visit(QQmlJS::AST::UiEnumDeclaration *ast) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall12 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall12>(taken[12]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiPublicMember *ast)
  bool visit(QQmlJS::AST::UiPublicMember *ast) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall13 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall13>(taken[13]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiScriptBinding *ast)
  bool visit(QQmlJS::AST::UiScriptBinding *ast) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall14 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall14>(taken[14]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  bool QmlIR::IRBuilder::visit(QQmlJS::AST::UiRequired *ast)
  bool visit(QQmlJS::AST::UiRequired *ast) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall15 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall15>(taken[15]);
      bool given = call(this, ast, &handled);
      if (handled) return given;
    }
    return QmlIR::IRBuilder::visit(ast);
  }

  //  void QmlIR::IRBuilder::throwRecursionDepthError()
  void throwRecursionDepthError() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall16 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QmlIR::IRBuilder::throwRecursionDepthError();
  }

  //  bool QQmlJS::AST::Visitor::preVisit(Node *a0)
  bool preVisit(QQmlJS::AST::Node *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall17 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::preVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::postVisit(Node *a0)
  void postVisit(QQmlJS::AST::Node *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall18 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::postVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)
  void endVisit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall19 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
  bool visit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall20 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
  void endVisit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall21 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
  bool visit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall22 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall22>(taken[22]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
  void endVisit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall23 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
  void endVisit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall24 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
  void endVisit(QQmlJS::AST::UiImport *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall25 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)
  void endVisit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall26 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
  void endVisit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall27 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)
  void endVisit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall28 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
  bool visit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall29 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall29>(taken[29]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
  void endVisit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall30 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)
  void endVisit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall31 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)
  void endVisit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall32 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)
  void endVisit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall33 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
  bool visit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall34 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall34>(taken[34]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
  void endVisit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall35 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
  bool visit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall36 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
  void endVisit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall37 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
  bool visit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall38 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
  void endVisit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall39 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
  bool visit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall40 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall40>(taken[40]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
  void endVisit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall41 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
  void endVisit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall42 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
  bool visit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall43 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall43>(taken[43]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
  void endVisit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall44 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall44>(taken[44]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
  bool visit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall45 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall45>(taken[45]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
  void endVisit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall46 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall46>(taken[46]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)
  void endVisit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall47 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
  bool visit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall48 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall48>(taken[48]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
  void endVisit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall49 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
  bool visit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall50 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall50>(taken[50]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
  void endVisit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall51 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
  void endVisit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall52 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall52>(taken[52]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
  bool visit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall53 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall53>(taken[53]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
  void endVisit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall54 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
  bool visit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall55 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall55>(taken[55]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
  void endVisit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall56 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall56>(taken[56]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)
  bool visit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall57 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall57>(taken[57]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
  void endVisit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall58 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall58>(taken[58]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
  bool visit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall59 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall59>(taken[59]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
  void endVisit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall60 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall60>(taken[60]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
  bool visit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall61 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall61>(taken[61]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
  void endVisit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall62 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
  bool visit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall63 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall63>(taken[63]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
  void endVisit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall64 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
  bool visit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall65 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall65>(taken[65]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
  void endVisit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall66 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall66>(taken[66]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
  bool visit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall67 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall67>(taken[67]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
  void endVisit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall68 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall68>(taken[68]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
  bool visit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall69 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall69>(taken[69]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
  void endVisit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall70 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall70>(taken[70]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
  bool visit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall71 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall71>(taken[71]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
  void endVisit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall72 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall72>(taken[72]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
  bool visit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall73 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall73>(taken[73]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
  void endVisit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall74 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall74>(taken[74]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
  bool visit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall75 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall75>(taken[75]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
  void endVisit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall76 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall76>(taken[76]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
  bool visit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall77 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall77>(taken[77]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
  void endVisit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall78 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall78>(taken[78]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
  bool visit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall79 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall79>(taken[79]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
  void endVisit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall80 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall80>(taken[80]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
  bool visit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall81 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall81>(taken[81]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
  void endVisit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall82 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall82>(taken[82]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElement *a0)
  bool visit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall83 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall83>(taken[83]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
  void endVisit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall84 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall84>(taken[84]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
  bool visit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall85 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall85>(taken[85]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
  void endVisit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall86 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall86>(taken[86]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Elision *a0)
  bool visit(QQmlJS::AST::Elision *a0) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall87 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall87>(taken[87]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
  void endVisit(QQmlJS::AST::Elision *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall88 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall88>(taken[88]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
  bool visit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall89 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall89>(taken[89]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
  void endVisit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall90 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall90>(taken[90]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
  bool visit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall91 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall91>(taken[91]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
  void endVisit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall92 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall92>(taken[92]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall93 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall93>(taken[93]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall94 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall94>(taken[94]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall95 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall95>(taken[95]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall96 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
  bool visit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall97 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall97>(taken[97]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
  void endVisit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall98 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall98>(taken[98]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
  bool visit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall99 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall99>(taken[99]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
  void endVisit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall100 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall100>(taken[100]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
  bool visit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall101 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall101>(taken[101]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression *a0)
  void endVisit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall102 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall102>(taken[102]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
  bool visit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall103 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall103>(taken[103]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
  void endVisit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall104 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall104>(taken[104]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
  bool visit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall105 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall105>(taken[105]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
  void endVisit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall106 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall106>(taken[106]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
  bool visit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall107 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall107>(taken[107]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
  void endVisit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall108 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
  bool visit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall109 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall109>(taken[109]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
  void endVisit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall110 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
  bool visit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall111 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall111>(taken[111]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
  void endVisit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall112 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall112>(taken[112]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
  bool visit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall113 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall113>(taken[113]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall114 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall114>(taken[114]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
  bool visit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall115 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall115>(taken[115]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall116 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall116>(taken[116]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
  bool visit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall117 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall117>(taken[117]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
  void endVisit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall118 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall118>(taken[118]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
  bool visit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall119 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall119>(taken[119]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
  void endVisit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall120 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall120>(taken[120]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
  bool visit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall121 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall121>(taken[121]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
  void endVisit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall122 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall122>(taken[122]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
  bool visit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall123 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall123>(taken[123]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall124 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall124>(taken[124]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
  bool visit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall125 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall125>(taken[125]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall126 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall126>(taken[126]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
  bool visit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall127 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall127>(taken[127]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall128 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall128>(taken[128]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
  bool visit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall129 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall129>(taken[129]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall130 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall130>(taken[130]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
  bool visit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall131 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall131>(taken[131]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
  void endVisit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall132 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall132>(taken[132]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
  bool visit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall133 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall133>(taken[133]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
  void endVisit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[134]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall134 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall134>(taken[134]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
  bool visit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[135]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall135 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall135>(taken[135]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
  void endVisit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[136]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall136 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall136>(taken[136]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
  bool visit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[137]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall137 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall137>(taken[137]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
  void endVisit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[138]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall138 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall138>(taken[138]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
  bool visit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[139]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall139 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall139>(taken[139]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
  void endVisit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[140]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall140 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall140>(taken[140]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Block *a0)
  bool visit(QQmlJS::AST::Block *a0) override {
    if (taken[141]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall141 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall141>(taken[141]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Block *a0)
  void endVisit(QQmlJS::AST::Block *a0) override {
    if (taken[142]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall142 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall142>(taken[142]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
  bool visit(QQmlJS::AST::StatementList *a0) override {
    if (taken[143]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall143 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall143>(taken[143]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
  void endVisit(QQmlJS::AST::StatementList *a0) override {
    if (taken[144]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall144 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall144>(taken[144]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
  bool visit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[145]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall145 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall145>(taken[145]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
  void endVisit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[146]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall146 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall146>(taken[146]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
  bool visit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[147]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall147 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall147>(taken[147]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
  void endVisit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[148]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall148 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall148>(taken[148]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
  bool visit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[149]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall149 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall149>(taken[149]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
  void endVisit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[150]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall150 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall150>(taken[150]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)
  bool visit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[151]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall151 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall151>(taken[151]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExpressionStatement *a0)
  void endVisit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[152]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall152 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall152>(taken[152]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IfStatement *a0)
  bool visit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[153]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall153 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall153>(taken[153]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
  void endVisit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[154]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall154 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall154>(taken[154]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
  bool visit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[155]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall155 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall155>(taken[155]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
  void endVisit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[156]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall156 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall156>(taken[156]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
  bool visit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[157]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall157 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall157>(taken[157]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
  void endVisit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[158]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall158 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall158>(taken[158]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ForStatement *a0)
  bool visit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[159]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall159 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall159>(taken[159]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)
  void endVisit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[160]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall160 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall160>(taken[160]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)
  bool visit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[161]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall161 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall161>(taken[161]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)
  void endVisit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[162]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall162 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall162>(taken[162]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
  bool visit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[163]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall163 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall163>(taken[163]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
  void endVisit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[164]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall164 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall164>(taken[164]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
  bool visit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[165]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall165 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall165>(taken[165]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
  void endVisit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[166]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall166 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall166>(taken[166]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
  bool visit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[167]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall167 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall167>(taken[167]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
  void endVisit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[168]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall168 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall168>(taken[168]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
  bool visit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[169]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall169 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall169>(taken[169]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
  void endVisit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[170]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall170 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall170>(taken[170]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WithStatement *a0)
  bool visit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[171]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall171 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall171>(taken[171]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)
  void endVisit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[172]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall172 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall172>(taken[172]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
  bool visit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[173]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall173 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall173>(taken[173]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
  void endVisit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[174]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall174 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall174>(taken[174]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)
  bool visit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[175]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall175 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall175>(taken[175]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)
  void endVisit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[176]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall176 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall176>(taken[176]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
  bool visit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[177]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall177 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall177>(taken[177]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
  void endVisit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[178]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall178 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall178>(taken[178]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
  bool visit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[179]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall179 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall179>(taken[179]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
  void endVisit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[180]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall180 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall180>(taken[180]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
  bool visit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[181]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall181 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall181>(taken[181]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
  void endVisit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[182]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall182 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall182>(taken[182]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
  bool visit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[183]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall183 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall183>(taken[183]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
  void endVisit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[184]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall184 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall184>(taken[184]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
  bool visit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[185]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall185 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall185>(taken[185]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
  void endVisit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[186]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall186 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall186>(taken[186]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
  bool visit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[187]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall187 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall187>(taken[187]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
  void endVisit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[188]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall188 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall188>(taken[188]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Catch *a0)
  bool visit(QQmlJS::AST::Catch *a0) override {
    if (taken[189]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall189 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall189>(taken[189]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Catch *a0)
  void endVisit(QQmlJS::AST::Catch *a0) override {
    if (taken[190]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall190 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall190>(taken[190]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Finally *a0)
  bool visit(QQmlJS::AST::Finally *a0) override {
    if (taken[191]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall191 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall191>(taken[191]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
  void endVisit(QQmlJS::AST::Finally *a0) override {
    if (taken[192]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall192 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall192>(taken[192]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration *a0)
  void endVisit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[193]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall193 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall193>(taken[193]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)
  void endVisit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[194]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall194 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall194>(taken[194]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)
  bool visit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[195]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall195 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall195>(taken[195]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
  void endVisit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[196]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall196 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall196>(taken[196]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)
  bool visit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[197]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall197 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall197>(taken[197]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)
  void endVisit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[198]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall198 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall198>(taken[198]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)
  bool visit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[199]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall199 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall199>(taken[199]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)
  void endVisit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[200]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall200 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall200>(taken[200]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
  bool visit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[201]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall201 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall201>(taken[201]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
  void endVisit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[202]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall202 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall202>(taken[202]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Program *a0)
  bool visit(QQmlJS::AST::Program *a0) override {
    if (taken[203]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall203 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall203>(taken[203]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Program *a0)
  void endVisit(QQmlJS::AST::Program *a0) override {
    if (taken[204]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall204 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall204>(taken[204]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
  bool visit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[205]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall205 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall205>(taken[205]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
  void endVisit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[206]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall206 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall206>(taken[206]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
  bool visit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[207]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall207 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall207>(taken[207]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
  void endVisit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[208]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall208 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall208>(taken[208]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
  bool visit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[209]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall209 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall209>(taken[209]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
  void endVisit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[210]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall210 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall210>(taken[210]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
  bool visit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[211]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall211 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall211>(taken[211]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
  void endVisit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[212]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall212 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall212>(taken[212]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
  bool visit(QQmlJS::AST::FromClause *a0) override {
    if (taken[213]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall213 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall213>(taken[213]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
  void endVisit(QQmlJS::AST::FromClause *a0) override {
    if (taken[214]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall214 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall214>(taken[214]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
  bool visit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[215]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall215 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall215>(taken[215]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
  void endVisit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[216]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall216 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall216>(taken[216]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
  bool visit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[217]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall217 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall217>(taken[217]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
  void endVisit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[218]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall218 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall218>(taken[218]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
  bool visit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[219]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall219 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall219>(taken[219]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
  void endVisit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[220]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall220 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall220>(taken[220]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
  bool visit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[221]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall221 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall221>(taken[221]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
  void endVisit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[222]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall222 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall222>(taken[222]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
  bool visit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[223]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall223 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall223>(taken[223]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
  void endVisit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[224]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall224 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall224>(taken[224]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)
  bool visit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[225]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall225 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall225>(taken[225]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)
  void endVisit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[226]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall226 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall226>(taken[226]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ESModule *a0)
  bool visit(QQmlJS::AST::ESModule *a0) override {
    if (taken[227]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall227 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall227>(taken[227]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ESModule *a0)
  void endVisit(QQmlJS::AST::ESModule *a0) override {
    if (taken[228]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall228 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall228>(taken[228]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
  bool visit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[229]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall229 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall229>(taken[229]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
  void endVisit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[230]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall230 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall230>(taken[230]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Type *a0)
  bool visit(QQmlJS::AST::Type *a0) override {
    if (taken[231]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall231 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall231>(taken[231]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Type *a0)
  void endVisit(QQmlJS::AST::Type *a0) override {
    if (taken[232]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall232 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall232>(taken[232]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
  bool visit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[233]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall233 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall233>(taken[233]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
  void endVisit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[234]) {
      int handled = 0;
      CuteQQmlJSAOTIRBuilderCall234 call = reinterpret_cast<CuteQQmlJSAOTIRBuilderCall234>(taken[234]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }
};

//  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::FunctionExpression *ast) {
  return self->visit(ast);
}

//  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::FunctionDeclaration *ast) {
  return self->visit(ast);
}

//  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::UiSourceElement *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST15UiSourceElementE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::UiSourceElement *node) {
  return self->visit(node);
}

//  void
//      QQmlJSAOTIRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpress
//      ion *fexp, IsQmlFunction a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSAOTIRBuilder20registerFunctionExprEPN6QQmlJS3AST18FunctionExpressionEN5QmlIR9IRBuilder13IsQmlFunctionE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::FunctionExpression *fexp,
    QmlIR::IRBuilder::IsQmlFunction a1) {
  self->registerFunctionExpr(fexp, a1);
}

//  void QQmlJSAOTIRBuilder::setBindingValue(QV4::CompiledData::Binding
//      *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
//      *parentNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSAOTIRBuilder15setBindingValueEPN3QV412CompiledData7BindingEPN6QQmlJS3AST9StatementEPNS5_4NodeE(
    QQmlJSAOTIRBuilder *self,
    QV4::CompiledData::Binding *binding,
    QQmlJS::AST::Statement *statement,
    QQmlJS::AST::Node *parentNode) {
  self->setBindingValue(binding, statement, parentNode);
}

//  QQmlJSAOTIRBuilder::~QQmlJSAOTIRBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSAOTIRBuilderD1Ev(QQmlJSAOTIRBuilder *self) {
  delete self;
}

//  a Python function taken by a CuteQQmlJSAOTIRBuilder, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSAOTIRBuilder(
    QQmlJSAOTIRBuilder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSAOTIRBuilder *>(self)->take(key, call);
}

//  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionExpression *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST18FunctionExpressionE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::FunctionExpression *ast) {
  return self->QQmlJSAOTIRBuilder::visit(ast);
}

//  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::FunctionDeclaration *ast)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST19FunctionDeclarationE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::FunctionDeclaration *ast) {
  return self->QQmlJSAOTIRBuilder::visit(ast);
}

//  bool QQmlJSAOTIRBuilder::visit(QQmlJS::AST::UiSourceElement *node)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQmlJSAOTIRBuilder5visitEPN6QQmlJS3AST15UiSourceElementE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::UiSourceElement *node) {
  return self->QQmlJSAOTIRBuilder::visit(node);
}

//  void
//      QQmlJSAOTIRBuilder::registerFunctionExpr(QQmlJS::AST::FunctionExpress
//      ion *fexp, IsQmlFunction a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlJSAOTIRBuilder20registerFunctionExprEPN6QQmlJS3AST18FunctionExpressionEN5QmlIR9IRBuilder13IsQmlFunctionE(
    QQmlJSAOTIRBuilder *self,
    QQmlJS::AST::FunctionExpression *fexp,
    QmlIR::IRBuilder::IsQmlFunction a1) {
  self->QQmlJSAOTIRBuilder::registerFunctionExpr(fexp, a1);
}

//  void QQmlJSAOTIRBuilder::setBindingValue(QV4::CompiledData::Binding
//      *binding, QQmlJS::AST::Statement *statement, QQmlJS::AST::Node
//      *parentNode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlJSAOTIRBuilder15setBindingValueEPN3QV412CompiledData7BindingEPN6QQmlJS3AST9StatementEPNS5_4NodeE(
    QQmlJSAOTIRBuilder *self,
    QV4::CompiledData::Binding *binding,
    QQmlJS::AST::Statement *statement,
    QQmlJS::AST::Node *parentNode) {
  self->QQmlJSAOTIRBuilder::setBindingValue(binding, statement, parentNode);
}
