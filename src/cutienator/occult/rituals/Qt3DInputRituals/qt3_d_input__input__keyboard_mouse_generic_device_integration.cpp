//  Written by dev_tooling.RitualGenerator from the records of Qt3DInput/6.12
//  .0/Qt3DInput/private/keyboardmousegenericdeviceintegration_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/keyboardmousegenericdeviceintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/Qt3DCore>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/keyboardmousegenericdeviceintegration_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 21, as _ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegrationD1Ev
namespace Qt3DInput::Input {
inline KeyboardMouseGenericDeviceIntegration::~KeyboardMouseGenericDeviceIntegration()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 29, as _ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration13jobsToExecuteEx
namespace Qt3DInput::Input {
inline std::vector<Qt3DCore::QAspectJobPtr> KeyboardMouseGenericDeviceIntegration::jobsToExecute(qint64 time)
{
    Q_UNUSED(time);
    return {};
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 35, as _ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration20createPhysicalDeviceERK7QString
namespace Qt3DInput::Input {
inline QAbstractPhysicalDevice *KeyboardMouseGenericDeviceIntegration::createPhysicalDevice(const QString &name)
{
    Q_UNUSED(name);
    return nullptr;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 41, as _ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration15physicalDevicesEv
namespace Qt3DInput::Input {
inline QList<Qt3DCore::QNodeId> KeyboardMouseGenericDeviceIntegration::physicalDevices() const
{
    // TO DO: could return the ids of active KeyboardDevice/MouseDevice
    return { };
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 47, as _ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration14physicalDeviceEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline QAbstractPhysicalDeviceBackendNode *KeyboardMouseGenericDeviceIntegration::physicalDevice(Qt3DCore::QNodeId id) const
{
    QAbstractPhysicalDeviceBackendNode *device = m_handler->keyboardDeviceManager()->lookupResource(id);
    if (!device)
        device = m_handler->mouseDeviceManager()->lookupResource(id);
    if (!device)
        device = m_handler->genericDeviceBackendNodeManager()->lookupResource(id);
    return device;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 25, as _ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration12onInitializeEv
namespace Qt3DInput::Input {
inline void KeyboardMouseGenericDeviceIntegration::onInitialize()
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  A Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration that Python can take functions over in. Every Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegration : public Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration {
public:
  using Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::KeyboardMouseGenericDeviceIntegration;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall0 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall1 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall2 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall3 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall4 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall5 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall6 call = reinterpret_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegrationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::metaObject(
//      ) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration10metaObjectEv(
    const Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self) {
  return self->metaObject();
}

//  void *Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::qt_metacas
//      t(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration11qt_metacastEPKc(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::qt_metacall(
//      QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::~KeyboardMouseGe
//      nericDeviceIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegrationD1Ev(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self) {
  delete self;
}

//  std::vector<Qt3DCore::QAspectJobPtr> Qt3DInput::Input::KeyboardMouseGener
//      icDeviceIntegration::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration13jobsToExecuteEx(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
}

//  QAbstractPhysicalDevice *Qt3DInput::Input::KeyboardMouseGenericDeviceInte
//      gration::createPhysicalDevice(const QString &name)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration20createPhysicalDeviceERK7QString(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self,
    const QString *name) {
  return self->createPhysicalDevice(*name);
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::KeyboardMouseGenericDeviceInte
//      gration::physicalDevices() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration15physicalDevicesEv(
    const Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self) {
  return new QList<Qt3DCore::QNodeId>(self->physicalDevices());
}

//  QAbstractPhysicalDeviceBackendNode *Qt3DInput::Input::KeyboardMouseGeneri
//      cDeviceIntegration::physicalDevice(Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceBackendNode *ritual_ZNK9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration14physicalDeviceEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self,
    const Qt3DCore::QNodeId *id) {
  return self->physicalDevice(*id);
}

//  void
//      Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration::onInitialize
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegration12onInitializeEv(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self) {
  self->onInitialize();
}

//  a Python function taken by a
//      CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_Input_KeyboardMouseGenericDeviceIntegration(
    Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_Input_KeyboardMouseGenericDeviceIntegration *>(self)->take(key, call);
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_KeyboardMouseGenericDeviceIntegration__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DInput::Input::KeyboardMouseGenericDeviceIntegration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_KeyboardMouseGenericDeviceIntegration__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
