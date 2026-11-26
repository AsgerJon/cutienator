//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <cstring>

//  A QQmlSA::ElementPass that Python can take functions over in. Every QQmlSA::ElementPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQmlSA_ElementPassCall0)(const void *, const QQmlSA::Element *, int *);
typedef void (*CuteQQmlSA_ElementPassCall1)(const void *, const QQmlSA::Element *, int *);
class CuteQQmlSA_ElementPass : public QQmlSA::ElementPass {
public:
  using QQmlSA::ElementPass::ElementPass;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlSA11ElementPass9shouldRunERKNS_7ElementE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QQmlSA11ElementPass3runERKNS_7ElementE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QQmlSA::ElementPass::shouldRun(const Element &element)
  bool shouldRun(const QQmlSA::Element &element) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSA_ElementPassCall0 call = reinterpret_cast<CuteQQmlSA_ElementPassCall0>(taken[0]);
      bool given = call(this, &element, &handled);
      if (handled) return given;
    }
    return QQmlSA::ElementPass::shouldRun(element);
  }

  //  void QQmlSA::ElementPass::run(const Element &element)
  void run(const QQmlSA::Element &element) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlSA_ElementPassCall1 call = reinterpret_cast<CuteQQmlSA_ElementPassCall1>(taken[1]);
      call(this, &element, &handled);
      if (handled) return;
    }
  }
};

//  QQmlSA::ElementPass::ElementPass(PassManager *manager)
extern "C" Q_DECL_EXPORT
QQmlSA::ElementPass *ritual_ZN6QQmlSA11ElementPassC1EPNS_11PassManagerE(
    QQmlSA::PassManager *manager) {
  return new CuteQQmlSA_ElementPass(manager);
}

//  bool QQmlSA::ElementPass::shouldRun(const Element &element)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSA11ElementPass9shouldRunERKNS_7ElementE(
    QQmlSA::ElementPass *self,
    const QQmlSA::Element *element) {
  return self->shouldRun(*element);
}

//  void QQmlSA::ElementPass::run(const Element &element)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA11ElementPass3runERKNS_7ElementE(
    QQmlSA::ElementPass *self,
    const QQmlSA::Element *element) {
  self->run(*element);
}

//  a Python function taken by a CuteQQmlSA_ElementPass, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSA_ElementPass(
    QQmlSA::ElementPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSA_ElementPass *>(self)->take(key, call);
}

//  bool QQmlSA::ElementPass::shouldRun(const Element &element)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN6QQmlSA11ElementPass9shouldRunERKNS_7ElementE(
    QQmlSA::ElementPass *self,
    const QQmlSA::Element *element) {
  return self->QQmlSA::ElementPass::shouldRun(*element);
}
