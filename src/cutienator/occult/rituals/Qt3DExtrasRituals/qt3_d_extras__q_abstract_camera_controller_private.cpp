//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qabstractcameracontroller_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qabstractcameracontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qabstractcameracontroller.cpp, line 24, as _ZN10Qt3DExtras32QAbstractCameraControllerPrivateC1Ev
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

//  from ../qt3d/src/extras/defaults/qabstractcameracontroller.cpp, line 65, as _ZN10Qt3DExtras32QAbstractCameraControllerPrivate4initEv
namespace Qt3DExtras {
inline void QAbstractCameraControllerPrivate::init()
{
    //// Actions

    // Left Mouse Button Action
    m_leftMouseButtonInput->setButtons(QList<int> { Qt::LeftButton });
    m_leftMouseButtonInput->setSourceDevice(m_mouseDevice);
    m_leftMouseButtonAction->addInput(m_leftMouseButtonInput);

    // Middle Mouse Button Action
    m_middleMouseButtonInput->setButtons(QList<int> { Qt::MiddleButton });
    m_middleMouseButtonInput->setSourceDevice(m_mouseDevice);
    m_middleMouseButtonAction->addInput(m_middleMouseButtonInput);

    // Right Mouse Button Action
    m_rightMouseButtonInput->setButtons(QList<int> { Qt::RightButton });
    m_rightMouseButtonInput->setSourceDevice(m_mouseDevice);
    m_rightMouseButtonAction->addInput(m_rightMouseButtonInput);

    // Alt Button Action
    m_altButtonInput->setButtons(QList<int> { Qt::Key_Alt });
    m_altButtonInput->setSourceDevice(m_keyboardDevice);
    m_altButtonAction->addInput(m_altButtonInput);

    // Shift Button Action
    m_shiftButtonInput->setButtons(QList<int> { Qt::Key_Shift });
    m_shiftButtonInput->setSourceDevice(m_keyboardDevice);
    m_shiftButtonAction->addInput(m_shiftButtonInput);

    // Escape Button Action
    m_escapeButtonInput->setButtons(QList<int> { Qt::Key_Escape });
    m_escapeButtonInput->setSourceDevice(m_keyboardDevice);
    m_escapeButtonAction->addInput(m_escapeButtonInput);

    //// Axes

    // Mouse X
    m_mouseRxInput->setAxis(Qt3DInput::QMouseDevice::X);
    m_mouseRxInput->setSourceDevice(m_mouseDevice);
    m_rxAxis->addInput(m_mouseRxInput);

    // Mouse Y
    m_mouseRyInput->setAxis(Qt3DInput::QMouseDevice::Y);
    m_mouseRyInput->setSourceDevice(m_mouseDevice);
    m_ryAxis->addInput(m_mouseRyInput);

    // Mouse Wheel X
    m_mouseTzXInput->setAxis(Qt3DInput::QMouseDevice::WheelX);
    m_mouseTzXInput->setSourceDevice(m_mouseDevice);
    m_tzAxis->addInput(m_mouseTzXInput);

    // Mouse Wheel Y
    m_mouseTzYInput->setAxis(Qt3DInput::QMouseDevice::WheelY);
    m_mouseTzYInput->setSourceDevice(m_mouseDevice);
    m_tzAxis->addInput(m_mouseTzYInput);

    // Keyboard Pos Tx
    m_keyboardTxPosInput->setButtons(QList<int> { Qt::Key_Right });
    m_keyboardTxPosInput->setScale(1.0f);
    m_keyboardTxPosInput->setSourceDevice(m_keyboardDevice);
    m_txAxis->addInput(m_keyboardTxPosInput);

    // Keyboard Pos Tz
    m_keyboardTzPosInput->setButtons(QList<int> { Qt::Key_PageUp });
    m_keyboardTzPosInput->setScale(1.0f);
    m_keyboardTzPosInput->setSourceDevice(m_keyboardDevice);
    m_tzAxis->addInput(m_keyboardTzPosInput);

    // Keyboard Pos Ty
    m_keyboardTyPosInput->setButtons(QList<int> { Qt::Key_Up });
    m_keyboardTyPosInput->setScale(1.0f);
    m_keyboardTyPosInput->setSourceDevice(m_keyboardDevice);
    m_tyAxis->addInput(m_keyboardTyPosInput);

    // Keyboard Neg Tx
    m_keyboardTxNegInput->setButtons(QList<int> { Qt::Key_Left });
    m_keyboardTxNegInput->setScale(-1.0f);
    m_keyboardTxNegInput->setSourceDevice(m_keyboardDevice);
    m_txAxis->addInput(m_keyboardTxNegInput);

    // Keyboard Neg Tz
    m_keyboardTzNegInput->setButtons(QList<int> { Qt::Key_PageDown });
    m_keyboardTzNegInput->setScale(-1.0f);
    m_keyboardTzNegInput->setSourceDevice(m_keyboardDevice);
    m_tzAxis->addInput(m_keyboardTzNegInput);

    // Keyboard Neg Ty
    m_keyboardTyNegInput->setButtons(QList<int> { Qt::Key_Down });
    m_keyboardTyNegInput->setScale(-1.0f);
    m_keyboardTyNegInput->setSourceDevice(m_keyboardDevice);
    m_tyAxis->addInput(m_keyboardTyNegInput);

    //// Logical Device

    m_logicalDevice->addAction(m_leftMouseButtonAction);
    m_logicalDevice->addAction(m_middleMouseButtonAction);
    m_logicalDevice->addAction(m_rightMouseButtonAction);
    m_logicalDevice->addAction(m_altButtonAction);
    m_logicalDevice->addAction(m_shiftButtonAction);
    m_logicalDevice->addAction(m_escapeButtonAction);
    m_logicalDevice->addAxis(m_rxAxis);
    m_logicalDevice->addAxis(m_ryAxis);
    m_logicalDevice->addAxis(m_txAxis);
    m_logicalDevice->addAxis(m_tyAxis);
    m_logicalDevice->addAxis(m_tzAxis);

    applyInputAccelerations();

    Q_Q(QAbstractCameraController);
    //// FrameAction

    // Disable the logical device when the entity is disabled
    QObject::connect(q, &Qt3DCore::QEntity::enabledChanged,
                     m_logicalDevice, &Qt3DInput::QLogicalDevice::setEnabled);
    QObject::connect(q, &Qt3DCore::QEntity::enabledChanged,
                     m_frameAction, &Qt3DLogic::QFrameAction::setEnabled);
    for (auto axis: {m_rxAxis, m_ryAxis, m_txAxis, m_tyAxis, m_tzAxis}) {
        QObject::connect(q, &Qt3DCore::QEntity::enabledChanged,
                         axis, &Qt3DInput::QAxis::setEnabled);
    }

    QObject::connect(m_escapeButtonAction, &Qt3DInput::QAction::activeChanged,
                     q, [this](bool isActive) {
                         if (isActive && m_camera)
                             m_camera->viewAll();
                     });

    q->addComponent(m_frameAction);
    q->addComponent(m_logicalDevice);
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qabstractcameracontroller.cpp, line 196, as _ZN10Qt3DExtras32QAbstractCameraControllerPrivate23applyInputAccelerationsEv
namespace Qt3DExtras {
inline void QAbstractCameraControllerPrivate::applyInputAccelerations()
{
    const auto inputs = {
        m_keyboardTxPosInput,
        m_keyboardTyPosInput,
        m_keyboardTzPosInput,
        m_keyboardTxNegInput,
        m_keyboardTyNegInput,
        m_keyboardTzNegInput
    };

    for (auto input : inputs) {
        input->setAcceleration(m_acceleration);
        input->setDeceleration(m_deceleration);
    }
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QAbstractCameraControllerPrivate that Python can take functions over in. Every Qt3DExtras::QAbstractCameraControllerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QAbstractCameraControllerPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QAbstractCameraControllerPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QAbstractCameraControllerPrivate : public Qt3DExtras::QAbstractCameraControllerPrivate {
public:
  using Qt3DExtras::QAbstractCameraControllerPrivate::QAbstractCameraControllerPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractCameraControllerPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QAbstractCameraControllerPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QAbstractCameraControllerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QAbstractCameraControllerPrivate::QAbstractCameraControllerPr
//      ivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QAbstractCameraControllerPrivate *ritual_ZN10Qt3DExtras32QAbstractCameraControllerPrivateC1Ev() {
  return new CuteQt3DExtras_QAbstractCameraControllerPrivate();
}

//  void Qt3DExtras::QAbstractCameraControllerPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QAbstractCameraControllerPrivate4initEv(
    Qt3DExtras::QAbstractCameraControllerPrivate *self) {
  self->init();
}

//  void
//      Qt3DExtras::QAbstractCameraControllerPrivate::applyInputAccelerations
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras32QAbstractCameraControllerPrivate23applyInputAccelerationsEv(
    Qt3DExtras::QAbstractCameraControllerPrivate *self) {
  self->applyInputAccelerations();
}

//  QAbstractCameraController
//      *Qt3DExtras::QAbstractCameraControllerPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QAbstractCameraController *ritual_ZN10Qt3DExtras32QAbstractCameraControllerPrivate6q_funcEv(
    Qt3DExtras::QAbstractCameraControllerPrivate *self) {
  return self->q_func();
}

//  const QAbstractCameraController
//      *Qt3DExtras::QAbstractCameraControllerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QAbstractCameraController *ritual_ZNK10Qt3DExtras32QAbstractCameraControllerPrivate6q_funcEv(
    const Qt3DExtras::QAbstractCameraControllerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QAbstractCameraControllerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QAbstractCameraControllerPrivate(
    Qt3DExtras::QAbstractCameraControllerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QAbstractCameraControllerPrivate *>(self)->take(key, call);
}
