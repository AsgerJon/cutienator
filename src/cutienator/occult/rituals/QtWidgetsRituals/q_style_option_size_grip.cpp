//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionSizeGrip::QStyleOptionSizeGrip()
extern "C" Q_DECL_EXPORT
QStyleOptionSizeGrip *ritual_ZN20QStyleOptionSizeGripC1Ev() {
  return new QStyleOptionSizeGrip();
}

//  QStyleOptionSizeGrip::QStyleOptionSizeGrip(const QStyleOptionSizeGrip
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionSizeGrip *ritual_ZN20QStyleOptionSizeGripC1ERKS_(
    const QStyleOptionSizeGrip *other) {
  return new QStyleOptionSizeGrip(*other);
}

//  QStyleOptionSizeGrip &QStyleOptionSizeGrip::operator=(const
//      QStyleOptionSizeGrip &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionSizeGrip *ritual_ZN20QStyleOptionSizeGripaSERKS_(
    QStyleOptionSizeGrip *self,
    const QStyleOptionSizeGrip *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionSizeGrip::QStyleOptionSizeGrip(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionSizeGrip *ritual_ZN20QStyleOptionSizeGripC1Ei(int version) {
  return new QStyleOptionSizeGrip(version);
}

//  QStyleOptionSizeGrip::~QStyleOptionSizeGrip()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionSizeGripD1Ev(QStyleOptionSizeGrip *self) {
  delete self;
}
