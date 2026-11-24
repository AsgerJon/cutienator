//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyimpl_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include "qnetworkreply.h"
#include "qnetworkreply_p.h"
#include <QtNetwork/qsslconfiguration.h>
#include "qnetworkrequest.h"
#include "qnetworkrequest_p.h"
#include "qplatformdefs.h"
#include "qnetworkcookie.h"
#include "qsslconfiguration.h"
#include "qhttpheadershelper_p.h"
#if QT_CONFIG(http)
#include "qhttp1configuration.h"
#include "qhttp2configuration.h"
#include "private/http2protocol_p.h"
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
#include <q20algorithm.h>
#include "qnetworkreplyimpl_p.h"
#include "qnetworkaccessbackend_p.h"
#include "qnetworkcookie.h"
#include "qnetworkcookiejar.h"
#include "qabstractnetworkcache.h"
#include "QtCore/qcoreapplication.h"
#include "QtCore/qdatetime.h"
#include "QtNetwork/qsslconfiguration.h"
#include "qnetworkaccessmanager_p.h"
#include <QtCore/QCoreApplication>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/network/access/qnetworkreplyimpl.cpp, line 21, as _ZN24QNetworkReplyImplPrivateC1Ev
inline QNetworkReplyImplPrivate::QNetworkReplyImplPrivate()
    : backend(nullptr), outgoingData(nullptr),
      copyDevice(nullptr),
      cacheEnabled(false), cacheSaveDevice(nullptr),
      notificationHandlingPaused(false),
      bytesDownloaded(0), bytesUploaded(-1),
      httpStatusCode(0),
      state(Idle)
      , downloadBufferReadPosition(0)
      , downloadBufferCurrentSize(0)
      , downloadBufferMaximumSize(0)
      , downloadBuffer(nullptr)
{
    if (request.attribute(QNetworkRequest::EmitAllUploadProgressSignalsAttribute).toBool() == true)
        emitAllUploadProgressSignals = true;
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 159, as _ZN24QNetworkReplyImplPrivate21_q_bufferOutgoingDataEv
inline void QNetworkReplyImplPrivate::_q_bufferOutgoingData()
{
    Q_Q(QNetworkReplyImpl);

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

//  from src/network/access/qnetworkreplyimpl.cpp, line 142, as _ZN24QNetworkReplyImplPrivate29_q_bufferOutgoingDataFinishedEv
inline void QNetworkReplyImplPrivate::_q_bufferOutgoingDataFinished()
{
    Q_Q(QNetworkReplyImpl);

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

//  from src/network/access/qnetworkreplyimpl.cpp, line 310, as _ZN24QNetworkReplyImplPrivate25pauseNotificationHandlingEv
inline void QNetworkReplyImplPrivate::pauseNotificationHandling()
{
    notificationHandlingPaused = true;
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 316, as _ZN24QNetworkReplyImplPrivate26resumeNotificationHandlingEv
inline void QNetworkReplyImplPrivate::resumeNotificationHandling()
{
    Q_Q(QNetworkReplyImpl);
    notificationHandlingPaused = false;
    if (pendingNotifications.size() >= 1)
        QCoreApplication::postEvent(q, new QEvent(QEvent::NetworkReplyUpdated));
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 274, as _ZN24QNetworkReplyImplPrivate13backendNotifyENS_21InternalNotificationsE
inline void QNetworkReplyImplPrivate::backendNotify(InternalNotifications notification)
{
    Q_Q(QNetworkReplyImpl);
    const auto it = std::find(pendingNotifications.cbegin(), pendingNotifications.cend(), notification);
    if (it == pendingNotifications.cend())
        pendingNotifications.push_back(notification);

    if (pendingNotifications.size() == 1)
        QCoreApplication::postEvent(q, new QEvent(QEvent::NetworkReplyUpdated));
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 331, as _ZN24QNetworkReplyImplPrivate11createCacheEv
inline void QNetworkReplyImplPrivate::createCache()
{
    // check if we can save and if we're allowed to
    if (!networkCache()
        || !request.attribute(QNetworkRequest::CacheSaveControlAttribute, true).toBool())
        return;
    cacheEnabled = true;
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 372, as _ZN24QNetworkReplyImplPrivate17completeCacheSaveEv
inline void QNetworkReplyImplPrivate::completeCacheSave()
{
    if (cacheEnabled && errorCode != QNetworkReplyImpl::NoError) {
        networkCache()->remove(url);
    } else if (cacheEnabled && cacheSaveDevice) {
        networkCache()->insert(cacheSaveDevice);
    }
    cacheSaveDevice = nullptr;
    cacheEnabled = false;
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 345, as _ZN24QNetworkReplyImplPrivate17setCachingEnabledEb
inline void QNetworkReplyImplPrivate::setCachingEnabled(bool enable)
{
    if (!enable && !cacheEnabled)
        return;                 // nothing to do
    if (enable && cacheEnabled)
        return;                 // nothing to do either!

    if (enable) {
        if (Q_UNLIKELY(bytesDownloaded)) {
            // refuse to enable in this case
            qCritical("QNetworkReplyImpl: backend error: caching was enabled after some bytes had been written");
            return;
        }

        createCache();
    } else {
        // someone told us to turn on, then back off?
        // ok... but you should make up your mind
        qDebug("QNetworkReplyImpl: setCachingEnabled(true) called after setCachingEnabled(false) -- "
               "backend %s probably needs to be fixed",
               backend->metaObject()->className());
        networkCache()->remove(url);
        cacheSaveDevice = nullptr;
        cacheEnabled = false;
    }
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 340, as _ZNK24QNetworkReplyImplPrivate16isCachingEnabledEv
inline bool QNetworkReplyImplPrivate::isCachingEnabled() const
{
    return (cacheEnabled && networkCache() != nullptr);
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 404, as _ZNK24QNetworkReplyImplPrivate23nextDownstreamBlockSizeEv
inline qint64 QNetworkReplyImplPrivate::nextDownstreamBlockSize() const
{
    enum { DesiredBufferSize = 32 * 1024 };
    if (readBufferMaxSize == 0)
        return DesiredBufferSize;

    return qMax<qint64>(0, readBufferMaxSize - buffer.size());
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 413, as _ZN24QNetworkReplyImplPrivate19initCacheSaveDeviceEv
inline void QNetworkReplyImplPrivate::initCacheSaveDevice()
{
    Q_Q(QNetworkReplyImpl);

    // The disk cache does not support partial content, so don't even try to
    // save any such content into the cache.
    if (q->attribute(QNetworkRequest::HttpStatusCodeAttribute).toInt() == 206) {
        cacheEnabled = false;
        return;
    }

    // save the meta data
    QNetworkCacheMetaData metaData;
    metaData.setUrl(url);
    // @todo @future: fetchCacheMetaData is not currently implemented in any backend, but can be useful again in the future
    // metaData = backend->fetchCacheMetaData(metaData);

    // save the redirect request also in the cache
    QVariant redirectionTarget = q->attribute(QNetworkRequest::RedirectionTargetAttribute);
    if (redirectionTarget.isValid()) {
        QNetworkCacheMetaData::AttributesMap attributes = metaData.attributes();
        attributes.insert(QNetworkRequest::RedirectionTargetAttribute, redirectionTarget);
        metaData.setAttributes(attributes);
    }

    cacheSaveDevice = networkCache()->prepare(metaData);

    if (!cacheSaveDevice || !cacheSaveDevice->isOpen()) {
        if (Q_UNLIKELY(cacheSaveDevice && !cacheSaveDevice->isOpen()))
            qCritical("QNetworkReplyImpl: network cache returned a device that is not open -- "
                  "class %s probably needs to be fixed",
                  networkCache()->metaObject()->className());

        networkCache()->remove(url);
        cacheSaveDevice = nullptr;
        cacheEnabled = false;
    }
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 590, as _ZN24QNetworkReplyImplPrivate8finishedEv
inline void QNetworkReplyImplPrivate::finished()
{
    Q_Q(QNetworkReplyImpl);

    if (state == Finished || state == Aborted)
        return;

    pauseNotificationHandling();
    const auto totalSizeOpt = QNetworkHeadersPrivate::toInt(
            headers().value(QHttpHeaders::WellKnownHeader::ContentLength));
    const auto totalSize = totalSizeOpt.value_or(-1);

    resumeNotificationHandling();

    state = Finished;
    q->setFinished(true);

    pendingNotifications.clear();

    pauseNotificationHandling();
    if (totalSize == -1) {
        emit q->downloadProgress(bytesDownloaded, bytesDownloaded);
    } else {
        emit q->downloadProgress(bytesDownloaded, totalSize);
    }

    if (bytesUploaded == -1 && (outgoingData || outgoingDataBuffer))
        emit q->uploadProgress(0, 0);
    resumeNotificationHandling();

    // if we don't know the total size of or we received everything save the cache
    if (totalSize == -1 || bytesDownloaded == totalSize)
        completeCacheSave();

    // note: might not be a good idea, since users could decide to delete us
    // which would delete the backend too...
    // maybe we should protect the backend
    pauseNotificationHandling();
    emit q->readChannelFinished();
    emit q->finished();
    resumeNotificationHandling();
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 633, as _ZN24QNetworkReplyImplPrivate5errorEN13QNetworkReply12NetworkErrorERK7QString
inline void QNetworkReplyImplPrivate::error(QNetworkReplyImpl::NetworkError code, const QString &errorMessage)
{
    Q_Q(QNetworkReplyImpl);
    // Can't set and emit multiple errors.
    if (errorCode != QNetworkReply::NoError) {
        qWarning( "QNetworkReplyImplPrivate::error: Internal problem, this method must only be called once.");
        return;
    }

    errorCode = code;
    q->setErrorString(errorMessage);

    // note: might not be a good idea, since users could decide to delete us
    // which would delete the backend too...
    // maybe we should protect the backend
    emit q->errorOccurred(code);
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 651, as _ZN24QNetworkReplyImplPrivate15metaDataChangedEv
inline void QNetworkReplyImplPrivate::metaDataChanged()
{
    Q_Q(QNetworkReplyImpl);
    // 1. do we have cookies?
    // 2. are we allowed to set them?
    if (!manager.isNull()) {
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
    }

    emit q->metaDataChanged();
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 673, as _ZN24QNetworkReplyImplPrivate20redirectionRequestedERK4QUrl
inline void QNetworkReplyImplPrivate::redirectionRequested(const QUrl &target)
{
    attributes.insert(QNetworkRequest::RedirectionTargetAttribute, target);
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 678, as _ZN24QNetworkReplyImplPrivate9encryptedEv
inline void QNetworkReplyImplPrivate::encrypted()
{
#ifndef QT_NO_SSL
    Q_Q(QNetworkReplyImpl);
    emit q->encrypted();
#endif
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 686, as _ZN24QNetworkReplyImplPrivate9sslErrorsERK5QListI9QSslErrorE
inline void QNetworkReplyImplPrivate::sslErrors(const QList<QSslError> &errors)
{
#ifndef QT_NO_SSL
    Q_Q(QNetworkReplyImpl);
    emit q->sslErrors(errors);
#else
    Q_UNUSED(errors);
#endif
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 696, as _ZN24QNetworkReplyImplPrivate15readFromBackendEv
inline void QNetworkReplyImplPrivate::readFromBackend()
{
    Q_Q(QNetworkReplyImpl);
    if (!backend)
        return;

    if (backend->ioFeatures() & QNetworkAccessBackend::IOFeature::ZeroCopy) {
        if (backend->bytesAvailable())
            emit q->readyRead();
    } else {
        bool anyBytesRead = false;
        while (backend->bytesAvailable()
               && (!readBufferMaxSize || buffer.size() < readBufferMaxSize)) {
            qint64 toRead = qMin(nextDownstreamBlockSize(), backend->bytesAvailable());
            if (toRead == 0)
                toRead = 16 * 1024; // try to read something
            char *data = buffer.reserve(toRead);
            qint64 bytesRead = backend->read(data, toRead);
            Q_ASSERT(bytesRead <= toRead);
            buffer.chop(toRead - bytesRead);
            anyBytesRead |= bytesRead > 0;
        }
        if (anyBytesRead)
            emit q->readyRead();
    }
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 324, as _ZNK24QNetworkReplyImplPrivate12networkCacheEv
inline QAbstractNetworkCache *QNetworkReplyImplPrivate::networkCache() const
{
    if (!backend)
        return nullptr;
    return backend->networkCache();
}
//  -----------------------------------------------------------------------

//  A QNetworkReplyImplPrivate that Python can take functions over in. Every QNetworkReplyImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNetworkReplyImplPrivateCall0)(const void *, char, int *);
typedef const QByteArray * (*CuteQNetworkReplyImplPrivateCall1)(const void *, qint64, int *);
class CuteQNetworkReplyImplPrivate : public QNetworkReplyImplPrivate {
public:
  using QNetworkReplyImplPrivate::QNetworkReplyImplPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyImplPrivateCall0 call = reinterpret_cast<CuteQNetworkReplyImplPrivateCall0>(taken[0]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyImplPrivateCall1 call = reinterpret_cast<CuteQNetworkReplyImplPrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QNetworkReplyImplPrivate::QNetworkReplyImplPrivate()
extern "C" Q_DECL_EXPORT
QNetworkReplyImplPrivate *ritual_ZN24QNetworkReplyImplPrivateC1Ev() {
  return new CuteQNetworkReplyImplPrivate();
}

//  void QNetworkReplyImplPrivate::_q_bufferOutgoingData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate21_q_bufferOutgoingDataEv(
    QNetworkReplyImplPrivate *self) {
  self->_q_bufferOutgoingData();
}

//  void QNetworkReplyImplPrivate::_q_bufferOutgoingDataFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate29_q_bufferOutgoingDataFinishedEv(
    QNetworkReplyImplPrivate *self) {
  self->_q_bufferOutgoingDataFinished();
}

//  void QNetworkReplyImplPrivate::pauseNotificationHandling()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate25pauseNotificationHandlingEv(
    QNetworkReplyImplPrivate *self) {
  self->pauseNotificationHandling();
}

//  void QNetworkReplyImplPrivate::resumeNotificationHandling()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate26resumeNotificationHandlingEv(
    QNetworkReplyImplPrivate *self) {
  self->resumeNotificationHandling();
}

//  void QNetworkReplyImplPrivate::backendNotify(InternalNotifications
//      notification)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate13backendNotifyENS_21InternalNotificationsE(
    QNetworkReplyImplPrivate *self,
    QNetworkReplyImplPrivate::InternalNotifications notification) {
  self->backendNotify(notification);
}

//  void QNetworkReplyImplPrivate::createCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate11createCacheEv(
    QNetworkReplyImplPrivate *self) {
  self->createCache();
}

//  void QNetworkReplyImplPrivate::completeCacheSave()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate17completeCacheSaveEv(
    QNetworkReplyImplPrivate *self) {
  self->completeCacheSave();
}

//  void QNetworkReplyImplPrivate::setCachingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate17setCachingEnabledEb(
    QNetworkReplyImplPrivate *self,
    bool enable) {
  self->setCachingEnabled(enable);
}

//  bool QNetworkReplyImplPrivate::isCachingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QNetworkReplyImplPrivate16isCachingEnabledEv(
    const QNetworkReplyImplPrivate *self) {
  return self->isCachingEnabled();
}

//  qint64 QNetworkReplyImplPrivate::nextDownstreamBlockSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK24QNetworkReplyImplPrivate23nextDownstreamBlockSizeEv(
    const QNetworkReplyImplPrivate *self) {
  return self->nextDownstreamBlockSize();
}

//  void QNetworkReplyImplPrivate::initCacheSaveDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate19initCacheSaveDeviceEv(
    QNetworkReplyImplPrivate *self) {
  self->initCacheSaveDevice();
}

//  void QNetworkReplyImplPrivate::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate8finishedEv(
    QNetworkReplyImplPrivate *self) {
  self->finished();
}

//  void QNetworkReplyImplPrivate::error(QNetworkReply::NetworkError code,
//      const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate5errorEN13QNetworkReply12NetworkErrorERK7QString(
    QNetworkReplyImplPrivate *self,
    QNetworkReply::NetworkError code,
    const QString *errorString) {
  self->error(code, *errorString);
}

//  void QNetworkReplyImplPrivate::metaDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate15metaDataChangedEv(
    QNetworkReplyImplPrivate *self) {
  self->metaDataChanged();
}

//  void QNetworkReplyImplPrivate::redirectionRequested(const QUrl &target)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate20redirectionRequestedERK4QUrl(
    QNetworkReplyImplPrivate *self,
    const QUrl *target) {
  self->redirectionRequested(*target);
}

//  void QNetworkReplyImplPrivate::encrypted()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate9encryptedEv(
    QNetworkReplyImplPrivate *self) {
  self->encrypted();
}

//  void QNetworkReplyImplPrivate::sslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate9sslErrorsERK5QListI9QSslErrorE(
    QNetworkReplyImplPrivate *self,
    const QList<QSslError> *errors) {
  self->sslErrors(*errors);
}

//  void QNetworkReplyImplPrivate::readFromBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkReplyImplPrivate15readFromBackendEv(
    QNetworkReplyImplPrivate *self) {
  self->readFromBackend();
}

//  QAbstractNetworkCache *QNetworkReplyImplPrivate::networkCache() const
extern "C" Q_DECL_EXPORT
QAbstractNetworkCache *ritual_ZNK24QNetworkReplyImplPrivate12networkCacheEv(
    const QNetworkReplyImplPrivate *self) {
  return self->networkCache();
}

//  QNetworkReplyImpl *QNetworkReplyImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyImpl *ritual_ZN24QNetworkReplyImplPrivate6q_funcEv(
    QNetworkReplyImplPrivate *self) {
  return self->q_func();
}

//  const QNetworkReplyImpl *QNetworkReplyImplPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyImpl *ritual_ZNK24QNetworkReplyImplPrivate6q_funcEv(
    const QNetworkReplyImplPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQNetworkReplyImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyImplPrivate(
    QNetworkReplyImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyImplPrivate *>(self)->take(key, call);
}
