//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandqtwindowmanager.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandqtwindowmanager.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QWaylandQtWindowManager that Python can take functions over in. Every QWaylandQtWindowManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandQtWindowManagerCall0)(const void *, int *);
class CuteQWaylandQtWindowManager : public QWaylandQtWindowManager {
public:
  using QWaylandQtWindowManager::QWaylandQtWindowManager;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QWaylandQtWindowManager10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandQtWindowManager::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQtWindowManagerCall0 call = reinterpret_cast<CuteQWaylandQtWindowManagerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQtWindowManager::initialize();
  }
};

//  const QMetaObject *QWaylandQtWindowManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QWaylandQtWindowManager10metaObjectEv(
    const QWaylandQtWindowManager *self) {
  return self->metaObject();
}

//  QString QWaylandQtWindowManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QWaylandQtWindowManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQtWindowManager::tr(s, c, n));
}

//  QWaylandQtWindowManager::QWaylandQtWindowManager()
extern "C" Q_DECL_EXPORT
QWaylandQtWindowManager *ritual_ZN23QWaylandQtWindowManagerC1Ev() {
  return new CuteQWaylandQtWindowManager();
}

//  QWaylandQtWindowManager::QWaylandQtWindowManager(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
QWaylandQtWindowManager *ritual_ZN23QWaylandQtWindowManagerC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandQtWindowManager(compositor);
}

//  bool QWaylandQtWindowManager::showIsFullScreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWaylandQtWindowManager16showIsFullScreenEv(
    const QWaylandQtWindowManager *self) {
  return self->showIsFullScreen();
}

//  void QWaylandQtWindowManager::setShowIsFullScreen(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQtWindowManager19setShowIsFullScreenEb(
    QWaylandQtWindowManager *self,
    bool value) {
  self->setShowIsFullScreen(value);
}

//  void QWaylandQtWindowManager::sendQuitMessage(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQtWindowManager15sendQuitMessageEP14QWaylandClient(
    QWaylandQtWindowManager *self,
    QWaylandClient *client) {
  self->sendQuitMessage(client);
}

//  void QWaylandQtWindowManager::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWaylandQtWindowManager10initializeEv(
    QWaylandQtWindowManager *self) {
  self->initialize();
}

//  QByteArray QWaylandQtWindowManager::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN23QWaylandQtWindowManager13interfaceNameEv() {
  return new QByteArray(QWaylandQtWindowManager::interfaceName());
}

//  a Python function taken by a CuteQWaylandQtWindowManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQtWindowManager(
    QWaylandQtWindowManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQtWindowManager *>(self)->take(key, call);
}

//  void QWaylandQtWindowManager::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QWaylandQtWindowManager10initializeEv(
    QWaylandQtWindowManager *self) {
  self->QWaylandQtWindowManager::initialize();
}
