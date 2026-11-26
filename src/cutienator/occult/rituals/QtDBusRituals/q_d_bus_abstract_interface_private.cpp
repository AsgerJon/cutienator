//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusabstractinterface_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/qdbusabstractinterface.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusabstractinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/private/qdbusintegrator_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/private/qlatch_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qobject.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qset.h>
#include <QtDBus/qdbusargument.h>
#include <QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/private/qdbusconnectionmanager_p.h>
#include <QtDBus/private/qdbusinterface_p.h>
#include <QtDBus/qdbusmessage.h>
#include <QtDBus/qdbusmetatype.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/qdbusabstractadaptor.h>
#include <QtDBus/private/qdbusabstractadaptor_p.h>
#include <QtDBus/qdbusserver.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtDBus/qdbusvirtualobject.h>
#include <QtDBus/private/qdbusmessage_p.h>
#include <QtDBus/private/qdbuscontext_p.h>
#include <QtDBus/private/qdbuspendingcall_p.h>
#include <QtDBus/private/qdbusthreaddebug_p.h>
#include <algorithm>
#include <QtDBus/qdbusabstractinterface.h>
#include <QtDBus/private/qdbusabstractinterface_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qthread.h>
#include <QtDBus/qdbusargument.h>
#include <QtDBus/qdbuspendingcall.h>
#include <QtDBus/private/qdbusmessage_p.h>
#include <QtDBus/private/qdbusmetaobject_p.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/qdbusservicewatcher.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/dbus/qdbusabstractinterface.cpp, line 51, as local:qdbusabstractinterface.cpp:checkIfValid
#if !defined(QT_NO_DBUS)
static QDBusError checkIfValid(const QString &service, const QString &path,
                               const QString &interface, bool isDynamic, bool isPeer)
{
    // We should be throwing exceptions here... oh well
    QDBusError error;

    // dynamic interfaces (QDBusInterface) can have empty interfaces, but not service and object paths
    // non-dynamic is the opposite: service and object paths can be empty, but not the interface
    if (!isDynamic) {
        // use assertion here because this should never happen, at all
        Q_ASSERT_X(!interface.isEmpty(), "QDBusAbstractInterface", "Interface name cannot be empty");
    }
    if (!QDBusUtil::checkBusName(service, (isDynamic && !isPeer) ? QDBusUtil::EmptyNotAllowed : QDBusUtil::EmptyAllowed, &error))
        return error;
    if (!QDBusUtil::checkObjectPath(path, isDynamic ? QDBusUtil::EmptyNotAllowed : QDBusUtil::EmptyAllowed, &error))
        return error;
    if (!QDBusUtil::checkInterfaceName(interface, QDBusUtil::EmptyAllowed, &error))
        return error;

    // no error
    return QDBusError();
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2581, as _ZN22QDBusConnectionPrivate12getNameOwnerERK7QString
#if !defined(QT_NO_DBUS)
inline QString QDBusConnectionPrivate::getNameOwner(const QString& serviceName)
{
    if (QDBusUtil::isValidUniqueConnectionName(serviceName))
        return serviceName;
    if (!connection)
        return QString();

    {
        // acquire a read lock for the cache
        QReadLocker locker(&lock);
        WatchedServicesHash::ConstIterator it = watchedServices.constFind(serviceName);
        if (it != watchedServices.constEnd())
            return it->owner;
    }

    // not cached
    return getNameOwnerNoCache(serviceName);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2536, as _ZN22QDBusConnectionPrivate18shouldWatchServiceERK7QString
#if !defined(QT_NO_DBUS)
inline bool QDBusConnectionPrivate::shouldWatchService(const QString &service)
{
    // we don't have to watch anything in peer mode
    if (mode != ClientMode)
        return false;
    // we don't have to watch wildcard services (empty strings)
    if (service.isEmpty())
        return false;
    // we don't have to watch the bus driver
    if (service == QDBusUtil::dbusService())
        return false;
    return true;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2600, as _ZN22QDBusConnectionPrivate19getNameOwnerNoCacheERK7QString
#if !defined(QT_NO_DBUS)
inline QString QDBusConnectionPrivate::getNameOwnerNoCache(const QString &serviceName)
{
    QDBusMessage msg = QDBusMessage::createMethodCall(QDBusUtil::dbusService(),
            QDBusUtil::dbusPath(), QDBusUtil::dbusInterface(),
            QStringLiteral("GetNameOwner"));
    QDBusMessagePrivate::setParametersValidated(msg, true);
    msg << serviceName;

    QDBusPendingCallPrivate *pcall = sendWithReplyAsync(msg, nullptr, nullptr, nullptr);
    if (pcall->replyMessage.type() == QDBusMessage::InvalidMessage) {
        if (thread() == QThread::currentThread()) {
            // this function may be called in our own thread and
            // QDBusPendingCallPrivate::waitForFinished() would deadlock there
            q_dbus_pending_call_block(pcall->pending);
        }
        pcall->waitForFinished();
    }
    msg = pcall->replyMessage;

    if (!pcall->ref.deref())
        delete pcall;

    if (msg.type() == QDBusMessage::ReplyMessage)
        return msg.arguments().at(0).toString();
    return QString();
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractinterface.cpp, line 74, as _ZN29QDBusAbstractInterfacePrivateC1ERK7QStringS2_S2_RK15QDBusConnectionb
#if !defined(QT_NO_DBUS)
inline QDBusAbstractInterfacePrivate::QDBusAbstractInterfacePrivate(const QString &serv,
                                                             const QString &p,
                                                             const QString &iface,
                                                             const QDBusConnection& con,
                                                             bool isDynamic)
    : connection(con), service(serv), path(p), interface(iface),
      lastError(checkIfValid(serv, p, iface, isDynamic, (connectionPrivate() &&
                                                         connectionPrivate()->mode == QDBusConnectionPrivate::PeerMode))),
      timeout(-1),
      interactiveAuthorizationAllowed(false),
      isValid(!lastError.isValid())
{
    if (!isValid)
        return;

    if (!connection.isConnected()) {
        lastError = QDBusError(QDBusError::Disconnected,
                               QDBusUtil::disconnectedErrorMessage());
    }
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractinterface.cpp, line 109, as _ZNK29QDBusAbstractInterfacePrivate12canMakeCallsEv
#if !defined(QT_NO_DBUS)
inline bool QDBusAbstractInterfacePrivate::canMakeCalls() const
{
    // recheck only if we have a wildcard (i.e. empty) service or path
    // if any are empty, set the error message according to QDBusUtil
    if (service.isEmpty() && connectionPrivate()->mode != QDBusConnectionPrivate::PeerMode)
        return QDBusUtil::checkBusName(service, QDBusUtil::EmptyNotAllowed, &lastError);
    if (path.isEmpty())
        return QDBusUtil::checkObjectPath(path, QDBusUtil::EmptyNotAllowed, &lastError);
    return true;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractinterface.cpp, line 120, as _ZNK29QDBusAbstractInterfacePrivate8propertyERK13QMetaPropertyPv
#if !defined(QT_NO_DBUS)
inline bool QDBusAbstractInterfacePrivate::property(const QMetaProperty &mp, void *returnValuePtr) const
{
    if (!isValid || !canMakeCalls())   // can't make calls
        return false;

    QMetaType type = mp.metaType();
    // is this metatype registered?
    const char *expectedSignature = "";
    if (type.id() != QMetaType::QVariant) {
        expectedSignature = QDBusMetaType::typeToSignature(type);
        if (expectedSignature == nullptr) {
            qWarning("QDBusAbstractInterface: type %s must be registered with Qt D-Bus before it can be "
                     "used to read property %s.%s",
                     mp.typeName(), qPrintable(interface), mp.name());
            lastError = QDBusError(QDBusError::Failed, "Unregistered type %1 cannot be handled"_L1
                                   .arg(QLatin1StringView(mp.typeName())));
            return false;
        }
    }

    // try to read this property
    QDBusMessage msg = QDBusMessage::createMethodCall(service, path,
                                                      QDBusUtil::dbusInterfaceProperties(),
                                                      QStringLiteral("Get"));
    QDBusMessagePrivate::setParametersValidated(msg, true);
    msg << interface << QString::fromUtf8(mp.name());
    QDBusMessage reply = connection.call(msg, QDBus::Block, timeout);

    if (reply.type() != QDBusMessage::ReplyMessage) {
        lastError = QDBusError(reply);
        return false;
    }
    if (reply.signature() != "v"_L1) {
        QString errmsg =
                "Invalid signature '%1' in return from call to " DBUS_INTERFACE_PROPERTIES ""_L1;
        lastError = QDBusError(QDBusError::InvalidSignature, std::move(errmsg).arg(reply.signature()));
        return false;
    }

    QByteArray foundSignature;
    const char *foundType = nullptr;
    QVariant value = qvariant_cast<QDBusVariant>(reply.arguments().at(0)).variant();

    if (value.metaType() == type || type.id() == QMetaType::QVariant
        || (expectedSignature[0] == 'v' && expectedSignature[1] == '\0')) {
        // simple match
        if (type.id() == QMetaType::QVariant) {
            *reinterpret_cast<QVariant*>(returnValuePtr) = value;
        } else {
            QMetaType(type).destruct(returnValuePtr);
            QMetaType(type).construct(returnValuePtr, value.constData());
        }
        return true;
    }

    if (value.metaType() == QMetaType::fromType<QDBusArgument>()) {
        QDBusArgument arg = qvariant_cast<QDBusArgument>(value);

        foundType = "user type";
        foundSignature = arg.currentSignature().toLatin1();
        if (foundSignature == expectedSignature) {
            // signatures match, we can demarshall
            return QDBusMetaType::demarshall(arg, QMetaType(type), returnValuePtr);
        }
    } else {
        foundType = value.typeName();
        foundSignature = QDBusMetaType::typeToSignature(value.metaType());
    }

    // there was an error...
    const auto errmsg = "Unexpected '%1' (%2) when retrieving property '%3.%4' "
                        "(expected type '%5' (%6))"_L1;
    lastError = QDBusError(QDBusError::InvalidSignature,
                           errmsg.arg(QLatin1StringView(foundType),
                                      QLatin1StringView(foundSignature),
                                      interface,
                                      QLatin1StringView(mp.name()),
                                      QLatin1StringView(mp.typeName()),
                                      QLatin1StringView(expectedSignature)));
    return false;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractinterface.cpp, line 202, as _ZN29QDBusAbstractInterfacePrivate11setPropertyERK13QMetaPropertyRK8QVariant
#if !defined(QT_NO_DBUS)
inline bool QDBusAbstractInterfacePrivate::setProperty(const QMetaProperty &mp, const QVariant &value)
{
    if (!isValid || !canMakeCalls())    // can't make calls
        return false;

    // send the value
    QDBusMessage msg = QDBusMessage::createMethodCall(service, path,
                                                      QDBusUtil::dbusInterfaceProperties(),
                                                      QStringLiteral("Set"));
    QDBusMessagePrivate::setParametersValidated(msg, true);
    msg << interface << QString::fromUtf8(mp.name()) << QVariant::fromValue(QDBusVariant(value));
    QDBusMessage reply = connection.call(msg, QDBus::Block, timeout);

    if (reply.type() != QDBusMessage::ReplyMessage) {
        lastError = QDBusError(reply);
        return false;
    }
    return true;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractinterface.cpp, line 222, as _ZN29QDBusAbstractInterfacePrivate22_q_serviceOwnerChangedERK7QStringS2_S2_
#if !defined(QT_NO_DBUS)
inline void QDBusAbstractInterfacePrivate::_q_serviceOwnerChanged(const QString &name,
                                                           const QString &oldOwner,
                                                           const QString &newOwner)
{
    Q_UNUSED(oldOwner);
    //qDebug() << "QDBusAbstractInterfacePrivate serviceOwnerChanged" << name << oldOwner << newOwner;
    Q_ASSERT(name == service);
    currentOwner = newOwner;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusAbstractInterface *QDBusAbstractInterfacePrivate::q_func()
extern "C" Q_DECL_EXPORT
QDBusAbstractInterface *ritual_ZN29QDBusAbstractInterfacePrivate6q_funcEv(
    QDBusAbstractInterfacePrivate *self) {
  return self->q_func();
}

//  const QDBusAbstractInterface *QDBusAbstractInterfacePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QDBusAbstractInterface *ritual_ZNK29QDBusAbstractInterfacePrivate6q_funcEv(
    const QDBusAbstractInterfacePrivate *self) {
  return self->q_func();
}

//  QDBusAbstractInterfacePrivate::QDBusAbstractInterfacePrivate(const
//      QString &serv, const QString &p, const QString &iface, const
//      QDBusConnection &con, bool dynamic)
extern "C" Q_DECL_EXPORT
QDBusAbstractInterfacePrivate *ritual_ZN29QDBusAbstractInterfacePrivateC1ERK7QStringS2_S2_RK15QDBusConnectionb(
    const QString *serv,
    const QString *p,
    const QString *iface,
    const QDBusConnection *con,
    bool dynamic) {
  return new QDBusAbstractInterfacePrivate(*serv, *p, *iface, *con, dynamic);
}

//  QDBusAbstractInterfacePrivate::~QDBusAbstractInterfacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusAbstractInterfacePrivateD1Ev(
    QDBusAbstractInterfacePrivate *self) {
  delete self;
}

#if !defined(QT_NO_DBUS)
//  bool QDBusAbstractInterfacePrivate::canMakeCalls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDBusAbstractInterfacePrivate12canMakeCallsEv(
    const QDBusAbstractInterfacePrivate *self) {
  return self->canMakeCalls();
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  bool QDBusAbstractInterfacePrivate::property(const QMetaProperty &mp,
//      void *returnValuePtr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QDBusAbstractInterfacePrivate8propertyERK13QMetaPropertyPv(
    const QDBusAbstractInterfacePrivate *self,
    const QMetaProperty *mp,
    void *returnValuePtr) {
  return self->property(*mp, returnValuePtr);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  bool QDBusAbstractInterfacePrivate::setProperty(const QMetaProperty &mp,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QDBusAbstractInterfacePrivate11setPropertyERK13QMetaPropertyRK8QVariant(
    QDBusAbstractInterfacePrivate *self,
    const QMetaProperty *mp,
    const QVariant *value) {
  return self->setProperty(*mp, *value);
}
#endif  // !defined(QT_NO_DBUS)

//  QDBusConnectionPrivate
//      *QDBusAbstractInterfacePrivate::connectionPrivate() const
extern "C" Q_DECL_EXPORT
QDBusConnectionPrivate *ritual_ZNK29QDBusAbstractInterfacePrivate17connectionPrivateEv(
    const QDBusAbstractInterfacePrivate *self) {
  return self->connectionPrivate();
}

#if !defined(QT_NO_DBUS)
//  void QDBusAbstractInterfacePrivate::_q_serviceOwnerChanged(const QString
//      &name, const QString &oldOwner, const QString &newOwner)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QDBusAbstractInterfacePrivate22_q_serviceOwnerChangedERK7QStringS2_S2_(
    QDBusAbstractInterfacePrivate *self,
    const QString *name,
    const QString *oldOwner,
    const QString *newOwner) {
  self->_q_serviceOwnerChanged(*name, *oldOwner, *newOwner);
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
