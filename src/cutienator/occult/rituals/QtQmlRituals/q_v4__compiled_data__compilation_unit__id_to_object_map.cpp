//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::CompiledData::CompilationUnit::IdToObjectMap::insert(int a0,
//      int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMap6insertEii(
    QV4::CompiledData::CompilationUnit::IdToObjectMap *self,
    int a0,
    int a1) {
  self->insert(a0, a1);
}

//  void QV4::CompiledData::CompilationUnit::IdToObjectMap::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMap5clearEv(
    QV4::CompiledData::CompilationUnit::IdToObjectMap *self) {
  self->clear();
}

//  bool QV4::CompiledData::CompilationUnit::IdToObjectMap::contains(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMap8containsEi(
    QV4::CompiledData::CompilationUnit::IdToObjectMap *self,
    int a0) {
  return self->contains(a0);
}

//  QV4::CompiledData::CompilationUnit::IdToObjectMap::~IdToObjectMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData15CompilationUnit13IdToObjectMapD1Ev(
    QV4::CompiledData::CompilationUnit::IdToObjectMap *self) {
  delete self;
}
