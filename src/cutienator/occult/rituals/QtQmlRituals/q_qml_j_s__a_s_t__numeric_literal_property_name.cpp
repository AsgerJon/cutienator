//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::NumericLiteralPropertyName that Python can take functions over in. Every QQmlJS::AST::NumericLiteralPropertyName
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef QString * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall2)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall3)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall4)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall10)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NumericLiteralPropertyNameCall11)(const void *, int *);
class CuteQQmlJS_AST_NumericLiteralPropertyName : public QQmlJS::AST::NumericLiteralPropertyName {
public:
  using QQmlJS::AST::NumericLiteralPropertyName::NumericLiteralPropertyName;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node7accept0EPNS0_11BaseVisitorE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST12PropertyName8asStringEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST4Node19firstSourceLocationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QQmlJS3AST4Node18lastSourceLocationEv")) {
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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20asFunctionDefinitionEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node17asClassDefinitionEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJS::AST::NumericLiteralPropertyName::accept0(BaseVisitor
  //      *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall0 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::NumericLiteralPropertyName::accept0(visitor);
  }

  //  QString QQmlJS::AST::NumericLiteralPropertyName::asString() const
  QString asString() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall1 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQmlJS::AST::NumericLiteralPropertyName::asString();
  }

  //  SourceLocation QQmlJS::AST::PropertyName::firstSourceLocation() const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall2 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::PropertyName::firstSourceLocation();
  }

  //  SourceLocation QQmlJS::AST::PropertyName::lastSourceLocation() const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall3 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall3>(taken[3]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::PropertyName::lastSourceLocation();
  }

  //  ExpressionNode *QQmlJS::AST::Node::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall4 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::Node::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall5 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall6 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall7 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall7>(taken[7]);
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
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall8 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::Node::leftHandSideExpressionCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall9 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }

  //  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall10 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::Node::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_NumericLiteralPropertyNameCall11 call = reinterpret_cast<CuteQQmlJS_AST_NumericLiteralPropertyNameCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  QQmlJS::AST::NumericLiteralPropertyName::NumericLiteralPropertyName(doubl
//      e n)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::NumericLiteralPropertyName *ritual_ZN6QQmlJS3AST26NumericLiteralPropertyNameC1Ed(
    QQmlJS::MemoryPool *pool,
    double n) {
  return new (pool) CuteQQmlJS_AST_NumericLiteralPropertyName(n);
}

//  void QQmlJS::AST::NumericLiteralPropertyName::accept0(BaseVisitor
//      *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST26NumericLiteralPropertyName7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::NumericLiteralPropertyName *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  QString QQmlJS::AST::NumericLiteralPropertyName::asString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlJS3AST26NumericLiteralPropertyName8asStringEv(
    const QQmlJS::AST::NumericLiteralPropertyName *self) {
  return new QString(self->asString());
}

//  a Python function taken by a CuteQQmlJS_AST_NumericLiteralPropertyName,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_NumericLiteralPropertyName(
    QQmlJS::AST::NumericLiteralPropertyName *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_NumericLiteralPropertyName *>(self)->take(key, call);
}

//  void QQmlJS::AST::NumericLiteralPropertyName::accept0(BaseVisitor
//      *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST26NumericLiteralPropertyName7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::NumericLiteralPropertyName *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::NumericLiteralPropertyName::accept0(visitor);
}

//  QString QQmlJS::AST::NumericLiteralPropertyName::asString() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK6QQmlJS3AST26NumericLiteralPropertyName8asStringEv(
    const QQmlJS::AST::NumericLiteralPropertyName *self) {
  return new QString(
      self->QQmlJS::AST::NumericLiteralPropertyName::asString());
}
