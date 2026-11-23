//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionProgressBar::QStyleOptionProgressBar()
extern "C" Q_DECL_EXPORT
QStyleOptionProgressBar *ritual_ZN23QStyleOptionProgressBarC1Ev() {
  return new QStyleOptionProgressBar();
}

//  QStyleOptionProgressBar::QStyleOptionProgressBar(const
//      QStyleOptionProgressBar &other)
extern "C" Q_DECL_EXPORT
QStyleOptionProgressBar *ritual_ZN23QStyleOptionProgressBarC1ERKS_(
    const QStyleOptionProgressBar *other) {
  return new QStyleOptionProgressBar(*other);
}

//  QStyleOptionProgressBar::QStyleOptionProgressBar(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionProgressBar *ritual_ZN23QStyleOptionProgressBarC1Ei(
    int version) {
  return new QStyleOptionProgressBar(version);
}

//  QStyleOptionProgressBar::~QStyleOptionProgressBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QStyleOptionProgressBarD1Ev(QStyleOptionProgressBar *self) {
  delete self;
}
