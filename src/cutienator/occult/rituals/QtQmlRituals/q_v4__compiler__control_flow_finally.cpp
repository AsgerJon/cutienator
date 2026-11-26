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

//  A QV4::Compiler::ControlFlowFinally that Python can take functions over in. Every QV4::Compiler::ControlFlowFinally
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQV4_Compiler_ControlFlowFinallyCall0)(const void *, int *);
typedef void * (*CuteQV4_Compiler_ControlFlowFinallyCall1)(const void *, int *);
typedef QString * (*CuteQV4_Compiler_ControlFlowFinallyCall2)(const void *, int *);
class CuteQV4_Compiler_ControlFlowFinally : public QV4::Compiler::ControlFlowFinally {
public:
  using QV4::Compiler::ControlFlowFinally::ControlFlowFinally;
  CuteQV4_Compiler_ControlFlowFinally(const QV4::Compiler::ControlFlowFinally & other) : QV4::Compiler::ControlFlowFinally(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV48Compiler11ControlFlow14requiresUnwindEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV48Compiler11ControlFlow13unwindHandlerEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK3QV48Compiler11ControlFlow5labelEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QV4::Compiler::ControlFlowFinally::requiresUnwind()
  bool requiresUnwind() override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowFinallyCall0 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowFinallyCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QV4::Compiler::ControlFlowFinally::requiresUnwind();
  }

  //  BytecodeGenerator::ExceptionHandler
  //      *QV4::Compiler::ControlFlowFinally::unwindHandler()
  BytecodeGenerator::ExceptionHandler *unwindHandler() override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowFinallyCall1 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowFinallyCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<BytecodeGenerator::ExceptionHandler *>(given);
    }
    return QV4::Compiler::ControlFlowFinally::unwindHandler();
  }

  //  QString QV4::Compiler::ControlFlow::label() const
  QString label() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowFinallyCall2 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowFinallyCall2>(taken[2]);
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

//  bool QV4::Compiler::ControlFlowFinally::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler18ControlFlowFinally14requiresUnwindEv(
    QV4::Compiler::ControlFlowFinally *self) {
  return self->requiresUnwind();
}

//  QV4::Compiler::ControlFlowFinally::~ControlFlowFinally()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler18ControlFlowFinallyD1Ev(
    QV4::Compiler::ControlFlowFinally *self) {
  delete self;
}

//  a Python function taken by a CuteQV4_Compiler_ControlFlowFinally, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_ControlFlowFinally(
    QV4::Compiler::ControlFlowFinally *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_ControlFlowFinally *>(self)->take(key, call);
}

//  bool QV4::Compiler::ControlFlowFinally::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler18ControlFlowFinally14requiresUnwindEv(
    QV4::Compiler::ControlFlowFinally *self) {
  return self->QV4::Compiler::ControlFlowFinally::requiresUnwind();
}
