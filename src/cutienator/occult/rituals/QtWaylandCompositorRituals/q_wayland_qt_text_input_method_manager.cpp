//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandqttextinputmethodmanager.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWaylandCompositor/qwaylandqttextinputmethodmanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QWaylandQtTextInputMethodManager that Python can take functions over in. Every QWaylandQtTextInputMethodManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandQtTextInputMethodManagerCall0)(const void *, int *);
class CuteQWaylandQtTextInputMethodManager : public QWaylandQtTextInputMethodManager {
public:
  using QWaylandQtTextInputMethodManager::QWaylandQtTextInputMethodManager;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN32QWaylandQtTextInputMethodManager10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandQtTextInputMethodManager::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQtTextInputMethodManagerCall0 call = reinterpret_cast<CuteQWaylandQtTextInputMethodManagerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQtTextInputMethodManager::initialize();
  }
};

//  const QMetaObject *QWaylandQtTextInputMethodManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QWaylandQtTextInputMethodManager10metaObjectEv(
    const QWaylandQtTextInputMethodManager *self) {
  return self->metaObject();
}

//  void *QWaylandQtTextInputMethodManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QWaylandQtTextInputMethodManager11qt_metacastEPKc(
    QWaylandQtTextInputMethodManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQtTextInputMethodManager::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QWaylandQtTextInputMethodManager11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQtTextInputMethodManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQtTextInputMethodManager::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QWaylandQtTextInputMethodManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQtTextInputMethodManager::tr(s, c, n));
}

//  QWaylandQtTextInputMethodManagerPrivate
//      *QWaylandQtTextInputMethodManager::d_func()
extern "C" Q_DECL_EXPORT
QWaylandQtTextInputMethodManagerPrivate *ritual_ZN32QWaylandQtTextInputMethodManager6d_funcEv(
    QWaylandQtTextInputMethodManager *self) {
  return self->d_func();
}

//  const QWaylandQtTextInputMethodManagerPrivate
//      *QWaylandQtTextInputMethodManager::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandQtTextInputMethodManagerPrivate *ritual_ZNK32QWaylandQtTextInputMethodManager6d_funcEv(
    const QWaylandQtTextInputMethodManager *self) {
  return self->d_func();
}

//  QWaylandQtTextInputMethodManager::QWaylandQtTextInputMethodManager()
extern "C" Q_DECL_EXPORT
QWaylandQtTextInputMethodManager *ritual_ZN32QWaylandQtTextInputMethodManagerC1Ev() {
  return new CuteQWaylandQtTextInputMethodManager();
}

//  QWaylandQtTextInputMethodManager::QWaylandQtTextInputMethodManager(QWayla
//      ndCompositor *compositor)
extern "C" Q_DECL_EXPORT
QWaylandQtTextInputMethodManager *ritual_ZN32QWaylandQtTextInputMethodManagerC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandQtTextInputMethodManager(compositor);
}

//  void QWaylandQtTextInputMethodManager::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QWaylandQtTextInputMethodManager10initializeEv(
    QWaylandQtTextInputMethodManager *self) {
  self->initialize();
}

//  const struct wl_interface *QWaylandQtTextInputMethodManager::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN32QWaylandQtTextInputMethodManager9interfaceEv() {
  return QWaylandQtTextInputMethodManager::interface();
}

//  QByteArray QWaylandQtTextInputMethodManager::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN32QWaylandQtTextInputMethodManager13interfaceNameEv() {
  return new QByteArray(QWaylandQtTextInputMethodManager::interfaceName());
}

//  a Python function taken by a CuteQWaylandQtTextInputMethodManager, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQtTextInputMethodManager(
    QWaylandQtTextInputMethodManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQtTextInputMethodManager *>(self)->take(key, call);
}

//  void QWaylandQtTextInputMethodManager::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QWaylandQtTextInputMethodManager10initializeEv(
    QWaylandQtTextInputMethodManager *self) {
  self->QWaylandQtTextInputMethodManager::initialize();
}
