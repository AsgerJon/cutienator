//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionRubberBand::QStyleOptionRubberBand()
extern "C" Q_DECL_EXPORT
QStyleOptionRubberBand *ritual_ZN22QStyleOptionRubberBandC1Ev() {
  return new QStyleOptionRubberBand();
}

//  QStyleOptionRubberBand::QStyleOptionRubberBand(const
//      QStyleOptionRubberBand &other)
extern "C" Q_DECL_EXPORT
QStyleOptionRubberBand *ritual_ZN22QStyleOptionRubberBandC1ERKS_(
    const QStyleOptionRubberBand *other) {
  return new QStyleOptionRubberBand(*other);
}

//  QStyleOptionRubberBand::~QStyleOptionRubberBand()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleOptionRubberBandD1Ev(QStyleOptionRubberBand *self) {
  delete self;
}
