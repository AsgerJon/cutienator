//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qiooperation_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(async_io)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qiooperation_p.h>
#include <QtCore/6.12.0/QtCore/private/qiooperation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qiooperation_p.h>
#include <QtCore/private/qiooperation_p_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qrandomaccessasyncfile_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qiooperation.cpp, line 13, as _ZN19QIOOperationPrivateC1EPN9QtPrivate23QIOOperationDataStorageE
inline QIOOperationPrivate::QIOOperationPrivate(QtPrivate::QIOOperationDataStorage *storage)
    : dataStorage(storage)
{
    Q_ASSERT(storage);
}

//  from src/corelib/io/qiooperation.cpp, line 19, as _ZN19QIOOperationPrivateD1Ev
inline QIOOperationPrivate::~QIOOperationPrivate()
{
}

//  from src/corelib/io/qiooperation.cpp, line 23, as _ZN19QIOOperationPrivate20appendBytesProcessedEx
inline void QIOOperationPrivate::appendBytesProcessed(qint64 num)
{
    processed += num;
}

//  from src/corelib/io/qiooperation.cpp, line 28, as _ZN19QIOOperationPrivate17operationCompleteEN12QIOOperation5ErrorE
inline void QIOOperationPrivate::operationComplete(QIOOperation::Error err)
{
    Q_Q(QIOOperation);

    error = err;
    state = State::Finished;
    if (err != QIOOperation::Error::None)
        Q_EMIT q->errorOccurred(err);
    Q_EMIT q->finished();
}

//  from src/corelib/io/qiooperation.cpp, line 39, as _ZN19QIOOperationPrivate8setErrorEN12QIOOperation5ErrorE
inline void QIOOperationPrivate::setError(QIOOperation::Error err)
{
    Q_Q(QIOOperation);
    error = err;
    if (err != QIOOperation::Error::None) {
        state = State::Finished;
        Q_EMIT q->errorOccurred(err);
        Q_EMIT q->finished();
    }
}
//  -----------------------------------------------------------------------

//  QIOOperation *QIOOperationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN19QIOOperationPrivate6q_funcEv(
    QIOOperationPrivate *self) {
  return self->q_func();
}

//  const QIOOperation *QIOOperationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QIOOperation *ritual_ZNK19QIOOperationPrivate6q_funcEv(
    const QIOOperationPrivate *self) {
  return self->q_func();
}

//  QIOOperationPrivate::QIOOperationPrivate(QtPrivate::QIOOperationDataStora
//      ge *storage)
extern "C" Q_DECL_EXPORT
QIOOperationPrivate *ritual_ZN19QIOOperationPrivateC1EPN9QtPrivate23QIOOperationDataStorageE(
    QtPrivate::QIOOperationDataStorage *storage) {
  return new QIOOperationPrivate(storage);
}

//  QIOOperationPrivate::~QIOOperationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIOOperationPrivateD1Ev(QIOOperationPrivate *self) {
  delete self;
}

//  QIOOperationPrivate *QIOOperationPrivate::get(QIOOperation *op)
extern "C" Q_DECL_EXPORT
QIOOperationPrivate *ritual_ZN19QIOOperationPrivate3getEP12QIOOperation(
    QIOOperation *op) {
  return QIOOperationPrivate::get(op);
}

//  void QIOOperationPrivate::appendBytesProcessed(qint64 num)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIOOperationPrivate20appendBytesProcessedEx(
    QIOOperationPrivate *self,
    qint64 num) {
  self->appendBytesProcessed(num);
}

//  void QIOOperationPrivate::operationComplete(QIOOperation::Error err)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIOOperationPrivate17operationCompleteEN12QIOOperation5ErrorE(
    QIOOperationPrivate *self,
    QIOOperation::Error err) {
  self->operationComplete(err);
}

//  void QIOOperationPrivate::setError(QIOOperation::Error err)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIOOperationPrivate8setErrorEN12QIOOperation5ErrorE(
    QIOOperationPrivate *self,
    QIOOperation::Error err) {
  self->setError(err);
}

#endif  // QT_CONFIG(async_io)
