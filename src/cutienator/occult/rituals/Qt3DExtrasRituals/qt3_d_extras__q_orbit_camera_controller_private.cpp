//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qorbitcameracontroller_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qorbitcameracontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qabstractcameracontroller.h>
#include <Qt3DExtras/private/qabstractcameracontroller_p.h>
#include <Qt3DRender/QCamera>
#include <Qt3DInput/QAxis>
#include <Qt3DInput/QAnalogAxisInput>
#include <Qt3DInput/QButtonAxisInput>
#include <Qt3DInput/QAction>
#include <Qt3DInput/QActionInput>
#include <Qt3DInput/QLogicalDevice>
#include <Qt3DInput/QKeyboardDevice>
#include <Qt3DInput/QMouseDevice>
#include <Qt3DInput/QMouseEvent>
#include <Qt3DLogic/QFrameAction>
#include <QtCore/QtGlobal>
#include <Qt3DExtras/qorbitcameracontroller.h>
#include <Qt3DExtras/private/qorbitcameracontroller_p.h>
#include <Qt3DRender/QCamera>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qabstractcameracontroller.cpp, line 24, as _ZN10Qt3DExtras32QAbstractCameraControllerPrivateC2Ev
namespace Qt3DExtras {
inline QAbstractCameraControllerPrivate::QAbstractCameraControllerPrivate()
    : Qt3DCore::QEntityPrivate()
    , m_camera(nullptr)
    , m_leftMouseButtonAction(new Qt3DInput::QAction())
    , m_middleMouseButtonAction(new Qt3DInput::QAction())
    , m_rightMouseButtonAction(new Qt3DInput::QAction())
    , m_altButtonAction(new Qt3DInput::QAction())
    , m_shiftButtonAction(new Qt3DInput::QAction())
    , m_escapeButtonAction(new Qt3DInput::QAction())
    , m_rxAxis(new Qt3DInput::QAxis())
    , m_ryAxis(new Qt3DInput::QAxis())
    , m_txAxis(new Qt3DInput::QAxis())
    , m_tyAxis(new Qt3DInput::QAxis())
    , m_tzAxis(new Qt3DInput::QAxis())
    , m_leftMouseButtonInput(new Qt3DInput::QActionInput())
    , m_middleMouseButtonInput(new Qt3DInput::QActionInput())
    , m_rightMouseButtonInput(new Qt3DInput::QActionInput())
    , m_altButtonInput(new Qt3DInput::QActionInput())
    , m_shiftButtonInput(new Qt3DInput::QActionInput())
    , m_escapeButtonInput(new Qt3DInput::QActionInput())
    , m_mouseRxInput(new Qt3DInput::QAnalogAxisInput())
    , m_mouseRyInput(new Qt3DInput::QAnalogAxisInput())
    , m_mouseTzXInput(new Qt3DInput::QAnalogAxisInput())
    , m_mouseTzYInput(new Qt3DInput::QAnalogAxisInput())
    , m_keyboardTxPosInput(new Qt3DInput::QButtonAxisInput())
    , m_keyboardTyPosInput(new Qt3DInput::QButtonAxisInput())
    , m_keyboardTzPosInput(new Qt3DInput::QButtonAxisInput())
    , m_keyboardTxNegInput(new Qt3DInput::QButtonAxisInput())
    , m_keyboardTyNegInput(new Qt3DInput::QButtonAxisInput())
    , m_keyboardTzNegInput(new Qt3DInput::QButtonAxisInput())
    , m_keyboardDevice(new Qt3DInput::QKeyboardDevice())
    , m_mouseDevice(new Qt3DInput::QMouseDevice())
    , m_logicalDevice(new Qt3DInput::QLogicalDevice())
    , m_frameAction(new Qt3DLogic::QFrameAction())
    , m_linearSpeed(10.0f)
    , m_lookSpeed(180.0f)
    , m_acceleration(-1.0f)
    , m_deceleration(-1.0f)
    , m_sceneUp(0.0f, 1.0f, 0.0f)
{}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qorbitcameracontroller.cpp, line 13, as _ZN10Qt3DExtras29QOrbitCameraControllerPrivateC1Ev
namespace Qt3DExtras {
inline QOrbitCameraControllerPrivate::QOrbitCameraControllerPrivate()
    : m_zoomInLimit(2.0f)
    , m_upVector(0.0f, 1.0f, 0.0f)
    , m_inverseXTranslate(false)
    , m_inverseYTranslate(false)
    , m_inversePan(false)
    , m_inverseTilt(false)
    , m_zoomTranslateViewCenter(true)
{}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  QOrbitCameraController
//      *Qt3DExtras::QOrbitCameraControllerPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QOrbitCameraController *ritual_ZN10Qt3DExtras29QOrbitCameraControllerPrivate6q_funcEv(
    Qt3DExtras::QOrbitCameraControllerPrivate *self) {
  return self->q_func();
}

//  const QOrbitCameraController
//      *Qt3DExtras::QOrbitCameraControllerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QOrbitCameraController *ritual_ZNK10Qt3DExtras29QOrbitCameraControllerPrivate6q_funcEv(
    const Qt3DExtras::QOrbitCameraControllerPrivate *self) {
  return self->q_func();
}

//  Qt3DExtras::QOrbitCameraControllerPrivate::QOrbitCameraControllerPrivate(
//      )
extern "C" Q_DECL_EXPORT
Qt3DExtras::QOrbitCameraControllerPrivate *ritual_ZN10Qt3DExtras29QOrbitCameraControllerPrivateC1Ev() {
  return new Qt3DExtras::QOrbitCameraControllerPrivate();
}
