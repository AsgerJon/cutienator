//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputhandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qmousedevice_p.h>
#include <Qt3DInput/private/mousehandler_p.h>
#include <Qt3DInput/qmousehandler.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/mousedevice_p.h>
#include <Qt3DInput/private/qmousehandler_p.h>
#include <Qt3DInput/private/genericdevicebackendnode_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qgenericinputdevice_p.h>
#include <Qt3DInput/private/qabstractphysicaldevice_p.h>
#include <Qt3DInput/private/inputchord_p.h>
#include <Qt3DInput/qinputchord.h>
#include <Qt3DInput/private/qinputchord_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/actioninput_p.h>
#include <Qt3DInput/qactioninput.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/qactioninput_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/utils_p.h>
#include <Qt3DInput/private/axissetting_p.h>
#include <Qt3DInput/qaxissetting.h>
#include <Qt3DInput/private/qaxissetting_p.h>
#include <Qt3DInput/private/inputsequence_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/qinputsequence.h>
#include <QtCore/QDateTime>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qinputsequence_p.h>
#include <Qt3DInput/private/logicaldevice_p.h>
#include <Qt3DInput/qaction.h>
#include <Qt3DInput/qaxis.h>
#include <Qt3DInput/qlogicaldevice.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qlogicaldevice_p.h>
#include <Qt3DInput/private/keyboarddevice_p.h>
#include <Qt3DInput/QKeyEvent>
#include <Qt3DCore/qnode.h>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/buttonaxisinput_p.h>
#include <Qt3DInput/qbuttonaxisinput.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/private/qabstractphysicaldevicebackendnode_p.h>
#include <Qt3DInput/private/qbuttonaxisinput_p.h>
#include <Qt3DInput/private/utils_p.h>
#include <Qt3DInput/private/physicaldeviceproxy_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <QtCore/QCoreApplication>
#include <Qt3DInput/private/inputmanagers_p.h>
#include <Qt3DInput/private/qabstractphysicaldeviceproxy_p.h>
#include <Qt3DInput/private/qabstractphysicaldeviceproxy_p_p.h>
#include <Qt3DInput/private/axis_p.h>
#include <Qt3DInput/qaxis.h>
#include <Qt3DInput/qabstractaxisinput.h>
#include <Qt3DInput/private/qaxis_p.h>
#include <algorithm>
#include <Qt3DInput/private/action_p.h>
#include <Qt3DInput/qaction.h>
#include <Qt3DInput/qabstractactioninput.h>
#include <Qt3DInput/private/qaction_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 71, as local:buttonaxisinput.cpp:anyOfRequiredButtonsPressed
namespace Qt3DInput::Input {
namespace {
inline bool anyOfRequiredButtonsPressed(const QList<int> &buttons, QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend)
{
    bool validButtonWasPressed = false;
    for (int button : buttons) {
        if (physicalDeviceBackend->isButtonPressed(button)) {
            validButtonWasPressed = true;
            break;
        }
    }
    return validButtonWasPressed;
}
}  // namespace
}  // namespace Qt3DInput::Input

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

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 20, as local:keyboarddevice.cpp:getKeyPosition
namespace Qt3DInput::Input {
namespace {
inline QPair<int, int> getKeyPosition(int key)
{
    QPair<int, int> position;

    switch (key) {
    case Qt::Key_Escape:
        return QPair<int, int>(0, 0);
    case Qt::Key_Tab:
        return QPair<int, int>(0, 1);
    case Qt::Key_Backtab:
        return QPair<int, int>(0, 2);
    case Qt::Key_Backspace:
        return QPair<int, int>(0, 3);
    case Qt::Key_Return:
        return QPair<int, int>(0, 4);
    case Qt::Key_Enter:
        return QPair<int, int>(0, 5);
    case Qt::Key_Insert:
        return QPair<int, int>(0, 6);
    case Qt::Key_Delete:
        return QPair<int, int>(0, 7);
    case Qt::Key_Pause:
        return QPair<int, int>(0, 8);
    case Qt::Key_Print:
        return QPair<int, int>(0, 9);
    case Qt::Key_SysReq:
        return QPair<int, int>(0, 10);
    case Qt::Key_Clear:
        return QPair<int, int>(0, 11);
    case Qt::Key_Home:
        return QPair<int, int>(0, 12);
    case Qt::Key_End:
        return QPair<int, int>(0, 13);
    case Qt::Key_Left:
        return QPair<int, int>(0, 14);
    case Qt::Key_Right:
        return QPair<int, int>(0, 16);
    case Qt::Key_Up:
        return QPair<int, int>(0, 15);
    case Qt::Key_Down:
        return QPair<int, int>(0, 17);
    case Qt::Key_PageUp:
        return QPair<int, int>(0, 18);
    case Qt::Key_PageDown:
        return QPair<int, int>(0, 19);
    case Qt::Key_Shift:
        return QPair<int, int>(0, 20);
    case Qt::Key_Alt:
        return QPair<int, int>(0, 23);
    case Qt::Key_Control:
        return QPair<int, int>(0, 21);
    case Qt::Key_Meta:
        return QPair<int, int>(0, 22);
    case Qt::Key_CapsLock:
        return QPair<int, int>(0, 24);
    case Qt::Key_NumLock:
        return QPair<int, int>(0, 25);
    case Qt::Key_ScrollLock:
        return QPair<int, int>(0, 26);
    case Qt::Key_F1:
        return QPair<int, int>(0, 27);
    case Qt::Key_F2:
        return QPair<int, int>(0, 28);
    case Qt::Key_F3:
        return QPair<int, int>(0, 29);
    case Qt::Key_F4:
        return QPair<int, int>(0, 30);
    case Qt::Key_F5:
        return QPair<int, int>(0, 31);
    case Qt::Key_F6:
        return QPair<int, int>(1, 0);
    case Qt::Key_F7:
        return QPair<int, int>(1, 1);
    case Qt::Key_F8:
        return QPair<int, int>(1, 2);
    case Qt::Key_F9:
        return QPair<int, int>(1, 3);
    case Qt::Key_F10:
        return QPair<int, int>(1, 4);
    case Qt::Key_F11:
        return QPair<int, int>(1, 5);
    case Qt::Key_F12:
        return QPair<int, int>(1, 6);
    case Qt::Key_F13:
        return QPair<int, int>(1, 7);
    case Qt::Key_F14:
        return QPair<int, int>(1, 8);
    case Qt::Key_F15:
        return QPair<int, int>(1, 9);
    case Qt::Key_F16:
        return QPair<int, int>(1, 10);
    case Qt::Key_F17:
        return QPair<int, int>(1, 11);
    case Qt::Key_F18:
        return QPair<int, int>(1, 12);
    case Qt::Key_F19:
        return QPair<int, int>(1, 13);
    case Qt::Key_F20:
        return QPair<int, int>(1, 14);
    case Qt::Key_F21:
        return QPair<int, int>(1, 15);
    case Qt::Key_F22:
        return QPair<int, int>(1, 16);
    case Qt::Key_F23:
        return QPair<int, int>(1, 17);
    case Qt::Key_F24:
        return QPair<int, int>(1, 18);
    case Qt::Key_F25:
        return QPair<int, int>(1, 19);
    case Qt::Key_F26:
        return QPair<int, int>(1, 20);
    case Qt::Key_F27:
        return QPair<int, int>(1, 21);
    case Qt::Key_F28:
        return QPair<int, int>(1, 22);
    case Qt::Key_F29:
        return QPair<int, int>(1, 23);
    case Qt::Key_F30:
        return QPair<int, int>(1, 24);
    case Qt::Key_F31:
        return QPair<int, int>(1, 25);
    case Qt::Key_F32:
        return QPair<int, int>(1, 26);
    case Qt::Key_F33:
        return QPair<int, int>(1, 27);
    case Qt::Key_F34:
        return QPair<int, int>(1, 28);
    case Qt::Key_F35:
        return QPair<int, int>(1, 29);
    case Qt::Key_Super_L:
        return QPair<int, int>(1, 30);
    case Qt::Key_Super_R:
        return QPair<int, int>(1, 31);
    case Qt::Key_Menu:
        return QPair<int, int>(2, 1);
    case Qt::Key_Help:
        return QPair<int, int>(2, 4);
    case Qt::Key_Hyper_L:
        return QPair<int, int>(2, 2);
    case Qt::Key_Hyper_R:
        return QPair<int, int>(2, 3);
    case Qt::Key_Direction_L:
        return QPair<int, int>(2, 5);
    case Qt::Key_Direction_R:
        return QPair<int, int>(2, 6);
    case Qt::Key_Space:
        return QPair<int, int>(2, 7);
    case Qt::Key_Exclam:
        return QPair<int, int>(2, 9);
    case Qt::Key_QuoteDbl:
        return QPair<int, int>(2, 10);
    case Qt::Key_NumberSign:
        return QPair<int, int>(2, 11);
    case Qt::Key_Dollar:
        return QPair<int, int>(2, 12);
    case Qt::Key_Percent:
        return QPair<int, int>(2, 13);
    case Qt::Key_Ampersand:
        return QPair<int, int>(2, 14);
    case Qt::Key_Apostrophe:
        return QPair<int, int>(2, 15);
    case Qt::Key_ParenLeft:
        return QPair<int, int>(2, 16);
    case Qt::Key_ParenRight:
        return QPair<int, int>(2, 17);
    case Qt::Key_Asterisk:
        return QPair<int, int>(2, 18);
    case Qt::Key_Plus:
        return QPair<int, int>(2, 19);
    case Qt::Key_Comma:
        return QPair<int, int>(2, 20);
    case Qt::Key_Minus:
        return QPair<int, int>(2, 21);
    case Qt::Key_Period:
        return QPair<int, int>(2, 22);
    case Qt::Key_Slash:
        return QPair<int, int>(2, 23);
    case Qt::Key_0:
        return QPair<int, int>(2, 24);
    case Qt::Key_1:
        return QPair<int, int>(2, 25);
    case Qt::Key_2:
        return QPair<int, int>(2, 26);
    case Qt::Key_3:
        return QPair<int, int>(2, 27);
    case Qt::Key_4:
        return QPair<int, int>(2, 28);
    case Qt::Key_5:
        return QPair<int, int>(2, 29);
    case Qt::Key_6:
        return QPair<int, int>(2, 30);
    case Qt::Key_7:
        return QPair<int, int>(2, 31);
    case Qt::Key_8:
        return QPair<int, int>(3, 0);
    case Qt::Key_9:
        return QPair<int, int>(3, 1);
    case Qt::Key_Colon:
        return QPair<int, int>(3, 2);
    case Qt::Key_Semicolon:
        return QPair<int, int>(3, 3);
    case Qt::Key_Less:
        return QPair<int, int>(3, 4);
    case Qt::Key_Equal:
        return QPair<int, int>(3, 5);
    case Qt::Key_Greater:
        return QPair<int, int>(3, 6);
    case Qt::Key_Question:
        return QPair<int, int>(3, 7);
    case Qt::Key_At:
        return QPair<int, int>(3, 8);
    case Qt::Key_A:
        return QPair<int, int>(3, 9);
    case Qt::Key_B:
        return QPair<int, int>(3, 10);
    case Qt::Key_C:
        return QPair<int, int>(3, 11);
    case Qt::Key_D:
        return QPair<int, int>(3, 12);
    case Qt::Key_E:
        return QPair<int, int>(3, 13);
    case Qt::Key_F:
        return QPair<int, int>(3, 14);
    case Qt::Key_G:
        return QPair<int, int>(3, 15);
    case Qt::Key_H:
        return QPair<int, int>(3, 16);
    case Qt::Key_I:
        return QPair<int, int>(3, 17);
    case Qt::Key_J:
        return QPair<int, int>(3, 18);
    case Qt::Key_K:
        return QPair<int, int>(3, 19);
    case Qt::Key_L:
        return QPair<int, int>(3, 20);
    case Qt::Key_M:
        return QPair<int, int>(3, 21);
    case Qt::Key_N:
        return QPair<int, int>(3, 22);
    case Qt::Key_O:
        return QPair<int, int>(3, 23);
    case Qt::Key_P:
        return QPair<int, int>(3, 24);
    case Qt::Key_Q:
        return QPair<int, int>(3, 25);
    case Qt::Key_R:
        return QPair<int, int>(3, 26);
    case Qt::Key_S:
        return QPair<int, int>(3, 27);
    case Qt::Key_T:
        return QPair<int, int>(3, 28);
    case Qt::Key_U:
        return QPair<int, int>(3, 29);
    case Qt::Key_V:
        return QPair<int, int>(3, 30);
    case Qt::Key_W:
        return QPair<int, int>(3, 31);
    case Qt::Key_X:
        return QPair<int, int>(4, 0);
    case Qt::Key_Y:
        return QPair<int, int>(4, 1);
    case Qt::Key_Z:
        return QPair<int, int>(4, 2);
    case Qt::Key_BracketLeft:
        return QPair<int, int>(4, 3);
    case Qt::Key_Backslash:
        return QPair<int, int>(4, 4);
    case Qt::Key_BracketRight:
        return QPair<int, int>(4, 5);
    case Qt::Key_AsciiCircum:
        return QPair<int, int>(4, 6);
    case Qt::Key_Underscore:
        return QPair<int, int>(4, 7);
    case Qt::Key_QuoteLeft:
        return QPair<int, int>(4, 8);
    case Qt::Key_BraceLeft:
        return QPair<int, int>(4, 9);
    case Qt::Key_Bar:
        return QPair<int, int>(4, 10);
    case Qt::Key_BraceRight:
        return QPair<int, int>(4, 11);
    case Qt::Key_AsciiTilde:
        return QPair<int, int>(4, 12);
    case Qt::Key_plusminus:
        return QPair<int, int>(4, 13);
    case Qt::Key_onesuperior:
        return QPair<int, int>(4, 14);
    case Qt::Key_multiply:
        return QPair<int, int>(4, 15);
    case Qt::Key_division:
        return QPair<int, int>(4, 16);
    case Qt::Key_diaeresis:
        return QPair<int, int>(4, 17);
    default:
        return QPair<int, int>(-1, -1);
    }
    return position;
}
}  // namespace
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 28, as _ZN9Qt3DInput5Input11MouseDeviceD1Ev
namespace Qt3DInput::Input {
inline MouseDevice::~MouseDevice()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousehandler.cpp, line 28, as _ZN9Qt3DInput5Input12MouseHandlerD1Ev
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline MouseHandler::~MouseHandler()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 24, as _ZN9Qt3DInput5Input24GenericDeviceBackendNodeD1Ev
namespace Qt3DInput::Input {
inline GenericDeviceBackendNode::~GenericDeviceBackendNode()
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputchord.cpp, line 57, as _ZN9Qt3DInput5Input10InputChord16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void InputChord::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    AbstractActionInput::syncFromFrontEnd(frontEnd, firstTime);
    const QInputChord *node = qobject_cast<const QInputChord *>(frontEnd);
    if (!node)
        return;

