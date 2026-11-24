//  Written by dev_tooling.RitualGenerator from the records of
//  QtGrpc/qtgrpcnamespace.h, Qt 6.12.0. Changes made here are lost.
#include <QtGrpc/qtgrpcnamespace.h>
#include <QtCore/qdebug.h>

//  bool operator==(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QtGrpceqERKNS_13RpcDescriptorES2_(
    const QtGrpc::RpcDescriptor *lhs,
    const QtGrpc::RpcDescriptor *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QtGrpcneERKNS_13RpcDescriptorES2_(
    const QtGrpc::RpcDescriptor *lhs,
    const QtGrpc::RpcDescriptor *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QtGrpcltERKNS_13RpcDescriptorES2_(
    const QtGrpc::RpcDescriptor *lhs,
    const QtGrpc::RpcDescriptor *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QtGrpcgtERKNS_13RpcDescriptorES2_(
    const QtGrpc::RpcDescriptor *lhs,
    const QtGrpc::RpcDescriptor *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QtGrpcleERKNS_13RpcDescriptorES2_(
    const QtGrpc::RpcDescriptor *lhs,
    const QtGrpc::RpcDescriptor *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const RpcDescriptor &lhs, const RpcDescriptor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QtGrpcgeERKNS_13RpcDescriptorES2_(
    const QtGrpc::RpcDescriptor *lhs,
    const QtGrpc::RpcDescriptor *rhs) {
  return operator>=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const RpcDescriptor &description)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN6QtGrpclsE6QDebugRKNS_13RpcDescriptorE(
    const QDebug *debug,
    const QtGrpc::RpcDescriptor *description) {
  return new QDebug(operator<<(*debug, *description));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QtGrpc::RpcDescriptor::~RpcDescriptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QtGrpc13RpcDescriptorD1Ev(QtGrpc::RpcDescriptor *self) {
  delete self;
}
