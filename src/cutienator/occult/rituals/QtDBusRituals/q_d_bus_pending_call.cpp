//  Edited by hand on 2026-11-25: the ritual of the constructor
//  'QDBusPendingCall::QDBusPendingCall()' is taken out, with its row.
//  The header declares it 'not defined', and Qt's library offers
//  nothing by that name (the linker found none). Kept as it is when the
//  generator runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbuspendingcall.h, Qt 6.12.0.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbuspendingcall.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusmessage.h>

//  QDBusPendingCall::QDBusPendingCall(const QDBusPendingCall &other)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCallC1ERKS_(
    const QDBusPendingCall *other) {
  return new QDBusPendingCall(*other);
}

//  QDBusPendingCall::QDBusPendingCall(QDBusPendingCall &&other)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCallC1EOS_(
    QDBusPendingCall *other) {
  return new QDBusPendingCall(std::move(*other));
}

//  QDBusPendingCall::~QDBusPendingCall()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusPendingCallD1Ev(QDBusPendingCall *self) {
  delete self;
}

//  QDBusPendingCall &QDBusPendingCall::operator=(QDBusPendingCall &&other)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCallaSEOS_(
    QDBusPendingCall *self,
    QDBusPendingCall *other) {
  return &(self->operator=(std::move(*other)));
}

//  QDBusPendingCall &QDBusPendingCall::operator=(const QDBusPendingCall
//      &other)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCallaSERKS_(
    QDBusPendingCall *self,
    const QDBusPendingCall *other) {
  return &(self->operator=(*other));
}

//  void QDBusPendingCall::swap(QDBusPendingCall &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusPendingCall4swapERS_(
    QDBusPendingCall *self,
    QDBusPendingCall *other) {
  self->swap(*other);
}

#if !defined(Q_QDOC)
//  bool QDBusPendingCall::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDBusPendingCall10isFinishedEv(
    const QDBusPendingCall *self) {
  return self->isFinished();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  void QDBusPendingCall::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDBusPendingCall15waitForFinishedEv(QDBusPendingCall *self) {
  self->waitForFinished();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  bool QDBusPendingCall::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDBusPendingCall7isErrorEv(const QDBusPendingCall *self) {
  return self->isError();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  bool QDBusPendingCall::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDBusPendingCall7isValidEv(const QDBusPendingCall *self) {
  return self->isValid();
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QDBusError QDBusPendingCall::error() const
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZNK16QDBusPendingCall5errorEv(
    const QDBusPendingCall *self) {
  return new QDBusError(self->error());
}
#endif  // !defined(Q_QDOC)

#if !defined(Q_QDOC)
//  QDBusMessage QDBusPendingCall::reply() const
extern "C" Q_DECL_EXPORT
QDBusMessage *ritual_ZNK16QDBusPendingCall5replyEv(
    const QDBusPendingCall *self) {
  return new QDBusMessage(self->reply());
}
#endif  // !defined(Q_QDOC)

//  QDBusPendingCall QDBusPendingCall::fromError(const QDBusError &error)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCall9fromErrorERK10QDBusError(
    const QDBusError *error) {
  return new QDBusPendingCall(QDBusPendingCall::fromError(*error));
}

//  QDBusPendingCall QDBusPendingCall::fromCompletedCall(const QDBusMessage
//      &message)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCall17fromCompletedCallERK12QDBusMessage(
    const QDBusMessage *message) {
  return new QDBusPendingCall(QDBusPendingCall::fromCompletedCall(*message));
}

//  QDBusPendingCall::QDBusPendingCall(QDBusPendingCallPrivate *dd)
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_ZN16QDBusPendingCallC1EP23QDBusPendingCallPrivate(
    QDBusPendingCallPrivate *dd) {
  return new QDBusPendingCall(dd);
}

#endif  // !defined(QT_NO_DBUS)
