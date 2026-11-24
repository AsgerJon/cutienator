//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusconnection.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbuspendingcall.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QDBusConnection::QDBusConnection(const QString &name)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnectionC1ERK7QString(
    const QString *name) {
  return new QDBusConnection(*name);
}

//  QDBusConnection::QDBusConnection(const QDBusConnection &other)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnectionC1ERKS_(
    const QDBusConnection *other) {
  return new QDBusConnection(*other);
}

//  QDBusConnection::~QDBusConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusConnectionD1Ev(QDBusConnection *self) {
  delete self;
}

//  bool QDBusConnection::isConnected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDBusConnection11isConnectedEv(
    const QDBusConnection *self) {
  return self->isConnected();
}

//  QString QDBusConnection::baseService() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDBusConnection11baseServiceEv(
    const QDBusConnection *self) {
  return new QString(self->baseService());
}

//  QDBusError QDBusConnection::lastError() const
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZNK15QDBusConnection9lastErrorEv(
    const QDBusConnection *self) {
  return new QDBusError(self->lastError());
}

//  QString QDBusConnection::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDBusConnection4nameEv(const QDBusConnection *self) {
  return new QString(self->name());
}

//  ConnectionCapabilities QDBusConnection::connectionCapabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDBusConnection22connectionCapabilitiesEv(
    const QDBusConnection *self) {
  return static_cast<int>(self->connectionCapabilities().toInt());
}

//  bool QDBusConnection::send(const QDBusMessage &message) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDBusConnection4sendERK12QDBusMessage(
    const QDBusConnection *self,
    const QDBusMessage *message) {
  return self->send(*message);
}

//  bool QDBusConnection::callWithCallback(const QDBusMessage &message,
//      QObject *receiver, const char *returnMethod, const char *errorMethod,
//      int timeout) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDBusConnection16callWithCallbackERK12QDBusMessageP7QObjectPKcS6_i(
    const QDBusConnection *self,
    const QDBusMessage *message,
    QObject *receiver,
    const char *returnMethod,
    const char *errorMethod,
    int timeout) {
  return self->callWithCallback(
      *message,
      receiver,
      returnMethod,
      errorMethod,
      timeout);
}

//  bool QDBusConnection::callWithCallback(const QDBusMessage &message,
//      QObject *receiver, const char *slot, int timeout) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDBusConnection16callWithCallbackERK12QDBusMessageP7QObjectPKci(
    const QDBusConnection *self,
    const QDBusMessage *message,
    QObject *receiver,
    const char *slot,
    int timeout) {
  return self->callWithCallback(*message, receiver, slot, timeout);
}

//  QDBusMessage QDBusConnection::call(const QDBusMessage &message,
//      QDBus::CallMode mode, int timeout) const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK15QDBusConnection4callERK12QDBusMessageN5QDBus8CallModeEi(
    const QDBusConnection *self,
    const QDBusMessage *message,
    QDBus::CallMode mode,
    int timeout) {
  return new QDBusMessage(self->call(*message, mode, timeout));
}

//  QDBusPendingCall QDBusConnection::asyncCall(const QDBusMessage &message,
//      int timeout) const
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZNK15QDBusConnection9asyncCallERK12QDBusMessagei(
    const QDBusConnection *self,
    const QDBusMessage *message,
    int timeout) {
  return new QDBusPendingCall(self->asyncCall(*message, timeout));
}

//  bool QDBusConnection::connect(const QString &service, const QString
//      &path, const QString &interface, const QString &name, QObject
//      *receiver, const char *slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection7connectERK7QStringS2_S2_S2_P7QObjectPKc(
    QDBusConnection *self,
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name,
    QObject *receiver,
    const char *slot) {
  return self->connect(*service, *path, *interface, *name, receiver, slot);
}

//  bool QDBusConnection::connect(const QString &service, const QString
//      &path, const QString &interface, const QString &name, const QString
//      &signature, QObject *receiver, const char *slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection7connectERK7QStringS2_S2_S2_S2_P7QObjectPKc(
    QDBusConnection *self,
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name,
    const QString *signature,
    QObject *receiver,
    const char *slot) {
  return self->connect(
      *service,
      *path,
      *interface,
      *name,
      *signature,
      receiver,
      slot);
}

//  bool QDBusConnection::connect(const QString &service, const QString
//      &path, const QString &interface, const QString &name, const
//      QStringList &argumentMatch, const QString &signature, QObject
//      *receiver, const char *slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection7connectERK7QStringS2_S2_S2_RK5QListIS0_ES2_P7QObjectPKc(
    QDBusConnection *self,
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name,
    const QList<QString> *argumentMatch,
    const QString *signature,
    QObject *receiver,
    const char *slot) {
  return self->connect(
      *service,
      *path,
      *interface,
      *name,
      *argumentMatch,
      *signature,
      receiver,
      slot);
}

//  bool QDBusConnection::disconnect(const QString &service, const QString
//      &path, const QString &interface, const QString &name, QObject
//      *receiver, const char *slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection10disconnectERK7QStringS2_S2_S2_P7QObjectPKc(
    QDBusConnection *self,
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name,
    QObject *receiver,
    const char *slot) {
  return self->disconnect(
      *service,
      *path,
      *interface,
      *name,
      receiver,
      slot);
}

//  bool QDBusConnection::disconnect(const QString &service, const QString
//      &path, const QString &interface, const QString &name, const QString
//      &signature, QObject *receiver, const char *slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection10disconnectERK7QStringS2_S2_S2_S2_P7QObjectPKc(
    QDBusConnection *self,
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name,
    const QString *signature,
    QObject *receiver,
    const char *slot) {
  return self->disconnect(
      *service,
      *path,
      *interface,
      *name,
      *signature,
      receiver,
      slot);
}

