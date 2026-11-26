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

//  A QQmlJS::AST::PatternElement that Python can take functions over in. Every QQmlJS::AST::PatternElement
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_PatternElementCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef bool (*CuteQQmlJS_AST_PatternElementCall1)(const void *, QQmlJS::SourceLocation *, QString *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_PatternElementCall2)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_PatternElementCall3)(const void *, int *);
typedef void (*CuteQQmlJS_AST_PatternElementCall4)(const void *, QQmlJS::AST::BoundNames *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall10)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall11)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_PatternElementCall12)(const void *, int *);
class CuteQQmlJS_AST_PatternElement : public QQmlJS::AST::PatternElement {
public:
  using QQmlJS::AST::PatternElement::PatternElement;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST4Node7accept0EPNS0_11BaseVisitorE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString")) {
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
    if (!std::strcmp(key, "_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10BoundNamesE")) {
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

  //  void QQmlJS::AST::PatternElement::accept0(BaseVisitor *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall0 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QQmlJS::AST::PatternElement::accept0(visitor);
  }

  //  bool QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(S
  //      ourceLocation *errorLocation, QString *errorMessage)
  bool convertLiteralToAssignmentPattern(
      QQmlJS::SourceLocation *errorLocation,
      QString *errorMessage) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall1 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall1>(taken[1]);
      bool given = call(this, errorLocation, errorMessage, &handled);
      if (handled) return given;
    }
    return QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(errorLocation, errorMessage);
  }

  //  SourceLocation QQmlJS::AST::PatternElement::firstSourceLocation()
  //      const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall2 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::PatternElement::firstSourceLocation();
  }

  //  SourceLocation QQmlJS::AST::PatternElement::lastSourceLocation()
  //      const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall3 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall3>(taken[3]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::AST::PatternElement::lastSourceLocation();
  }

  //  void QQmlJS::AST::PatternElement::boundNames(BoundNames *names)
  void boundNames(QQmlJS::AST::BoundNames *names) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall4 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall4>(taken[4]);
      call(this, names, &handled);
      if (handled) return;
    }
    QQmlJS::AST::PatternElement::boundNames(names);
  }

  //  ExpressionNode *QQmlJS::AST::Node::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall5 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::Node::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall6 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall7 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall8 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall8>(taken[8]);
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
      CuteQQmlJS_AST_PatternElementCall9 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::Node::leftHandSideExpressionCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall10 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }

  //  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall11 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::Node::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJS_AST_PatternElementCall12 call = reinterpret_cast<CuteQQmlJS_AST_PatternElementCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  void QQmlJS::AST::PatternElement::unwrapInitializer()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST14PatternElement17unwrapInitializerEv(
    QQmlJS::AST::PatternElement *self) {
  self->unwrapInitializer();
}

//  QQmlJS::AST::PatternElement::PatternElement(ExpressionNode *i, Type t)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::PatternElement *ritual_ZN6QQmlJS3AST14PatternElementC1EPNS0_14ExpressionNodeENS1_4TypeE(
    QQmlJS::MemoryPool *pool,
    QQmlJS::AST::ExpressionNode *i,
    QQmlJS::AST::PatternElement::Type t) {
  return new (pool) CuteQQmlJS_AST_PatternElement(i, t);
}

//  QQmlJS::AST::PatternElement::PatternElement(QStringView n, TypeAnnotation
//      *typeAnnotation, ExpressionNode *i, Type t)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::PatternElement *ritual_ZN6QQmlJS3AST14PatternElementC1E11QStringViewPNS0_14TypeAnnotationEPNS0_14ExpressionNodeENS1_4TypeE(
    QQmlJS::MemoryPool *pool,
    const QString *n,
    QQmlJS::AST::TypeAnnotation *typeAnnotation,
    QQmlJS::AST::ExpressionNode *i,
    QQmlJS::AST::PatternElement::Type t) {
  return new (pool) CuteQQmlJS_AST_PatternElement(
      QStringView(*n),
      typeAnnotation,
      i,
      t);
}

//  QQmlJS::AST::PatternElement::PatternElement(Pattern *pattern,
//      ExpressionNode *i, Type t)
extern "C" Q_DECL_EXPORT
QQmlJS::AST::PatternElement *ritual_ZN6QQmlJS3AST14PatternElementC1EPNS0_7PatternEPNS0_14ExpressionNodeENS1_4TypeE(
    QQmlJS::MemoryPool *pool,
    QQmlJS::AST::Pattern *pattern,
    QQmlJS::AST::ExpressionNode *i,
    QQmlJS::AST::PatternElement::Type t) {
  return new (pool) CuteQQmlJS_AST_PatternElement(pattern, i, t);
}

