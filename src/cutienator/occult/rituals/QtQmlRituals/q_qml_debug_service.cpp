//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugservice_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlDebugService that Python can take functions over in. Every QQmlDebugService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall2)(const void *, const QByteArray *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall3)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall4)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall5)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlDebugServiceCall6)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugServiceCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlDebugServiceCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServiceCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServiceCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServiceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServiceCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlDebugServiceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlDebugService : public QQmlDebugService {
public:
  using QQmlDebugService::QQmlDebugService;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService12stateChangedENS_5StateE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService15messageReceivedERK10QByteArray")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService11engineAddedEP9QJSEngine")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService13engineRemovedEP9QJSEngine")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::stateAboutToBeChanged(State a0)
  void stateAboutToBeChanged(QQmlDebugService::State a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlDebugServiceCall0 call = reinterpret_cast<CuteQQmlDebugServiceCall0>(taken[0]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDebugService::stateAboutToBeChanged(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::stateChanged(State a0)
  void stateChanged(QQmlDebugService::State a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlDebugServiceCall1 call = reinterpret_cast<CuteQQmlDebugServiceCall1>(taken[1]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDebugService::stateChanged(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::messageReceived(const QByteArray &a0)
  void messageReceived(const QByteArray &a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlDebugServiceCall2 call = reinterpret_cast<CuteQQmlDebugServiceCall2>(taken[2]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::messageReceived(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAboutToBeAdded(QJSEngine *engine)
  void engineAboutToBeAdded(QJSEngine *engine) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlDebugServiceCall3 call = reinterpret_cast<CuteQQmlDebugServiceCall3>(taken[3]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAboutToBeAdded(engine);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAboutToBeRemoved(QJSEngine *engine)
  void engineAboutToBeRemoved(QJSEngine *engine) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlDebugServiceCall4 call = reinterpret_cast<CuteQQmlDebugServiceCall4>(taken[4]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAboutToBeRemoved(engine);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAdded(QJSEngine *a0)
  void engineAdded(QJSEngine *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlDebugServiceCall5 call = reinterpret_cast<CuteQQmlDebugServiceCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAdded(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineRemoved(QJSEngine *a0)
  void engineRemoved(QJSEngine *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlDebugServiceCall6 call = reinterpret_cast<CuteQQmlDebugServiceCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineRemoved(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlDebugServiceCall7 call = reinterpret_cast<CuteQQmlDebugServiceCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlDebugServiceCall8 call = reinterpret_cast<CuteQQmlDebugServiceCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlDebugServiceCall9 call = reinterpret_cast<CuteQQmlDebugServiceCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlDebugServiceCall10 call = reinterpret_cast<CuteQQmlDebugServiceCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlDebugServiceCall11 call = reinterpret_cast<CuteQQmlDebugServiceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlDebugServiceCall12 call = reinterpret_cast<CuteQQmlDebugServiceCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlDebugServiceCall13 call = reinterpret_cast<CuteQQmlDebugServiceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlDebugService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlDebugService10metaObjectEv(
    const QQmlDebugService *self) {
  return self->metaObject();
}

//  QString QQmlDebugService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlDebugService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlDebugService::tr(s, c, n));
}

//  QQmlDebugService::~QQmlDebugService()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugServiceD1Ev(QQmlDebugService *self) {
  delete self;
}

//  const QString &QQmlDebugService::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQmlDebugService4nameEv(const QQmlDebugService *self) {
  return new QString(self->name());
}

//  float QQmlDebugService::version() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QQmlDebugService7versionEv(const QQmlDebugService *self) {
  return self->version();
}

//  State QQmlDebugService::state() const
extern "C" Q_DECL_EXPORT
QQmlDebugService::State ritual_ZNK16QQmlDebugService5stateEv(
    const QQmlDebugService *self) {
  return self->state();
}

//  void QQmlDebugService::setState(State newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService8setStateENS_5StateE(
    QQmlDebugService *self,
    QQmlDebugService::State newState) {
  self->setState(newState);
}

//  void QQmlDebugService::stateAboutToBeChanged(State a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE(
    QQmlDebugService *self,
    QQmlDebugService::State a0) {
  self->stateAboutToBeChanged(a0);
}

//  void QQmlDebugService::stateChanged(State a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService12stateChangedENS_5StateE(
    QQmlDebugService *self,
    QQmlDebugService::State a0) {
  self->stateChanged(a0);
}

//  void QQmlDebugService::messageReceived(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService15messageReceivedERK10QByteArray(
    QQmlDebugService *self,
    const QByteArray *a0) {
  self->messageReceived(*a0);
}

//  void QQmlDebugService::engineAboutToBeAdded(QJSEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *engine) {
  self->engineAboutToBeAdded(engine);
}

//  void QQmlDebugService::engineAboutToBeRemoved(QJSEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *engine) {
  self->engineAboutToBeRemoved(engine);
}

//  void QQmlDebugService::engineAdded(QJSEngine *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService11engineAddedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *a0) {
  self->engineAdded(a0);
}

//  void QQmlDebugService::engineRemoved(QJSEngine *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlDebugService13engineRemovedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *a0) {
  self->engineRemoved(a0);
}

//  const QHash<int, QObject *> &QQmlDebugService::objectsForIds()
extern "C" Q_DECL_EXPORT
QHash<int, QObject *> *ritual_ZN16QQmlDebugService13objectsForIdsEv() {
  return new QHash<int, QObject *>(QQmlDebugService::objectsForIds());
}

//  int QQmlDebugService::idForObject(QObject *a0)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlDebugService11idForObjectEP7QObject(QObject *a0) {
  return QQmlDebugService::idForObject(a0);
}

//  QObject *QQmlDebugService::objectForId(int id)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN16QQmlDebugService11objectForIdEi(int id) {
  return QQmlDebugService::objectForId(id);
}

//  QQmlDebugService::QQmlDebugService(const QString &a0, float version,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlDebugService *ritual_ZN16QQmlDebugServiceC1ERK7QStringfP7QObject(
    const QString *a0,
    float version,
    QObject *parent) {
  return new CuteQQmlDebugService(*a0, version, parent);
}

