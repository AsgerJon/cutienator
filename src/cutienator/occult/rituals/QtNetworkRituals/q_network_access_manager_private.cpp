//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessmanager_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  'qnetworkaccessdebugpipebackend_p.h' is taken out. Qt installs that
//  header only when it is built with its feature 'private_tests', and
//  nothing in this file uses what it declares. Kept as it is when the
//  generator runs again.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhstsstore_p.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <utility>
#include <QtNetwork/private/qnetworkaccesscache_p.h>
#include "QtCore/qpointer.h"
#include "QtCore/qdeadlinetimer.h"
#include <QtNetwork/private/qnetworkaccessauthenticationmanager_p.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/private/qnetworkaccessmanager_p.h>
#include "QtCore/qbuffer.h"
#include "QtCore/qlist.h"
#include "QtCore/qurl.h"
#include "QtCore/QMutexLocker"
#include "QtNetwork/qauthenticator.h"
#include <algorithm>
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/private/qnetworkaccessmanager_p.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/private/qnetworkreply_p.h>
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/qnetworkcookiejar.h>
#include <QtNetwork/qabstractnetworkcache.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtNetwork/private/qhsts_p.h>
#if QT_CONFIG(settings)
#include <QtNetwork/private/qhstsstore_p.h>
#endif
#include <QtNetwork/private/qnetworkaccessfilebackend_p.h>
#include <QtNetwork/private/qnetworkaccesscachebackend_p.h>
#include <QtNetwork/private/qnetworkreplydataimpl_p.h>
#include <QtNetwork/private/qnetworkreplyfileimpl_p.h>
#include <QtNetwork/private/qnetworkaccessbackend_p.h>
#include <QtNetwork/private/qnetworkreplyimpl_p.h>
#include "QtCore/qbuffer.h"
#include "QtCore/qlist.h"
#include "QtCore/qurl.h"
#include "QtNetwork/private/qauthenticator_p.h"
#include "QtNetwork/qsslconfiguration.h"
#if QT_CONFIG(http)
#include "QtNetwork/private/http2protocol_p.h"
#include <QtNetwork/qhttpmultipart.h>
#include <QtNetwork/private/qhttpmultipart_p.h>
#include <QtNetwork/private/qnetworkreplyhttpimpl_p.h>
#endif
#include <QtCore/qthread.h>
#include <QtNetwork/QHostInfo>
#include "QtCore/qapplicationstatic.h"
#include "QtCore/qloggingcategory.h"
#include <QtCore/private/qfactoryloader_p.h>
#if defined(Q_OS_MACOS)
#include <QtCore/private/qcore_mac_p.h>
#include <CoreServices/CoreServices.h>
#include <SystemConfiguration/SystemConfiguration.h>
#include <Security/Security.h>
#endif
#ifdef Q_OS_WASM
#include <QtNetwork/private/qnetworkreplywasmimpl_p.h>
#include <QtNetwork/qhttpmultipart.h>
#include <QtNetwork/private/qhttpmultipart_p.h>
#endif
#include <mutex>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhstsstore.cpp, line 41, as _ZN10QHstsStoreD1Ev
inline QHstsStore::~QHstsStore()
{
    synchronize();
}

//  from src/network/access/qnetworkaccesscache.cpp, line 46, as _ZN19QNetworkAccessCacheD1Ev
inline QNetworkAccessCache::~QNetworkAccessCache()
{
    clear();
}

