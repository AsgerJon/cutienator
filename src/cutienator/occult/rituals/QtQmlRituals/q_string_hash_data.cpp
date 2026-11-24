//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qstringhash_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qstringhash_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QStringHashData::QStringHashData()
extern "C" Q_DECL_EXPORT
QStringHashData *ritual_ZN15QStringHashDataC1Ev() {
  return new QStringHashData();
}

//  QStringHashData::~QStringHashData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringHashDataD1Ev(QStringHashData *self) {
  delete self;
}

//  void QStringHashData::rehashToBits(short bits)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringHashData12rehashToBitsEs(
    QStringHashData *self,
    short bits) {
  self->rehashToBits(bits);
}

//  void QStringHashData::rehashToSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStringHashData12rehashToSizeEi(
    QStringHashData *self,
    int size) {
  self->rehashToSize(size);
}
