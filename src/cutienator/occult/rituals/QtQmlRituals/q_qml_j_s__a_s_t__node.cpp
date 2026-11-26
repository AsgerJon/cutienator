//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again.
//  Not written: the constructor and the destructor, as a node is made
//  in a QQmlJS::MemoryPool (the 'operator new' of Managed takes only
//  that) and its destructor is never called; and the templates 'cast'
//  and 'lastListElement', which are not of the class.
//  A function Qt leaves pure ('accept0', 'firstSourceLocation',
//  'lastSourceLocation') has no 'own' ritual, as it has no body of
//  Qt's to run, and its Cute function gives an empty answer when
//  Python has taken nothing over for it.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#include <cstring>

//  A QQmlJS::AST::Node that Python can take functions over in. Every
//  QQmlJS::AST::Node Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJS_AST_NodeCall0)(const void *, QQmlJS::AST::BaseVisitor *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_NodeCall1)(const void *, int *);
typedef const QQmlJS::SourceLocation * (*CuteQQmlJS_AST_NodeCall2)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall3)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall4)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall5)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall6)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall7)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall8)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall9)(const void *, int *);
typedef void * (*CuteQQmlJS_AST_NodeCall10)(const void *, int *);
class CuteQQmlJS_AST_Node : public QQmlJS::AST::Node {
public:
  using QQmlJS::AST::Node::Node;
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

  //  void QQmlJS::AST::Node::accept0(BaseVisitor *visitor)
  void accept0(QQmlJS::AST::BaseVisitor *visitor) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall0 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall0>(taken[0]);
      call(this, visitor, &handled);
      if (handled) return;
    }
  }

  //  SourceLocation QQmlJS::AST::Node::firstSourceLocation() const
  QQmlJS::SourceLocation firstSourceLocation() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall1 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall1>(taken[1]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::SourceLocation();
  }

  //  SourceLocation QQmlJS::AST::Node::lastSourceLocation() const
  QQmlJS::SourceLocation lastSourceLocation() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall2 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall2>(taken[2]);
      const QQmlJS::SourceLocation * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQmlJS::SourceLocation();
  }

  //  ExpressionNode *QQmlJS::AST::Node::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall3 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::Node::expressionCast();
  }

  //  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
  QQmlJS::AST::BinaryExpression *binaryExpressionCast() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall4 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::BinaryExpression *>(given);
    }
    return QQmlJS::AST::Node::binaryExpressionCast();
  }

  //  Statement *QQmlJS::AST::Node::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall5 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Node::statementCast();
  }

  //  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
  QQmlJS::AST::UiObjectMember *uiObjectMemberCast() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall6 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall6>(taken[6]);
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
      CuteQQmlJS_AST_NodeCall7 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::LeftHandSideExpression *>(given);
    }
    return QQmlJS::AST::Node::leftHandSideExpressionCast();
  }

  //  Pattern *QQmlJS::AST::Node::patternCast()
  QQmlJS::AST::Pattern *patternCast() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall8 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Pattern *>(given);
    }
    return QQmlJS::AST::Node::patternCast();
  }

  //  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
  QQmlJS::AST::FunctionExpression *asFunctionDefinition() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall9 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::FunctionExpression *>(given);
    }
    return QQmlJS::AST::Node::asFunctionDefinition();
  }

  //  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
  QQmlJS::AST::ClassExpression *asClassDefinition() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJS_AST_NodeCall10 call = reinterpret_cast<CuteQQmlJS_AST_NodeCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ClassExpression *>(given);
    }
    return QQmlJS::AST::Node::asClassDefinition();
  }
};

//  ExpressionNode *QQmlJS::AST::Node::expressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ExpressionNode *ritual_ZN6QQmlJS3AST4Node14expressionCastEv(
    QQmlJS::AST::Node *self) {
  return self->expressionCast();
}

//  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::BinaryExpression *ritual_ZN6QQmlJS3AST4Node20binaryExpressionCastEv(
    QQmlJS::AST::Node *self) {
  return self->binaryExpressionCast();
}

//  Statement *QQmlJS::AST::Node::statementCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Statement *ritual_ZN6QQmlJS3AST4Node13statementCastEv(
    QQmlJS::AST::Node *self) {
  return self->statementCast();
}

//  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::UiObjectMember *ritual_ZN6QQmlJS3AST4Node18uiObjectMemberCastEv(
    QQmlJS::AST::Node *self) {
  return self->uiObjectMemberCast();
}

