//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideosink_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformvideosink_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QPlatformVideoSink may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPlatformVideoSink : QPlatformVideoSink {
  using QPlatformVideoSink::onVideoFrameChanged;
};

//  A QPlatformVideoSink that Python can take functions over in. Every QPlatformVideoSink
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformVideoSinkCall0)(const void *, QRhi *, int *);
typedef void (*CuteQPlatformVideoSinkCall1)(const void *, WId, int *);
typedef void (*CuteQPlatformVideoSinkCall2)(const void *, const QRect *, int *);
typedef void (*CuteQPlatformVideoSinkCall3)(const void *, bool, int *);
typedef void (*CuteQPlatformVideoSinkCall4)(const void *, int, int *);
typedef void (*CuteQPlatformVideoSinkCall5)(const void *, float, int *);
typedef void (*CuteQPlatformVideoSinkCall6)(const void *, float, int *);
typedef void (*CuteQPlatformVideoSinkCall7)(const void *, float, int *);
typedef void (*CuteQPlatformVideoSinkCall8)(const void *, float, int *);
typedef void (*CuteQPlatformVideoSinkCall9)(const void *, const QVideoFrame *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformVideoSinkCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformVideoSinkCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSinkCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSinkCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSinkCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSinkCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformVideoSinkCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformVideoSink : public QPlatformVideoSink {
public:
  using QPlatformVideoSink::QPlatformVideoSink;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink6setRhiEP4QRhi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink8setWinIdEy")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink14setDisplayRectERK5QRect")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink13setFullScreenEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink18setAspectRatioModeEN2Qt15AspectRatioModeE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink13setBrightnessEf")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink11setContrastEf")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink6setHueEf")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink13setSaturationEf")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformVideoSink19onVideoFrameChangedERK11QVideoFrame")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPlatformVideoSink::setRhi(QRhi *a0)
  void setRhi(QRhi *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall0 call = reinterpret_cast<CuteQPlatformVideoSinkCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setRhi(a0);
  }

  //  void QPlatformVideoSink::setWinId(WId a0)
  void setWinId(WId a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall1 call = reinterpret_cast<CuteQPlatformVideoSinkCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setWinId(a0);
  }

  //  void QPlatformVideoSink::setDisplayRect(const QRect &a0)
  void setDisplayRect(const QRect &a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall2 call = reinterpret_cast<CuteQPlatformVideoSinkCall2>(taken[2]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setDisplayRect(a0);
  }

  //  void QPlatformVideoSink::setFullScreen(bool a0)
  void setFullScreen(bool a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall3 call = reinterpret_cast<CuteQPlatformVideoSinkCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setFullScreen(a0);
  }

  //  void QPlatformVideoSink::setAspectRatioMode(Qt::AspectRatioMode a0)
  void setAspectRatioMode(Qt::AspectRatioMode a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall4 call = reinterpret_cast<CuteQPlatformVideoSinkCall4>(taken[4]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setAspectRatioMode(a0);
  }

  //  void QPlatformVideoSink::setBrightness(float a0)
  void setBrightness(float a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall5 call = reinterpret_cast<CuteQPlatformVideoSinkCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setBrightness(a0);
  }

  //  void QPlatformVideoSink::setContrast(float a0)
  void setContrast(float a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall6 call = reinterpret_cast<CuteQPlatformVideoSinkCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setContrast(a0);
  }

  //  void QPlatformVideoSink::setHue(float a0)
  void setHue(float a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall7 call = reinterpret_cast<CuteQPlatformVideoSinkCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setHue(a0);
  }

  //  void QPlatformVideoSink::setSaturation(float a0)
  void setSaturation(float a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall8 call = reinterpret_cast<CuteQPlatformVideoSinkCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::setSaturation(a0);
  }

  //  void QPlatformVideoSink::onVideoFrameChanged(const QVideoFrame &a0)
  void onVideoFrameChanged(const QVideoFrame &a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall9 call = reinterpret_cast<CuteQPlatformVideoSinkCall9>(taken[9]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QPlatformVideoSink::onVideoFrameChanged(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall10 call = reinterpret_cast<CuteQPlatformVideoSinkCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall11 call = reinterpret_cast<CuteQPlatformVideoSinkCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall12 call = reinterpret_cast<CuteQPlatformVideoSinkCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall13 call = reinterpret_cast<CuteQPlatformVideoSinkCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall14 call = reinterpret_cast<CuteQPlatformVideoSinkCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall15 call = reinterpret_cast<CuteQPlatformVideoSinkCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformVideoSinkCall16 call = reinterpret_cast<CuteQPlatformVideoSinkCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformVideoSink::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPlatformVideoSink10metaObjectEv(
    const QPlatformVideoSink *self) {
  return self->metaObject();
}

//  QString QPlatformVideoSink::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPlatformVideoSink2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformVideoSink::tr(s, c, n));
}

//  QPlatformVideoSink::~QPlatformVideoSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSinkD1Ev(QPlatformVideoSink *self) {
  delete self;
}

//  void QPlatformVideoSink::setRhi(QRhi *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink6setRhiEP4QRhi(
    QPlatformVideoSink *self,
    QRhi *a0) {
  self->setRhi(a0);
}

//  void QPlatformVideoSink::setWinId(WId a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink8setWinIdEy(
    QPlatformVideoSink *self,
    WId a0) {
  self->setWinId(a0);
}

//  void QPlatformVideoSink::setDisplayRect(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink14setDisplayRectERK5QRect(
    QPlatformVideoSink *self,
    const QRect *a0) {
  self->setDisplayRect(*a0);
}

//  void QPlatformVideoSink::setFullScreen(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink13setFullScreenEb(
    QPlatformVideoSink *self,
    bool a0) {
  self->setFullScreen(a0);
}

