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

//  A QQmlJS::AST::NestedExpression that Python can take functions over in. Every QQmlJS::AST::NestedExpression
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_NestedExpressionCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_NestedExpressionCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_NestedExpressionCall2)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall3)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall4)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NestedExpressionCall10)(const void *, int *);
class CuteQQmlJS_AST_NestedExpression : public QQmlJS::AST::NestedExpression {
public:
  using QQmlJS::AST::NestedExpression::NestedExpression;
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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node17asClassDefinitionEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node26leftHandSideExpressionCastEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node14expressionCastEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20binaryExpressionCastEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node13statementCastEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node18uiObjectMemberCastEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node11patternCastEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJS::AST::NestedExpression::accept0(BaseVisitor *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall0 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::NestedExpression::accept0(visitor);
  }

  //  SourceLocation QQmlJS::AST::NestedExpression::firstSourceLocation()
  //      const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall1 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::NestedExpression::firstSourceLocation();
  }

  //  SourceLocation QQmlJS::AST::NestedExpression::lastSourceLocation()
  //      const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall2 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::NestedExpression::lastSourceLocation();
  }

  //  FunctionExpression
  //      *QQmlJS::AST::NestedExpression::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall3 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::NestedExpression::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::NestedExpression::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall4 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::NestedExpression::asClassDefinition();
  }

  //  LeftHandSideExpression
  //      *QQmlJS::AST::LeftHandSideExpression::leftHandSideExpressionCast(
  //      )
  QQmlJS::AST::LeftHandSideExpression *leftHandSideExpressionCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall5 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::LeftHandSideExpression::leftHandSideExpressionCast();
  }

  //  ExpressionNode *QQmlJS::AST::ExpressionNode::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall6 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::ExpressionNode::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall7 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall8 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall9 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::UiObjectMember *>(given);
    }
    return QQmlJS::AST::Node::uiObjectMemberCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_NestedExpressionCall10 call = reinterpret_cast<CuteQQmlJS_AST_NestedExpressionCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }
};

//  QQmlJS::AST::NestedExpression::NestedExpression(ExpressionNode
//      *expression)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::NestedExpression *ritual_ZN6QQmlJS3AST16NestedExpressionC1EPNS0_14ExpressionNodeE(
    QQmlJS::MemoryPool *pool,
    QQmlJS::AST::ExpressionNode *expression) {
  return new (pool) CuteQQmlJS_AST_NestedExpression(expression);
}

//  void QQmlJS::AST::NestedExpression::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST16NestedExpression7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::NestedExpression *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  SourceLocation QQmlJS::AST::NestedExpression::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST16NestedExpression19firstSourceLocationEv(
    const QQmlJS::AST::NestedExpression *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::NestedExpression::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST16NestedExpression18lastSourceLocationEv(
    const QQmlJS::AST::NestedExpression *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  FunctionExpression *QQmlJS::AST::NestedExpression::asFunctionDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::FunctionExpression *ritual_ZN6QQmlJS3AST16NestedExpression20asFunctionDefinitionEv(
    QQmlJS::AST::NestedExpression *self) {
  return self->asFunctionDefinition();
}

//  ClassExpression *QQmlJS::AST::NestedExpression::asClassDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ClassExpression *ritual_ZN6QQmlJS3AST16NestedExpression17asClassDefinitionEv(
    QQmlJS::AST::NestedExpression *self) {
  return self->asClassDefinition();
}

//  a Python function taken by a CuteQQmlJS_AST_NestedExpression, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_NestedExpression(
    QQmlJS::AST::NestedExpression *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_NestedExpression *>(self)->take(key, call);
}

//  void QQmlJS::AST::NestedExpression::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST16NestedExpression7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::NestedExpression *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::NestedExpression::accept0(visitor);
}

//  SourceLocation QQmlJS::AST::NestedExpression::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST16NestedExpression19firstSourceLocationEv(
    const QQmlJS::AST::NestedExpression *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::NestedExpression::firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::NestedExpression::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST16NestedExpression18lastSourceLocationEv(
    const QQmlJS::AST::NestedExpression *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::NestedExpression::lastSourceLocation());
}

//  FunctionExpression *QQmlJS::AST::NestedExpression::asFunctionDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::FunctionExpression *ritual_own_ZN6QQmlJS3AST16NestedExpression20asFunctionDefinitionEv(
    QQmlJS::AST::NestedExpression *self) {
  return self->QQmlJS::AST::NestedExpression::asFunctionDefinition();
}

//  ClassExpression *QQmlJS::AST::NestedExpression::asClassDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ClassExpression *ritual_own_ZN6QQmlJS3AST16NestedExpression17asClassDefinitionEv(
    QQmlJS::AST::NestedExpression *self) {
  return self->QQmlJS::AST::NestedExpression::asClassDefinition();
}
