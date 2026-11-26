//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qinputaspect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DCore/private/qscene_p.h>
#include <Qt3DInput/qmousehandler.h>
#include <Qt3DInput/qkeyboardhandler.h>
#include <Qt3DInput/private/assignkeyboardfocusjob_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputsettings_p.h>
#include <Qt3DInput/private/qinputdeviceintegration_p.h>
#include <Qt3DInput/private/qmousehandler_p.h>
#include <Qt3DInput/private/qkeyboardhandler_p.h>
#include <Qt3DCore/private/qeventfilterservice_p.h>
#include <Qt3DInput/private/keyboardmousegenericdeviceintegration_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qmousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 25, as local:inputhandler.cpp:InternalEventFilter
namespace Qt3DInput::Input {
using namespace Qt3DCore;
class InternalEventFilter : public QObject
{
public:
    explicit InternalEventFilter(QObject *parent = nullptr) : QObject(parent), m_inputHandler(nullptr) { }
    ~InternalEventFilter() override;

    void setInputHandler(Qt3DInput::Input::InputHandler *handler) { m_inputHandler = handler; }
    inline Qt3DInput::Input::InputHandler *inputHandler() const { return m_inputHandler; }

protected:
    bool eventFilter(QObject *obj, QEvent *e) override {
        switch (e->type()) {
        case QEvent::MouseMove:
        case QEvent::MouseButtonPress:
        case QEvent::MouseButtonRelease:
        case QEvent::MouseButtonDblClick:
            return processMouseEvent(obj, static_cast<QT_PREPEND_NAMESPACE(QMouseEvent) *>(e));
        case QEvent::HoverMove: {
            const QHoverEvent *he = static_cast<QHoverEvent *>(e);
            auto mouseEvent = QT_PREPEND_NAMESPACE(QMouseEvent)(QEvent::MouseMove,
                                                                he->position(),
                                                                he->globalPosition(),
                                                                Qt::NoButton, Qt::NoButton,
                                                                he->modifiers());
            return processMouseEvent(obj, static_cast<QT_PREPEND_NAMESPACE(QMouseEvent) *>(&mouseEvent));
        }
#if QT_CONFIG(wheelevent)
        case QEvent::Wheel:
            return processWheelEvent(obj, static_cast<QT_PREPEND_NAMESPACE(QWheelEvent) *>(e));
#endif
        case QEvent::KeyPress:
        case QEvent::KeyRelease:
            return processKeyEvent(obj, static_cast<QT_PREPEND_NAMESPACE(QKeyEvent) *>(e));
        default:
            break;
        }
        return false;
    }

