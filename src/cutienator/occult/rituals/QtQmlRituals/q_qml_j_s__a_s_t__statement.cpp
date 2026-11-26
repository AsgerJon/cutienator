//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0, from Qt's
//  source. Kept as it is when the generator runs again.
//  Not written: the constructor, as a node is made in a
//  QQmlJS::MemoryPool (the 'operator new' of Managed takes only that).
//  The class is still abstract, as 'accept0' and the two source
//  locations stay pure, so its Cute class holds only the function
//  the class itself declares.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmljsast_p.h>
#include <cstring>

//  A QQmlJS::AST::Statement that Python can take functions over in.
//  Every QQmlJS::AST::Statement Python makes is one. Each function
//  below asks the Python function handed over for it, and runs Qt's own
//  without one.
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

//  Statement *QQmlJS::AST::Statement::statementCast()
extern "C" Q_DECL_EXPORT
QQmlJS::AST::Statement *ritual_ZN6QQmlJS3AST9Statement13statementCastEv(
    QQmlJS::AST::Statement *self) {
  return self->statementCast();
}

//  a Python function taken by a CuteQQmlJS_AST_Statement, for the
//      function named by the key
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