    m_timeout = milliToNano(node->timeout());
    m_chords = Qt3DCore::qIdsForNodes(node->chords());
    m_inputsToTrigger = m_chords;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputchord.cpp, line 69, as _ZN9Qt3DInput5Input10InputChord7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline bool InputChord::process(InputHandler *inputHandler, qint64 currentTime)
{
    if (!isEnabled())
        return false;

    const qint64 startTime = m_startTime;
    bool triggered = false;
    int activeInputs = 0;
    for (const Qt3DCore::QNodeId &actionInputId : std::as_const(m_chords)) {
        AbstractActionInput *actionInput = inputHandler->lookupActionInput(actionInputId);
        if (actionInput && actionInput->process(inputHandler, currentTime)) {
            triggered |= actionTriggered(actionInputId);
            activeInputs++;
            if (startTime == 0)
                m_startTime = currentTime;
        }
    }

    if (startTime != 0) {
        // Check if we are still inside the time limit for the chord
        if ((currentTime - startTime) > m_timeout) {
            reset();
            if (activeInputs > 0)
                m_startTime = startTime;
            return false;
        }
    }

    return triggered;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/actioninput.cpp, line 30, as _ZN9Qt3DInput5Input11ActionInput16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void ActionInput::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    AbstractActionInput::syncFromFrontEnd(frontEnd, firstTime);
    const QActionInput *node = qobject_cast<const QActionInput *>(frontEnd);
    if (!node)
        return;

    m_sourceDevice = Qt3DCore::qIdForNode(node->sourceDevice());
    m_buttons = node->buttons();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/actioninput.cpp, line 41, as _ZN9Qt3DInput5Input11ActionInput7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline bool ActionInput::process(InputHandler *inputHandler, qint64 currentTime)
{
    Q_UNUSED(currentTime);

    if (!isEnabled())
        return false;

    QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend = Utils::physicalDeviceForInput(this, inputHandler);
    if (!physicalDeviceBackend)
        return false;

    for (int button : std::as_const(m_buttons)) {
        if (physicalDeviceBackend->isButtonPressed(button))
            return true;
    }

    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axissetting.cpp, line 30, as _ZN9Qt3DInput5Input11AxisSetting16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void AxisSetting::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAxisSetting *node = qobject_cast<const QAxisSetting *>(frontEnd);
    if (!node)
        return;

    m_deadZoneRadius = node->deadZoneRadius();
    m_axes = node->axes();
    m_smooth = node->isSmoothEnabled();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 81, as _ZN9Qt3DInput5Input13InputSequence16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void InputSequence::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    AbstractActionInput::syncFromFrontEnd(frontEnd, firstTime);
    const QInputSequence *node = qobject_cast<const QInputSequence *>(frontEnd);
    if (!node)
        return;

    m_timeout = milliToNano(node->timeout());
    m_buttonInterval = milliToNano(node->buttonInterval());
    m_sequences = Qt3DCore::qIdsForNodes(node->sequences());
    m_inputsToTrigger = m_sequences;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 94, as _ZN9Qt3DInput5Input13InputSequence7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline bool InputSequence::process(InputHandler *inputHandler, qint64 currentTime)
{
    if (!isEnabled())
        return false;

    if (m_startTime != 0) {
        // Check if we are still inside the time limit for the sequence
        if ((currentTime - m_startTime) > m_timeout) {
            reset();
            return false;
        }
    }

    bool triggered = false;
    for (const Qt3DCore::QNodeId &actionInputId : std::as_const(m_sequences)) {
        AbstractActionInput *actionInput = inputHandler->lookupActionInput(actionInputId);
        if (actionInput && actionInput->process(inputHandler, currentTime)) {
            triggered |= actionTriggered(actionInputId, currentTime);
            if (m_startTime == 0)
                m_startTime = currentTime;
        }
    }
    return triggered;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/logicaldevice.cpp, line 31, as _ZN9Qt3DInput5Input13LogicalDevice16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void LogicalDevice::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QLogicalDevice *node = qobject_cast<const QLogicalDevice *>(frontEnd);
    if (!node)
        return;

    m_actions = Qt3DCore::qIdsForNodes(node->actions());
    m_axes = Qt3DCore::qIdsForNodes(node->axes());
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 335, as _ZN9Qt3DInput5Input14KeyboardDevice7cleanupEv
namespace Qt3DInput::Input {
inline void KeyboardDevice::cleanup()
{
    QAbstractPhysicalDeviceBackendNode::cleanup();
    m_keyStates.keys[0] = 0;
    m_keyStates.keys[1] = 0;
    m_keyStates.keys[2] = 0;
    m_keyStates.keys[3] = 0;
    m_keyStates.keys[4] = 0;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 363, as _ZNK9Qt3DInput5Input14KeyboardDevice9axisValueEi
namespace Qt3DInput::Input {
inline float KeyboardDevice::axisValue(int axisIdentifier) const
{
    Q_UNUSED(axisIdentifier);
    return 0.0f;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/keyboarddevice.cpp, line 369, as _ZNK9Qt3DInput5Input14KeyboardDevice15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool KeyboardDevice::isButtonPressed(int buttonIdentifier) const
{
    QPair<int, int> position = getKeyPosition(buttonIdentifier);
    if (position.first != -1 && position.second != -1)
        return m_keyStates.keys[position.first] & (1 << position.second);
    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/buttonaxisinput.cpp, line 85, as _ZN9Qt3DInput5Input15ButtonAxisInput7processEPNS0_12InputHandlerEx
namespace Qt3DInput::Input {
inline float ButtonAxisInput::process(InputHandler *inputHandler, qint64 currentTime)
{
    if (!isEnabled())
        return 0.0f;

    if (m_buttons.isEmpty())
        return 0.0f;

    QAbstractPhysicalDeviceBackendNode *physicalDeviceBackend = Utils::physicalDeviceForInput(this, inputHandler);
    if (!physicalDeviceBackend)
        return 0.0f;

    // TO DO: Linear Curver for the progression of the scale value
    if (anyOfRequiredButtonsPressed(m_buttons, physicalDeviceBackend))
        updateSpeedRatio(currentTime, ButtonAxisInput::Accelerate);
    else if (m_speedRatio != 0.0f)
        updateSpeedRatio(currentTime, ButtonAxisInput::Decelerate);

    return m_speedRatio * m_scale;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 63, as _ZN9Qt3DInput5Input19PhysicalDeviceProxy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void PhysicalDeviceProxy::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);

    if (firstTime) {
        const QAbstractPhysicalDeviceProxy *node = qobject_cast<const QAbstractPhysicalDeviceProxy *>(frontEnd);
        if (!node)
            return;

        m_deviceName = node->deviceName();

        // Request to load the actual device
        m_manager->addPendingProxyToLoad(peerId());
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/axis.cpp, line 37, as _ZN9Qt3DInput5Input4Axis16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void Axis::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QAxis *node = qobject_cast<const Qt3DInput::QAxis *>(frontEnd);
    if (!node)
        return;

    auto ids = Qt3DCore::qIdsForNodes(node->inputs());
    m_inputs = ids;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/action.cpp, line 36, as _ZN9Qt3DInput5Input6Action16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void Action::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QAction *node = qobject_cast<const Qt3DInput::QAction *>(frontEnd);
    if (!node)
        return;

    auto ids = Qt3DCore::qIdsForNodes(node->inputs());
    m_inputs = ids;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/mousedevice.cpp, line 121, as _ZN9Qt3DInput5Input11MouseDevice19resetMouseAxisStateEv
namespace Qt3DInput::Input {
inline void MouseDevice::resetMouseAxisState()
{
    // Reset axis values before we accumulate new values for this frame
    m_mouseState.xAxis = 0.0f;
    m_mouseState.yAxis = 0.0f;
#if QT_CONFIG(wheelevent)
    m_mouseState.wXAxis = 0.0f;
    m_mouseState.wYAxis = 0.0f;
#endif
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 128, as _ZN9Qt3DInput5Input12InputHandler22unregisterEventFiltersEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::unregisterEventFilters()
{
    if (m_service)
        m_service->unregisterEventFilter(m_eventFilter);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 122, as _ZN9Qt3DInput5Input12InputHandler20registerEventFiltersEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::registerEventFilters()
{
    if (m_service)
        m_service->registerEventFilter(m_eventFilter, 512);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputchord.cpp, line 41, as _ZN9Qt3DInput5Input10InputChord15actionTriggeredEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
inline bool InputChord::actionTriggered(Qt3DCore::QNodeId input)
{
    m_inputsToTrigger.removeOne(input);
    if (m_inputsToTrigger.isEmpty()) {
        //All Triggered
        reset();
        return true;
    }
    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputchord.cpp, line 35, as _ZN9Qt3DInput5Input10InputChord5resetEv
namespace Qt3DInput::Input {
inline void InputChord::reset()
{
    m_startTime = 0;
    m_inputsToTrigger = m_chords;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 55, as _ZN9Qt3DInput5Input13InputSequence15actionTriggeredEN8Qt3DCore7QNodeIdEx
namespace Qt3DInput::Input {
inline bool InputSequence::actionTriggered(Qt3DCore::QNodeId input, const qint64 currentTime)
{
    if (input != m_inputsToTrigger.first())
        return false;

    // Save the last input
    m_lastInputId = input;
    // Return false if we've spent too much time in between two sequences
    if ((m_lastInputTime != 0) && ((currentTime - m_lastInputTime) > m_buttonInterval)) {
        reset();
        return false;
    }

    // Update lastInputTime and remove the inputs to trigger from the sequence
    m_lastInputTime = currentTime;
    m_inputsToTrigger.removeOne(input);

    // If we have no more remaining inputs in the sequences of inputs
    if (m_inputsToTrigger.isEmpty()) {
        // All Triggered
        reset();
        return true;
    }
    return false;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 47, as _ZN9Qt3DInput5Input13InputSequence5resetEv
namespace Qt3DInput::Input {
inline void InputSequence::reset()
{
    m_startTime = 0;
    m_lastInputTime = 0;
    m_inputsToTrigger = m_sequences;
    m_lastInputId = Qt3DCore::QNodeId();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 28, as _ZN9Qt3DInput5Input24GenericDeviceBackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DInput::Input {
inline void GenericDeviceBackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    QAbstractPhysicalDeviceBackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const Qt3DInput::QGenericInputDevice *node = qobject_cast<const Qt3DInput::QGenericInputDevice *>(frontEnd);
    if (!node)
        return;

    auto *d = static_cast<Qt3DInput::QAbstractPhysicalDevicePrivate *>( Qt3DCore::QNodePrivate::get(const_cast<Qt3DCore::QNode *>(frontEnd)) );

    {
        const QMutexLocker lock(&m_mutex);
        for (const auto &val: std::as_const(d->m_pendingAxisEvents))
            m_axesValues[val.first] = val.second;
        for (const auto &val: std::as_const(d->m_pendingButtonsEvents))
            m_buttonsValues[val.first] = val.second;

        d->m_pendingAxisEvents.clear();
        d->m_pendingButtonsEvents.clear();
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 49, as _ZN9Qt3DInput5Input24GenericDeviceBackendNode7cleanupEv
namespace Qt3DInput::Input {
inline void GenericDeviceBackendNode::cleanup()
{
    const QMutexLocker lock(&m_mutex);
    m_axesValues.clear();
    m_buttonsValues.clear();
    QAbstractPhysicalDeviceBackendNode::cleanup();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/physicaldeviceproxy.cpp, line 58, as _ZNK9Qt3DInput5Input19PhysicalDeviceProxy16physicalDeviceIdEv
namespace Qt3DInput::Input {
inline Qt3DCore::QNodeId PhysicalDeviceProxy::physicalDeviceId() const
{
    return m_physicalDeviceId;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 63, as _ZNK9Qt3DInput5Input24GenericDeviceBackendNode15isButtonPressedEi
namespace Qt3DInput::Input {
inline bool GenericDeviceBackendNode::isButtonPressed(int buttonIdentifier) const
{
    const QMutexLocker lock(&m_mutex);
    return m_buttonsValues[buttonIdentifier];
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/genericdevicebackendnode.cpp, line 57, as _ZNK9Qt3DInput5Input24GenericDeviceBackendNode9axisValueEi
namespace Qt3DInput::Input {
inline float GenericDeviceBackendNode::axisValue(int axisIdentifier) const
{
    const QMutexLocker lock(&m_mutex);
    return m_axesValues[axisIdentifier];
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 167, as _ZN9Qt3DInput5Input12InputHandler20appendKeyboardDeviceEN8Qt3DCore7QHandleINS0_14KeyboardDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::appendKeyboardDevice(HKeyboardDevice device)
{
    m_activeKeyboardDevices.append(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 172, as _ZN9Qt3DInput5Input12InputHandler20removeKeyboardDeviceEN8Qt3DCore7QHandleINS0_14KeyboardDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::removeKeyboardDevice(HKeyboardDevice device)
{
    m_activeKeyboardDevices.removeAll(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 177, as _ZN9Qt3DInput5Input12InputHandler17appendMouseDeviceEN8Qt3DCore7QHandleINS0_11MouseDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::appendMouseDevice(HMouseDevice device)
{
    m_activeMouseDevices.append(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 182, as _ZN9Qt3DInput5Input12InputHandler17removeMouseDeviceEN8Qt3DCore7QHandleINS0_11MouseDeviceEEE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::removeMouseDevice(HMouseDevice device)
{
    m_activeMouseDevices.removeAll(device);
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 187, as _ZN9Qt3DInput5Input12InputHandler19appendGenericDeviceEN8Qt3DCore7QHandleINS0_24GenericDeviceBackendNodeEEE
inline void Qt3DInput::Input::InputHandler::appendGenericDevice(HGenericDeviceBackendNode device)
{
    m_activeGenericPhysicalDevices.append(device);
}

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 192, as _ZN9Qt3DInput5Input12InputHandler19removeGenericDeviceEN8Qt3DCore7QHandleINS0_24GenericDeviceBackendNodeEEE
inline void Qt3DInput::Input::InputHandler::removeGenericDevice(HGenericDeviceBackendNode device)
{
    m_activeGenericPhysicalDevices.removeAll(device);
}

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 198, as _ZN9Qt3DInput5Input12InputHandler19resetMouseAxisStateEv
inline void Qt3DInput::Input::InputHandler::resetMouseAxisState()
{
    for (const HMouseDevice &cHandle : std::as_const(m_activeMouseDevices)) {
        MouseDevice *controller = m_mouseDeviceManager->data(cHandle);
        controller->resetMouseAxisState();
    }
}

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 206, as _ZNK9Qt3DInput5Input12InputHandler23inputDeviceIntegrationsEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline QList<QInputDeviceIntegration *> InputHandler::inputDeviceIntegrations() const
{
    return m_inputDeviceIntegrations;
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

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 134, as _ZN9Qt3DInput5Input12InputHandler16setInputSettingsEPNS0_13InputSettingsE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::setInputSettings(InputSettings *settings)
{
    if (m_settings && settings == nullptr) {
        unregisterEventFilters();
        m_lastEventSource = nullptr;
        if (m_settings->eventSource() && m_service)
            m_service->shutdown(m_settings->eventSource());
    }
    if (m_service) {
        unregisterEventFilters();
        if (m_settings && m_settings->eventSource())
            m_service->shutdown(m_settings->eventSource());
    }
    m_settings = settings;
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 150, as _ZN9Qt3DInput5Input12InputHandler17updateEventSourceEv
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline void InputHandler::updateEventSource()
{
    // Called every frame from input aspect
    // Should probably just listen to changes in source property on settings object
    if (!m_settings || !m_service)
        return;

    // Will be updated only if eventSource is different than
    // what was set last
    QObject *eventSource = m_settings->eventSource();
    if (eventSource && m_lastEventSource != eventSource) {
        m_service->initialize(eventSource);
        registerEventFilters();
        m_lastEventSource = eventSource;
    }
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 226, as _ZN9Qt3DInput5Input12InputHandler21setEventFilterServiceEPN8Qt3DCore19QEventFilterServiceE
inline void Qt3DInput::Input::InputHandler::setEventFilterService(QEventFilterService *service)
{
    m_service = service;
}

//  from ../qt3d/src/input/backend/inputhandler.cpp, line 231, as _ZNK9Qt3DInput5Input12InputHandler17lookupActionInputEN8Qt3DCore7QNodeIdE
namespace Qt3DInput::Input {
using namespace Qt3DCore;
inline AbstractActionInput *InputHandler::lookupActionInput(Qt3DCore::QNodeId id) const
{
    AbstractActionInput *input = nullptr;
    if ((input = actionInputManager()->lookupResource(id)) != nullptr)
        return input;
    if ((input = inputSequenceManager()->lookupResource(id)) != nullptr)
        return input;
    return inputChordManager()->lookupResource(id); // nullptr if not found
}
}  // namespace Qt3DInput::Input
//  -----------------------------------------------------------------------

//  void Qt3DInput::Input::InputHandler::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DInput::Input::InputHandler *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  KeyboardDeviceManager
//      *Qt3DInput::Input::InputHandler::keyboardDeviceManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::KeyboardDeviceManager *ritual_ZNK9Qt3DInput5Input12InputHandler21keyboardDeviceManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->keyboardDeviceManager();
}

//  KeyboardInputManager
//      *Qt3DInput::Input::InputHandler::keyboardInputManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::KeyboardInputManager *ritual_ZNK9Qt3DInput5Input12InputHandler20keyboardInputManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->keyboardInputManager();
}

//  MouseDeviceManager *Qt3DInput::Input::InputHandler::mouseDeviceManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseDeviceManager *ritual_ZNK9Qt3DInput5Input12InputHandler18mouseDeviceManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->mouseDeviceManager();
}

//  MouseInputManager *Qt3DInput::Input::InputHandler::mouseInputManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseInputManager *ritual_ZNK9Qt3DInput5Input12InputHandler17mouseInputManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->mouseInputManager();
}

//  AxisManager *Qt3DInput::Input::InputHandler::axisManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AxisManager *ritual_ZNK9Qt3DInput5Input12InputHandler11axisManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->axisManager();
}

//  AxisAccumulatorManager
//      *Qt3DInput::Input::InputHandler::axisAccumulatorManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AxisAccumulatorManager *ritual_ZNK9Qt3DInput5Input12InputHandler22axisAccumulatorManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->axisAccumulatorManager();
}

//  ActionManager *Qt3DInput::Input::InputHandler::actionManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::ActionManager *ritual_ZNK9Qt3DInput5Input12InputHandler13actionManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->actionManager();
}

//  AxisSettingManager *Qt3DInput::Input::InputHandler::axisSettingManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AxisSettingManager *ritual_ZNK9Qt3DInput5Input12InputHandler18axisSettingManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->axisSettingManager();
}

//  ActionInputManager *Qt3DInput::Input::InputHandler::actionInputManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::ActionInputManager *ritual_ZNK9Qt3DInput5Input12InputHandler18actionInputManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->actionInputManager();
}

//  AnalogAxisInputManager
//      *Qt3DInput::Input::InputHandler::analogAxisInputManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AnalogAxisInputManager *ritual_ZNK9Qt3DInput5Input12InputHandler22analogAxisInputManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->analogAxisInputManager();
}

//  ButtonAxisInputManager
//      *Qt3DInput::Input::InputHandler::buttonAxisInputManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::ButtonAxisInputManager *ritual_ZNK9Qt3DInput5Input12InputHandler22buttonAxisInputManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->buttonAxisInputManager();
}

//  InputChordManager *Qt3DInput::Input::InputHandler::inputChordManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputChordManager *ritual_ZNK9Qt3DInput5Input12InputHandler17inputChordManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->inputChordManager();
}

//  InputSequenceManager
//      *Qt3DInput::Input::InputHandler::inputSequenceManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputSequenceManager *ritual_ZNK9Qt3DInput5Input12InputHandler20inputSequenceManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->inputSequenceManager();
}

//  LogicalDeviceManager
//      *Qt3DInput::Input::InputHandler::logicalDeviceManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::LogicalDeviceManager *ritual_ZNK9Qt3DInput5Input12InputHandler20logicalDeviceManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->logicalDeviceManager();
}

//  GenericDeviceBackendNodeManager
//      *Qt3DInput::Input::InputHandler::genericDeviceBackendNodeManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::GenericDeviceBackendNodeManager *ritual_ZNK9Qt3DInput5Input12InputHandler31genericDeviceBackendNodeManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->genericDeviceBackendNodeManager();
}

//  PhysicalDeviceProxyManager
//      *Qt3DInput::Input::InputHandler::physicalDeviceProxyManager() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::PhysicalDeviceProxyManager *ritual_ZNK9Qt3DInput5Input12InputHandler26physicalDeviceProxyManagerEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->physicalDeviceProxyManager();
}

//  InputSettings *Qt3DInput::Input::InputHandler::inputSettings() const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputSettings *ritual_ZNK9Qt3DInput5Input12InputHandler13inputSettingsEv(
    const Qt3DInput::Input::InputHandler *self) {
  return self->inputSettings();
}

//  void Qt3DInput::Input::InputHandler::appendKeyboardDevice(HKeyboardDevice
//      device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler20appendKeyboardDeviceEN8Qt3DCore7QHandleINS0_14KeyboardDeviceEEE(
    Qt3DInput::Input::InputHandler *self,
    const Qt3DInput::Input::HKeyboardDevice *device) {
  self->appendKeyboardDevice(*device);
}

//  void Qt3DInput::Input::InputHandler::removeKeyboardDevice(HKeyboardDevice
//      device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler20removeKeyboardDeviceEN8Qt3DCore7QHandleINS0_14KeyboardDeviceEEE(
    Qt3DInput::Input::InputHandler *self,
    const Qt3DInput::Input::HKeyboardDevice *device) {
  self->removeKeyboardDevice(*device);
}

//  void Qt3DInput::Input::InputHandler::appendMouseDevice(HMouseDevice
//      device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler17appendMouseDeviceEN8Qt3DCore7QHandleINS0_11MouseDeviceEEE(
    Qt3DInput::Input::InputHandler *self,
    const Qt3DInput::Input::HMouseDevice *device) {
  self->appendMouseDevice(*device);
}

//  void Qt3DInput::Input::InputHandler::removeMouseDevice(HMouseDevice
//      device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler17removeMouseDeviceEN8Qt3DCore7QHandleINS0_11MouseDeviceEEE(
    Qt3DInput::Input::InputHandler *self,
    const Qt3DInput::Input::HMouseDevice *device) {
  self->removeMouseDevice(*device);
}

//  void Qt3DInput::Input::InputHandler::appendGenericDevice(HGenericDeviceBa
//      ckendNode device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler19appendGenericDeviceEN8Qt3DCore7QHandleINS0_24GenericDeviceBackendNodeEEE(
    Qt3DInput::Input::InputHandler *self,
    const Qt3DInput::Input::HGenericDeviceBackendNode *device) {
  self->appendGenericDevice(*device);
}

//  void Qt3DInput::Input::InputHandler::removeGenericDevice(HGenericDeviceBa
//      ckendNode device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler19removeGenericDeviceEN8Qt3DCore7QHandleINS0_24GenericDeviceBackendNodeEEE(
    Qt3DInput::Input::InputHandler *self,
    const Qt3DInput::Input::HGenericDeviceBackendNode *device) {
  self->removeGenericDevice(*device);
}

//  void Qt3DInput::Input::InputHandler::resetMouseAxisState()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler19resetMouseAxisStateEv(
    Qt3DInput::Input::InputHandler *self) {
  self->resetMouseAxisState();
}

//  QList<Qt3DInput::QInputDeviceIntegration *>
//      Qt3DInput::Input::InputHandler::inputDeviceIntegrations() const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::QInputDeviceIntegration *> *ritual_ZNK9Qt3DInput5Input12InputHandler23inputDeviceIntegrationsEv(
    const Qt3DInput::Input::InputHandler *self) {
  return new QList<Qt3DInput::QInputDeviceIntegration *>(
      self->inputDeviceIntegrations());
}

//  void Qt3DInput::Input::InputHandler::addInputDeviceIntegration(QInputDevi
//      ceIntegration *inputIntegration)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler25addInputDeviceIntegrationEPNS_23QInputDeviceIntegrationE(
    Qt3DInput::Input::InputHandler *self,
    Qt3DInput::QInputDeviceIntegration *inputIntegration) {
  self->addInputDeviceIntegration(inputIntegration);
}

//  void Qt3DInput::Input::InputHandler::setInputSettings(InputSettings
//      *settings)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler16setInputSettingsEPNS0_13InputSettingsE(
    Qt3DInput::Input::InputHandler *self,
    Qt3DInput::Input::InputSettings *settings) {
  self->setInputSettings(settings);
}

//  void Qt3DInput::Input::InputHandler::updateEventSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler17updateEventSourceEv(
    Qt3DInput::Input::InputHandler *self) {
  self->updateEventSource();
}

//  void Qt3DInput::Input::InputHandler::setEventFilterService(Qt3DCore::QEve
//      ntFilterService *service)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input12InputHandler21setEventFilterServiceEPN8Qt3DCore19QEventFilterServiceE(
    Qt3DInput::Input::InputHandler *self,
    Qt3DCore::QEventFilterService *service) {
  self->setEventFilterService(service);
}

//  AbstractActionInput
//      *Qt3DInput::Input::InputHandler::lookupActionInput(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::AbstractActionInput *ritual_ZNK9Qt3DInput5Input12InputHandler17lookupActionInputEN8Qt3DCore7QNodeIdE(
    const Qt3DInput::Input::InputHandler *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupActionInput(*id);
}

//  a QList<Qt3DInput::QInputDeviceIntegration *> a ritual of
//      Qt3DInput::Input::InputHandler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_InputHandler__QList_Qt3DInput_QInputDeviceIntegration(
    QList<Qt3DInput::QInputDeviceIntegration *> *self) {
  delete self;
}
