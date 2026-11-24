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

//  A QQmlJS::AST::ArrayPattern that Python can take functions over in. Every QQmlJS::AST::ArrayPattern
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_ArrayPatternCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_ArrayPatternCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_ArrayPatternCall2)(const void *, int *);
typedef bool (*CuteQQmlJS_AST_ArrayPatternCall3)(const void *, QQmlJS::SourceLocation *, QString *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall4)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall10)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_ArrayPatternCall11)(const void *, int *);
class CuteQQmlJS_AST_ArrayPattern : public QQmlJS::AST::ArrayPattern {
public:
  using QQmlJS::AST::ArrayPattern::ArrayPattern;
  void *taken[12] = {};

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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST7Pattern33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node11patternCastEv")) {
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

  //  void QQmlJS::AST::ArrayPattern::accept0(BaseVisitor *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall0 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::ArrayPattern::accept0(visitor);
  }

  //  SourceLocation QQmlJS::AST::ArrayPattern::firstSourceLocation() const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall1 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::ArrayPattern::firstSourceLocation();
  }

  //  SourceLocation QQmlJS::AST::ArrayPattern::lastSourceLocation() const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall2 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::ArrayPattern::lastSourceLocation();
  }

  //  bool QQmlJS::AST::ArrayPattern::convertLiteralToAssignmentPattern(Sou
  //      rceLocation *errorLocation, QString *errorMessage)
  bool convertLiteralToAssignmentPattern(
      QQmlJS::SourceLocation *errorLocation,
      QString *errorMessage) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall3 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall3>(taken[3]);
      bool given = call(this, errorLocation, errorMessage, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::ArrayPattern::convertLiteralToAssignmentPattern(errorLocation, errorMessage);
  }

  //  Pattern *QQmlJS::AST::Pattern::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall4 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Pattern::patternCast();
  }

  //  LeftHandSideExpression
  //      *QQmlJS::AST::LeftHandSideExpression::leftHandSideExpressionCast(
  //      )
  QQmlJS::AST::LeftHandSideExpression *leftHandSideExpressionCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall5 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::LeftHandSideExpression::leftHandSideExpressionCast();
  }

  //  ExpressionNode *QQmlJS::AST::ExpressionNode::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall6 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::ExpressionNode::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall7 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall8 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall9 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::UiObjectMember *>(given);
    }
    return QQmlJS::AST::Node::uiObjectMemberCast();
  }

  //  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall10 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::Node::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_ArrayPatternCall11 call = reinterpret_cast<CuteQQmlJS_AST_ArrayPatternCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  SourceLocation QQmlJS::AST::ArrayPattern::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST12ArrayPattern19firstSourceLocationEv(
    const QQmlJS::AST::ArrayPattern *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::ArrayPattern::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST12ArrayPattern18lastSourceLocationEv(
    const QQmlJS::AST::ArrayPattern *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  a Python function taken by a CuteQQmlJS_AST_ArrayPattern, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_ArrayPattern(
    QQmlJS::AST::ArrayPattern *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_ArrayPattern *>(self)->take(key, call);
}

//  void QQmlJS::AST::ArrayPattern::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST12ArrayPattern7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::ArrayPattern *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::ArrayPattern::accept0(visitor);
}

//  SourceLocation QQmlJS::AST::ArrayPattern::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST12ArrayPattern19firstSourceLocationEv(
    const QQmlJS::AST::ArrayPattern *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::ArrayPattern::firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::ArrayPattern::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST12ArrayPattern18lastSourceLocationEv(
    const QQmlJS::AST::ArrayPattern *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::ArrayPattern::lastSourceLocation());
}

//  bool QQmlJS::AST::ArrayPattern::convertLiteralToAssignmentPattern(SourceL
//      ocation *errorLocation, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST12ArrayPattern33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString(
    QQmlJS::AST::ArrayPattern *self,
    QQmlJS::SourceLocation *errorLocation,
    QString *errorMessage) {
  return self->QQmlJS::AST::ArrayPattern::convertLiteralToAssignmentPattern(
      errorLocation,
      errorMessage);
}
