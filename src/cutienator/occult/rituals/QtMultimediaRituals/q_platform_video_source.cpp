//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideosource_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qvideoframeformat.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <optional>

//  A QPlatformVideoSource that Python can take functions over in. Every QPlatformVideoSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformVideoSourceCall0)(const void *, bool, int *);
typedef bool (*CuteQPlatformVideoSourceCall1)(const void *, int *);
typedef const QVideoFrameFormat * (*CuteQPlatformVideoSourceCall2)(const void *, int *);
typedef void (*CuteQPlatformVideoSourceCall3)(const void *, QPlatformMediaCaptureSession *, int *);
typedef QString * (*CuteQPlatformVideoSourceCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformVideoSourceCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformVideoSourceCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSourceCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSourceCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSourceCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSourceCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSourceCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformVideoSource : public QPlatformVideoSource {
public:
  using QPlatformVideoSource::QPlatformVideoSource;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QPlatformVideoSource9setActiveEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformVideoSource8isActiveEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformVideoSource11frameFormatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatformMediaCaptureSession")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformVideoSource11errorStringEv")) {
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

  //  void QPlatformVideoSource::setActive(bool active)
  void setActive(bool active) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformVideoSourceCall0 call = reinterpret_cast<CuteQPlatformVideoSourceCall0>(taken[0]);
      call(this, active, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformVideoSource::isActive() const
  bool isActive() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformVideoSourceCall1 call = reinterpret_cast<CuteQPlatformVideoSourceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QVideoFrameFormat QPlatformVideoSource::frameFormat() const
  QVideoFrameFormat frameFormat() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformVideoSourceCall2 call = reinterpret_cast<CuteQPlatformVideoSourceCall2>(taken[2]);
      const QVideoFrameFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void
  //      QPlatformVideoSource::setCaptureSession(QPlatformMediaCaptureSess
  //      ion *a0)
  void setCaptureSession(QPlatformMediaCaptureSession *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformVideoSourceCall3 call = reinterpret_cast<CuteQPlatformVideoSourceCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSource::setCaptureSession(a0);
  }

  //  QString QPlatformVideoSource::errorString() const
  QString errorString() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformVideoSourceCall4 call = reinterpret_cast<CuteQPlatformVideoSourceCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformVideoSourceCall5 call = reinterpret_cast<CuteQPlatformVideoSourceCall5>(taken[5]);
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
      CuteQPlatformVideoSourceCall6 call = reinterpret_cast<CuteQPlatformVideoSourceCall6>(taken[6]);
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
      CuteQPlatformVideoSourceCall7 call = reinterpret_cast<CuteQPlatformVideoSourceCall7>(taken[7]);
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
      CuteQPlatformVideoSourceCall8 call = reinterpret_cast<CuteQPlatformVideoSourceCall8>(taken[8]);
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
      CuteQPlatformVideoSourceCall9 call = reinterpret_cast<CuteQPlatformVideoSourceCall9>(taken[9]);
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
      CuteQPlatformVideoSourceCall10 call = reinterpret_cast<CuteQPlatformVideoSourceCall10>(taken[10]);
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
      CuteQPlatformVideoSourceCall11 call = reinterpret_cast<CuteQPlatformVideoSourceCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformVideoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QPlatformVideoSource10metaObjectEv(
    const QPlatformVideoSource *self) {
  return self->metaObject();
}

//  void *QPlatformVideoSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QPlatformVideoSource11qt_metacastEPKc(
    QPlatformVideoSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformVideoSource::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QPlatformVideoSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformVideoSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformVideoSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QPlatformVideoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformVideoSource::tr(s, c, n));
}

//  void QPlatformVideoSource::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformVideoSource9setActiveEb(
    QPlatformVideoSource *self,
    bool active) {
  self->setActive(active);
}

//  bool QPlatformVideoSource::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformVideoSource8isActiveEv(
    const QPlatformVideoSource *self) {
  return self->isActive();
}

//  QVideoFrameFormat QPlatformVideoSource::frameFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK20QPlatformVideoSource11frameFormatEv(
    const QPlatformVideoSource *self) {
  return new QVideoFrameFormat(self->frameFormat());
}

//  std::optional<int> QPlatformVideoSource::ffmpegHWPixelFormat() const
extern "C" Q_DECL_EXPORT
std::optional<int> *ritual_ZNK20QPlatformVideoSource19ffmpegHWPixelFormatEv(
    const QPlatformVideoSource *self) {
  return new std::optional<int>(self->ffmpegHWPixelFormat());
}

//  void QPlatformVideoSource::setCaptureSession(QPlatformMediaCaptureSession
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatformMediaCaptureSession(
    QPlatformVideoSource *self,
    QPlatformMediaCaptureSession *a0) {
  self->setCaptureSession(a0);
}

//  QString QPlatformVideoSource::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlatformVideoSource11errorStringEv(
    const QPlatformVideoSource *self) {
  return new QString(self->errorString());
}

//  bool QPlatformVideoSource::hasError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformVideoSource8hasErrorEv(
    const QPlatformVideoSource *self) {
  return self->hasError();
}

//  void QPlatformVideoSource::newVideoFrame(const QVideoFrame &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformVideoSource13newVideoFrameERK11QVideoFrame(
    QPlatformVideoSource *self,
    const QVideoFrame *a0) {
  self->newVideoFrame(*a0);
}

//  void QPlatformVideoSource::activeChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformVideoSource13activeChangedEb(
    QPlatformVideoSource *self,
    bool a0) {
  self->activeChanged(a0);
}

//  void QPlatformVideoSource::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformVideoSource12errorChangedEv(
    QPlatformVideoSource *self) {
  self->errorChanged();
}

//  a Python function taken by a CuteQPlatformVideoSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformVideoSource(
    QPlatformVideoSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformVideoSource *>(self)->take(key, call);
}

//  void QPlatformVideoSource::setCaptureSession(QPlatformMediaCaptureSession
//      *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformVideoSource17setCaptureSessionEP28QPlatformMediaCaptureSession(
    QPlatformVideoSource *self,
    QPlatformMediaCaptureSession *a0) {
  self->QPlatformVideoSource::setCaptureSession(a0);
}

//  a std::optional<int> a ritual of QPlatformVideoSource gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformVideoSource__std_optional_int(
    std::optional<int> *self) {
  delete self;
}
