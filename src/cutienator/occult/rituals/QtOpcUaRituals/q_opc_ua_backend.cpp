//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/6.12.0/QtOpcUa/private/qopcuabackend_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/QtOpcUa>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpcUa/6.12.0/QtOpcUa/private/qopcuabackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpcUaBackend that Python can take functions over in. Every QOpcUaBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaBackendCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaBackendCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaBackendCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaBackend : public QOpcUaBackend {
public:
  using QOpcUaBackend::QOpcUaBackend;
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
      CuteQOpcUaBackendCall0 call = reinterpret_cast<CuteQOpcUaBackendCall0>(taken[0]);
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
      CuteQOpcUaBackendCall1 call = reinterpret_cast<CuteQOpcUaBackendCall1>(taken[1]);
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
      CuteQOpcUaBackendCall2 call = reinterpret_cast<CuteQOpcUaBackendCall2>(taken[2]);
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
      CuteQOpcUaBackendCall3 call = reinterpret_cast<CuteQOpcUaBackendCall3>(taken[3]);
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
      CuteQOpcUaBackendCall4 call = reinterpret_cast<CuteQOpcUaBackendCall4>(taken[4]);
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
      CuteQOpcUaBackendCall5 call = reinterpret_cast<CuteQOpcUaBackendCall5>(taken[5]);
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
      CuteQOpcUaBackendCall6 call = reinterpret_cast<CuteQOpcUaBackendCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaBackend::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QOpcUaBackend10metaObjectEv(
    const QOpcUaBackend *self) {
  return self->metaObject();
}

//  QString QOpcUaBackend::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QOpcUaBackend2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaBackend::tr(s, c, n));
}

//  QOpcUaBackend::QOpcUaBackend()
extern "C" Q_DECL_EXPORT
QOpcUaBackend *ritual_ZN13QOpcUaBackendC1Ev() {
  return new CuteQOpcUaBackend();
}

//  QOpcUaBackend::~QOpcUaBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaBackendD1Ev(QOpcUaBackend *self) {
  delete self;
}

//  QOpcUa::Types QOpcUaBackend::attributeIdToTypeId(QOpcUa::NodeAttribute
//      attr)
extern "C" Q_DECL_EXPORT
QOpcUa::Types ritual_ZN13QOpcUaBackend19attributeIdToTypeIdEN6QOpcUa13NodeAttributeE(
    QOpcUaBackend *self,
    QOpcUa::NodeAttribute attr) {
  return self->attributeIdToTypeId(attr);
}

//  double QOpcUaBackend::revisePublishingInterval(double requestedValue,
//      double minimumValue)
extern "C" Q_DECL_EXPORT
double ritual_ZN13QOpcUaBackend24revisePublishingIntervalEdd(
    QOpcUaBackend *self,
    double requestedValue,
    double minimumValue) {
  return self->revisePublishingInterval(requestedValue, minimumValue);
}

//  QOpcUaClient::ClientError QOpcUaBackend::verifyEndpointDescription(const
//      QOpcUaEndpointDescription &endpoint, QString *message)
extern "C" Q_DECL_EXPORT
QOpcUaClient::ClientError ritual_ZN13QOpcUaBackend25verifyEndpointDescriptionERK25QOpcUaEndpointDescriptionP7QString(
    const QOpcUaEndpointDescription *endpoint,
    QString *message) {
  return QOpcUaBackend::verifyEndpointDescription(*endpoint, message);
}

//  a Python function taken by a CuteQOpcUaBackend, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaBackend(
    QOpcUaBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaBackend *>(self)->take(key, call);
}
