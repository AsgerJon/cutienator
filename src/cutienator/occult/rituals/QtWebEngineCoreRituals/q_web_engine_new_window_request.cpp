//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginenewwindowrequest.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginenewwindowrequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QRect>
#include <QtCore/QUrl>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  A QWebEngineNewWindowRequest that Python can take functions over in. Every QWebEngineNewWindowRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineNewWindowRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineNewWindowRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNewWindowRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNewWindowRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNewWindowRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNewWindowRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNewWindowRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineNewWindowRequest : public QWebEngineNewWindowRequest {
public:
  using QWebEngineNewWindowRequest::QWebEngineNewWindowRequest;
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
      CuteQWebEngineNewWindowRequestCall0 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall0>(taken[0]);
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
      CuteQWebEngineNewWindowRequestCall1 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall1>(taken[1]);
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
      CuteQWebEngineNewWindowRequestCall2 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall2>(taken[2]);
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
      CuteQWebEngineNewWindowRequestCall3 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall3>(taken[3]);
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
      CuteQWebEngineNewWindowRequestCall4 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall4>(taken[4]);
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
      CuteQWebEngineNewWindowRequestCall5 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall5>(taken[5]);
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
      CuteQWebEngineNewWindowRequestCall6 call = reinterpret_cast<CuteQWebEngineNewWindowRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineNewWindowRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWebEngineNewWindowRequest10metaObjectEv(
    const QWebEngineNewWindowRequest *self) {
  return self->metaObject();
}

//  void *QWebEngineNewWindowRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWebEngineNewWindowRequest11qt_metacastEPKc(
    QWebEngineNewWindowRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineNewWindowRequest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWebEngineNewWindowRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineNewWindowRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineNewWindowRequest::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWebEngineNewWindowRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineNewWindowRequest::tr(s, c, n));
}

//  QWebEngineNewWindowRequest::~QWebEngineNewWindowRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineNewWindowRequestD1Ev(
    QWebEngineNewWindowRequest *self) {
  delete self;
}

//  DestinationType QWebEngineNewWindowRequest::destination() const
extern "C" Q_DECL_EXPORT
QWebEngineNewWindowRequest::DestinationType ritual_ZNK26QWebEngineNewWindowRequest11destinationEv(
    const QWebEngineNewWindowRequest *self) {
  return self->destination();
}

//  QUrl QWebEngineNewWindowRequest::requestedUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK26QWebEngineNewWindowRequest12requestedUrlEv(
    const QWebEngineNewWindowRequest *self) {
  return new QUrl(self->requestedUrl());
}

//  QRect QWebEngineNewWindowRequest::requestedGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK26QWebEngineNewWindowRequest17requestedGeometryEv(
    const QWebEngineNewWindowRequest *self) {
  return new QRect(self->requestedGeometry());
}

//  bool QWebEngineNewWindowRequest::isUserInitiated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebEngineNewWindowRequest15isUserInitiatedEv(
    const QWebEngineNewWindowRequest *self) {
  return self->isUserInitiated();
}

//  void QWebEngineNewWindowRequest::openIn(QWebEnginePage *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineNewWindowRequest6openInEP14QWebEnginePage(
    QWebEngineNewWindowRequest *self,
    QWebEnginePage *a0) {
  self->openIn(a0);
}

//  QWebEngineNewWindowRequest::QWebEngineNewWindowRequest(DestinationType
//      a0, const QRect &a1, const QUrl &a2, bool a3,
//      QSharedPointer<QtWebEngineCore::WebContentsAdapter> a4, QObject *a5)
extern "C" Q_DECL_EXPORT
QWebEngineNewWindowRequest *ritual_ZN26QWebEngineNewWindowRequestC1ENS_15DestinationTypeERK5QRectRK4QUrlb14QSharedPointerIN15QtWebEngineCore18WebContentsAdapterEEP7QObject(
    QWebEngineNewWindowRequest::DestinationType a0,
    const QRect *a1,
    const QUrl *a2,
    bool a3,
    const QSharedPointer<QtWebEngineCore::WebContentsAdapter> *a4,
    QObject *a5) {
  return new CuteQWebEngineNewWindowRequest(a0, *a1, *a2, a3, *a4, a5);
}

//  a Python function taken by a CuteQWebEngineNewWindowRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineNewWindowRequest(
    QWebEngineNewWindowRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineNewWindowRequest *>(self)->take(key, call);
}
