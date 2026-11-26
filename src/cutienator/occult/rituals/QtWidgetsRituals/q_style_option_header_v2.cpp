//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionHeaderV2::QStyleOptionHeaderV2()
extern "C" Q_DECL_EXPORT
QStyleOptionHeaderV2 *ritual_ZN20QStyleOptionHeaderV2C1Ev() {
  return new QStyleOptionHeaderV2();
}

//  QStyleOptionHeaderV2::QStyleOptionHeaderV2(const QStyleOptionHeaderV2
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionHeaderV2 *ritual_ZN20QStyleOptionHeaderV2C1ERKS_(
    const QStyleOptionHeaderV2 *other) {
  return new QStyleOptionHeaderV2(*other);
}

//  QStyleOptionHeaderV2 &QStyleOptionHeaderV2::operator=(const
//      QStyleOptionHeaderV2 &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionHeaderV2 *ritual_ZN20QStyleOptionHeaderV2aSERKS_(
    QStyleOptionHeaderV2 *self,
    const QStyleOptionHeaderV2 *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionHeaderV2::QStyleOptionHeaderV2(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionHeaderV2 *ritual_ZN20QStyleOptionHeaderV2C1Ei(int version) {
  return new QStyleOptionHeaderV2(version);
}

//  QStyleOptionHeaderV2::~QStyleOptionHeaderV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionHeaderV2D1Ev(QStyleOptionHeaderV2 *self) {
  delete self;
}
