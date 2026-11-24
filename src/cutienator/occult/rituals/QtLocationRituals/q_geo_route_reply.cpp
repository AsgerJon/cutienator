//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeoroutereply.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeoroutereply.h>
#include <QtCore/qstring.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtLocation/qgeoroute.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QGeoRouteReply that Python can take functions over in. Every QGeoRouteReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoRouteReplyCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRouteReplyCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRouteReplyCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteReplyCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteReplyCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteReplyCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteReplyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteReplyCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoRouteReply : public QGeoRouteReply {
public:
  using QGeoRouteReply::QGeoRouteReply;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QGeoRouteReply5abortEv")) {
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

  //  void QGeoRouteReply::abort()
  void abort() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoRouteReplyCall0 call = reinterpret_cast<CuteQGeoRouteReplyCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoRouteReply::abort();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoRouteReplyCall1 call = reinterpret_cast<CuteQGeoRouteReplyCall1>(taken[1]);
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
      CuteQGeoRouteReplyCall2 call = reinterpret_cast<CuteQGeoRouteReplyCall2>(taken[2]);
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
      CuteQGeoRouteReplyCall3 call = reinterpret_cast<CuteQGeoRouteReplyCall3>(taken[3]);
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
      CuteQGeoRouteReplyCall4 call = reinterpret_cast<CuteQGeoRouteReplyCall4>(taken[4]);
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
      CuteQGeoRouteReplyCall5 call = reinterpret_cast<CuteQGeoRouteReplyCall5>(taken[5]);
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
      CuteQGeoRouteReplyCall6 call = reinterpret_cast<CuteQGeoRouteReplyCall6>(taken[6]);
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
      CuteQGeoRouteReplyCall7 call = reinterpret_cast<CuteQGeoRouteReplyCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoRouteReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGeoRouteReply10metaObjectEv(
    const QGeoRouteReply *self) {
  return self->metaObject();
}

//  QString QGeoRouteReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGeoRouteReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoRouteReply::tr(s, c, n));
}

//  QGeoRouteReply::QGeoRouteReply(Error error, const QString &errorString,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_ZN14QGeoRouteReplyC1ENS_5ErrorERK7QStringP7QObject(
    QGeoRouteReply::Error error,
    const QString *errorString,
    QObject *parent) {
  return new CuteQGeoRouteReply(error, *errorString, parent);
}

//  QGeoRouteReply::~QGeoRouteReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoRouteReplyD1Ev(QGeoRouteReply *self) {
  delete self;
}

//  bool QGeoRouteReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGeoRouteReply10isFinishedEv(const QGeoRouteReply *self) {
  return self->isFinished();
}

//  Error QGeoRouteReply::error() const
extern "C" Q_DECL_EXPORT
QGeoRouteReply::Error ritual_ZNK14QGeoRouteReply5errorEv(
    const QGeoRouteReply *self) {
  return self->error();
}

//  QString QGeoRouteReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QGeoRouteReply11errorStringEv(
    const QGeoRouteReply *self) {
  return new QString(self->errorString());
}

//  QGeoRouteRequest QGeoRouteReply::request() const
extern "C" Q_DECL_EXPORT
QGeoRouteRequest *ritual_ZNK14QGeoRouteReply7requestEv(
    const QGeoRouteReply *self) {
  return new QGeoRouteRequest(self->request());
}

//  QList<QGeoRoute> QGeoRouteReply::routes() const
extern "C" Q_DECL_EXPORT
QList<QGeoRoute> *ritual_ZNK14QGeoRouteReply6routesEv(
    const QGeoRouteReply *self) {
  return new QList<QGeoRoute>(self->routes());
}

//  void QGeoRouteReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoRouteReply5abortEv(QGeoRouteReply *self) {
  self->abort();
}

//  QGeoRouteReply::QGeoRouteReply(const QGeoRouteRequest &request, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoRouteReply *ritual_ZN14QGeoRouteReplyC1ERK16QGeoRouteRequestP7QObject(
    const QGeoRouteRequest *request,
    QObject *parent) {
  return new CuteQGeoRouteReply(*request, parent);
}

//  void QGeoRouteReply::setError(Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoRouteReply8setErrorENS_5ErrorERK7QString(
    QGeoRouteReply *self,
    QGeoRouteReply::Error error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QGeoRouteReply::setFinished(bool finished)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoRouteReply11setFinishedEb(
    QGeoRouteReply *self,
    bool finished) {
  self->setFinished(finished);
}

//  void QGeoRouteReply::setRoutes(const QList<QGeoRoute> &routes)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoRouteReply9setRoutesERK5QListI9QGeoRouteE(
    QGeoRouteReply *self,
    const QList<QGeoRoute> *routes) {
  self->setRoutes(*routes);
}

//  void QGeoRouteReply::addRoutes(const QList<QGeoRoute> &routes)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoRouteReply9addRoutesERK5QListI9QGeoRouteE(
    QGeoRouteReply *self,
    const QList<QGeoRoute> *routes) {
  self->addRoutes(*routes);
}

//  a Python function taken by a CuteQGeoRouteReply, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRouteReply(
    QGeoRouteReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRouteReply *>(self)->take(key, call);
}

//  void QGeoRouteReply::abort()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGeoRouteReply5abortEv(QGeoRouteReply *self) {
  self->QGeoRouteReply::abort();
}
