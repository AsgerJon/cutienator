//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeocodereply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeocodereply.h>
#include <QtCore/qstring.h>
#include <QtPositioning/qgeoshape.h>
#include <QtPositioning/qgeolocation.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoCodeReply that Python can take functions over in. Every QGeoCodeReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoCodeReplyCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCodeReplyCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoCodeReplyCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodeReplyCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodeReplyCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodeReplyCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodeReplyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoCodeReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoCodeReply : public QGeoCodeReply {
public:
  using QGeoCodeReply::QGeoCodeReply;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QGeoCodeReply5abortEv")) {
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

  //  void QGeoCodeReply::abort()
  void abort() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoCodeReplyCall0 call = reinterpret_cast<CuteQGeoCodeReplyCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoCodeReply::abort();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoCodeReplyCall1 call = reinterpret_cast<CuteQGeoCodeReplyCall1>(taken[1]);
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
      CuteQGeoCodeReplyCall2 call = reinterpret_cast<CuteQGeoCodeReplyCall2>(taken[2]);
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
      CuteQGeoCodeReplyCall3 call = reinterpret_cast<CuteQGeoCodeReplyCall3>(taken[3]);
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
      CuteQGeoCodeReplyCall4 call = reinterpret_cast<CuteQGeoCodeReplyCall4>(taken[4]);
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
      CuteQGeoCodeReplyCall5 call = reinterpret_cast<CuteQGeoCodeReplyCall5>(taken[5]);
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
      CuteQGeoCodeReplyCall6 call = reinterpret_cast<CuteQGeoCodeReplyCall6>(taken[6]);
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
      CuteQGeoCodeReplyCall7 call = reinterpret_cast<CuteQGeoCodeReplyCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoCodeReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QGeoCodeReply10metaObjectEv(
    const QGeoCodeReply *self) {
  return self->metaObject();
}

//  void *QGeoCodeReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QGeoCodeReply11qt_metacastEPKc(
    QGeoCodeReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoCodeReply::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QGeoCodeReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoCodeReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoCodeReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QGeoCodeReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoCodeReply::tr(s, c, n));
}

//  QGeoCodeReply::QGeoCodeReply(Error error, const QString &errorString,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN13QGeoCodeReplyC1ENS_5ErrorERK7QStringP7QObject(
    QGeoCodeReply::Error error,
    const QString *errorString,
    QObject *parent) {
  return new CuteQGeoCodeReply(error, *errorString, parent);
}

//  QGeoCodeReply::~QGeoCodeReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReplyD1Ev(QGeoCodeReply *self) {
  delete self;
}

//  bool QGeoCodeReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGeoCodeReply10isFinishedEv(const QGeoCodeReply *self) {
  return self->isFinished();
}

//  Error QGeoCodeReply::error() const
extern "C" Q_DECL_EXPORT
QGeoCodeReply::Error ritual_ZNK13QGeoCodeReply5errorEv(
    const QGeoCodeReply *self) {
  return self->error();
}

//  QString QGeoCodeReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QGeoCodeReply11errorStringEv(
    const QGeoCodeReply *self) {
  return new QString(self->errorString());
}

//  QGeoShape QGeoCodeReply::viewport() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK13QGeoCodeReply8viewportEv(const QGeoCodeReply *self) {
  return new QGeoShape(self->viewport());
}

//  QList<QGeoLocation> QGeoCodeReply::locations() const
extern "C" Q_DECL_EXPORT
QList<QGeoLocation> *ritual_ZNK13QGeoCodeReply9locationsEv(
    const QGeoCodeReply *self) {
  return new QList<QGeoLocation>(self->locations());
}

//  qsizetype QGeoCodeReply::limit() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QGeoCodeReply5limitEv(const QGeoCodeReply *self) {
  return self->limit();
}

//  qsizetype QGeoCodeReply::offset() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QGeoCodeReply6offsetEv(const QGeoCodeReply *self) {
  return self->offset();
}

//  void QGeoCodeReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply5abortEv(QGeoCodeReply *self) {
  self->abort();
}

//  void QGeoCodeReply::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply8finishedEv(QGeoCodeReply *self) {
  self->finished();
}

//  void QGeoCodeReply::aborted()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply7abortedEv(QGeoCodeReply *self) {
  self->aborted();
}

//  void QGeoCodeReply::errorOccurred(QGeoCodeReply::Error error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply13errorOccurredENS_5ErrorERK7QString(
    QGeoCodeReply *self,
    QGeoCodeReply::Error error,
    const QString *errorString) {
  self->errorOccurred(error, *errorString);
}

//  QGeoCodeReply::QGeoCodeReply(QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoCodeReply *ritual_ZN13QGeoCodeReplyC1EP7QObject(QObject *parent) {
  return new CuteQGeoCodeReply(parent);
}

//  void QGeoCodeReply::setError(Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply8setErrorENS_5ErrorERK7QString(
    QGeoCodeReply *self,
    QGeoCodeReply::Error error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QGeoCodeReply::setFinished(bool finished)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply11setFinishedEb(
    QGeoCodeReply *self,
    bool finished) {
  self->setFinished(finished);
}

//  void QGeoCodeReply::setViewport(const QGeoShape &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply11setViewportERK9QGeoShape(
    QGeoCodeReply *self,
    const QGeoShape *viewport) {
  self->setViewport(*viewport);
}

//  void QGeoCodeReply::addLocation(const QGeoLocation &location)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply11addLocationERK12QGeoLocation(
    QGeoCodeReply *self,
    const QGeoLocation *location) {
  self->addLocation(*location);
}

//  void QGeoCodeReply::setLocations(const QList<QGeoLocation> &locations)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply12setLocationsERK5QListI12QGeoLocationE(
    QGeoCodeReply *self,
    const QList<QGeoLocation> *locations) {
  self->setLocations(*locations);
}

//  void QGeoCodeReply::setLimit(qsizetype limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply8setLimitEx(
    QGeoCodeReply *self,
    qsizetype limit) {
  self->setLimit(limit);
}

//  void QGeoCodeReply::setOffset(qsizetype offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoCodeReply9setOffsetEx(
    QGeoCodeReply *self,
    qsizetype offset) {
  self->setOffset(offset);
}

//  a Python function taken by a CuteQGeoCodeReply, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoCodeReply(
    QGeoCodeReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoCodeReply *>(self)->take(key, call);
}

//  void QGeoCodeReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QGeoCodeReply5abortEv(QGeoCodeReply *self) {
  self->QGeoCodeReply::abort();
}
