//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputchord_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputchord_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/private/abstractactioninput_p.h>
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
#include <Qt3DInput/private/inputchord_p.h>
#include <Qt3DInput/qinputchord.h>
#include <Qt3DInput/private/qinputchord_p.h>
#include <Qt3DInput/private/inputhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/backend/abstractactioninput.cpp, line 12, as _ZN9Qt3DInput5Input19AbstractActionInputC2Ev
namespace Qt3DInput::Input {
inline AbstractActionInput::AbstractActionInput()
    : BackendNode()
{
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

//  from ../qt3d/src/input/backend/inputchord.cpp, line 17, as _ZN9Qt3DInput5Input10InputChordC1Ev
namespace Qt3DInput::Input {
inline InputChord::InputChord()
    : AbstractActionInput()
    , m_chords()
    , m_inputsToTrigger()
    , m_timeout(0)
    , m_startTime(0)
{
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputchord.cpp, line 26, as _ZN9Qt3DInput5Input10InputChord7cleanupEv
namespace Qt3DInput::Input {
inline void InputChord::cleanup()
{
    setEnabled(false);
    m_timeout = 0;
    m_startTime = 0;
    m_chords.clear();
    m_inputsToTrigger.clear();
}
}  // namespace Qt3DInput::Input

//  from ../qt3d/src/input/backend/inputchord.cpp, line 52, as _ZN9Qt3DInput5Input10InputChord12setStartTimeEx
namespace Qt3DInput::Input {
inline void InputChord::setStartTime(qint64 time)
{
    m_startTime = time;
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
//  -----------------------------------------------------------------------

//  Qt3DInput::Input::InputChord::InputChord()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::InputChord *ritual_ZN9Qt3DInput5Input10InputChordC1Ev() {
  return new Qt3DInput::Input::InputChord();
}

//  void Qt3DInput::Input::InputChord::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input10InputChord7cleanupEv(
    Qt3DInput::Input::InputChord *self) {
  self->cleanup();
}

//  QList<Qt3DCore::QNodeId> Qt3DInput::Input::InputChord::chords() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK9Qt3DInput5Input10InputChord6chordsEv(
    const Qt3DInput::Input::InputChord *self) {
  return new QList<Qt3DCore::QNodeId>(self->chords());
}

//  qint64 Qt3DInput::Input::InputChord::timeout() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9Qt3DInput5Input10InputChord7timeoutEv(
    const Qt3DInput::Input::InputChord *self) {
  return self->timeout();
}

//  qint64 Qt3DInput::Input::InputChord::startTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9Qt3DInput5Input10InputChord9startTimeEv(
    const Qt3DInput::Input::InputChord *self) {
  return self->startTime();
}

//  void Qt3DInput::Input::InputChord::setStartTime(qint64 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input10InputChord12setStartTimeEx(
    Qt3DInput::Input::InputChord *self,
    qint64 time) {
  self->setStartTime(time);
}

//  void Qt3DInput::Input::InputChord::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input10InputChord5resetEv(
    Qt3DInput::Input::InputChord *self) {
  self->reset();
}

//  bool Qt3DInput::Input::InputChord::actionTriggered(Qt3DCore::QNodeId
//      input)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DInput5Input10InputChord15actionTriggeredEN8Qt3DCore7QNodeIdE(
    Qt3DInput::Input::InputChord *self,
    const Qt3DCore::QNodeId *input) {
  return self->actionTriggered(*input);
}

//  void Qt3DInput::Input::InputChord::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input10InputChord16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::InputChord *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  bool Qt3DInput::Input::InputChord::process(InputHandler *inputHandler,
//      qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9Qt3DInput5Input10InputChord7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::InputChord *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->process(inputHandler, currentTime);
}

//  void Qt3DInput::Input::InputChord::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9Qt3DInput5Input10InputChord16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DInput::Input::InputChord *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DInput::Input::InputChord::syncFromFrontEnd(frontEnd, firstTime);
}

//  bool Qt3DInput::Input::InputChord::process(InputHandler *inputHandler,
//      qint64 currentTime)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9Qt3DInput5Input10InputChord7processEPNS0_12InputHandlerEx(
    Qt3DInput::Input::InputChord *self,
    Qt3DInput::Input::InputHandler *inputHandler,
    qint64 currentTime) {
  return self->Qt3DInput::Input::InputChord::process(
      inputHandler,
      currentTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DInput::Input::InputChord gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_InputChord__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
