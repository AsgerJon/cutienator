//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsastvisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::Visitor that Python can take functions over in. Every QQmlJS::AST::Visitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlJS_AST_VisitorCall0)(const void *, QQmlJS::AST::Node *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall1)(const void *, QQmlJS::AST::Node *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall2)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall3)(const void *, QQmlJS::AST::UiProgram *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall4)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall5)(const void *, QQmlJS::AST::UiHeaderItemList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall6)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall7)(const void *, QQmlJS::AST::UiPragmaValueList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall8)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall9)(const void *, QQmlJS::AST::UiPragma *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall10)(const void *, QQmlJS::AST::UiImport *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall11)(const void *, QQmlJS::AST::UiImport *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall12)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall13)(const void *, QQmlJS::AST::UiPublicMember *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall14)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall15)(const void *, QQmlJS::AST::UiSourceElement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall16)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall17)(const void *, QQmlJS::AST::UiObjectDefinition *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall18)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall19)(const void *, QQmlJS::AST::UiObjectInitializer *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall20)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall21)(const void *, QQmlJS::AST::UiObjectBinding *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall22)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall23)(const void *, QQmlJS::AST::UiScriptBinding *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall24)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall25)(const void *, QQmlJS::AST::UiArrayBinding *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall26)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall27)(const void *, QQmlJS::AST::UiParameterList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall28)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall29)(const void *, QQmlJS::AST::UiObjectMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall30)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall31)(const void *, QQmlJS::AST::UiArrayMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall32)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall33)(const void *, QQmlJS::AST::UiQualifiedId *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall34)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall35)(const void *, QQmlJS::AST::UiEnumDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall36)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall37)(const void *, QQmlJS::AST::UiEnumMemberList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall38)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall39)(const void *, QQmlJS::AST::UiVersionSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall40)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall41)(const void *, QQmlJS::AST::UiInlineComponent *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall42)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall43)(const void *, QQmlJS::AST::UiAnnotation *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall44)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall45)(const void *, QQmlJS::AST::UiAnnotationList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall46)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall47)(const void *, QQmlJS::AST::UiRequired *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall48)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall49)(const void *, QQmlJS::AST::TypeExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall50)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall51)(const void *, QQmlJS::AST::ThisExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall52)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall53)(const void *, QQmlJS::AST::IdentifierExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall54)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall55)(const void *, QQmlJS::AST::NullExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall56)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall57)(const void *, QQmlJS::AST::TrueLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall58)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall59)(const void *, QQmlJS::AST::FalseLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall60)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall61)(const void *, QQmlJS::AST::SuperLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall62)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall63)(const void *, QQmlJS::AST::StringLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall64)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall65)(const void *, QQmlJS::AST::TemplateLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall66)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall67)(const void *, QQmlJS::AST::NumericLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall68)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall69)(const void *, QQmlJS::AST::RegExpLiteral *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall70)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall71)(const void *, QQmlJS::AST::ArrayPattern *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall72)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall73)(const void *, QQmlJS::AST::ObjectPattern *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall74)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall75)(const void *, QQmlJS::AST::PatternElementList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall76)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall77)(const void *, QQmlJS::AST::PatternPropertyList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall78)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall79)(const void *, QQmlJS::AST::PatternElement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall80)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall81)(const void *, QQmlJS::AST::PatternProperty *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall82)(const void *, QQmlJS::AST::Elision *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall83)(const void *, QQmlJS::AST::Elision *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall84)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall85)(const void *, QQmlJS::AST::NestedExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall86)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall87)(const void *, QQmlJS::AST::IdentifierPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall88)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall89)(const void *, QQmlJS::AST::StringLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall90)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall91)(const void *, QQmlJS::AST::NumericLiteralPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall92)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall93)(const void *, QQmlJS::AST::ComputedPropertyName *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall94)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall95)(const void *, QQmlJS::AST::ArrayMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall96)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall97)(const void *, QQmlJS::AST::FieldMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall98)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall99)(const void *, QQmlJS::AST::TaggedTemplate *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall100)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall101)(const void *, QQmlJS::AST::NewMemberExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall102)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall103)(const void *, QQmlJS::AST::NewExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall104)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall105)(const void *, QQmlJS::AST::CallExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall106)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall107)(const void *, QQmlJS::AST::ArgumentList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall108)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall109)(const void *, QQmlJS::AST::PostIncrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall110)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall111)(const void *, QQmlJS::AST::PostDecrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall112)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall113)(const void *, QQmlJS::AST::DeleteExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall114)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall115)(const void *, QQmlJS::AST::VoidExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall116)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall117)(const void *, QQmlJS::AST::TypeOfExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall118)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall119)(const void *, QQmlJS::AST::PreIncrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall120)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall121)(const void *, QQmlJS::AST::PreDecrementExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall122)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall123)(const void *, QQmlJS::AST::UnaryPlusExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall124)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall125)(const void *, QQmlJS::AST::UnaryMinusExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall126)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall127)(const void *, QQmlJS::AST::TildeExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall128)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall129)(const void *, QQmlJS::AST::NotExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall130)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall131)(const void *, QQmlJS::AST::BinaryExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall132)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall133)(const void *, QQmlJS::AST::ConditionalExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall134)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall135)(const void *, QQmlJS::AST::CommaExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall136)(const void *, QQmlJS::AST::Block *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall137)(const void *, QQmlJS::AST::Block *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall138)(const void *, QQmlJS::AST::StatementList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall139)(const void *, QQmlJS::AST::StatementList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall140)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall141)(const void *, QQmlJS::AST::VariableStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall142)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall143)(const void *, QQmlJS::AST::VariableDeclarationList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall144)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall145)(const void *, QQmlJS::AST::EmptyStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall146)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall147)(const void *, QQmlJS::AST::ExpressionStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall148)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall149)(const void *, QQmlJS::AST::IfStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall150)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall151)(const void *, QQmlJS::AST::DoWhileStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall152)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall153)(const void *, QQmlJS::AST::WhileStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall154)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall155)(const void *, QQmlJS::AST::ForStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall156)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall157)(const void *, QQmlJS::AST::ForEachStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall158)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall159)(const void *, QQmlJS::AST::ContinueStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall160)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall161)(const void *, QQmlJS::AST::BreakStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall162)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall163)(const void *, QQmlJS::AST::ReturnStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall164)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall165)(const void *, QQmlJS::AST::YieldExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall166)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall167)(const void *, QQmlJS::AST::WithStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall168)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall169)(const void *, QQmlJS::AST::SwitchStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall170)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall171)(const void *, QQmlJS::AST::CaseBlock *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall172)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall173)(const void *, QQmlJS::AST::CaseClauses *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall174)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall175)(const void *, QQmlJS::AST::CaseClause *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall176)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall177)(const void *, QQmlJS::AST::DefaultClause *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall178)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall179)(const void *, QQmlJS::AST::LabelledStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall180)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall181)(const void *, QQmlJS::AST::ThrowStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall182)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall183)(const void *, QQmlJS::AST::TryStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall184)(const void *, QQmlJS::AST::Catch *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall185)(const void *, QQmlJS::AST::Catch *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall186)(const void *, QQmlJS::AST::Finally *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall187)(const void *, QQmlJS::AST::Finally *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall188)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall189)(const void *, QQmlJS::AST::FunctionDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall190)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall191)(const void *, QQmlJS::AST::FunctionExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall192)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall193)(const void *, QQmlJS::AST::FormalParameterList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall194)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall195)(const void *, QQmlJS::AST::ClassExpression *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall196)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall197)(const void *, QQmlJS::AST::ClassDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall198)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall199)(const void *, QQmlJS::AST::ClassElementList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall200)(const void *, QQmlJS::AST::Program *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall201)(const void *, QQmlJS::AST::Program *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall202)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall203)(const void *, QQmlJS::AST::NameSpaceImport *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall204)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall205)(const void *, QQmlJS::AST::ImportSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall206)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall207)(const void *, QQmlJS::AST::ImportsList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall208)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall209)(const void *, QQmlJS::AST::NamedImports *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall210)(const void *, QQmlJS::AST::FromClause *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall211)(const void *, QQmlJS::AST::FromClause *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall212)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall213)(const void *, QQmlJS::AST::ImportClause *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall214)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall215)(const void *, QQmlJS::AST::ImportDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall216)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall217)(const void *, QQmlJS::AST::ExportSpecifier *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall218)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall219)(const void *, QQmlJS::AST::ExportsList *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall220)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall221)(const void *, QQmlJS::AST::ExportClause *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall222)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall223)(const void *, QQmlJS::AST::ExportDeclaration *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall224)(const void *, QQmlJS::AST::ESModule *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall225)(const void *, QQmlJS::AST::ESModule *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall226)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall227)(const void *, QQmlJS::AST::DebuggerStatement *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall228)(const void *, QQmlJS::AST::Type *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall229)(const void *, QQmlJS::AST::Type *, int *);
typedef bool (*CuteQQmlJS_AST_VisitorCall230)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall231)(const void *, QQmlJS::AST::TypeAnnotation *, int *);
typedef void (*CuteQQmlJS_AST_VisitorCall232)(const void *, int *);
class CuteQQmlJS_AST_Visitor : public QQmlJS::AST::Visitor {
public:
  using QQmlJS::AST::Visitor::Visitor;
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

