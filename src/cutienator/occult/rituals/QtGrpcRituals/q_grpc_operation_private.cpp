//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpcoperation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/qgrpcoperation.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpcoperation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <optional>
#include <QtCore/QByteArray>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/private/qgrpcoperation_p.h>
#include <QtGrpc/private/qgrpcoperationcontext_p.h>
#include <QtGrpc/private/qtgrpclogging_p.h>
#include <QtGrpc/qabstractgrpcchannel.h>
#include <QtGrpc/qgrpcoperation.h>
#include <QtGrpc/qgrpcoperationcontext.h>
#include <QtProtobuf/private/qprotobufmessage_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qeventloop.h>
#include <QtCore/qpointer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtgrpc/src/grpc/qgrpcoperation.cpp, line 25, as _ZN21QGrpcOperationPrivate18asyncFinishInvalidEO11QGrpcStatus
inline void QGrpcOperationPrivate::asyncFinishInvalid(QGrpcStatus &&status)
{
    Q_ASSERT(!status.isOk());
    Q_Q(QGrpcOperation);
    state = State::Invalid;
    QMetaObject::invokeMethod(
        q,
        [qPtr = QPointer(q), s = std::move(status)] {
            if (!qPtr)
                return;
            emit qPtr->context().finished(s);
        },
        Qt::QueuedConnection);
}

//  from ../qtgrpc/src/grpc/qgrpcoperation.cpp, line 40, as _ZN21QGrpcOperationPrivate23serializeInitialMessageERK16QProtobufMessage
inline std::optional<QByteArray>
QGrpcOperationPrivate::serializeInitialMessage(const QProtobufMessage &message)
{
    const auto serializer = operationContext->serializer();
    auto ch = channel.lock();

    Q_ASSERT(state == State::Valid);
    Q_ASSERT(serializer);
    Q_ASSERT(ch.get()); // This function should only be called if the channel is valid

    auto &interceptorEngine = QAbstractGrpcChannelPrivate::get(ch.get())->interceptorEngine;

    if (interceptorEngine.hasHandlerFor(QtGrpc::InterceptorCapability::Start)) {
        auto mt = QProtobufMessagePrivate::get(&message)->metaObject->metaType();
        auto *interceptedMessage = static_cast<QProtobufMessage *>(mt.create(&message));
        Q_ASSERT(interceptedMessage);
        const QScopeGuard mtGuard([mt = std::move(mt), interceptedMessage] {
            mt.destroy(interceptedMessage);
        });
        const auto continuation = interceptorEngine.onStart(*operationContext,
                                                            *interceptedMessage,
                                                            operationContext->d_func()->options);
        if (continuation == QGrpcStartInterceptor::Continuation::Drop) {
            Q_Q(QGrpcOperation);
            QMetaObject::invokeMethod(
                q,
                [qPtr = QPointer(q)] {
                    if (!qPtr)
                        return;
                    emit qPtr->context().finished({ QtGrpc::StatusCode::Aborted,
                                                    "Interceptors dropped the call"_L1 });
                },
                Qt::QueuedConnection);
            return {};
        }
        return serializer->serialize(interceptedMessage);
    }

    return serializer->serialize(&message);
}
//  -----------------------------------------------------------------------

//  QGrpcOperation *QGrpcOperationPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGrpcOperation *ritual_ZN21QGrpcOperationPrivate6q_funcEv(
    QGrpcOperationPrivate *self) {
  return self->q_func();
}

//  const QGrpcOperation *QGrpcOperationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGrpcOperation *ritual_ZNK21QGrpcOperationPrivate6q_funcEv(
    const QGrpcOperationPrivate *self) {
  return self->q_func();
}

//  QGrpcOperationPrivate::~QGrpcOperationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationPrivateD1Ev(QGrpcOperationPrivate *self) {
  delete self;
}

//  const QGrpcOperationPrivate *QGrpcOperationPrivate::get(const
//      QGrpcOperation *op)
extern "C" Q_DECL_EXPORT
const QGrpcOperationPrivate *ritual_ZN21QGrpcOperationPrivate3getEPK14QGrpcOperation(
    const QGrpcOperation *op) {
  return QGrpcOperationPrivate::get(op);
}

//  QGrpcOperationPrivate *QGrpcOperationPrivate::get(QGrpcOperation *op)
extern "C" Q_DECL_EXPORT
QGrpcOperationPrivate *ritual_ZN21QGrpcOperationPrivate3getEP14QGrpcOperation(
    QGrpcOperation *op) {
  return QGrpcOperationPrivate::get(op);
}

//  void QGrpcOperationPrivate::asyncFinishInvalid(QGrpcStatus &&status)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGrpcOperationPrivate18asyncFinishInvalidEO11QGrpcStatus(
    QGrpcOperationPrivate *self,
    QGrpcStatus *status) {
  self->asyncFinishInvalid(std::move(*status));
}

//  std::optional<QByteArray>
//      QGrpcOperationPrivate::serializeInitialMessage(const QProtobufMessage
//      &message)
extern "C" Q_DECL_EXPORT
std::optional<QByteArray> *ritual_ZN21QGrpcOperationPrivate23serializeInitialMessageERK16QProtobufMessage(
    QGrpcOperationPrivate *self,
    const QProtobufMessage *message) {
  return new std::optional<QByteArray>(
      self->serializeInitialMessage(
          *message));
}

//  a std::optional<QByteArray> a ritual of QGrpcOperationPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGrpcOperationPrivate__std_optional_QByteArray(
    std::optional<QByteArray> *self) {
  delete self;
}
