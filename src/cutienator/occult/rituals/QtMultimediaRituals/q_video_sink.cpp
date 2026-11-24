//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qvideosink.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qvideosink.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QVideoSink that Python can take functions over in. Every QVideoSink
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoSinkCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQVideoSinkCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoSinkCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoSinkCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoSinkCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoSinkCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQVideoSinkCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQVideoSink : public QVideoSink {
public:
  using QVideoSink::QVideoSink;
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
      CuteQVideoSinkCall0 call = reinterpret_cast<CuteQVideoSinkCall0>(taken[0]);
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
      CuteQVideoSinkCall1 call = reinterpret_cast<CuteQVideoSinkCall1>(taken[1]);
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
      CuteQVideoSinkCall2 call = reinterpret_cast<CuteQVideoSinkCall2>(taken[2]);
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
      CuteQVideoSinkCall3 call = reinterpret_cast<CuteQVideoSinkCall3>(taken[3]);
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
      CuteQVideoSinkCall4 call = reinterpret_cast<CuteQVideoSinkCall4>(taken[4]);
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
      CuteQVideoSinkCall5 call = reinterpret_cast<CuteQVideoSinkCall5>(taken[5]);
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
      CuteQVideoSinkCall6 call = reinterpret_cast<CuteQVideoSinkCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QVideoSink::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QVideoSink10metaObjectEv(
    const QVideoSink *self) {
  return self->metaObject();
}

//  QString QVideoSink::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QVideoSink2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QVideoSink::tr(s, c, n));
}

//  QVideoSink::QVideoSink(QObject *parent)
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZN10QVideoSinkC1EP7QObject(QObject *parent) {
  return new CuteQVideoSink(parent);
}

//  QVideoSink::~QVideoSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVideoSinkD1Ev(QVideoSink *self) {
  delete self;
}

//  QRhi *QVideoSink::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK10QVideoSink3rhiEv(const QVideoSink *self) {
  return self->rhi();
}

//  void QVideoSink::setRhi(QRhi *rhi)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVideoSink6setRhiEP4QRhi(QVideoSink *self, QRhi *rhi) {
  self->setRhi(rhi);
}

//  QSize QVideoSink::videoSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QVideoSink9videoSizeEv(const QVideoSink *self) {
  return new QSize(self->videoSize());
}

//  QString QVideoSink::subtitleText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QVideoSink12subtitleTextEv(const QVideoSink *self) {
  return new QString(self->subtitleText());
}

//  void QVideoSink::setSubtitleText(const QString &subtitle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVideoSink15setSubtitleTextERK7QString(
    QVideoSink *self,
    const QString *subtitle) {
  self->setSubtitleText(*subtitle);
}

//  void QVideoSink::setVideoFrame(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVideoSink13setVideoFrameERK11QVideoFrame(
    QVideoSink *self,
    const QVideoFrame *frame) {
  self->setVideoFrame(*frame);
}

//  QVideoFrame QVideoSink::videoFrame() const
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZNK10QVideoSink10videoFrameEv(const QVideoSink *self) {
  return new QVideoFrame(self->videoFrame());
}

//  QPlatformVideoSink *QVideoSink::platformVideoSink() const
extern "C" Q_DECL_EXPORT
QPlatformVideoSink *ritual_ZNK10QVideoSink17platformVideoSinkEv(
    const QVideoSink *self) {
  return self->platformVideoSink();
}

//  void QVideoSink::setSource(QObject *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QVideoSink9setSourceEP7QObject(
    QVideoSink *self,
    QObject *source) {
  self->setSource(source);
}

//  a Python function taken by a CuteQVideoSink, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QVideoSink(QVideoSink *self, const char *key, void *call) {
  return static_cast<CuteQVideoSink *>(self)->take(key, call);
}
