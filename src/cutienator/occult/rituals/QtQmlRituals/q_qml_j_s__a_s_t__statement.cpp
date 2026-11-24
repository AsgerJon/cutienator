//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJS::AST::Statement that Python can take functions over in. Every QQmlJS::AST::Statement
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQmlJS_AST_StatementCall0)(const void *, int *);
class CuteQQmlJS_AST_Statement : public QQmlJS::AST::Statement {
public:
  using QQmlJS::AST::Statement::Statement;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlJS3AST9Statement13statementCastEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Statement *QQmlJS::AST::Statement::statementCast()
  QQmlJS::AST::Statement *statementCast() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJS_AST_StatementCall0 call = reinterpret_cast<CuteQQmlJS_AST_StatementCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQmlJS::AST::Statement *>(given);
    }
    return QQmlJS::AST::Statement::statementCast();
  }
};

//  a Python function taken by a CuteQQmlJS_AST_Statement, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJS_AST_Statement(
    QQmlJS::AST::Statement *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJS_AST_Statement *>(self)->take(key, call);
}

//  Statement *QQmlJS::AST::Statement::statementCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Statement *ritual_own_ZN6QQmlJS3AST9Statement13statementCastEv(
    QQmlJS::AST::Statement *self) {
  return self->QQmlJS::AST::Statement::statementCast();
}
