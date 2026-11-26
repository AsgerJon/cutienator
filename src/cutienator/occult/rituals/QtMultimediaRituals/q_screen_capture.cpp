//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qscreencapture.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qscreencapture.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <optional>

//  A QScreenCapture that Python can take functions over in. Every QScreenCapture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScreenCaptureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScreenCaptureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCaptureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCaptureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCaptureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCaptureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScreenCaptureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScreenCapture : public QScreenCapture {
public:
  using QScreenCapture::QScreenCapture;
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
      CuteQScreenCaptureCall0 call = reinterpret_cast<CuteQScreenCaptureCall0>(taken[0]);
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
      CuteQScreenCaptureCall1 call = reinterpret_cast<CuteQScreenCaptureCall1>(taken[1]);
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
      CuteQScreenCaptureCall2 call = reinterpret_cast<CuteQScreenCaptureCall2>(taken[2]);
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
      CuteQScreenCaptureCall3 call = reinterpret_cast<CuteQScreenCaptureCall3>(taken[3]);
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
      CuteQScreenCaptureCall4 call = reinterpret_cast<CuteQScreenCaptureCall4>(taken[4]);
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
      CuteQScreenCaptureCall5 call = reinterpret_cast<CuteQScreenCaptureCall5>(taken[5]);
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
      CuteQScreenCaptureCall6 call = reinterpret_cast<CuteQScreenCaptureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScreenCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScreenCapture10metaObjectEv(
    const QScreenCapture *self) {
  return self->metaObject();
}

//  void *QScreenCapture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QScreenCapture11qt_metacastEPKc(
    QScreenCapture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScreenCapture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QScreenCapture11qt_metacallEN11QMetaObject4CallEiPPv(
    QScreenCapture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScreenCapture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QScreenCapture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScreenCapture::tr(s, c, n));
}

//  QScreenCapture::QScreenCapture(QObject *parent)
extern "C" Q_DECL_EXPORT
QScreenCapture *ritual_ZN14QScreenCaptureC1EP7QObject(QObject *parent) {
  return new CuteQScreenCapture(parent);
}

//  QScreenCapture::~QScreenCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCaptureD1Ev(QScreenCapture *self) {
  delete self;
}

//  QMediaCaptureSession *QScreenCapture::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK14QScreenCapture14captureSessionEv(
    const QScreenCapture *self) {
  return self->captureSession();
}

//  void QScreenCapture::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture9setScreenEP7QScreen(
    QScreenCapture *self,
    QScreen *screen) {
  self->setScreen(screen);
}

//  QScreen *QScreenCapture::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK14QScreenCapture6screenEv(const QScreenCapture *self) {
  return self->screen();
}

//  bool QScreenCapture::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QScreenCapture8isActiveEv(const QScreenCapture *self) {
  return self->isActive();
}

//  Error QScreenCapture::error() const
extern "C" Q_DECL_EXPORT
QScreenCapture::Error ritual_ZNK14QScreenCapture5errorEv(
    const QScreenCapture *self) {
  return self->error();
}

//  QString QScreenCapture::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QScreenCapture11errorStringEv(
    const QScreenCapture *self) {
  return new QString(self->errorString());
}

//  void QScreenCapture::setMaximumFrameRate(std::optional<qreal> frameRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture19setMaximumFrameRateESt8optionalIdE(
    QScreenCapture *self,
    const std::optional<qreal> *frameRate) {
  self->setMaximumFrameRate(*frameRate);
}

//  std::optional<qreal> QScreenCapture::maximumFrameRate() const
extern "C" Q_DECL_EXPORT
std::optional<qreal> *ritual_ZNK14QScreenCapture16maximumFrameRateEv(
    const QScreenCapture *self) {
  return new std::optional<qreal>(self->maximumFrameRate());
}

//  void QScreenCapture::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture9setActiveEb(
    QScreenCapture *self,
    bool active) {
  self->setActive(active);
}

//  void QScreenCapture::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture5startEv(QScreenCapture *self) {
  self->start();
}

//  void QScreenCapture::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture4stopEv(QScreenCapture *self) {
  self->stop();
}

//  void QScreenCapture::activeChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture13activeChangedEb(
    QScreenCapture *self,
    bool a0) {
  self->activeChanged(a0);
}

//  void QScreenCapture::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture12errorChangedEv(QScreenCapture *self) {
  self->errorChanged();
}

//  void QScreenCapture::screenChanged(QScreen *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture13screenChangedEP7QScreen(
    QScreenCapture *self,
    QScreen *a0) {
  self->screenChanged(a0);
}

//  void QScreenCapture::errorOccurred(QScreenCapture::Error error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture13errorOccurredENS_5ErrorERK7QString(
    QScreenCapture *self,
    QScreenCapture::Error error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QScreenCapture::maximumFrameRateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture23maximumFrameRateChangedEv(
    QScreenCapture *self) {
  self->maximumFrameRateChanged();
}

//  void QScreenCapture::setCaptureSession(QMediaCaptureSession
//      *captureSession)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScreenCapture17setCaptureSessionEP20QMediaCaptureSession(
    QScreenCapture *self,
    QMediaCaptureSession *captureSession) {
  self->setCaptureSession(captureSession);
}

//  QPlatformSurfaceCapture *QScreenCapture::platformScreenCapture() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_ZNK14QScreenCapture21platformScreenCaptureEv(
    const QScreenCapture *self) {
  return self->platformScreenCapture();
}

//  QScreenCapturePrivate *QScreenCapture::d_func()
extern "C" Q_DECL_EXPORT
QScreenCapturePrivate *ritual_ZN14QScreenCapture6d_funcEv(
    QScreenCapture *self) {
  return self->d_func();
}

//  const QScreenCapturePrivate *QScreenCapture::d_func() const
extern "C" Q_DECL_EXPORT
const QScreenCapturePrivate *ritual_ZNK14QScreenCapture6d_funcEv(
    const QScreenCapture *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQScreenCapture, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScreenCapture(
    QScreenCapture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScreenCapture *>(self)->take(key, call);
}

//  a std::optional<qreal> a ritual of QScreenCapture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QScreenCapture__std_optional_qreal(
    std::optional<qreal> *self) {
  delete self;
}