//  void QPlatformVideoSink::setAspectRatioMode(Qt::AspectRatioMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink18setAspectRatioModeEN2Qt15AspectRatioModeE(
    QPlatformVideoSink *self,
    Qt::AspectRatioMode a0) {
  self->setAspectRatioMode(a0);
}

//  QSize QPlatformVideoSink::nativeSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QPlatformVideoSink10nativeSizeEv(
    const QPlatformVideoSink *self) {
  return new QSize(self->nativeSize());
}

//  void QPlatformVideoSink::setBrightness(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink13setBrightnessEf(
    QPlatformVideoSink *self,
    float a0) {
  self->setBrightness(a0);
}

//  void QPlatformVideoSink::setContrast(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink11setContrastEf(
    QPlatformVideoSink *self,
    float a0) {
  self->setContrast(a0);
}

//  void QPlatformVideoSink::setHue(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink6setHueEf(
    QPlatformVideoSink *self,
    float a0) {
  self->setHue(a0);
}

//  void QPlatformVideoSink::setSaturation(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink13setSaturationEf(
    QPlatformVideoSink *self,
    float a0) {
  self->setSaturation(a0);
}

//  QVideoSink *QPlatformVideoSink::videoSink()
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZN18QPlatformVideoSink9videoSinkEv(
    QPlatformVideoSink *self) {
  return self->videoSink();
}

//  void QPlatformVideoSink::setNativeSize(QSize s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink13setNativeSizeE5QSize(
    QPlatformVideoSink *self,
    const QSize *s) {
  self->setNativeSize(*s);
}

//  void QPlatformVideoSink::setVideoFrame(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink13setVideoFrameERK11QVideoFrame(
    QPlatformVideoSink *self,
    const QVideoFrame *frame) {
  self->setVideoFrame(*frame);
}

//  QVideoFrame QPlatformVideoSink::currentVideoFrame() const
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZNK18QPlatformVideoSink17currentVideoFrameEv(
    const QPlatformVideoSink *self) {
  return new QVideoFrame(self->currentVideoFrame());
}

//  void QPlatformVideoSink::setSubtitleText(const QString &subtitleText)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink15setSubtitleTextERK7QString(
    QPlatformVideoSink *self,
    const QString *subtitleText) {
  self->setSubtitleText(*subtitleText);
}

//  QString QPlatformVideoSink::subtitleText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QPlatformVideoSink12subtitleTextEv(
    const QPlatformVideoSink *self) {
  return new QString(self->subtitleText());
}

//  QPlatformVideoSink::QPlatformVideoSink(QVideoSink *parent)
extern "C" Q_DECL_EXPORT
QPlatformVideoSink *ritual_ZN18QPlatformVideoSinkC1EP10QVideoSink(
    QVideoSink *parent) {
  return new CuteQPlatformVideoSink(parent);
}

//  void QPlatformVideoSink::onVideoFrameChanged(const QVideoFrame &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformVideoSink19onVideoFrameChangedERK11QVideoFrame(
    QPlatformVideoSink *self,
    const QVideoFrame *a0) {
  self->onVideoFrameChanged(*a0);
}

//  a Python function taken by a CuteQPlatformVideoSink, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformVideoSink(
    QPlatformVideoSink *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformVideoSink *>(self)->take(key, call);
}

//  void QPlatformVideoSink::setRhi(QRhi *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink6setRhiEP4QRhi(
    QPlatformVideoSink *self,
    QRhi *a0) {
  self->QPlatformVideoSink::setRhi(a0);
}

//  void QPlatformVideoSink::setWinId(WId a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink8setWinIdEy(
    QPlatformVideoSink *self,
    WId a0) {
  self->QPlatformVideoSink::setWinId(a0);
}

//  void QPlatformVideoSink::setDisplayRect(const QRect &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink14setDisplayRectERK5QRect(
    QPlatformVideoSink *self,
    const QRect *a0) {
  self->QPlatformVideoSink::setDisplayRect(*a0);
}

//  void QPlatformVideoSink::setFullScreen(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink13setFullScreenEb(
    QPlatformVideoSink *self,
    bool a0) {
  self->QPlatformVideoSink::setFullScreen(a0);
}

//  void QPlatformVideoSink::setAspectRatioMode(Qt::AspectRatioMode a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink18setAspectRatioModeEN2Qt15AspectRatioModeE(
    QPlatformVideoSink *self,
    Qt::AspectRatioMode a0) {
  self->QPlatformVideoSink::setAspectRatioMode(a0);
}

//  void QPlatformVideoSink::setBrightness(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink13setBrightnessEf(
    QPlatformVideoSink *self,
    float a0) {
  self->QPlatformVideoSink::setBrightness(a0);
}

//  void QPlatformVideoSink::setContrast(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink11setContrastEf(
    QPlatformVideoSink *self,
    float a0) {
  self->QPlatformVideoSink::setContrast(a0);
}

//  void QPlatformVideoSink::setHue(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink6setHueEf(
    QPlatformVideoSink *self,
    float a0) {
  self->QPlatformVideoSink::setHue(a0);
}

//  void QPlatformVideoSink::setSaturation(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink13setSaturationEf(
    QPlatformVideoSink *self,
    float a0) {
  self->QPlatformVideoSink::setSaturation(a0);
}

//  void QPlatformVideoSink::onVideoFrameChanged(const QVideoFrame &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformVideoSink19onVideoFrameChangedERK11QVideoFrame(
    QPlatformVideoSink *self,
    const QVideoFrame *a0) {
  static_cast<OwnQPlatformVideoSink *>(self)->OwnQPlatformVideoSink::onVideoFrameChanged(
      *a0);
}
