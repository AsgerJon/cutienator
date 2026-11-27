//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  A QQuickWebEngineColorDialogRequest that Python can take functions over in. Every QQuickWebEngineColorDialogRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineColorDialogRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineColorDialogRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineColorDialogRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineColorDialogRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineColorDialogRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineColorDialogRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineColorDialogRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineColorDialogRequest : public QQuickWebEngineColorDialogRequest {
public:
  using QQuickWebEngineColorDialogRequest::QQuickWebEngineColorDialogRequest;
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
      CuteQQuickWebEngineColorDialogRequestCall0 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall0>(taken[0]);
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
      CuteQQuickWebEngineColorDialogRequestCall1 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall1>(taken[1]);
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
      CuteQQuickWebEngineColorDialogRequestCall2 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall2>(taken[2]);
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
      CuteQQuickWebEngineColorDialogRequestCall3 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall3>(taken[3]);
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
      CuteQQuickWebEngineColorDialogRequestCall4 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall4>(taken[4]);
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
      CuteQQuickWebEngineColorDialogRequestCall5 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall5>(taken[5]);
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
      CuteQQuickWebEngineColorDialogRequestCall6 call = reinterpret_cast<CuteQQuickWebEngineColorDialogRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineColorDialogRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK33QQuickWebEngineColorDialogRequest10metaObjectEv(
    const QQuickWebEngineColorDialogRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineColorDialogRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN33QQuickWebEngineColorDialogRequest11qt_metacastEPKc(
    QQuickWebEngineColorDialogRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineColorDialogRequest::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN33QQuickWebEngineColorDialogRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineColorDialogRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineColorDialogRequest::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN33QQuickWebEngineColorDialogRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineColorDialogRequest::tr(s, c, n));
}

//  void QQuickWebEngineColorDialogRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickWebEngineColorDialogRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineColorDialogRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineColorDialogRequest::~QQuickWebEngineColorDialogRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickWebEngineColorDialogRequestD1Ev(
    QQuickWebEngineColorDialogRequest *self) {
  delete self;
}

//  QColor QQuickWebEngineColorDialogRequest::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK33QQuickWebEngineColorDialogRequest5colorEv(
    const QQuickWebEngineColorDialogRequest *self) {
  return new QColor(self->color());
}

//  bool QQuickWebEngineColorDialogRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK33QQuickWebEngineColorDialogRequest10isAcceptedEv(
    const QQuickWebEngineColorDialogRequest *self) {
  return self->isAccepted();
}

//  void QQuickWebEngineColorDialogRequest::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickWebEngineColorDialogRequest11setAcceptedEb(
    QQuickWebEngineColorDialogRequest *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  void QQuickWebEngineColorDialogRequest::dialogAccept(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickWebEngineColorDialogRequest12dialogAcceptERK6QColor(
    QQuickWebEngineColorDialogRequest *self,
    const QColor *color) {
  self->dialogAccept(*color);
}

//  void QQuickWebEngineColorDialogRequest::dialogReject()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QQuickWebEngineColorDialogRequest12dialogRejectEv(
    QQuickWebEngineColorDialogRequest *self) {
  self->dialogReject();
}

//  QQuickWebEngineColorDialogRequest::QQuickWebEngineColorDialogRequest(QSha
//      redPointer<QtWebEngineCore::ColorChooserController> controller,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineColorDialogRequest *ritual_ZN33QQuickWebEngineColorDialogRequestC1E14QSharedPointerIN15QtWebEngineCore22ColorChooserControllerEEP7QObject(
    const QSharedPointer<QtWebEngineCore::ColorChooserController> *controller,
    QObject *parent) {
  return new CuteQQuickWebEngineColorDialogRequest(*controller, parent);
}

//  a Python function taken by a CuteQQuickWebEngineColorDialogRequest, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineColorDialogRequest(
    QQuickWebEngineColorDialogRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineColorDialogRequest *>(self)->take(key, call);
}
