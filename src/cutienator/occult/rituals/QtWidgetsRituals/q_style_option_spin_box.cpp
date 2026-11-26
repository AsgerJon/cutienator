//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(spinbox)
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionSpinBox::QStyleOptionSpinBox()
extern "C" Q_DECL_EXPORT
QStyleOptionSpinBox *ritual_ZN19QStyleOptionSpinBoxC1Ev() {
  return new QStyleOptionSpinBox();
}

//  QStyleOptionSpinBox::QStyleOptionSpinBox(const QStyleOptionSpinBox
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionSpinBox *ritual_ZN19QStyleOptionSpinBoxC1ERKS_(
    const QStyleOptionSpinBox *other) {
  return new QStyleOptionSpinBox(*other);
}

//  QStyleOptionSpinBox &QStyleOptionSpinBox::operator=(const
//      QStyleOptionSpinBox &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionSpinBox *ritual_ZN19QStyleOptionSpinBoxaSERKS_(
    QStyleOptionSpinBox *self,
    const QStyleOptionSpinBox *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionSpinBox::QStyleOptionSpinBox(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionSpinBox *ritual_ZN19QStyleOptionSpinBoxC1Ei(int version) {
  return new QStyleOptionSpinBox(version);
}

//  QStyleOptionSpinBox::~QStyleOptionSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyleOptionSpinBoxD1Ev(QStyleOptionSpinBox *self) {
  delete self;
}

#endif  // QT_CONFIG(spinbox)
