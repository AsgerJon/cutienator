//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(slider)
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionSlider::QStyleOptionSlider()
extern "C" Q_DECL_EXPORT
QStyleOptionSlider *ritual_ZN18QStyleOptionSliderC1Ev() {
  return new QStyleOptionSlider();
}

//  QStyleOptionSlider::QStyleOptionSlider(const QStyleOptionSlider &other)
extern "C" Q_DECL_EXPORT
QStyleOptionSlider *ritual_ZN18QStyleOptionSliderC1ERKS_(
    const QStyleOptionSlider *other) {
  return new QStyleOptionSlider(*other);
}

//  QStyleOptionSlider &QStyleOptionSlider::operator=(const
//      QStyleOptionSlider &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionSlider *ritual_ZN18QStyleOptionSlideraSERKS_(
    QStyleOptionSlider *self,
    const QStyleOptionSlider *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionSlider::QStyleOptionSlider(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionSlider *ritual_ZN18QStyleOptionSliderC1Ei(int version) {
  return new QStyleOptionSlider(version);
}

//  QStyleOptionSlider::~QStyleOptionSlider()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStyleOptionSliderD1Ev(QStyleOptionSlider *self) {
  delete self;
}

#endif  // QT_CONFIG(slider)
