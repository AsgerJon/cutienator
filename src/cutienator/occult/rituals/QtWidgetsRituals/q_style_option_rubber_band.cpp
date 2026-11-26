//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(rubberband)
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

//  QStyleOptionRubberBand &QStyleOptionRubberBand::operator=(const
//      QStyleOptionRubberBand &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionRubberBand *ritual_ZN22QStyleOptionRubberBandaSERKS_(
    QStyleOptionRubberBand *self,
    const QStyleOptionRubberBand *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionRubberBand::QStyleOptionRubberBand(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionRubberBand *ritual_ZN22QStyleOptionRubberBandC1Ei(int version) {
  return new QStyleOptionRubberBand(version);
}

//  QStyleOptionRubberBand::~QStyleOptionRubberBand()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleOptionRubberBandD1Ev(QStyleOptionRubberBand *self) {
  delete self;
}

#endif  // QT_CONFIG(rubberband)
