//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractformeditorplugin.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDesigner/abstractformeditorplugin.h>
#include <cstring>

//  A QDesignerFormEditorPluginInterface that Python can take functions over in. Every QDesignerFormEditorPluginInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQDesignerFormEditorPluginInterfaceCall0)(const void *, int *);
typedef void (*CuteQDesignerFormEditorPluginInterfaceCall1)(const void *, QDesignerFormEditorInterface *, int *);
typedef void * (*CuteQDesignerFormEditorPluginInterfaceCall2)(const void *, int *);
typedef void * (*CuteQDesignerFormEditorPluginInterfaceCall3)(const void *, int *);
class CuteQDesignerFormEditorPluginInterface : public QDesignerFormEditorPluginInterface {
public:
  using QDesignerFormEditorPluginInterface::QDesignerFormEditorPluginInterface;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK34QDesignerFormEditorPluginInterface13isInitializedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN34QDesignerFormEditorPluginInterface10initializeEP28QDesignerFormEditorInterface")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormEditorPluginInterface6actionEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK34QDesignerFormEditorPluginInterface4coreEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool QDesignerFormEditorPluginInterface::isInitialized() const
  bool isInitialized() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerFormEditorPluginInterfaceCall0 call = reinterpret_cast<CuteQDesignerFormEditorPluginInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QDesignerFormEditorPluginInterface::initialize(QDesignerFormEdit
  //      orInterface *core)
  void initialize(QDesignerFormEditorInterface *core) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerFormEditorPluginInterfaceCall1 call = reinterpret_cast<CuteQDesignerFormEditorPluginInterfaceCall1>(taken[1]);
      call(this, core, &handled);
      if (handled) return;
    }
  }

  //  QAction *QDesignerFormEditorPluginInterface::action() const
  QAction *action() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerFormEditorPluginInterfaceCall2 call = reinterpret_cast<CuteQDesignerFormEditorPluginInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAction *>(given);
    }
    return {};
  }

  //  QDesignerFormEditorInterface
  //      *QDesignerFormEditorPluginInterface::core() const
  QDesignerFormEditorInterface *core() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerFormEditorPluginInterfaceCall3 call = reinterpret_cast<CuteQDesignerFormEditorPluginInterfaceCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDesignerFormEditorInterface *>(given);
    }
    return {};
  }
};

//  QDesignerFormEditorPluginInterface::~QDesignerFormEditorPluginInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormEditorPluginInterfaceD1Ev(
    QDesignerFormEditorPluginInterface *self) {
  delete self;
}

//  bool QDesignerFormEditorPluginInterface::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK34QDesignerFormEditorPluginInterface13isInitializedEv(
    const QDesignerFormEditorPluginInterface *self) {
  return self->isInitialized();
}

//  void QDesignerFormEditorPluginInterface::initialize(QDesignerFormEditorIn
//      terface *core)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QDesignerFormEditorPluginInterface10initializeEP28QDesignerFormEditorInterface(
    QDesignerFormEditorPluginInterface *self,
    QDesignerFormEditorInterface *core) {
  self->initialize(core);
}

//  QAction *QDesignerFormEditorPluginInterface::action() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK34QDesignerFormEditorPluginInterface6actionEv(
    const QDesignerFormEditorPluginInterface *self) {
  return self->action();
}

//  QDesignerFormEditorInterface *QDesignerFormEditorPluginInterface::core()
//      const
extern "C" Q_DECL_EXPORT
QDesignerFormEditorInterface *ritual_ZNK34QDesignerFormEditorPluginInterface4coreEv(
    const QDesignerFormEditorPluginInterface *self) {
  return self->core();
}

//  a Python function taken by a CuteQDesignerFormEditorPluginInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerFormEditorPluginInterface(
    QDesignerFormEditorPluginInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerFormEditorPluginInterface *>(self)->take(key, call);
}
