//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcborcommon.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcborcommon.h>
#include <QtCore/qstring.h>

//  Code QCborError::operator QCborError::Code() const
extern "C" Q_DECL_EXPORT
QCborError::Code ritual_ZNK10QCborErrorcvNS_4CodeEEv(
    const QCborError *self) {
  return self->operator QCborError::Code();
}

//  QString QCborError::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCborError8toStringEv(const QCborError *self) {
  return new QString(self->toString());
}

//  QCborError::~QCborError()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCborErrorD1Ev(QCborError *self) {
  delete self;
}
