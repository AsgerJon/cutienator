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

//  A QV4::Compiler::ControlFlowUnwind that Python can take functions over in. Every QV4::Compiler::ControlFlowUnwind
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQV4_Compiler_ControlFlowUnwindCall0)(const void *, int *);
typedef QString * (*CuteQV4_Compiler_ControlFlowUnwindCall1)(const void *, int *);
typedef bool (*CuteQV4_Compiler_ControlFlowUnwindCall2)(const void *, int *);
class CuteQV4_Compiler_ControlFlowUnwind : public QV4::Compiler::ControlFlowUnwind {
public:
  using QV4::Compiler::ControlFlowUnwind::ControlFlowUnwind;
  CuteQV4_Compiler_ControlFlowUnwind(const QV4::Compiler::ControlFlowUnwind & other) : QV4::Compiler::ControlFlowUnwind(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV48Compiler11ControlFlow13unwindHandlerEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK3QV48Compiler11ControlFlow5labelEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV48Compiler11ControlFlow14requiresUnwindEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  BytecodeGenerator::ExceptionHandler
  //      *QV4::Compiler::ControlFlowUnwind::unwindHandler()
  BytecodeGenerator::ExceptionHandler *unwindHandler() override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowUnwindCall0 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowUnwindCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<BytecodeGenerator::ExceptionHandler *>(given);
    }
    return QV4::Compiler::ControlFlowUnwind::unwindHandler();
  }

  //  QString QV4::Compiler::ControlFlow::label() const
  QString label() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowUnwindCall1 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowUnwindCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QV4::Compiler::ControlFlow::label();
  }

  //  bool QV4::Compiler::ControlFlow::requiresUnwind()
  bool requiresUnwind() override {
    if (taken[2]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowUnwindCall2 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowUnwindCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QV4::Compiler::ControlFlow::requiresUnwind();
  }
};

//  QV4::Compiler::ControlFlowUnwind::ControlFlowUnwind(Codegen *cg, Type
//      type)
extern "C" Q_DECL_EXPORT
QV4::Compiler::ControlFlowUnwind *ritual_ZN3QV48Compiler17ControlFlowUnwindC1EPNS0_7CodegenENS0_11ControlFlow4TypeE(
    QV4::Compiler::Codegen *cg,
    QV4::Compiler::ControlFlow::Type type) {
  return new CuteQV4_Compiler_ControlFlowUnwind(cg, type);
}

//  void QV4::Compiler::ControlFlowUnwind::setupUnwindHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler17ControlFlowUnwind18setupUnwindHandlerEv(
    QV4::Compiler::ControlFlowUnwind *self) {
  self->setupUnwindHandler();
}

//  QV4::Compiler::ControlFlowUnwind::~ControlFlowUnwind()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler17ControlFlowUnwindD1Ev(
    QV4::Compiler::ControlFlowUnwind *self) {
  delete self;
}

//  a Python function taken by a CuteQV4_Compiler_ControlFlowUnwind, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_ControlFlowUnwind(
    QV4::Compiler::ControlFlowUnwind *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_ControlFlowUnwind *>(self)->take(key, call);
}
