//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsurfacecapturegrabber_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsurfacecapturegrabber_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSurfaceCaptureGrabber may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSurfaceCaptureGrabber : QSurfaceCaptureGrabber {
  using QSurfaceCaptureGrabber::initializeGrabbingContext;
  using QSurfaceCaptureGrabber::finalizeGrabbingContext;
};

//  A QSurfaceCaptureGrabber that Python can take functions over in. Every QSurfaceCaptureGrabber
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVideoFrame * (*CuteQSurfaceCaptureGrabberCall0)(const void *, int *);
typedef void (*CuteQSurfaceCaptureGrabberCall1)(const void *, int *);
typedef void (*CuteQSurfaceCaptureGrabberCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceCaptureGrabberCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSurfaceCaptureGrabberCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceCaptureGrabberCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceCaptureGrabberCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceCaptureGrabberCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceCaptureGrabberCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSurfaceCaptureGrabberCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSurfaceCaptureGrabber : public QSurfaceCaptureGrabber {
public:
  using QSurfaceCaptureGrabber::QSurfaceCaptureGrabber;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QSurfaceCaptureGrabber9grabFrameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSurfaceCaptureGrabber25initializeGrabbingContextEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QSurfaceCaptureGrabber23finalizeGrabbingContextEv")) {
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

  //  QVideoFrame QSurfaceCaptureGrabber::grabFrame()
  QVideoFrame grabFrame() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSurfaceCaptureGrabberCall0 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall0>(taken[0]);
      const QVideoFrame * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSurfaceCaptureGrabber::initializeGrabbingContext()
  void initializeGrabbingContext() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSurfaceCaptureGrabberCall1 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSurfaceCaptureGrabber::initializeGrabbingContext();
  }

  //  void QSurfaceCaptureGrabber::finalizeGrabbingContext()
  void finalizeGrabbingContext() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSurfaceCaptureGrabberCall2 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSurfaceCaptureGrabber::finalizeGrabbingContext();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSurfaceCaptureGrabberCall3 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall3>(taken[3]);
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
      CuteQSurfaceCaptureGrabberCall4 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall4>(taken[4]);
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
      CuteQSurfaceCaptureGrabberCall5 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall5>(taken[5]);
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
      CuteQSurfaceCaptureGrabberCall6 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall6>(taken[6]);
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
      CuteQSurfaceCaptureGrabberCall7 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall7>(taken[7]);
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
      CuteQSurfaceCaptureGrabberCall8 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall8>(taken[8]);
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
      CuteQSurfaceCaptureGrabberCall9 call = reinterpret_cast<CuteQSurfaceCaptureGrabberCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSurfaceCaptureGrabber::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QSurfaceCaptureGrabber10metaObjectEv(
    const QSurfaceCaptureGrabber *self) {
  return self->metaObject();
}

//  QString QSurfaceCaptureGrabber::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QSurfaceCaptureGrabber2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSurfaceCaptureGrabber::tr(s, c, n));
}

//  QSurfaceCaptureGrabber::~QSurfaceCaptureGrabber()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabberD1Ev(QSurfaceCaptureGrabber *self) {
  delete self;
}

//  void QSurfaceCaptureGrabber::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber5startEv(
    QSurfaceCaptureGrabber *self) {
  self->start();
}

//  void QSurfaceCaptureGrabber::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber4stopEv(QSurfaceCaptureGrabber *self) {
  self->stop();
}

//  qreal QSurfaceCaptureGrabber::frameRate() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QSurfaceCaptureGrabber9frameRateEv(
    const QSurfaceCaptureGrabber *self) {
  return self->frameRate();
}

//  void QSurfaceCaptureGrabber::updateError(QPlatformSurfaceCapture::Error
//      error, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber11updateErrorEN23QPlatformSurfaceCapture5ErrorERK7QString(
    QSurfaceCaptureGrabber *self,
    QPlatformSurfaceCapture::Error error,
    const QString *description) {
  self->updateError(error, *description);
}

//  QVideoFrame QSurfaceCaptureGrabber::grabFrame()
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN22QSurfaceCaptureGrabber9grabFrameEv(
    QSurfaceCaptureGrabber *self) {
  return new QVideoFrame(self->grabFrame());
}

//  void QSurfaceCaptureGrabber::updateTimerInterval()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber19updateTimerIntervalEv(
    QSurfaceCaptureGrabber *self) {
  self->updateTimerInterval();
}

//  void QSurfaceCaptureGrabber::initializeGrabbingContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber25initializeGrabbingContextEv(
    QSurfaceCaptureGrabber *self) {
  self->initializeGrabbingContext();
}

//  void QSurfaceCaptureGrabber::finalizeGrabbingContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber23finalizeGrabbingContextEv(
    QSurfaceCaptureGrabber *self) {
  self->finalizeGrabbingContext();
}

//  bool QSurfaceCaptureGrabber::isGrabbingContextInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSurfaceCaptureGrabber28isGrabbingContextInitializedEv(
    const QSurfaceCaptureGrabber *self) {
  return self->isGrabbingContextInitialized();
}

//  void QSurfaceCaptureGrabber::injectContextToGrabbingThread(QObject
//      *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSurfaceCaptureGrabber29injectContextToGrabbingThreadEP7QObject(
    QSurfaceCaptureGrabber *self,
    QObject *context) {
  self->injectContextToGrabbingThread(context);
}

//  a Python function taken by a CuteQSurfaceCaptureGrabber, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurfaceCaptureGrabber(
    QSurfaceCaptureGrabber *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurfaceCaptureGrabber *>(self)->take(key, call);
}

//  void QSurfaceCaptureGrabber::initializeGrabbingContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSurfaceCaptureGrabber25initializeGrabbingContextEv(
    QSurfaceCaptureGrabber *self) {
  static_cast<OwnQSurfaceCaptureGrabber *>(self)->OwnQSurfaceCaptureGrabber::initializeGrabbingContext();
}

//  void QSurfaceCaptureGrabber::finalizeGrabbingContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QSurfaceCaptureGrabber23finalizeGrabbingContextEv(
    QSurfaceCaptureGrabber *self) {
  static_cast<OwnQSurfaceCaptureGrabber *>(self)->OwnQSurfaceCaptureGrabber::finalizeGrabbingContext();
}
