//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::ConditionalExpression that Python can take functions over in. Every QQmlJS::AST::ConditionalExpression
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_ConditionalExpressionCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_ConditionalExpressionCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_ConditionalExpressionCall2)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall3)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall4)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ConditionalExpressionCall10)(const void *, int *);
class CuteQQmlJS_AST_ConditionalExpression : public QQmlJS::AST::ConditionalExpression {
public:
  using QQmlJS::AST::ConditionalExpression::ConditionalExpression;
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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node14expressionCastEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20binaryExpressionCastEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node13statementCastEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node18uiObjectMemberCastEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node26leftHandSideExpressionCastEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node11patternCastEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20asFunctionDefinitionEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node17asClassDefinitionEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJS::AST::ConditionalExpression::accept0(BaseVisitor
  //      *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall0 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::ConditionalExpression::accept0(visitor);
  }

  //  SourceLocation
  //      QQmlJS::AST::ConditionalExpression::firstSourceLocation() const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall1 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::ConditionalExpression::firstSourceLocation();
  }

  //  SourceLocation
  //      QQmlJS::AST::ConditionalExpression::lastSourceLocation() const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall2 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::ConditionalExpression::lastSourceLocation();
  }

  //  ExpressionNode *QQmlJS::AST::ExpressionNode::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall3 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::ExpressionNode::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall4 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall5 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall6 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::UiObjectMember *>(given);
    }
    return QQmlJS::AST::Node::uiObjectMemberCast();
  }

  //  LeftHandSideExpression
  //      *QQmlJS::AST::Node::leftHandSideExpressionCast()
  QQmlJS::AST::LeftHandSideExpression *leftHandSideExpressionCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall7 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::Node::leftHandSideExpressionCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall8 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }

  //  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall9 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::Node::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_ConditionalExpressionCall10 call = reinterpret_cast<CuteQQmlJS_AST_ConditionalExpressionCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  QQmlJS::AST::ConditionalExpression::ConditionalExpression(ExpressionNode
//      *e, ExpressionNode *t, ExpressionNode *f)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ConditionalExpression *ritual_ZN6QQmlJS3AST21ConditionalExpressionC1EPNS0_14ExpressionNodeES3_S3_(
    QQmlJS::MemoryPool *pool,
    QQmlJS::AST::ExpressionNode *e,
    QQmlJS::AST::ExpressionNode *t,
    QQmlJS::AST::ExpressionNode *f) {
  return new (pool) CuteQQmlJS_AST_ConditionalExpression(e, t, f);
}

//  void QQmlJS::AST::ConditionalExpression::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST21ConditionalExpression7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::ConditionalExpression *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  SourceLocation QQmlJS::AST::ConditionalExpression::firstSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST21ConditionalExpression19firstSourceLocationEv(
    const QQmlJS::AST::ConditionalExpression *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::ConditionalExpression::lastSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST21ConditionalExpression18lastSourceLocationEv(
    const QQmlJS::AST::ConditionalExpression *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  a Python function taken by a CuteQQmlJS_AST_ConditionalExpression, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_ConditionalExpression(
    QQmlJS::AST::ConditionalExpression *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_ConditionalExpression *>(self)->take(key, call);
}

//  void QQmlJS::AST::ConditionalExpression::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST21ConditionalExpression7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::ConditionalExpression *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::ConditionalExpression::accept0(visitor);
}

//  SourceLocation QQmlJS::AST::ConditionalExpression::firstSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST21ConditionalExpression19firstSourceLocationEv(
    const QQmlJS::AST::ConditionalExpression *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::ConditionalExpression::firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::ConditionalExpression::lastSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST21ConditionalExpression18lastSourceLocationEv(
    const QQmlJS::AST::ConditionalExpression *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::ConditionalExpression::lastSourceLocation());
}
