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

//  A QV4::Compiler::ControlFlowLoop that Python can take functions over in. Every QV4::Compiler::ControlFlowLoop
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQV4_Compiler_ControlFlowLoopCall0)(const void *, int *);
typedef bool (*CuteQV4_Compiler_ControlFlowLoopCall1)(const void *, int *);
class CuteQV4_Compiler_ControlFlowLoop : public QV4::Compiler::ControlFlowLoop {
public:
  using QV4::Compiler::ControlFlowLoop::ControlFlowLoop;
  CuteQV4_Compiler_ControlFlowLoop(const QV4::Compiler::ControlFlowLoop &other) : QV4::Compiler::ControlFlowLoop(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK3QV48Compiler11ControlFlow5labelEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV48Compiler11ControlFlow14requiresUnwindEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QString QV4::Compiler::ControlFlowLoop::label() const
  QString label() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowLoopCall0 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowLoopCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QV4::Compiler::ControlFlowLoop::label();
  }

  //  bool QV4::Compiler::ControlFlowUnwindCleanup::requiresUnwind()
  bool requiresUnwind() override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowLoopCall1 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowLoopCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QV4::Compiler::ControlFlowUnwindCleanup::requiresUnwind();
  }
};

//  QString QV4::Compiler::ControlFlowLoop::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler15ControlFlowLoop5labelEv(
    const QV4::Compiler::ControlFlowLoop *self) {
  return new QString(self->label());
}

//  QV4::Compiler::ControlFlowLoop::~ControlFlowLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler15ControlFlowLoopD1Ev(
    QV4::Compiler::ControlFlowLoop *self) {
  delete self;
}

//  a Python function taken by a CuteQV4_Compiler_ControlFlowLoop, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_ControlFlowLoop(
    QV4::Compiler::ControlFlowLoop *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_ControlFlowLoop *>(self)->take(key, call);
}

//  QString QV4::Compiler::ControlFlowLoop::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK3QV48Compiler15ControlFlowLoop5labelEv(
    const QV4::Compiler::ControlFlowLoop *self) {
  return new QString(self->QV4::Compiler::ControlFlowLoop::label());
}
