//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderthread.cpp, line 15, as _ZN20QQmlTypeLoaderThreadC1EP14QQmlTypeLoader
inline QQmlTypeLoaderThread::QQmlTypeLoaderThread(QQmlTypeLoader *loader)
    : m_loader(loader)
{
}
//  -----------------------------------------------------------------------

//  QQmlTypeLoaderThread *QQmlTypeLoaderLockedData::thread() const
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderThread *ritual_ZNK24QQmlTypeLoaderLockedData6threadEv(
    const QQmlTypeLoaderLockedData *self) {
  return self->thread();
}

//  QV4::ExecutionEngine *QQmlTypeLoaderLockedData::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK24QQmlTypeLoaderLockedData6engineEv(
    const QQmlTypeLoaderLockedData *self) {
  return self->engine();
}

//  bool QQmlTypeLoaderLockedData::isCurrentJsEngineThread() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQmlTypeLoaderLockedData23isCurrentJsEngineThreadEv(
    const QQmlTypeLoaderLockedData *self) {
  return self->isCurrentJsEngineThread();
}
