//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpcchanneloptions_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpcQuick/QtGrpcQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpcchanneloptions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGrpc/qgrpcchanneloptions.h>
#if QT_CONFIG(qml_ssl)
#include <QtQmlNetwork/QtQmlNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlGrpcChannelOptions that Python can take functions over in. Every QQmlGrpcChannelOptions
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcChannelOptionsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlGrpcChannelOptionsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcChannelOptionsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcChannelOptionsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcChannelOptionsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcChannelOptionsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlGrpcChannelOptionsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlGrpcChannelOptions : public QQmlGrpcChannelOptions {
public:
  using QQmlGrpcChannelOptions::QQmlGrpcChannelOptions;
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
      CuteQQmlGrpcChannelOptionsCall0 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall0>(taken[0]);
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
      CuteQQmlGrpcChannelOptionsCall1 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall1>(taken[1]);
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
      CuteQQmlGrpcChannelOptionsCall2 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall2>(taken[2]);
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
      CuteQQmlGrpcChannelOptionsCall3 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall3>(taken[3]);
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
      CuteQQmlGrpcChannelOptionsCall4 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall4>(taken[4]);
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
      CuteQQmlGrpcChannelOptionsCall5 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall5>(taken[5]);
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
      CuteQQmlGrpcChannelOptionsCall6 call = reinterpret_cast<CuteQQmlGrpcChannelOptionsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlGrpcChannelOptions::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlGrpcChannelOptions10metaObjectEv(
    const QQmlGrpcChannelOptions *self) {
  return self->metaObject();
}

//  void *QQmlGrpcChannelOptions::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQmlGrpcChannelOptions11qt_metacastEPKc(
    QQmlGrpcChannelOptions *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlGrpcChannelOptions::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlGrpcChannelOptions11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlGrpcChannelOptions *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlGrpcChannelOptions::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQmlGrpcChannelOptions2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlGrpcChannelOptions::tr(s, c, n));
}

//  QQmlGrpcChannelOptions::QQmlGrpcChannelOptions(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlGrpcChannelOptions *ritual_ZN22QQmlGrpcChannelOptionsC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlGrpcChannelOptions(parent);
}

//  QQmlGrpcChannelOptions::~QQmlGrpcChannelOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptionsD1Ev(QQmlGrpcChannelOptions *self) {
  delete self;
}

//  const QGrpcChannelOptions &QQmlGrpcChannelOptions::options() const
extern "C" Q_DECL_EXPORT
QGrpcChannelOptions *ritual_ZNKR22QQmlGrpcChannelOptions7optionsEv(
    const QQmlGrpcChannelOptions *self) {
  return new QGrpcChannelOptions(self->options());
}

//  qint64 QQmlGrpcChannelOptions::deadlineTimeout() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QQmlGrpcChannelOptions15deadlineTimeoutEv(
    const QQmlGrpcChannelOptions *self) {
  return self->deadlineTimeout();
}

//  void QQmlGrpcChannelOptions::setDeadlineTimeout(qint64 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions18setDeadlineTimeoutEx(
    QQmlGrpcChannelOptions *self,
    qint64 value) {
  self->setDeadlineTimeout(value);
}

//  QQmlGrpcMetadata *QQmlGrpcChannelOptions::metadata() const
extern "C" Q_DECL_EXPORT
QQmlGrpcMetadata *ritual_ZNK22QQmlGrpcChannelOptions8metadataEv(
    const QQmlGrpcChannelOptions *self) {
  return self->metadata();
}

//  void QQmlGrpcChannelOptions::setMetadata(QQmlGrpcMetadata *value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions11setMetadataEP16QQmlGrpcMetadata(
    QQmlGrpcChannelOptions *self,
    QQmlGrpcMetadata *value) {
  self->setMetadata(value);
}

//  QtGrpc::SerializationFormat QQmlGrpcChannelOptions::serializationFormat()
//      const
extern "C" Q_DECL_EXPORT
QtGrpc::SerializationFormat ritual_ZNK22QQmlGrpcChannelOptions19serializationFormatEv(
    const QQmlGrpcChannelOptions *self) {
  return self->serializationFormat();
}

//  void QQmlGrpcChannelOptions::setSerializationFormat(QtGrpc::Serialization
//      Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions22setSerializationFormatEN6QtGrpc19SerializationFormatE(
    QQmlGrpcChannelOptions *self,
    QtGrpc::SerializationFormat format) {
  self->setSerializationFormat(format);
}

#if QT_CONFIG(ssl)
//  QQmlSslConfiguration QQmlGrpcChannelOptions::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QQmlSslConfiguration *ritual_ZNK22QQmlGrpcChannelOptions16sslConfigurationEv(
    const QQmlGrpcChannelOptions *self) {
  return new QQmlSslConfiguration(self->sslConfiguration());
}
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
//  void QQmlGrpcChannelOptions::setSslConfiguration(const
//      QQmlSslConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions19setSslConfigurationERK20QQmlSslConfiguration(
    QQmlGrpcChannelOptions *self,
    const QQmlSslConfiguration *config) {
  self->setSslConfiguration(*config);
}
#endif  // QT_CONFIG(ssl)

//  void QQmlGrpcChannelOptions::deadlineTimeoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions22deadlineTimeoutChangedEv(
    QQmlGrpcChannelOptions *self) {
  self->deadlineTimeoutChanged();
}

//  void QQmlGrpcChannelOptions::metadataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions15metadataChangedEv(
    QQmlGrpcChannelOptions *self) {
  self->metadataChanged();
}

//  void QQmlGrpcChannelOptions::serializationFormatChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions26serializationFormatChangedEv(
    QQmlGrpcChannelOptions *self) {
  self->serializationFormatChanged();
}

#if QT_CONFIG(ssl)
//  void QQmlGrpcChannelOptions::sslConfigurationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGrpcChannelOptions23sslConfigurationChangedEv(
    QQmlGrpcChannelOptions *self) {
  self->sslConfigurationChanged();
}
#endif  // QT_CONFIG(ssl)

//  QQmlGrpcChannelOptionsPrivate *QQmlGrpcChannelOptions::d_func()
extern "C" Q_DECL_EXPORT
QQmlGrpcChannelOptionsPrivate *ritual_ZN22QQmlGrpcChannelOptions6d_funcEv(
    QQmlGrpcChannelOptions *self) {
  return self->d_func();
}

//  const QQmlGrpcChannelOptionsPrivate *QQmlGrpcChannelOptions::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlGrpcChannelOptionsPrivate *ritual_ZNK22QQmlGrpcChannelOptions6d_funcEv(
    const QQmlGrpcChannelOptions *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQmlGrpcChannelOptions, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlGrpcChannelOptions(
    QQmlGrpcChannelOptions *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlGrpcChannelOptions *>(self)->take(key, call);
}
