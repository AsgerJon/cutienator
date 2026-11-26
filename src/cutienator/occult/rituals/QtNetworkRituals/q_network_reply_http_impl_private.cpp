//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyhttpimpl_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: took out the include of
//  qnetworkaccessdebugpipebackend_p.h, which Qt installs only when built
//  with private tests, and which no ritual here needs. Kept as it is when
//  the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyhttpimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/private/qnetworkreply_p.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qnetworkreplyhttpimpl_p.h>
#include <QtNetwork/private/qnetworkaccessmanager_p.h>
#include <QtNetwork/private/qnetworkaccesscache_p.h>
#include <QtNetwork/qabstractnetworkcache.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/private/qnetworkcookie_p.h>
#include "QtCore/qdatetime.h"
#include "QtCore/qelapsedtimer.h"
#include "QtNetwork/qsslconfiguration.h"
#include <QtNetwork/private/qhttpthreaddelegate_p.h>
#include <QtNetwork/private/qhsts_p.h>
#include <QtCore/qthread.h>
#include "QtCore/qcoreapplication.h"
#include <QtCore/private/qthread_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtNetwork/qnetworkcookiejar.h>
#include <QtNetwork/private/qnetworkreplyimpl_p.h>
#include <string.h>             // for strchr
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include "qplatformdefs.h"
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qhttpheadershelper_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/qhttp1configuration.h>
#include <QtNetwork/qhttp2configuration.h>
#include <QtNetwork/private/http2protocol_p.h>
#endif
#include "QtCore/qdatetime.h"
#include "QtCore/qlocale.h"
#include "QtCore/qshareddata.h"
#include "QtCore/qtimezone.h"
#include "QtCore/private/qduplicatetracker_p.h"
#include "QtCore/private/qtools_p.h"
#if QT_CONFIG(datestring)
# include <stdio.h>
#endif
#include <algorithm>
#include <QtCore/q20algorithm.h>
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qnetworkreply.cpp, line 17, as _ZN20QNetworkReplyPrivateC2Ev
inline QNetworkReplyPrivate::QNetworkReplyPrivate()
    : readBufferMaxSize(0),
      emitAllUploadProgressSignals(false),
      operation(QNetworkAccessManager::UnknownOperation),
      errorCode(QNetworkReply::NoError)
    , isFinished(false)
{
    // set the default attribute values
    attributes.insert(QNetworkRequest::ConnectionEncryptedAttribute, false);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 278, as _ZN21QNetworkReplyHttpImpl9abortImplEN13QNetworkReply12NetworkErrorE
inline void QNetworkReplyHttpImpl::abortImpl(QNetworkReply::NetworkError error)
{
    Q_D(QNetworkReplyHttpImpl);
    // FIXME
    if (d->state == QNetworkReplyPrivate::Finished || d->state == QNetworkReplyPrivate::Aborted)
        return;

    QNetworkReply::close();

    if (d->state != QNetworkReplyPrivate::Finished) {
        // call finished which will emit signals
        // FIXME shouldn't this be emitted Queued?
        d->error(error,
                 error == TimeoutError ? tr("Operation timed out") : tr("Operation canceled"));
        d->finished();
    }

    d->state = QNetworkReplyPrivate::Aborted;

    emit abortHttpRequest();
}

//  from src/network/access/qnetworkrequest.cpp, line 1885, as _ZN22QNetworkHeadersPrivate5toIntE14QByteArrayView
inline std::optional<qint64> QNetworkHeadersPrivate::toInt(QByteArrayView value)
{
    if (value.empty())
        return std::nullopt;

    bool ok;
    qint64 res = value.toLongLong(&ok);
    if (ok)
        return res;
    return std::nullopt;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 219, as _ZNK19QHttpNetworkRequest17isFollowRedirectsEv
inline bool QHttpNetworkRequest::isFollowRedirects() const
{
    return d->redirectPolicy != QNetworkRequest::ManualRedirectPolicy;
}

//  from src/network/access/qnetworkrequest.cpp, line 1669, as _ZNK22QNetworkHeadersPrivate7headersEv
inline QHttpHeaders QNetworkHeadersPrivate::headers() const
{
    return httpHeaders;
}

//  from src/network/access/qnetworkrequest.cpp, line 1897, as _ZN22QNetworkHeadersPrivate15toSetCookieListERK5QListI10QByteArrayE
inline std::optional<QNetworkHeadersPrivate::NetworkCookieList> QNetworkHeadersPrivate::toSetCookieList(
        const QList<QByteArray> &values)
{
    if (values.empty())
        return std::nullopt;

    QList<QNetworkCookie> cookies;
    for (const auto &s : values)
        cookies += QNetworkCookie::parseCookies(s);

    if (cookies.empty())
        return std::nullopt;
    return cookies;
}

//  from src/network/access/qnetworkrequest.cpp, line 1700, as _ZN22QNetworkHeadersPrivate12clearHeadersEv
inline void QNetworkHeadersPrivate::clearHeaders()
{
    httpHeaders.clear();
    cookedHeaders.clear();
    invalidateHeaderCache();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 192, as _ZNK19QHttpNetworkRequest3urlEv
inline QUrl QHttpNetworkRequest::url() const
{
    return d->url;
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1623, as _ZN28QNetworkAccessManagerPrivate22authenticationRequiredEP14QAuthenticatorP13QNetworkReplybR4QUrlPS4_b
inline void QNetworkAccessManagerPrivate::authenticationRequired(QAuthenticator *authenticator,
                                                          QNetworkReply *reply,
                                                          bool synchronous,
                                                          QUrl &url,
                                                          QUrl *urlForLastAuthentication,
                                                          bool allowAuthenticationReuse)
{
    Q_Q(QNetworkAccessManager);

    // don't try the cache for the same URL twice in a row
    // being called twice for the same URL means the authentication failed
    // also called when last URL is empty, e.g. on first call
    if (allowAuthenticationReuse && (urlForLastAuthentication->isEmpty()
            || url != *urlForLastAuthentication)) {
        // if credentials are included in the url, then use them, unless they were already used
        if (!url.userName().isEmpty() && !url.password().isEmpty()
            && (url.userName() != authenticator->user()
                || url.password() != authenticator->password())) {
            authenticator->setUser(url.userName(QUrl::FullyDecoded));
            authenticator->setPassword(url.password(QUrl::FullyDecoded));
            *urlForLastAuthentication = url;
            authenticationManager->cacheCredentials(url, authenticator);
            return;
        }

        QNetworkAuthenticationCredential cred = authenticationManager->fetchCachedCredentials(url, authenticator);
        if (!cred.isNull()
            && (cred.user != authenticator->user() || cred.password != authenticator->password())) {
            authenticator->setUser(cred.user);
            authenticator->setPassword(cred.password);
            *urlForLastAuthentication = url;
            return;
        }
    }

    // if we emit a signal here in synchronous mode, the user might spin
    // an event loop, which might recurse and lead to problems
    if (synchronous)
        return;

    *urlForLastAuthentication = url;
    emit q->authenticationRequired(reply, authenticator);
    if (allowAuthenticationReuse)
        authenticationManager->cacheCredentials(url, authenticator);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 361, as _ZNK19QHttpNetworkRequest15withCredentialsEv
inline bool QHttpNetworkRequest::withCredentials() const
{
    return d->withCredentials;
}

//  from src/network/access/qnetworkaccessmanager.cpp, line 1670, as _ZN28QNetworkAccessManagerPrivate27proxyAuthenticationRequiredERK4QUrlRK13QNetworkProxybP14QAuthenticatorPS3_
#if !defined(QT_NO_NETWORKPROXY)
#if defined(Q_OS_LINUX)
inline void QNetworkAccessManagerPrivate::proxyAuthenticationRequired(const QUrl &url,
                                                               const QNetworkProxy &proxy,
                                                               bool synchronous,
                                                               QAuthenticator *authenticator,
                                                               QNetworkProxy *lastProxyAuthentication)
{
    Q_Q(QNetworkAccessManager);
    QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(*authenticator);
    if (proxy != *lastProxyAuthentication && (!priv || !priv->hasFailed)) {
        QNetworkAuthenticationCredential cred = authenticationManager->fetchCachedProxyCredentials(proxy);
        if (!cred.isNull()) {
            authenticator->setUser(cred.user);
            authenticator->setPassword(cred.password);
            return;
        }
    }

#if defined(Q_OS_MACOS)
    //now we try to get the username and password from keychain
    //if not successful signal will be emitted
    QString username;
    QString password;
    if (getProxyAuth(proxy.hostName(), url.scheme(), username, password)) {
        // only cache the system credentials if they are correct (or if they have changed)
        // to not run into an endless loop in case they are wrong
        QNetworkAuthenticationCredential cred = authenticationManager->fetchCachedProxyCredentials(proxy);
        if (!priv->hasFailed || cred.user != username || cred.password != password) {
            authenticator->setUser(username);
            authenticator->setPassword(password);
            authenticationManager->cacheProxyCredentials(proxy, authenticator);
            return;
        }
    }
#else
    Q_UNUSED(url);
#endif

    // if we emit a signal here in synchronous mode, the user might spin
    // an event loop, which might recurse and lead to problems
    if (synchronous)
        return;

    *lastProxyAuthentication = proxy;
    emit q->proxyAuthenticationRequired(proxy, authenticator);
    authenticationManager->cacheProxyCredentials(proxy, authenticator);
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/access/qnetworkrequest.cpp, line 1932, as _ZN22QNetworkHeadersPrivate21invalidateHeaderCacheEv
inline void QNetworkHeadersPrivate::invalidateHeaderCache()
{
    rawHeaderCache.headersList.clear();
    rawHeaderCache.isCached = false;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 643, as _ZN28QNetworkReplyHttpImplPrivate7convertEN15QNetworkRequest8PriorityE
inline QHttpNetworkRequest::Priority QNetworkReplyHttpImplPrivate::convert(QNetworkRequest::Priority prio)
{
    switch (prio) {
    case QNetworkRequest::LowPriority:
        return QHttpNetworkRequest::LowPriority;
    case QNetworkRequest::HighPriority:
        return QHttpNetworkRequest::HighPriority;
    case QNetworkRequest::NormalPriority:
        return QHttpNetworkRequest::NormalPriority;
    }
    Q_UNREACHABLE_RETURN(QHttpNetworkRequest::NormalPriority);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 498, as _ZN28QNetworkReplyHttpImplPrivateD1Ev
inline QNetworkReplyHttpImplPrivate::~QNetworkReplyHttpImplPrivate()
{
    if (cacheSaveDevice)
        managerPrivate->networkCache->remove(url);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2097, as _ZN28QNetworkReplyHttpImplPrivate21_q_bufferOutgoingDataEv
inline void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingData()
{
    Q_Q(QNetworkReplyHttpImpl);

    if (!outgoingDataBuffer) {
        // first call, create our buffer
        outgoingDataBuffer = std::make_shared<QRingBuffer>();

        QObject::connect(outgoingData, SIGNAL(readyRead()), q, SLOT(_q_bufferOutgoingData()));
        QObject::connect(outgoingData, SIGNAL(readChannelFinished()), q, SLOT(_q_bufferOutgoingDataFinished()));
    }

    qint64 bytesBuffered = 0;
    qint64 bytesToBuffer = 0;

    // read data into our buffer
    forever {
        bytesToBuffer = outgoingData->bytesAvailable();
        // unknown? just try 2 kB, this also ensures we always try to read the EOF
        if (bytesToBuffer <= 0)
            bytesToBuffer = 2*1024;

        char *dst = outgoingDataBuffer->reserve(bytesToBuffer);
        bytesBuffered = outgoingData->read(dst, bytesToBuffer);

        if (bytesBuffered == -1) {
            // EOF has been reached.
            outgoingDataBuffer->chop(bytesToBuffer);

            _q_bufferOutgoingDataFinished();
            break;
        } else if (bytesBuffered == 0) {
            // nothing read right now, just wait until we get called again
            outgoingDataBuffer->chop(bytesToBuffer);

            break;
        } else {
            // don't break, try to read() again
            outgoingDataBuffer->chop(bytesToBuffer - bytesBuffered);
        }
    }
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2073, as _ZN28QNetworkReplyHttpImplPrivate29_q_bufferOutgoingDataFinishedEv
inline void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingDataFinished()
{
    Q_Q(QNetworkReplyHttpImpl);

    // make sure this is only called once, ever.
    //_q_bufferOutgoingData may call it or the readChannelFinished emission
    if (state != Buffering)
        return;

    // disconnect signals
    QObject::disconnect(outgoingData, SIGNAL(readyRead()), q, SLOT(_q_bufferOutgoingData()));
    QObject::disconnect(outgoingData, SIGNAL(readChannelFinished()), q, SLOT(_q_bufferOutgoingDataFinished()));

    // finally, start the request
    QMetaObject::invokeMethod(q, "_q_startOperation", Qt::QueuedConnection);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2090, as _ZN28QNetworkReplyHttpImplPrivate30_q_cacheSaveDeviceAboutToCloseEv
inline void QNetworkReplyHttpImplPrivate::_q_cacheSaveDeviceAboutToClose()
{
    // do not keep a dangling pointer to the device around (device
    // is closing because e.g. QAbstractNetworkCache::remove() was called).
    cacheSaveDevice = nullptr;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2207, as _ZN28QNetworkReplyHttpImplPrivate11_q_finishedEv
inline void QNetworkReplyHttpImplPrivate::_q_finished()
{
    // This gets called queued, just forward to real call then
    finished();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2213, as _ZN28QNetworkReplyHttpImplPrivate8finishedEv
inline void QNetworkReplyHttpImplPrivate::finished()
{
    Q_Q(QNetworkReplyHttpImpl);
    if (transferTimeout)
      transferTimeout->stop();
    if (state == Finished || state == Aborted)
        return;

    const auto totalSizeOpt = QNetworkHeadersPrivate::toInt(
            headers().value(QHttpHeaders::WellKnownHeader::ContentLength));
    const qint64 totalSize = totalSizeOpt.value_or(-1);

    // if we don't know the total size of or we received everything save the cache.
    // If the data is compressed then this is done in readData()
    if ((totalSize == -1 || bytesDownloaded == totalSize)
        && !decompressHelper.isValid()) {
        completeCacheSave();
    }

    // We check for errorCode too as in case of SSL handshake failure, we still
    // get the HTTP redirect status code (301, 303 etc)
    if (isHttpRedirectResponse() && errorCode == QNetworkReply::NoError)
        return;

    state = Finished;
    q->setFinished(true);

    if (totalSize == -1) {
        emit q->downloadProgress(bytesDownloaded, bytesDownloaded);
    } else {
        emit q->downloadProgress(bytesDownloaded, totalSize);
    }

    if (bytesUploaded == -1 && (outgoingData || outgoingDataBuffer))
        emit q->uploadProgress(0, 0);

    emit q->readChannelFinished();
    emit q->finished();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2259, as _ZN28QNetworkReplyHttpImplPrivate5errorEN13QNetworkReply12NetworkErrorERK7QString
inline void QNetworkReplyHttpImplPrivate::error(QNetworkReplyImpl::NetworkError code, const QString &errorMessage)
{
    Q_Q(QNetworkReplyHttpImpl);
    // Can't set and emit multiple errors.
    if (errorCode != QNetworkReply::NoError) {
        // But somewhat unavoidable if we have cancelled the request:
        if (errorCode != QNetworkReply::OperationCanceledError
            && errorCode != QNetworkReply::TimeoutError) {
            qWarning("QNetworkReplyImplPrivate::error: Internal problem, this method must only be called once.");
        }
        return;
    }

    errorCode = code;
    q->setErrorString(errorMessage);

    // note: might not be a good idea, since users could decide to delete us
    // which would delete the backend too...
    // maybe we should protect the backend
    emit q->errorOccurred(code);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2253, as _ZN28QNetworkReplyHttpImplPrivate8_q_errorEN13QNetworkReply12NetworkErrorERK7QString
inline void QNetworkReplyHttpImplPrivate::_q_error(QNetworkReplyImpl::NetworkError code, const QString &errorMessage)
{
    this->error(code, errorMessage);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2281, as _ZN28QNetworkReplyHttpImplPrivate18_q_metaDataChangedEv
inline void QNetworkReplyHttpImplPrivate::_q_metaDataChanged()
{
    // FIXME merge this with replyDownloadMetaData(); ?

    Q_Q(QNetworkReplyHttpImpl);
    // 1. do we have cookies?
    // 2. are we allowed to set them?
    Q_ASSERT(manager);

    const auto cookiesOpt = QNetworkHeadersPrivate::toSetCookieList(
            headers().values(QHttpHeaders::WellKnownHeader::SetCookie));
    const auto cookies = cookiesOpt.value_or(QList<QNetworkCookie>());
    if (!cookies.empty()
        && request.attribute(QNetworkRequest::CookieSaveControlAttribute,
                                QNetworkRequest::Automatic).toInt() == QNetworkRequest::Automatic) {
        QNetworkCookieJar *jar = manager->cookieJar();
        if (jar) {
            jar->setCookiesFromUrl(cookies, url);
        }
    }
    emit q->metaDataChanged();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 656, as _ZN28QNetworkReplyHttpImplPrivate21maybeDropUploadDeviceERK15QNetworkRequest
inline void QNetworkReplyHttpImplPrivate::maybeDropUploadDevice(const QNetworkRequest &newHttpRequest)
{
    // Check for 0-length upload device. Following RFC9110, we are discouraged
    // from sending "content-length: 0" for methods where a content-length would
    // not normally be expected. E.g. get, connect, head, delete
    // https://www.rfc-editor.org/rfc/rfc9110.html#section-8.6-5
    auto contentLength0Allowed = [&]{
        switch (operation) {
        case QNetworkAccessManager::CustomOperation: {
            const QByteArray customVerb = newHttpRequest.attribute(QNetworkRequest::CustomVerbAttribute)
                                                .toByteArray();
            if (customVerb.compare("connect", Qt::CaseInsensitive) != 0)
                return true; // Trust user => content-length 0 is presumably okay!
            // else:
            [[fallthrough]];
        }
        case QNetworkAccessManager::HeadOperation:
        case QNetworkAccessManager::GetOperation:
        case QNetworkAccessManager::DeleteOperation:
            // no content-length 0
            return false;
        case QNetworkAccessManager::PutOperation:
        case QNetworkAccessManager::PostOperation:
        case QNetworkAccessManager::UnknownOperation:
            // yes content-length 0
            return true;
        }
        Q_UNREACHABLE_RETURN(false);
    };

    const auto hasEmptyOutgoingPayload = [&]() {
        if (!outgoingData)
            return false;
        if (outgoingDataBuffer)
            return outgoingDataBuffer->isEmpty();
        return outgoingData->size() == 0;
    };
    if (Q_UNLIKELY(hasEmptyOutgoingPayload()) && !contentLength0Allowed()) {
        outgoingData = nullptr;
        outgoingDataBuffer.reset();
    }
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2187, as _ZN28QNetworkReplyHttpImplPrivate22createUploadByteDeviceEv
inline QNonContiguousByteDevice* QNetworkReplyHttpImplPrivate::createUploadByteDevice()
{
    Q_Q(QNetworkReplyHttpImpl);

    if (outgoingDataBuffer)
        uploadByteDevice = QNonContiguousByteDeviceFactory::createShared(outgoingDataBuffer);
    else if (outgoingData) {
        uploadByteDevice = QNonContiguousByteDeviceFactory::createShared(outgoingData);
    } else {
        return nullptr;
    }

    // We want signal emissions only for normal asynchronous uploads
    if (!synchronous)
        QObject::connect(uploadByteDevice.get(), SIGNAL(readProgress(qint64,qint64)),
                         q, SLOT(emitReplyUploadProgress(qint64,qint64)));

    return uploadByteDevice.get();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2304, as _ZN28QNetworkReplyHttpImplPrivate11createCacheEv
inline void QNetworkReplyHttpImplPrivate::createCache()
{
    // check if we can save and if we're allowed to
    if (!managerPrivate->networkCache
        || !request.attribute(QNetworkRequest::CacheSaveControlAttribute, true).toBool())
        return;
    cacheEnabled = true;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2349, as _ZN28QNetworkReplyHttpImplPrivate17completeCacheSaveEv
inline void QNetworkReplyHttpImplPrivate::completeCacheSave()
{
    if (cacheEnabled && errorCode != QNetworkReplyImpl::NoError) {
        managerPrivate->networkCache->remove(url);
    } else if (cacheEnabled && cacheSaveDevice) {
        managerPrivate->networkCache->insert(cacheSaveDevice);
    }
    cacheSaveDevice = nullptr;
    cacheEnabled = false;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2318, as _ZN28QNetworkReplyHttpImplPrivate17setCachingEnabledEb
inline void QNetworkReplyHttpImplPrivate::setCachingEnabled(bool enable)
{
    if (!enable && !cacheEnabled)
        return;                 // nothing to do
    if (enable && cacheEnabled)
        return;                 // nothing to do either!

    if (enable) {
        if (Q_UNLIKELY(bytesDownloaded)) {
            qDebug() << "setCachingEnabled: " << bytesDownloaded << " bytesDownloaded";
            // refuse to enable in this case
            qCritical("QNetworkReplyImpl: backend error: caching was enabled after some bytes had been written");
            return;
        }

        createCache();
    } else {
        // someone told us to turn on, then back off?
        // ok... but you should make up your mind
        qDebug("QNetworkReplyImpl: setCachingEnabled(true) called after setCachingEnabled(false)");
        managerPrivate->networkCache->remove(url);
        cacheSaveDevice = nullptr;
        cacheEnabled = false;
    }
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2313, as _ZNK28QNetworkReplyHttpImplPrivate16isCachingEnabledEv
inline bool QNetworkReplyHttpImplPrivate::isCachingEnabled() const
{
    return (cacheEnabled && managerPrivate->networkCache != nullptr);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 2344, as _ZNK28QNetworkReplyHttpImplPrivate16isCachingAllowedEv
inline bool QNetworkReplyHttpImplPrivate::isCachingAllowed() const
{
    return operation == QNetworkAccessManager::GetOperation || operation == QNetworkAccessManager::HeadOperation;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1987, as _ZN28QNetworkReplyHttpImplPrivate15setResumeOffsetEy
inline void QNetworkReplyHttpImplPrivate::setResumeOffset(quint64 offset)
{
    resumeOffset = offset;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1095, as _ZN28QNetworkReplyHttpImplPrivate15invalidateCacheEv
inline void QNetworkReplyHttpImplPrivate::invalidateCache()
{
    QAbstractNetworkCache *nc = managerPrivate->networkCache;
    if (nc)
        nc->remove(httpRequest.url());
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1270, as _ZN28QNetworkReplyHttpImplPrivate20getRedirectOperationEN21QNetworkAccessManager9OperationEi
inline QNetworkAccessManager::Operation QNetworkReplyHttpImplPrivate::getRedirectOperation(QNetworkAccessManager::Operation currentOp, int httpStatus)
{
    // HTTP status code can be used to decide if we can redirect with a GET
    // operation or not. See http://www.ietf.org/rfc/rfc2616.txt [Sec 10.3] for
    // more details

    // We MUST keep using the verb that was used originally when being redirected with 307 or 308.
    if (httpStatus == 307 || httpStatus == 308)
        return currentOp;

    switch (currentOp) {
    case QNetworkAccessManager::HeadOperation:
        return QNetworkAccessManager::HeadOperation;
    default:
        break;
    }
    // Use GET for everything else.
    return QNetworkAccessManager::GetOperation;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1295, as _ZN28QNetworkReplyHttpImplPrivate21createRedirectRequestERK15QNetworkRequestRK4QUrli
inline QNetworkRequest QNetworkReplyHttpImplPrivate::createRedirectRequest(const QNetworkRequest &originalRequest,
                                                                    const QUrl &url,
                                                                    int maxRedirectsRemaining)
{
    QNetworkRequest newRequest(originalRequest);
    newRequest.setUrl(url);
    newRequest.setMaximumRedirectsAllowed(maxRedirectsRemaining);

    return newRequest;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1290, as _ZNK28QNetworkReplyHttpImplPrivate22isHttpRedirectResponseEv
inline bool QNetworkReplyHttpImplPrivate::isHttpRedirectResponse() const
{
    return httpRequest.isFollowRedirects() && QHttpNetworkReply::isHttpRedirect(statusCode);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1260, as _ZN28QNetworkReplyHttpImplPrivate13replyFinishedEv
inline void QNetworkReplyHttpImplPrivate::replyFinished()
{
    // We are already loading from cache, we still however
    // got this signal because it was posted already
    if (loadingFromCache)
        return;

    finished();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1616, as _ZN28QNetworkReplyHttpImplPrivate9httpErrorEN13QNetworkReply12NetworkErrorERK7QString
inline void QNetworkReplyHttpImplPrivate::httpError(QNetworkReply::NetworkError errorCode,
                                          const QString &errorString)
{
#if defined(QNETWORKACCESSHTTPBACKEND_DEBUG)
    qDebug() << "http error!" << errorCode << errorString;
#endif

    // FIXME?
    error(errorCode, errorString);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1628, as _ZN28QNetworkReplyHttpImplPrivate14replyEncryptedEv
#if !defined(QT_NO_SSL)
inline void QNetworkReplyHttpImplPrivate::replyEncrypted()
{
    Q_Q(QNetworkReplyHttpImpl);
    emit q->encrypted();
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1634, as _ZN28QNetworkReplyHttpImplPrivate14replySslErrorsERK5QListI9QSslErrorEPbPS2_
#if !defined(QT_NO_SSL)
inline void QNetworkReplyHttpImplPrivate::replySslErrors(
        const QList<QSslError> &list, bool *ignoreAll, QList<QSslError> *toBeIgnored)
{
    Q_Q(QNetworkReplyHttpImpl);
    emit q->sslErrors(list);
    // Check if the callback set any ignore and return this here to http thread
    if (pendingIgnoreAllSslErrors)
        *ignoreAll = true;
    if (!pendingIgnoreSslErrorsList.isEmpty())
        *toBeIgnored = pendingIgnoreSslErrorsList;
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1646, as _ZN28QNetworkReplyHttpImplPrivate28replySslConfigurationChangedERK17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QNetworkReplyHttpImplPrivate::replySslConfigurationChanged(const QSslConfiguration &newSslConfiguration)
{
    // Receiving the used SSL configuration from the HTTP thread
    if (sslConfiguration)
        *sslConfiguration = newSslConfiguration;
    else
        sslConfiguration.reset(new QSslConfiguration(newSslConfiguration));
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1655, as _ZN28QNetworkReplyHttpImplPrivate43replyPreSharedKeyAuthenticationRequiredSlotEP29QSslPreSharedKeyAuthenticator
#if !defined(QT_NO_SSL)
inline void QNetworkReplyHttpImplPrivate::replyPreSharedKeyAuthenticationRequiredSlot(QSslPreSharedKeyAuthenticator *authenticator)
{
    Q_Q(QNetworkReplyHttpImpl);
    emit q->preSharedKeyAuthenticationRequired(authenticator);
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1663, as _ZN28QNetworkReplyHttpImplPrivate19resetUploadDataSlotEPb
inline void QNetworkReplyHttpImplPrivate::resetUploadDataSlot(bool *r)
{
    *r = uploadByteDevice->reset();
    if (*r) {
        // reset our own position which is used for the inter-thread communication
        uploadByteDevicePosition = 0;
    }
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 1673, as _ZN28QNetworkReplyHttpImplPrivate18sentUploadDataSlotExx
inline void QNetworkReplyHttpImplPrivate::sentUploadDataSlot(qint64 pos, qint64 amount)
{
    if (!uploadByteDevice) // uploadByteDevice is no longer available
        return;

    if (uploadByteDevicePosition + amount != pos) {
        // Sanity check, should not happen.
        error(QNetworkReply::UnknownNetworkError, QString());
        return;
    }
    uploadByteDevice->advanceReadPointer(amount);
    uploadByteDevicePosition += amount;
}
//  -----------------------------------------------------------------------

//  A QNetworkReplyHttpImplPrivate that Python can take functions over in. Every QNetworkReplyHttpImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNetworkReplyHttpImplPrivateCall0)(const void *, char, int *);
typedef qint64 (*CuteQNetworkReplyHttpImplPrivateCall1)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQNetworkReplyHttpImplPrivateCall2)(const void *, qint64, int *);
class CuteQNetworkReplyHttpImplPrivate : public QNetworkReplyHttpImplPrivate {
public:
  using QNetworkReplyHttpImplPrivate::QNetworkReplyHttpImplPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEPcx")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplPrivateCall0 call = reinterpret_cast<CuteQNetworkReplyHttpImplPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplPrivateCall1 call = reinterpret_cast<CuteQNetworkReplyHttpImplPrivateCall1>(taken[1]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplPrivateCall2 call = reinterpret_cast<CuteQNetworkReplyHttpImplPrivateCall2>(taken[2]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QHttpNetworkRequest::Priority
//      QNetworkReplyHttpImplPrivate::convert(QNetworkRequest::Priority prio)
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest::Priority ritual_ZN28QNetworkReplyHttpImplPrivate7convertEN15QNetworkRequest8PriorityE(
    QNetworkRequest::Priority prio) {
  return QNetworkReplyHttpImplPrivate::convert(prio);
}

//  QNetworkReplyHttpImplPrivate::~QNetworkReplyHttpImplPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivateD1Ev(
    QNetworkReplyHttpImplPrivate *self) {
  delete self;
}

//  void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingData()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate21_q_bufferOutgoingDataEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->_q_bufferOutgoingData();
}

//  void QNetworkReplyHttpImplPrivate::_q_bufferOutgoingDataFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate29_q_bufferOutgoingDataFinishedEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->_q_bufferOutgoingDataFinished();
}

//  void QNetworkReplyHttpImplPrivate::_q_cacheSaveDeviceAboutToClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate30_q_cacheSaveDeviceAboutToCloseEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->_q_cacheSaveDeviceAboutToClose();
}

//  void QNetworkReplyHttpImplPrivate::_q_finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate11_q_finishedEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->_q_finished();
}

//  void QNetworkReplyHttpImplPrivate::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate8finishedEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->finished();
}

//  void QNetworkReplyHttpImplPrivate::error(QNetworkReply::NetworkError
//      code, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate5errorEN13QNetworkReply12NetworkErrorERK7QString(
    QNetworkReplyHttpImplPrivate *self,
    QNetworkReply::NetworkError code,
    const QString *errorString) {
  self->error(code, *errorString);
}

//  void QNetworkReplyHttpImplPrivate::_q_error(QNetworkReply::NetworkError
//      code, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate8_q_errorEN13QNetworkReply12NetworkErrorERK7QString(
    QNetworkReplyHttpImplPrivate *self,
    QNetworkReply::NetworkError code,
    const QString *errorString) {
  self->_q_error(code, *errorString);
}

//  void QNetworkReplyHttpImplPrivate::_q_metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate18_q_metaDataChangedEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->_q_metaDataChanged();
}

//  void QNetworkReplyHttpImplPrivate::maybeDropUploadDevice(const
//      QNetworkRequest &newHttpRequest)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate21maybeDropUploadDeviceERK15QNetworkRequest(
    QNetworkReplyHttpImplPrivate *self,
    const QNetworkRequest *newHttpRequest) {
  self->maybeDropUploadDevice(*newHttpRequest);
}

//  QNonContiguousByteDevice
//      *QNetworkReplyHttpImplPrivate::createUploadByteDevice()
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZN28QNetworkReplyHttpImplPrivate22createUploadByteDeviceEv(
    QNetworkReplyHttpImplPrivate *self) {
  return self->createUploadByteDevice();
}

//  void QNetworkReplyHttpImplPrivate::createCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate11createCacheEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->createCache();
}

//  void QNetworkReplyHttpImplPrivate::completeCacheSave()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate17completeCacheSaveEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->completeCacheSave();
}

//  void QNetworkReplyHttpImplPrivate::setCachingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate17setCachingEnabledEb(
    QNetworkReplyHttpImplPrivate *self,
    bool enable) {
  self->setCachingEnabled(enable);
}

//  bool QNetworkReplyHttpImplPrivate::isCachingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QNetworkReplyHttpImplPrivate16isCachingEnabledEv(
    const QNetworkReplyHttpImplPrivate *self) {
  return self->isCachingEnabled();
}

//  bool QNetworkReplyHttpImplPrivate::isCachingAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QNetworkReplyHttpImplPrivate16isCachingAllowedEv(
    const QNetworkReplyHttpImplPrivate *self) {
  return self->isCachingAllowed();
}

//  void QNetworkReplyHttpImplPrivate::setResumeOffset(quint64 offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate15setResumeOffsetEy(
    QNetworkReplyHttpImplPrivate *self,
    quint64 offset) {
  self->setResumeOffset(offset);
}

//  void QNetworkReplyHttpImplPrivate::invalidateCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate15invalidateCacheEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->invalidateCache();
}

//  QNetworkAccessManager::Operation QNetworkReplyHttpImplPrivate::getRedirec
//      tOperation(QNetworkAccessManager::Operation currentOp, int
//      httpStatus)
extern "C" Q_DECL_EXPORT
QNetworkAccessManager::Operation ritual_ZN28QNetworkReplyHttpImplPrivate20getRedirectOperationEN21QNetworkAccessManager9OperationEi(
    QNetworkReplyHttpImplPrivate *self,
    QNetworkAccessManager::Operation currentOp,
    int httpStatus) {
  return self->getRedirectOperation(currentOp, httpStatus);
}

//  QNetworkRequest QNetworkReplyHttpImplPrivate::createRedirectRequest(const
//      QNetworkRequest &originalRequests, const QUrl &url, int
//      maxRedirectsRemainig)
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZN28QNetworkReplyHttpImplPrivate21createRedirectRequestERK15QNetworkRequestRK4QUrli(
    QNetworkReplyHttpImplPrivate *self,
    const QNetworkRequest *originalRequests,
    const QUrl *url,
    int maxRedirectsRemainig) {
  return new QNetworkRequest(
      self->createRedirectRequest(
          *originalRequests,
          *url,
          maxRedirectsRemainig));
}

//  bool QNetworkReplyHttpImplPrivate::isHttpRedirectResponse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QNetworkReplyHttpImplPrivate22isHttpRedirectResponseEv(
    const QNetworkReplyHttpImplPrivate *self) {
  return self->isHttpRedirectResponse();
}

//  void QNetworkReplyHttpImplPrivate::replyFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate13replyFinishedEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->replyFinished();
}

//  void QNetworkReplyHttpImplPrivate::httpError(QNetworkReply::NetworkError
//      error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate9httpErrorEN13QNetworkReply12NetworkErrorERK7QString(
    QNetworkReplyHttpImplPrivate *self,
    QNetworkReply::NetworkError error,
    const QString *errorString) {
  self->httpError(error, *errorString);
}

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImplPrivate::replyEncrypted()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate14replyEncryptedEv(
    QNetworkReplyHttpImplPrivate *self) {
  self->replyEncrypted();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImplPrivate::replySslErrors(const QList<QSslError>
//      &a0, bool *a1, QList<QSslError> *a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate14replySslErrorsERK5QListI9QSslErrorEPbPS2_(
    QNetworkReplyHttpImplPrivate *self,
    const QList<QSslError> *a0,
    bool *a1,
    QList<QSslError> *a2) {
  self->replySslErrors(*a0, a1, a2);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImplPrivate::replySslConfigurationChanged(const
//      QSslConfiguration &newSslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate28replySslConfigurationChangedERK17QSslConfiguration(
    QNetworkReplyHttpImplPrivate *self,
    const QSslConfiguration *newSslConfiguration) {
  self->replySslConfigurationChanged(*newSslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImplPrivate::replyPreSharedKeyAuthenticationRequire
//      dSlot(QSslPreSharedKeyAuthenticator *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate43replyPreSharedKeyAuthenticationRequiredSlotEP29QSslPreSharedKeyAuthenticator(
    QNetworkReplyHttpImplPrivate *self,
    QSslPreSharedKeyAuthenticator *a0) {
  self->replyPreSharedKeyAuthenticationRequiredSlot(a0);
}
#endif  // !defined(QT_NO_SSL)

//  void QNetworkReplyHttpImplPrivate::resetUploadDataSlot(bool *r)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate19resetUploadDataSlotEPb(
    QNetworkReplyHttpImplPrivate *self,
    bool *r) {
  self->resetUploadDataSlot(r);
}

//  void QNetworkReplyHttpImplPrivate::sentUploadDataSlot(qint64 a0, qint64
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QNetworkReplyHttpImplPrivate18sentUploadDataSlotExx(
    QNetworkReplyHttpImplPrivate *self,
    qint64 a0,
    qint64 a1) {
  self->sentUploadDataSlot(a0, a1);
}

//  QNetworkReplyHttpImpl *QNetworkReplyHttpImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyHttpImpl *ritual_ZN28QNetworkReplyHttpImplPrivate6q_funcEv(
    QNetworkReplyHttpImplPrivate *self) {
  return self->q_func();
}

//  const QNetworkReplyHttpImpl *QNetworkReplyHttpImplPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyHttpImpl *ritual_ZNK28QNetworkReplyHttpImplPrivate6q_funcEv(
    const QNetworkReplyHttpImplPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQNetworkReplyHttpImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyHttpImplPrivate(
    QNetworkReplyHttpImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyHttpImplPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
