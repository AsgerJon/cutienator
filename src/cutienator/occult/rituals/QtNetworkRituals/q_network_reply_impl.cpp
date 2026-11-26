//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyimpl_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals whose code, copied from
//  Qt's source, reads constant data Qt keeps to itself
//  ('QNetworkReplyPrivate::progressSignalInterval'), copied with it 'inline'
//  from Qt's source, drafted by a copy of the generator that takes it along.
//  Kept as it is when the generator runs again.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qnetworkreplyimpl_p.h>
#include <QtNetwork/private/qnetworkaccessbackend_p.h>
#include <QtNetwork/qnetworkcookie.h>
#include <QtNetwork/qnetworkcookiejar.h>
#include <QtNetwork/qabstractnetworkcache.h>
#include "QtCore/qcoreapplication.h"
#include "QtCore/qdatetime.h"
#include "QtNetwork/qsslconfiguration.h"
#include <QtNetwork/private/qnetworkaccessmanager_p.h>
#include <QtCore/QCoreApplication>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qnetworkreplyimpl.cpp, line 830, as _ZN17QNetworkReplyImpl15ignoreSslErrorsEv
#if !defined(QT_NO_SSL)
inline void QNetworkReplyImpl::ignoreSslErrors()
{
    Q_D(QNetworkReplyImpl);
    if (d->backend)
        d->backend->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyimpl.cpp, line 806, as _ZN17QNetworkReplyImpl17setReadBufferSizeEx
inline void QNetworkReplyImpl::setReadBufferSize(qint64 size)
{
    Q_D(QNetworkReplyImpl);
    qint64 oldMaxSize = d->readBufferMaxSize;
    QNetworkReply::setReadBufferSize(size);
    if (size > oldMaxSize && size > d->buffer.size())
        d->readFromBackend();
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 837, as _ZN17QNetworkReplyImpl29ignoreSslErrorsImplementationERK5QListI9QSslErrorE
#if !defined(QT_NO_SSL)
inline void QNetworkReplyImpl::ignoreSslErrorsImplementation(const QList<QSslError> &errors)
{
    Q_D(QNetworkReplyImpl);
    if (d->backend)
        d->backend->ignoreSslErrors(errors);
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyimpl.cpp, line 823, as _ZN17QNetworkReplyImpl33setSslConfigurationImplementationERK17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QNetworkReplyImpl::setSslConfigurationImplementation(const QSslConfiguration &config)
{
    Q_D(QNetworkReplyImpl);
    if (d->backend && !config.isNull())
        d->backend->setSslConfiguration(config);
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyimpl.cpp, line 739, as _ZN17QNetworkReplyImpl5abortEv
inline void QNetworkReplyImpl::abort()
{
    Q_D(QNetworkReplyImpl);
    if (d->state == QNetworkReplyPrivate::Finished || d->state == QNetworkReplyPrivate::Aborted)
        return;

    // stop both upload and download
    if (d->outgoingData)
        disconnect(d->outgoingData, nullptr, this, nullptr);
    if (d->copyDevice)
        disconnect(d->copyDevice, nullptr, this, nullptr);

    QNetworkReply::close();

    // call finished which will emit signals
    d->error(OperationCanceledError, tr("Operation canceled"));
    d->finished();
    d->state = QNetworkReplyPrivate::Aborted;

    // finished may access the backend
    if (d->backend) {
        d->backend->deleteLater();
        d->backend = nullptr;
    }
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 765, as _ZN17QNetworkReplyImpl5closeEv
inline void QNetworkReplyImpl::close()
{
    Q_D(QNetworkReplyImpl);
    if (d->state == QNetworkReplyPrivate::Aborted ||
        d->state == QNetworkReplyPrivate::Finished)
        return;

    // stop the download
    if (d->backend)
        d->backend->close();
    if (d->copyDevice)
        disconnect(d->copyDevice, nullptr, this, nullptr);

    QNetworkReply::close();

    // call finished which will emit signals
    d->error(OperationCanceledError, tr("Operation canceled"));
    d->finished();
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 905, as _ZN17QNetworkReplyImpl5eventEP6QEvent
inline bool QNetworkReplyImpl::event(QEvent *e)
{
    if (e->type() == QEvent::NetworkReplyUpdated) {
        d_func()->handleNotifications();
        return true;
    }

    return QObject::event(e);
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 848, as _ZN17QNetworkReplyImpl8readDataEPcx
inline qint64 QNetworkReplyImpl::readData(char *data, qint64 maxlen)
{
    Q_D(QNetworkReplyImpl);

    if (d->backend
        && d->backend->ioFeatures().testFlag(QNetworkAccessBackend::IOFeature::ZeroCopy)) {
        qint64 bytesRead = 0;
        while (d->backend->bytesAvailable()) {
            QByteArrayView view = d->backend->readPointer();
            if (view.size()) {
                qint64 bytesToCopy = qMin(qint64(view.size()), maxlen - bytesRead);
                memcpy(data + bytesRead, view.data(), bytesToCopy); // from zero to one copy

                // We might have to cache this
                if (d->cacheEnabled && !d->cacheSaveDevice)
                    d->initCacheSaveDevice();
                if (d->cacheEnabled && d->cacheSaveDevice)
                    d->cacheSaveDevice->write(view.data(), view.size());

                bytesRead += bytesToCopy;
                d->backend->advanceReadPointer(bytesToCopy);
            } else {
                break;
            }
        }

        const auto totalSizeOpt = QNetworkHeadersPrivate::toInt(
                headers().value(QHttpHeaders::WellKnownHeader::ContentLength));
        emit downloadProgress(bytesRead, totalSizeOpt.value_or(-1));
        return bytesRead;
    } else if (d->backend && d->backend->bytesAvailable()) {
        return d->backend->read(data, maxlen);
    }

    // Special case code if we have the "zero copy" download buffer
    if (d->downloadBuffer) {
        qint64 maxAvail = qMin<qint64>(d->downloadBufferCurrentSize - d->downloadBufferReadPosition, maxlen);
        if (maxAvail == 0)
            return d->state == QNetworkReplyPrivate::Finished ? -1 : 0;
        // FIXME what about "Aborted" state?
        memcpy(data, d->downloadBuffer + d->downloadBufferReadPosition, maxAvail);
        d->downloadBufferReadPosition += maxAvail;
        return maxAvail;
    }


    // FIXME what about "Aborted" state?
    if (d->state == QNetworkReplyPrivate::Finished)
        return -1;

    d->backendNotify(QNetworkReplyImplPrivate::NotifyDownstreamReadyWrite);
    return 0;
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 83, as _ZN24QNetworkReplyImplPrivate16_q_copyReadyReadEv
inline void QNetworkReplyImplPrivate::_q_copyReadyRead()
{
    Q_Q(QNetworkReplyImpl);
    if (state != Working)
        return;
    if (!copyDevice || !q->isOpen())
        return;

    // FIXME Optimize to use download buffer if it is a QBuffer.
    // Needs to be done where sendCacheContents() (?) of HTTP is emitting
    // metaDataChanged ?
    qint64 lastBytesDownloaded = bytesDownloaded;
    forever {
        qint64 bytesToRead = nextDownstreamBlockSize();
        if (bytesToRead == 0)
            // we'll be called again, eventually
            break;

        bytesToRead = qBound<qint64>(1, bytesToRead, copyDevice->bytesAvailable());
        qint64 bytesActuallyRead = copyDevice->read(buffer.reserve(bytesToRead), bytesToRead);
        if (bytesActuallyRead == -1) {
            buffer.chop(bytesToRead);
            break;
        }
        buffer.chop(bytesToRead - bytesActuallyRead);

        if (!copyDevice->isSequential() && copyDevice->atEnd()) {
            bytesDownloaded += bytesActuallyRead;
            break;
        }

        bytesDownloaded += bytesActuallyRead;
    }

    if (bytesDownloaded == lastBytesDownloaded) {
        // we didn't read anything
        return;
    }

    const auto totalSizeOpt = QNetworkHeadersPrivate::toInt(
            headers().value(QHttpHeaders::WellKnownHeader::ContentLength));

    pauseNotificationHandling();
    // emit readyRead before downloadProgress in case this will cause events to be
    // processed and we get into a recursive call (as in QProgressDialog).
    emit q->readyRead();
    if (downloadProgressSignalChoke.isValid() &&
        downloadProgressSignalChoke.elapsed() >= progressSignalInterval) {
        downloadProgressSignalChoke.start();
        emit q->downloadProgress(bytesDownloaded, totalSizeOpt.value_or(-1));
    }
    resumeNotificationHandling();
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 38, as _ZN24QNetworkReplyImplPrivate17_q_startOperationEv
inline void QNetworkReplyImplPrivate::_q_startOperation()
{
    // ensure this function is only being called once
    if (state == Working || state == Finished) {
        qDebug() << "QNetworkReplyImpl::_q_startOperation was called more than once" << url;
        return;
    }
    state = Working;

    // note: if that method is called directly, it cannot happen that the backend is 0,
    // because we just checked via a qobject_cast that we got a http backend (see
    // QNetworkReplyImplPrivate::setup())
    if (!backend) {
        error(QNetworkReplyImpl::ProtocolUnknownError,
              QCoreApplication::translate("QNetworkReply", "Protocol \"%1\" is unknown").arg(url.scheme())); // not really true!;
        finished();
        return;
    }

    if (!backend->start()) {
        qWarning("Backend start failed");
        state = Working;
        error(QNetworkReplyImpl::UnknownNetworkError,
              QCoreApplication::translate("QNetworkReply", "backend start error."));
        finished();
        return;
    }

    // Prepare timer for progress notifications
    downloadProgressSignalChoke.start();
    uploadProgressSignalChoke.invalidate();

    if (backend && backend->isSynchronous()) {
        state = Finished;
        q_func()->setFinished(true);
    } else {
        if (state != Finished) {
            if (operation == QNetworkAccessManager::GetOperation)
                pendingNotifications.push_back(NotifyDownstreamReadyWrite);

            handleNotifications();
        }
    }
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

//  from src/network/access/qnetworkreplyimpl.cpp, line 137, as _ZN24QNetworkReplyImplPrivate26_q_copyReadChannelFinishedEv
inline void QNetworkReplyImplPrivate::_q_copyReadChannelFinished()
{
    _q_copyReadyRead();
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

//  from src/network/access/qnetworkreplyimpl.cpp, line 795, as _ZNK17QNetworkReplyImpl14bytesAvailableEv
inline qint64 QNetworkReplyImpl::bytesAvailable() const
{
    // Special case for the "zero copy" download buffer
    Q_D(const QNetworkReplyImpl);
    if (d->downloadBuffer) {
        qint64 maxAvail = d->downloadBufferCurrentSize - d->downloadBufferReadPosition;
        return QNetworkReply::bytesAvailable() + maxAvail;
    }
    return QNetworkReply::bytesAvailable() + (d->backend ? d->backend->bytesAvailable() : 0);
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 816, as _ZNK17QNetworkReplyImpl30sslConfigurationImplementationER17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QNetworkReplyImpl::sslConfigurationImplementation(QSslConfiguration &configuration) const
{
    Q_D(const QNetworkReplyImpl);
    if (d->backend)
        configuration = d->backend->sslConfiguration();
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyimpl.cpp, line 324, as _ZNK24QNetworkReplyImplPrivate12networkCacheEv
inline QAbstractNetworkCache *QNetworkReplyImplPrivate::networkCache() const
{
    if (!backend)
        return nullptr;
    return backend->networkCache();
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 340, as _ZNK24QNetworkReplyImplPrivate16isCachingEnabledEv
inline bool QNetworkReplyImplPrivate::isCachingEnabled() const
{
    return (cacheEnabled && networkCache() != nullptr);
}

//  from src/network/access/qnetworkreply.cpp, line 15, as _ZN20QNetworkReplyPrivate22progressSignalIntervalE
inline const int QNetworkReplyPrivate::progressSignalInterval = 100;

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

//  from src/network/access/qnetworkreplyimpl.cpp, line 285, as _ZN24QNetworkReplyImplPrivate19handleNotificationsEv
inline void QNetworkReplyImplPrivate::handleNotifications()
{
    if (notificationHandlingPaused)
        return;

     for (InternalNotifications notification : std::exchange(pendingNotifications, {})) {
        if (state != Working)
            return;
        switch (notification) {
        case NotifyDownstreamReadyWrite:
            if (copyDevice) {
                _q_copyReadyRead();
            } else if (backend) {
                if (backend->bytesAvailable() > 0)
                    readFromBackend();
                else if (backend->wantToRead())
                    readFromBackend();
            }
            break;
        }
    }
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

//  from src/network/access/qnetworkrequest.cpp, line 1669, as _ZNK22QNetworkHeadersPrivate7headersEv
inline QHttpHeaders QNetworkHeadersPrivate::headers() const
{
    return httpHeaders;
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 404, as _ZNK24QNetworkReplyImplPrivate23nextDownstreamBlockSizeEv
inline qint64 QNetworkReplyImplPrivate::nextDownstreamBlockSize() const
{
    enum { DesiredBufferSize = 32 * 1024 };
    if (readBufferMaxSize == 0)
        return DesiredBufferSize;

    return qMax<qint64>(0, readBufferMaxSize - buffer.size());
}

//  from src/network/access/qnetworkreplyimpl.cpp, line 728, as _ZN17QNetworkReplyImplD1Ev
inline QNetworkReplyImpl::~QNetworkReplyImpl()
{
    Q_D(QNetworkReplyImpl);

    // This code removes the data from the cache if it was prematurely aborted.
    // See QNetworkReplyImplPrivate::completeCacheSave(), we disable caching there after the cache
    // save had been properly finished. So if it is still enabled it means we got deleted/aborted.
    if (d->isCachingEnabled())
        d->networkCache()->remove(url());
}
//  -----------------------------------------------------------------------

//  Only a class built on QNetworkReplyImpl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNetworkReplyImpl : QNetworkReplyImpl {
  using QNetworkReplyImpl::setSslConfigurationImplementation;
  using QNetworkReplyImpl::ignoreSslErrors;
};

//  A QNetworkReplyImpl that Python can take functions over in. Every QNetworkReplyImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNetworkReplyImplCall0)(const void *, int *);
typedef void (*CuteQNetworkReplyImplCall1)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyImplCall2)(const void *, int *);
typedef void (*CuteQNetworkReplyImplCall3)(const void *, qint64, int *);
typedef qint64 (*CuteQNetworkReplyImplCall4)(const void *, char *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyImplCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(ssl)
#if !defined(QT_NO_SSL)
typedef void (*CuteQNetworkReplyImplCall6)(const void *, const QSslConfiguration *, int *);
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(ssl)
#if !defined(QT_NO_SSL)
typedef void (*CuteQNetworkReplyImplCall7)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
typedef bool (*CuteQNetworkReplyImplCall8)(const void *, int *);
typedef bool (*CuteQNetworkReplyImplCall9)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyImplCall10)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyImplCall11)(const void *, int *);
typedef bool (*CuteQNetworkReplyImplCall12)(const void *, qint64, int *);
typedef bool (*CuteQNetworkReplyImplCall13)(const void *, int *);
typedef bool (*CuteQNetworkReplyImplCall14)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyImplCall15)(const void *, int *);
typedef bool (*CuteQNetworkReplyImplCall16)(const void *, int *);
typedef bool (*CuteQNetworkReplyImplCall17)(const void *, int, int *);
typedef bool (*CuteQNetworkReplyImplCall18)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyImplCall19)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQNetworkReplyImplCall20)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyImplCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyImplCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyImplCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyImplCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyImplCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyImplCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkReplyImpl : public QNetworkReplyImpl {
public:
  using QNetworkReplyImpl::QNetworkReplyImpl;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QNetworkReply5abortEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QNetworkReply17setReadBufferSizeEx")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(ssl)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(ssl)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN13QNetworkReply15ignoreSslErrorsEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[20] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QNetworkReplyImpl::abort()
  void abort() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyImplCall0 call = reinterpret_cast<CuteQNetworkReplyImplCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyImpl::abort();
  }

  //  void QNetworkReplyImpl::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyImplCall1 call = reinterpret_cast<CuteQNetworkReplyImplCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyImpl::close();
  }

  //  qint64 QNetworkReplyImpl::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyImplCall2 call = reinterpret_cast<CuteQNetworkReplyImplCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyImpl::bytesAvailable();
  }

  //  void QNetworkReplyImpl::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkReplyImplCall3 call = reinterpret_cast<CuteQNetworkReplyImplCall3>(taken[3]);
      call(this, size, &handled);
      if (handled) return;
    }
    QNetworkReplyImpl::setReadBufferSize(size);
  }

  //  qint64 QNetworkReplyImpl::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkReplyImplCall4 call = reinterpret_cast<CuteQNetworkReplyImplCall4>(taken[4]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QNetworkReplyImpl::readData(data, maxlen);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QNetworkReplyImpl::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkReplyImplCall5 call = reinterpret_cast<CuteQNetworkReplyImplCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QNetworkReplyImpl::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(ssl)
#if !defined(QT_NO_SSL)
  //  void QNetworkReplyImpl::setSslConfigurationImplementation(const
  //      QSslConfiguration &configuration)
  void setSslConfigurationImplementation(
      const QSslConfiguration &configuration) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkReplyImplCall6 call = reinterpret_cast<CuteQNetworkReplyImplCall6>(taken[6]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
    QNetworkReplyImpl::setSslConfigurationImplementation(configuration);
  }
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(ssl)

#if !defined(QT_NO_SSL)
  //  void QNetworkReplyImpl::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkReplyImplCall7 call = reinterpret_cast<CuteQNetworkReplyImplCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyImpl::ignoreSslErrors();
  }
#endif  // !defined(QT_NO_SSL)

  //  bool QNetworkReply::isSequential() const
  bool isSequential() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkReplyImplCall8 call = reinterpret_cast<CuteQNetworkReplyImplCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReply::isSequential();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkReplyImplCall9 call = reinterpret_cast<CuteQNetworkReplyImplCall9>(taken[9]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkReplyImplCall10 call = reinterpret_cast<CuteQNetworkReplyImplCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkReplyImplCall11 call = reinterpret_cast<CuteQNetworkReplyImplCall11>(taken[11]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkReplyImplCall12 call = reinterpret_cast<CuteQNetworkReplyImplCall12>(taken[12]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkReplyImplCall13 call = reinterpret_cast<CuteQNetworkReplyImplCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkReplyImplCall14 call = reinterpret_cast<CuteQNetworkReplyImplCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkReplyImplCall15 call = reinterpret_cast<CuteQNetworkReplyImplCall15>(taken[15]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkReplyImplCall16 call = reinterpret_cast<CuteQNetworkReplyImplCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkReplyImplCall17 call = reinterpret_cast<CuteQNetworkReplyImplCall17>(taken[17]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNetworkReplyImplCall18 call = reinterpret_cast<CuteQNetworkReplyImplCall18>(taken[18]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNetworkReplyImplCall19 call = reinterpret_cast<CuteQNetworkReplyImplCall19>(taken[19]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[20]) {
      int handled = 0;
      CuteQNetworkReplyImplCall20 call = reinterpret_cast<CuteQNetworkReplyImplCall20>(taken[20]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQNetworkReplyImplCall21 call = reinterpret_cast<CuteQNetworkReplyImplCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQNetworkReplyImplCall22 call = reinterpret_cast<CuteQNetworkReplyImplCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQNetworkReplyImplCall23 call = reinterpret_cast<CuteQNetworkReplyImplCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQNetworkReplyImplCall24 call = reinterpret_cast<CuteQNetworkReplyImplCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQNetworkReplyImplCall25 call = reinterpret_cast<CuteQNetworkReplyImplCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQNetworkReplyImplCall26 call = reinterpret_cast<CuteQNetworkReplyImplCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkReplyImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QNetworkReplyImpl10metaObjectEv(
    const QNetworkReplyImpl *self) {
  return self->metaObject();
}

//  void *QNetworkReplyImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QNetworkReplyImpl11qt_metacastEPKc(
    QNetworkReplyImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkReplyImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QNetworkReplyImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkReplyImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNetworkReplyImpl::~QNetworkReplyImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImplD1Ev(QNetworkReplyImpl *self) {
  delete self;
}

//  void QNetworkReplyImpl::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImpl5abortEv(QNetworkReplyImpl *self) {
  self->abort();
}

//  void QNetworkReplyImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImpl5closeEv(QNetworkReplyImpl *self) {
  self->close();
}

//  qint64 QNetworkReplyImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QNetworkReplyImpl14bytesAvailableEv(
    const QNetworkReplyImpl *self) {
  return self->bytesAvailable();
}

//  void QNetworkReplyImpl::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImpl17setReadBufferSizeEx(
    QNetworkReplyImpl *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  qint64 QNetworkReplyImpl::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QNetworkReplyImpl8readDataEPcx(
    QNetworkReplyImpl *self,
    char *data,
    qint64 maxlen) {
  return self->readData(data, maxlen);
}

//  bool QNetworkReplyImpl::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNetworkReplyImpl5eventEP6QEvent(
    QNetworkReplyImpl *self,
    QEvent *a0) {
  return self->event(a0);
}

//  QNetworkReplyImplPrivate *QNetworkReplyImpl::d_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyImplPrivate *ritual_ZN17QNetworkReplyImpl6d_funcEv(
    QNetworkReplyImpl *self) {
  return self->d_func();
}

//  const QNetworkReplyImplPrivate *QNetworkReplyImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyImplPrivate *ritual_ZNK17QNetworkReplyImpl6d_funcEv(
    const QNetworkReplyImpl *self) {
  return self->d_func();
}

#if !defined(QT_NO_SSL)
//  void QNetworkReplyImpl::sslConfigurationImplementation(QSslConfiguration
//      &configuration) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QNetworkReplyImpl30sslConfigurationImplementationER17QSslConfiguration(
    const QNetworkReplyImpl *self,
    QSslConfiguration *configuration) {
  self->sslConfigurationImplementation(*configuration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyImpl::setSslConfigurationImplementation(const
//      QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImpl33setSslConfigurationImplementationERK17QSslConfiguration(
    QNetworkReplyImpl *self,
    const QSslConfiguration *configuration) {
  self->setSslConfigurationImplementation(*configuration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyImpl::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImpl15ignoreSslErrorsEv(
    QNetworkReplyImpl *self) {
  self->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyImpl::ignoreSslErrorsImplementation(const
//      QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkReplyImpl29ignoreSslErrorsImplementationERK5QListI9QSslErrorE(
    QNetworkReplyImpl *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrorsImplementation(*errors);
}
#endif  // !defined(QT_NO_SSL)

//  a Python function taken by a CuteQNetworkReplyImpl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyImpl(
    QNetworkReplyImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyImpl *>(self)->take(key, call);
}

//  qint64 QNetworkReplyImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK17QNetworkReplyImpl14bytesAvailableEv(
    const QNetworkReplyImpl *self) {
  return self->QNetworkReplyImpl::bytesAvailable();
}

//  void QNetworkReplyImpl::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNetworkReplyImpl17setReadBufferSizeEx(
    QNetworkReplyImpl *self,
    qint64 size) {
  self->QNetworkReplyImpl::setReadBufferSize(size);
}

//  qint64 QNetworkReplyImpl::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN17QNetworkReplyImpl8readDataEPcx(
    QNetworkReplyImpl *self,
    char *data,
    qint64 maxlen) {
  return self->QNetworkReplyImpl::readData(data, maxlen);
}

//  bool QNetworkReplyImpl::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QNetworkReplyImpl5eventEP6QEvent(
    QNetworkReplyImpl *self,
    QEvent *a0) {
  return self->QNetworkReplyImpl::event(a0);
}

#if !defined(QT_NO_SSL)
//  void QNetworkReplyImpl::setSslConfigurationImplementation(const
//      QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNetworkReplyImpl33setSslConfigurationImplementationERK17QSslConfiguration(
    QNetworkReplyImpl *self,
    const QSslConfiguration *configuration) {
  static_cast<OwnQNetworkReplyImpl *>(self)->OwnQNetworkReplyImpl::setSslConfigurationImplementation(
      *configuration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyImpl::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNetworkReplyImpl15ignoreSslErrorsEv(
    QNetworkReplyImpl *self) {
  static_cast<OwnQNetworkReplyImpl *>(self)->OwnQNetworkReplyImpl::ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)