    bool processMouseEvent(QObject *obj, QT_PREPEND_NAMESPACE(QMouseEvent) *event);
#if QT_CONFIG(wheelevent)
    bool processWheelEvent(QObject *obj, QT_PREPEND_NAMESPACE(QWheelEvent) *event);
#endif
    bool processKeyEvent(QObject *obj, QT_PREPEND_NAMESPACE(QKeyEvent) *event);

private:
    Qt3DInput::Input::InputHandler *m_inputHandler;
};
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 243, as local:inputhandler.cpp:InternalEventFilter::processMouseEvent
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline bool InternalEventFilter::processMouseEvent(QObject *obj, QT_PREPEND_NAMESPACE(QMouseEvent) *event)
{
    Q_UNUSED(obj);
    Q_ASSERT(m_inputHandler);
    if (!m_inputHandler->m_scene)
        return false;

    for (const HMouseDevice &cHandle : std::as_const(m_inputHandler->m_activeMouseDevices)) {
        MouseDevice *controller = m_inputHandler->m_mouseDeviceManager->data(cHandle);

        controller->updateMouseEvent(event);

        // Send the events to the mouse handlers that have for sourceDevice controller
        const std::vector<HMouseHandler> &activeMouseHandlers = m_inputHandler->m_mouseInputManager->activeHandles();
        for (const HMouseHandler &mouseHandlerHandle : activeMouseHandlers) {
            MouseHandler *mouseHandler = m_inputHandler->m_mouseInputManager->data(mouseHandlerHandle);
            Q_ASSERT(mouseHandler);

            if (mouseHandler->mouseDevice() == controller->peerId()) {
                QMouseHandler *node = qobject_cast<QMouseHandler *>(m_inputHandler->m_scene->lookupNode(mouseHandler->peerId()));
                if (node) {
                    QMouseHandlerPrivate *dnode = static_cast<QMouseHandlerPrivate *>(QMouseHandlerPrivate::get(node));
                    dnode->mouseEvent(QMouseEventPtr::create(*event));  // Do we really need Qt3D specific events?
                }
            }
        }
    }

    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 275, as local:inputhandler.cpp:InternalEventFilter::processWheelEvent
#if QT_CONFIG(wheelevent)
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline bool InternalEventFilter::processWheelEvent(QObject *obj, QT_PREPEND_NAMESPACE(QWheelEvent) *event)
{
    Q_UNUSED(obj);
    Q_ASSERT(m_inputHandler);
    if (!m_inputHandler->m_scene)
        return false;

    for (const HMouseDevice &cHandle : std::as_const(m_inputHandler->m_activeMouseDevices)) {
        MouseDevice *controller = m_inputHandler->m_mouseDeviceManager->data(cHandle);

        controller->updateWheelEvent(event);

        // Send the events to the mouse handlers that have for sourceDevice controller
        const std::vector<HMouseHandler> &activeMouseHandlers = m_inputHandler->m_mouseInputManager->activeHandles();
        for (const HMouseHandler &mouseHandlerHandle : activeMouseHandlers) {
            MouseHandler *mouseHandler = m_inputHandler->m_mouseInputManager->data(mouseHandlerHandle);
            Q_ASSERT(mouseHandler);

            if (mouseHandler->mouseDevice() == controller->peerId()) {
                QMouseHandler *node = qobject_cast<QMouseHandler *>(m_inputHandler->m_scene->lookupNode(mouseHandler->peerId()));
                QWheelEvent we(*event);
                node->wheel(&we);  // Do we really need Qt3D specific events?
            }
        }
    }

    return false;
}
}  // namespace Qt3DInput::Input
#endif  // QT_CONFIG(wheelevent)

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 305, as local:inputhandler.cpp:InternalEventFilter::processKeyEvent
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline bool InternalEventFilter::processKeyEvent(QObject *obj, QT_PREPEND_NAMESPACE(QKeyEvent) *event)
{
    Q_UNUSED(obj);
    Q_ASSERT(m_inputHandler);
    if (!m_inputHandler->m_scene)
        return false;

    for (const HKeyboardDevice &cHandle : std::as_const(m_inputHandler->m_activeKeyboardDevices)) {
        KeyboardDevice *keyboardDevice = m_inputHandler->m_keyboardDeviceManager->data(cHandle);
        if (keyboardDevice) {
            keyboardDevice->updateKeyEvent(event);

            // update the focus
            if (keyboardDevice->lastKeyboardInputRequester() != keyboardDevice->currentFocusItem()) {
                const auto handles = m_inputHandler->keyboardInputManager()->activeHandles();
                for (const HKeyboardHandler &handle : handles) {
                    KeyboardHandler *input = m_inputHandler->keyboardInputManager()->data(handle);
                    Q_ASSERT(input);
                    if (input->keyboardDevice() == keyboardDevice->peerId()) {
                        bool hasFocus = input->peerId() == keyboardDevice->lastKeyboardInputRequester();
                        input->setFocus(hasFocus);
                        QKeyboardHandler *node = qobject_cast<QKeyboardHandler *>(m_inputHandler->m_scene->lookupNode(input->peerId()));
                        if (node) {
                            const bool b = node->blockNotifications(true);
                            node->setFocus(hasFocus);
                            node->blockNotifications(b);
                        }
                        if (hasFocus)
                            keyboardDevice->setCurrentFocusItem(input->peerId());
                    }
                }
            }

            // deliver the event
            QKeyboardHandler *node = qobject_cast<QKeyboardHandler *>(m_inputHandler->m_scene->lookupNode(keyboardDevice->currentFocusItem()));
            if (node) {
                QKeyboardHandlerPrivate *dnode = static_cast<QKeyboardHandlerPrivate *>(QKeyboardHandlerPrivate::get(node));

                QKeyEvent ke(*event);
                dnode->keyEvent(&ke);  // Do we really need Qt3D specific events?
            }
        }
    }

    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 100, as _ZN9Qt3DInput5Input12InputHandlerD1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline InputHandler::~InputHandler()
{
    delete m_keyboardDeviceManager;
    delete m_keyboardInputManager;
    delete m_mouseDeviceManager;
    delete m_mouseInputManager;
    delete m_eventFilter;
    delete m_axisManager;
    delete m_axisAccumulatorManager;
    delete m_actionManager;
    delete m_axisSettingManager;
    delete m_analogAxisInputManager;
    delete m_buttonAxisInputManager;
    delete m_actionInputManager;
    delete m_inputChordManager;
    delete m_inputSequenceManager;
    delete m_logicalDeviceManager;
    delete m_genericPhysicalDeviceBackendNodeManager;
    delete m_physicalDeviceProxyManager;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboardmousegenericdeviceintegration.cpp, line 15, as _ZN9Qt3DInput5Input37KeyboardMouseGenericDeviceIntegrationC1EPNS0_12InputHandlerE
namespace Qt3DInput::Input {
inline KeyboardMouseGenericDeviceIntegration::KeyboardMouseGenericDeviceIntegration(InputHandler *handler)
    : Qt3DInput::QInputDeviceIntegration()
    , m_handler(handler)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 211, as _ZN9Qt3DInput5Input12InputHandler25addInputDeviceIntegrationEPNS_23QInputDeviceIntegrationE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::addInputDeviceIntegration(QInputDeviceIntegration *inputIntegration)
{
    m_inputDeviceIntegrations.push_back(inputIntegration);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 28, as _ZN9Qt3DInput5Input11MouseDeviceD1Ev
namespace Qt3DInput::Input {
inline MouseDevice::~MouseDevice()
{
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  A Qt3DInput::QInputAspectPrivate that Python can take functions over in. Every Qt3DInput::QInputAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QInputAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DInput_QInputAspectPrivateCall3)(const void *, int *);
class CuteQt3DInput_QInputAspectPrivate : public Qt3DInput::QInputAspectPrivate {
public:
  using Qt3DInput::QInputAspectPrivate::QInputAspectPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::frameDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectPrivateCall2 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectPrivateCall3 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  QInputAspect *Qt3DInput::QInputAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputAspect *ritual_ZN9Qt3DInput19QInputAspectPrivate6q_funcEv(
    Qt3DInput::QInputAspectPrivate *self) {
  return self->q_func();
}

//  const QInputAspect *Qt3DInput::QInputAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputAspect *ritual_ZNK9Qt3DInput19QInputAspectPrivate6q_funcEv(
    const Qt3DInput::QInputAspectPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DInput_QInputAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputAspectPrivate(
    Qt3DInput::QInputAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputAspectPrivate *>(self)->take(key, call);
}
