//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyhttpimpl_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyhttpimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtNetwork/private/qhsts_p.h>
#include <QtNetwork/qhttpheaders.h>
#include "QtCore/private/qipaddress_p.h"
#include "QtCore/qlist.h"
#if QT_CONFIG(settings)
#include <QtNetwork/private/qhstsstore_p.h>
#endif
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhsts.cpp, line 18, as local:qhsts.cpp:is_valid_domain_name
static bool is_valid_domain_name(const QString &host)
{
    if (!host.size())
        return false;

    // RFC6797 8.1.1
    // If the substring matching the host production from the Request-URI
    // (of the message to which the host responded) syntactically matches
    //the IP-literal or IPv4address productions from Section 3.2.2 of
    //[RFC3986], then the UA MUST NOT note this host as a Known HSTS Host.
    using namespace QIPAddressUtils;

    IPv4Address ipv4Addr = {};
    if (parseIp4(ipv4Addr, host.constBegin(), host.constEnd()))
        return false;

    IPv6Address ipv6Addr = {};
    // Unlike parseIp4, parseIp6 returns nullptr if it managed to parse IPv6
    // address successfully.
    if (!parseIp6(ipv6Addr, host.constBegin(), host.constEnd()))
        return false;

    // TODO: for now we do not test IPvFuture address, it must be addressed
    // by introducing parseIpFuture (actually, there is an implementation
    // in QUrl that can be adopted/modified/moved to QIPAddressUtils).
    return true;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 144, as local:qnetworkreplyhttpimpl.cpp:remapCustom
static auto remapCustom(QNetworkAccessManager::Operation operation, const QNetworkRequest &req)
{
    if (operation == QNetworkAccessManager::CustomOperation) {
        const QByteArray customVerb = req.attribute(QNetworkRequest::CustomVerbAttribute)
                                              .toByteArray();
        if (customVerb.compare("get", Qt::CaseInsensitive) == 0)
            return QNetworkAccessManager::GetOperation;
        if (customVerb.compare("head", Qt::CaseInsensitive) == 0)
            return QNetworkAccessManager::HeadOperation;
        if (customVerb.compare("delete", Qt::CaseInsensitive) == 0)
            return QNetworkAccessManager::DeleteOperation;
        if (customVerb.compare("put", Qt::CaseInsensitive) == 0)
            return QNetworkAccessManager::PutOperation;
        if (customVerb.compare("post", Qt::CaseInsensitive) == 0)
            return QNetworkAccessManager::PostOperation;
    }
    return operation;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 255, as _ZN21QNetworkReplyHttpImpl5closeEv
inline void QNetworkReplyHttpImpl::close()
{
    Q_D(QNetworkReplyHttpImpl);

    if (d->state == QNetworkReplyPrivate::Aborted ||
        d->state == QNetworkReplyPrivate::Finished)
        return;

    // According to the documentation close only stops the download
    // by closing we can ignore the download part and continue uploading.
    QNetworkReply::close();

    // call finished which will emit signals
    // FIXME shouldn't this be emitted Queued?
    d->error(OperationCanceledError, tr("Operation canceled"));
    d->finished();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 273, as _ZN21QNetworkReplyHttpImpl5abortEv
inline void QNetworkReplyHttpImpl::abort()
{
    abortImpl(QNetworkReply::OperationCanceledError);
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 300, as _ZNK21QNetworkReplyHttpImpl14bytesAvailableEv
inline qint64 QNetworkReplyHttpImpl::bytesAvailable() const
{
    Q_D(const QNetworkReplyHttpImpl);

    // if we load from cache device
    if (d->cacheLoadDevice) {
        return QNetworkReply::bytesAvailable() + d->cacheLoadDevice->bytesAvailable();
    }

    // zerocopy buffer
    if (d->downloadZerocopyBuffer) {
        return QNetworkReply::bytesAvailable() + d->downloadBufferCurrentSize - d->downloadBufferReadPosition;
    }

    if (d->decompressHelper.isValid()) {
        if (d->decompressHelper.isCountingBytes())
            return QNetworkReply::bytesAvailable() + d->decompressHelper.uncompressedSize();
        if (d->decompressHelper.hasData())
            return QNetworkReply::bytesAvailable() + 1;
    }

    // normal buffer
    return QNetworkReply::bytesAvailable();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 325, as _ZNK21QNetworkReplyHttpImpl12isSequentialEv
inline bool QNetworkReplyHttpImpl::isSequential () const
{
    // FIXME In the cache of a cached load or the zero-copy buffer we could actually be non-sequential.
    // FIXME however this requires us to implement stuff like seek() too.
    return true;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 332, as _ZNK21QNetworkReplyHttpImpl4sizeEv
inline qint64 QNetworkReplyHttpImpl::size() const
{
    // FIXME At some point, this could return a proper value, e.g. if we're non-sequential.
    return QNetworkReply::size();
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 338, as _ZN21QNetworkReplyHttpImpl8readDataEPcx
inline qint64 QNetworkReplyHttpImpl::readData(char* data, qint64 maxlen)
{
    Q_D(QNetworkReplyHttpImpl);

    // cacheload device
    if (d->cacheLoadDevice) {
        // FIXME bytesdownloaded, position etc?

        qint64 ret = d->cacheLoadDevice->read(data, maxlen);
        return ret;
    }

    // zerocopy buffer
    if (d->downloadZerocopyBuffer) {
        // FIXME bytesdownloaded, position etc?

        qint64 howMuch = qMin(maxlen, (d->downloadBufferCurrentSize - d->downloadBufferReadPosition));
        memcpy(data, d->downloadZerocopyBuffer + d->downloadBufferReadPosition, howMuch);
        d->downloadBufferReadPosition += howMuch;
        return howMuch;

    }

    if (d->decompressHelper.isValid() && (d->decompressHelper.hasData() || !isFinished())) {
        if (maxlen == 0 || !d->decompressHelper.hasData())
            return 0;
        const qint64 bytesRead = d->decompressHelper.read(data, maxlen);
        if (!d->decompressHelper.isValid()) {
            d->error(QNetworkReplyImpl::NetworkError::UnknownContentError,
                     QCoreApplication::translate("QHttp", "Decompression failed: %1")
                             .arg(d->decompressHelper.errorString()));
            d->decompressHelper.clear();
            return -1;
        }
        if (d->cacheSaveDevice) {
            // Need to write to the cache now that we have the data
            d->cacheSaveDevice->write(data, bytesRead);
            // ... and if we've read everything then the cache can be closed.
            if (isFinished() && !d->decompressHelper.hasData())
                d->completeCacheSave();
        }
        // In case of buffer size restriction we need to emit that it has been emptied
        qint64 wasBuffered = d->bytesBuffered;
        d->bytesBuffered = 0;
        if (readBufferSize())
            emit readBufferFreed(wasBuffered);
        return bytesRead;
    }

    // normal buffer
    if (d->state == d->Finished || d->state == d->Aborted)
        return -1;

    qint64 wasBuffered = d->bytesBuffered;
    d->bytesBuffered = 0;
    if (readBufferSize())
        emit readBufferFreed(wasBuffered);
    return 0;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 398, as _ZN21QNetworkReplyHttpImpl17setReadBufferSizeEx
inline void QNetworkReplyHttpImpl::setReadBufferSize(qint64 size)
{
    QNetworkReply::setReadBufferSize(size);
    emit readBufferSizeChanged(size);
    return;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 405, as _ZNK21QNetworkReplyHttpImpl11canReadLineEv
inline bool QNetworkReplyHttpImpl::canReadLine () const
{
    Q_D(const QNetworkReplyHttpImpl);

    if (QNetworkReply::canReadLine())
        return true;

    if (d->cacheLoadDevice)
        return d->cacheLoadDevice->canReadLine();

    if (d->downloadZerocopyBuffer)
        return memchr(d->downloadZerocopyBuffer + d->downloadBufferReadPosition, '\n', d->downloadBufferCurrentSize - d->downloadBufferReadPosition);

    return false;
}

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 422, as _ZN21QNetworkReplyHttpImpl15ignoreSslErrorsEv
#if !defined(QT_NO_SSL)
inline void QNetworkReplyHttpImpl::ignoreSslErrors()
{
    Q_D(QNetworkReplyHttpImpl);
    Q_ASSERT(d->managerPrivate);

    if (d->managerPrivate->stsEnabled && d->managerPrivate->stsCache.isKnownHost(url())) {
        // We cannot ignore any Security Transport-related errors for this host.
        return;
    }

    d->pendingIgnoreAllSslErrors = true;
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qnetworkreplyhttpimpl.cpp, line 450, as _ZN21QNetworkReplyHttpImpl33setSslConfigurationImplementationERK17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QNetworkReplyHttpImpl::setSslConfigurationImplementation(const QSslConfiguration &newconfig)
{
    // Setting a SSL configuration on a reply is not supported. The user needs to set
    // her/his QSslConfiguration on the QNetworkRequest.
    Q_UNUSED(newconfig);
}
#endif  // !defined(QT_NO_SSL)

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

//  from src/network/access/qhsts.cpp, line 135, as _ZNK10QHstsCache11isKnownHostERK4QUrl
inline bool QHstsCache::isKnownHost(const QUrl &url) const
{
    if (!url.isValid() || !is_valid_domain_name(url.host()))
        return false;

    /*
        RFC6797, 8.2.  Known HSTS Host Domain Name Matching

        * Superdomain Match
          If a label-for-label match between an entire Known HSTS Host's
          domain name and a right-hand portion of the given domain name
          is found, then this Known HSTS Host's domain name is a
          superdomain match for the given domain name.  There could be
          multiple superdomain matches for a given domain name.
        * Congruent Match
          If a label-for-label match between a Known HSTS Host's domain
          name and the given domain name is found -- i.e., there are no
          further labels to compare -- then the given domain name
          congruently matches this Known HSTS Host.

        We start from the congruent match, and then chop labels and dots and
        proceed with superdomain match. While RFC6797 recommends to start from
        superdomain, the result is the same - some valid policy will make a host
        known.
    */

    bool superDomainMatch = false;
    const QString hostNameAsString(url.host());
    HostName nameToTest(QStringView{hostNameAsString});
    while (nameToTest.fragment.size()) {
        auto const pos = knownHosts.find(nameToTest);
        if (pos != knownHosts.end()) {
            if (pos->second.isExpired()) {
                knownHosts.erase(pos);
#if QT_CONFIG(settings)
                if (hstsStore) {
                    // Inform our store that this policy has expired.
                    hstsStore->addToObserved(pos->second);
                }
#endif // QT_CONFIG(settings)
            } else if (!superDomainMatch || pos->second.includesSubDomains()) {
                return true;
            }
        }

        const qsizetype dot = nameToTest.fragment.indexOf(u'.');
        if (dot == -1)
            break;

        nameToTest.fragment = nameToTest.fragment.mid(dot + 1);
        superDomainMatch = true;
    }

    return false;
}

//  from src/network/access/qhstsstore.cpp, line 72, as _ZN10QHstsStore13addToObservedERK11QHstsPolicy
inline void QHstsStore::addToObserved(const QHstsPolicy &policy)
{
    observedPolicies.push_back(policy);
}
//  -----------------------------------------------------------------------

//  Only a class built on QNetworkReplyHttpImpl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNetworkReplyHttpImpl : QNetworkReplyHttpImpl {
  using QNetworkReplyHttpImpl::ignoreSslErrors;
  using QNetworkReplyHttpImpl::setSslConfigurationImplementation;
};

//  A QNetworkReplyHttpImpl that Python can take functions over in. Every QNetworkReplyHttpImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef void (*CuteQNetworkReplyHttpImplCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQNetworkReplyHttpImplCall1)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQNetworkReplyHttpImplCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQNetworkReplyHttpImplCall3)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQNetworkReplyHttpImplCall4)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQNetworkReplyHttpImplCall5)(const void *, char *, qint64, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQNetworkReplyHttpImplCall6)(const void *, qint64, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef bool (*CuteQNetworkReplyHttpImplCall7)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_SSL)
typedef void (*CuteQNetworkReplyHttpImplCall8)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(ssl)
#if QT_CONFIG(http)
#if !defined(QT_NO_SSL)
typedef void (*CuteQNetworkReplyHttpImplCall9)(const void *, const QSslConfiguration *, int *);
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(ssl)
typedef bool (*CuteQNetworkReplyHttpImplCall10)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyHttpImplCall11)(const void *, int *);
typedef bool (*CuteQNetworkReplyHttpImplCall12)(const void *, qint64, int *);
typedef bool (*CuteQNetworkReplyHttpImplCall13)(const void *, int *);
typedef bool (*CuteQNetworkReplyHttpImplCall14)(const void *, int *);
typedef qint64 (*CuteQNetworkReplyHttpImplCall15)(const void *, int *);
typedef bool (*CuteQNetworkReplyHttpImplCall16)(const void *, int, int *);
typedef bool (*CuteQNetworkReplyHttpImplCall17)(const void *, int, int *);
typedef qint64 (*CuteQNetworkReplyHttpImplCall18)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQNetworkReplyHttpImplCall19)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyHttpImplCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkReplyHttpImplCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyHttpImplCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyHttpImplCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyHttpImplCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyHttpImplCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkReplyHttpImplCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkReplyHttpImpl : public QNetworkReplyHttpImpl {
public:
  using QNetworkReplyHttpImpl::QNetworkReplyHttpImpl;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN13QNetworkReply5abortEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN13QNetworkReply17setReadBufferSizeEx")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN13QNetworkReply15ignoreSslErrorsEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(http)
#if QT_CONFIG(ssl)
#if QT_CONFIG(http)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN13QNetworkReply33setSslConfigurationImplementationERK17QSslConfiguration")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
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
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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

#if QT_CONFIG(http)
  //  void QNetworkReplyHttpImpl::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall0 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyHttpImpl::close();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QNetworkReplyHttpImpl::abort()
  void abort() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall1 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyHttpImpl::abort();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QNetworkReplyHttpImpl::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall2 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyHttpImpl::bytesAvailable();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QNetworkReplyHttpImpl::isSequential() const
  bool isSequential() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall3 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyHttpImpl::isSequential();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QNetworkReplyHttpImpl::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall4 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyHttpImpl::size();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QNetworkReplyHttpImpl::readData(char *a0, qint64 a1)
  qint64 readData(char *a0, qint64 a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall5 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall5>(taken[5]);
      qint64 given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QNetworkReplyHttpImpl::readData(a0, a1);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QNetworkReplyHttpImpl::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall6 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall6>(taken[6]);
      call(this, size, &handled);
      if (handled) return;
    }
    QNetworkReplyHttpImpl::setReadBufferSize(size);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  bool QNetworkReplyHttpImpl::canReadLine() const
  bool canReadLine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall7 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkReplyHttpImpl::canReadLine();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
#if !defined(QT_NO_SSL)
  //  void QNetworkReplyHttpImpl::ignoreSslErrors()
  void ignoreSslErrors() override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall8 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkReplyHttpImpl::ignoreSslErrors();
  }
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(http)

#if QT_CONFIG(ssl)
#if QT_CONFIG(http)
#if !defined(QT_NO_SSL)
  //  void QNetworkReplyHttpImpl::setSslConfigurationImplementation(const
  //      QSslConfiguration &configuration)
  void setSslConfigurationImplementation(
      const QSslConfiguration &configuration) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall9 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall9>(taken[9]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
    QNetworkReplyHttpImpl::setSslConfigurationImplementation(configuration);
  }
#endif  // !defined(QT_NO_SSL)
#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(ssl)

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall10 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall10>(taken[10]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall11 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall11>(taken[11]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall12 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall12>(taken[12]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall13 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[14]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall14 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall15 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall15>(taken[15]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall16 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[17]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall17 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall17>(taken[17]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall18 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall19 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall19>(taken[19]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall20 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQNetworkReplyHttpImplCall21 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall21>(taken[21]);
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
      CuteQNetworkReplyHttpImplCall22 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall22>(taken[22]);
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
      CuteQNetworkReplyHttpImplCall23 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall23>(taken[23]);
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
      CuteQNetworkReplyHttpImplCall24 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall24>(taken[24]);
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
      CuteQNetworkReplyHttpImplCall25 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall25>(taken[25]);
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
      CuteQNetworkReplyHttpImplCall26 call = reinterpret_cast<CuteQNetworkReplyHttpImplCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkReplyHttpImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QNetworkReplyHttpImpl10metaObjectEv(
    const QNetworkReplyHttpImpl *self) {
  return self->metaObject();
}

//  void *QNetworkReplyHttpImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QNetworkReplyHttpImpl11qt_metacastEPKc(
    QNetworkReplyHttpImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QNetworkReplyHttpImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QNetworkReplyHttpImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QNetworkReplyHttpImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QNetworkReplyHttpImpl::~QNetworkReplyHttpImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImplD1Ev(QNetworkReplyHttpImpl *self) {
  delete self;
}

//  void QNetworkReplyHttpImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl5closeEv(QNetworkReplyHttpImpl *self) {
  self->close();
}

//  void QNetworkReplyHttpImpl::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl5abortEv(QNetworkReplyHttpImpl *self) {
  self->abort();
}

//  qint64 QNetworkReplyHttpImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkReplyHttpImpl14bytesAvailableEv(
    const QNetworkReplyHttpImpl *self) {
  return self->bytesAvailable();
}

//  bool QNetworkReplyHttpImpl::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkReplyHttpImpl12isSequentialEv(
    const QNetworkReplyHttpImpl *self) {
  return self->isSequential();
}

//  qint64 QNetworkReplyHttpImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QNetworkReplyHttpImpl4sizeEv(
    const QNetworkReplyHttpImpl *self) {
  return self->size();
}

//  qint64 QNetworkReplyHttpImpl::readData(char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN21QNetworkReplyHttpImpl8readDataEPcx(
    QNetworkReplyHttpImpl *self,
    char *a0,
    qint64 a1) {
  return self->readData(a0, a1);
}

//  void QNetworkReplyHttpImpl::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl17setReadBufferSizeEx(
    QNetworkReplyHttpImpl *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  bool QNetworkReplyHttpImpl::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkReplyHttpImpl11canReadLineEv(
    const QNetworkReplyHttpImpl *self) {
  return self->canReadLine();
}

//  QNetworkReplyHttpImplPrivate *QNetworkReplyHttpImpl::d_func()
extern "C" Q_DECL_EXPORT
QNetworkReplyHttpImplPrivate *ritual_ZN21QNetworkReplyHttpImpl6d_funcEv(
    QNetworkReplyHttpImpl *self) {
  return self->d_func();
}

//  const QNetworkReplyHttpImplPrivate *QNetworkReplyHttpImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkReplyHttpImplPrivate *ritual_ZNK21QNetworkReplyHttpImpl6d_funcEv(
    const QNetworkReplyHttpImpl *self) {
  return self->d_func();
}

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImpl::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl15ignoreSslErrorsEv(
    QNetworkReplyHttpImpl *self) {
  self->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImpl::ignoreSslErrorsImplementation(const
//      QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl29ignoreSslErrorsImplementationERK5QListI9QSslErrorE(
    QNetworkReplyHttpImpl *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrorsImplementation(*errors);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImpl::setSslConfigurationImplementation(const
//      QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl33setSslConfigurationImplementationERK17QSslConfiguration(
    QNetworkReplyHttpImpl *self,
    const QSslConfiguration *configuration) {
  self->setSslConfigurationImplementation(*configuration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void
//      QNetworkReplyHttpImpl::sslConfigurationImplementation(QSslConfigurati
//      on &configuration) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QNetworkReplyHttpImpl30sslConfigurationImplementationER17QSslConfiguration(
    const QNetworkReplyHttpImpl *self,
    QSslConfiguration *configuration) {
  self->sslConfigurationImplementation(*configuration);
}
#endif  // !defined(QT_NO_SSL)

//  void QNetworkReplyHttpImpl::startHttpRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl16startHttpRequestEv(
    QNetworkReplyHttpImpl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyHttpImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "startHttpRequest()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "startHttpRequest()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkReplyHttpImpl::abortHttpRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl16abortHttpRequestEv(
    QNetworkReplyHttpImpl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyHttpImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "abortHttpRequest()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "abortHttpRequest()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkReplyHttpImpl::readBufferSizeChanged(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl21readBufferSizeChangedEx(
    QNetworkReplyHttpImpl *self,
    qint64 size) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyHttpImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readBufferSizeChanged(qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readBufferSizeChanged(qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&size)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkReplyHttpImpl::readBufferFreed(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl15readBufferFreedEx(
    QNetworkReplyHttpImpl *self,
    qint64 size) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyHttpImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readBufferFreed(qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readBufferFreed(qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&size)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkReplyHttpImpl::startHttpRequestSynchronously()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl29startHttpRequestSynchronouslyEv(
    QNetworkReplyHttpImpl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyHttpImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "startHttpRequestSynchronously()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "startHttpRequestSynchronously()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QNetworkReplyHttpImpl::haveUploadData(const qint64 pos, const
//      QByteArray &dataArray, bool dataAtEnd, qint64 dataSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkReplyHttpImpl14haveUploadDataExRK10QByteArraybx(
    QNetworkReplyHttpImpl *self,
    qint64 pos,
    const QByteArray *dataArray,
    bool dataAtEnd,
    qint64 dataSize) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QNetworkReplyHttpImpl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "haveUploadData(const qint64,const QByteArray &,bool,qint64)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "haveUploadData(const qint64,const QByteArray &,bool,qint64)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&pos)),
      const_cast<void *>(static_cast<const void *>(dataArray)),
      const_cast<void *>(static_cast<const void *>(&dataAtEnd)),
      const_cast<void *>(static_cast<const void *>(&dataSize)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQNetworkReplyHttpImpl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkReplyHttpImpl(
    QNetworkReplyHttpImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkReplyHttpImpl *>(self)->take(key, call);
}

//  qint64 QNetworkReplyHttpImpl::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK21QNetworkReplyHttpImpl14bytesAvailableEv(
    const QNetworkReplyHttpImpl *self) {
  return self->QNetworkReplyHttpImpl::bytesAvailable();
}

//  bool QNetworkReplyHttpImpl::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QNetworkReplyHttpImpl12isSequentialEv(
    const QNetworkReplyHttpImpl *self) {
  return self->QNetworkReplyHttpImpl::isSequential();
}

//  qint64 QNetworkReplyHttpImpl::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK21QNetworkReplyHttpImpl4sizeEv(
    const QNetworkReplyHttpImpl *self) {
  return self->QNetworkReplyHttpImpl::size();
}

//  bool QNetworkReplyHttpImpl::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QNetworkReplyHttpImpl11canReadLineEv(
    const QNetworkReplyHttpImpl *self) {
  return self->QNetworkReplyHttpImpl::canReadLine();
}

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImpl::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkReplyHttpImpl15ignoreSslErrorsEv(
    QNetworkReplyHttpImpl *self) {
  static_cast<OwnQNetworkReplyHttpImpl *>(self)->OwnQNetworkReplyHttpImpl::ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkReplyHttpImpl::setSslConfigurationImplementation(const
//      QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QNetworkReplyHttpImpl33setSslConfigurationImplementationERK17QSslConfiguration(
    QNetworkReplyHttpImpl *self,
    const QSslConfiguration *configuration) {
  static_cast<OwnQNetworkReplyHttpImpl *>(self)->OwnQNetworkReplyHttpImpl::setSslConfigurationImplementation(
      *configuration);
}
#endif  // !defined(QT_NO_SSL)

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
