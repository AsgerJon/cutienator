//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QV4::CompiledData::TemplateObject::calculateSize(int size)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData14TemplateObject13calculateSizeEi(int size) {
  return QV4::CompiledData::TemplateObject::calculateSize(size);
}

//  uint QV4::CompiledData::TemplateObject::stringIndexAt(uint i) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV412CompiledData14TemplateObject13stringIndexAtEj(
    const QV4::CompiledData::TemplateObject *self,
    uint i) {
  return self->stringIndexAt(i);
}

//  uint QV4::CompiledData::TemplateObject::rawStringIndexAt(uint i) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV412CompiledData14TemplateObject16rawStringIndexAtEj(
    const QV4::CompiledData::TemplateObject *self,
    uint i) {
  return self->rawStringIndexAt(i);
}

//  QV4::CompiledData::TemplateObject::~TemplateObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData14TemplateObjectD1Ev(
    QV4::CompiledData::TemplateObject *self) {
  delete self;
}
