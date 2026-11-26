//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventloop_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qeventloop.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventloop_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qeventloop.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qeventloop_p.h>
#include <QtCore/private/qthread_p.h>
#if __has_include(<cxxabi.h>)
#  include <cxxabi.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qeventloop.cpp, line 22, as _ZN17QEventLoopPrivateD1Ev
inline QEventLoopPrivate::~QEventLoopPrivate()
    = default;
//  -----------------------------------------------------------------------

//  QEventLoop *QEventLoopPrivate::q_func()
extern "C" Q_DECL_EXPORT
QEventLoop *ritual_ZN17QEventLoopPrivate6q_funcEv(QEventLoopPrivate *self) {
  return self->q_func();
}

//  const QEventLoop *QEventLoopPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QEventLoop *ritual_ZNK17QEventLoopPrivate6q_funcEv(
    const QEventLoopPrivate *self) {
  return self->q_func();
}

//  QEventLoopPrivate::QEventLoopPrivate()
extern "C" Q_DECL_EXPORT
QEventLoopPrivate *ritual_ZN17QEventLoopPrivateC1Ev() {
  return new QEventLoopPrivate();
}

//  QEventLoopPrivate::~QEventLoopPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QEventLoopPrivateD1Ev(QEventLoopPrivate *self) {
  delete self;
}

//  void QEventLoopPrivate::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QEventLoopPrivate3refEv(QEventLoopPrivate *self) {
  self->ref();
}

//  void QEventLoopPrivate::deref()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QEventLoopPrivate5derefEv(QEventLoopPrivate *self) {
  self->deref();
}
