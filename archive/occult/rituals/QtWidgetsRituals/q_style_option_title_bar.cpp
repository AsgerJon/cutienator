//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionTitleBar::QStyleOptionTitleBar()
extern "C" Q_DECL_EXPORT
QStyleOptionTitleBar *ritual_ZN20QStyleOptionTitleBarC1Ev() {
  return new QStyleOptionTitleBar();
}

//  QStyleOptionTitleBar::QStyleOptionTitleBar(const QStyleOptionTitleBar
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionTitleBar *ritual_ZN20QStyleOptionTitleBarC1ERKS_(
    const QStyleOptionTitleBar *other) {
  return new QStyleOptionTitleBar(*other);
}

//  QStyleOptionTitleBar::QStyleOptionTitleBar(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionTitleBar *ritual_ZN20QStyleOptionTitleBarC1Ei(int version) {
  return new QStyleOptionTitleBar(version);
}

//  QStyleOptionTitleBar::~QStyleOptionTitleBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionTitleBarD1Ev(QStyleOptionTitleBar *self) {
  delete self;
}
