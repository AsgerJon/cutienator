//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlabstractprofileradapter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_debug)
#if QT_CONFIG(qml_debug)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlabstractprofileradapter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlAbstractProfilerAdapter that Python can take functions over in. Every QQmlAbstractProfilerAdapter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractProfilerAdapterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAbstractProfilerAdapterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAbstractProfilerAdapterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlAbstractProfilerAdapter : public QQmlAbstractProfilerAdapter {
public:
  using QQmlAbstractProfilerAdapter::QQmlAbstractProfilerAdapter;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall0 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall1 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall2 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall3 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall4 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall5 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlAbstractProfilerAdapterCall6 call = reinterpret_cast<CuteQQmlAbstractProfilerAdapterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlAbstractProfilerAdapter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQmlAbstractProfilerAdapter10metaObjectEv(
    const QQmlAbstractProfilerAdapter *self) {
  return self->metaObject();
}

//  QString QQmlAbstractProfilerAdapter::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QQmlAbstractProfilerAdapter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAbstractProfilerAdapter::tr(s, c, n));
}

//  QQmlAbstractProfilerAdapter::~QQmlAbstractProfilerAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapterD1Ev(
    QQmlAbstractProfilerAdapter *self) {
  delete self;
}

//  void QQmlAbstractProfilerAdapter::setService(QQmlProfilerService
//      *new_service)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter10setServiceEP19QQmlProfilerService(
    QQmlAbstractProfilerAdapter *self,
    QQmlProfilerService *new_service) {
  self->setService(new_service);
}

//  void QQmlAbstractProfilerAdapter::startProfiling(quint64 features)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter14startProfilingEy(
    QQmlAbstractProfilerAdapter *self,
    quint64 features) {
  self->startProfiling(features);
}

//  void QQmlAbstractProfilerAdapter::stopProfiling()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter13stopProfilingEv(
    QQmlAbstractProfilerAdapter *self) {
  self->stopProfiling();
}

//  void QQmlAbstractProfilerAdapter::reportData()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter10reportDataEv(
    QQmlAbstractProfilerAdapter *self) {
  self->reportData();
}

//  void QQmlAbstractProfilerAdapter::stopWaiting()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter11stopWaitingEv(
    QQmlAbstractProfilerAdapter *self) {
  self->stopWaiting();
}

//  void QQmlAbstractProfilerAdapter::startWaiting()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter12startWaitingEv(
    QQmlAbstractProfilerAdapter *self) {
  self->startWaiting();
}

//  bool QQmlAbstractProfilerAdapter::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQmlAbstractProfilerAdapter9isRunningEv(
    const QQmlAbstractProfilerAdapter *self) {
  return self->isRunning();
}

//  quint64 QQmlAbstractProfilerAdapter::features() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK27QQmlAbstractProfilerAdapter8featuresEv(
    const QQmlAbstractProfilerAdapter *self) {
  return self->features();
}

//  void QQmlAbstractProfilerAdapter::synchronize(const QElapsedTimer &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlAbstractProfilerAdapter11synchronizeERK13QElapsedTimer(
    QQmlAbstractProfilerAdapter *self,
    const QElapsedTimer *t) {
  self->synchronize(*t);
}

//  QQmlAbstractProfilerAdapter as the QQmlProfilerDefinitions it is built on
extern "C" Q_DECL_EXPORT
QQmlProfilerDefinitions *ritual_cast_QQmlAbstractProfilerAdapter_QQmlProfilerDefinitions(
    QQmlAbstractProfilerAdapter *self) {
  return static_cast<QQmlProfilerDefinitions *>(self);
}

//  a Python function taken by a CuteQQmlAbstractProfilerAdapter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractProfilerAdapter(
    QQmlAbstractProfilerAdapter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractProfilerAdapter *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_debug)
#endif  // QT_CONFIG(qml_debug)
