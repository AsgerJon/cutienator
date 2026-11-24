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

//  Only a class built on QV4::Compiler::ControlFlow may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQV4_Compiler_ControlFlow : QV4::Compiler::ControlFlow {
  using QV4::Compiler::ControlFlow::requiresUnwind;
};

//  A QV4::Compiler::ControlFlow that Python can take functions over in. Every QV4::Compiler::ControlFlow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQV4_Compiler_ControlFlowCall0)(const void *, int *);
typedef bool (*CuteQV4_Compiler_ControlFlowCall1)(const void *, int *);
class CuteQV4_Compiler_ControlFlow : public QV4::Compiler::ControlFlow {
public:
  using QV4::Compiler::ControlFlow::ControlFlow;
  CuteQV4_Compiler_ControlFlow(const QV4::Compiler::ControlFlow &other) : QV4::Compiler::ControlFlow(other) {}
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

  //  QString QV4::Compiler::ControlFlow::label() const
  QString label() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowCall0 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowCall1 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QV4::Compiler::ControlFlow::requiresUnwind();
  }
};

//  QV4::Compiler::ControlFlow::ControlFlow(Codegen *cg, Type type)
extern "C" Q_DECL_EXPORT
QV4::Compiler::ControlFlow *ritual_ZN3QV48Compiler11ControlFlowC1EPNS0_7CodegenENS1_4TypeE(
    QV4::Compiler::Codegen *cg,
    QV4::Compiler::ControlFlow::Type type) {
  return new CuteQV4_Compiler_ControlFlow(cg, type);
}

//  QV4::Compiler::ControlFlow::~ControlFlow()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler11ControlFlowD1Ev(
    QV4::Compiler::ControlFlow *self) {
  delete self;
}

//  UnwindTarget QV4::Compiler::ControlFlow::unwindTarget(UnwindType type,
//      const QString &label)
extern "C" Q_DECL_EXPORT
QV4::Compiler::ControlFlow::UnwindTarget *ritual_ZN3QV48Compiler11ControlFlow12unwindTargetENS1_10UnwindTypeERK7QString(
    QV4::Compiler::ControlFlow *self,
    QV4::Compiler::ControlFlow::UnwindType type,
    const QString *label) {
  return new QV4::Compiler::ControlFlow::UnwindTarget(
      self->unwindTarget(
          type,
          *label));
}

//  QString QV4::Compiler::ControlFlow::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler11ControlFlow5labelEv(
    const QV4::Compiler::ControlFlow *self) {
  return new QString(self->label());
}

//  bool QV4::Compiler::ControlFlow::hasLoop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler11ControlFlow7hasLoopEv(
    const QV4::Compiler::ControlFlow *self) {
  return self->hasLoop();
}

//  bool QV4::Compiler::ControlFlow::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler11ControlFlow14requiresUnwindEv(
    QV4::Compiler::ControlFlow *self) {
  return self->requiresUnwind();
}

//  QString QV4::Compiler::ControlFlow::loopLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV48Compiler11ControlFlow9loopLabelEv(
    const QV4::Compiler::ControlFlow *self) {
  return new QString(self->loopLabel());
}

//  a Python function taken by a CuteQV4_Compiler_ControlFlow, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_ControlFlow(
    QV4::Compiler::ControlFlow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_ControlFlow *>(self)->take(key, call);
}

//  QString QV4::Compiler::ControlFlow::label() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK3QV48Compiler11ControlFlow5labelEv(
    const QV4::Compiler::ControlFlow *self) {
  return new QString(self->QV4::Compiler::ControlFlow::label());
}

//  bool QV4::Compiler::ControlFlow::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler11ControlFlow14requiresUnwindEv(
    QV4::Compiler::ControlFlow *self) {
  return static_cast<OwnQV4_Compiler_ControlFlow *>(self)->OwnQV4_Compiler_ControlFlow::requiresUnwind();
}
