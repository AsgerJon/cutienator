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
#include <QtCore/qmetaobject.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusintegrator_p.h"
#include <qcoreapplication.h>
#include <qelapsedtimer.h>
#include <private/qlatch_p.h>
#include <qloggingcategory.h>
#include <qmetaobject.h>
#include <qobject.h>
#include <qsocketnotifier.h>
#include <qstringlist.h>
#include <qthread.h>
#include <private/qlocking_p.h>
#include <QtCore/qset.h>
#include "qdbusargument.h"
#include "qdbusconnection_p.h"
#include "qdbusconnectionmanager_p.h"
#include "qdbusinterface_p.h"
#include "qdbusmessage.h"
#include "qdbusmetatype.h"
#include "qdbusmetatype_p.h"
#include "qdbusabstractadaptor.h"
#include "qdbusabstractadaptor_p.h"
#include "qdbusserver.h"
#include "qdbusutil_p.h"
#include "qdbusvirtualobject.h"
#include "qdbusmessage_p.h"
#include "qdbuscontext_p.h"
#include "qdbuspendingcall_p.h"
#include "qdbusthreaddebug_p.h"
#include <algorithm>
#include "qdbusabstractinterface.h"
#include "qdbusabstractinterface_p.h"
#include <qcoreapplication.h>
#include <qthread.h>
#include "qdbusargument.h"
#include "qdbuspendingcall.h"
#include "qdbusmessage_p.h"
#include "qdbusmetaobject_p.h"
#include "qdbusmetatype_p.h"
#include "qdbusservicewatcher.h"
#include "qdbusutil_p.h"
#include <qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
