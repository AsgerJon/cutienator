//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBinaryJsonPrivate::MutableData::MutableData(uint reserved,
//      QJsonValue::Type valueType)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::MutableData *ritual_ZN18QBinaryJsonPrivate11MutableDataC1EjN10QJsonValue4TypeE(
    uint reserved,
    QJsonValue::Type valueType) {
  return new QBinaryJsonPrivate::MutableData(reserved, valueType);
}

//  QBinaryJsonPrivate::MutableData::~MutableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate11MutableDataD1Ev(
    QBinaryJsonPrivate::MutableData *self) {
  delete self;
}

//  MutableData *QBinaryJsonPrivate::MutableData::clone(const Base *b, uint
//      reserve)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::MutableData *ritual_ZN18QBinaryJsonPrivate11MutableData5cloneEPKNS_4BaseEj(
    QBinaryJsonPrivate::MutableData *self,
    const QBinaryJsonPrivate::Base *b,
    uint reserve) {
  return self->clone(b, reserve);
}
