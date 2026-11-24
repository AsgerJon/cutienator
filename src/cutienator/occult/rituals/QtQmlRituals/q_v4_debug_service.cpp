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

//  A QV4DebugService that Python can take functions over in. Every QV4DebugService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQV4DebugServiceCall0)(const void *, const QString *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall1)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall2)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall3)(const void *, const QByteArray *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall4)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall5)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall6)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQV4DebugServiceCall7)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQV4DebugServiceCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQV4DebugServiceCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4DebugServiceCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4DebugServiceCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4DebugServiceCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4DebugServiceCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQV4DebugServiceCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQV4DebugService : public QV4DebugService {
public:
  using QV4DebugService::QV4DebugService;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN15QV4DebugService13signalEmittedERK7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService12stateChangedENS_5StateE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService15messageReceivedERK10QByteArray")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService11engineAddedEP9QJSEngine")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService13engineRemovedEP9QJSEngine")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !(!QT_CONFIG(qml_debug))
  //  void QV4DebugService::signalEmitted(const QString &signal)
  void signalEmitted(const QString &signal) override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4DebugServiceCall0 call = reinterpret_cast<CuteQV4DebugServiceCall0>(taken[0]);
      call(this, &signal, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::stateAboutToBeChanged(State a0)
  void stateAboutToBeChanged(QQmlDebugService::State a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQV4DebugServiceCall1 call = reinterpret_cast<CuteQV4DebugServiceCall1>(taken[1]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDebugService::stateAboutToBeChanged(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::stateChanged(State a0)
  void stateChanged(QQmlDebugService::State a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQV4DebugServiceCall2 call = reinterpret_cast<CuteQV4DebugServiceCall2>(taken[2]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDebugService::stateChanged(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::messageReceived(const QByteArray &a0)
  void messageReceived(const QByteArray &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQV4DebugServiceCall3 call = reinterpret_cast<CuteQV4DebugServiceCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::messageReceived(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAboutToBeAdded(QJSEngine *engine)
  void engineAboutToBeAdded(QJSEngine *engine) override {
    if (taken[4]) {
      int handled = 0;
      CuteQV4DebugServiceCall4 call = reinterpret_cast<CuteQV4DebugServiceCall4>(taken[4]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAboutToBeAdded(engine);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAboutToBeRemoved(QJSEngine *engine)
  void engineAboutToBeRemoved(QJSEngine *engine) override {
    if (taken[5]) {
      int handled = 0;
      CuteQV4DebugServiceCall5 call = reinterpret_cast<CuteQV4DebugServiceCall5>(taken[5]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAboutToBeRemoved(engine);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAdded(QJSEngine *a0)
  void engineAdded(QJSEngine *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQV4DebugServiceCall6 call = reinterpret_cast<CuteQV4DebugServiceCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAdded(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineRemoved(QJSEngine *a0)
  void engineRemoved(QJSEngine *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQV4DebugServiceCall7 call = reinterpret_cast<CuteQV4DebugServiceCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineRemoved(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQV4DebugServiceCall8 call = reinterpret_cast<CuteQV4DebugServiceCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQV4DebugServiceCall9 call = reinterpret_cast<CuteQV4DebugServiceCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQV4DebugServiceCall10 call = reinterpret_cast<CuteQV4DebugServiceCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQV4DebugServiceCall11 call = reinterpret_cast<CuteQV4DebugServiceCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQV4DebugServiceCall12 call = reinterpret_cast<CuteQV4DebugServiceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQV4DebugServiceCall13 call = reinterpret_cast<CuteQV4DebugServiceCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQV4DebugServiceCall14 call = reinterpret_cast<CuteQV4DebugServiceCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QV4DebugService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QV4DebugService10metaObjectEv(
    const QV4DebugService *self) {
  return self->metaObject();
}

//  QString QV4DebugService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QV4DebugService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QV4DebugService::tr(s, c, n));
}

//  QV4DebugService::~QV4DebugService()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QV4DebugServiceD1Ev(QV4DebugService *self) {
  delete self;
}

//  void QV4DebugService::signalEmitted(const QString &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QV4DebugService13signalEmittedERK7QString(
    QV4DebugService *self,
    const QString *signal) {
  self->signalEmitted(*signal);
}

//  a Python function taken by a CuteQV4DebugService, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4DebugService(
    QV4DebugService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4DebugService *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
