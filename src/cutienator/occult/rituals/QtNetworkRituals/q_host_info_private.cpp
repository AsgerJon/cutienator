//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QHostInfoPrivate::QHostInfoPrivate()
extern "C" Q_DECL_EXPORT
QHostInfoPrivate *ritual_ZN16QHostInfoPrivateC1Ev() {
  return new QHostInfoPrivate();
}

//  QHostInfoPrivate::~QHostInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QHostInfoPrivateD1Ev(QHostInfoPrivate *self) {
  delete self;
}
