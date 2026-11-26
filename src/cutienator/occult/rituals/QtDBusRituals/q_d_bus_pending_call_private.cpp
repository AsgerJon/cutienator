//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/6.12.0/QtDBus/private/qdbuspendingcall_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  from src/dbus/qdbuspendingcall.cpp, line 210, as _ZN23QDBusPendingCallPrivate22waitForFinishedWithGuiEv
#if !defined(QT_NO_DBUS)
inline void QDBusPendingCallPrivate::waitForFinishedWithGui()
{
    QEventLoop loop;

    {
        const auto locker = qt_scoped_lock(mutex);
        if (replyMessage.type() != QDBusMessage::InvalidMessage)
            return; // already finished

        Q_ASSERT(!watcherHelper);
        watcherHelper = new QDBusPendingCallWatcherHelper;
        loop.connect(watcherHelper, &QDBusPendingCallWatcherHelper::reply, &loop,
                     &QEventLoop::quit);
        loop.connect(watcherHelper, &QDBusPendingCallWatcherHelper::error, &loop,
                     &QEventLoop::quit);
    }

    loop.exec(QEventLoop::ExcludeUserInputEvents | QEventLoop::WaitForMoreEvents);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbuspendingcall.cpp, line 158, as _ZN23QDBusPendingCallPrivate12setMetaTypesEiPK9QMetaType
#if !defined(QT_NO_DBUS)
inline void QDBusPendingCallPrivate::setMetaTypes(int count, const QMetaType *types)
{
    if (count == 0) {
        expectedReplySignature = ""_L1; // not null
        return;
    }

    QByteArray sig;
    sig.reserve(count + count / 2);
    for (int i = 0; i < count; ++i) {
        const char *typeSig = QDBusMetaType::typeToSignature(types[i]);
        if (Q_UNLIKELY(!typeSig))
            qFatal("QDBusPendingReply: type %s is not registered with QtDBus", types[i].name());
        sig += typeSig;
    }

    expectedReplySignature = QString::fromLatin1(sig);
}
#endif  // !defined(QT_NO_DBUS)

//  from src/dbus/qdbuspendingcall.cpp, line 177, as _ZN23QDBusPendingCallPrivate22checkReceivedSignatureEv
#if !defined(QT_NO_DBUS)
inline void QDBusPendingCallPrivate::checkReceivedSignature()
{
    // MUST BE CALLED WITH A LOCKED MUTEX!

    if (replyMessage.type() == QDBusMessage::InvalidMessage)
        return;                 // not yet finished - no message to
                                // validate against
    if (replyMessage.type() == QDBusMessage::ErrorMessage)
        return;                 // we don't have to check the signature of an error reply

    if (expectedReplySignature.isNull())
        return;                 // no signature to validate against

    // can't use startsWith here because a null string doesn't start or end with an empty string
    if (replyMessage.signature().indexOf(expectedReplySignature) != 0) {
        const auto errorMsg = "Unexpected reply signature: got \"%1\", expected \"%2\""_L1;
        replyMessage = QDBusMessage::createError(
            QDBusError::InvalidSignature,
            errorMsg.arg(replyMessage.signature(), expectedReplySignature));

    }
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

#if !defined(QT_NO_DBUS)
//  void QDBusPendingCallPrivate::waitForFinishedWithGui()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallPrivate22waitForFinishedWithGuiEv(
    QDBusPendingCallPrivate *self) {
  self->waitForFinishedWithGui();
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusPendingCallPrivate::setMetaTypes(int count, const QMetaType
//      *types)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallPrivate12setMetaTypesEiPK9QMetaType(
    QDBusPendingCallPrivate *self,
    int count,
    const QMetaType *types) {
  self->setMetaTypes(count, types);
}
#endif  // !defined(QT_NO_DBUS)

#if !defined(QT_NO_DBUS)
//  void QDBusPendingCallPrivate::checkReceivedSignature()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallPrivate22checkReceivedSignatureEv(
    QDBusPendingCallPrivate *self) {
  self->checkReceivedSignature();
}
#endif  // !defined(QT_NO_DBUS)

#endif  // !defined(QT_NO_DBUS)
