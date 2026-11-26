//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOption::QStyleOption(int version, int type)
extern "C" Q_DECL_EXPORT
QStyleOption *ritual_ZN12QStyleOptionC1Eii(int version, int type) {
  return new QStyleOption(version, type);
}

//  QStyleOption::QStyleOption(const QStyleOption &other)
extern "C" Q_DECL_EXPORT
QStyleOption *ritual_ZN12QStyleOptionC1ERKS_(const QStyleOption *other) {
  return new QStyleOption(*other);
}

//  QStyleOption::~QStyleOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QStyleOptionD1Ev(QStyleOption *self) {
  delete self;
}

//  void QStyleOption::initFrom(const QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QStyleOption8initFromEPK7QWidget(
    QStyleOption *self,
    const QWidget *w) {
  self->initFrom(w);
}

//  QStyleOption &QStyleOption::operator=(const QStyleOption &other)
extern "C" Q_DECL_EXPORT
QStyleOption *ritual_ZN12QStyleOptionaSERKS_(
    QStyleOption *self,
    const QStyleOption *other) {
  return &(self->operator=(*other));
}