//  a Python function taken by a CuteQQmlDebugService, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlDebugService(
    QQmlDebugService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlDebugService *>(self)->take(key, call);
}

//  void QQmlDebugService::stateAboutToBeChanged(State a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE(
    QQmlDebugService *self,
    QQmlDebugService::State a0) {
  self->QQmlDebugService::stateAboutToBeChanged(a0);
}

//  void QQmlDebugService::stateChanged(State a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService12stateChangedENS_5StateE(
    QQmlDebugService *self,
    QQmlDebugService::State a0) {
  self->QQmlDebugService::stateChanged(a0);
}

//  void QQmlDebugService::messageReceived(const QByteArray &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService15messageReceivedERK10QByteArray(
    QQmlDebugService *self,
    const QByteArray *a0) {
  self->QQmlDebugService::messageReceived(*a0);
}

//  void QQmlDebugService::engineAboutToBeAdded(QJSEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *engine) {
  self->QQmlDebugService::engineAboutToBeAdded(engine);
}

//  void QQmlDebugService::engineAboutToBeRemoved(QJSEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *engine) {
  self->QQmlDebugService::engineAboutToBeRemoved(engine);
}

//  void QQmlDebugService::engineAdded(QJSEngine *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService11engineAddedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *a0) {
  self->QQmlDebugService::engineAdded(a0);
}

//  void QQmlDebugService::engineRemoved(QJSEngine *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQmlDebugService13engineRemovedEP9QJSEngine(
    QQmlDebugService *self,
    QJSEngine *a0) {
  self->QQmlDebugService::engineRemoved(a0);
}

#endif  // QT_CONFIG(qml_debug)
#endif  // QT_CONFIG(qml_debug)
