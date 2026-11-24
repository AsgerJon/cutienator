//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandtextinputmanager.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandtextinputmanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QWaylandTextInputManager that Python can take functions over in. Every QWaylandTextInputManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandTextInputManagerCall0)(const void *, int *);
class CuteQWaylandTextInputManager : public QWaylandTextInputManager {
public:
  using QWaylandTextInputManager::QWaylandTextInputManager;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QWaylandTextInputManager10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandTextInputManager::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandTextInputManagerCall0 call = reinterpret_cast<CuteQWaylandTextInputManagerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandTextInputManager::initialize();
  }
};

//  const QMetaObject *QWaylandTextInputManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QWaylandTextInputManager10metaObjectEv(
    const QWaylandTextInputManager *self) {
  return self->metaObject();
}

//  QString QWaylandTextInputManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QWaylandTextInputManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandTextInputManager::tr(s, c, n));
}

//  QWaylandTextInputManager::QWaylandTextInputManager()
extern "C" Q_DECL_EXPORT
QWaylandTextInputManager *ritual_ZN24QWaylandTextInputManagerC1Ev() {
  return new CuteQWaylandTextInputManager();
}

//  QWaylandTextInputManager::QWaylandTextInputManager(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
QWaylandTextInputManager *ritual_ZN24QWaylandTextInputManagerC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandTextInputManager(compositor);
}

//  void QWaylandTextInputManager::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandTextInputManager10initializeEv(
    QWaylandTextInputManager *self) {
  self->initialize();
}

//  QByteArray QWaylandTextInputManager::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN24QWaylandTextInputManager13interfaceNameEv() {
  return new QByteArray(QWaylandTextInputManager::interfaceName());
}

//  a Python function taken by a CuteQWaylandTextInputManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandTextInputManager(
    QWaylandTextInputManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandTextInputManager *>(self)->take(key, call);
}

//  void QWaylandTextInputManager::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWaylandTextInputManager10initializeEv(
    QWaylandTextInputManager *self) {
  self->QWaylandTextInputManager::initialize();
}
