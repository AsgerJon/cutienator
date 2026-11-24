//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamervideosource.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(gstreamer_qt_api)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/spi/qgstreamervideosource.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGStreamerVideoSource that Python can take functions over in. Every QGStreamerVideoSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGStreamerVideoSourceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGStreamerVideoSourceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGStreamerVideoSourceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGStreamerVideoSourceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGStreamerVideoSourceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGStreamerVideoSourceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGStreamerVideoSourceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGStreamerVideoSource : public QGStreamerVideoSource {
public:
  using QGStreamerVideoSource::QGStreamerVideoSource;
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
      CuteQGStreamerVideoSourceCall0 call = reinterpret_cast<CuteQGStreamerVideoSourceCall0>(taken[0]);
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
      CuteQGStreamerVideoSourceCall1 call = reinterpret_cast<CuteQGStreamerVideoSourceCall1>(taken[1]);
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
      CuteQGStreamerVideoSourceCall2 call = reinterpret_cast<CuteQGStreamerVideoSourceCall2>(taken[2]);
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
      CuteQGStreamerVideoSourceCall3 call = reinterpret_cast<CuteQGStreamerVideoSourceCall3>(taken[3]);
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
      CuteQGStreamerVideoSourceCall4 call = reinterpret_cast<CuteQGStreamerVideoSourceCall4>(taken[4]);
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
      CuteQGStreamerVideoSourceCall5 call = reinterpret_cast<CuteQGStreamerVideoSourceCall5>(taken[5]);
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
      CuteQGStreamerVideoSourceCall6 call = reinterpret_cast<CuteQGStreamerVideoSourceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGStreamerVideoSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGStreamerVideoSource10metaObjectEv(
    const QGStreamerVideoSource *self) {
  return self->metaObject();
}

//  QString QGStreamerVideoSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGStreamerVideoSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGStreamerVideoSource::tr(s, c, n));
}

//  QGStreamerVideoSource::QGStreamerVideoSource(const QString
//      &gstBinDescription, QObject *parent)
extern "C" Q_DECL_EXPORT
QGStreamerVideoSource *ritual_ZN21QGStreamerVideoSourceC1ERK7QStringP7QObject(
    const QString *gstBinDescription,
    QObject *parent) {
  return new CuteQGStreamerVideoSource(*gstBinDescription, parent);
}

//  QGStreamerVideoSource::~QGStreamerVideoSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGStreamerVideoSourceD1Ev(QGStreamerVideoSource *self) {
  delete self;
}

//  bool QGStreamerVideoSource::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGStreamerVideoSource8isActiveEv(
    const QGStreamerVideoSource *self) {
  return self->isActive();
}

//  QString QGStreamerVideoSource::gstBinDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QGStreamerVideoSource17gstBinDescriptionEv(
    const QGStreamerVideoSource *self) {
  return new QString(self->gstBinDescription());
}

//  QMediaCaptureSession *QGStreamerVideoSource::captureSession() const
extern "C" Q_DECL_EXPORT
QMediaCaptureSession *ritual_ZNK21QGStreamerVideoSource14captureSessionEv(
    const QGStreamerVideoSource *self) {
  return self->captureSession();
}

//  void QGStreamerVideoSource::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGStreamerVideoSource9setActiveEb(
    QGStreamerVideoSource *self,
    bool active) {
  self->setActive(active);
}

//  void QGStreamerVideoSource::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGStreamerVideoSource5startEv(QGStreamerVideoSource *self) {
  self->start();
}

//  void QGStreamerVideoSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGStreamerVideoSource4stopEv(QGStreamerVideoSource *self) {
  self->stop();
}

//  QGStreamerVideoSource::QGStreamerVideoSource(QObject *parent)
extern "C" Q_DECL_EXPORT
QGStreamerVideoSource *ritual_ZN21QGStreamerVideoSourceC1EP7QObject(
    QObject *parent) {
  return new CuteQGStreamerVideoSource(parent);
}

//  void QGStreamerVideoSource::setCaptureSession(QMediaCaptureSession
//      *session)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGStreamerVideoSource17setCaptureSessionEP20QMediaCaptureSession(
    QGStreamerVideoSource *self,
    QMediaCaptureSession *session) {
  self->setCaptureSession(session);
}

//  QGStreamerVideoSourcePrivate *QGStreamerVideoSource::d_func()
extern "C" Q_DECL_EXPORT
QGStreamerVideoSourcePrivate *ritual_ZN21QGStreamerVideoSource6d_funcEv(
    QGStreamerVideoSource *self) {
  return self->d_func();
}

//  const QGStreamerVideoSourcePrivate *QGStreamerVideoSource::d_func() const
extern "C" Q_DECL_EXPORT
const QGStreamerVideoSourcePrivate *ritual_ZNK21QGStreamerVideoSource6d_funcEv(
    const QGStreamerVideoSource *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGStreamerVideoSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGStreamerVideoSource(
    QGStreamerVideoSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGStreamerVideoSource *>(self)->take(key, call);
}

#endif  // QT_CONFIG(gstreamer_qt_api)
