//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DXr/6.
//  12.0/QtQuick3DXr/private/qquick3dxrinputmanager_visionos_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  'defined(Q_OS_VISIONOS)'. Qt builds the visionOS files of Quick3DXr
//  (its 'visionos' directory) only when VISIONOS is set, as its
//  CMakeLists.txt says, and installs the header named here for no other
//  system. Kept as it is when the generator runs again.
//  Completed by hand on 2026-11-25: the OpenXR version of the class,
//  which Qt builds when VISIONOS is not set, as the CMakeLists.txt of
//  Quick3DXr says, and when <openxr/openxr.h> is there. The file now
//  stands under either; its header there is qopenxrinputmanager_p.h.
//  Added: handSpace and getPokeJointIndex, metaObject (the class is a
//  QObject there). The rituals the two versions share stay as they
//  were. Left out of the OpenXR version: the constructor, init,
//  teardown and the rest that calls OpenXR or a function of Qt that is
//  not exported (isHandActive and isHandTrackerActive call
//  QQuick3DXrHandInput, setInputValue calls QQuick3DXrActionMapper,
//  setupHandModel calls a private function), and what takes or gives a
//  QList, a QMap or std::function.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#if defined(Q_OS_VISIONOS) || __has_include(<openxr/openxr.h>)
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#if defined(Q_OS_VISIONOS)
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrinputmanager_visionos_p.h>
#else
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qopenxrinputmanager_p.h>
#endif  // defined(Q_OS_VISIONOS), else OpenXR
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/private/qquick3dxrcontroller_p.h>
#include <QtQuick3DXr/private/qquick3dxrinputmanager_p.h>
#if !defined(Q_OS_VISIONOS)
#endif
#include <QtQuick3DXr/private/qquick3dxrview_p.h>
#include <QtQuick3DXr/private/qquick3dxractionmapper_p.h>
#include <QtGui/qquaternion.h>
#include <QtQuick3DXr/private/qquick3dxrhandinput_p.h>
#include <QtQuick3DXr/private/qquick3dxrhandmodel_p.h>
#include <QtQuick3DXr/private/qquick3dxrcontroller_p.h> //### InputAction enum
#include <QtCore/QDebug>
#include <QtQuick3D/private/qquick3djoint_p.h>
#include <QtGui/qquaternion.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/xr/quick3dxr/qquick3dxrcontroller.cpp, line 186, as _ZN11QtQuick3DXr23handednessForControllerENS_10ControllerE
inline QtQuick3DXr::Handedness QtQuick3DXr::handednessForController(QtQuick3DXr::Controller controller)
{
    QSSG_ASSERT(controller != QtQuick3DXr::Controller::UnknownController, return QtQuick3DXr::Handedness::Right);
    switch (controller) {
    case QtQuick3DXr::Controller::LeftController:
        return QtQuick3DXr::Handedness::Left;
    case QtQuick3DXr::Controller::RightController:
        return QtQuick3DXr::Handedness::Right;
    default:
        Q_UNREACHABLE();
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 465, as _ZN29QQuick3DXrInputManagerPrivate3getEP22QQuick3DXrInputManager
inline QQuick3DXrInputManagerPrivate *QQuick3DXrInputManagerPrivate::get(QQuick3DXrInputManager *inputManager)
{
    QSSG_ASSERT(inputManager != nullptr, return nullptr);
    return inputManager->d_func();
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 936, as _ZN29QQuick3DXrInputManagerPrivate26setPosePositionAndRotationEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceERK9QVector3DRK11QQuaternion
inline void QQuick3DXrInputManagerPrivate::setPosePositionAndRotation(Handedness handedness, HandPoseSpace poseSpace, const QVector3D &position, const QQuaternion &rotation)
{
    for (auto *controller : std::as_const(m_controllers)) {
        if (QtQuick3DXr::handednessForController(static_cast<QtQuick3DXr::Controller>(controller->controller())) == handedness && static_cast<QtQuick3DXr::HandPoseSpace>(controller->poseSpace()) == poseSpace) {
            controller->setPosition(position);
            controller->setRotation(rotation);
        }
    }
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 1021, as _ZN29QQuick3DXrInputManagerPrivate18registerControllerEP20QQuick3DXrController
inline void QQuick3DXrInputManagerPrivate::registerController(QQuick3DXrController *controller)
{
    m_poseUsageDirty = true;
    if (static_cast<QtQuick3DXr::Controller>(controller->controller()) == QtQuick3DXr::Controller::UnknownController) {
        m_controllers.remove(controller);
        return;
    }
    // No point in checking whether it's already in the set: that's just as expensive as inserting
    m_controllers.insert(controller);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 1032, as _ZN29QQuick3DXrInputManagerPrivate20unregisterControllerEP20QQuick3DXrController
inline void QQuick3DXrInputManagerPrivate::unregisterController(QQuick3DXrController *controller)
{
    m_poseUsageDirty = m_controllers.remove(controller);
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 1037, as _ZN29QQuick3DXrInputManagerPrivate11isPoseInUseEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceE
inline bool QQuick3DXrInputManagerPrivate::isPoseInUse(Handedness handedness, HandPoseSpace poseSpace)
{
    QSSG_ASSERT(uint(handedness) < 2 && uint(poseSpace) < 2, return false);
    if (m_poseUsageDirty) {
        std::fill_n(&m_poseInUse[0][0], 4, false);
        for (const auto *controller : std::as_const(m_controllers)) {
            m_poseInUse[uint(controller->controller())][uint(controller->poseSpace())] = true;
        }
        m_poseUsageDirty = false;
    }
    return m_poseInUse[uint(handedness)][uint(poseSpace)];
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 952, as _ZNK29QQuick3DXrInputManagerPrivate13leftHandInputEv
inline QQuick3DXrHandInput *QQuick3DXrInputManagerPrivate::leftHandInput() const
{
    return m_handInputState[uint(Handedness::Left)];
}

//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 957, as _ZNK29QQuick3DXrInputManagerPrivate14rightHandInputEv
inline QQuick3DXrHandInput *QQuick3DXrInputManagerPrivate::rightHandInput() const
{
    return m_handInputState[uint(Handedness::Right)];
}
#if !defined(Q_OS_VISIONOS)
//  from ../qtquick3d/src/xr/quick3dxr/openxr/qopenxrinputmanager.cpp, line 918, as _ZN29QQuick3DXrInputManagerPrivate9handSpaceEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceE
inline XrSpace QQuick3DXrInputManagerPrivate::handSpace(QQuick3DXrInputManagerPrivate::Handedness handedness, HandPoseSpace poseSpace)
{
    if (poseSpace == HandPoseSpace::GripPose)
        return m_handGripSpace[uint(handedness)];
    else
        return m_handAimSpace[uint(handedness)];
}
#endif  // !defined(Q_OS_VISIONOS)
//  -----------------------------------------------------------------------

//  QQuick3DXrInputManager *QQuick3DXrInputManagerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuick3DXrInputManager *ritual_ZN29QQuick3DXrInputManagerPrivate6q_funcEv(
    QQuick3DXrInputManagerPrivate *self) {
  return self->q_func();
}

//  const QQuick3DXrInputManager *QQuick3DXrInputManagerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuick3DXrInputManager *ritual_ZNK29QQuick3DXrInputManagerPrivate6q_funcEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->q_func();
}

//  bool QQuick3DXrInputManagerPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QQuick3DXrInputManagerPrivate7isValidEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->isValid();
}

//  QQuick3DXrInputManagerPrivate
//      *QQuick3DXrInputManagerPrivate::get(QQuick3DXrInputManager
//      *inputManager)
extern "C" Q_DECL_EXPORT
QQuick3DXrInputManagerPrivate *ritual_ZN29QQuick3DXrInputManagerPrivate3getEP22QQuick3DXrInputManager(
    QQuick3DXrInputManager *inputManager) {
  return QQuick3DXrInputManagerPrivate::get(inputManager);
}

//  void QQuick3DXrInputManagerPrivate::setPosePositionAndRotation(Handedness
//      handedness, HandPoseSpace poseSpace, const QVector3D &position, const
//      QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DXrInputManagerPrivate26setPosePositionAndRotationEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceERK9QVector3DRK11QQuaternion(
    QQuick3DXrInputManagerPrivate *self,
    QQuick3DXrInputManagerPrivate::Handedness handedness,
    QQuick3DXrInputManagerPrivate::HandPoseSpace poseSpace,
    const QVector3D *position,
    const QQuaternion *rotation) {
  self->setPosePositionAndRotation(
      handedness,
      poseSpace,
      *position,
      *rotation);
}

//  void
//      QQuick3DXrInputManagerPrivate::registerController(QQuick3DXrControlle
//      r *controller)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DXrInputManagerPrivate18registerControllerEP20QQuick3DXrController(
    QQuick3DXrInputManagerPrivate *self,
    QQuick3DXrController *controller) {
  self->registerController(controller);
}

//  void
//      QQuick3DXrInputManagerPrivate::unregisterController(QQuick3DXrControl
//      ler *controller)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DXrInputManagerPrivate20unregisterControllerEP20QQuick3DXrController(
    QQuick3DXrInputManagerPrivate *self,
    QQuick3DXrController *controller) {
  self->unregisterController(controller);
}

//  bool QQuick3DXrInputManagerPrivate::isPoseInUse(Handedness handedness,
//      HandPoseSpace poseSpace)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QQuick3DXrInputManagerPrivate11isPoseInUseEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceE(
    QQuick3DXrInputManagerPrivate *self,
    QQuick3DXrInputManagerPrivate::Handedness handedness,
    QQuick3DXrInputManagerPrivate::HandPoseSpace poseSpace) {
  return self->isPoseInUse(handedness, poseSpace);
}