//  LeftHandSideExpression
//      *QQmlJS::AST::Node::leftHandSideExpressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::LeftHandSideExpression *ritual_ZN6QQmlJS3AST4Node26leftHandSideExpressionCastEv(
    QQmlJS::AST::Node *self) {
  return self->leftHandSideExpressionCast();
}

//  Pattern *QQmlJS::AST::Node::patternCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Pattern *ritual_ZN6QQmlJS3AST4Node11patternCastEv(
    QQmlJS::AST::Node *self) {
  return self->patternCast();
}

//  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::FunctionExpression *ritual_ZN6QQmlJS3AST4Node20asFunctionDefinitionEv(
    QQmlJS::AST::Node *self) {
  return self->asFunctionDefinition();
}

//  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ClassExpression *ritual_ZN6QQmlJS3AST4Node17asClassDefinitionEv(
    QQmlJS::AST::Node *self) {
  return self->asClassDefinition();
}

//  bool QQmlJS::AST::Node::ignoreRecursionDepth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS3AST4Node20ignoreRecursionDepthEv(
    const QQmlJS::AST::Node *self) {
  return self->ignoreRecursionDepth();
}

//  void QQmlJS::AST::Node::accept(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST4Node6acceptEPNS0_11BaseVisitorE(
    QQmlJS::AST::Node *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept(visitor);
}

//  void QQmlJS::AST::Node::accept(Node *node, BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST4Node6acceptEPS1_PNS0_11BaseVisitorE(
    QQmlJS::AST::Node *node,
    QQmlJS::AST::BaseVisitor *visitor) {
  QQmlJS::AST::Node::accept(node, visitor);
}

//  void QQmlJS::AST::Node::accept0(BaseVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS3AST4Node7accept0EPNS0_11BaseVisitorE(
    QQmlJS::AST::Node *self,
    QQmlJS::AST::BaseVisitor *visitor) {
  self->accept0(visitor);
}

//  SourceLocation QQmlJS::AST::Node::firstSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST4Node19firstSourceLocationEv(
    const QQmlJS::AST::Node *self) {
  return new QQmlJS::SourceLocation(self->firstSourceLocation());
}

//  SourceLocation QQmlJS::AST::Node::lastSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK6QQmlJS3AST4Node18lastSourceLocationEv(
    const QQmlJS::AST::Node *self) {
  return new QQmlJS::SourceLocation(self->lastSourceLocation());
}

//  a Python function taken by a CuteQQmlJS_AST_Node, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_Node(
    QQmlJS::AST::Node *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_Node *>(self)->take(key, call);
}

//  ExpressionNode *QQmlJS::AST::Node::expressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ExpressionNode *ritual_own_ZN6QQmlJS3AST4Node14expressionCastEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::expressionCast();
}

//  BinaryExpression *QQmlJS::AST::Node::binaryExpressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::BinaryExpression *ritual_own_ZN6QQmlJS3AST4Node20binaryExpressionCastEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::binaryExpressionCast();
}

//  Statement *QQmlJS::AST::Node::statementCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Statement *ritual_own_ZN6QQmlJS3AST4Node13statementCastEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::statementCast();
}

//  UiObjectMember *QQmlJS::AST::Node::uiObjectMemberCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::UiObjectMember *ritual_own_ZN6QQmlJS3AST4Node18uiObjectMemberCastEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::uiObjectMemberCast();
}

//  LeftHandSideExpression
//      *QQmlJS::AST::Node::leftHandSideExpressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::LeftHandSideExpression *ritual_own_ZN6QQmlJS3AST4Node26leftHandSideExpressionCastEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::leftHandSideExpressionCast();
}

//  Pattern *QQmlJS::AST::Node::patternCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Pattern *ritual_own_ZN6QQmlJS3AST4Node11patternCastEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::patternCast();
}

//  FunctionExpression *QQmlJS::AST::Node::asFunctionDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::FunctionExpression *ritual_own_ZN6QQmlJS3AST4Node20asFunctionDefinitionEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::asFunctionDefinition();
}

//  ClassExpression *QQmlJS::AST::Node::asClassDefinition()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ClassExpression *ritual_own_ZN6QQmlJS3AST4Node17asClassDefinitionEv(
    QQmlJS::AST::Node *self) {
  return self->QQmlJS::AST::Node::asClassDefinition();
}
