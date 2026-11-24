//  Written by dev_tooling.RitualGenerator from the records of QtNetworkAuth/
//  6.12.0/QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauth2deviceauthorizationflow.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/qabstractoauth2.h>
#include <QtNetworkAuth/private/qabstractoauth2_p.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmessageauthenticationcode.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/qhttpmultipart.h>
#ifndef QT_NO_SSL
#include <QtNetwork/qsslconfiguration.h>
#endif
#include <QtNetworkAuth/qabstractoauth.h>
#include <QtNetworkAuth/qabstractoauthreplyhandler.h>
#include <QtNetworkAuth/private/qabstractoauth_p.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qmessageauthenticationcode.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtCore/qrandom.h>
#include <QtCore/private/qlocking_p.h>
#include <QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h>
#include <QtNetworkAuth/qoauth2deviceauthorizationflow.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmap.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qvariant.h>
#include <QtNetwork/qrestaccessmanager.h>
#include <QtNetwork/qrestreply.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 691, as _ZN22QAbstractOAuth2Private21_q_tokenRequestFailedEN14QAbstractOAuth5ErrorERK7QString
inline void QAbstractOAuth2Private::_q_tokenRequestFailed(QAbstractOAuth::Error error,
                                                const QString& errorString)
{
    Q_Q(QAbstractOAuth);
    qCWarning(loggingCategory) << "Token request failed:" << errorString;
    // If we were refreshing, reset status to Granted if we have an access token.
    // The access token might still be valid, and even if it wouldn't be,
    // refreshing can be attempted again.
    if (q->status() == QAbstractOAuth::Status::RefreshingToken) {
        if (!q->token().isEmpty())
            setStatus(QAbstractOAuth::Status::Granted);
        else
            setStatus(QAbstractOAuth::Status::NotAuthenticated);
    }
    emit q->requestFailed(error);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 278, as _ZN21QAbstractOAuthPrivate20networkAccessManagerEv
inline QNetworkAccessManager *QAbstractOAuthPrivate::networkAccessManager()
{
    Q_Q(QAbstractOAuth);
    if (!networkAccessManagerPointer)
        networkAccessManagerPointer = new QNetworkAccessManager(q);
    return networkAccessManagerPointer.data();
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 286, as _ZN21QAbstractOAuthPrivate9setStatusEN14QAbstractOAuth6StatusE
inline void QAbstractOAuthPrivate::setStatus(QAbstractOAuth::Status newStatus)
{
    Q_Q(QAbstractOAuth);
    if (status != newStatus) {
        status = newStatus;
        Q_EMIT q->statusChanged(status);
        if (status == QAbstractOAuth::Status::Granted)
            Q_EMIT q->granted();
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 166, as _ZN37QOAuth2DeviceAuthorizationFlowPrivateD1Ev
inline QOAuth2DeviceAuthorizationFlowPrivate::~QOAuth2DeviceAuthorizationFlowPrivate()
{
    resetCurrentAuthorizationReply();
    resetCurrentTokenReply();
    tokenPollingTimer.stop();
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 333, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate22tokenAcquisitionFailedEN14QAbstractOAuth5ErrorERK7QString
inline void QOAuth2DeviceAuthorizationFlowPrivate::tokenAcquisitionFailed(QAbstractOAuth::Error error,
                                                                   const QString &errorString)
{
    _q_tokenRequestFailed(error, errorString);
    stopTokenPolling();
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 340, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate11setUserCodeERK7QString
inline void QOAuth2DeviceAuthorizationFlowPrivate::setUserCode(const QString &code)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (userCode == code)
        return;
    userCode = code;
    emit q->userCodeChanged(userCode);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 349, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate18setVerificationUrlERK4QUrl
inline void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrl(const QUrl &url)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (verificationUrl == url)
        return;
    verificationUrl = url;
    emit q->verificationUrlChanged(verificationUrl);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 358, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate26setVerificationUrlCompleteERK4QUrl
inline void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrlComplete(const QUrl &url)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (completeVerificationUrl == url)
        return;
    completeVerificationUrl = url;
    emit q->completeVerificationUrlChanged(completeVerificationUrl);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 367, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate21setUserCodeExpirationERK9QDateTime
inline void QOAuth2DeviceAuthorizationFlowPrivate::setUserCodeExpiration(const QDateTime &expiration)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    Q_ASSERT(!expiration.isValid() || expiration.timeSpec() == Qt::TimeSpec::UTC);
    if (userCodeExpirationUtc == expiration)
        return;
    userCodeExpirationUtc = expiration;
    emit q->userCodeExpirationAtChanged(userCodeExpirationUtc.toLocalTime());
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 408, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate16stopTokenPollingEv
inline void QOAuth2DeviceAuthorizationFlowPrivate::stopTokenPolling()
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (!q->isPolling())
        return;

    qCDebug(loggingCategory, "Token stage: Stopping token polling");
    resetCurrentTokenReply();
    tokenPollingTimer.stop();
    emit q->pollingChanged(false);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 496, as _ZNK37QOAuth2DeviceAuthorizationFlowPrivate25isNextPollAfterExpirationEv
inline bool QOAuth2DeviceAuthorizationFlowPrivate::isNextPollAfterExpiration() const
{
    if (!userCodeExpirationUtc.isValid())
        return true;

    const QDateTime nextPoll = QDateTime::currentDateTimeUtc().addDuration(
        std::chrono::duration_cast<std::chrono::milliseconds>(tokenPollingTimer.interval()));

    return nextPoll > userCodeExpirationUtc;
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 507, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate22resetCurrentTokenReplyEv
inline void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentTokenReply()
{
    if (currentTokenReply) {
        const auto reply = currentTokenReply.get();
        // Clear current reply before abort to avoid handling the finished signal
        currentTokenReply.clear();
        reply->abort();
        reply->deleteLater();
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 518, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate30resetCurrentAuthorizationReplyEv
inline void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentAuthorizationReply()
{
    if (currentAuthorizationReply) {
        const auto reply = currentAuthorizationReply.get();
        // Clear current reply before abort to avoid handling the finished signal
        currentAuthorizationReply.clear();
        reply->abort();
        reply->deleteLater();
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 529, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate7networkEv
inline QRestAccessManager *QOAuth2DeviceAuthorizationFlowPrivate::network()
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (!restAccessManager) {
        // First usage, create
        restAccessManager = new QRestAccessManager(networkAccessManager(), q);
    } else if (restAccessManager->networkAccessManager() != networkAccessManager()) {
        // QNetworkAccessManager has changed, re-create
        resetCurrentAuthorizationReply();
        resetCurrentTokenReply();
        delete restAccessManager;
        restAccessManager = new QRestAccessManager(networkAccessManager(), q);
    }
    return restAccessManager;
}
//  -----------------------------------------------------------------------

//  QOAuth2DeviceAuthorizationFlow
//      *QOAuth2DeviceAuthorizationFlowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlow *ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate6q_funcEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->q_func();
}

//  const QOAuth2DeviceAuthorizationFlow
//      *QOAuth2DeviceAuthorizationFlowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOAuth2DeviceAuthorizationFlow *ritual_ZNK37QOAuth2DeviceAuthorizationFlowPrivate6q_funcEv(
    const QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->q_func();
}

//  QOAuth2DeviceAuthorizationFlowPrivate::~QOAuth2DeviceAuthorizationFlowPri
//      vate()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivateD1Ev(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  delete self;
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::tokenAcquisitionFailed(QAbstr
//      actOAuth::Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate22tokenAcquisitionFailedEN14QAbstractOAuth5ErrorERK7QString(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    QAbstractOAuth::Error error,
    const QString *errorString) {
  self->tokenAcquisitionFailed(error, *errorString);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::setUserCode(const QString
//      &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate11setUserCodeERK7QString(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QString *code) {
  self->setUserCode(*code);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrl(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate18setVerificationUrlERK4QUrl(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QUrl *url) {
  self->setVerificationUrl(*url);
}

//  void
//      QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrlComplete(con
//      st QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate26setVerificationUrlCompleteERK4QUrl(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QUrl *url) {
  self->setVerificationUrlComplete(*url);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::setUserCodeExpiration(const
//      QDateTime &expiration)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate21setUserCodeExpirationERK9QDateTime(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QDateTime *expiration) {
  self->setUserCodeExpiration(*expiration);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::stopTokenPolling()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate16stopTokenPollingEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  self->stopTokenPolling();
}

//  bool QOAuth2DeviceAuthorizationFlowPrivate::isNextPollAfterExpiration()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK37QOAuth2DeviceAuthorizationFlowPrivate25isNextPollAfterExpirationEv(
    const QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->isNextPollAfterExpiration();
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentTokenReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate22resetCurrentTokenReplyEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  self->resetCurrentTokenReply();
}

//  void
//      QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentAuthorizationReply
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate30resetCurrentAuthorizationReplyEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  self->resetCurrentAuthorizationReply();
}

//  QRestAccessManager *QOAuth2DeviceAuthorizationFlowPrivate::network()
extern "C" Q_DECL_EXPORT
QRestAccessManager *ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate7networkEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->network();
}