//  bool QDBusConnection::disconnect(const QString &service, const QString
//      &path, const QString &interface, const QString &name, const
//      QStringList &argumentMatch, const QString &signature, QObject
//      *receiver, const char *slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection10disconnectERK7QStringS2_S2_S2_RK5QListIS0_ES2_P7QObjectPKc(
    QDBusConnection *self,
    const QString *service,
    const QString *path,
    const QString *interface,
    const QString *name,
    const QList<QString> *argumentMatch,
    const QString *signature,
    QObject *receiver,
    const char *slot) {
  return self->disconnect(
      *service,
      *path,
      *interface,
      *name,
      *argumentMatch,
      *signature,
      receiver,
      slot);
}

//  bool QDBusConnection::registerObject(const QString &path, QObject
//      *object, RegisterOptions options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection14registerObjectERK7QStringP7QObject6QFlagsINS_14RegisterOptionEE(
    QDBusConnection *self,
    const QString *path,
    QObject *object,
    int options) {
  return self->registerObject(
      *path,
      object,
      QFlags<QDBusConnection::RegisterOption>::fromInt(options));
}

//  bool QDBusConnection::registerObject(const QString &path, const QString
//      &interface, QObject *object, RegisterOptions options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection14registerObjectERK7QStringS2_P7QObject6QFlagsINS_14RegisterOptionEE(
    QDBusConnection *self,
    const QString *path,
    const QString *interface,
    QObject *object,
    int options) {
  return self->registerObject(
      *path,
      *interface,
      object,
      QFlags<QDBusConnection::RegisterOption>::fromInt(options));
}

//  void QDBusConnection::unregisterObject(const QString &path,
//      UnregisterMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusConnection16unregisterObjectERK7QStringNS_14UnregisterModeE(
    QDBusConnection *self,
    const QString *path,
    QDBusConnection::UnregisterMode mode) {
  self->unregisterObject(*path, mode);
}

//  QObject *QDBusConnection::objectRegisteredAt(const QString &path) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK15QDBusConnection18objectRegisteredAtERK7QString(
    const QDBusConnection *self,
    const QString *path) {
  return self->objectRegisteredAt(*path);
}

//  bool QDBusConnection::registerVirtualObject(const QString &path,
//      QDBusVirtualObject *object, VirtualObjectRegisterOption options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection21registerVirtualObjectERK7QStringP18QDBusVirtualObjectNS_27VirtualObjectRegisterOptionE(
    QDBusConnection *self,
    const QString *path,
    QDBusVirtualObject *object,
    QDBusConnection::VirtualObjectRegisterOption options) {
  return self->registerVirtualObject(*path, object, options);
}

//  bool QDBusConnection::registerService(const QString &serviceName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection15registerServiceERK7QString(
    QDBusConnection *self,
    const QString *serviceName) {
  return self->registerService(*serviceName);
}

//  bool QDBusConnection::unregisterService(const QString &serviceName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QDBusConnection17unregisterServiceERK7QString(
    QDBusConnection *self,
    const QString *serviceName) {
  return self->unregisterService(*serviceName);
}

//  QDBusConnectionInterface *QDBusConnection::interface() const
extern "C" Q_DECL_EXPORT
QDBusConnectionInterface *ritual_ZNK15QDBusConnection9interfaceEv(
    const QDBusConnection *self) {
  return self->interface();
}

//  QDBusConnection QDBusConnection::connectToBus(BusType type, const QString
//      &name)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnection12connectToBusENS_7BusTypeERK7QString(
    QDBusConnection::BusType type,
    const QString *name) {
  return new QDBusConnection(QDBusConnection::connectToBus(type, *name));
}

//  QDBusConnection QDBusConnection::connectToBus(const QString &address,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnection12connectToBusERK7QStringS2_(
    const QString *address,
    const QString *name) {
  return new QDBusConnection(QDBusConnection::connectToBus(*address, *name));
}

//  QDBusConnection QDBusConnection::connectToPeer(const QString &address,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnection13connectToPeerERK7QStringS2_(
    const QString *address,
    const QString *name) {
  return new QDBusConnection(
      QDBusConnection::connectToPeer(
          *address,
          *name));
}

//  void QDBusConnection::disconnectFromBus(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusConnection17disconnectFromBusERK7QString(
    const QString *name) {
  QDBusConnection::disconnectFromBus(*name);
}

//  void QDBusConnection::disconnectFromPeer(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDBusConnection18disconnectFromPeerERK7QString(
    const QString *name) {
  QDBusConnection::disconnectFromPeer(*name);
}

//  QByteArray QDBusConnection::localMachineId()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QDBusConnection14localMachineIdEv() {
  return new QByteArray(QDBusConnection::localMachineId());
}

//  QDBusConnection QDBusConnection::sessionBus()
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnection10sessionBusEv() {
  return new QDBusConnection(QDBusConnection::sessionBus());
}

//  QDBusConnection QDBusConnection::systemBus()
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnection9systemBusEv() {
  return new QDBusConnection(QDBusConnection::systemBus());
}

//  QDBusConnection::QDBusConnection(QDBusConnectionPrivate *dd)
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZN15QDBusConnectionC1EP22QDBusConnectionPrivate(
    QDBusConnectionPrivate *dd) {
  return new QDBusConnection(dd);
}

#endif  // !defined(QT_NO_DBUS)
