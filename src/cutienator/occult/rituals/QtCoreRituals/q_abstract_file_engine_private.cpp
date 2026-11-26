//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qabstractfileengine_p.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef QT_BUILD_CORE_LIB
#include <QtCore/private/qresource_p.h>
#endif
#include <QtCore/qdatetime.h>
#include <QtCore/qreadwritelock.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdirlisting.h>
#include <QtCore/qstringbuilder.h>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/private/qfilesystemmetadata_p.h>
#include <QtCore/private/qfilesystemengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qabstractfileengine.cpp, line 36, as _ZN26QAbstractFileEnginePrivateD1Ev
inline QAbstractFileEnginePrivate::~QAbstractFileEnginePrivate()
    = default;
//  -----------------------------------------------------------------------

//  QAbstractFileEnginePrivate::QAbstractFileEnginePrivate(QAbstractFileEngin
//      e *q)
extern "C" Q_DECL_EXPORT
QAbstractFileEnginePrivate *ritual_ZN26QAbstractFileEnginePrivateC1EP19QAbstractFileEngine(
    QAbstractFileEngine *q) {
  return new QAbstractFileEnginePrivate(q);
}

//  QAbstractFileEnginePrivate::~QAbstractFileEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractFileEnginePrivateD1Ev(
    QAbstractFileEnginePrivate *self) {
  delete self;
}

//  QAbstractFileEngine *QAbstractFileEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_ZN26QAbstractFileEnginePrivate6q_funcEv(
    QAbstractFileEnginePrivate *self) {
  return self->q_func();
}

//  const QAbstractFileEngine *QAbstractFileEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractFileEngine *ritual_ZNK26QAbstractFileEnginePrivate6q_funcEv(
    const QAbstractFileEnginePrivate *self) {
  return self->q_func();
}
