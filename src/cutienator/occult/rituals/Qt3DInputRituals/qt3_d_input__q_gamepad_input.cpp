//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qgamepadinput_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/qt3dinput_global.h>
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#if 0
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qgamepadinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *Qt3DInput::QGamepadInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput13QGamepadInput10metaObjectEv(
    const Qt3DInput::QGamepadInput *self) {
  return self->metaObject();
}

//  QString Qt3DInput::QGamepadInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput13QGamepadInput2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QGamepadInput::tr(s, c, n));
}

#endif  // 0
