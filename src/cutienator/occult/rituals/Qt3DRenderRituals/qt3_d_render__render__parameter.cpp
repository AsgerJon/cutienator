//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/parameter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/parameter_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/uniform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  int Qt3DRender::Render::Parameter::nameId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render9Parameter6nameIdEv(
    const Qt3DRender::Render::Parameter *self) {
  return self->nameId();
}

//  const UniformValue &Qt3DRender::Render::Parameter::uniformValue() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UniformValue *ritual_ZNK10Qt3DRender6Render9Parameter12uniformValueEv(
    const Qt3DRender::Render::Parameter *self) {
  return new Qt3DRender::Render::UniformValue(self->uniformValue());
}

//  QVariant Qt3DRender::Render::Parameter::backendValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DRender6Render9Parameter12backendValueEv(
    const Qt3DRender::Render::Parameter *self) {
  return new QVariant(self->backendValue());
}

//  void Qt3DRender::Render::Parameter::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render9Parameter16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Parameter *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Parameter::syncFromFrontEnd(frontEnd, firstTime);
}
