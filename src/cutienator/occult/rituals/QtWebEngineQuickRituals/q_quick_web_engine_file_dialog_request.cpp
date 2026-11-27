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
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtWebEngineCore/QtWebEngineCore>

//  A QQuickWebEngineFileDialogRequest that Python can take functions over in. Every QQuickWebEngineFileDialogRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineFileDialogRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickWebEngineFileDialogRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFileDialogRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFileDialogRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFileDialogRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFileDialogRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickWebEngineFileDialogRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickWebEngineFileDialogRequest : public QQuickWebEngineFileDialogRequest {
public:
  using QQuickWebEngineFileDialogRequest::QQuickWebEngineFileDialogRequest;
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
      CuteQQuickWebEngineFileDialogRequestCall0 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall0>(taken[0]);
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
      CuteQQuickWebEngineFileDialogRequestCall1 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall1>(taken[1]);
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
      CuteQQuickWebEngineFileDialogRequestCall2 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall2>(taken[2]);
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
      CuteQQuickWebEngineFileDialogRequestCall3 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall3>(taken[3]);
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
      CuteQQuickWebEngineFileDialogRequestCall4 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall4>(taken[4]);
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
      CuteQQuickWebEngineFileDialogRequestCall5 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall5>(taken[5]);
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
      CuteQQuickWebEngineFileDialogRequestCall6 call = reinterpret_cast<CuteQQuickWebEngineFileDialogRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickWebEngineFileDialogRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickWebEngineFileDialogRequest10metaObjectEv(
    const QQuickWebEngineFileDialogRequest *self) {
  return self->metaObject();
}

//  void *QQuickWebEngineFileDialogRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickWebEngineFileDialogRequest11qt_metacastEPKc(
    QQuickWebEngineFileDialogRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickWebEngineFileDialogRequest::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickWebEngineFileDialogRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickWebEngineFileDialogRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickWebEngineFileDialogRequest::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN32QQuickWebEngineFileDialogRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickWebEngineFileDialogRequest::tr(s, c, n));
}

//  void QQuickWebEngineFileDialogRequest::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickWebEngineFileDialogRequest24qt_qmlMarker_uncreatableEv(
    QQuickWebEngineFileDialogRequest *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickWebEngineFileDialogRequest::~QQuickWebEngineFileDialogRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickWebEngineFileDialogRequestD1Ev(
    QQuickWebEngineFileDialogRequest *self) {
  delete self;
}

//  QStringList QQuickWebEngineFileDialogRequest::acceptedMimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK32QQuickWebEngineFileDialogRequest17acceptedMimeTypesEv(
    const QQuickWebEngineFileDialogRequest *self) {
  return new QList<QString>(self->acceptedMimeTypes());
}

//  QString QQuickWebEngineFileDialogRequest::defaultFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickWebEngineFileDialogRequest15defaultFileNameEv(
    const QQuickWebEngineFileDialogRequest *self) {
  return new QString(self->defaultFileName());
}

//  FileMode QQuickWebEngineFileDialogRequest::mode() const
extern "C" Q_DECL_EXPORT
QQuickWebEngineFileDialogRequest::FileMode ritual_ZNK32QQuickWebEngineFileDialogRequest4modeEv(
    const QQuickWebEngineFileDialogRequest *self) {
  return self->mode();
}

//  bool QQuickWebEngineFileDialogRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickWebEngineFileDialogRequest10isAcceptedEv(
    const QQuickWebEngineFileDialogRequest *self) {
  return self->isAccepted();
}

//  void QQuickWebEngineFileDialogRequest::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickWebEngineFileDialogRequest11setAcceptedEb(
    QQuickWebEngineFileDialogRequest *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  void QQuickWebEngineFileDialogRequest::dialogAccept(const QStringList
//      &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickWebEngineFileDialogRequest12dialogAcceptERK5QListI7QStringE(
    QQuickWebEngineFileDialogRequest *self,
    const QList<QString> *files) {
  self->dialogAccept(*files);
}

//  void QQuickWebEngineFileDialogRequest::dialogReject()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickWebEngineFileDialogRequest12dialogRejectEv(
    QQuickWebEngineFileDialogRequest *self) {
  self->dialogReject();
}

//  QQuickWebEngineFileDialogRequest::QQuickWebEngineFileDialogRequest(QShare
//      dPointer<QtWebEngineCore::FilePickerController> controller, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickWebEngineFileDialogRequest *ritual_ZN32QQuickWebEngineFileDialogRequestC1E14QSharedPointerIN15QtWebEngineCore20FilePickerControllerEEP7QObject(
    const QSharedPointer<QtWebEngineCore::FilePickerController> *controller,
    QObject *parent) {
  return new CuteQQuickWebEngineFileDialogRequest(*controller, parent);
}

//  a Python function taken by a CuteQQuickWebEngineFileDialogRequest, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWebEngineFileDialogRequest(
    QQuickWebEngineFileDialogRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWebEngineFileDialogRequest *>(self)->take(key, call);
}
