//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbusinterface_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/qdbusinterface.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbusinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtDBus/qdbusinterface.h>
#include <QtDBus/private/qdbusinterface_p.h>
#include <QtDBus/private/qdbus_symbols_p.h>
#include <QtCore/qpointer.h>
#include <QtCore/qstringlist.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/private/qdbusconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from src/dbus/qdbusinterface.cpp, line 21, as local:qdbusinterface.cpp:copyArgument
#if !defined(QT_NO_DBUS)
static void copyArgument(void *to, int id, const QVariant &arg)
{
    if (id == arg.metaType().id()) {
        switch (id) {
        case QMetaType::Bool:
            *reinterpret_cast<bool *>(to) = arg.toBool();
            return;

        case QMetaType::UChar:
            *reinterpret_cast<uchar *>(to) = qvariant_cast<uchar>(arg);
            return;

        case QMetaType::Short:
            *reinterpret_cast<short *>(to) = qvariant_cast<short>(arg);
            return;

        case QMetaType::UShort:
            *reinterpret_cast<ushort *>(to) = qvariant_cast<ushort>(arg);
            return;

        case QMetaType::Int:
            *reinterpret_cast<int *>(to) = arg.toInt();
            return;

        case QMetaType::UInt:
            *reinterpret_cast<uint *>(to) = arg.toUInt();
            return;

        case QMetaType::LongLong:
            *reinterpret_cast<qlonglong *>(to) = arg.toLongLong();
            return;

        case QMetaType::ULongLong:
            *reinterpret_cast<qulonglong *>(to) = arg.toULongLong();
            return;

        case QMetaType::Double:
            *reinterpret_cast<double *>(to) = arg.toDouble();
            return;

        case QMetaType::QString:
            *reinterpret_cast<QString *>(to) = arg.toString();
            return;

        case QMetaType::QByteArray:
            *reinterpret_cast<QByteArray *>(to) = arg.toByteArray();
            return;

        case QMetaType::QStringList:
            *reinterpret_cast<QStringList *>(to) = arg.toStringList();
            return;
        }

        if (id == QDBusMetaTypeId::variant().id()) {
            *reinterpret_cast<QDBusVariant *>(to) = qvariant_cast<QDBusVariant>(arg);
            return;
        } else if (id == QDBusMetaTypeId::objectpath().id()) {
            *reinterpret_cast<QDBusObjectPath *>(to) = qvariant_cast<QDBusObjectPath>(arg);
            return;
        } else if (id == QDBusMetaTypeId::signature().id()) {
            *reinterpret_cast<QDBusSignature *>(to) = qvariant_cast<QDBusSignature>(arg);
            return;
        }

        // those above are the only types possible
        // the demarshaller code doesn't demarshall anything else
        qFatal("Found a decoded basic type in a D-Bus reply that shouldn't be there");
    }

    // if we got here, it's either an un-dermarshalled type or a mismatch
    if (arg.metaType() != QDBusMetaTypeId::argument()) {
        // it's a mismatch
        //qWarning?
        return;
    }

    // is this type registered?
    const char *userSignature = QDBusMetaType::typeToSignature(QMetaType(id));
    if (!userSignature || !*userSignature) {
        // type not registered
        //qWarning?
        return;
    }

    // is it the same signature?
    QDBusArgument dbarg = qvariant_cast<QDBusArgument>(arg);
    if (dbarg.currentSignature() != QLatin1StringView(userSignature)) {
        // not the same signature, another mismatch
        //qWarning?
        return;
    }

    // we can demarshall
    QDBusMetaType::demarshall(dbarg, QMetaType(id), to);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusintegrator.cpp, line 2627, as _ZN22QDBusConnectionPrivate14findMetaObjectERK7QStringS2_S2_R10QDBusError
#if !defined(QT_NO_DBUS)
inline QDBusMetaObject *
QDBusConnectionPrivate::findMetaObject(const QString &service, const QString &path,
                                       const QString &interface, QDBusError &error)
{
    // service must be a unique connection name
    if (!interface.isEmpty()) {
        QDBusReadLocker locker(FindMetaObject1Action, this);
        QDBusMetaObject *mo = cachedMetaObjects.value(interface, nullptr);
        if (mo)
            return mo;
    }
    if (path.isEmpty()) {
        error = QDBusError(QDBusError::InvalidObjectPath, "Object path cannot be empty"_L1);
        lastError = error;
        return nullptr;
    }

    // introspect the target object
    QDBusMessage msg = QDBusMessage::createMethodCall(service, path,
                                                QDBusUtil::dbusInterfaceIntrospectable(),
                                                QStringLiteral("Introspect"));
    QDBusMessagePrivate::setParametersValidated(msg, true);

    QDBusMessage reply = sendWithReply(msg, QDBus::Block);

    // it doesn't exist yet, we have to create it
    QDBusWriteLocker locker(FindMetaObject2Action, this);
    QDBusMetaObject *mo = nullptr;
    if (!interface.isEmpty())
        mo = cachedMetaObjects.value(interface, nullptr);
    if (mo)
        // maybe it got created when we switched from read to write lock
        return mo;

    QString xml;
    if (reply.type() == QDBusMessage::ReplyMessage) {
        if (reply.signature() == "s"_L1)
            // fetch the XML description
            xml = reply.arguments().at(0).toString();
    } else {
        error = QDBusError(reply);
        lastError = error;
        if (reply.type() != QDBusMessage::ErrorMessage || error.type() != QDBusError::UnknownMethod)
            return nullptr; // error
    }

    // release the lock and return
    QDBusMetaObject *result = QDBusMetaObject::createMetaObject(interface, xml,
                                                                cachedMetaObjects, error);
    lastError = error;
    return result;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbusabstractinterface.cpp, line 74, as _ZN29QDBusAbstractInterfacePrivateC2ERK7QStringS2_S2_RK15QDBusConnectionb
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

//  from src/dbus/qdbusinterface.cpp, line 136, as _ZN21QDBusInterfacePrivateD1Ev
#if !defined(QT_NO_DBUS)
inline QDBusInterfacePrivate::~QDBusInterfacePrivate()
{
    if (metaObject && !metaObject->cached)
        delete metaObject;
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusInterface *QDBusInterfacePrivate::q_func()
extern "C" Q_DECL_EXPORT
QDBusInterface *ritual_ZN21QDBusInterfacePrivate6q_funcEv(
    QDBusInterfacePrivate *self) {
  return self->q_func();
}

//  const QDBusInterface *QDBusInterfacePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDBusInterface *ritual_ZNK21QDBusInterfacePrivate6q_funcEv(
    const QDBusInterfacePrivate *self) {
  return self->q_func();
}

//  QDBusInterfacePrivate::~QDBusInterfacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusInterfacePrivateD1Ev(QDBusInterfacePrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_DBUS)
