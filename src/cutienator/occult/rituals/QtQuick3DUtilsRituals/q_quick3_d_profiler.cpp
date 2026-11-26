//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQuick3DUtils/qtquick3dutilsexports.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#if !(!QT_CONFIG(qml_debug))
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQuick3DProfiler that Python can take functions over in. Every QQuick3DProfiler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DProfilerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DProfilerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DProfilerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DProfilerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DProfilerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DProfilerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DProfilerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DProfiler : public QQuick3DProfiler {
public:
  using QQuick3DProfiler::QQuick3DProfiler;
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
      CuteQQuick3DProfilerCall0 call = reinterpret_cast<CuteQQuick3DProfilerCall0>(taken[0]);
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
      CuteQQuick3DProfilerCall1 call = reinterpret_cast<CuteQQuick3DProfilerCall1>(taken[1]);
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
      CuteQQuick3DProfilerCall2 call = reinterpret_cast<CuteQQuick3DProfilerCall2>(taken[2]);
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
      CuteQQuick3DProfilerCall3 call = reinterpret_cast<CuteQQuick3DProfilerCall3>(taken[3]);
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
      CuteQQuick3DProfilerCall4 call = reinterpret_cast<CuteQQuick3DProfilerCall4>(taken[4]);
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
      CuteQQuick3DProfilerCall5 call = reinterpret_cast<CuteQQuick3DProfilerCall5>(taken[5]);
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
      CuteQQuick3DProfilerCall6 call = reinterpret_cast<CuteQQuick3DProfilerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DProfiler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DProfiler10metaObjectEv(
    const QQuick3DProfiler *self) {
  return self->metaObject();
}

//  void *QQuick3DProfiler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuick3DProfiler11qt_metacastEPKc(
    QQuick3DProfiler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DProfiler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DProfiler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DProfiler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DProfiler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DProfiler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DProfiler::tr(s, c, n));
}

//  qint64 QQuick3DProfiler::timestamp()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QQuick3DProfiler9timestampEv(QQuick3DProfiler *self) {
  return self->timestamp();
}

//  void QQuick3DProfiler::initialize(QObject *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler10initializeEP7QObject(QObject *parent) {
  QQuick3DProfiler::initialize(parent);
}

//  QQuick3DProfiler::~QQuick3DProfiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfilerD1Ev(QQuick3DProfiler *self) {
  delete self;
}

//  int QQuick3DProfiler::registerObject(const QObject *object)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DProfiler14registerObjectEPK7QObject(
    const QObject *object) {
  return QQuick3DProfiler::registerObject(object);
}

//  int QQuick3DProfiler::registerString(const QByteArray &string)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DProfiler14registerStringERK10QByteArray(
    const QByteArray *string) {
  return QQuick3DProfiler::registerString(*string);
}

//  void QQuick3DProfiler::dataReady(const QVector<QQuick3DProfilerData>
//      &data, const QHash<int, QByteArray> &eventData)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler9dataReadyERK5QListI20QQuick3DProfilerDataERK5QHashIi10QByteArrayE(
    QQuick3DProfiler *self,
    const QVector<QQuick3DProfilerData> *data,
    const QHash<int, QByteArray> *eventData) {
  self->dataReady(*data, *eventData);
}

//  QQuick3DProfiler::QQuick3DProfiler(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DProfiler *ritual_ZN16QQuick3DProfilerC1EP7QObject(QObject *parent) {
  return new CuteQQuick3DProfiler(parent);
}

//  void QQuick3DProfiler::processMessage(const QQuick3DProfilerData
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler14processMessageERK20QQuick3DProfilerData(
    QQuick3DProfiler *self,
    const QQuick3DProfilerData *message) {
  self->processMessage(*message);
}

//  void QQuick3DProfiler::startProfilingImpl(quint64 features)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler18startProfilingImplEy(
    QQuick3DProfiler *self,
    quint64 features) {
  self->startProfilingImpl(features);
}

//  void QQuick3DProfiler::stopProfilingImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler17stopProfilingImplEv(
    QQuick3DProfiler *self) {
  self->stopProfilingImpl();
}

//  void QQuick3DProfiler::reportDataImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler14reportDataImplEv(QQuick3DProfiler *self) {
  self->reportDataImpl();
}

//  void QQuick3DProfiler::setTimer(const QElapsedTimer &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DProfiler8setTimerERK13QElapsedTimer(
    QQuick3DProfiler *self,
    const QElapsedTimer *t) {
  self->setTimer(*t);
}

//  QQuick3DProfiler as the QQmlProfilerDefinitions it is built on
extern "C" Q_DECL_EXPORT
QQmlProfilerDefinitions *ritual_cast_QQuick3DProfiler_QQmlProfilerDefinitions(
    QQuick3DProfiler *self) {
  return static_cast<QQmlProfilerDefinitions *>(self);
}

//  a Python function taken by a CuteQQuick3DProfiler, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DProfiler(
    QQuick3DProfiler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DProfiler *>(self)->take(key, call);
}

#endif  // !(!QT_CONFIG(qml_debug))
