//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(processenvironment)
#if QT_CONFIG(process)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qprocess_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qdebug.h>
#include <qdir.h>
#include <qscopedvaluerollback.h>
#include "qprocess.h"
#include "qprocess_p.h"
#include <qbytearray.h>
#include <qdeadlinetimer.h>
#include <qcoreapplication.h>
#if __has_include(<paths.h>)
#include <paths.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qprocess.cpp, line 392, as _ZN15QProcessPrivate7Channel5clearEv
#if QT_CONFIG(process)
inline void QProcessPrivate::Channel::clear()
{
    switch (type) {
    case PipeSource:
        Q_ASSERT(process);
        process->stdinChannel.type = Normal;
        process->stdinChannel.process = nullptr;
        break;
    case PipeSink:
        Q_ASSERT(process);
        process->stdoutChannel.type = Normal;
        process->stdoutChannel.process = nullptr;
        break;
    default:
        break;
    }

    type = Normal;
    file.clear();
    process = nullptr;
}
#endif  // QT_CONFIG(process)
//  -----------------------------------------------------------------------

#if QT_CONFIG(process)
//  void QProcessPrivate::Channel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate7Channel5clearEv(
    QProcessPrivate::Channel *self) {
  self->clear();
}
#endif  // QT_CONFIG(process)

#if QT_CONFIG(process)
//  void QProcessPrivate::Channel::pipeTo(QProcessPrivate *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate7Channel6pipeToEPS_(
    QProcessPrivate::Channel *self,
    QProcessPrivate *other) {
  self->pipeTo(other);
}
#endif  // QT_CONFIG(process)

#if QT_CONFIG(process)
//  void QProcessPrivate::Channel::pipeFrom(QProcessPrivate *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate7Channel8pipeFromEPS_(
    QProcessPrivate::Channel *self,
    QProcessPrivate *other) {
  self->pipeFrom(other);
}
#endif  // QT_CONFIG(process)

//  QProcessPrivate::Channel::~Channel()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QProcessPrivate7ChannelD1Ev(QProcessPrivate::Channel *self) {
  delete self;
}

#endif  // QT_CONFIG(process)
#endif  // QT_CONFIG(processenvironment)
