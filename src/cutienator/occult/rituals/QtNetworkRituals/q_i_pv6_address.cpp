//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhostaddress.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qhostaddress.h>

//  quint8 QIPv6Address::operator[](int index) const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK12QIPv6AddressixEi(const QIPv6Address *self, int index) {
  return self->operator[](index);
}

//  QIPv6Address::~QIPv6Address()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QIPv6AddressD1Ev(QIPv6Address *self) {
  delete self;
}