//  QQuick3DXrHandInput *QQuick3DXrInputManagerPrivate::leftHandInput() const
extern "C" Q_DECL_EXPORT
QQuick3DXrHandInput *ritual_ZNK29QQuick3DXrInputManagerPrivate13leftHandInputEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->leftHandInput();
}

//  QQuick3DXrHandInput *QQuick3DXrInputManagerPrivate::rightHandInput()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DXrHandInput *ritual_ZNK29QQuick3DXrInputManagerPrivate14rightHandInputEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->rightHandInput();
}

#if !defined(Q_OS_VISIONOS)
//  const QMetaObject *QQuick3DXrInputManagerPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuick3DXrInputManagerPrivate10metaObjectEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->metaObject();
}

//  XrSpace QQuick3DXrInputManagerPrivate::handSpace(Handedness handedness,
//      HandPoseSpace poseSpace)
extern "C" Q_DECL_EXPORT
XrSpace ritual_ZN29QQuick3DXrInputManagerPrivate9handSpaceEN11QtQuick3DXr10HandednessENS0_13HandPoseSpaceE(
    QQuick3DXrInputManagerPrivate *self,
    QQuick3DXrInputManagerPrivate::Handedness handedness,
    QQuick3DXrInputManagerPrivate::HandPoseSpace poseSpace) {
  return self->handSpace(handedness, poseSpace);
}

//  qsizetype QQuick3DXrInputManagerPrivate::getPokeJointIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK29QQuick3DXrInputManagerPrivate17getPokeJointIndexEv(
    const QQuick3DXrInputManagerPrivate *self) {
  return self->getPokeJointIndex();
}
#endif  // !defined(Q_OS_VISIONOS)

#endif  // defined(Q_OS_VISIONOS) || OpenXR
