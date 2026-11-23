//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionToolButton::QStyleOptionToolButton()
extern "C" Q_DECL_EXPORT
QStyleOptionToolButton *ritual_ZN22QStyleOptionToolButtonC1Ev() {
  return new QStyleOptionToolButton();
}

//  QStyleOptionToolButton::QStyleOptionToolButton(const
//      QStyleOptionToolButton &other)
extern "C" Q_DECL_EXPORT
QStyleOptionToolButton *ritual_ZN22QStyleOptionToolButtonC1ERKS_(
    const QStyleOptionToolButton *other) {
  return new QStyleOptionToolButton(*other);
}

//  QStyleOptionToolButton::QStyleOptionToolButton(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionToolButton *ritual_ZN22QStyleOptionToolButtonC1Ei(int version) {
  return new QStyleOptionToolButton(version);
}

//  QStyleOptionToolButton::~QStyleOptionToolButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleOptionToolButtonD1Ev(QStyleOptionToolButton *self) {
  delete self;
}
