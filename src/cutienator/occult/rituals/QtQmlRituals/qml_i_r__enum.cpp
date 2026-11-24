//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QmlIR::Enum::enumValueCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QmlIR4Enum14enumValueCountEv(const QmlIR::Enum *self) {
  return self->enumValueCount();
}

//  QmlIR::Enum::~Enum()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR4EnumD1Ev(QmlIR::Enum *self) {
  delete self;
}
