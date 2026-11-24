//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugserviceinterfaces_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlEngineControlService that Python can take functions over in. Every QQmlEngineControlService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall2)(const void *, const QByteArray *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall3)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall4)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall5)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlEngineControlServiceCall6)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlEngineControlServiceCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlEngineControlServiceCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineControlServiceCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineControlServiceCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineControlServiceCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineControlServiceCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlEngineControlServiceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlEngineControlService : public QQmlEngineControlService {
public:
  using QQmlEngineControlService::QQmlEngineControlService;
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
      CuteQQmlEngineControlServiceCall0 call = reinterpret_cast<CuteQQmlEngineControlServiceCall0>(taken[0]);
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
      CuteQQmlEngineControlServiceCall1 call = reinterpret_cast<CuteQQmlEngineControlServiceCall1>(taken[1]);
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
      CuteQQmlEngineControlServiceCall2 call = reinterpret_cast<CuteQQmlEngineControlServiceCall2>(taken[2]);
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
      CuteQQmlEngineControlServiceCall3 call = reinterpret_cast<CuteQQmlEngineControlServiceCall3>(taken[3]);
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
      CuteQQmlEngineControlServiceCall4 call = reinterpret_cast<CuteQQmlEngineControlServiceCall4>(taken[4]);
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
      CuteQQmlEngineControlServiceCall5 call = reinterpret_cast<CuteQQmlEngineControlServiceCall5>(taken[5]);
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
      CuteQQmlEngineControlServiceCall6 call = reinterpret_cast<CuteQQmlEngineControlServiceCall6>(taken[6]);
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
      CuteQQmlEngineControlServiceCall7 call = reinterpret_cast<CuteQQmlEngineControlServiceCall7>(taken[7]);
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
      CuteQQmlEngineControlServiceCall8 call = reinterpret_cast<CuteQQmlEngineControlServiceCall8>(taken[8]);
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
      CuteQQmlEngineControlServiceCall9 call = reinterpret_cast<CuteQQmlEngineControlServiceCall9>(taken[9]);
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
      CuteQQmlEngineControlServiceCall10 call = reinterpret_cast<CuteQQmlEngineControlServiceCall10>(taken[10]);
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
      CuteQQmlEngineControlServiceCall11 call = reinterpret_cast<CuteQQmlEngineControlServiceCall11>(taken[11]);
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
      CuteQQmlEngineControlServiceCall12 call = reinterpret_cast<CuteQQmlEngineControlServiceCall12>(taken[12]);
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
      CuteQQmlEngineControlServiceCall13 call = reinterpret_cast<CuteQQmlEngineControlServiceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlEngineControlService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQmlEngineControlService10metaObjectEv(
    const QQmlEngineControlService *self) {
  return self->metaObject();
}

//  QString QQmlEngineControlService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQmlEngineControlService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlEngineControlService::tr(s, c, n));
}

//  QQmlEngineControlService::~QQmlEngineControlService()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlEngineControlServiceD1Ev(
    QQmlEngineControlService *self) {
  delete self;
}

//  QQmlEngineControlService::QQmlEngineControlService(float version, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQmlEngineControlService *ritual_ZN24QQmlEngineControlServiceC1EfP7QObject(
    float version,
    QObject *parent) {
  return new CuteQQmlEngineControlService(version, parent);
}

//  a Python function taken by a CuteQQmlEngineControlService, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlEngineControlService(
    QQmlEngineControlService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlEngineControlService *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
