//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  bool
//      QV4::Compiler::Codegen::VolatileMemoryLocations::isVolatile(QStringVi
//      ew name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV48Compiler7Codegen23VolatileMemoryLocations10isVolatileE11QStringView(
    QV4::Compiler::Codegen::VolatileMemoryLocations *self,
    const QString *name) {
  return self->isVolatile(QStringView(*name));
}

//  void QV4::Compiler::Codegen::VolatileMemoryLocations::add(QStringView
//      name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen23VolatileMemoryLocations3addE11QStringView(
    QV4::Compiler::Codegen::VolatileMemoryLocations *self,
    const QString *name) {
  self->add(QStringView(*name));
}

//  void QV4::Compiler::Codegen::VolatileMemoryLocations::setAllVolatile()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen23VolatileMemoryLocations14setAllVolatileEv(
    QV4::Compiler::Codegen::VolatileMemoryLocations *self) {
  self->setAllVolatile();
}

//  QV4::Compiler::Codegen::VolatileMemoryLocations::~VolatileMemoryLocations
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen23VolatileMemoryLocationsD1Ev(
    QV4::Compiler::Codegen::VolatileMemoryLocations *self) {
  delete self;
}
