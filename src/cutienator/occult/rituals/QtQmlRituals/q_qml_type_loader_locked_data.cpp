//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypeloaderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypeloaderdata_p.h>
#include <QtQml/private/qqmldirdata_p.h>
#include <QtQml/private/qqmlprofiler_p.h>
#include <QtQml/private/qqmlscriptblob_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypeloaderdata.cpp, line 14, as _ZN24QQmlTypeLoaderLockedDataC1EPN3QV415ExecutionEngineE
inline QQmlTypeLoaderLockedData::QQmlTypeLoaderLockedData(QV4::ExecutionEngine *engine)
    : m_engine(engine)
{}
//  -----------------------------------------------------------------------

//  QQmlTypeLoaderLockedData::QQmlTypeLoaderLockedData(QV4::ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QQmlTypeLoaderLockedData *ritual_ZN24QQmlTypeLoaderLockedDataC1EPN3QV415ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QQmlTypeLoaderLockedData(engine);
}

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
