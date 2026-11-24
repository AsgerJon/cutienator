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

#if defined(Q_OS_LINUX)
//  bool QIORing::isResultFailure(NativeResultType result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QIORing15isResultFailureEi(QIORing::NativeResultType result) {
  return QIORing::isResultFailure(result);
}
#endif  // defined(Q_OS_LINUX)

#endif  // (QT_CONFIG(liburing)) || (QT_CONFIG(windows_ioring))
