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

//  A QQmlInspectorService that Python can take functions over in. Every QQmlInspectorService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlInspectorServiceCall0)(const void *, QQuickWindow *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlInspectorServiceCall1)(const void *, QQuickWindow *, QWindow *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
typedef void (*CuteQQmlInspectorServiceCall2)(const void *, QQuickWindow *, int *);
#endif  // !(!QT_CONFIG(qml_debug))
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall3)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall4)(const void *, int, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall5)(const void *, const QByteArray *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall6)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall7)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall8)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
typedef void (*CuteQQmlInspectorServiceCall9)(const void *, QJSEngine *, int *);
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlInspectorServiceCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlInspectorServiceCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInspectorServiceCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInspectorServiceCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInspectorServiceCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInspectorServiceCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlInspectorServiceCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlInspectorService : public QQmlInspectorService {
public:
  using QQmlInspectorService::QQmlInspectorService;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN20QQmlInspectorService9addWindowEP12QQuickWindow")) {
      taken[0] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN20QQmlInspectorService15setParentWindowEP12QQuickWindowP7QWindow")) {
      taken[1] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if !(!QT_CONFIG(qml_debug))
    if (!std::strcmp(key, "_ZN20QQmlInspectorService12removeWindowEP12QQuickWindow")) {
      taken[2] = call;
      return true;
    }
#endif  // !(!QT_CONFIG(qml_debug))
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService21stateAboutToBeChangedENS_5StateE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService12stateChangedENS_5StateE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService15messageReceivedERK10QByteArray")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService20engineAboutToBeAddedEP9QJSEngine")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService22engineAboutToBeRemovedEP9QJSEngine")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService11engineAddedEP9QJSEngine")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
    if (!std::strcmp(key, "_ZN16QQmlDebugService13engineRemovedEP9QJSEngine")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_debug)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlInspectorService::addWindow(QQuickWindow *a0)
  void addWindow(QQuickWindow *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall0 call = reinterpret_cast<CuteQQmlInspectorServiceCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlInspectorService::setParentWindow(QQuickWindow *a0, QWindow
  //      *a1)
  void setParentWindow(QQuickWindow *a0, QWindow *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall1 call = reinterpret_cast<CuteQQmlInspectorServiceCall1>(taken[1]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if !(!QT_CONFIG(qml_debug))
  //  void QQmlInspectorService::removeWindow(QQuickWindow *a0)
  void removeWindow(QQuickWindow *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall2 call = reinterpret_cast<CuteQQmlInspectorServiceCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
#endif  // !(!QT_CONFIG(qml_debug))

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::stateAboutToBeChanged(State a0)
  void stateAboutToBeChanged(QQmlDebugService::State a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall3 call = reinterpret_cast<CuteQQmlInspectorServiceCall3>(taken[3]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDebugService::stateAboutToBeChanged(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::stateChanged(State a0)
  void stateChanged(QQmlDebugService::State a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall4 call = reinterpret_cast<CuteQQmlInspectorServiceCall4>(taken[4]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlDebugService::stateChanged(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::messageReceived(const QByteArray &a0)
  void messageReceived(const QByteArray &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall5 call = reinterpret_cast<CuteQQmlInspectorServiceCall5>(taken[5]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::messageReceived(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAboutToBeAdded(QJSEngine *engine)
  void engineAboutToBeAdded(QJSEngine *engine) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall6 call = reinterpret_cast<CuteQQmlInspectorServiceCall6>(taken[6]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAboutToBeAdded(engine);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAboutToBeRemoved(QJSEngine *engine)
  void engineAboutToBeRemoved(QJSEngine *engine) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall7 call = reinterpret_cast<CuteQQmlInspectorServiceCall7>(taken[7]);
      call(this, engine, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAboutToBeRemoved(engine);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineAdded(QJSEngine *a0)
  void engineAdded(QJSEngine *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall8 call = reinterpret_cast<CuteQQmlInspectorServiceCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineAdded(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if QT_CONFIG(qml_debug)
  //  void QQmlDebugService::engineRemoved(QJSEngine *a0)
  void engineRemoved(QJSEngine *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall9 call = reinterpret_cast<CuteQQmlInspectorServiceCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlDebugService::engineRemoved(a0);
  }
#endif  // QT_CONFIG(qml_debug)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall10 call = reinterpret_cast<CuteQQmlInspectorServiceCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall11 call = reinterpret_cast<CuteQQmlInspectorServiceCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall12 call = reinterpret_cast<CuteQQmlInspectorServiceCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall13 call = reinterpret_cast<CuteQQmlInspectorServiceCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall14 call = reinterpret_cast<CuteQQmlInspectorServiceCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall15 call = reinterpret_cast<CuteQQmlInspectorServiceCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlInspectorServiceCall16 call = reinterpret_cast<CuteQQmlInspectorServiceCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlInspectorService::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQmlInspectorService10metaObjectEv(
    const QQmlInspectorService *self) {
  return self->metaObject();
}

//  QString QQmlInspectorService::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQmlInspectorService2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlInspectorService::tr(s, c, n));
}

//  QQmlInspectorService::~QQmlInspectorService()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlInspectorServiceD1Ev(QQmlInspectorService *self) {
  delete self;
}

//  void QQmlInspectorService::addWindow(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlInspectorService9addWindowEP12QQuickWindow(
    QQmlInspectorService *self,
    QQuickWindow *a0) {
  self->addWindow(a0);
}

//  void QQmlInspectorService::setParentWindow(QQuickWindow *a0, QWindow *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlInspectorService15setParentWindowEP12QQuickWindowP7QWindow(
    QQmlInspectorService *self,
    QQuickWindow *a0,
    QWindow *a1) {
  self->setParentWindow(a0, a1);
}

//  void QQmlInspectorService::removeWindow(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlInspectorService12removeWindowEP12QQuickWindow(
    QQmlInspectorService *self,
    QQuickWindow *a0) {
  self->removeWindow(a0);
}

//  a Python function taken by a CuteQQmlInspectorService, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlInspectorService(
    QQmlInspectorService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlInspectorService *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
