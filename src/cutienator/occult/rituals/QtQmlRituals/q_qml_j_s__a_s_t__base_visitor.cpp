//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::BaseVisitor that Python can take functions over in. Every QQmlJS::AST::BaseVisitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall0)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall1)(const void *, QQmlJS::AST::Node *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall2)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall3)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall4)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall5)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall6)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall7)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall8)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall9)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall10)(const void *, QQmlJS::AST::UiImport *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall11)(const void *, QQmlJS::AST::UiImport *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall12)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall13)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall14)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall15)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall16)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall17)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall18)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall19)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall20)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall21)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall22)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall23)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall24)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall25)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall26)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall27)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall28)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall29)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall30)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall31)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall32)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall33)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall34)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall35)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall36)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall37)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall38)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall39)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall40)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall41)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall42)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall43)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall44)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall45)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall46)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall47)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall48)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall49)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall50)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall51)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall52)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall53)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall54)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall55)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall56)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall57)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall58)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall59)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall60)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall61)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall62)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall63)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall64)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall65)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall66)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall67)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall68)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall69)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall70)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall71)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall72)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall73)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall74)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall75)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall76)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall77)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall78)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall79)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall80)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall81)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall82)(const void *, QQmlJS::AST::Elision *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall83)(const void *, QQmlJS::AST::Elision *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall84)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall85)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall86)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall87)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall88)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall89)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall90)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall91)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall92)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall93)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall94)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall95)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall96)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall97)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall98)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall99)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall100)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall101)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall102)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall103)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall104)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall105)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall106)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall107)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall108)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall109)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall110)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall111)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall112)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall113)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall114)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall115)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall116)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall117)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall118)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall119)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall120)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall121)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall122)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall123)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall124)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall125)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall126)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall127)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall128)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall129)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall130)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall131)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall132)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall133)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall134)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall135)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall136)(const void *, QQmlJS::AST::Block *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall137)(const void *, QQmlJS::AST::Block *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall138)(const void *, QQmlJS::AST::StatementList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall139)(const void *, QQmlJS::AST::StatementList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall140)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall141)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall142)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall143)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall144)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall145)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall146)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall147)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall148)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall149)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall150)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall151)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall152)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall153)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall154)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall155)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall156)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall157)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall158)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall159)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall160)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall161)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall162)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall163)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall164)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall165)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall166)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall167)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall168)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall169)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall170)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall171)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall172)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall173)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall174)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall175)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall176)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall177)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall178)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall179)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall180)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall181)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall182)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall183)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall184)(const void *, QQmlJS::AST::Catch *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall185)(const void *, QQmlJS::AST::Catch *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall186)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall187)(const void *, QQmlJS::AST::Finally *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall188)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall189)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall190)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall191)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall192)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall193)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall194)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall195)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall196)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall197)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall198)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall199)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall200)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall201)(const void *, QQmlJS::AST::Program *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall202)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall203)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall204)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall205)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall206)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall207)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall208)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall209)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall210)(const void *, QQmlJS::AST::FromClause *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall211)(const void *, QQmlJS::AST::FromClause *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall212)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall213)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall214)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall215)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall216)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall217)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall218)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall219)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall220)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall221)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall222)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall223)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall224)(const void *, QQmlJS::AST::ESModule *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall225)(const void *, QQmlJS::AST::ESModule *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall226)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall227)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall228)(const void *, QQmlJS::AST::Type *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall229)(const void *, QQmlJS::AST::Type *, int *);
typedef bool (*CuteQQmlJS_AST_BaseVisitorCall230)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall231)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_BaseVisitorCall232)(const void *, int *);
class CuteQQmlJS_AST_BaseVisitor : public QQmlJS::AST::BaseVisitor {
public:
  using QQmlJS::AST::BaseVisitor::BaseVisitor;
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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9UiProgramE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9UiProgramE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiHeaderItemListE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiHeaderItemListE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiPragmaValueListE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiPragmaValueListE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiPragmaE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiPragmaE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiImportE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiImportE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiPublicMemberE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiPublicMemberE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiSourceElementE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiSourceElementE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectDefinitionE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectDefinitionE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UiObjectInitializerE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UiObjectInitializerE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiObjectBindingE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiObjectBindingE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiScriptBindingE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiScriptBindingE")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiArrayBindingE")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiArrayBindingE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiParameterListE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiParameterListE")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectMemberListE")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectMemberListE")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiArrayMemberListE")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiArrayMemberListE")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13UiQualifiedIdE")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13UiQualifiedIdE")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiEnumDeclarationE")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiEnumDeclarationE")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiEnumMemberListE")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiEnumMemberListE")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiVersionSpecifierE")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiVersionSpecifierE")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiInlineComponentE")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiInlineComponentE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12UiAnnotationE")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12UiAnnotationE")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiAnnotationListE")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiAnnotationListE")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10UiRequiredE")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10UiRequiredE")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeExpressionE")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeExpressionE")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThisExpressionE")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThisExpressionE")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20IdentifierExpressionE")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20IdentifierExpressionE")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NullExpressionE")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NullExpressionE")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11TrueLiteralE")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11TrueLiteralE")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12FalseLiteralE")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12FalseLiteralE")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12SuperLiteralE")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12SuperLiteralE")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StringLiteralE")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StringLiteralE")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TemplateLiteralE")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TemplateLiteralE")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NumericLiteralE")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NumericLiteralE")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13RegExpLiteralE")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13RegExpLiteralE")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArrayPatternE")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArrayPatternE")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13ObjectPatternE")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13ObjectPatternE")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18PatternElementListE")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18PatternElementListE")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19PatternPropertyListE")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19PatternPropertyListE")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14PatternElementE")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14PatternElementE")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15PatternPropertyE")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15PatternPropertyE")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ElisionE")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ElisionE")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16NestedExpressionE")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16NestedExpressionE")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22IdentifierPropertyNameE")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22IdentifierPropertyNameE")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_25StringLiteralPropertyNameE")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_25StringLiteralPropertyNameE")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20ComputedPropertyNameE")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20ComputedPropertyNameE")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ArrayMemberExpressionE")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ArrayMemberExpressionE")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21FieldMemberExpressionE")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21FieldMemberExpressionE")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TaggedTemplateE")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TaggedTemplateE")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19NewMemberExpressionE")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19NewMemberExpressionE")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NewExpressionE")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NewExpressionE")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14CallExpressionE")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14CallExpressionE")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArgumentListE")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArgumentListE")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostIncrementExpressionE")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostIncrementExpressionE")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostDecrementExpressionE")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostDecrementExpressionE")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DeleteExpressionE")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DeleteExpressionE")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14VoidExpressionE")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14VoidExpressionE")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16TypeOfExpressionE")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16TypeOfExpressionE")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreIncrementExpressionE")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreIncrementExpressionE")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreDecrementExpressionE")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreDecrementExpressionE")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UnaryPlusExpressionE")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UnaryPlusExpressionE")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20UnaryMinusExpressionE")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20UnaryMinusExpressionE")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TildeExpressionE")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TildeExpressionE")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NotExpressionE")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NotExpressionE")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16BinaryExpressionE")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16BinaryExpressionE")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ConditionalExpressionE")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ConditionalExpressionE")) {
      taken[133] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15CommaExpressionE")) {
      taken[134] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15CommaExpressionE")) {
      taken[135] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5BlockE")) {
      taken[136] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5BlockE")) {
      taken[137] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StatementListE")) {
      taken[138] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StatementListE")) {
      taken[139] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17VariableStatementE")) {
      taken[140] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17VariableStatementE")) {
      taken[141] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23VariableDeclarationListE")) {
      taken[142] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23VariableDeclarationListE")) {
      taken[143] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14EmptyStatementE")) {
      taken[144] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14EmptyStatementE")) {
      taken[145] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19ExpressionStatementE")) {
      taken[146] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19ExpressionStatementE")) {
      taken[147] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11IfStatementE")) {
      taken[148] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11IfStatementE")) {
      taken[149] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DoWhileStatementE")) {
      taken[150] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DoWhileStatementE")) {
      taken[151] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14WhileStatementE")) {
      taken[152] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14WhileStatementE")) {
      taken[153] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ForStatementE")) {
      taken[154] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ForStatementE")) {
      taken[155] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ForEachStatementE")) {
      taken[156] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ForEachStatementE")) {
      taken[157] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ContinueStatementE")) {
      taken[158] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ContinueStatementE")) {
      taken[159] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14BreakStatementE")) {
      taken[160] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14BreakStatementE")) {
      taken[161] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ReturnStatementE")) {
      taken[162] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ReturnStatementE")) {
      taken[163] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15YieldExpressionE")) {
      taken[164] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15YieldExpressionE")) {
      taken[165] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13WithStatementE")) {
      taken[166] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13WithStatementE")) {
      taken[167] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15SwitchStatementE")) {
      taken[168] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15SwitchStatementE")) {
      taken[169] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9CaseBlockE")) {
      taken[170] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9CaseBlockE")) {
      taken[171] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11CaseClausesE")) {
      taken[172] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11CaseClausesE")) {
      taken[173] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10CaseClauseE")) {
      taken[174] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10CaseClauseE")) {
      taken[175] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13DefaultClauseE")) {
      taken[176] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13DefaultClauseE")) {
      taken[177] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17LabelledStatementE")) {
      taken[178] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17LabelledStatementE")) {
      taken[179] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThrowStatementE")) {
      taken[180] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThrowStatementE")) {
      taken[181] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12TryStatementE")) {
      taken[182] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12TryStatementE")) {
      taken[183] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5CatchE")) {
      taken[184] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5CatchE")) {
      taken[185] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7FinallyE")) {
      taken[186] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7FinallyE")) {
      taken[187] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FunctionDeclarationE")) {
      taken[188] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FunctionDeclarationE")) {
      taken[189] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18FunctionExpressionE")) {
      taken[190] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18FunctionExpressionE")) {
      taken[191] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FormalParameterListE")) {
      taken[192] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FormalParameterListE")) {
      taken[193] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ClassExpressionE")) {
      taken[194] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ClassExpressionE")) {
      taken[195] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassDeclarationE")) {
      taken[196] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassDeclarationE")) {
      taken[197] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassElementListE")) {
      taken[198] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassElementListE")) {
      taken[199] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ProgramE")) {
      taken[200] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ProgramE")) {
      taken[201] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15NameSpaceImportE")) {
      taken[202] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15NameSpaceImportE")) {
      taken[203] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ImportSpecifierE")) {
      taken[204] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ImportSpecifierE")) {
      taken[205] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ImportsListE")) {
      taken[206] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ImportsListE")) {
      taken[207] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12NamedImportsE")) {
      taken[208] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12NamedImportsE")) {
      taken[209] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10FromClauseE")) {
      taken[210] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10FromClauseE")) {
      taken[211] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ImportClauseE")) {
      taken[212] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ImportClauseE")) {
      taken[213] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ImportDeclarationE")) {
      taken[214] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ImportDeclarationE")) {
      taken[215] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ExportSpecifierE")) {
      taken[216] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ExportSpecifierE")) {
      taken[217] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ExportsListE")) {
      taken[218] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ExportsListE")) {
      taken[219] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ExportClauseE")) {
      taken[220] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ExportClauseE")) {
      taken[221] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ExportDeclarationE")) {
      taken[222] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ExportDeclarationE")) {
      taken[223] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8ESModuleE")) {
      taken[224] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8ESModuleE")) {
      taken[225] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17DebuggerStatementE")) {
      taken[226] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17DebuggerStatementE")) {
      taken[227] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_4TypeE")) {
      taken[228] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_4TypeE")) {
      taken[229] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeAnnotationE")) {
      taken[230] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeAnnotationE")) {
      taken[231] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST11BaseVisitor24throwRecursionDepthErrorEv")) {
      taken[232] = call;
      return true;
    }
    return false;
  }

  //  bool QQmlJS::AST::BaseVisitor::preVisit(Node *a0)
  bool preVisit(QQmlJS::AST::Node *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall0 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::postVisit(Node *a0)
  void postVisit(QQmlJS::AST::Node *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall1 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiProgram *a0)
  bool visit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall2 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiProgram *a0)
  void endVisit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall3 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiHeaderItemList *a0)
  bool visit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall4 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiHeaderItemList *a0)
  void endVisit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall5 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiPragmaValueList *a0)
  bool visit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall6 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiPragmaValueList *a0)
  void endVisit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall7 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiPragma *a0)
  bool visit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall8 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiPragma *a0)
  void endVisit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall9 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiImport *a0)
  bool visit(QQmlJS::AST::UiImport *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall10 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiImport *a0)
  void endVisit(QQmlJS::AST::UiImport *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall11 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiPublicMember *a0)
  bool visit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall12 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiPublicMember *a0)
  void endVisit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall13 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiSourceElement *a0)
  bool visit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall14 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiSourceElement *a0)
  void endVisit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall15 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiObjectDefinition *a0)
  bool visit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall16 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall16>(taken[16]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectDefinition *a0)
  void endVisit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall17 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiObjectInitializer *a0)
  bool visit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall18 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectInitializer *a0)
  void endVisit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall19 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiObjectBinding *a0)
  bool visit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall20 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectBinding *a0)
  void endVisit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall21 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiScriptBinding *a0)
  bool visit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall22 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall22>(taken[22]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiScriptBinding *a0)
  void endVisit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall23 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiArrayBinding *a0)
  bool visit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall24 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall24>(taken[24]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiArrayBinding *a0)
  void endVisit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall25 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiParameterList *a0)
  bool visit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall26 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall26>(taken[26]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiParameterList *a0)
  void endVisit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall27 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiObjectMemberList *a0)
  bool visit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall28 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall28>(taken[28]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectMemberList *a0)
  void endVisit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall29 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiArrayMemberList *a0)
  bool visit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall30 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall30>(taken[30]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiArrayMemberList *a0)
  void endVisit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall31 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiQualifiedId *a0)
  bool visit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall32 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall32>(taken[32]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiQualifiedId *a0)
  void endVisit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall33 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiEnumDeclaration *a0)
  bool visit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall34 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall34>(taken[34]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiEnumDeclaration *a0)
  void endVisit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall35 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiEnumMemberList *a0)
  bool visit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall36 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiEnumMemberList *a0)
  void endVisit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall37 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiVersionSpecifier *a0)
  bool visit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall38 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiVersionSpecifier *a0)
  void endVisit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall39 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiInlineComponent *a0)
  bool visit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall40 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall40>(taken[40]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiInlineComponent *a0)
  void endVisit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall41 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiAnnotation *a0)
  bool visit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall42 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall42>(taken[42]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiAnnotation *a0)
  void endVisit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall43 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiAnnotationList *a0)
  bool visit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall44 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall44>(taken[44]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiAnnotationList *a0)
  void endVisit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall45 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UiRequired *a0)
  bool visit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall46 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall46>(taken[46]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UiRequired *a0)
  void endVisit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall47 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TypeExpression *a0)
  bool visit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall48 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall48>(taken[48]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TypeExpression *a0)
  void endVisit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall49 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ThisExpression *a0)
  bool visit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall50 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall50>(taken[50]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ThisExpression *a0)
  void endVisit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall51 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(IdentifierExpression *a0)
  bool visit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall52 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall52>(taken[52]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(IdentifierExpression *a0)
  void endVisit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall53 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall53>(taken[53]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NullExpression *a0)
  bool visit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall54 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall54>(taken[54]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NullExpression *a0)
  void endVisit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall55 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall55>(taken[55]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TrueLiteral *a0)
  bool visit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall56 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall56>(taken[56]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TrueLiteral *a0)
  void endVisit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall57 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall57>(taken[57]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(FalseLiteral *a0)
  bool visit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall58 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall58>(taken[58]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(FalseLiteral *a0)
  void endVisit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall59 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall59>(taken[59]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(SuperLiteral *a0)
  bool visit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall60 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall60>(taken[60]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(SuperLiteral *a0)
  void endVisit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall61 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(StringLiteral *a0)
  bool visit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall62 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall62>(taken[62]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(StringLiteral *a0)
  void endVisit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall63 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TemplateLiteral *a0)
  bool visit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall64 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall64>(taken[64]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TemplateLiteral *a0)
  void endVisit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall65 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NumericLiteral *a0)
  bool visit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall66 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall66>(taken[66]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NumericLiteral *a0)
  void endVisit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall67 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(RegExpLiteral *a0)
  bool visit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall68 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall68>(taken[68]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(RegExpLiteral *a0)
  void endVisit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall69 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ArrayPattern *a0)
  bool visit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall70 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall70>(taken[70]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ArrayPattern *a0)
  void endVisit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall71 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall71>(taken[71]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ObjectPattern *a0)
  bool visit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall72 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall72>(taken[72]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ObjectPattern *a0)
  void endVisit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall73 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PatternElementList *a0)
  bool visit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall74 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall74>(taken[74]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PatternElementList *a0)
  void endVisit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall75 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall75>(taken[75]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PatternPropertyList *a0)
  bool visit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall76 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall76>(taken[76]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PatternPropertyList *a0)
  void endVisit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall77 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall77>(taken[77]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PatternElement *a0)
  bool visit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall78 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall78>(taken[78]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PatternElement *a0)
  void endVisit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall79 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall79>(taken[79]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PatternProperty *a0)
  bool visit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall80 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall80>(taken[80]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PatternProperty *a0)
  void endVisit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall81 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall81>(taken[81]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(Elision *a0)
  bool visit(QQmlJS::AST::Elision *a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall82 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall82>(taken[82]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(Elision *a0)
  void endVisit(QQmlJS::AST::Elision *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall83 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall83>(taken[83]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NestedExpression *a0)
  bool visit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall84 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall84>(taken[84]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NestedExpression *a0)
  void endVisit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall85 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall85>(taken[85]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(IdentifierPropertyName *a0)
  bool visit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall86 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall86>(taken[86]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(IdentifierPropertyName *a0)
  void endVisit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall87 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall87>(taken[87]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(StringLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall88 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall88>(taken[88]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(StringLiteralPropertyName
  //      *a0)
  void endVisit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall89 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall89>(taken[89]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NumericLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall90 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall90>(taken[90]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NumericLiteralPropertyName
  //      *a0)
  void endVisit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall91 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall91>(taken[91]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ComputedPropertyName *a0)
  bool visit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall92 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall92>(taken[92]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ComputedPropertyName *a0)
  void endVisit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall93 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall93>(taken[93]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ArrayMemberExpression *a0)
  bool visit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall94 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall94>(taken[94]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ArrayMemberExpression *a0)
  void endVisit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall95 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(FieldMemberExpression *a0)
  bool visit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall96 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall96>(taken[96]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(FieldMemberExpression *a0)
  void endVisit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall97 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall97>(taken[97]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TaggedTemplate *a0)
  bool visit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall98 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall98>(taken[98]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TaggedTemplate *a0)
  void endVisit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall99 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall99>(taken[99]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NewMemberExpression *a0)
  bool visit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall100 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall100>(taken[100]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NewMemberExpression *a0)
  void endVisit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall101 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall101>(taken[101]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NewExpression *a0)
  bool visit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall102 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall102>(taken[102]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NewExpression *a0)
  void endVisit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall103 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall103>(taken[103]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(CallExpression *a0)
  bool visit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall104 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall104>(taken[104]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(CallExpression *a0)
  void endVisit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall105 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall105>(taken[105]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ArgumentList *a0)
  bool visit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall106 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall106>(taken[106]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ArgumentList *a0)
  void endVisit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall107 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall107>(taken[107]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PostIncrementExpression *a0)
  bool visit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall108 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall108>(taken[108]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PostIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall109 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall109>(taken[109]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PostDecrementExpression *a0)
  bool visit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall110 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall110>(taken[110]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PostDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall111 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(DeleteExpression *a0)
  bool visit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall112 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall112>(taken[112]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(DeleteExpression *a0)
  void endVisit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall113 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall113>(taken[113]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(VoidExpression *a0)
  bool visit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall114 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall114>(taken[114]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(VoidExpression *a0)
  void endVisit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall115 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall115>(taken[115]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TypeOfExpression *a0)
  bool visit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall116 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall116>(taken[116]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TypeOfExpression *a0)
  void endVisit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall117 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall117>(taken[117]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PreIncrementExpression *a0)
  bool visit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall118 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall118>(taken[118]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PreIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall119 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall119>(taken[119]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(PreDecrementExpression *a0)
  bool visit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall120 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall120>(taken[120]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(PreDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall121 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall121>(taken[121]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UnaryPlusExpression *a0)
  bool visit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall122 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall122>(taken[122]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UnaryPlusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall123 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall123>(taken[123]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(UnaryMinusExpression *a0)
  bool visit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall124 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall124>(taken[124]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(UnaryMinusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall125 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall125>(taken[125]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TildeExpression *a0)
  bool visit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall126 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall126>(taken[126]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TildeExpression *a0)
  void endVisit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall127 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall127>(taken[127]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NotExpression *a0)
  bool visit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall128 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall128>(taken[128]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NotExpression *a0)
  void endVisit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall129 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall129>(taken[129]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(BinaryExpression *a0)
  bool visit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall130 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall130>(taken[130]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(BinaryExpression *a0)
  void endVisit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall131 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall131>(taken[131]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ConditionalExpression *a0)
  bool visit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall132 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall132>(taken[132]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ConditionalExpression *a0)
  void endVisit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall133 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall133>(taken[133]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(CommaExpression *a0)
  bool visit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[134]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall134 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall134>(taken[134]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(CommaExpression *a0)
  void endVisit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[135]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall135 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall135>(taken[135]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(Block *a0)
  bool visit(QQmlJS::AST::Block *a0) override {
    if (taken[136]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall136 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall136>(taken[136]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(Block *a0)
  void endVisit(QQmlJS::AST::Block *a0) override {
    if (taken[137]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall137 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall137>(taken[137]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(StatementList *a0)
  bool visit(QQmlJS::AST::StatementList *a0) override {
    if (taken[138]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall138 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall138>(taken[138]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(StatementList *a0)
  void endVisit(QQmlJS::AST::StatementList *a0) override {
    if (taken[139]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall139 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall139>(taken[139]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(VariableStatement *a0)
  bool visit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[140]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall140 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall140>(taken[140]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(VariableStatement *a0)
  void endVisit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[141]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall141 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall141>(taken[141]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(VariableDeclarationList *a0)
  bool visit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[142]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall142 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall142>(taken[142]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(VariableDeclarationList *a0)
  void endVisit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[143]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall143 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall143>(taken[143]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(EmptyStatement *a0)
  bool visit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[144]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall144 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall144>(taken[144]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(EmptyStatement *a0)
  void endVisit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[145]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall145 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall145>(taken[145]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ExpressionStatement *a0)
  bool visit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[146]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall146 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall146>(taken[146]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ExpressionStatement *a0)
  void endVisit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[147]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall147 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall147>(taken[147]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(IfStatement *a0)
  bool visit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[148]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall148 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall148>(taken[148]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(IfStatement *a0)
  void endVisit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[149]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall149 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall149>(taken[149]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(DoWhileStatement *a0)
  bool visit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[150]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall150 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall150>(taken[150]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(DoWhileStatement *a0)
  void endVisit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[151]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall151 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall151>(taken[151]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(WhileStatement *a0)
  bool visit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[152]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall152 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall152>(taken[152]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(WhileStatement *a0)
  void endVisit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[153]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall153 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall153>(taken[153]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ForStatement *a0)
  bool visit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[154]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall154 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall154>(taken[154]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ForStatement *a0)
  void endVisit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[155]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall155 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall155>(taken[155]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ForEachStatement *a0)
  bool visit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[156]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall156 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall156>(taken[156]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ForEachStatement *a0)
  void endVisit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[157]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall157 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall157>(taken[157]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ContinueStatement *a0)
  bool visit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[158]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall158 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall158>(taken[158]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ContinueStatement *a0)
  void endVisit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[159]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall159 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall159>(taken[159]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(BreakStatement *a0)
  bool visit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[160]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall160 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall160>(taken[160]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(BreakStatement *a0)
  void endVisit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[161]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall161 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall161>(taken[161]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ReturnStatement *a0)
  bool visit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[162]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall162 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall162>(taken[162]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ReturnStatement *a0)
  void endVisit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[163]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall163 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall163>(taken[163]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(YieldExpression *a0)
  bool visit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[164]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall164 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall164>(taken[164]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(YieldExpression *a0)
  void endVisit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[165]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall165 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall165>(taken[165]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(WithStatement *a0)
  bool visit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[166]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall166 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall166>(taken[166]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(WithStatement *a0)
  void endVisit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[167]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall167 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall167>(taken[167]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(SwitchStatement *a0)
  bool visit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[168]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall168 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall168>(taken[168]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(SwitchStatement *a0)
  void endVisit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[169]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall169 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall169>(taken[169]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(CaseBlock *a0)
  bool visit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[170]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall170 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall170>(taken[170]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(CaseBlock *a0)
  void endVisit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[171]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall171 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall171>(taken[171]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(CaseClauses *a0)
  bool visit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[172]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall172 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall172>(taken[172]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(CaseClauses *a0)
  void endVisit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[173]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall173 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall173>(taken[173]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(CaseClause *a0)
  bool visit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[174]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall174 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall174>(taken[174]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(CaseClause *a0)
  void endVisit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[175]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall175 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall175>(taken[175]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(DefaultClause *a0)
  bool visit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[176]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall176 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall176>(taken[176]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(DefaultClause *a0)
  void endVisit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[177]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall177 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall177>(taken[177]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(LabelledStatement *a0)
  bool visit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[178]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall178 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall178>(taken[178]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(LabelledStatement *a0)
  void endVisit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[179]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall179 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall179>(taken[179]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ThrowStatement *a0)
  bool visit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[180]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall180 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall180>(taken[180]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ThrowStatement *a0)
  void endVisit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[181]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall181 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall181>(taken[181]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TryStatement *a0)
  bool visit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[182]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall182 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall182>(taken[182]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TryStatement *a0)
  void endVisit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[183]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall183 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall183>(taken[183]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(Catch *a0)
  bool visit(QQmlJS::AST::Catch *a0) override {
    if (taken[184]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall184 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall184>(taken[184]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(Catch *a0)
  void endVisit(QQmlJS::AST::Catch *a0) override {
    if (taken[185]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall185 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall185>(taken[185]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(Finally *a0)
  bool visit(QQmlJS::AST::Finally *a0) override {
    if (taken[186]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall186 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall186>(taken[186]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(Finally *a0)
  void endVisit(QQmlJS::AST::Finally *a0) override {
    if (taken[187]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall187 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall187>(taken[187]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(FunctionDeclaration *a0)
  bool visit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[188]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall188 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall188>(taken[188]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(FunctionDeclaration *a0)
  void endVisit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[189]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall189 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall189>(taken[189]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(FunctionExpression *a0)
  bool visit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[190]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall190 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall190>(taken[190]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(FunctionExpression *a0)
  void endVisit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[191]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall191 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall191>(taken[191]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(FormalParameterList *a0)
  bool visit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[192]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall192 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall192>(taken[192]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(FormalParameterList *a0)
  void endVisit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[193]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall193 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall193>(taken[193]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ClassExpression *a0)
  bool visit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[194]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall194 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall194>(taken[194]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ClassExpression *a0)
  void endVisit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[195]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall195 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall195>(taken[195]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ClassDeclaration *a0)
  bool visit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[196]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall196 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall196>(taken[196]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ClassDeclaration *a0)
  void endVisit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[197]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall197 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall197>(taken[197]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ClassElementList *a0)
  bool visit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[198]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall198 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall198>(taken[198]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ClassElementList *a0)
  void endVisit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[199]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall199 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall199>(taken[199]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(Program *a0)
  bool visit(QQmlJS::AST::Program *a0) override {
    if (taken[200]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall200 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall200>(taken[200]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(Program *a0)
  void endVisit(QQmlJS::AST::Program *a0) override {
    if (taken[201]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall201 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall201>(taken[201]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NameSpaceImport *a0)
  bool visit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[202]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall202 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall202>(taken[202]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NameSpaceImport *a0)
  void endVisit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[203]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall203 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall203>(taken[203]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ImportSpecifier *a0)
  bool visit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[204]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall204 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall204>(taken[204]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ImportSpecifier *a0)
  void endVisit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[205]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall205 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall205>(taken[205]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ImportsList *a0)
  bool visit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[206]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall206 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall206>(taken[206]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ImportsList *a0)
  void endVisit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[207]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall207 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall207>(taken[207]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(NamedImports *a0)
  bool visit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[208]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall208 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall208>(taken[208]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(NamedImports *a0)
  void endVisit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[209]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall209 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall209>(taken[209]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(FromClause *a0)
  bool visit(QQmlJS::AST::FromClause *a0) override {
    if (taken[210]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall210 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall210>(taken[210]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(FromClause *a0)
  void endVisit(QQmlJS::AST::FromClause *a0) override {
    if (taken[211]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall211 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall211>(taken[211]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ImportClause *a0)
  bool visit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[212]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall212 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall212>(taken[212]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ImportClause *a0)
  void endVisit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[213]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall213 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall213>(taken[213]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ImportDeclaration *a0)
  bool visit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[214]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall214 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall214>(taken[214]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ImportDeclaration *a0)
  void endVisit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[215]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall215 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall215>(taken[215]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ExportSpecifier *a0)
  bool visit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[216]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall216 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall216>(taken[216]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ExportSpecifier *a0)
  void endVisit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[217]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall217 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall217>(taken[217]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ExportsList *a0)
  bool visit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[218]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall218 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall218>(taken[218]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ExportsList *a0)
  void endVisit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[219]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall219 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall219>(taken[219]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ExportClause *a0)
  bool visit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[220]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall220 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall220>(taken[220]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ExportClause *a0)
  void endVisit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[221]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall221 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall221>(taken[221]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ExportDeclaration *a0)
  bool visit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[222]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall222 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall222>(taken[222]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ExportDeclaration *a0)
  void endVisit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[223]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall223 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall223>(taken[223]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(ESModule *a0)
  bool visit(QQmlJS::AST::ESModule *a0) override {
    if (taken[224]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall224 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall224>(taken[224]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(ESModule *a0)
  void endVisit(QQmlJS::AST::ESModule *a0) override {
    if (taken[225]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall225 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall225>(taken[225]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(DebuggerStatement *a0)
  bool visit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[226]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall226 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall226>(taken[226]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(DebuggerStatement *a0)
  void endVisit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[227]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall227 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall227>(taken[227]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(Type *a0)
  bool visit(QQmlJS::AST::Type *a0) override {
    if (taken[228]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall228 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall228>(taken[228]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(Type *a0)
  void endVisit(QQmlJS::AST::Type *a0) override {
    if (taken[229]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall229 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall229>(taken[229]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  bool QQmlJS::AST::BaseVisitor::visit(TypeAnnotation *a0)
  bool visit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[230]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall230 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall230>(taken[230]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QQmlJS::AST::BaseVisitor::endVisit(TypeAnnotation *a0)
  void endVisit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[231]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall231 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall231>(taken[231]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }

  //  void QQmlJS::AST::BaseVisitor::throwRecursionDepthError()
  void throwRecursionDepthError() override {
    if (taken[232]) {
      int handled = 0;
      CuteQQmlJS_AST_BaseVisitorCall232 call = reinterpret_cast<CuteQQmlJS_AST_BaseVisitorCall232>(taken[232]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QQmlJS::AST::BaseVisitor::BaseVisitor(quint16 parentRecursionDepth)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::BaseVisitor *ritual_ZN6QQmlJS3AST11BaseVisitorC1Et(
    quint16 parentRecursionDepth) {
  return new CuteQQmlJS_AST_BaseVisitor(parentRecursionDepth);
}

//  QQmlJS::AST::BaseVisitor::~BaseVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitorD1Ev(QQmlJS::AST::BaseVisitor *self) {
  delete self;
}

//  bool QQmlJS::AST::BaseVisitor::preVisit(Node *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor8preVisitEPNS0_4NodeE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Node *a0) {
  return self->preVisit(a0);
}

//  void QQmlJS::AST::BaseVisitor::postVisit(Node *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor9postVisitEPNS0_4NodeE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Node *a0) {
  self->postVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9UiProgramE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9UiProgramE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiProgram *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiPragmaE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiPragma *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiPragmaE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiPragma *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8UiImportE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiImport *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8UiImportE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiImport *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiSourceElementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiSourceElementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15UiParameterListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15UiParameterListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12UiAnnotationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12UiAnnotationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10UiRequiredE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiRequired *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10UiRequiredE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UiRequired *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThisExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThisExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NullExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NullExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NullExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NullExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11TrueLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11TrueLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12FalseLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12FalseLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12SuperLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12SuperLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StringLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StringLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14NumericLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14NumericLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArrayPatternE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArrayPatternE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13ObjectPatternE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13ObjectPatternE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18PatternElementListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18PatternElementListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14PatternElementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14PatternElementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternElement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15PatternPropertyE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15PatternPropertyE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(Elision *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ElisionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Elision *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(Elision *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ElisionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Elision *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16NestedExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16NestedExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NewExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NewExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NewExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NewExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14CallExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CallExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14CallExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CallExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ArgumentListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ArgumentListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14VoidExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14VoidExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15TildeExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15TildeExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13NotExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NotExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13NotExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NotExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15CommaExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15CommaExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(Block *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5BlockE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Block *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(Block *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5BlockE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Block *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(StatementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13StatementListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::StatementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(StatementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13StatementListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::StatementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17VariableStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17VariableStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14EmptyStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14EmptyStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11IfStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11IfStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::IfStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14WhileStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14WhileStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ForStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ForStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ForStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ForStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ForEachStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ForEachStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ContinueStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ContinueStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14BreakStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14BreakStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ReturnStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ReturnStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15YieldExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15YieldExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13WithStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::WithStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13WithStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::WithStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15SwitchStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15SwitchStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_9CaseBlockE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_9CaseBlockE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11CaseClausesE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11CaseClausesE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10CaseClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CaseClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10CaseClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::CaseClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_13DefaultClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_13DefaultClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17LabelledStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17LabelledStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14ThrowStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14ThrowStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12TryStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TryStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12TryStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TryStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(Catch *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_5CatchE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Catch *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(Catch *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_5CatchE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Catch *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(Finally *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7FinallyE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Finally *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(Finally *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7FinallyE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Finally *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_19FormalParameterListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_19FormalParameterListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ClassExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ClassExpressionE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_16ClassElementListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_16ClassElementListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(Program *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_7ProgramE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Program *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_7ProgramE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Program *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ImportsListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportsList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ImportsListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportsList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12NamedImportsE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NamedImports *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12NamedImportsE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::NamedImports *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(FromClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_10FromClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FromClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(FromClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_10FromClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::FromClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ImportClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ImportClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_11ExportsListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportsList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_11ExportsListE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportsList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_12ExportClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_12ExportClauseE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(ESModule *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_8ESModuleE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ESModule *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_8ESModuleE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::ESModule *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(Type *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_4TypeE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Type *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(Type *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_4TypeE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::Type *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::BaseVisitor::visit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST11BaseVisitor5visitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::BaseVisitor::endVisit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor8endVisitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::BaseVisitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  self->endVisit(a0);
}

//  void QQmlJS::AST::BaseVisitor::throwRecursionDepthError()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST11BaseVisitor24throwRecursionDepthErrorEv(
    QQmlJS::AST::BaseVisitor *self) {
  self->throwRecursionDepthError();
}

//  quint16 QQmlJS::AST::BaseVisitor::recursionDepth() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK6QQmlJS3AST11BaseVisitor14recursionDepthEv(
    const QQmlJS::AST::BaseVisitor *self) {
  return self->recursionDepth();
}

//  a Python function taken by a CuteQQmlJS_AST_BaseVisitor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_BaseVisitor(
    QQmlJS::AST::BaseVisitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_BaseVisitor *>(self)->take(key, call);
}
