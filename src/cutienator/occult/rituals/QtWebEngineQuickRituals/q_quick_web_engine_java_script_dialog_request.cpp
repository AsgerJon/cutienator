//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  A QQuickWebEngineJavaScriptDialogRequest that Python can take functions over in. Every QQuickWebEngineJavaScriptDialogRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineJavaScriptDialogRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineJavaScriptDialogRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineJavaScriptDialogRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineJavaScriptDialogRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineJavaScriptDialogRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineJavaScriptDialogRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineJavaScriptDialogRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineJavaScriptDialogRequest : public QQuickWebEngineJavaScriptDialogRequest {
public:
  using QQuickWebEngineJavaScriptDialogRequest::QQuickWebEngineJavaScriptDialogRequest;
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall0 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall0>(taken[0]);
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall1 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall1>(taken[1]);
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall2 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall2>(taken[2]);
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall3 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall3>(taken[3]);
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall4 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall4>(taken[4]);
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall5 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall5>(taken[5]);
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
      CuteQQuickWebEngineJavaScriptDialogRequestCall6 call = reinterpret_cast<CuteQQuickWebEngineJavaScriptDialogRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineJavaScriptDialogRequest::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest10metaObjectEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineJavaScriptDialogRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN38QQuickWebEngineJavaScriptDialogRequest11qt_metacastEPKc(
    QQuickWebEngineJavaScriptDialogRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineJavaScriptDialogRequest::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN38QQuickWebEngineJavaScriptDialogRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineJavaScriptDialogRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineJavaScriptDialogRequest::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN38QQuickWebEngineJavaScriptDialogRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineJavaScriptDialogRequest::tr(s, c, n));
}

//  void QQuickWebEngineJavaScriptDialogRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineJavaScriptDialogRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineJavaScriptDialogRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineJavaScriptDialogRequest::~QQuickWebEngineJavaScriptDialogR
//      equest()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineJavaScriptDialogRequestD1Ev(
    QQuickWebEngineJavaScriptDialogRequest *self) {
  delete self;
}

//  QString QQuickWebEngineJavaScriptDialogRequest::message() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest7messageEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return new QString(self->message());
}

//  QString QQuickWebEngineJavaScriptDialogRequest::defaultText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest11defaultTextEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return new QString(self->defaultText());
}

//  QString QQuickWebEngineJavaScriptDialogRequest::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest5titleEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return new QString(self->title());
}

//  DialogType QQuickWebEngineJavaScriptDialogRequest::type() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineJavaScriptDialogRequest::DialogType ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest4typeEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return self->type();
}

//  QUrl QQuickWebEngineJavaScriptDialogRequest::securityOrigin() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest14securityOriginEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return new QUrl(self->securityOrigin());
}

//  bool QQuickWebEngineJavaScriptDialogRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QQuickWebEngineJavaScriptDialogRequest10isAcceptedEv(
    const QQuickWebEngineJavaScriptDialogRequest *self) {
  return self->isAccepted();
}

//  void QQuickWebEngineJavaScriptDialogRequest::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineJavaScriptDialogRequest11setAcceptedEb(
    QQuickWebEngineJavaScriptDialogRequest *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  void QQuickWebEngineJavaScriptDialogRequest::dialogAccept(const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineJavaScriptDialogRequest12dialogAcceptERK7QString(
    QQuickWebEngineJavaScriptDialogRequest *self,
    const QString *text) {
  self->dialogAccept(*text);
}

//  void QQuickWebEngineJavaScriptDialogRequest::dialogReject()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickWebEngineJavaScriptDialogRequest12dialogRejectEv(
    QQuickWebEngineJavaScriptDialogRequest *self) {
  self->dialogReject();
}

//  QQuickWebEngineJavaScriptDialogRequest::QQuickWebEngineJavaScriptDialogRe
//      quest(QSharedPointer<QtWebEngineCore::JavaScriptDialogController>
//      controller, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineJavaScriptDialogRequest *ritual_ZN38QQuickWebEngineJavaScriptDialogRequestC1E14QSharedPointerIN15QtWebEngineCore26JavaScriptDialogControllerEEP7QObject(
    const QSharedPointer<QtWebEngineCore::JavaScriptDialogController> *controller,
    QObject *parent) {
  return new CuteQQuickWebEngineJavaScriptDialogRequest(*controller, parent);
}

//  a Python function taken by a CuteQQuickWebEngineJavaScriptDialogRequest,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineJavaScriptDialogRequest(
    QQuickWebEngineJavaScriptDialogRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineJavaScriptDialogRequest *>(self)->take(key, call);
}
