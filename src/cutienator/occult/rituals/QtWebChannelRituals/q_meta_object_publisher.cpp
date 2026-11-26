//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebChannel/6.12.0/QtWebChannel/private/qmetaobjectpublisher_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebChannel/QtWebChannel>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebChannel/6.12.0/QtWebChannel/private/qmetaobjectpublisher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qjsonvalue.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QMetaObjectPublisher may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMetaObjectPublisher : QMetaObjectPublisher {
  using QMetaObjectPublisher::timerEvent;
};

//  A QMetaObjectPublisher that Python can take functions over in. Every QMetaObjectPublisher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMetaObjectPublisherCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMetaObjectPublisherCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMetaObjectPublisherCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMetaObjectPublisherCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMetaObjectPublisherCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMetaObjectPublisherCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMetaObjectPublisherCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMetaObjectPublisher : public QMetaObjectPublisher {
public:
  using QMetaObjectPublisher::QMetaObjectPublisher;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
  //  void QMetaObjectPublisher::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMetaObjectPublisherCall0 call = reinterpret_cast<CuteQMetaObjectPublisherCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QMetaObjectPublisher::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMetaObjectPublisherCall1 call = reinterpret_cast<CuteQMetaObjectPublisherCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMetaObjectPublisherCall2 call = reinterpret_cast<CuteQMetaObjectPublisherCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMetaObjectPublisherCall3 call = reinterpret_cast<CuteQMetaObjectPublisherCall3>(taken[3]);
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
      CuteQMetaObjectPublisherCall4 call = reinterpret_cast<CuteQMetaObjectPublisherCall4>(taken[4]);
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
      CuteQMetaObjectPublisherCall5 call = reinterpret_cast<CuteQMetaObjectPublisherCall5>(taken[5]);
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
      CuteQMetaObjectPublisherCall6 call = reinterpret_cast<CuteQMetaObjectPublisherCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMetaObjectPublisher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QMetaObjectPublisher10metaObjectEv(
    const QMetaObjectPublisher *self) {
  return self->metaObject();
}

//  void *QMetaObjectPublisher::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QMetaObjectPublisher11qt_metacastEPKc(
    QMetaObjectPublisher *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMetaObjectPublisher::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QMetaObjectPublisher11qt_metacallEN11QMetaObject4CallEiPPv(
    QMetaObjectPublisher *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMetaObjectPublisher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QMetaObjectPublisher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMetaObjectPublisher::tr(s, c, n));
}

//  QMetaObjectPublisher::QMetaObjectPublisher(QWebChannel *webChannel)
extern "C" Q_DECL_EXPORT
QMetaObjectPublisher *ritual_ZN20QMetaObjectPublisherC1EP11QWebChannel(
    QWebChannel *webChannel) {
  return new CuteQMetaObjectPublisher(webChannel);
}

//  QMetaObjectPublisher::~QMetaObjectPublisher()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisherD1Ev(QMetaObjectPublisher *self) {
  delete self;
}

//  void QMetaObjectPublisher::registerObject(const QString &id, QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher14registerObjectERK7QStringP7QObject(
    QMetaObjectPublisher *self,
    const QString *id,
    QObject *object) {
  self->registerObject(*id, object);
}

//  void QMetaObjectPublisher::broadcastMessage(const QJsonObject &message)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QMetaObjectPublisher16broadcastMessageERK11QJsonObject(
    const QMetaObjectPublisher *self,
    const QJsonObject *message) {
  self->broadcastMessage(*message);
}

//  void QMetaObjectPublisher::enqueueBroadcastMessage(const QJsonObject
//      &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher23enqueueBroadcastMessageERK11QJsonObject(
    QMetaObjectPublisher *self,
    const QJsonObject *message) {
  self->enqueueBroadcastMessage(*message);
}

//  void QMetaObjectPublisher::enqueueMessage(const QJsonObject &message,
//      QWebChannelAbstractTransport *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher14enqueueMessageERK11QJsonObjectP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    const QJsonObject *message,
    QWebChannelAbstractTransport *transport) {
  self->enqueueMessage(*message, transport);
}

//  void QMetaObjectPublisher::sendEnqueuedPropertyUpdates(QWebChannelAbstrac
//      tTransport *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher27sendEnqueuedPropertyUpdatesEP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    QWebChannelAbstractTransport *transport) {
  self->sendEnqueuedPropertyUpdates(transport);
}

