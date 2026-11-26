//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionButton::QStyleOptionButton()
extern "C" Q_DECL_EXPORT
QStyleOptionButton *ritual_ZN18QStyleOptionButtonC1Ev() {
  return new QStyleOptionButton();
}

//  QStyleOptionButton::QStyleOptionButton(const QStyleOptionButton &other)
extern "C" Q_DECL_EXPORT
QStyleOptionButton *ritual_ZN18QStyleOptionButtonC1ERKS_(
    const QStyleOptionButton *other) {
  return new QStyleOptionButton(*other);
}

//  QStyleOptionButton &QStyleOptionButton::operator=(const
//      QStyleOptionButton &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionButton *ritual_ZN18QStyleOptionButtonaSERKS_(
    QStyleOptionButton *self,
    const QStyleOptionButton *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionButton::QStyleOptionButton(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionButton *ritual_ZN18QStyleOptionButtonC1Ei(int version) {
  return new QStyleOptionButton(version);
}

//  QStyleOptionButton::~QStyleOptionButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStyleOptionButtonD1Ev(QStyleOptionButton *self) {
  delete self;
}
