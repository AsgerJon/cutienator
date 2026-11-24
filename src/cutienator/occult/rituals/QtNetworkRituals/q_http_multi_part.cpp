//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhttpmultipart.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(http)
#include <QtNetwork/qhttpmultipart.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QHttpMultiPart that Python can take functions over in. Every QHttpMultiPart
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpMultiPartCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpMultiPartCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpMultiPartCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpMultiPart : public QHttpMultiPart {
public:
  using QHttpMultiPart::QHttpMultiPart;
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
      CuteQHttpMultiPartCall0 call = reinterpret_cast<CuteQHttpMultiPartCall0>(taken[0]);
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
      CuteQHttpMultiPartCall1 call = reinterpret_cast<CuteQHttpMultiPartCall1>(taken[1]);
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
      CuteQHttpMultiPartCall2 call = reinterpret_cast<CuteQHttpMultiPartCall2>(taken[2]);
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
      CuteQHttpMultiPartCall3 call = reinterpret_cast<CuteQHttpMultiPartCall3>(taken[3]);
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
      CuteQHttpMultiPartCall4 call = reinterpret_cast<CuteQHttpMultiPartCall4>(taken[4]);
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
      CuteQHttpMultiPartCall5 call = reinterpret_cast<CuteQHttpMultiPartCall5>(taken[5]);
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
      CuteQHttpMultiPartCall6 call = reinterpret_cast<CuteQHttpMultiPartCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttpMultiPart::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QHttpMultiPart10metaObjectEv(
    const QHttpMultiPart *self) {
  return self->metaObject();
}

//  QString QHttpMultiPart::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QHttpMultiPart2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHttpMultiPart::tr(s, c, n));
}

//  QHttpMultiPart::QHttpMultiPart(QObject *parent)
extern "C" Q_DECL_EXPORT
QHttpMultiPart *ritual_ZN14QHttpMultiPartC1EP7QObject(QObject *parent) {
  return new CuteQHttpMultiPart(parent);
}

//  QHttpMultiPart::QHttpMultiPart(ContentType contentType, QObject *parent)
extern "C" Q_DECL_EXPORT
QHttpMultiPart *ritual_ZN14QHttpMultiPartC1ENS_11ContentTypeEP7QObject(
    QHttpMultiPart::ContentType contentType,
    QObject *parent) {
  return new CuteQHttpMultiPart(contentType, parent);
}

//  QHttpMultiPart::~QHttpMultiPart()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHttpMultiPartD1Ev(QHttpMultiPart *self) {
  delete self;
}

//  void QHttpMultiPart::append(const QHttpPart &httpPart)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHttpMultiPart6appendERK9QHttpPart(
    QHttpMultiPart *self,
    const QHttpPart *httpPart) {
  self->append(*httpPart);
}

//  void QHttpMultiPart::setContentType(ContentType contentType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHttpMultiPart14setContentTypeENS_11ContentTypeE(
    QHttpMultiPart *self,
    QHttpMultiPart::ContentType contentType) {
  self->setContentType(contentType);
}

//  QByteArray QHttpMultiPart::boundary() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QHttpMultiPart8boundaryEv(
    const QHttpMultiPart *self) {
  return new QByteArray(self->boundary());
}

//  void QHttpMultiPart::setBoundary(const QByteArray &boundary)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QHttpMultiPart11setBoundaryERK10QByteArray(
    QHttpMultiPart *self,
    const QByteArray *boundary) {
  self->setBoundary(*boundary);
}

//  QHttpMultiPartPrivate *QHttpMultiPart::d_func()
extern "C" Q_DECL_EXPORT
QHttpMultiPartPrivate *ritual_ZN14QHttpMultiPart6d_funcEv(
    QHttpMultiPart *self) {
  return self->d_func();
}

//  const QHttpMultiPartPrivate *QHttpMultiPart::d_func() const
extern "C" Q_DECL_EXPORT
const QHttpMultiPartPrivate *ritual_ZNK14QHttpMultiPart6d_funcEv(
    const QHttpMultiPart *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHttpMultiPart, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpMultiPart(
    QHttpMultiPart *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpMultiPart *>(self)->take(key, call);
}

#endif  // QT_CONFIG(http)
