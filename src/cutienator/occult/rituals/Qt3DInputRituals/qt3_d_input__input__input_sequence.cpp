//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputsequence_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputsequence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/abstractactioninput_p.h>
#include <Qt3DInput/private/inputsequence_p.h>
#include <Qt3DInput/qabstractphysicaldevice.h>
#include <Qt3DInput/qinputsequence.h>
#include <QtCore/QDateTime>
#include <Qt3DInput/private/inputhandler_p.h>
#include <Qt3DInput/private/qinputsequence_p.h>
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

//  from ../qt3d/src/input/backend/abstractactioninput.cpp, line 12, as _ZN9Qt3DInput5Input19AbstractActionInputC2Ev
namespace Qt3DInput::Input {
inline AbstractActionInput::AbstractActionInput()
    : BackendNode()
{
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

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 19, as _ZN9Qt3DInput5Input13InputSequenceC1Ev
namespace Qt3DInput::Input {
inline InputSequence::InputSequence()
    : AbstractActionInput()
    , m_sequences()
    , m_inputsToTrigger()
    , m_timeout(0)
    , m_buttonInterval(0)
    , m_startTime(0)
    , m_lastInputTime(0)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 30, as _ZN9Qt3DInput5Input13InputSequence7cleanupEv
namespace Qt3DInput::Input {
inline void InputSequence::cleanup()
{
    setEnabled(false);
    m_timeout = 0;
    m_buttonInterval = 0;
    m_startTime = 0;
    m_lastInputTime = 0;
    m_lastInputId = Qt3DCore::QNodeId();
    m_sequences.clear();
    m_inputsToTrigger.clear();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputsequence.cpp, line 42, as _ZN9Qt3DInput5Input13InputSequence12setStartTimeEx
namespace Qt3DInput::Input {
inline void InputSequence::setStartTime(qint64 time)
{
    m_startTime = time;
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
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::InputSequence::InputSequence()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputSequence *ritual_ZN9Qt3DInput5Input13InputSequenceC1Ev() {
  return new Qt3DInput::Input::InputSequence();
}

//  void Qt3DInput::Input::InputSequence::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13InputSequence7cleanupEv(
    Qt3DInput::Input::InputSequence *self) {
  self->cleanup();
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::InputSequence::sequences()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input13InputSequence9sequencesEv(
    const Qt3DInput::Input::InputSequence *self) {
  return new QList<Qt3DCore::QNodeId>(self->sequences());
}

//  qint64 Qt3DInput::Input::InputSequence::timeout() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9Qt3DInput5Input13InputSequence7timeoutEv(
    const Qt3DInput::Input::InputSequence *self) {
  return self->timeout();
}

//  qint64 Qt3DInput::Input::InputSequence::buttonInterval() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9Qt3DInput5Input13InputSequence14buttonIntervalEv(
    const Qt3DInput::Input::InputSequence *self) {
  return self->buttonInterval();
}

//  qint64 Qt3DInput::Input::InputSequence::startTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9Qt3DInput5Input13InputSequence9startTimeEv(
    const Qt3DInput::Input::InputSequence *self) {
  return self->startTime();
}

//  void Qt3DInput::Input::InputSequence::setStartTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13InputSequence12setStartTimeEx(
    Qt3DInput::Input::InputSequence *self,
    qint64 time) {
  self->setStartTime(time);
}

//  void Qt3DInput::Input::InputSequence::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13InputSequence5resetEv(
    Qt3DInput::Input::InputSequence *self) {
  self->reset();
}

//  bool Qt3DInput::Input::InputSequence::actionTriggered(Qt3DCore::QNodeId
//      input, const qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DInput5Input13InputSequence15actionTriggeredEN8Qt3DCore7QNodeIdEx(
    Qt3DInput::Input::InputSequence *self,
    const Qt3DCore::QNodeId *input,
    qint64 currentTime) {
  return self->actionTriggered(*input, currentTime);
}

//  void Qt3DInput::Input::InputSequence::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input13InputSequence16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::InputSequence *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  bool Qt3DInput::Input::InputSequence::process(InputHandler *inputHandler,
//      qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DInput5Input13InputSequence7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::InputSequence *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  void Qt3DInput::Input::InputSequence::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input13InputSequence16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::InputSequence *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::InputSequence::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  bool Qt3DInput::Input::InputSequence::process(InputHandler *inputHandler,
//      qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9Qt3DInput5Input13InputSequence7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::InputSequence *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->Qt3DInput::Input::InputSequence::process(
      inputHandler,
      currentTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DInput::Input::InputSequence
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_InputSequence__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
