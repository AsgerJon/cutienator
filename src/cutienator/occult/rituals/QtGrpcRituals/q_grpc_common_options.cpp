//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/6.12.0/QtGrpc/private/qgrpccommonoptions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtGrpc/QtGrpc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/6.12.0/QtGrpc/private/qgrpccommonoptions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGrpc/private/qgrpccommonoptions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 195, as _ZN18QGrpcCommonOptions23setFilterServerMetadataEb
inline void QGrpcCommonOptions::setFilterServerMetadata(bool value)
{
    m_filterServerMetadata = value;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 243, as _ZN18QGrpcCommonOptions28setMaximumReceiveMessageSizeEy
inline void QGrpcCommonOptions::setMaximumReceiveMessageSize(quint64 size)
{
    m_maximumReceiveMessageSize = size;
}

//  from ../qtgrpc/src/grpc/qgrpccommonoptions.cpp, line 286, as _ZN18QGrpcCommonOptions21setRequestCompressionEN6QtGrpc20CompressionAlgorithmE
inline void QGrpcCommonOptions::setRequestCompression(QtGrpc::CompressionAlgorithm algorithm)
{
    m_requestCompression = algorithm;
}
//  -----------------------------------------------------------------------

//  QGrpcCommonOptions::QGrpcCommonOptions()
extern "C" Q_DECL_EXPORT
QGrpcCommonOptions *ritual_ZN18QGrpcCommonOptionsC1Ev() {
  return new QGrpcCommonOptions();
}

//  QGrpcCommonOptions::~QGrpcCommonOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptionsD1Ev(QGrpcCommonOptions *self) {
  delete self;
}

//  void QGrpcCommonOptions::setFilterServerMetadata(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions23setFilterServerMetadataEb(
    QGrpcCommonOptions *self,
    bool value) {
  self->setFilterServerMetadata(value);
}

//  void QGrpcCommonOptions::setMaximumReceiveMessageSize(quint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions28setMaximumReceiveMessageSizeEy(
    QGrpcCommonOptions *self,
    quint64 size) {
  self->setMaximumReceiveMessageSize(size);
}

//  void
//      QGrpcCommonOptions::setRequestCompression(QtGrpc::CompressionAlgorith
//      m algorithm)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGrpcCommonOptions21setRequestCompressionEN6QtGrpc20CompressionAlgorithmE(
    QGrpcCommonOptions *self,
    QtGrpc::CompressionAlgorithm algorithm) {
  self->setRequestCompression(algorithm);
}
