//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtcpkeepaliveconfiguration_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtcpkeepaliveconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QTcpKeepAliveConfiguration::isEqual(const QTcpKeepAliveConfiguration
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QTcpKeepAliveConfiguration7isEqualERKS_(
    const QTcpKeepAliveConfiguration *self,
    const QTcpKeepAliveConfiguration *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QTcpKeepAliveConfiguration &lhs, const
//      QTcpKeepAliveConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QTcpKeepAliveConfigurationS1_(
    const QTcpKeepAliveConfiguration *lhs,
    const QTcpKeepAliveConfiguration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QTcpKeepAliveConfiguration &lhs, const
//      QTcpKeepAliveConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QTcpKeepAliveConfigurationS1_(
    const QTcpKeepAliveConfiguration *lhs,
    const QTcpKeepAliveConfiguration *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QTcpKeepAliveConfiguration::~QTcpKeepAliveConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QTcpKeepAliveConfigurationD1Ev(
    QTcpKeepAliveConfiguration *self) {
  delete self;
}
