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

//  A QQmlJS::AST::PatternProperty that Python can take functions over in. Every QQmlJS::AST::PatternProperty
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_PatternPropertyCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_PatternPropertyCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_PatternPropertyCall2)(const void *, int *);
typedef void (*CuteQQmlJS_AST_PatternPropertyCall3)(const void *, QQmlJS::AST::BoundNames *, int *);
typedef bool (*CuteQQmlJS_AST_PatternPropertyCall4)(const void *, QQmlJS::SourceLocation *, QString *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall10)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall11)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternPropertyCall12)(const void *, int *);
class CuteQQmlJS_AST_PatternProperty : public QQmlJS::AST::PatternProperty {
public:
  using QQmlJS::AST::PatternProperty::PatternProperty;
  void *taken[13] = {};

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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10BoundNamesE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node14expressionCastEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20binaryExpressionCastEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node13statementCastEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node18uiObjectMemberCastEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node26leftHandSideExpressionCastEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node11patternCastEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node20asFunctionDefinitionEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node17asClassDefinitionEv")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJS::AST::PatternProperty::accept0(BaseVisitor *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall0 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::PatternProperty::accept0(visitor);
  }

  //  SourceLocation QQmlJS::AST::PatternProperty::firstSourceLocation()
  //      const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall1 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::PatternProperty::firstSourceLocation();
  }

  //  SourceLocation QQmlJS::AST::PatternProperty::lastSourceLocation()
  //      const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall2 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::PatternProperty::lastSourceLocation();
  }

  //  void QQmlJS::AST::PatternProperty::boundNames(BoundNames *names)
  void boundNames(QQmlJS::AST::BoundNames *names) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall3 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall3>(taken[3]);
      call(this, names, &handled);
      if (handled) return;
    }
    QQmlJS::AST::PatternProperty::boundNames(names);
  }

  //  bool QQmlJS::AST::PatternProperty::convertLiteralToAssignmentPattern(
  //      SourceLocation *errorLocation, QString *errorMessage)
  bool convertLiteralToAssignmentPattern(
      QQmlJS::SourceLocation *errorLocation,
      QString *errorMessage) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall4 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall4>(taken[4]);
      bool given = call(this, errorLocation, errorMessage, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::PatternProperty::convertLiteralToAssignmentPattern(errorLocation, errorMessage);
  }

  //  ExpressionNode *QQmlJS::AST::Node::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall5 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::Node::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall6 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall7 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall8 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::UiObjectMember *>(given);
    }
    return QQmlJS::AST::Node::uiObjectMemberCast();
  }

  //  LeftHandSideExpression
  //      *QQmlJS::AST::Node::leftHandSideExpressionCast()
  QQmlJS::AST::LeftHandSideExpression *leftHandSideExpressionCast() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall9 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::Node::leftHandSideExpressionCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall10 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }

  //  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall11 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::Node::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternPropertyCall12 call = reinterpret_cast<CuteQQmlJS_AST_PatternPropertyCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  SourceLocation QQmlJS::AST::PatternProperty::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST15PatternProperty19firstSourceLocationEv(
    const QQmlJS::AST::PatternProperty *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::PatternProperty::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST15PatternProperty18lastSourceLocationEv(
    const QQmlJS::AST::PatternProperty *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  a Python function taken by a CuteQQmlJS_AST_PatternProperty, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_PatternProperty(
    QQmlJS::AST::PatternProperty *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_PatternProperty *>(self)->take(key, call);
}

//  void QQmlJS::AST::PatternProperty::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST15PatternProperty7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::PatternProperty *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::PatternProperty::accept0(visitor);
}

//  SourceLocation QQmlJS::AST::PatternProperty::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST15PatternProperty19firstSourceLocationEv(
    const QQmlJS::AST::PatternProperty *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::PatternProperty::firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::PatternProperty::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST15PatternProperty18lastSourceLocationEv(
    const QQmlJS::AST::PatternProperty *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::PatternProperty::lastSourceLocation());
}

//  void QQmlJS::AST::PatternProperty::boundNames(BoundNames *names)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST15PatternProperty10boundNamesEPNS0_10BoundNamesE(
    QQmlJS::AST::PatternProperty *self,
    QQmlJS::AST::BoundNames *names) {
  self->QQmlJS::AST::PatternProperty::boundNames(names);
}

//  bool QQmlJS::AST::PatternProperty::convertLiteralToAssignmentPattern(Sour
//      ceLocation *errorLocation, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST15PatternProperty33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString(
    QQmlJS::AST::PatternProperty *self,
    QQmlJS::SourceLocation *errorLocation,
    QString *errorMessage) {
  return self->QQmlJS::AST::PatternProperty::convertLiteralToAssignmentPattern(
      errorLocation,
      errorMessage);
}
