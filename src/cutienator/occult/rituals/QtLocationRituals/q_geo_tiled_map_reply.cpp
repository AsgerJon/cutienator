//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmapreply_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoTiledMapReply that Python can take functions over in. Every QGeoTiledMapReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoTiledMapReplyCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMapReplyCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMapReplyCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapReplyCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapReplyCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapReplyCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapReplyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMapReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoTiledMapReply : public QGeoTiledMapReply {
public:
  using QGeoTiledMapReply::QGeoTiledMapReply;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QGeoTiledMapReply5abortEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGeoTiledMapReply::abort()
  void abort() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall0 call = reinterpret_cast<CuteQGeoTiledMapReplyCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoTiledMapReply::abort();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall1 call = reinterpret_cast<CuteQGeoTiledMapReplyCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall2 call = reinterpret_cast<CuteQGeoTiledMapReplyCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall3 call = reinterpret_cast<CuteQGeoTiledMapReplyCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall4 call = reinterpret_cast<CuteQGeoTiledMapReplyCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall5 call = reinterpret_cast<CuteQGeoTiledMapReplyCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall6 call = reinterpret_cast<CuteQGeoTiledMapReplyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoTiledMapReplyCall7 call = reinterpret_cast<CuteQGeoTiledMapReplyCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoTiledMapReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGeoTiledMapReply10metaObjectEv(
    const QGeoTiledMapReply *self) {
  return self->metaObject();
}

//  QString QGeoTiledMapReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGeoTiledMapReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoTiledMapReply::tr(s, c, n));
}

//  QGeoTiledMapReply::QGeoTiledMapReply(const QGeoTileSpec &spec, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoTiledMapReply *ritual_ZN17QGeoTiledMapReplyC1ERK12QGeoTileSpecP7QObject(
    const QGeoTileSpec *spec,
    QObject *parent) {
  return new CuteQGeoTiledMapReply(*spec, parent);
}

//  QGeoTiledMapReply::QGeoTiledMapReply(Error error, const QString
//      &errorString, QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoTiledMapReply *ritual_ZN17QGeoTiledMapReplyC1ENS_5ErrorERK7QStringP7QObject(
    QGeoTiledMapReply::Error error,
    const QString *errorString,
    QObject *parent) {
  return new CuteQGeoTiledMapReply(error, *errorString, parent);
}

//  QGeoTiledMapReply::~QGeoTiledMapReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReplyD1Ev(QGeoTiledMapReply *self) {
  delete self;
}

//  bool QGeoTiledMapReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoTiledMapReply10isFinishedEv(
    const QGeoTiledMapReply *self) {
  return self->isFinished();
}

//  Error QGeoTiledMapReply::error() const
extern "C" Q_DECL_EXPORT
QGeoTiledMapReply::Error ritual_ZNK17QGeoTiledMapReply5errorEv(
    const QGeoTiledMapReply *self) {
  return self->error();
}

//  QString QGeoTiledMapReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGeoTiledMapReply11errorStringEv(
    const QGeoTiledMapReply *self) {
  return new QString(self->errorString());
}

//  bool QGeoTiledMapReply::isCached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoTiledMapReply8isCachedEv(
    const QGeoTiledMapReply *self) {
  return self->isCached();
}

//  QGeoTileSpec QGeoTiledMapReply::tileSpec() const
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_ZNK17QGeoTiledMapReply8tileSpecEv(
    const QGeoTiledMapReply *self) {
  return new QGeoTileSpec(self->tileSpec());
}

//  QByteArray QGeoTiledMapReply::mapImageData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QGeoTiledMapReply12mapImageDataEv(
    const QGeoTiledMapReply *self) {
  return new QByteArray(self->mapImageData());
}

//  QString QGeoTiledMapReply::mapImageFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGeoTiledMapReply14mapImageFormatEv(
    const QGeoTiledMapReply *self) {
  return new QString(self->mapImageFormat());
}

//  void QGeoTiledMapReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReply5abortEv(QGeoTiledMapReply *self) {
  self->abort();
}

//  void QGeoTiledMapReply::setError(Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReply8setErrorENS_5ErrorERK7QString(
    QGeoTiledMapReply *self,
    QGeoTiledMapReply::Error error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QGeoTiledMapReply::setFinished(bool finished)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReply11setFinishedEb(
    QGeoTiledMapReply *self,
    bool finished) {
  self->setFinished(finished);
}

//  void QGeoTiledMapReply::setCached(bool cached)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReply9setCachedEb(
    QGeoTiledMapReply *self,
    bool cached) {
  self->setCached(cached);
}

//  void QGeoTiledMapReply::setMapImageData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReply15setMapImageDataERK10QByteArray(
    QGeoTiledMapReply *self,
    const QByteArray *data) {
  self->setMapImageData(*data);
}

//  void QGeoTiledMapReply::setMapImageFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoTiledMapReply17setMapImageFormatERK7QString(
    QGeoTiledMapReply *self,
    const QString *format) {
  self->setMapImageFormat(*format);
}

//  a Python function taken by a CuteQGeoTiledMapReply, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMapReply(
    QGeoTiledMapReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMapReply *>(self)->take(key, call);
}

//  void QGeoTiledMapReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoTiledMapReply5abortEv(QGeoTiledMapReply *self) {
  self->QGeoTiledMapReply::abort();
}
