//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qioring_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if (QT_CONFIG(liburing)) || (QT_CONFIG(windows_ioring))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qioring_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qioring_linux.cpp, line 46, as local:qioring_linux.cpp:maxReadWriteLen
#if QT_CONFIG(liburing)
static qsizetype maxReadWriteLen()
{
#ifndef QT_DEBUG
    return MaxReadWriteLen;
#else
    return QtPrivate::testMaxReadWriteLen.load(std::memory_order_relaxed);
#endif
}
#endif  // QT_CONFIG(liburing)

//  from src/corelib/io/qioring.cpp, line 11, as _Z9lcQIORingv
inline const QLoggingCategory &lcQIORing()
{
    static const QLoggingCategory category("qt.core.ioring", QtCriticalMsg);
    return category;
}

//  from src/corelib/io/qioring.cpp, line 110, as _ZN7QIORing20handleReadCompletionEmP5QSpanISt4byteLm18446744073709551615EEPvN3qxp12function_refIJFxxEEEE
inline QIORing::ReadWriteStatus QIORing::handleReadCompletion(size_t value, QSpan<std::byte> *destinations,
                                                       void *voidExtra, SetResultFn setResultFn)
{
    if (value == 0) {
        // Since we are reading, presumably this indicates EOF.
        // In case this is our only callback, notify that it at least wasn't a
        // failure:
        setResultFn(qint64(0));
        return ReadWriteStatus::Finished;
    }
    if (auto *extra = static_cast<QtPrivate::ReadWriteExtra *>(voidExtra)) {
        const qsizetype bytesRead = q26::saturating_cast<qsizetype>(value);
        qCDebug(lcQIORing) << "Partial read of" << bytesRead << "bytes completed";
        extra->totalProcessed = setResultFn(bytesRead);
        // [0/1] Add the number of bytes processed to the spanOffset - we use this to test how many
        // spans were fully processed, and/or how far into the last span we have data.
        extra->spanOffset += bytesRead;
        qCDebug(lcQIORing) << "Read operation progress: span" << extra->spanIndex << "offset"
                           << extra->spanOffset << "of" << destinations[extra->spanIndex].size()
                           << "bytes. Total read:" << extra->totalProcessed << "bytes";
        // [1/1] We subtract the size of the spans, in order, here. When a span's size is larger
        // than the "spanOffset" it means we have a partially-used span. Otherwise it stops
        // processing when we run out of spans to check, or we hit spanOffset == 0.
        while (extra->spanOffset >= destinations[extra->spanIndex].size()) {
            extra->spanOffset -= destinations[extra->spanIndex].size();
            // Move to next span
            if (++extra->spanIndex == extra->numSpans)
                return ReadWriteStatus::Finished;
        }
        return ReadWriteStatus::MoreToDo;
    }
    setResultFn(q26::saturating_cast<qsizetype>(value));
    return ReadWriteStatus::Finished;
}

//  from src/corelib/io/qioring.cpp, line 145, as _ZN7QIORing21handleWriteCompletionEmPK5QSpanIKSt4byteLm18446744073709551615EEPvN3qxp12function_refIJFxxEEEE
inline QIORing::ReadWriteStatus QIORing::handleWriteCompletion(size_t value,
                                                        const QSpan<const std::byte> *sources,
                                                        void *voidExtra, SetResultFn setResultFn)
{
    if (auto *extra = static_cast<QtPrivate::ReadWriteExtra *>(voidExtra)) {
        const qsizetype bytesWritten = q26::saturating_cast<qsizetype>(value);
        qCDebug(lcQIORing) << "Partial write of" << bytesWritten << "bytes completed";
        extra->totalProcessed = setResultFn(bytesWritten);
        // [0/1] Add the number of bytes processed to the spanOffset - we use this to test how many
        // spans were fully processed, and/or how far into the last span we have data.
        extra->spanOffset += bytesWritten;
        qCDebug(lcQIORing) << "Write operation progress: span" << extra->spanIndex << "offset"
                           << extra->spanOffset << "of" << sources[extra->spanIndex].size()
                           << "bytes. Total written:" << extra->totalProcessed << "bytes";
        // [1/1] We subtract the size of the spans, in order, here. When a span's size is larger
        // than the "spanOffset" it means we have a partially-used span. Otherwise it stops
        // processing when we run out of spans to check, or we hit spanOffset == 0.
        while (extra->spanOffset >= sources[extra->spanIndex].size()) {
            extra->spanOffset -= sources[extra->spanIndex].size();
            // Move to next span
            if (++extra->spanIndex == extra->numSpans)
                return ReadWriteStatus::Finished;
        }
        return ReadWriteStatus::MoreToDo;
    }
    setResultFn(q26::saturating_cast<qsizetype>(value));
    return ReadWriteStatus::Finished;
}

