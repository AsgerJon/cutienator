//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtDBus/qtdbusglobal.h>
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/6.12.0/QtDBus/private/qtdbusglobal_p.h>
#include <QtDBus/QtDBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusmessage.h>
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
#include <QtDBus/qdbuspendingcall.h>
#include <QtDBus/private/qdbuspendingcall_p.h>
#include <QtDBus/private/qdbusconnection_p.h>
#include <QtDBus/private/qdbusmetatype_p.h>
#include <QtDBus/private/qdbusutil_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qlocking_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/dbus/qdbusintegrator.cpp, line 1310, as _ZN22QDBusConnectionPrivate8findSlotEP7QObjectRK10QByteArrayR5QListI9QMetaTypeER7QString
#if !defined(QT_NO_DBUS)
inline int QDBusConnectionPrivate::findSlot(QObject *obj, const QByteArray &normalizedName,
                                     QList<QMetaType> &params, QString &errorMsg)
{
    errorMsg.clear();
    int midx = obj->metaObject()->indexOfMethod(normalizedName);
    if (midx == -1)
        return -1;

    int inputCount = qDBusParametersForMethod(obj->metaObject()->method(midx), params, errorMsg);
    if (inputCount == -1 || inputCount + 1 != params.size())
        return -1;

    return midx;
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbuspendingcall.cpp, line 200, as _ZN23QDBusPendingCallPrivate15waitForFinishedEv
#if !defined(QT_NO_DBUS)
inline void QDBusPendingCallPrivate::waitForFinished()
{
    const auto locker = qt_scoped_lock(mutex);

    if (replyMessage.type() != QDBusMessage::InvalidMessage)
        return;                 // already finished

    waitForFinishedCondition.wait(&mutex);
}
#endif  // !defined(QT_NO_DBUS)
//  -----------------------------------------------------------------------

//  QDBusPendingCallPrivate::QDBusPendingCallPrivate(const QDBusMessage
//      &sent, QDBusConnectionPrivate *connection)
extern "C" Q_DECL_EXPORT
QDBusPendingCallPrivate *ritual_ZN23QDBusPendingCallPrivateC1ERK12QDBusMessageP22QDBusConnectionPrivate(
    const QDBusMessage *sent,
    QDBusConnectionPrivate *connection) {
  return new QDBusPendingCallPrivate(*sent, connection);
}

#if !defined(QT_NO_DBUS)
//  void QDBusPendingCallPrivate::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallPrivate15waitForFinishedEv(
    QDBusPendingCallPrivate *self) {
  self->waitForFinished();
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
