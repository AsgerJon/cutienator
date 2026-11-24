//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapresource_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapresource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCoapResourcePrivate::QCoapResourcePrivate()
extern "C" Q_DECL_EXPORT
QCoapResourcePrivate *ritual_ZN20QCoapResourcePrivateC1Ev() {
  return new QCoapResourcePrivate();
}

//  QCoapResourcePrivate::QCoapResourcePrivate(const QCoapResourcePrivate
//      &other)
extern "C" Q_DECL_EXPORT
QCoapResourcePrivate *ritual_ZN20QCoapResourcePrivateC1ERKS_(
    const QCoapResourcePrivate *other) {
  return new QCoapResourcePrivate(*other);
}

//  QCoapResourcePrivate::~QCoapResourcePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCoapResourcePrivateD1Ev(QCoapResourcePrivate *self) {
  delete self;
}
