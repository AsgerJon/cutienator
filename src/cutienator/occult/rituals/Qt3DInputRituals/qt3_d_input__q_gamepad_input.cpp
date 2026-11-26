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

//  void *Qt3DInput::QGamepadInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput13QGamepadInput11qt_metacastEPKc(
    Qt3DInput::QGamepadInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::QGamepadInput::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput13QGamepadInput11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::QGamepadInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DInput::QGamepadInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput13QGamepadInput2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QGamepadInput::tr(s, c, n));
}

//  Qt3DInput::QGamepadInput::QGamepadInput(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DInput::QGamepadInput *ritual_ZN9Qt3DInput13QGamepadInputC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new Qt3DInput::QGamepadInput(parent);
}

//  int Qt3DInput::QGamepadInput::deviceId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput13QGamepadInput8deviceIdEv(
    const Qt3DInput::QGamepadInput *self) {
  return self->deviceId();
}

//  void Qt3DInput::QGamepadInput::setDeviceId(int deviceId)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QGamepadInput11setDeviceIdEi(
    Qt3DInput::QGamepadInput *self,
    int deviceId) {
  self->setDeviceId(deviceId);
}

//  void Qt3DInput::QGamepadInput::deviceIdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput13QGamepadInput15deviceIdChangedEv(
    Qt3DInput::QGamepadInput *self) {
  self->deviceIdChanged();
}

//  QGamepadInputPrivate *Qt3DInput::QGamepadInput::d_func()
extern "C" Q_DECL_EXPORT
QGamepadInputPrivate *ritual_ZN9Qt3DInput13QGamepadInput6d_funcEv(
    Qt3DInput::QGamepadInput *self) {
  return self->d_func();
}

//  const QGamepadInputPrivate *Qt3DInput::QGamepadInput::d_func() const
extern "C" Q_DECL_EXPORT
const QGamepadInputPrivate *ritual_ZNK9Qt3DInput13QGamepadInput6d_funcEv(
    const Qt3DInput::QGamepadInput *self) {
  return self->d_func();
}

#endif  // 0
