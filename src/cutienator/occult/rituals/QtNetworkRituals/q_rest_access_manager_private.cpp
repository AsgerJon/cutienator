//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qrestaccessmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qrestaccessmanager.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qrestaccessmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qrestaccessmanager.h>
#include <QtNetwork/private/qrestaccessmanager_p.h>
#include <QtNetwork/qrestreply.h>
#include <QtNetwork/qhttpmultipart.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qthread.h>
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

//  from src/network/access/qrestaccessmanager.cpp, line 826, as local:qrestaccessmanager.cpp:warnNoAccessManager
Q_DECL_COLD_FUNCTION
static QNetworkReply* warnNoAccessManager()
{
    qCWarning(lcQrest, "QRestAccessManager: QNetworkAccessManager not set");
    return nullptr;
}

//  from src/network/access/qrestaccessmanager.cpp, line 581, as _ZN25QRestAccessManagerPrivateD1Ev
inline QRestAccessManagerPrivate::~QRestAccessManagerPrivate()
{
    if (!activeRequests.isEmpty()) {
        qCWarning(lcQrest, "Access manager destroyed while %lld requests were still in progress",
                  qlonglong(activeRequests.size()));
    }
}

//  from src/network/access/qrestaccessmanager.cpp, line 22, as _Z7lcQrestv
inline const QLoggingCategory &lcQrest()
{
    static const QLoggingCategory category("qt.network.access.rest");
    return category;
}

//  from src/network/access/qrestaccessmanager.cpp, line 784, as _ZN25QRestAccessManagerPrivate19createActiveRequestEP13QNetworkReplyPK7QObjectSt10unique_ptrIN9QtPrivate15QSlotObjectBaseENS7_7DeleterEE
inline QNetworkReply *QRestAccessManagerPrivate::createActiveRequest(QNetworkReply *reply,
                                                    const QObject *contextObject,
                                                    QtPrivate::SlotObjUniquePtr slot)
{
    Q_Q(QRestAccessManager);
    Q_ASSERT(reply);
    [[maybe_unused]] const auto [_, inserted] =
        activeRequests.try_emplace(reply, CallerInfo{contextObject, std::move(slot)});
    Q_ASSERT(inserted); // if this fails, we have an ABA problem...

    // The signal connections below are made to 'q' to avoid stray signal
    // handling upon its destruction while requests were still in progress

    QObject::connect(reply, &QNetworkReply::finished, q, [reply, this]() {
        handleReplyFinished(reply);
    });
    // Safe guard in case reply is destroyed before it's finished
    QObject::connect(reply, &QObject::destroyed, q, [reply, this]() {
        activeRequests.remove(reply);
    });
    // If context object is destroyed, clean up any possible replies it had associated with it
    if (contextObject) {
        QObject::connect(contextObject, &QObject::destroyed, q, [reply, this]() {
            activeRequests.remove(reply);
        });
    }
    return reply;
}

//  from src/network/access/qrestaccessmanager.cpp, line 578, as _ZN25QRestAccessManagerPrivateC1Ev
inline QRestAccessManagerPrivate::QRestAccessManagerPrivate()
    = default;

//  from src/network/access/qrestaccessmanager.cpp, line 833, as _ZN25QRestAccessManagerPrivate19handleReplyFinishedEP13QNetworkReply
inline void QRestAccessManagerPrivate::handleReplyFinished(QNetworkReply *reply)
{
    auto request = activeRequests.find(reply);
    if (request == activeRequests.end()) {
        qCDebug(lcQrest, "QRestAccessManager: Unexpected reply received, ignoring");
        return;
    }

    CallerInfo caller = std::move(request.value());
    activeRequests.erase(request);

    if (caller.slot) {
        // Callback was provided
        QRestReply restReply(reply);
        void *argv[] = { nullptr, &restReply };
        // If we have context object, use it
        QObject *context = caller.contextObject
                ? const_cast<QObject*>(caller.contextObject.get()) : nullptr;
        caller.slot->call(context, argv);
    }
}

//  from src/network/access/qrestaccessmanager.cpp, line 855, as _ZN25QRestAccessManagerPrivate14executeRequestEN3qxp12function_refIJKFP13QNetworkReplyP21QNetworkAccessManagerEEEEPK7QObjectPN9QtPrivate15QSlotObjectBaseE
inline QNetworkReply *
QRestAccessManagerPrivate::executeRequest(ReqOpRef requestOperation, const QObject *context,
                                          QtPrivate::QSlotObjectBase *rawSlot)
{
    QtPrivate::SlotObjUniquePtr slot(rawSlot);
    if (!qnam)
        return warnNoAccessManager();
    verifyThreadAffinity(context);
    QNetworkReply *reply = requestOperation(qnam);
    return createActiveRequest(reply, context, std::move(slot));
}

//  from src/network/access/qrestaccessmanager.cpp, line 813, as _ZN25QRestAccessManagerPrivate20verifyThreadAffinityEPK7QObject
inline void QRestAccessManagerPrivate::verifyThreadAffinity(const QObject *contextObject)
{
    Q_Q(QRestAccessManager);
    if (QThread::currentThread() != q->thread()) {
        qCWarning(lcQrest, "QRestAccessManager can only be called in the thread it belongs to");
        Q_ASSERT(false);
    }
    if (contextObject && (contextObject->thread() != q->thread())) {
        qCWarning(lcQrest, "QRestAccessManager: the context object must reside in the same thread");
        Q_ASSERT(false);
    }
}
//  -----------------------------------------------------------------------

//  QRestAccessManagerPrivate::QRestAccessManagerPrivate()
extern "C" Q_DECL_EXPORT
QRestAccessManagerPrivate *ritual_ZN25QRestAccessManagerPrivateC1Ev() {
  return new QRestAccessManagerPrivate();
}

//  QRestAccessManagerPrivate::~QRestAccessManagerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRestAccessManagerPrivateD1Ev(
    QRestAccessManagerPrivate *self) {
  delete self;
}

//  void QRestAccessManagerPrivate::handleReplyFinished(QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRestAccessManagerPrivate19handleReplyFinishedEP13QNetworkReply(
    QRestAccessManagerPrivate *self,
    QNetworkReply *reply) {
  self->handleReplyFinished(reply);
}

//  QNetworkReply *QRestAccessManagerPrivate::executeRequest(ReqOpRef
//      requestOperation, const QObject *context, QtPrivate::QSlotObjectBase
//      *rawSlot)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN25QRestAccessManagerPrivate14executeRequestEN3qxp12function_refIJKFP13QNetworkReplyP21QNetworkAccessManagerEEEEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QRestAccessManagerPrivate *self,
    const QRestAccessManagerPrivate::ReqOpRef *requestOperation,
    const QObject *context,
    QtPrivate::QSlotObjectBase *rawSlot) {
  return self->executeRequest(*requestOperation, context, rawSlot);
}

//  void QRestAccessManagerPrivate::verifyThreadAffinity(const QObject
//      *contextObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QRestAccessManagerPrivate20verifyThreadAffinityEPK7QObject(
    QRestAccessManagerPrivate *self,
    const QObject *contextObject) {
  self->verifyThreadAffinity(contextObject);
}

//  QRestAccessManager *QRestAccessManagerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QRestAccessManager *ritual_ZN25QRestAccessManagerPrivate6q_funcEv(
    QRestAccessManagerPrivate *self) {
  return self->q_func();
}

//  const QRestAccessManager *QRestAccessManagerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRestAccessManager *ritual_ZNK25QRestAccessManagerPrivate6q_funcEv(
    const QRestAccessManagerPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(http)
