//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <cstring>

//  A QQmlSA::LintPlugin that Python can take functions over in. Every QQmlSA::LintPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlSA_LintPluginCall0)(const void *, QQmlSA::PassManager *, const QQmlSA::Element *, int *);
class CuteQQmlSA_LintPlugin : public QQmlSA::LintPlugin {
public:
  using QQmlSA::LintPlugin::LintPlugin;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QQmlSA10LintPlugin14registerPassesEPNS_11PassManagerERKNS_7ElementE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQmlSA::LintPlugin::registerPasses(PassManager *manager, const
  //      Element &rootElement)
  void registerPasses(
      QQmlSA::PassManager *manager,
      const QQmlSA::Element &rootElement) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlSA_LintPluginCall0 call = reinterpret_cast<CuteQQmlSA_LintPluginCall0>(taken[0]);
      call(this, manager, &rootElement, &handled);
      if (handled) return;
    }
  }
};

//  QQmlSA::LintPlugin::LintPlugin()
extern "C" Q_DECL_EXPORT
QQmlSA::LintPlugin *ritual_ZN6QQmlSA10LintPluginC1Ev() {
  return new CuteQQmlSA_LintPlugin();
}

//  QQmlSA::LintPlugin::~LintPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA10LintPluginD1Ev(QQmlSA::LintPlugin *self) {
  delete self;
}

//  void QQmlSA::LintPlugin::registerPasses(PassManager *manager, const
//      Element &rootElement)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA10LintPlugin14registerPassesEPNS_11PassManagerERKNS_7ElementE(
    QQmlSA::LintPlugin *self,
    QQmlSA::PassManager *manager,
    const QQmlSA::Element *rootElement) {
  self->registerPasses(manager, *rootElement);
}

//  a Python function taken by a CuteQQmlSA_LintPlugin, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlSA_LintPlugin(
    QQmlSA::LintPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlSA_LintPlugin *>(self)->take(key, call);
}
