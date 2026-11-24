//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenera
//  tor_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercodegenerator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGFragmentShaderGenerator::QSSGFragmentShaderGenerator()
extern "C" Q_DECL_EXPORT
QSSGFragmentShaderGenerator *ritual_ZN27QSSGFragmentShaderGeneratorC1Ev() {
  return new QSSGFragmentShaderGenerator();
}

//  void QSSGFragmentShaderGenerator::addShaderIncomingMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGFragmentShaderGenerator20addShaderIncomingMapEv(
    QSSGFragmentShaderGenerator *self) {
  self->addShaderIncomingMap();
}

//  void QSSGFragmentShaderGenerator::addShaderOutgoingMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGFragmentShaderGenerator20addShaderOutgoingMapEv(
    QSSGFragmentShaderGenerator *self) {
  self->addShaderOutgoingMap();
}

//  QSSGFragmentShaderGenerator::~QSSGFragmentShaderGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QSSGFragmentShaderGeneratorD1Ev(
    QSSGFragmentShaderGenerator *self) {
  delete self;
}