//  void QQmlJS::AST::PatternElement::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST14PatternElement7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::PatternElement *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  bool QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(Sourc
//      eLocation *errorLocation, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString(
    QQmlJS::AST::PatternElement *self,
    QQmlJS::SourceLocation *errorLocation,
    QString *errorMessage) {
  return self->convertLiteralToAssignmentPattern(
      errorLocation,
      errorMessage);
}

//  SourceLocation QQmlJS::AST::PatternElement::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14PatternElement19firstSourceLocationEv(
    const QQmlJS::AST::PatternElement *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::PatternElement::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST14PatternElement18lastSourceLocationEv(
    const QQmlJS::AST::PatternElement *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  ExpressionNode *QQmlJS::AST::PatternElement::destructuringTarget() const
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ExpressionNode *ritual_ZNK6QQmlJS3AST14PatternElement19destructuringTargetEv(
    const QQmlJS::AST::PatternElement *self) {
  return self->destructuringTarget();
}

//  Pattern *QQmlJS::AST::PatternElement::destructuringPattern() const
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Pattern *ritual_ZNK6QQmlJS3AST14PatternElement20destructuringPatternEv(
    const QQmlJS::AST::PatternElement *self) {
  return self->destructuringPattern();
}

//  PatternElementList *QQmlJS::AST::PatternElement::elementList() const
extern "C" Q_DECL_EXPORT
QQmlJS::AST::PatternElementList *ritual_ZNK6QQmlJS3AST14PatternElement11elementListEv(
    const QQmlJS::AST::PatternElement *self) {
  return self->elementList();
}

//  PatternPropertyList *QQmlJS::AST::PatternElement::propertyList() const
extern "C" Q_DECL_EXPORT
QQmlJS::AST::PatternPropertyList *ritual_ZNK6QQmlJS3AST14PatternElement12propertyListEv(
    const QQmlJS::AST::PatternElement *self) {
  return self->propertyList();
}

//  bool QQmlJS::AST::PatternElement::isVariableDeclaration() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14PatternElement21isVariableDeclarationEv(
    const QQmlJS::AST::PatternElement *self) {
  return self->isVariableDeclaration();
}

//  bool QQmlJS::AST::PatternElement::isLexicallyScoped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST14PatternElement17isLexicallyScopedEv(
    const QQmlJS::AST::PatternElement *self) {
  return self->isLexicallyScoped();
}

//  void QQmlJS::AST::PatternElement::boundNames(BoundNames *names)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10BoundNamesE(
    QQmlJS::AST::PatternElement *self,
    QQmlJS::AST::BoundNames *names) {
  self->boundNames(names);
}

//  a Python function taken by a CuteQQmlJS_AST_PatternElement, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_PatternElement(
    QQmlJS::AST::PatternElement *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_PatternElement *>(self)->take(key, call);
}

//  void QQmlJS::AST::PatternElement::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST14PatternElement7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::PatternElement *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->QQmlJS::AST::PatternElement::accept0(visitor);
}

//  bool QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(Sourc
//      eLocation *errorLocation, QString *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssignmentPatternEPNS_14SourceLocationEP7QString(
    QQmlJS::AST::PatternElement *self,
    QQmlJS::SourceLocation *errorLocation,
    QString *errorMessage) {
  return self->QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(
      errorLocation,
      errorMessage);
}

//  SourceLocation QQmlJS::AST::PatternElement::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST14PatternElement19firstSourceLocationEv(
    const QQmlJS::AST::PatternElement *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::PatternElement::firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::PatternElement::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_own_ZNK6QQmlJS3AST14PatternElement18lastSourceLocationEv(
    const QQmlJS::AST::PatternElement *self) {
  return new QQmlJS::SourceLocation(
      self->QQmlJS::AST::PatternElement::lastSourceLocation());
}

//  void QQmlJS::AST::PatternElement::boundNames(BoundNames *names)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10BoundNamesE(
    QQmlJS::AST::PatternElement *self,
    QQmlJS::AST::BoundNames *names) {
  self->QQmlJS::AST::PatternElement::boundNames(names);
}