//  from src/network/access/qnetworkaccessauthenticationmanager.cpp, line 272, as _ZN35QNetworkAccessAuthenticationManager10clearCacheEv
inline void QNetworkAccessAuthenticationManager::clearCache()
{
    authenticationCache.clear();
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1748, as _ZN28QNetworkAccessManagerPrivateD1Ev
inline QNetworkAccessManagerPrivate::~QNetworkAccessManagerPrivate()
{
    destroyThread();
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1753, as _ZN28QNetworkAccessManagerPrivate12createThreadEv
inline QThread * QNetworkAccessManagerPrivate::createThread()
{
    if (!thread) {
        thread = new QThread;
        thread->setObjectName(QStringLiteral("QNetworkAccessManager thread"));
        thread->start();
    }
    Q_ASSERT(thread);
    return thread;
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1764, as _ZN28QNetworkAccessManagerPrivate13destroyThreadEv
inline void QNetworkAccessManagerPrivate::destroyThread()
{
    if (thread) {
        thread->quit();
        thread->wait(QDeadlineTimer(5000));
        if (thread->isFinished())
            delete thread;
        else
            QObject::connect(thread, SIGNAL(finished()), thread, SLOT(deleteLater()));
        thread = nullptr;
    }
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1554, as _ZN28QNetworkAccessManagerPrivate16_q_replyFinishedEP13QNetworkReply
inline void QNetworkAccessManagerPrivate::_q_replyFinished(QNetworkReply *reply)
{
    Q_Q(QNetworkAccessManager);

    emit q->finished(reply);
    if (reply->request().attribute(QNetworkRequest::AutoDeleteReplyOnFinishAttribute, false).toBool())
        QMetaObject::invokeMethod(reply, [reply] { reply->deleteLater(); }, Qt::QueuedConnection);
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1563, as _ZN28QNetworkAccessManagerPrivate17_q_replyEncryptedEP13QNetworkReply
inline void QNetworkAccessManagerPrivate::_q_replyEncrypted(QNetworkReply *reply)
{
#ifndef QT_NO_SSL
    Q_Q(QNetworkAccessManager);
    emit q->encrypted(reply);
#else
    Q_UNUSED(reply);
#endif
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1573, as _ZN28QNetworkAccessManagerPrivate17_q_replySslErrorsERK5QListI9QSslErrorE
inline void QNetworkAccessManagerPrivate::_q_replySslErrors(const QList<QSslError> &errors)
{
#ifndef QT_NO_SSL
    Q_Q(QNetworkAccessManager);
    QNetworkReply *reply = qobject_cast<QNetworkReply *>(q->sender());
    if (reply)
        emit q->sslErrors(reply, errors);
#else
    Q_UNUSED(errors);
#endif
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1586, as _ZN28QNetworkAccessManagerPrivate42_q_replyPreSharedKeyAuthenticationRequiredEP29QSslPreSharedKeyAuthenticator
#if !defined(QT_NO_SSL)
inline void QNetworkAccessManagerPrivate::_q_replyPreSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator *authenticator)
{
    Q_Q(QNetworkAccessManager);
    QNetworkReply *reply = qobject_cast<QNetworkReply *>(q->sender());
    if (reply)
    emit q->preSharedKeyAuthenticationRequired(reply, authenticator);
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkaccessmanager.cpp, line 1595, as _ZN28QNetworkAccessManagerPrivate11postProcessEP13QNetworkReply
inline QNetworkReply *QNetworkAccessManagerPrivate::postProcess(QNetworkReply *reply)
{
    Q_Q(QNetworkAccessManager);
    QNetworkReplyPrivate::setManager(reply, q);
    q->connect(reply, &QNetworkReply::finished, reply,
               [this, reply]() { _q_replyFinished(reply); });
#ifndef QT_NO_SSL
    /* In case we're compiled without SSL support, we don't have this signal and we need to
     * avoid getting a connection error. */
    q->connect(reply, &QNetworkReply::encrypted, reply,
               [this, reply]() { _q_replyEncrypted(reply); });
    q->connect(reply, SIGNAL(sslErrors(QList<QSslError>)), SLOT(_q_replySslErrors(QList<QSslError>)));
    q->connect(reply, SIGNAL(preSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*)), SLOT(_q_replyPreSharedKeyAuthenticationRequired(QSslPreSharedKeyAuthenticator*)));
#endif

    return reply;
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1613, as _ZNK28QNetworkAccessManagerPrivate15createCookieJarEv
inline void QNetworkAccessManagerPrivate::createCookieJar() const
{
    if (!cookieJarCreated) {
        // keep the ugly hack in here
        QNetworkAccessManagerPrivate *that = const_cast<QNetworkAccessManagerPrivate *>(this);
        that->cookieJar = new QNetworkCookieJar(that->q_func());
        that->cookieJarCreated = true;
    }
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1717, as _ZN28QNetworkAccessManagerPrivate10queryProxyERK18QNetworkProxyQuery
#if !defined(QT_NO_NETWORKPROXY)
inline QList<QNetworkProxy> QNetworkAccessManagerPrivate::queryProxy(const QNetworkProxyQuery &query)
{
    QList<QNetworkProxy> proxies;
    if (proxyFactory) {
        proxies = proxyFactory->queryProxy(query);
        if (proxies.isEmpty()) {
            qWarning("QNetworkAccessManager: factory %p has returned an empty result set",
                     proxyFactory);
            proxies << QNetworkProxy::NoProxy;
        }
    } else if (proxy.type() == QNetworkProxy::DefaultProxy) {
        // no proxy set, query the application
        return QNetworkProxyFactory::proxyForQuery(query);
    } else {
        proxies << proxy;
    }

    return proxies;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/access/qnetworkaccessmanager.cpp, line 1743, as _ZN28QNetworkAccessManagerPrivate20clearConnectionCacheEP21QNetworkAccessManager
inline void QNetworkAccessManagerPrivate::clearConnectionCache(QNetworkAccessManager *manager)
{
    manager->d_func()->destroyThread();
}
//  -----------------------------------------------------------------------

//  QNetworkAccessManagerPrivate::~QNetworkAccessManagerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivateD1Ev(
    QNetworkAccessManagerPrivate *self) {
  delete self;
}

//  QThread *QNetworkAccessManagerPrivate::createThread()
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN28QNetworkAccessManagerPrivate12createThreadEv(
    QNetworkAccessManagerPrivate *self) {
  return self->createThread();
}

//  void QNetworkAccessManagerPrivate::destroyThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivate13destroyThreadEv(
    QNetworkAccessManagerPrivate *self) {
  self->destroyThread();
}

//  void QNetworkAccessManagerPrivate::_q_replyFinished(QNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivate16_q_replyFinishedEP13QNetworkReply(
    QNetworkAccessManagerPrivate *self,
    QNetworkReply *reply) {
  self->_q_replyFinished(reply);
}

//  void QNetworkAccessManagerPrivate::_q_replyEncrypted(QNetworkReply
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivate17_q_replyEncryptedEP13QNetworkReply(
    QNetworkAccessManagerPrivate *self,
    QNetworkReply *reply) {
  self->_q_replyEncrypted(reply);
}

//  void QNetworkAccessManagerPrivate::_q_replySslErrors(const
//      QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivate17_q_replySslErrorsERK5QListI9QSslErrorE(
    QNetworkAccessManagerPrivate *self,
    const QList<QSslError> *errors) {
  self->_q_replySslErrors(*errors);
}

#if !defined(QT_NO_SSL)
//  void QNetworkAccessManagerPrivate::_q_replyPreSharedKeyAuthenticationRequ
//      ired(QSslPreSharedKeyAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivate42_q_replyPreSharedKeyAuthenticationRequiredEP29QSslPreSharedKeyAuthenticator(
    QNetworkAccessManagerPrivate *self,
    QSslPreSharedKeyAuthenticator *authenticator) {
  self->_q_replyPreSharedKeyAuthenticationRequired(authenticator);
}
#endif  // !defined(QT_NO_SSL)

//  QNetworkReply *QNetworkAccessManagerPrivate::postProcess(QNetworkReply
//      *reply)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN28QNetworkAccessManagerPrivate11postProcessEP13QNetworkReply(
    QNetworkAccessManagerPrivate *self,
    QNetworkReply *reply) {
  return self->postProcess(reply);
}

//  void QNetworkAccessManagerPrivate::createCookieJar() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QNetworkAccessManagerPrivate15createCookieJarEv(
    const QNetworkAccessManagerPrivate *self) {
  self->createCookieJar();
}

#if !defined(QT_NO_NETWORKPROXY)
//  QList<QNetworkProxy> QNetworkAccessManagerPrivate::queryProxy(const
//      QNetworkProxyQuery &query)
extern "C" Q_DECL_EXPORT
QList<QNetworkProxy> *ritual_ZN28QNetworkAccessManagerPrivate10queryProxyERK18QNetworkProxyQuery(
    QNetworkAccessManagerPrivate *self,
    const QNetworkProxyQuery *query) {
  return new QList<QNetworkProxy>(self->queryProxy(*query));
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void
//      QNetworkAccessManagerPrivate::clearConnectionCache(QNetworkAccessMana
//      ger *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkAccessManagerPrivate20clearConnectionCacheEP21QNetworkAccessManager(
    QNetworkAccessManager *manager) {
  QNetworkAccessManagerPrivate::clearConnectionCache(manager);
}

//  QNetworkAccessManager *QNetworkAccessManagerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZN28QNetworkAccessManagerPrivate6q_funcEv(
    QNetworkAccessManagerPrivate *self) {
  return self->q_func();
}

//  const QNetworkAccessManager *QNetworkAccessManagerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNetworkAccessManager *ritual_ZNK28QNetworkAccessManagerPrivate6q_funcEv(
    const QNetworkAccessManagerPrivate *self) {
  return self->q_func();
}
