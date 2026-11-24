//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QV4::CompiledData::JSClass::calculateSize(int nMembers)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData7JSClass13calculateSizeEi(int nMembers) {
  return QV4::CompiledData::JSClass::calculateSize(nMembers);
}

//  QV4::CompiledData::JSClass::~JSClass()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData7JSClassD1Ev(
    QV4::CompiledData::JSClass *self) {
  delete self;
}
