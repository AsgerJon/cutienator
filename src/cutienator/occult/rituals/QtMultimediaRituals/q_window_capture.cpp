//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qwindowcapture.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qwindowcapture.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qcapturablewindow.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <optional>

//  A QWindowCapture that Python can take functions over in. Every QWindowCapture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowCaptureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowCaptureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowCaptureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowCaptureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowCaptureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowCaptureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowCaptureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowCapture : public QWindowCapture {
public:
  using QWindowCapture::QWindowCapture;
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
      CuteQWindowCaptureCall0 call = reinterpret_cast<CuteQWindowCaptureCall0>(taken[0]);
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
      CuteQWindowCaptureCall1 call = reinterpret_cast<CuteQWindowCaptureCall1>(taken[1]);
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
      CuteQWindowCaptureCall2 call = reinterpret_cast<CuteQWindowCaptureCall2>(taken[2]);
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
      CuteQWindowCaptureCall3 call = reinterpret_cast<CuteQWindowCaptureCall3>(taken[3]);
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
      CuteQWindowCaptureCall4 call = reinterpret_cast<CuteQWindowCaptureCall4>(taken[4]);
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
      CuteQWindowCaptureCall5 call = reinterpret_cast<CuteQWindowCaptureCall5>(taken[5]);
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
      CuteQWindowCaptureCall6 call = reinterpret_cast<CuteQWindowCaptureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowCapture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QWindowCapture10metaObjectEv(
    const QWindowCapture *self) {
  return self->metaObject();
}

//  void *QWindowCapture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QWindowCapture11qt_metacastEPKc(
    QWindowCapture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWindowCapture::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QWindowCapture11qt_metacallEN11QMetaObject4CallEiPPv(
    QWindowCapture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWindowCapture::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QWindowCapture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowCapture::tr(s, c, n));
}

//  QWindowCapture::QWindowCapture(QObject *parent)
extern "C" Q_DECL_EXPORT
QWindowCapture *ritual_ZN14QWindowCaptureC1EP7QObject(QObject *parent) {
  return new CuteQWindowCapture(parent);
}

//  QWindowCapture::~QWindowCapture()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCaptureD1Ev(QWindowCapture *self) {
  delete self;
}

//  QList<QCapturableWindow> QWindowCapture::capturableWindows()
extern "C" Q_DECL_EXPORT
QList<QCapturableWindow> *ritual_ZN14QWindowCapture17capturableWindowsEv() {
  return new QList<QCapturableWindow>(QWindowCapture::capturableWindows());
}

//  QMediaCaptureSession *QWindowCapture::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK14QWindowCapture14captureSessionEv(
    const QWindowCapture *self) {
  return self->captureSession();
}

//  void QWindowCapture::setWindow(QCapturableWindow window)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture9setWindowE17QCapturableWindow(
    QWindowCapture *self,
    const QCapturableWindow *window) {
  self->setWindow(*window);
}

//  QCapturableWindow QWindowCapture::window() const
extern "C" Q_DECL_EXPORT
QCapturableWindow *ritual_ZNK14QWindowCapture6windowEv(
    const QWindowCapture *self) {
  return new QCapturableWindow(self->window());
}

//  bool QWindowCapture::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWindowCapture8isActiveEv(const QWindowCapture *self) {
  return self->isActive();
}

//  Error QWindowCapture::error() const
extern "C" Q_DECL_EXPORT
QWindowCapture::Error ritual_ZNK14QWindowCapture5errorEv(
    const QWindowCapture *self) {
  return self->error();
}

//  QString QWindowCapture::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QWindowCapture11errorStringEv(
    const QWindowCapture *self) {
  return new QString(self->errorString());
}

//  void QWindowCapture::setMaximumFrameRate(std::optional<qreal> frameRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture19setMaximumFrameRateESt8optionalIdE(
    QWindowCapture *self,
    const std::optional<qreal> *frameRate) {
  self->setMaximumFrameRate(*frameRate);
}

//  std::optional<qreal> QWindowCapture::maximumFrameRate() const
extern "C" Q_DECL_EXPORT
std::optional<qreal> *ritual_ZNK14QWindowCapture16maximumFrameRateEv(
    const QWindowCapture *self) {
  return new std::optional<qreal>(self->maximumFrameRate());
}

//  void QWindowCapture::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture9setActiveEb(
    QWindowCapture *self,
    bool active) {
  self->setActive(active);
}

//  void QWindowCapture::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture5startEv(QWindowCapture *self) {
  self->start();
}

//  void QWindowCapture::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture4stopEv(QWindowCapture *self) {
  self->stop();
}

//  void QWindowCapture::activeChanged(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture13activeChangedEb(
    QWindowCapture *self,
    bool a0) {
  self->activeChanged(a0);
}

//  void QWindowCapture::windowChanged(QCapturableWindow window)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture13windowChangedE17QCapturableWindow(
    QWindowCapture *self,
    const QCapturableWindow *window) {
  self->windowChanged(*window);
}

//  void QWindowCapture::errorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture12errorChangedEv(QWindowCapture *self) {
  self->errorChanged();
}

//  void QWindowCapture::errorOccurred(QWindowCapture::Error error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture13errorOccurredENS_5ErrorERK7QString(
    QWindowCapture *self,
    QWindowCapture::Error error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  void QWindowCapture::maximumFrameRateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture23maximumFrameRateChangedEv(
    QWindowCapture *self) {
  self->maximumFrameRateChanged();
}

//  void QWindowCapture::setCaptureSession(QMediaCaptureSession
//      *captureSession)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowCapture17setCaptureSessionEP20QMediaCaptureSession(
    QWindowCapture *self,
    QMediaCaptureSession *captureSession) {
  self->setCaptureSession(captureSession);
}

//  QPlatformSurfaceCapture *QWindowCapture::platformWindowCapture() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceCapture *ritual_ZNK14QWindowCapture21platformWindowCaptureEv(
    const QWindowCapture *self) {
  return self->platformWindowCapture();
}

//  QWindowCapturePrivate *QWindowCapture::d_func()
extern "C" Q_DECL_EXPORT
QWindowCapturePrivate *ritual_ZN14QWindowCapture6d_funcEv(
    QWindowCapture *self) {
  return self->d_func();
}

//  const QWindowCapturePrivate *QWindowCapture::d_func() const
extern "C" Q_DECL_EXPORT
const QWindowCapturePrivate *ritual_ZNK14QWindowCapture6d_funcEv(
    const QWindowCapture *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWindowCapture, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowCapture(
    QWindowCapture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowCapture *>(self)->take(key, call);
}

//  a std::optional<qreal> a ritual of QWindowCapture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWindowCapture__std_optional_qreal(
    std::optional<qreal> *self) {
  delete self;
}
