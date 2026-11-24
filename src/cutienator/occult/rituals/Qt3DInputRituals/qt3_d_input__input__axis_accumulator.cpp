//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/axisaccumulator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/axisaccumulator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DCore::QNodeId Qt3DInput::Input::AxisAccumulator::sourceAxisId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input15AxisAccumulator12sourceAxisIdEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return new Qt3DCore::QNodeId(self->sourceAxisId());
}

//  QAxisAccumulator::SourceAxisType
//      Qt3DInput::Input::AxisAccumulator::sourceAxisType() const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisAccumulator::SourceAxisType ritual_ZNK9Qt3DInput5Input15AxisAccumulator14sourceAxisTypeEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->sourceAxisType();
}

//  float Qt3DInput::Input::AxisAccumulator::scale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15AxisAccumulator5scaleEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->scale();
}

//  float Qt3DInput::Input::AxisAccumulator::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15AxisAccumulator5valueEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->value();
}

//  float Qt3DInput::Input::AxisAccumulator::velocity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9Qt3DInput5Input15AxisAccumulator8velocityEv(
    const Qt3DInput::Input::AxisAccumulator *self) {
  return self->velocity();
}