//  from src/corelib/io/qioring.cpp, line 174, as _ZN7QIORing27finalizeReadWriteCompletionEPNS_18GenericRequestTypeENS_15ReadWriteStatusE
inline void QIORing::finalizeReadWriteCompletion(GenericRequestType *request, ReadWriteStatus rwstatus)
{
    switch (rwstatus) {
    case ReadWriteStatus::Finished:
        if (request->getExtra<void>())
            --ongoingSplitOperations;
        break;
    case ReadWriteStatus::MoreToDo: {
        // Move the request such that it is next in the list to be processed:
        auto &it = addrItMap[request];
        const auto where = lastUnqueuedIterator.value_or(pendingRequests.end());
        pendingRequests.splice(where, pendingRequests, it);
        it = std::prev(where);
        lastUnqueuedIterator = it;
        break;
    }
    }
}
//  -----------------------------------------------------------------------

//  QIORing::QIORing(quint32 submissionQueueSize, quint32
//      completionQueueSize)
extern "C" Q_DECL_EXPORT
QIORing *ritual_ZN7QIORingC1Ejj(
    quint32 submissionQueueSize,
    quint32 completionQueueSize) {
  return new QIORing(submissionQueueSize, completionQueueSize);
}

//  QIORing::~QIORing()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QIORingD1Ev(QIORing *self) {
  delete self;
}

//  QIORing *QIORing::sharedInstance()
extern "C" Q_DECL_EXPORT
QIORing *ritual_ZN7QIORing14sharedInstanceEv() {
  return QIORing::sharedInstance();
}

//  bool QIORing::ensureInitialized()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QIORing17ensureInitializedEv(QIORing *self) {
  return self->ensureInitialized();
}

//  bool QIORing::supportsOperation(Operation op)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QIORing17supportsOperationEN9QtPrivate9OperationE(
    QIORing::Operation op) {
  return QIORing::supportsOperation(op);
}

//  void QIORing::submitRequests()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QIORing14submitRequestsEv(QIORing *self) {
  self->submitRequests();
}

//  bool QIORing::waitForRequest(RequestHandle handle, QDeadlineTimer
//      deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QIORing14waitForRequestEPNS_16RequestHandleTagE14QDeadlineTimer(
    QIORing *self,
    QIORing::RequestHandle handle,
    const QDeadlineTimer *deadline) {
  return self->waitForRequest(handle, *deadline);
}

//  quint32 QIORing::submissionQueueSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK7QIORing19submissionQueueSizeEv(const QIORing *self) {
  return self->submissionQueueSize();
}

//  quint32 QIORing::completionQueueSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK7QIORing19completionQueueSizeEv(const QIORing *self) {
  return self->completionQueueSize();
}

//  bool QIORing::initializeIORing()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QIORing16initializeIORingEv(QIORing *self) {
  return self->initializeIORing();
}

//  QueuedRequestStatus QIORing::queueRequestInternal(GenericRequestType
//      &request)
extern "C" Q_DECL_EXPORT
QIORing::QueuedRequestStatus ritual_ZN7QIORing20queueRequestInternalERNS_18GenericRequestTypeE(
    QIORing *self,
    QIORing::GenericRequestType *request) {
  return self->queueRequestInternal(*request);
}

#if defined(Q_OS_LINUX)
//  bool QIORing::isResultFailure(NativeResultType result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QIORing15isResultFailureEi(QIORing::NativeResultType result) {
  return QIORing::isResultFailure(result);
}
#endif  // defined(Q_OS_LINUX)

//  ReadWriteStatus QIORing::handleReadCompletion(size_t value,
//      QSpan<std::byte> *destinations, void *voidExtra, SetResultFn
//      setResult)
extern "C" Q_DECL_EXPORT
QIORing::ReadWriteStatus ritual_ZN7QIORing20handleReadCompletionEmP5QSpanISt4byteLm18446744073709551615EEPvN3qxp12function_refIJFxxEEEE(
    size_t value,
    QSpan<std::byte> *destinations,
    void *voidExtra,
    const QIORing::SetResultFn *setResult) {
  return QIORing::handleReadCompletion(
      value,
      destinations,
      voidExtra,
      *setResult);
}

//  ReadWriteStatus QIORing::handleWriteCompletion(size_t value, const
//      QSpan<const std::byte> *sources, void *voidExtra, SetResultFn
//      setResult)
extern "C" Q_DECL_EXPORT
QIORing::ReadWriteStatus ritual_ZN7QIORing21handleWriteCompletionEmPK5QSpanIKSt4byteLm18446744073709551615EEPvN3qxp12function_refIJFxxEEEE(
    size_t value,
    const QSpan<const std::byte> *sources,
    void *voidExtra,
    const QIORing::SetResultFn *setResult) {
  return QIORing::handleWriteCompletion(
      value,
      sources,
      voidExtra,
      *setResult);
}

//  void QIORing::finalizeReadWriteCompletion(GenericRequestType *request,
//      ReadWriteStatus rwstatus)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QIORing27finalizeReadWriteCompletionEPNS_18GenericRequestTypeENS_15ReadWriteStatusE(
    QIORing *self,
    QIORing::GenericRequestType *request,
    QIORing::ReadWriteStatus rwstatus) {
  self->finalizeReadWriteCompletion(request, rwstatus);
}

#endif  // (QT_CONFIG(liburing)) || (QT_CONFIG(windows_ioring))