//  QJsonObject QMetaObjectPublisher::classInfoForObject(const QObject
//      *object, QWebChannelAbstractTransport *transport)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN20QMetaObjectPublisher18classInfoForObjectEPK7QObjectP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    const QObject *object,
    QWebChannelAbstractTransport *transport) {
  return new QJsonObject(self->classInfoForObject(object, transport));
}

//  void QMetaObjectPublisher::setClientIsIdle(bool isIdle,
//      QWebChannelAbstractTransport *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher15setClientIsIdleEbP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    bool isIdle,
    QWebChannelAbstractTransport *transport) {
  self->setClientIsIdle(isIdle, transport);
}

//  bool QMetaObjectPublisher::isClientIdle(QWebChannelAbstractTransport
//      *transport)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QMetaObjectPublisher12isClientIdleEP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    QWebChannelAbstractTransport *transport) {
  return self->isClientIdle(transport);
}

//  QJsonObject
//      QMetaObjectPublisher::initializeClient(QWebChannelAbstractTransport
//      *transport)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN20QMetaObjectPublisher16initializeClientEP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    QWebChannelAbstractTransport *transport) {
  return new QJsonObject(self->initializeClient(transport));
}

//  void QMetaObjectPublisher::initializePropertyUpdates(QObject *const
//      object, const QJsonObject &objectInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher25initializePropertyUpdatesEP7QObjectRK11QJsonObject(
    QMetaObjectPublisher *self,
    QObject *const object,
    const QJsonObject *objectInfo) {
  self->initializePropertyUpdates(object, *objectInfo);
}

//  void QMetaObjectPublisher::sendPendingPropertyUpdates()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher26sendPendingPropertyUpdatesEv(
    QMetaObjectPublisher *self) {
  self->sendPendingPropertyUpdates();
}

//  QVariant QMetaObjectPublisher::invokeMethod_helper(QObject *const object,
//      const QMetaMethod &method, const QJsonArray &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QMetaObjectPublisher19invokeMethod_helperEP7QObjectRK11QMetaMethodRK10QJsonArray(
    QMetaObjectPublisher *self,
    QObject *const object,
    const QMetaMethod *method,
    const QJsonArray *args) {
  return new QVariant(self->invokeMethod_helper(object, *method, *args));
}

//  QVariant QMetaObjectPublisher::invokeMethod(QObject *const object, const
//      QMetaMethod &method, const QJsonArray &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QMetaObjectPublisher12invokeMethodEP7QObjectRK11QMetaMethodRK10QJsonArray(
    QMetaObjectPublisher *self,
    QObject *const object,
    const QMetaMethod *method,
    const QJsonArray *args) {
  return new QVariant(self->invokeMethod(object, *method, *args));
}

//  QVariant QMetaObjectPublisher::invokeMethod(QObject *const object, const
//      int methodIndex, const QJsonArray &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QMetaObjectPublisher12invokeMethodEP7QObjectiRK10QJsonArray(
    QMetaObjectPublisher *self,
    QObject *const object,
    int methodIndex,
    const QJsonArray *args) {
  return new QVariant(self->invokeMethod(object, methodIndex, *args));
}

//  QVariant QMetaObjectPublisher::invokeMethod(QObject *const object, const
//      QByteArray &methodName, const QJsonArray &args)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN20QMetaObjectPublisher12invokeMethodEP7QObjectRK10QByteArrayRK10QJsonArray(
    QMetaObjectPublisher *self,
    QObject *const object,
    const QByteArray *methodName,
    const QJsonArray *args) {
  return new QVariant(self->invokeMethod(object, *methodName, *args));
}

//  void QMetaObjectPublisher::setProperty(QObject *object, const int
//      propertyIndex, const QJsonValue &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher11setPropertyEP7QObjectiRK10QJsonValue(
    QMetaObjectPublisher *self,
    QObject *object,
    int propertyIndex,
    const QJsonValue *value) {
  self->setProperty(object, propertyIndex, *value);
}

//  void QMetaObjectPublisher::signalEmitted(const QObject *object, const int
//      signalIndex, const QVariantList &arguments)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher13signalEmittedEPK7QObjectiRK5QListI8QVariantE(
    QMetaObjectPublisher *self,
    const QObject *object,
    int signalIndex,
    const QList<QVariant> *arguments) {
  self->signalEmitted(object, signalIndex, *arguments);
}

