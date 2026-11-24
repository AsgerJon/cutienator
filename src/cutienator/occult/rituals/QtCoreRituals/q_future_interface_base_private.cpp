//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(future)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfutureinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfuture.h"
#include "qfutureinterface_p.h"
#include <QtCore/qatomic.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qthread.h>
#include <QtCore/qvarlengtharray.h>
#include <private/qthreadpool_p.h>
#include <private/qobject_p.h>
#include <climits> // For INT_MAX
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/thread/qfutureinterface.cpp, line 714, as _ZN27QFutureInterfaceBasePrivateC1EN20QFutureInterfaceBase5StateE
inline QFutureInterfaceBasePrivate::QFutureInterfaceBasePrivate(QFutureInterfaceBase::State initialState)
    : state(initialState)
{
    progressTime.invalidate();
}

//  from src/corelib/thread/qfutureinterface.cpp, line 720, as _ZN27QFutureInterfaceBasePrivateD1Ev
inline QFutureInterfaceBasePrivate::~QFutureInterfaceBasePrivate()
{
    if (hasException)
        data.m_exceptionStore.~ExceptionStore();
    else
        data.m_results.~ResultStoreBase();
}

//  from src/corelib/thread/qfutureinterface.cpp, line 728, as _ZNK27QFutureInterfaceBasePrivate20internal_resultCountEv
inline int QFutureInterfaceBasePrivate::internal_resultCount() const
{
    return hasException ? 0 : data.m_results.count(); // ### subtract canceled results.
}

//  from src/corelib/thread/qfutureinterface.cpp, line 733, as _ZNK27QFutureInterfaceBasePrivate24internal_isResultReadyAtEi
inline bool QFutureInterfaceBasePrivate::internal_isResultReadyAt(int index) const
{
    return hasException ? false : (data.m_results.contains(index));
}

//  from src/corelib/thread/qfutureinterface.cpp, line 738, as _ZN27QFutureInterfaceBasePrivate26internal_waitForNextResultEv
inline bool QFutureInterfaceBasePrivate::internal_waitForNextResult()
{
    if (hasException)
        return false;

    if (data.m_results.hasNextResult())
        return true;

    while ((state.loadRelaxed() & QFutureInterfaceBase::Running)
           && data.m_results.hasNextResult() == false)
        waitCondition.wait(&m_mutex);

    return !(state.loadRelaxed() & QFutureInterfaceBase::Canceled)
            && data.m_results.hasNextResult();
}

//  from src/corelib/thread/qfutureinterface.cpp, line 831, as _ZN27QFutureInterfaceBasePrivate22connectOutputInterfaceEP23QFutureCallOutInterface
inline void QFutureInterfaceBasePrivate::connectOutputInterface(QFutureCallOutInterface *iface)
{
    QMutexLocker locker(&m_mutex);

    const auto currentState = state.loadRelaxed();
    if (currentState & QFutureInterfaceBase::Started) {
        iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Started));
        if (m_progress) {
            iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::ProgressRange,
                                                        m_progress->minimum,
                                                        m_progress->maximum));
            iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Progress,
                                                        m_progressValue,
                                                        m_progress->text));
        } else {
            iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::ProgressRange,
                                                        0,
                                                        0));
            iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Progress,
                                                        m_progressValue,
                                                        QString()));
        }
    }

    if (!hasException) {
        QtPrivate::ResultIteratorBase it = data.m_results.begin();
        while (it != data.m_results.end()) {
            const int begin = it.resultIndex();
            const int end = begin + it.batchSize();
            iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::ResultsReady,
                                                        begin,
                                                        end));
            it.batchedAdvance();
        }
    }

    if (currentState & QFutureInterfaceBase::Suspended)
        iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Suspended));
    else if (currentState & QFutureInterfaceBase::Suspending)
        iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Suspending));

    if (currentState & QFutureInterfaceBase::Canceled)
        iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Canceled));

    if (currentState & QFutureInterfaceBase::Finished)
        iface->postCallOutEvent(QFutureCallOutEvent(QFutureCallOutEvent::Finished));

    outputConnections.append(iface);
}

//  from src/corelib/thread/qfutureinterface.cpp, line 881, as _ZN27QFutureInterfaceBasePrivate25disconnectOutputInterfaceEP23QFutureCallOutInterface
inline void QFutureInterfaceBasePrivate::disconnectOutputInterface(QFutureCallOutInterface *iface)
{
    QMutexLocker lock(&m_mutex);
    const qsizetype index = outputConnections.indexOf(iface);
    if (index == -1)
        return;
    outputConnections.removeAt(index);

    iface->callOutInterfaceDisconnected();
}

//  from src/corelib/thread/qfutureinterface.cpp, line 892, as _ZN27QFutureInterfaceBasePrivate8setStateEN20QFutureInterfaceBase5StateE
inline void QFutureInterfaceBasePrivate::setState(QFutureInterfaceBase::State newState)
{
    state.storeRelaxed(newState);
}
//  -----------------------------------------------------------------------

//  QFutureInterfaceBasePrivate::QFutureInterfaceBasePrivate(QFutureInterface
//      Base::State initialState)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBasePrivate *ritual_ZN27QFutureInterfaceBasePrivateC1EN20QFutureInterfaceBase5StateE(
    QFutureInterfaceBase::State initialState) {
  return new QFutureInterfaceBasePrivate(initialState);
}

//  QFutureInterfaceBasePrivate::~QFutureInterfaceBasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivateD1Ev(
    QFutureInterfaceBasePrivate *self) {
  delete self;
}

//  QThreadPool *QFutureInterfaceBasePrivate::pool() const
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZNK27QFutureInterfaceBasePrivate4poolEv(
    const QFutureInterfaceBasePrivate *self) {
  return self->pool();
}

//  int QFutureInterfaceBasePrivate::internal_resultCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QFutureInterfaceBasePrivate20internal_resultCountEv(
    const QFutureInterfaceBasePrivate *self) {
  return self->internal_resultCount();
}

//  bool QFutureInterfaceBasePrivate::internal_isResultReadyAt(int index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QFutureInterfaceBasePrivate24internal_isResultReadyAtEi(
    const QFutureInterfaceBasePrivate *self,
    int index) {
  return self->internal_isResultReadyAt(index);
}

//  bool QFutureInterfaceBasePrivate::internal_waitForNextResult()
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QFutureInterfaceBasePrivate26internal_waitForNextResultEv(
    QFutureInterfaceBasePrivate *self) {
  return self->internal_waitForNextResult();
}

//  void QFutureInterfaceBasePrivate::connectOutputInterface(QFutureCallOutIn
//      terface *iface)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivate22connectOutputInterfaceEP23QFutureCallOutInterface(
    QFutureInterfaceBasePrivate *self,
    QFutureCallOutInterface *iface) {
  self->connectOutputInterface(iface);
}

//  void QFutureInterfaceBasePrivate::disconnectOutputInterface(QFutureCallOu
//      tInterface *iface)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivate25disconnectOutputInterfaceEP23QFutureCallOutInterface(
    QFutureInterfaceBasePrivate *self,
    QFutureCallOutInterface *iface) {
  self->disconnectOutputInterface(iface);
}

//  void QFutureInterfaceBasePrivate::setState(QFutureInterfaceBase::State
//      state)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QFutureInterfaceBasePrivate8setStateEN20QFutureInterfaceBase5StateE(
    QFutureInterfaceBasePrivate *self,
    QFutureInterfaceBase::State state) {
  self->setState(state);
}

#endif  // QT_CONFIG(future)
