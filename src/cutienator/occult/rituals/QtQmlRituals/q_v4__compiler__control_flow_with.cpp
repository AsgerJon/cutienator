//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontrolflow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontrolflow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QV4::Compiler::ControlFlowWith that Python can take functions over in. Every QV4::Compiler::ControlFlowWith
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQV4_Compiler_ControlFlowWithCall0)(const void *, int *);
typedef QString * (*CuteQV4_Compiler_ControlFlowWithCall1)(const void *, int *);
class CuteQV4_Compiler_ControlFlowWith : public QV4::Compiler::ControlFlowWith {
public:
  using QV4::Compiler::ControlFlowWith::ControlFlowWith;
  CuteQV4_Compiler_ControlFlowWith(const QV4::Compiler::ControlFlowWith &other) : QV4::Compiler::ControlFlowWith(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV48Compiler11ControlFlow14requiresUnwindEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK3QV48Compiler11ControlFlow5labelEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QV4::Compiler::ControlFlowWith::requiresUnwind()
  bool requiresUnwind() override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowWithCall0 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowWithCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QV4::Compiler::ControlFlowWith::requiresUnwind();
  }

  //  QString QV4::Compiler::ControlFlow::label() const
  QString label() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowWithCall1 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowWithCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QV4::Compiler::ControlFlow::label();
  }
};

//  QV4::Compiler::ControlFlowWith::~ControlFlowWith()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler15ControlFlowWithD1Ev(
    QV4::Compiler::ControlFlowWith *self) {
  delete self;
}

//  bool QV4::Compiler::ControlFlowWith::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler15ControlFlowWith14requiresUnwindEv(
    QV4::Compiler::ControlFlowWith *self) {
  return self->requiresUnwind();
}

//  a Python function taken by a CuteQV4_Compiler_ControlFlowWith, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_ControlFlowWith(
    QV4::Compiler::ControlFlowWith *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_ControlFlowWith *>(self)->take(key, call);
}

//  bool QV4::Compiler::ControlFlowWith::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler15ControlFlowWith14requiresUnwindEv(
    QV4::Compiler::ControlFlowWith *self) {
  return self->QV4::Compiler::ControlFlowWith::requiresUnwind();
}
