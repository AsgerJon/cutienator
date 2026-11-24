//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpcmetadata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpcQuick/QtGrpcQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpcmetadata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QQmlGrpcMetadata that Python can take functions over in. Every QQmlGrpcMetadata
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcMetadataCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcMetadataCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcMetadataCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcMetadataCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcMetadataCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcMetadataCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcMetadataCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlGrpcMetadata : public QQmlGrpcMetadata {
public:
  using QQmlGrpcMetadata::QQmlGrpcMetadata;
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
      CuteQQmlGrpcMetadataCall0 call = reinterpret_cast<CuteQQmlGrpcMetadataCall0>(taken[0]);
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
      CuteQQmlGrpcMetadataCall1 call = reinterpret_cast<CuteQQmlGrpcMetadataCall1>(taken[1]);
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
      CuteQQmlGrpcMetadataCall2 call = reinterpret_cast<CuteQQmlGrpcMetadataCall2>(taken[2]);
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
      CuteQQmlGrpcMetadataCall3 call = reinterpret_cast<CuteQQmlGrpcMetadataCall3>(taken[3]);
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
      CuteQQmlGrpcMetadataCall4 call = reinterpret_cast<CuteQQmlGrpcMetadataCall4>(taken[4]);
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
      CuteQQmlGrpcMetadataCall5 call = reinterpret_cast<CuteQQmlGrpcMetadataCall5>(taken[5]);
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
      CuteQQmlGrpcMetadataCall6 call = reinterpret_cast<CuteQQmlGrpcMetadataCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlGrpcMetadata::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlGrpcMetadata10metaObjectEv(
    const QQmlGrpcMetadata *self) {
  return self->metaObject();
}

//  QString QQmlGrpcMetadata::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlGrpcMetadata2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlGrpcMetadata::tr(s, c, n));
}

//  QQmlGrpcMetadata::QQmlGrpcMetadata(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlGrpcMetadata *ritual_ZN16QQmlGrpcMetadataC1EP7QObject(QObject *parent) {
  return new CuteQQmlGrpcMetadata(parent);
}

//  QQmlGrpcMetadata::~QQmlGrpcMetadata()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlGrpcMetadataD1Ev(QQmlGrpcMetadata *self) {
  delete self;
}

//  const QVariantMap &QQmlGrpcMetadata::data() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK16QQmlGrpcMetadata4dataEv(
    const QQmlGrpcMetadata *self) {
  return new QMap<QString, QVariant>(self->data());
}

//  void QQmlGrpcMetadata::setData(const QVariantMap &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlGrpcMetadata7setDataERK4QMapI7QString8QVariantE(
    QQmlGrpcMetadata *self,
    const QMap<QString, QVariant> *data) {
  self->setData(*data);
}

//  a Python function taken by a CuteQQmlGrpcMetadata, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGrpcMetadata(
    QQmlGrpcMetadata *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGrpcMetadata *>(self)->take(key, call);
}
