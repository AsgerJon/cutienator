//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirloader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlIRLoader::QQmlIRLoader(const QV4::CompiledData::Unit *unit,
//      QmlIR::Document *output)
extern "C" Q_DECL_EXPORT
QQmlIRLoader *ritual_ZN12QQmlIRLoaderC1EPKN3QV412CompiledData4UnitEPN5QmlIR8DocumentE(
    const QV4::CompiledData::Unit *unit,
    QmlIR::Document *output) {
  return new QQmlIRLoader(unit, output);
}

//  void QQmlIRLoader::load()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlIRLoader4loadEv(QQmlIRLoader *self) {
  self->load();
}

//  QmlIR::Object *QQmlIRLoader::loadObject(const QV4::CompiledData::Object
//      *serializedObject)
extern "C" Q_DECL_EXPORT
QmlIR::Object *ritual_ZN12QQmlIRLoader10loadObjectEPKN3QV412CompiledData6ObjectE(
    QQmlIRLoader *self,
    const QV4::CompiledData::Object *serializedObject) {
  return self->loadObject(serializedObject);
}

//  QQmlIRLoader::~QQmlIRLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlIRLoaderD1Ev(QQmlIRLoader *self) {
  delete self;
}