  //  bool QQmlJS::AST::Visitor::preVisit(Node *a0)
  bool preVisit(QQmlJS::AST::Node *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall0 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::preVisit(a0);
  }

  //  void QQmlJS::AST::Visitor::postVisit(Node *a0)
  void postVisit(QQmlJS::AST::Node *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall1 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::postVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiProgram *a0)
  bool visit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall2 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)
  void endVisit(QQmlJS::AST::UiProgram *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall3 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
  bool visit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall4 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall4>(taken[4]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
  void endVisit(QQmlJS::AST::UiHeaderItemList *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall5 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
  bool visit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall6 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
  void endVisit(QQmlJS::AST::UiPragmaValueList *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall7 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiPragma *a0)
  bool visit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall8 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
  void endVisit(QQmlJS::AST::UiPragma *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall9 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiImport *a0)
  bool visit(QQmlJS::AST::UiImport *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall10 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
  void endVisit(QQmlJS::AST::UiImport *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall11 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiPublicMember *a0)
  bool visit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall12 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall12>(taken[12]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)
  void endVisit(QQmlJS::AST::UiPublicMember *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall13 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiSourceElement *a0)
  bool visit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall14 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall14>(taken[14]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
  void endVisit(QQmlJS::AST::UiSourceElement *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall15 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectDefinition *a0)
  bool visit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall16 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall16>(taken[16]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)
  void endVisit(QQmlJS::AST::UiObjectDefinition *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall17 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
  bool visit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall18 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
  void endVisit(QQmlJS::AST::UiObjectInitializer *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall19 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectBinding *a0)
  bool visit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall20 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)
  void endVisit(QQmlJS::AST::UiObjectBinding *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall21 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiScriptBinding *a0)
  bool visit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall22 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall22>(taken[22]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)
  void endVisit(QQmlJS::AST::UiScriptBinding *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall23 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiArrayBinding *a0)
  bool visit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall24 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall24>(taken[24]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)
  void endVisit(QQmlJS::AST::UiArrayBinding *a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall25 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
  bool visit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall26 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall26>(taken[26]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
  void endVisit(QQmlJS::AST::UiParameterList *a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall27 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
  bool visit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall28 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall28>(taken[28]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
  void endVisit(QQmlJS::AST::UiObjectMemberList *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall29 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
  bool visit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall30 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall30>(taken[30]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
  void endVisit(QQmlJS::AST::UiArrayMemberList *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall31 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
  bool visit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall32 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall32>(taken[32]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
  void endVisit(QQmlJS::AST::UiQualifiedId *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall33 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiEnumDeclaration *a0)
  bool visit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall34 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall34>(taken[34]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
  void endVisit(QQmlJS::AST::UiEnumDeclaration *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall35 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
  bool visit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall36 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall36>(taken[36]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
  void endVisit(QQmlJS::AST::UiEnumMemberList *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall37 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
  bool visit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall38 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall38>(taken[38]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
  void endVisit(QQmlJS::AST::UiVersionSpecifier *a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall39 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiInlineComponent *a0)
  bool visit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall40 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall40>(taken[40]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)
  void endVisit(QQmlJS::AST::UiInlineComponent *a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall41 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
  bool visit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall42 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall42>(taken[42]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
  void endVisit(QQmlJS::AST::UiAnnotation *a0) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall43 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall43>(taken[43]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
  bool visit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall44 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall44>(taken[44]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
  void endVisit(QQmlJS::AST::UiAnnotationList *a0) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall45 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall45>(taken[45]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UiRequired *a0)
  bool visit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall46 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall46>(taken[46]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
  void endVisit(QQmlJS::AST::UiRequired *a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall47 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
  bool visit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall48 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall48>(taken[48]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
  void endVisit(QQmlJS::AST::TypeExpression *a0) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall49 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall49>(taken[49]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
  bool visit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall50 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall50>(taken[50]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
  void endVisit(QQmlJS::AST::ThisExpression *a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall51 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)
  bool visit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall52 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall52>(taken[52]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
  void endVisit(QQmlJS::AST::IdentifierExpression *a0) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall53 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall53>(taken[53]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
  bool visit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall54 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall54>(taken[54]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
  void endVisit(QQmlJS::AST::NullExpression *a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall55 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall55>(taken[55]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
  bool visit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall56 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall56>(taken[56]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
  void endVisit(QQmlJS::AST::TrueLiteral *a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall57 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall57>(taken[57]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
  bool visit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall58 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall58>(taken[58]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
  void endVisit(QQmlJS::AST::FalseLiteral *a0) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall59 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall59>(taken[59]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
  bool visit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall60 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall60>(taken[60]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
  void endVisit(QQmlJS::AST::SuperLiteral *a0) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall61 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall61>(taken[61]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
  bool visit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall62 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall62>(taken[62]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
  void endVisit(QQmlJS::AST::StringLiteral *a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall63 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
  bool visit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall64 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall64>(taken[64]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
  void endVisit(QQmlJS::AST::TemplateLiteral *a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall65 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
  bool visit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall66 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall66>(taken[66]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
  void endVisit(QQmlJS::AST::NumericLiteral *a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall67 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
  bool visit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall68 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall68>(taken[68]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
  void endVisit(QQmlJS::AST::RegExpLiteral *a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall69 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
  bool visit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall70 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall70>(taken[70]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
  void endVisit(QQmlJS::AST::ArrayPattern *a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall71 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall71>(taken[71]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
  bool visit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall72 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall72>(taken[72]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
  void endVisit(QQmlJS::AST::ObjectPattern *a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall73 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
  bool visit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall74 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall74>(taken[74]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
  void endVisit(QQmlJS::AST::PatternElementList *a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall75 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall75>(taken[75]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
  bool visit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall76 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall76>(taken[76]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
  void endVisit(QQmlJS::AST::PatternPropertyList *a0) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall77 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall77>(taken[77]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternElement *a0)
  bool visit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall78 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall78>(taken[78]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
  void endVisit(QQmlJS::AST::PatternElement *a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall79 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall79>(taken[79]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
  bool visit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall80 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall80>(taken[80]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
  void endVisit(QQmlJS::AST::PatternProperty *a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall81 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall81>(taken[81]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Elision *a0)
  bool visit(QQmlJS::AST::Elision *a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall82 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall82>(taken[82]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
  void endVisit(QQmlJS::AST::Elision *a0) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall83 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall83>(taken[83]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
  bool visit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall84 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall84>(taken[84]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
  void endVisit(QQmlJS::AST::NestedExpression *a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall85 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall85>(taken[85]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
  bool visit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall86 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall86>(taken[86]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
  void endVisit(QQmlJS::AST::IdentifierPropertyName *a0) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall87 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall87>(taken[87]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall88 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall88>(taken[88]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::StringLiteralPropertyName *a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall89 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall89>(taken[89]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
  bool visit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall90 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall90>(taken[90]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
  void endVisit(QQmlJS::AST::NumericLiteralPropertyName *a0) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall91 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall91>(taken[91]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
  bool visit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall92 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall92>(taken[92]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
  void endVisit(QQmlJS::AST::ComputedPropertyName *a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall93 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall93>(taken[93]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
  bool visit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall94 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall94>(taken[94]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
  void endVisit(QQmlJS::AST::ArrayMemberExpression *a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall95 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
  bool visit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall96 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall96>(taken[96]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression *a0)
  void endVisit(QQmlJS::AST::FieldMemberExpression *a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall97 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall97>(taken[97]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
  bool visit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall98 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall98>(taken[98]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
  void endVisit(QQmlJS::AST::TaggedTemplate *a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall99 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall99>(taken[99]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
  bool visit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall100 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall100>(taken[100]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
  void endVisit(QQmlJS::AST::NewMemberExpression *a0) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall101 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall101>(taken[101]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
  bool visit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall102 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall102>(taken[102]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
  void endVisit(QQmlJS::AST::NewExpression *a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall103 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall103>(taken[103]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
  bool visit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall104 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall104>(taken[104]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
  void endVisit(QQmlJS::AST::CallExpression *a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall105 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall105>(taken[105]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
  bool visit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall106 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall106>(taken[106]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
  void endVisit(QQmlJS::AST::ArgumentList *a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall107 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall107>(taken[107]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
  bool visit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall108 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall108>(taken[108]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PostIncrementExpression *a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall109 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall109>(taken[109]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
  bool visit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall110 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall110>(taken[110]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PostDecrementExpression *a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall111 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
  bool visit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall112 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall112>(taken[112]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
  void endVisit(QQmlJS::AST::DeleteExpression *a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall113 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall113>(taken[113]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
  bool visit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall114 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall114>(taken[114]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
  void endVisit(QQmlJS::AST::VoidExpression *a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall115 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall115>(taken[115]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
  bool visit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall116 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall116>(taken[116]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
  void endVisit(QQmlJS::AST::TypeOfExpression *a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall117 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall117>(taken[117]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
  bool visit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall118 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall118>(taken[118]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
  void endVisit(QQmlJS::AST::PreIncrementExpression *a0) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall119 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall119>(taken[119]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
  bool visit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall120 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall120>(taken[120]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
  void endVisit(QQmlJS::AST::PreDecrementExpression *a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall121 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall121>(taken[121]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
  bool visit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall122 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall122>(taken[122]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryPlusExpression *a0) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall123 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall123>(taken[123]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
  bool visit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall124 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall124>(taken[124]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
  void endVisit(QQmlJS::AST::UnaryMinusExpression *a0) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall125 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall125>(taken[125]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
  bool visit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall126 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall126>(taken[126]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
  void endVisit(QQmlJS::AST::TildeExpression *a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall127 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall127>(taken[127]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
  bool visit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall128 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall128>(taken[128]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
  void endVisit(QQmlJS::AST::NotExpression *a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall129 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall129>(taken[129]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
  bool visit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall130 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall130>(taken[130]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
  void endVisit(QQmlJS::AST::BinaryExpression *a0) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall131 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall131>(taken[131]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
  bool visit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall132 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall132>(taken[132]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
  void endVisit(QQmlJS::AST::ConditionalExpression *a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall133 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall133>(taken[133]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
  bool visit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[134]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall134 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall134>(taken[134]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
  void endVisit(QQmlJS::AST::CommaExpression *a0) override {
    if (taken[135]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall135 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall135>(taken[135]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Block *a0)
  bool visit(QQmlJS::AST::Block *a0) override {
    if (taken[136]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall136 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall136>(taken[136]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Block *a0)
  void endVisit(QQmlJS::AST::Block *a0) override {
    if (taken[137]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall137 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall137>(taken[137]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
  bool visit(QQmlJS::AST::StatementList *a0) override {
    if (taken[138]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall138 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall138>(taken[138]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
  void endVisit(QQmlJS::AST::StatementList *a0) override {
    if (taken[139]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall139 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall139>(taken[139]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
  bool visit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[140]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall140 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall140>(taken[140]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
  void endVisit(QQmlJS::AST::VariableStatement *a0) override {
    if (taken[141]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall141 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall141>(taken[141]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
  bool visit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[142]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall142 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall142>(taken[142]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
  void endVisit(QQmlJS::AST::VariableDeclarationList *a0) override {
    if (taken[143]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall143 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall143>(taken[143]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
  bool visit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[144]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall144 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall144>(taken[144]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
  void endVisit(QQmlJS::AST::EmptyStatement *a0) override {
    if (taken[145]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall145 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall145>(taken[145]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)
  bool visit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[146]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall146 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall146>(taken[146]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExpressionStatement *a0)
  void endVisit(QQmlJS::AST::ExpressionStatement *a0) override {
    if (taken[147]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall147 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall147>(taken[147]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(IfStatement *a0)
  bool visit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[148]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall148 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall148>(taken[148]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
  void endVisit(QQmlJS::AST::IfStatement *a0) override {
    if (taken[149]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall149 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall149>(taken[149]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
  bool visit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[150]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall150 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall150>(taken[150]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
  void endVisit(QQmlJS::AST::DoWhileStatement *a0) override {
    if (taken[151]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall151 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall151>(taken[151]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
  bool visit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[152]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall152 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall152>(taken[152]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
  void endVisit(QQmlJS::AST::WhileStatement *a0) override {
    if (taken[153]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall153 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall153>(taken[153]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ForStatement *a0)
  bool visit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[154]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall154 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall154>(taken[154]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)
  void endVisit(QQmlJS::AST::ForStatement *a0) override {
    if (taken[155]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall155 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall155>(taken[155]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)
  bool visit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[156]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall156 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall156>(taken[156]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)
  void endVisit(QQmlJS::AST::ForEachStatement *a0) override {
    if (taken[157]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall157 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall157>(taken[157]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
  bool visit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[158]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall158 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall158>(taken[158]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
  void endVisit(QQmlJS::AST::ContinueStatement *a0) override {
    if (taken[159]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall159 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall159>(taken[159]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
  bool visit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[160]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall160 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall160>(taken[160]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
  void endVisit(QQmlJS::AST::BreakStatement *a0) override {
    if (taken[161]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall161 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall161>(taken[161]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
  bool visit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[162]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall162 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall162>(taken[162]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
  void endVisit(QQmlJS::AST::ReturnStatement *a0) override {
    if (taken[163]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall163 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall163>(taken[163]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
  bool visit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[164]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall164 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall164>(taken[164]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
  void endVisit(QQmlJS::AST::YieldExpression *a0) override {
    if (taken[165]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall165 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall165>(taken[165]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(WithStatement *a0)
  bool visit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[166]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall166 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall166>(taken[166]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)
  void endVisit(QQmlJS::AST::WithStatement *a0) override {
    if (taken[167]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall167 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall167>(taken[167]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
  bool visit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[168]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall168 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall168>(taken[168]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
  void endVisit(QQmlJS::AST::SwitchStatement *a0) override {
    if (taken[169]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall169 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall169>(taken[169]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)
  bool visit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[170]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall170 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall170>(taken[170]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)
  void endVisit(QQmlJS::AST::CaseBlock *a0) override {
    if (taken[171]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall171 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall171>(taken[171]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
  bool visit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[172]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall172 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall172>(taken[172]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
  void endVisit(QQmlJS::AST::CaseClauses *a0) override {
    if (taken[173]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall173 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall173>(taken[173]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
  bool visit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[174]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall174 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall174>(taken[174]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
  void endVisit(QQmlJS::AST::CaseClause *a0) override {
    if (taken[175]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall175 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall175>(taken[175]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
  bool visit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[176]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall176 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall176>(taken[176]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
  void endVisit(QQmlJS::AST::DefaultClause *a0) override {
    if (taken[177]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall177 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall177>(taken[177]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
  bool visit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[178]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall178 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall178>(taken[178]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
  void endVisit(QQmlJS::AST::LabelledStatement *a0) override {
    if (taken[179]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall179 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall179>(taken[179]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
  bool visit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[180]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall180 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall180>(taken[180]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
  void endVisit(QQmlJS::AST::ThrowStatement *a0) override {
    if (taken[181]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall181 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall181>(taken[181]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
  bool visit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[182]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall182 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall182>(taken[182]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
  void endVisit(QQmlJS::AST::TryStatement *a0) override {
    if (taken[183]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall183 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall183>(taken[183]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Catch *a0)
  bool visit(QQmlJS::AST::Catch *a0) override {
    if (taken[184]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall184 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall184>(taken[184]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Catch *a0)
  void endVisit(QQmlJS::AST::Catch *a0) override {
    if (taken[185]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall185 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall185>(taken[185]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Finally *a0)
  bool visit(QQmlJS::AST::Finally *a0) override {
    if (taken[186]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall186 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall186>(taken[186]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
  void endVisit(QQmlJS::AST::Finally *a0) override {
    if (taken[187]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall187 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall187>(taken[187]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FunctionDeclaration *a0)
  bool visit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[188]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall188 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall188>(taken[188]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration *a0)
  void endVisit(QQmlJS::AST::FunctionDeclaration *a0) override {
    if (taken[189]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall189 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall189>(taken[189]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FunctionExpression *a0)
  bool visit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[190]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall190 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall190>(taken[190]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)
  void endVisit(QQmlJS::AST::FunctionExpression *a0) override {
    if (taken[191]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall191 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall191>(taken[191]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)
  bool visit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[192]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall192 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall192>(taken[192]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
  void endVisit(QQmlJS::AST::FormalParameterList *a0) override {
    if (taken[193]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall193 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall193>(taken[193]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)
  bool visit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[194]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall194 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall194>(taken[194]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)
  void endVisit(QQmlJS::AST::ClassExpression *a0) override {
    if (taken[195]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall195 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall195>(taken[195]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)
  bool visit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[196]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall196 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall196>(taken[196]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)
  void endVisit(QQmlJS::AST::ClassDeclaration *a0) override {
    if (taken[197]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall197 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall197>(taken[197]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
  bool visit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[198]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall198 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall198>(taken[198]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
  void endVisit(QQmlJS::AST::ClassElementList *a0) override {
    if (taken[199]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall199 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall199>(taken[199]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Program *a0)
  bool visit(QQmlJS::AST::Program *a0) override {
    if (taken[200]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall200 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall200>(taken[200]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Program *a0)
  void endVisit(QQmlJS::AST::Program *a0) override {
    if (taken[201]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall201 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall201>(taken[201]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
  bool visit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[202]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall202 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall202>(taken[202]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
  void endVisit(QQmlJS::AST::NameSpaceImport *a0) override {
    if (taken[203]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall203 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall203>(taken[203]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
  bool visit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[204]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall204 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall204>(taken[204]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
  void endVisit(QQmlJS::AST::ImportSpecifier *a0) override {
    if (taken[205]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall205 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall205>(taken[205]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
  bool visit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[206]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall206 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall206>(taken[206]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
  void endVisit(QQmlJS::AST::ImportsList *a0) override {
    if (taken[207]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall207 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall207>(taken[207]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
  bool visit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[208]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall208 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall208>(taken[208]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
  void endVisit(QQmlJS::AST::NamedImports *a0) override {
    if (taken[209]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall209 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall209>(taken[209]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
  bool visit(QQmlJS::AST::FromClause *a0) override {
    if (taken[210]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall210 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall210>(taken[210]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
  void endVisit(QQmlJS::AST::FromClause *a0) override {
    if (taken[211]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall211 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall211>(taken[211]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
  bool visit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[212]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall212 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall212>(taken[212]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
  void endVisit(QQmlJS::AST::ImportClause *a0) override {
    if (taken[213]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall213 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall213>(taken[213]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
  bool visit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[214]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall214 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall214>(taken[214]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
  void endVisit(QQmlJS::AST::ImportDeclaration *a0) override {
    if (taken[215]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall215 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall215>(taken[215]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
  bool visit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[216]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall216 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall216>(taken[216]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
  void endVisit(QQmlJS::AST::ExportSpecifier *a0) override {
    if (taken[217]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall217 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall217>(taken[217]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
  bool visit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[218]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall218 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall218>(taken[218]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
  void endVisit(QQmlJS::AST::ExportsList *a0) override {
    if (taken[219]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall219 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall219>(taken[219]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
  bool visit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[220]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall220 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall220>(taken[220]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
  void endVisit(QQmlJS::AST::ExportClause *a0) override {
    if (taken[221]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall221 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall221>(taken[221]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)
  bool visit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[222]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall222 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall222>(taken[222]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)
  void endVisit(QQmlJS::AST::ExportDeclaration *a0) override {
    if (taken[223]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall223 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall223>(taken[223]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(ESModule *a0)
  bool visit(QQmlJS::AST::ESModule *a0) override {
    if (taken[224]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall224 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall224>(taken[224]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(ESModule *a0)
  void endVisit(QQmlJS::AST::ESModule *a0) override {
    if (taken[225]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall225 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall225>(taken[225]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
  bool visit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[226]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall226 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall226>(taken[226]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
  void endVisit(QQmlJS::AST::DebuggerStatement *a0) override {
    if (taken[227]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall227 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall227>(taken[227]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(Type *a0)
  bool visit(QQmlJS::AST::Type *a0) override {
    if (taken[228]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall228 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall228>(taken[228]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(Type *a0)
  void endVisit(QQmlJS::AST::Type *a0) override {
    if (taken[229]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall229 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall229>(taken[229]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
  bool visit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[230]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall230 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall230>(taken[230]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::Visitor::visit(a0);
  }

  //  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
  void endVisit(QQmlJS::AST::TypeAnnotation *a0) override {
    if (taken[231]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall231 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall231>(taken[231]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJS::AST::Visitor::endVisit(a0);
  }

  //  void QQmlJS::AST::BaseVisitor::throwRecursionDepthError()
  void throwRecursionDepthError() override {
    if (taken[232]) {
      int handled = 0;
      CuteQQmlJS_AST_VisitorCall232 call = reinterpret_cast<CuteQQmlJS_AST_VisitorCall232>(taken[232]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QQmlJS::AST::Visitor::Visitor(quint16 parentRecursionDepth)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Visitor *ritual_ZN6QQmlJS3AST7VisitorC1Et(
    quint16 parentRecursionDepth) {
  return new CuteQQmlJS_AST_Visitor(parentRecursionDepth);
}

//  bool QQmlJS::AST::Visitor::preVisit(Node *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor8preVisitEPNS0_4NodeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Node *a0) {
  return self->preVisit(a0);
}

//  void QQmlJS::AST::Visitor::postVisit(Node *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor9postVisitEPNS0_4NodeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Node *a0) {
  self->postVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_9UiProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9UiProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiProgram *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiPragmaE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragma *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiPragmaE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragma *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiImport *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiImport *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiSourceElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiSourceElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12UiAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12UiAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_10UiRequiredE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiRequired *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10UiRequiredE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiRequired *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThisExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThisExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NullExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NullExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NullExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NullExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11TrueLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11TrueLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12FalseLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12FalseLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12SuperLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12SuperLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StringLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StringLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NumericLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NumericLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArrayPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArrayPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13ObjectPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13ObjectPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18PatternElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18PatternElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14PatternElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14PatternElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15PatternPropertyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15PatternPropertyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Elision *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ElisionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Elision *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ElisionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Elision *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16NestedExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16NestedExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NewExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NewExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14CallExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CallExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14CallExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CallExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArgumentListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArgumentListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14VoidExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14VoidExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TildeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TildeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NotExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NotExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NotExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NotExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15CommaExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15CommaExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Block *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_5BlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Block *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Block *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5BlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Block *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StatementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StatementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StatementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StatementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17VariableStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17VariableStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14EmptyStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14EmptyStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11IfStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11IfStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IfStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14WhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14WhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ForStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ForStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ForEachStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ForEachStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ContinueStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ContinueStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14BreakStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14BreakStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ReturnStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ReturnStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15YieldExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15YieldExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13WithStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WithStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13WithStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WithStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15SwitchStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15SwitchStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_9CaseBlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9CaseBlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11CaseClausesE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11CaseClausesE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_10CaseClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10CaseClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_13DefaultClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13DefaultClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17LabelledStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17LabelledStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThrowStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThrowStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12TryStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TryStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12TryStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TryStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Catch *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_5CatchE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Catch *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Catch *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5CatchE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Catch *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Finally *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_7FinallyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Finally *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7FinallyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Finally *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FormalParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FormalParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ClassExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ClassExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Program *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Program *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Program *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ImportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportsList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ImportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportsList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12NamedImportsE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NamedImports *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12NamedImportsE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NamedImports *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_10FromClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FromClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10FromClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FromClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ImportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ImportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ExportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportsList *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ExportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportsList *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ExportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportClause *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ExportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportClause *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ESModule *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_8ESModuleE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ESModule *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8ESModuleE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ESModule *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Type *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_4TypeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Type *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Type *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_4TypeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Type *a0) {
  self->endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  return self->visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  self->endVisit(a0);
}

//  a Python function taken by a CuteQQmlJS_AST_Visitor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_Visitor(
    QQmlJS::AST::Visitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_Visitor *>(self)->take(key, call);
}

//  bool QQmlJS::AST::Visitor::preVisit(Node *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor8preVisitEPNS0_4NodeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Node *a0) {
  return self->QQmlJS::AST::Visitor::preVisit(a0);
}

//  void QQmlJS::AST::Visitor::postVisit(Node *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor9postVisitEPNS0_4NodeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Node *a0) {
  self->QQmlJS::AST::Visitor::postVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_9UiProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiProgram *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiProgram *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9UiProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiProgram *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiHeaderItemList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiHeaderItemListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiHeaderItemList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiPragmaValueList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiPragmaValueListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragmaValueList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiPragmaE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragma *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiPragma *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiPragmaE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPragma *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_8UiImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiImport *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8UiImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiImport *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiPublicMember *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiPublicMemberE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiPublicMember *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiSourceElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiSourceElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiSourceElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiSourceElement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectDefinition *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectDefinitionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectDefinition *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectInitializer *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UiObjectInitializerE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectInitializer *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiObjectBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectBinding *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiScriptBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiScriptBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiScriptBinding *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiArrayBinding *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14UiArrayBindingE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayBinding *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15UiParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15UiParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiParameterList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiObjectMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiObjectMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiObjectMemberList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiArrayMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiArrayMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiArrayMemberList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiQualifiedId *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13UiQualifiedIdE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiQualifiedId *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiEnumDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiEnumDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumDeclaration *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiEnumMemberList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiEnumMemberListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiEnumMemberList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiVersionSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18UiVersionSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiVersionSpecifier *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiInlineComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17UiInlineComponentE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiInlineComponent *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12UiAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12UiAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotation *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiAnnotationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16UiAnnotationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiAnnotationList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_10UiRequiredE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiRequired *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UiRequired *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10UiRequiredE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UiRequired *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TypeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThisExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ThisExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThisExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThisExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(IdentifierExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20IdentifierExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NullExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NullExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NullExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NullExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NullExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11TrueLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TrueLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11TrueLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TrueLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12FalseLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FalseLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12FalseLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FalseLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12SuperLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(SuperLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12SuperLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SuperLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StringLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(StringLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StringLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TemplateLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TemplateLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TemplateLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14NumericLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NumericLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14NumericLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(RegExpLiteral *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13RegExpLiteralE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::RegExpLiteral *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArrayPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ArrayPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArrayPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayPattern *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13ObjectPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ObjectPattern *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13ObjectPatternE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ObjectPattern *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18PatternElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18PatternElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElementList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternPropertyList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19PatternPropertyListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternPropertyList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14PatternElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternElement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14PatternElementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternElement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15PatternPropertyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PatternProperty *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15PatternPropertyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PatternProperty *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Elision *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ElisionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Elision *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Elision *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ElisionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Elision *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16NestedExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NestedExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16NestedExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NestedExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(IdentifierPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22IdentifierPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IdentifierPropertyName *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(StringLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_25StringLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StringLiteralPropertyName *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NumericLiteralPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_26NumericLiteralPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NumericLiteralPropertyName *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ComputedPropertyName *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20ComputedPropertyNameE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ComputedPropertyName *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ArrayMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ArrayMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArrayMemberExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FieldMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21FieldMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FieldMemberExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TaggedTemplate *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TaggedTemplateE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TaggedTemplate *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NewMemberExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19NewMemberExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewMemberExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NewExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NewExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NewExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NewExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14CallExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CallExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CallExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14CallExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CallExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ArgumentListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ArgumentList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ArgumentListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ArgumentList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PostIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostIncrementExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PostDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23PostDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PostDecrementExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DeleteExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DeleteExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DeleteExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14VoidExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(VoidExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14VoidExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VoidExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TypeOfExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16TypeOfExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeOfExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PreIncrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreIncrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreIncrementExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(PreDecrementExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_22PreDecrementExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::PreDecrementExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UnaryPlusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19UnaryPlusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryPlusExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(UnaryMinusExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_20UnaryMinusExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::UnaryMinusExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15TildeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TildeExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15TildeExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TildeExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13NotExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NotExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NotExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13NotExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NotExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(BinaryExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16BinaryExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BinaryExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ConditionalExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_21ConditionalExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ConditionalExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15CommaExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CommaExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15CommaExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CommaExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Block *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_5BlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Block *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Block *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5BlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Block *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(StatementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13StatementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StatementList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(StatementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13StatementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::StatementList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17VariableStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(VariableStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17VariableStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(VariableDeclarationList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_23VariableDeclarationListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::VariableDeclarationList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14EmptyStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(EmptyStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14EmptyStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::EmptyStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExpressionStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19ExpressionStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExpressionStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11IfStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IfStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(IfStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11IfStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::IfStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DoWhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16DoWhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DoWhileStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14WhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(WhileStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14WhileStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WhileStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ForStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ForStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ForStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ForEachStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ForEachStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ForEachStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ForEachStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ContinueStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ContinueStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ContinueStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ContinueStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14BreakStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(BreakStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14BreakStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::BreakStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ReturnStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ReturnStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ReturnStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ReturnStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15YieldExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(YieldExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15YieldExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::YieldExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13WithStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WithStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(WithStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13WithStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::WithStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15SwitchStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(SwitchStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15SwitchStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::SwitchStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_9CaseBlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CaseBlock *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_9CaseBlockE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseBlock *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11CaseClausesE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CaseClauses *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11CaseClausesE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClauses *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_10CaseClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClause *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(CaseClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10CaseClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::CaseClause *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_13DefaultClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DefaultClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_13DefaultClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DefaultClause *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17LabelledStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(LabelledStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17LabelledStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::LabelledStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14ThrowStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ThrowStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14ThrowStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ThrowStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12TryStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TryStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TryStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12TryStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TryStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Catch *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_5CatchE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Catch *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Catch *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_5CatchE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Catch *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Finally *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_7FinallyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Finally *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Finally *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7FinallyE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Finally *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FunctionDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FunctionDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionDeclaration *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FunctionExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_18FunctionExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FunctionExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_19FormalParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FormalParameterList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_19FormalParameterListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FormalParameterList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ClassExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ClassExpression *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ClassExpressionE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassExpression *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ClassDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassDeclaration *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_16ClassElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ClassElementList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_16ClassElementListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ClassElementList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Program *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_7ProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Program *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Program *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_7ProgramE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Program *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NameSpaceImport *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15NameSpaceImportE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NameSpaceImport *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ImportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportSpecifier *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ImportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportsList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ImportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportsList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12NamedImportsE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NamedImports *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(NamedImports *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12NamedImportsE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::NamedImports *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(FromClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_10FromClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FromClause *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(FromClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_10FromClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::FromClause *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ImportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportClause *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ImportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportClause *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ImportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ImportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ImportDeclaration *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportSpecifier *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_15ExportSpecifierE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportSpecifier *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_11ExportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportsList *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportsList *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_11ExportsListE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportsList *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_12ExportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportClause *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportClause *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_12ExportClauseE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportClause *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ExportDeclaration *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17ExportDeclarationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ExportDeclaration *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(ESModule *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_8ESModuleE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ESModule *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(ESModule *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_8ESModuleE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::ESModule *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(DebuggerStatement *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_17DebuggerStatementE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::DebuggerStatement *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(Type *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_4TypeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Type *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(Type *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_4TypeE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::Type *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}

//  bool QQmlJS::AST::Visitor::visit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST7Visitor5visitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  return self->QQmlJS::AST::Visitor::visit(a0);
}

//  void QQmlJS::AST::Visitor::endVisit(TypeAnnotation *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST7Visitor8endVisitEPNS0_14TypeAnnotationE(
    QQmlJS::AST::Visitor *self,
    QQmlJS::AST::TypeAnnotation *a0) {
  self->QQmlJS::AST::Visitor::endVisit(a0);
}
