//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qplugin_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(DecodedArchRequirements r1, DecodedArchRequirements r2)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12_GLOBAL__N_1eqENS_23DecodedArchRequirementsES0_(
    const DecodedArchRequirements *r1,
    const DecodedArchRequirements *r2) {
  return operator==(*r1, *r2);
}

//  ::DecodedArchRequirements::~DecodedArchRequirements()
extern "C" Q_DECL_EXPORT
void ritual_ZN023DecodedArchRequirementsD1Ev(
    ::DecodedArchRequirements *self) {
  delete self;
}
