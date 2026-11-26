//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qpipewire_screencapture_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if (QT_CONFIG(pipewire)) && (QT_CONFIG(pipewire_screencapture))
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qpipewire_screencapture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <memory>

//  Only a class built on QtPipeWire::QPipeWireCapture may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtPipeWire_QPipeWireCapture : QtPipeWire::QPipeWireCapture {
  using QtPipeWire::QPipeWireCapture::setActiveInternal;
};

//  A QtPipeWire::QPipeWireCapture that Python can take functions over in. Every QtPipeWire::QPipeWireCapture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVideoFrameFormat * (*CuteQtPipeWire_QPipeWireCaptureCall0)(const void *, int *);
typedef bool (*CuteQtPipeWire_QPipeWireCaptureCall1)(const void *, bool, int *);
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall2)(const void *, bool, int *);
typedef bool (*CuteQtPipeWire_QPipeWireCaptureCall3)(const void *, int *);
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall4)(const void *, QPlatformMediaCaptureSession *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPipeWire_QPipeWireCaptureCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtPipeWire_QPipeWireCaptureCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtPipeWire_QPipeWireCaptureCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtPipeWire_QPipeWireCapture : public QtPipeWire::QPipeWireCapture {
public:
  using QtPipeWire::QPipeWireCapture::QPipeWireCapture;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QPlatformVideoSource11frameFormatEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QPlatformSurfaceCapture17setActiveInternalEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformVideoSource9setActiveEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformVideoSource8isActiveEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatformMediaCaptureSession")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVideoFrameFormat QtPipeWire::QPipeWireCapture::frameFormat() const
  QVideoFrameFormat frameFormat() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall0 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall0>(taken[0]);
      const QVideoFrameFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QtPipeWire::QPipeWireCapture::frameFormat();
  }

  //  bool QtPipeWire::QPipeWireCapture::setActiveInternal(bool active)
  bool setActiveInternal(bool active) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall1 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall1>(taken[1]);
      bool given = call(this, active, &handled);
      if (handled) return given;
    }
    return QtPipeWire::QPipeWireCapture::setActiveInternal(active);
  }

  //  void QPlatformSurfaceCapture::setActive(bool active)
  void setActive(bool active) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall2 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall2>(taken[2]);
      call(this, active, &handled);
      if (handled) return;
    }
    QPlatformSurfaceCapture::setActive(active);
  }

  //  bool QPlatformSurfaceCapture::isActive() const
  bool isActive() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall3 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformSurfaceCapture::isActive();
  }

  //  void
  //      QPlatformVideoSource::setCaptureSession(QPlatformMediaCaptureSess
  //      ion *a0)
  void setCaptureSession(QPlatformMediaCaptureSession *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall4 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSource::setCaptureSession(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall5 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall6 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall7 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall8 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall9 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall10 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQtPipeWire_QPipeWireCaptureCall11 call = reinterpret_cast<CuteQtPipeWire_QPipeWireCaptureCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtPipeWire::QPipeWireCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QtPipeWire16QPipeWireCapture10metaObjectEv(
    const QtPipeWire::QPipeWireCapture *self) {
  return self->metaObject();
}

//  void *QtPipeWire::QPipeWireCapture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QtPipeWire16QPipeWireCapture11qt_metacastEPKc(
    QtPipeWire::QPipeWireCapture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtPipeWire::QPipeWireCapture::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QtPipeWire16QPipeWireCapture11qt_metacallEN11QMetaObject4CallEiPPv(
    QtPipeWire::QPipeWireCapture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtPipeWire::QPipeWireCapture::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QtPipeWire16QPipeWireCapture2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtPipeWire::QPipeWireCapture::tr(s, c, n));
}

//  QtPipeWire::QPipeWireCapture::~QPipeWireCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtPipeWire16QPipeWireCaptureD1Ev(
    QtPipeWire::QPipeWireCapture *self) {
  delete self;
}

//  QVideoFrameFormat QtPipeWire::QPipeWireCapture::frameFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK10QtPipeWire16QPipeWireCapture11frameFormatEv(
    const QtPipeWire::QPipeWireCapture *self) {
  return new QVideoFrameFormat(self->frameFormat());
}

//  std::unique_ptr<QPipeWireCapture>
//      QtPipeWire::QPipeWireCapture::create(Source initialSource)
extern "C" Q_DECL_EXPORT
std::unique_ptr<QtPipeWire::QPipeWireCapture> *ritual_ZN10QtPipeWire16QPipeWireCapture6createESt7variantIJ8QPointerI7QScreenE17QCapturableWindowEE(
    const QPlatformSurfaceCapture::Source *initialSource) {
  return new std::unique_ptr<QtPipeWire::QPipeWireCapture>(
      QtPipeWire::QPipeWireCapture::create(
          *initialSource));
}

//  bool QtPipeWire::QPipeWireCapture::setActiveInternal(bool active)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QtPipeWire16QPipeWireCapture17setActiveInternalEb(
    QtPipeWire::QPipeWireCapture *self,
    bool active) {
  return self->setActiveInternal(active);
}

//  a Python function taken by a CuteQtPipeWire_QPipeWireCapture, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtPipeWire_QPipeWireCapture(
    QtPipeWire::QPipeWireCapture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtPipeWire_QPipeWireCapture *>(self)->take(key, call);
}

//  QVideoFrameFormat QtPipeWire::QPipeWireCapture::frameFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_own_ZNK10QtPipeWire16QPipeWireCapture11frameFormatEv(
    const QtPipeWire::QPipeWireCapture *self) {
  return new QVideoFrameFormat(
      self->QtPipeWire::QPipeWireCapture::frameFormat());
}

//  bool QtPipeWire::QPipeWireCapture::setActiveInternal(bool active)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QtPipeWire16QPipeWireCapture17setActiveInternalEb(
    QtPipeWire::QPipeWireCapture *self,
    bool active) {
  return static_cast<OwnQtPipeWire_QPipeWireCapture *>(self)->OwnQtPipeWire_QPipeWireCapture::setActiveInternal(
      active);
}

//  a std::unique_ptr<QtPipeWire::QPipeWireCapture> a ritual of
//      QtPipeWire::QPipeWireCapture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtPipeWire_QPipeWireCapture__std_unique_ptr_QtPipeWire_QPipeWireCapture(
    std::unique_ptr<QtPipeWire::QPipeWireCapture> *self) {
  delete self;
}

#endif  // (QT_CONFIG(pipewire)) && (QT_CONFIG(pipewire_screencapture))
