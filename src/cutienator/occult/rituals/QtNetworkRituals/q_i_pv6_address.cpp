//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qhostaddress.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, rituals for functions the generator leaves out: 1. Kept as it is
//  when the generator runs again.
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

//  quint8 &QIPv6Address::operator[](int index)
extern "C" Q_DECL_EXPORT
quint8 *ritual_ZN12QIPv6AddressixEi(
    QIPv6Address *self,
    int index) {
  return &((*self)[index]);
}
