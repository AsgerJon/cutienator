//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeorouteparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtLocation/qgeorouterequest.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGeoRouteParser that Python can take functions over in. Every QGeoRouteParser
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRouteParserCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoRouteParserCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoRouteParserCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoRouteParser : public QGeoRouteParser {
public:
  using QGeoRouteParser::QGeoRouteParser;
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
      CuteQGeoRouteParserCall0 call = reinterpret_cast<CuteQGeoRouteParserCall0>(taken[0]);
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
      CuteQGeoRouteParserCall1 call = reinterpret_cast<CuteQGeoRouteParserCall1>(taken[1]);
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
      CuteQGeoRouteParserCall2 call = reinterpret_cast<CuteQGeoRouteParserCall2>(taken[2]);
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
      CuteQGeoRouteParserCall3 call = reinterpret_cast<CuteQGeoRouteParserCall3>(taken[3]);
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
      CuteQGeoRouteParserCall4 call = reinterpret_cast<CuteQGeoRouteParserCall4>(taken[4]);
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
      CuteQGeoRouteParserCall5 call = reinterpret_cast<CuteQGeoRouteParserCall5>(taken[5]);
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
      CuteQGeoRouteParserCall6 call = reinterpret_cast<CuteQGeoRouteParserCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoRouteParser::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGeoRouteParser10metaObjectEv(
    const QGeoRouteParser *self) {
  return self->metaObject();
}

//  void *QGeoRouteParser::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QGeoRouteParser11qt_metacastEPKc(
    QGeoRouteParser *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGeoRouteParser::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QGeoRouteParser11qt_metacallEN11QMetaObject4CallEiPPv(
    QGeoRouteParser *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QGeoRouteParser::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGeoRouteParser2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoRouteParser::tr(s, c, n));
}

//  QGeoRouteParserPrivate *QGeoRouteParser::d_func()
extern "C" Q_DECL_EXPORT
QGeoRouteParserPrivate *ritual_ZN15QGeoRouteParser6d_funcEv(
    QGeoRouteParser *self) {
  return self->d_func();
}

//  const QGeoRouteParserPrivate *QGeoRouteParser::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoRouteParserPrivate *ritual_ZNK15QGeoRouteParser6d_funcEv(
    const QGeoRouteParser *self) {
  return self->d_func();
}

//  QGeoRouteParser::~QGeoRouteParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoRouteParserD1Ev(QGeoRouteParser *self) {
  delete self;
}

//  QGeoRouteReply::Error QGeoRouteParser::parseReply(QList<QGeoRoute>
//      &routes, QString &errorString, const QByteArray &reply) const
extern "C" Q_DECL_EXPORT
QGeoRouteReply::Error ritual_ZNK15QGeoRouteParser10parseReplyER5QListI9QGeoRouteER7QStringRK10QByteArray(
    const QGeoRouteParser *self,
    QList<QGeoRoute> *routes,
    QString *errorString,
    const QByteArray *reply) {
  return self->parseReply(*routes, *errorString, *reply);
}

//  QUrl QGeoRouteParser::requestUrl(const QGeoRouteRequest &request, const
//      QString &prefix) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QGeoRouteParser10requestUrlERK16QGeoRouteRequestRK7QString(
    const QGeoRouteParser *self,
    const QGeoRouteRequest *request,
    const QString *prefix) {
  return new QUrl(self->requestUrl(*request, *prefix));
}

//  TrafficSide QGeoRouteParser::trafficSide() const
extern "C" Q_DECL_EXPORT
QGeoRouteParser::TrafficSide ritual_ZNK15QGeoRouteParser11trafficSideEv(
    const QGeoRouteParser *self) {
  return self->trafficSide();
}

//  void QGeoRouteParser::setTrafficSide(TrafficSide trafficSide)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoRouteParser14setTrafficSideENS_11TrafficSideE(
    QGeoRouteParser *self,
    QGeoRouteParser::TrafficSide trafficSide) {
  self->setTrafficSide(trafficSide);
}

//  void QGeoRouteParser::trafficSideChanged(TrafficSide trafficSide)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGeoRouteParser18trafficSideChangedENS_11TrafficSideE(
    QGeoRouteParser *self,
    QGeoRouteParser::TrafficSide trafficSide) {
  self->trafficSideChanged(trafficSide);
}

//  QGeoRouteParser::QGeoRouteParser(QGeoRouteParserPrivate &dd, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoRouteParser *ritual_ZN15QGeoRouteParserC1ER22QGeoRouteParserPrivateP7QObject(
    QGeoRouteParserPrivate *dd,
    QObject *parent) {
  return new CuteQGeoRouteParser(*dd, parent);
}

//  a Python function taken by a CuteQGeoRouteParser, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoRouteParser(
    QGeoRouteParser *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoRouteParser *>(self)->take(key, call);
}
