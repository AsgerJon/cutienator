//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickWebEngineTooltipRequest that Python can take functions over in. Every QQuickWebEngineTooltipRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineTooltipRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineTooltipRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTooltipRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTooltipRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTooltipRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTooltipRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineTooltipRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineTooltipRequest : public QQuickWebEngineTooltipRequest {
public:
  using QQuickWebEngineTooltipRequest::QQuickWebEngineTooltipRequest;
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
      CuteQQuickWebEngineTooltipRequestCall0 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall0>(taken[0]);
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
      CuteQQuickWebEngineTooltipRequestCall1 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall1>(taken[1]);
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
      CuteQQuickWebEngineTooltipRequestCall2 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall2>(taken[2]);
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
      CuteQQuickWebEngineTooltipRequestCall3 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall3>(taken[3]);
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
      CuteQQuickWebEngineTooltipRequestCall4 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall4>(taken[4]);
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
      CuteQQuickWebEngineTooltipRequestCall5 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall5>(taken[5]);
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
      CuteQQuickWebEngineTooltipRequestCall6 call = reinterpret_cast<CuteQQuickWebEngineTooltipRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineTooltipRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickWebEngineTooltipRequest10metaObjectEv(
    const QQuickWebEngineTooltipRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineTooltipRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuickWebEngineTooltipRequest11qt_metacastEPKc(
    QQuickWebEngineTooltipRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineTooltipRequest::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuickWebEngineTooltipRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineTooltipRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineTooltipRequest::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickWebEngineTooltipRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineTooltipRequest::tr(s, c, n));
}

//  void QQuickWebEngineTooltipRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickWebEngineTooltipRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineTooltipRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineTooltipRequest::~QQuickWebEngineTooltipRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickWebEngineTooltipRequestD1Ev(
    QQuickWebEngineTooltipRequest *self) {
  delete self;
}

//  int QQuickWebEngineTooltipRequest::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickWebEngineTooltipRequest1xEv(
    const QQuickWebEngineTooltipRequest *self) {
  return self->x();
}

//  int QQuickWebEngineTooltipRequest::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickWebEngineTooltipRequest1yEv(
    const QQuickWebEngineTooltipRequest *self) {
  return self->y();
}

//  QString QQuickWebEngineTooltipRequest::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QQuickWebEngineTooltipRequest4textEv(
    const QQuickWebEngineTooltipRequest *self) {
  return new QString(self->text());
}

//  RequestType QQuickWebEngineTooltipRequest::type() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineTooltipRequest::RequestType ritual_ZNK29QQuickWebEngineTooltipRequest4typeEv(
    const QQuickWebEngineTooltipRequest *self) {
  return self->type();
}

//  bool QQuickWebEngineTooltipRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuickWebEngineTooltipRequest10isAcceptedEv(
    const QQuickWebEngineTooltipRequest *self) {
  return self->isAccepted();
}

//  void QQuickWebEngineTooltipRequest::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickWebEngineTooltipRequest11setAcceptedEb(
    QQuickWebEngineTooltipRequest *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QQuickWebEngineTooltipRequest::QQuickWebEngineTooltipRequest(const
//      QString &text, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineTooltipRequest *ritual_ZN29QQuickWebEngineTooltipRequestC1ERK7QStringP7QObject(
    const QString *text,
    QObject *parent) {
  return new CuteQQuickWebEngineTooltipRequest(*text, parent);
}

//  a Python function taken by a CuteQQuickWebEngineTooltipRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineTooltipRequest(
    QQuickWebEngineTooltipRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineTooltipRequest *>(self)->take(key, call);
}