//  void QMetaObjectPublisher::propertyValueChanged(const QObject *object,
//      const int propertyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher20propertyValueChangedEPK7QObjecti(
    QMetaObjectPublisher *self,
    const QObject *object,
    int propertyIndex) {
  self->propertyValueChanged(object, propertyIndex);
}

//  void QMetaObjectPublisher::startPropertyUpdateTimer(bool forceRestart)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher24startPropertyUpdateTimerEb(
    QMetaObjectPublisher *self,
    bool forceRestart) {
  self->startPropertyUpdateTimer(forceRestart);
}

//  void QMetaObjectPublisher::objectDestroyed(const QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher15objectDestroyedEPK7QObject(
    QMetaObjectPublisher *self,
    const QObject *object) {
  self->objectDestroyed(object);
}

//  QObject *QMetaObjectPublisher::unwrapObject(const QString &objectId)
//      const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK20QMetaObjectPublisher12unwrapObjectERK7QString(
    const QMetaObjectPublisher *self,
    const QString *objectId) {
  return self->unwrapObject(*objectId);
}

//  QVariant QMetaObjectPublisher::unwrapMap(QVariantMap map) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QMetaObjectPublisher9unwrapMapE4QMapI7QString8QVariantE(
    const QMetaObjectPublisher *self,
    const QMap<QString, QVariant> *map) {
  return new QVariant(self->unwrapMap(*map));
}

//  QVariant QMetaObjectPublisher::unwrapList(QVariantList list) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QMetaObjectPublisher10unwrapListE5QListI8QVariantE(
    const QMetaObjectPublisher *self,
    const QList<QVariant> *list) {
  return new QVariant(self->unwrapList(*list));
}

//  QVariant QMetaObjectPublisher::unwrapVariant(const QVariant &value) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QMetaObjectPublisher13unwrapVariantERK8QVariant(
    const QMetaObjectPublisher *self,
    const QVariant *value) {
  return new QVariant(self->unwrapVariant(*value));
}

//  QVariant QMetaObjectPublisher::toVariant(const QJsonValue &value, int
//      targetType) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QMetaObjectPublisher9toVariantERK10QJsonValuei(
    const QMetaObjectPublisher *self,
    const QJsonValue *value,
    int targetType) {
  return new QVariant(self->toVariant(*value, targetType));
}

//  int QMetaObjectPublisher::conversionScore(const QJsonValue &value, int
//      targetType) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QMetaObjectPublisher15conversionScoreERK10QJsonValuei(
    const QMetaObjectPublisher *self,
    const QJsonValue *value,
    int targetType) {
  return self->conversionScore(*value, targetType);
}

//  int QMetaObjectPublisher::methodOverloadBadness(const QMetaMethod
//      &method, const QJsonArray &args) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QMetaObjectPublisher21methodOverloadBadnessERK11QMetaMethodRK10QJsonArray(
    const QMetaObjectPublisher *self,
    const QMetaMethod *method,
    const QJsonArray *args) {
  return self->methodOverloadBadness(*method, *args);
}

//  void QMetaObjectPublisher::transportRemoved(QWebChannelAbstractTransport
//      *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher16transportRemovedEP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    QWebChannelAbstractTransport *transport) {
  self->transportRemoved(transport);
}

//  QJsonValue QMetaObjectPublisher::wrapResult(const QVariant &result,
//      QWebChannelAbstractTransport *transport, const QString
//      &parentObjectId)
extern "C" Q_DECL_EXPORT
QJsonValue *ritual_ZN20QMetaObjectPublisher10wrapResultERK8QVariantP28QWebChannelAbstractTransportRK7QString(
    QMetaObjectPublisher *self,
    const QVariant *result,
    QWebChannelAbstractTransport *transport,
    const QString *parentObjectId) {
  return new QJsonValue(
      self->wrapResult(
          *result,
          transport,
          *parentObjectId));
}

//  QJsonArray QMetaObjectPublisher::wrapList(const QVariantList &list,
//      QWebChannelAbstractTransport *transport, const QString
//      &parentObjectId)
extern "C" Q_DECL_EXPORT
QJsonArray *ritual_ZN20QMetaObjectPublisher8wrapListERK5QListI8QVariantEP28QWebChannelAbstractTransportRK7QString(
    QMetaObjectPublisher *self,
    const QList<QVariant> *list,
    QWebChannelAbstractTransport *transport,
    const QString *parentObjectId) {
  return new QJsonArray(self->wrapList(*list, transport, *parentObjectId));
}

