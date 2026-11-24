//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_network)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloadernetworkreplyproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qqmltypeloadernetworkreplyproxy_p.h>
#include <private/qqmltypeloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 16, as _ZN31QQmlTypeLoaderNetworkReplyProxy8finishedEv
inline void QQmlTypeLoaderNetworkReplyProxy::finished()
{
    Q_ASSERT(sender());
    Q_ASSERT(qobject_cast<QNetworkReply *>(sender()));
    QNetworkReply *reply = static_cast<QNetworkReply *>(sender());
    l->networkReplyFinished(reply);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 24, as _ZN31QQmlTypeLoaderNetworkReplyProxy16downloadProgressExx
inline void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64 bytesReceived, qint64 bytesTotal)
{
    Q_ASSERT(sender());
    Q_ASSERT(qobject_cast<QNetworkReply *>(sender()));
    QNetworkReply *reply = static_cast<QNetworkReply *>(sender());
    l->networkReplyProgress(reply, bytesReceived, bytesTotal);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 33, as _ZN31QQmlTypeLoaderNetworkReplyProxy14manualFinishedEP13QNetworkReply
inline void QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply *reply)
{
    qint64 replySize = reply->size();
    l->networkReplyProgress(reply, replySize, replySize);
    l->networkReplyFinished(reply);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQmlTypeLoaderNetworkReplyProxy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQmlTypeLoaderNetworkReplyProxy10metaObjectEv(
    const QQmlTypeLoaderNetworkReplyProxy *self) {
  return self->metaObject();
}

//  void QQmlTypeLoaderNetworkReplyProxy::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy8finishedEv(
    QQmlTypeLoaderNetworkReplyProxy *self) {
  self->finished();
}

//  void QQmlTypeLoaderNetworkReplyProxy::downloadProgress(qint64 a0, qint64
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy16downloadProgressExx(
    QQmlTypeLoaderNetworkReplyProxy *self,
    qint64 a0,
    qint64 a1) {
  self->downloadProgress(a0, a1);
}

//  void QQmlTypeLoaderNetworkReplyProxy::manualFinished(QNetworkReply *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQmlTypeLoaderNetworkReplyProxy14manualFinishedEP13QNetworkReply(
    QQmlTypeLoaderNetworkReplyProxy *self,
    QNetworkReply *a0) {
  self->manualFinished(a0);
}

#endif  // QT_CONFIG(qml_network)
