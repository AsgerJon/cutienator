//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qndefrecord_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qndefrecord_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QNdefRecordPrivate::QNdefRecordPrivate()
extern "C" Q_DECL_EXPORT
QNdefRecordPrivate *ritual_ZN18QNdefRecordPrivateC1Ev() {
  return new QNdefRecordPrivate();
}

//  QNdefRecordPrivate::~QNdefRecordPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QNdefRecordPrivateD1Ev(QNdefRecordPrivate *self) {
  delete self;
}