//  QJsonObject QMetaObjectPublisher::wrapMap(const QVariantMap &map,
//      QWebChannelAbstractTransport *transport, const QString
//      &parentObjectId)
extern "C" Q_DECL_EXPORT
QJsonObject *ritual_ZN20QMetaObjectPublisher7wrapMapERK4QMapI7QString8QVariantEP28QWebChannelAbstractTransportRKS1_(
    QMetaObjectPublisher *self,
    const QMap<QString, QVariant> *map,
    QWebChannelAbstractTransport *transport,
    const QString *parentObjectId) {
  return new QJsonObject(self->wrapMap(*map, transport, *parentObjectId));
}

//  void QMetaObjectPublisher::deleteWrappedObject(QObject *object) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QMetaObjectPublisher19deleteWrappedObjectEP7QObject(
    const QMetaObjectPublisher *self,
    QObject *object) {
  self->deleteWrappedObject(object);
}

//  int QMetaObjectPublisher::propertyUpdateInterval()
extern "C" Q_DECL_EXPORT
int ritual_ZN20QMetaObjectPublisher22propertyUpdateIntervalEv(
    QMetaObjectPublisher *self) {
  return self->propertyUpdateInterval();
}

//  void QMetaObjectPublisher::setPropertyUpdateInterval(int ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher25setPropertyUpdateIntervalEi(
    QMetaObjectPublisher *self,
    int ms) {
  self->setPropertyUpdateInterval(ms);
}

//  void QMetaObjectPublisher::setBlockUpdates(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher15setBlockUpdatesEb(
    QMetaObjectPublisher *self,
    bool block) {
  self->setBlockUpdates(block);
}

//  bool QMetaObjectPublisher::blockUpdates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMetaObjectPublisher12blockUpdatesEv(
    const QMetaObjectPublisher *self) {
  return self->blockUpdates();
}

//  void QMetaObjectPublisher::blockUpdatesChanged(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher19blockUpdatesChangedEb(
    QMetaObjectPublisher *self,
    bool block) {
  self->blockUpdatesChanged(block);
}

//  void QMetaObjectPublisher::handleMessage(const QJsonObject &message,
//      QWebChannelAbstractTransport *transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher13handleMessageERK11QJsonObjectP28QWebChannelAbstractTransport(
    QMetaObjectPublisher *self,
    const QJsonObject *message,
    QWebChannelAbstractTransport *transport) {
  self->handleMessage(*message, transport);
}

//  void QMetaObjectPublisher::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher10timerEventEP11QTimerEvent(
    QMetaObjectPublisher *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QMetaObjectPublisher::onBlockUpdatesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMetaObjectPublisher21onBlockUpdatesChangedEv(
    QMetaObjectPublisher *self) {
  self->onBlockUpdatesChanged();
}

//  SignalHandler<QMetaObjectPublisher>
//      *QMetaObjectPublisher::signalHandlerFor(const QObject *object)
extern "C" Q_DECL_EXPORT
SignalHandler<QMetaObjectPublisher> *ritual_ZN20QMetaObjectPublisher16signalHandlerForEPK7QObject(
    QMetaObjectPublisher *self,
    const QObject *object) {
  return self->signalHandlerFor(object);
}

//  size_t QMetaObjectPublisher::_qt_property_blockUpdatesStatus_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QMetaObjectPublisher38_qt_property_blockUpdatesStatus_offsetEv() {
  return QMetaObjectPublisher::_qt_property_blockUpdatesStatus_offset();
}

//  size_t
//      QMetaObjectPublisher::_qt_property_propertyUpdateIntervalTime_offset(
//      )
extern "C" Q_DECL_EXPORT
size_t ritual_ZN20QMetaObjectPublisher46_qt_property_propertyUpdateIntervalTime_offsetEv() {
  return QMetaObjectPublisher::_qt_property_propertyUpdateIntervalTime_offset();
}

//  a Python function taken by a CuteQMetaObjectPublisher, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMetaObjectPublisher(
    QMetaObjectPublisher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMetaObjectPublisher *>(self)->take(key, call);
}

//  void QMetaObjectPublisher::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QMetaObjectPublisher10timerEventEP11QTimerEvent(
    QMetaObjectPublisher *self,
    QTimerEvent *a0) {
  static_cast<OwnQMetaObjectPublisher *>(self)->OwnQMetaObjectPublisher::timerEvent(
      a0);
}
