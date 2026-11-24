//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlProfiler that Python can take functions over in. Every QQmlProfiler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlProfilerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlProfilerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlProfilerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlProfilerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlProfilerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlProfilerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlProfilerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlProfiler : public QQmlProfiler {
public:
  using QQmlProfiler::QQmlProfiler;
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
      CuteQQmlProfilerCall0 call = reinterpret_cast<CuteQQmlProfilerCall0>(taken[0]);
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
      CuteQQmlProfilerCall1 call = reinterpret_cast<CuteQQmlProfilerCall1>(taken[1]);
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
      CuteQQmlProfilerCall2 call = reinterpret_cast<CuteQQmlProfilerCall2>(taken[2]);
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
      CuteQQmlProfilerCall3 call = reinterpret_cast<CuteQQmlProfilerCall3>(taken[3]);
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
      CuteQQmlProfilerCall4 call = reinterpret_cast<CuteQQmlProfilerCall4>(taken[4]);
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
      CuteQQmlProfilerCall5 call = reinterpret_cast<CuteQQmlProfilerCall5>(taken[5]);
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
      CuteQQmlProfilerCall6 call = reinterpret_cast<CuteQQmlProfilerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlProfiler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQmlProfiler10metaObjectEv(
    const QQmlProfiler *self) {
  return self->metaObject();
}

//  QString QQmlProfiler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQmlProfiler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlProfiler::tr(s, c, n));
}

//  void QQmlProfiler::startBinding(QV4::Function *function)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler12startBindingEPN3QV48FunctionE(
    QQmlProfiler *self,
    QV4::Function *function) {
  self->startBinding(function);
}

//  void QQmlProfiler::startCompiling(QQmlDataBlob *blob)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler14startCompilingEP12QQmlDataBlob(
    QQmlProfiler *self,
    QQmlDataBlob *blob) {
  self->startCompiling(blob);
}

//  void QQmlProfiler::startHandlingSignal(QQmlBoundSignalExpression
//      *expression)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler19startHandlingSignalEP25QQmlBoundSignalExpression(
    QQmlProfiler *self,
    QQmlBoundSignalExpression *expression) {
  self->startHandlingSignal(expression);
}

//  void QQmlProfiler::startCreating(const QV4::CompiledData::Object *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler13startCreatingEPKN3QV412CompiledData6ObjectE(
    QQmlProfiler *self,
    const QV4::CompiledData::Object *obj) {
  self->startCreating(obj);
}

//  void QQmlProfiler::updateCreating(const QV4::CompiledData::Object *obj,
//      QV4::ExecutableCompilationUnit *ref, const QUrl &url, const QString
//      &type)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler14updateCreatingEPKN3QV412CompiledData6ObjectEPNS0_25ExecutableCompilationUnitERK4QUrlRK7QString(
    QQmlProfiler *self,
    const QV4::CompiledData::Object *obj,
    QV4::ExecutableCompilationUnit *ref,
    const QUrl *url,
    const QString *type) {
  self->updateCreating(obj, ref, *url, *type);
}

//  QQmlProfiler::QQmlProfiler()
extern "C" Q_DECL_EXPORT
QQmlProfiler *ritual_ZN12QQmlProfilerC1Ev() {
  return new CuteQQmlProfiler();
}

//  void QQmlProfiler::startProfiling(quint64 features)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler14startProfilingEy(
    QQmlProfiler *self,
    quint64 features) {
  self->startProfiling(features);
}

//  void QQmlProfiler::stopProfiling()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler13stopProfilingEv(QQmlProfiler *self) {
  self->stopProfiling();
}

//  void QQmlProfiler::reportData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler10reportDataEv(QQmlProfiler *self) {
  self->reportData();
}

//  void QQmlProfiler::setTimer(const QElapsedTimer &timer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlProfiler8setTimerERK13QElapsedTimer(
    QQmlProfiler *self,
    const QElapsedTimer *timer) {
  self->setTimer(*timer);
}

//  QQmlProfiler as the QQmlProfilerDefinitions it is built on
extern "C" Q_DECL_EXPORT
QQmlProfilerDefinitions *ritual_cast_QQmlProfiler_QQmlProfilerDefinitions(
    QQmlProfiler *self) {
  return static_cast<QQmlProfilerDefinitions *>(self);
}

//  a Python function taken by a CuteQQmlProfiler, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlProfiler(
    QQmlProfiler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlProfiler *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
