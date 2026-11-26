//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloaderthread_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypeloadernetworkreplyproxy_p.h>
#include <QtQml/private/qqmltypeloader_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlextensionplugin_p.h>
#include <QtQml/private/qqmltypeloaderthread_p.h>
#if QT_CONFIG(qml_network)
#include <QtQml/private/qqmltypeloadernetworkreplyproxy_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypeloadernetworkreplyproxy.cpp, line 10, as _ZN31QQmlTypeLoaderNetworkReplyProxyC1EP14QQmlTypeLoaderP7QObject
inline QQmlTypeLoaderNetworkReplyProxy::QQmlTypeLoaderNetworkReplyProxy(
        QQmlTypeLoader *l, QObject *parent)
    : QObject(parent), l(l)
{
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 20, as _ZN20QQmlTypeLoaderThreadD1Ev
inline QQmlTypeLoaderThread::~QQmlTypeLoaderThread()
{
    // The thread has to be shutdown() first.
#if QT_CONFIG(qml_type_loader_thread)
    Q_ASSERT(!thread()->isRunning());
#endif

    // Discard all remaining messages.
    // We don't need the lock anymore because the thread is dead.
    discardMessages();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 113, as _ZN20QQmlTypeLoaderThread10loadThreadERK14QQmlRefPointerI12QQmlDataBlobE
inline void QQmlTypeLoaderThread::loadThread(const QQmlDataBlob::Ptr &b)
{
    m_loader->loadThread(b);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 118, as _ZN20QQmlTypeLoaderThread24loadWithStaticDataThreadERK14QQmlRefPointerI12QQmlDataBlobERK10QByteArray
inline void QQmlTypeLoaderThread::loadWithStaticDataThread(const QQmlDataBlob::Ptr &b, const QByteArray &d)
{
    m_loader->loadWithStaticDataThread(b, d);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 123, as _ZN20QQmlTypeLoaderThread24loadWithCachedUnitThreadERK14QQmlRefPointerI12QQmlDataBlobEPKN11QQmlPrivate13CachedQmlUnitE
inline void QQmlTypeLoaderThread::loadWithCachedUnitThread(const QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)
{
    m_loader->loadWithCachedUnitThread(b, unit);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 128, as _ZN20QQmlTypeLoaderThread17callCompletedMainERK14QQmlRefPointerI12QQmlDataBlobE
inline void QQmlTypeLoaderThread::callCompletedMain(const QQmlDataBlob::Ptr &b)
{
#ifdef DATABLOB_DEBUG
    qWarning("QQmlTypeLoaderThread: %s completed() callback", qPrintable(b->urlString()));
#endif
    b->completed();
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 136, as _ZN20QQmlTypeLoaderThread31callDownloadProgressChangedMainERK14QQmlRefPointerI12QQmlDataBlobEd
inline void QQmlTypeLoaderThread::callDownloadProgressChangedMain(const QQmlDataBlob::Ptr &b, qreal p)
{
#ifdef DATABLOB_DEBUG
    qWarning("QQmlTypeLoaderThread: %s downloadProgressChanged(%f) callback",
             qPrintable(b->urlString()), p);
#endif
    b->downloadProgressChanged(p);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 145, as _ZN20QQmlTypeLoaderThread23initializeExtensionMainEP22QQmlExtensionInterfacePKc
inline void QQmlTypeLoaderThread::initializeExtensionMain(QQmlExtensionInterface *iface,
                                                const char *uri)
{
    // We can use m_engine because we're on the engine thread.
    QQmlEngine *engine = m_loader->engine()->qmlEngine();
    Q_ASSERT(engine && engine->thread() == QThread::currentThread());
    iface->initializeEngine(engine, uri);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 154, as _ZN20QQmlTypeLoaderThread29initializeEngineExtensionMainEP28QQmlEngineExtensionInterfacePKc
inline void QQmlTypeLoaderThread::initializeEngineExtensionMain(QQmlEngineExtensionInterface *iface,
                                                const char *uri)
{
    // We can use m_engine because we're on the engine thread.
    QQmlEngine *engine = m_loader->engine()->qmlEngine();
    Q_ASSERT(engine && engine->thread() == QThread::currentThread());
    iface->initializeEngine(engine, uri);
}

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 163, as _ZN20QQmlTypeLoaderThread10dropThreadERK14QQmlRefPointerI12QQmlDataBlobE
inline void QQmlTypeLoaderThread::dropThread(const QQmlDataBlob::Ptr &b)
{
    // Simply drop the reference to b
    Q_UNUSED(b);
}
//  -----------------------------------------------------------------------

//  QQmlTypeLoaderThread::~QQmlTypeLoaderThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThreadD1Ev(QQmlTypeLoaderThread *self) {
  delete self;
}

//  void QQmlTypeLoaderThread::loadThread(const QQmlDataBlob::Ptr &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread10loadThreadERK14QQmlRefPointerI12QQmlDataBlobE(
    QQmlTypeLoaderThread *self,
    const QQmlDataBlob::Ptr *b) {
  self->loadThread(*b);
}

//  void QQmlTypeLoaderThread::loadWithStaticDataThread(const
//      QQmlDataBlob::Ptr &b, const QByteArray &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread24loadWithStaticDataThreadERK14QQmlRefPointerI12QQmlDataBlobERK10QByteArray(
    QQmlTypeLoaderThread *self,
    const QQmlDataBlob::Ptr *b,
    const QByteArray *a1) {
  self->loadWithStaticDataThread(*b, *a1);
}

//  void QQmlTypeLoaderThread::loadWithCachedUnitThread(const
//      QQmlDataBlob::Ptr &b, const QQmlPrivate::CachedQmlUnit *unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread24loadWithCachedUnitThreadERK14QQmlRefPointerI12QQmlDataBlobEPKN11QQmlPrivate13CachedQmlUnitE(
    QQmlTypeLoaderThread *self,
    const QQmlDataBlob::Ptr *b,
    const QQmlPrivate::CachedQmlUnit *unit) {
  self->loadWithCachedUnitThread(*b, unit);
}

//  void QQmlTypeLoaderThread::callCompletedMain(const QQmlDataBlob::Ptr &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread17callCompletedMainERK14QQmlRefPointerI12QQmlDataBlobE(
    QQmlTypeLoaderThread *self,
    const QQmlDataBlob::Ptr *b) {
  self->callCompletedMain(*b);
}

//  void QQmlTypeLoaderThread::callDownloadProgressChangedMain(const
//      QQmlDataBlob::Ptr &b, qreal p)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread31callDownloadProgressChangedMainERK14QQmlRefPointerI12QQmlDataBlobEd(
    QQmlTypeLoaderThread *self,
    const QQmlDataBlob::Ptr *b,
    qreal p) {
  self->callDownloadProgressChangedMain(*b, p);
}

//  void QQmlTypeLoaderThread::initializeExtensionMain(QQmlExtensionInterface
//      *iface, const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread23initializeExtensionMainEP22QQmlExtensionInterfacePKc(
    QQmlTypeLoaderThread *self,
    QQmlExtensionInterface *iface,
    const char *uri) {
  self->initializeExtensionMain(iface, uri);
}

//  void QQmlTypeLoaderThread::initializeEngineExtensionMain(QQmlEngineExtens
//      ionInterface *iface, const char *uri)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread29initializeEngineExtensionMainEP28QQmlEngineExtensionInterfacePKc(
    QQmlTypeLoaderThread *self,
    QQmlEngineExtensionInterface *iface,
    const char *uri) {
  self->initializeEngineExtensionMain(iface, uri);
}

//  void QQmlTypeLoaderThread::dropThread(const QQmlDataBlob::Ptr &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlTypeLoaderThread10dropThreadERK14QQmlRefPointerI12QQmlDataBlobE(
    QQmlTypeLoaderThread *self,
    const QQmlDataBlob::Ptr *b) {
  self->dropThread(*b);
}
