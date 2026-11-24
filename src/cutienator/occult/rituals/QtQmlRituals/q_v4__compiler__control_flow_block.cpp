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

//  A QV4::Compiler::ControlFlowBlock that Python can take functions over in. Every QV4::Compiler::ControlFlowBlock
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQV4_Compiler_ControlFlowBlockCall0)(const void *, int *);
typedef QString * (*CuteQV4_Compiler_ControlFlowBlockCall1)(const void *, int *);
class CuteQV4_Compiler_ControlFlowBlock : public QV4::Compiler::ControlFlowBlock {
public:
  using QV4::Compiler::ControlFlowBlock::ControlFlowBlock;
  CuteQV4_Compiler_ControlFlowBlock(const QV4::Compiler::ControlFlowBlock &other) : QV4::Compiler::ControlFlowBlock(other) {}
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

  //  bool QV4::Compiler::ControlFlowBlock::requiresUnwind()
  bool requiresUnwind() override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowBlockCall0 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowBlockCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QV4::Compiler::ControlFlowBlock::requiresUnwind();
  }

  //  QString QV4::Compiler::ControlFlow::label() const
  QString label() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4_Compiler_ControlFlowBlockCall1 call = reinterpret_cast<CuteQV4_Compiler_ControlFlowBlockCall1>(taken[1]);
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

//  QV4::Compiler::ControlFlowBlock::~ControlFlowBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler16ControlFlowBlockD1Ev(
    QV4::Compiler::ControlFlowBlock *self) {
  delete self;
}

//  bool QV4::Compiler::ControlFlowBlock::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler16ControlFlowBlock14requiresUnwindEv(
    QV4::Compiler::ControlFlowBlock *self) {
  return self->requiresUnwind();
}

//  a Python function taken by a CuteQV4_Compiler_ControlFlowBlock, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_Compiler_ControlFlowBlock(
    QV4::Compiler::ControlFlowBlock *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_Compiler_ControlFlowBlock *>(self)->take(key, call);
}

//  bool QV4::Compiler::ControlFlowBlock::requiresUnwind()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN3QV48Compiler16ControlFlowBlock14requiresUnwindEv(
    QV4::Compiler::ControlFlowBlock *self) {
  return self->QV4::Compiler::ControlFlowBlock::requiresUnwind();
}
