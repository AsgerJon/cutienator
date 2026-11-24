//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::ExpressionNode that Python can take functions over in. Every QQmlJS::AST::ExpressionNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQmlJS_AST_ExpressionNodeCall0)(const void *, int *);
class CuteQQmlJS_AST_ExpressionNode : public QQmlJS::AST::ExpressionNode {
public:
  using QQmlJS::AST::ExpressionNode::ExpressionNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST14ExpressionNode14expressionCastEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  ExpressionNode *QQmlJS::AST::ExpressionNode::expressionCast()
  QQmlJS::AST::ExpressionNode *expressionCast() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_ExpressionNodeCall0 call = reinterpret_cast<CuteQQmlJS_AST_ExpressionNodeCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::ExpressionNode *>(given);
    }
    return QQmlJS::AST::ExpressionNode::expressionCast();
  }
};

//  a Python function taken by a CuteQQmlJS_AST_ExpressionNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_ExpressionNode(
    QQmlJS::AST::ExpressionNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_ExpressionNode *>(self)->take(key, call);
}

//  ExpressionNode *QQmlJS::AST::ExpressionNode::expressionCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::ExpressionNode *ritual_own_ZN6QQmlJS3AST14ExpressionNode14expressionCastEv(
    QQmlJS::AST::ExpressionNode *self) {
  return self->QQmlJS::AST::ExpressionNode::expressionCast();
}
