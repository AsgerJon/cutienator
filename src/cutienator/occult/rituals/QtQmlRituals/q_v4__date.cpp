//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Date::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initEv(QV4::Date *self) {
  self->init();
}

//  void QV4::Date::init(Date date)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Date4initES0_(QV4::Date *self, const QV4::Date *date) {
  self->init(*date);
}

//  double QV4::Date::operator double() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV44DatecvdEv(const QV4::Date *self) {
  return self->operator double();
}

//  QV4::Date::~Date()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44DateD1Ev(QV4::Date *self) {
  delete self;
}
