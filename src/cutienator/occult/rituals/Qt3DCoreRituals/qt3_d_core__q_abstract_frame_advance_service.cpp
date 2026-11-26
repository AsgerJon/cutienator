//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractframeadvanceservice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractframeadvanceservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DCore::QAbstractFrameAdvanceService that Python can take functions over in. Every Qt3DCore::QAbstractFrameAdvanceService
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall1)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QAbstractFrameAdvanceServiceCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QAbstractFrameAdvanceService : public Qt3DCore::QAbstractFrameAdvanceService {
public:
  using Qt3DCore::QAbstractFrameAdvanceService::QAbstractFrameAdvanceService;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore28QAbstractFrameAdvanceService16waitForNextFrameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore28QAbstractFrameAdvanceService5startEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore28QAbstractFrameAdvanceService4stopEv")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  qint64 Qt3DCore::QAbstractFrameAdvanceService::waitForNextFrame()
  qint64 waitForNextFrame() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DCore::QAbstractFrameAdvanceService::start()
  void start() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall1 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DCore::QAbstractFrameAdvanceService::stop()
  void stop() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall2 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall3 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall4 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall5 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall6 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall7 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall8 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFrameAdvanceServiceCall9 call = reinterpret_cast<CuteQt3DCore_QAbstractFrameAdvanceServiceCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QAbstractFrameAdvanceService::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore28QAbstractFrameAdvanceService10metaObjectEv(
    const Qt3DCore::QAbstractFrameAdvanceService *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QAbstractFrameAdvanceService::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService11qt_metacastEPKc(
    Qt3DCore::QAbstractFrameAdvanceService *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QAbstractFrameAdvanceService::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QAbstractFrameAdvanceService *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::QAbstractFrameAdvanceService::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::QAbstractFrameAdvanceService::tr(s, c, n));
}

//  qint64 Qt3DCore::QAbstractFrameAdvanceService::waitForNextFrame()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService16waitForNextFrameEv(
    Qt3DCore::QAbstractFrameAdvanceService *self) {
  return self->waitForNextFrame();
}

//  void Qt3DCore::QAbstractFrameAdvanceService::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService5startEv(
    Qt3DCore::QAbstractFrameAdvanceService *self) {
  self->start();
}

//  void Qt3DCore::QAbstractFrameAdvanceService::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore28QAbstractFrameAdvanceService4stopEv(
    Qt3DCore::QAbstractFrameAdvanceService *self) {
  self->stop();
}

//  Qt3DCore::QAbstractFrameAdvanceService::QAbstractFrameAdvanceService(cons
//      t QString &description)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrameAdvanceService *ritual_ZN8Qt3DCore28QAbstractFrameAdvanceServiceC1ERK7QString(
    const QString *description) {
  return new CuteQt3DCore_QAbstractFrameAdvanceService(*description);
}

//  Qt3DCore::QAbstractFrameAdvanceService::QAbstractFrameAdvanceService(QAbs
//      tractFrameAdvanceServicePrivate &dd)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrameAdvanceService *ritual_ZN8Qt3DCore28QAbstractFrameAdvanceServiceC1ERNS_35QAbstractFrameAdvanceServicePrivateE(
    Qt3DCore::QAbstractFrameAdvanceServicePrivate *dd) {
  return new CuteQt3DCore_QAbstractFrameAdvanceService(*dd);
}

//  a Python function taken by a CuteQt3DCore_QAbstractFrameAdvanceService,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractFrameAdvanceService(
    Qt3DCore::QAbstractFrameAdvanceService *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractFrameAdvanceService *>(self)->take(key, call);
}
