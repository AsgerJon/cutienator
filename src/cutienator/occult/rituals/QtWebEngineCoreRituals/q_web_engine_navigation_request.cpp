//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginenavigationrequest.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginenavigationrequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWebEngineNavigationRequest that Python can take functions over in. Every QWebEngineNavigationRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineNavigationRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineNavigationRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNavigationRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNavigationRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNavigationRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNavigationRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineNavigationRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineNavigationRequest : public QWebEngineNavigationRequest {
public:
  using QWebEngineNavigationRequest::QWebEngineNavigationRequest;
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
      CuteQWebEngineNavigationRequestCall0 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall0>(taken[0]);
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
      CuteQWebEngineNavigationRequestCall1 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall1>(taken[1]);
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
      CuteQWebEngineNavigationRequestCall2 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall2>(taken[2]);
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
      CuteQWebEngineNavigationRequestCall3 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall3>(taken[3]);
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
      CuteQWebEngineNavigationRequestCall4 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall4>(taken[4]);
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
      CuteQWebEngineNavigationRequestCall5 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall5>(taken[5]);
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
      CuteQWebEngineNavigationRequestCall6 call = reinterpret_cast<CuteQWebEngineNavigationRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineNavigationRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QWebEngineNavigationRequest10metaObjectEv(
    const QWebEngineNavigationRequest *self) {
  return self->metaObject();
}

//  void *QWebEngineNavigationRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QWebEngineNavigationRequest11qt_metacastEPKc(
    QWebEngineNavigationRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineNavigationRequest::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QWebEngineNavigationRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineNavigationRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineNavigationRequest::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QWebEngineNavigationRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineNavigationRequest::tr(s, c, n));
}

//  QWebEngineNavigationRequest::~QWebEngineNavigationRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineNavigationRequestD1Ev(
    QWebEngineNavigationRequest *self) {
  delete self;
}

//  QUrl QWebEngineNavigationRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK27QWebEngineNavigationRequest3urlEv(
    const QWebEngineNavigationRequest *self) {
  return new QUrl(self->url());
}

//  bool QWebEngineNavigationRequest::isMainFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebEngineNavigationRequest11isMainFrameEv(
    const QWebEngineNavigationRequest *self) {
  return self->isMainFrame();
}

//  bool QWebEngineNavigationRequest::hasFormData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebEngineNavigationRequest11hasFormDataEv(
    const QWebEngineNavigationRequest *self) {
  return self->hasFormData();
}

//  NavigationType QWebEngineNavigationRequest::navigationType() const
extern "C" Q_DECL_EXPORT
QWebEngineNavigationRequest::NavigationType ritual_ZNK27QWebEngineNavigationRequest14navigationTypeEv(
    const QWebEngineNavigationRequest *self) {
  return self->navigationType();
}

//  bool QWebEngineNavigationRequest::isUserInitiated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebEngineNavigationRequest15isUserInitiatedEv(
    const QWebEngineNavigationRequest *self) {
  return self->isUserInitiated();
}

//  void QWebEngineNavigationRequest::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineNavigationRequest6acceptEv(
    QWebEngineNavigationRequest *self) {
  self->accept();
}

//  void QWebEngineNavigationRequest::reject()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineNavigationRequest6rejectEv(
    QWebEngineNavigationRequest *self) {
  self->reject();
}

#if QT_DEPRECATED_SINCE(6, 2)
//  NavigationRequestAction QWebEngineNavigationRequest::action() const
extern "C" Q_DECL_EXPORT
QWebEngineNavigationRequest::NavigationRequestAction ritual_ZNK27QWebEngineNavigationRequest6actionEv(
    const QWebEngineNavigationRequest *self) {
  return self->action();
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

#if QT_DEPRECATED_SINCE(6, 2)
//  void QWebEngineNavigationRequest::setAction(NavigationRequestAction
//      action)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineNavigationRequest9setActionENS_23NavigationRequestActionE(
    QWebEngineNavigationRequest *self,
    QWebEngineNavigationRequest::NavigationRequestAction action) {
  self->setAction(action);
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

#if QT_DEPRECATED_SINCE(6, 2)
//  void QWebEngineNavigationRequest::actionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QWebEngineNavigationRequest13actionChangedEv(
    QWebEngineNavigationRequest *self) {
  self->actionChanged();
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

//  QWebEngineNavigationRequest::QWebEngineNavigationRequest(const QUrl &url,
//      NavigationType navigationType, bool mainFrame, bool formData, bool
//      userInitiated, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebEngineNavigationRequest *ritual_ZN27QWebEngineNavigationRequestC1ERK4QUrlNS_14NavigationTypeEbbbP7QObject(
    const QUrl *url,
    QWebEngineNavigationRequest::NavigationType navigationType,
    bool mainFrame,
    bool formData,
    bool userInitiated,
    QObject *parent) {
  return new CuteQWebEngineNavigationRequest(
      *url,
      navigationType,
      mainFrame,
      formData,
      userInitiated,
      parent);
}

//  bool QWebEngineNavigationRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QWebEngineNavigationRequest10isAcceptedEv(
    const QWebEngineNavigationRequest *self) {
  return self->isAccepted();
}

//  QWebEngineNavigationRequestPrivate *QWebEngineNavigationRequest::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineNavigationRequestPrivate *ritual_ZN27QWebEngineNavigationRequest6d_funcEv(
    QWebEngineNavigationRequest *self) {
  return self->d_func();
}

//  const QWebEngineNavigationRequestPrivate
//      *QWebEngineNavigationRequest::d_func() const
extern "C" Q_DECL_EXPORT
const QWebEngineNavigationRequestPrivate *ritual_ZNK27QWebEngineNavigationRequest6d_funcEv(
    const QWebEngineNavigationRequest *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQWebEngineNavigationRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineNavigationRequest(
    QWebEngineNavigationRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineNavigationRequest *>(self)->take(key, call);
}
