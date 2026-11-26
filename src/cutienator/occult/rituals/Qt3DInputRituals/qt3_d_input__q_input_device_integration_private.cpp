//  Written by hand on 2026-11-25 from
//  Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Its header does not stand alone: Q_DECLARE_PUBLIC in it needs
//  'QInputDeviceIntegration' as a complete class, which only the header
//  of that class gives, so that header is included first. Not written:
//  the data member, and 'flagsForDumping' of QObjectPrivate (it gives a
//  std::string). The Cute class takes the one other virtual function of
//  QObjectPrivate.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p.h>
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputdeviceintegration_p_p.h>
#include <QtCore/qdebug.h>
#include <cstring>

//  A Qt3DInput::QInputDeviceIntegrationPrivate that Python can take functions over in. Every Qt3DInput::QInputDeviceIntegrationPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#ifndef QT_NO_DEBUG_STREAM
typedef void (*CuteQt3DInput_QInputDeviceIntegrationPrivateCall0)(const void *, QDebug *, int *);
#endif  // QT_NO_DEBUG_STREAM
class CuteQt3DInput_QInputDeviceIntegrationPrivate : public Qt3DInput::QInputDeviceIntegrationPrivate {
public:
  using Qt3DInput::QInputDeviceIntegrationPrivate::QInputDeviceIntegrationPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#ifndef QT_NO_DEBUG_STREAM
    if (!std::strcmp(key, "_ZNK14QObjectPrivate18writeToDebugStreamER6QDebug")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_NO_DEBUG_STREAM
    return false;
  }

#ifndef QT_NO_DEBUG_STREAM
  //  void QObjectPrivate::writeToDebugStream(QDebug &a0) const
  void writeToDebugStream(QDebug &a0) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QInputDeviceIntegrationPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QInputDeviceIntegrationPrivateCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QObjectPrivate::writeToDebugStream(a0);
  }
#endif  // QT_NO_DEBUG_STREAM
};

//  Qt3DInput::QInputDeviceIntegrationPrivate::QInputDeviceIntegrationPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputDeviceIntegrationPrivate *ritual_ZN9Qt3DInput30QInputDeviceIntegrationPrivateC1Ev() {
  return new CuteQt3DInput_QInputDeviceIntegrationPrivate();
}

//  QInputDeviceIntegration
//      *Qt3DInput::QInputDeviceIntegrationPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputDeviceIntegration *ritual_ZN9Qt3DInput30QInputDeviceIntegrationPrivate6q_funcEv(
    Qt3DInput::QInputDeviceIntegrationPrivate *self) {
  return self->q_func();
}

//  const QInputDeviceIntegration
//      *Qt3DInput::QInputDeviceIntegrationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputDeviceIntegration *ritual_ZNK9Qt3DInput30QInputDeviceIntegrationPrivate6q_funcEv(
    const Qt3DInput::QInputDeviceIntegrationPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DInput_QInputDeviceIntegrationPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputDeviceIntegrationPrivate(
    Qt3DInput::QInputDeviceIntegrationPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputDeviceIntegrationPrivate *>(self)->take(key, call);
}
