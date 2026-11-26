//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::FunctionDeclaration that Python can take functions over in. Every QQmlJS::AST::FunctionDeclaration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_FunctionDeclarationCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_FunctionDeclarationCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_FunctionDeclarationCall2)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall3)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall4)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_FunctionDeclarationCall10)(const void *, int *);
class CuteQQmlJS_AST_FunctionDeclaration : public QQmlJS::AST::FunctionDeclaration {
public:
  using QQmlJS::AST::FunctionDeclaration::FunctionDeclaration;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node7accept0EPNS0_11BaseVisitorE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST4Node19firstSourceLocationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST4Node18lastSourceLocationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20asFunctionDefinitionEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node14expressionCastEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20binaryExpressionCastEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node13statementCastEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node18uiObjectMemberCastEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node26leftHandSideExpressionCastEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node11patternCastEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node17asClassDefinitionEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJS::AST::FunctionDeclaration::accept0(BaseVisitor *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall0 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::FunctionDeclaration::accept0(visitor);
  }

  //  SourceLocation QQmlJS::AST::FunctionExpression::firstSourceLocation()
  //      const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall1 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::FunctionExpression::firstSourceLocation();
  }

  //  SourceLocation QQmlJS::AST::FunctionExpression::lastSourceLocation()
  //      const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall2 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::FunctionExpression::lastSourceLocation();
  }

  //  FunctionExpression
  //      *QQmlJS::AST::FunctionExpression::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall3 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::FunctionExpression::asFunctionDefinition();
  }

  //  ExpressionNode *QQmlJS::AST::ExpressionNode::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall4 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::ExpressionNode::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall5 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall6 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall7 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::UiObjectMember *>(given);
    }
    return QQmlJS::AST::Node::uiObjectMemberCast();
  }

  //  LeftHandSideExpression
  //      *QQmlJS::AST::Node::leftHandSideExpressionCast()
  QQmlJS::AST::LeftHandSideExpression *leftHandSideExpressionCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall8 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::Node::leftHandSideExpressionCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall9 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_FunctionDeclarationCall10 call = reinterpret_cast<CuteQQmlJS_AST_FunctionDeclarationCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  QQmlJS::AST::FunctionDeclaration::FunctionDeclaration(QStringView n,
//      FormalParameterList *f, StatementList *b, TypeAnnotation
//      *typeAnnotation)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::FunctionDeclaration *ritual_ZN6QQmlJS3AST19FunctionDeclarationC1E11QStringViewPNS0_19FormalParameterListEPNS0_13StatementListEPNS0_14TypeAnnotationE(
    QQmlJS::MemoryPool *pool,
    const QString *n,
    QQmlJS::AST::FormalParameterList *f,
    QQmlJS::AST::StatementList *b,
    QQmlJS::AST::TypeAnnotation *typeAnnotation) {
  return new (pool) CuteQQmlJS_AST_FunctionDeclaration(
      QStringView(*n),
      f,
      b,
      typeAnnotation);
}

//  void QQmlJS::AST::FunctionDeclaration::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST19FunctionDeclaration7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::FunctionDeclaration *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  a Python function taken by a CuteQQmlJS_AST_FunctionDeclaration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_FunctionDeclaration(
    QQmlJS::AST::FunctionDeclaration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_FunctionDeclaration *>(self)->take(key, call);
}

//  void QQmlJS::AST::FunctionDeclaration::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST19FunctionDeclaration7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::FunctionDeclaration *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::FunctionDeclaration::accept0(visitor);
}
