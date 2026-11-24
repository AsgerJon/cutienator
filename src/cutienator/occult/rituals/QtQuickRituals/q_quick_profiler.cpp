//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickProfiler that Python can take functions over in. Every QQuickProfiler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickProfilerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickProfilerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickProfilerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickProfiler : public QQuickProfiler {
public:
  using QQuickProfiler::QQuickProfiler;
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
      CuteQQuickProfilerCall0 call = reinterpret_cast<CuteQQuickProfilerCall0>(taken[0]);
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
      CuteQQuickProfilerCall1 call = reinterpret_cast<CuteQQuickProfilerCall1>(taken[1]);
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
      CuteQQuickProfilerCall2 call = reinterpret_cast<CuteQQuickProfilerCall2>(taken[2]);
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
      CuteQQuickProfilerCall3 call = reinterpret_cast<CuteQQuickProfilerCall3>(taken[3]);
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
      CuteQQuickProfilerCall4 call = reinterpret_cast<CuteQQuickProfilerCall4>(taken[4]);
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
      CuteQQuickProfilerCall5 call = reinterpret_cast<CuteQQuickProfilerCall5>(taken[5]);
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
      CuteQQuickProfilerCall6 call = reinterpret_cast<CuteQQuickProfilerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickProfiler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickProfiler10metaObjectEv(
    const QQuickProfiler *self) {
  return self->metaObject();
}

//  QString QQuickProfiler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickProfiler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickProfiler::tr(s, c, n));
}

//  void QQuickProfiler::animationFrame(qint64 delta, AnimationThread
//      threadId)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler14animationFrameExNS_15AnimationThreadE(
    qint64 delta,
    QQuickProfiler::AnimationThread threadId) {
  QQuickProfiler::animationFrame(delta, threadId);
}

//  void QQuickProfiler::pixmapLoadingFinished(const QUrl &url, const QSize
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler21pixmapLoadingFinishedERK4QUrlRK5QSize(
    const QUrl *url,
    const QSize *size) {
  QQuickProfiler::pixmapLoadingFinished(*url, *size);
}

//  void QQuickProfiler::registerAnimationCallback()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler25registerAnimationCallbackEv() {
  QQuickProfiler::registerAnimationCallback();
}

//  qint64 QQuickProfiler::timestamp()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN14QQuickProfiler9timestampEv(QQuickProfiler *self) {
  return self->timestamp();
}

//  void QQuickProfiler::initialize(QObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler10initializeEP7QObject(QObject *parent) {
  QQuickProfiler::initialize(parent);
}

//  QQuickProfiler::~QQuickProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfilerD1Ev(QQuickProfiler *self) {
  delete self;
}

//  QQuickProfiler::QQuickProfiler(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickProfiler *ritual_ZN14QQuickProfilerC1EP7QObject(QObject *parent) {
  return new CuteQQuickProfiler(parent);
}

//  void QQuickProfiler::processMessage(const QQuickProfilerData &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler14processMessageERK18QQuickProfilerData(
    QQuickProfiler *self,
    const QQuickProfilerData *message) {
  self->processMessage(*message);
}

//  void QQuickProfiler::startProfilingImpl(quint64 features)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler18startProfilingImplEy(
    QQuickProfiler *self,
    quint64 features) {
  self->startProfilingImpl(features);
}

//  void QQuickProfiler::stopProfilingImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler17stopProfilingImplEv(QQuickProfiler *self) {
  self->stopProfilingImpl();
}

//  void QQuickProfiler::reportDataImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler14reportDataImplEv(QQuickProfiler *self) {
  self->reportDataImpl();
}

//  void QQuickProfiler::setTimer(const QElapsedTimer &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickProfiler8setTimerERK13QElapsedTimer(
    QQuickProfiler *self,
    const QElapsedTimer *t) {
  self->setTimer(*t);
}

//  QQuickProfiler as the QQmlProfilerDefinitions it is built on
extern "C" Q_DECL_EXPORT
QQmlProfilerDefinitions *ritual_cast_QQuickProfiler_QQmlProfilerDefinitions(
    QQuickProfiler *self) {
  return static_cast<QQmlProfilerDefinitions *>(self);
}

//  a Python function taken by a CuteQQuickProfiler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickProfiler(
    QQuickProfiler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickProfiler *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
