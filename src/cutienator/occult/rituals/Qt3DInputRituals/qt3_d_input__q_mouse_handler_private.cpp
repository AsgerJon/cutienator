//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qmousehandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qmousehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/qmousehandler.h>
#include <Qt3DInput/private/qmousehandler_p.h>
#include <Qt3DInput/qmousedevice.h>
#include <Qt3DInput/qmouseevent.h>
#include <QtCore/QTimer>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/input/frontend/qmousehandler.cpp, line 19, as _ZN9Qt3DInput20QMouseHandlerPrivateC1Ev
namespace Qt3DInput {
using namespace Qt3DCore;
using namespace std::chrono_literals;
inline QMouseHandlerPrivate::QMouseHandlerPrivate()
    : QComponentPrivate()
    , m_mouseDevice(nullptr)
    , m_containsMouse(false)
{
    m_shareable = false;
}
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qmousehandler.cpp, line 27, as _ZN9Qt3DInput20QMouseHandlerPrivateD1Ev
namespace Qt3DInput {
using namespace Qt3DCore;
using namespace std::chrono_literals;
inline QMouseHandlerPrivate::~QMouseHandlerPrivate()
{
}
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qmousehandler.cpp, line 31, as _ZN9Qt3DInput20QMouseHandlerPrivate4initEv
namespace Qt3DInput {
using namespace Qt3DCore;
using namespace std::chrono_literals;
inline void QMouseHandlerPrivate::init()
{
    Q_Q(QMouseHandler);

    m_pressAndHoldTimer = new QTimer(q);
    m_pressAndHoldTimer->setSingleShot(true);
    m_pressAndHoldTimer->setInterval(800ms);
    QObject::connect(m_pressAndHoldTimer, &QTimer::timeout, q, [this, q] {
        emit q->pressAndHold(m_lastPressedEvent.data());
    });
}
}  // namespace Qt3DInput

//  from ../qt3d/src/input/frontend/qmousehandler.cpp, line 43, as _ZN9Qt3DInput20QMouseHandlerPrivate10mouseEventERK14QSharedPointerINS_11QMouseEventEE
namespace Qt3DInput {
using namespace Qt3DCore;
using namespace std::chrono_literals;
inline void QMouseHandlerPrivate::mouseEvent(const QMouseEventPtr &event)
{
    Q_Q(QMouseHandler);
    switch (event->type()) {
    case QEvent::MouseButtonPress:
        m_lastPressedEvent = event;
        m_pressAndHoldTimer->start();
        emit q->pressed(event.data());
        break;
    case QEvent::MouseButtonRelease:
        m_pressAndHoldTimer->stop();
        emit q->released(event.data());
        emit q->clicked(event.data());
        break;
#if QT_CONFIG(gestures)
    case QEvent::Gesture:
        emit q->clicked(event.data());
        break;
#endif
    case QEvent::MouseButtonDblClick:
        emit q->doubleClicked(event.data());
        break;
    case QEvent::MouseMove:
        m_pressAndHoldTimer->stop();
        emit q->positionChanged(event.data());
        break;
    default:
        break;
    }
}
}  // namespace Qt3DInput
//  -----------------------------------------------------------------------

//  A Qt3DInput::QMouseHandlerPrivate that Python can take functions over in. Every Qt3DInput::QMouseHandlerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QMouseHandlerPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QMouseHandlerPrivateCall1)(const void *, int *);
class CuteQt3DInput_QMouseHandlerPrivate : public Qt3DInput::QMouseHandlerPrivate {
public:
  using Qt3DInput::QMouseHandlerPrivate::QMouseHandlerPrivate;
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
      CuteQt3DInput_QMouseHandlerPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QMouseHandlerPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QMouseHandlerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QMouseHandlerPrivate::QMouseHandlerPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseHandlerPrivate *ritual_ZN9Qt3DInput20QMouseHandlerPrivateC1Ev() {
  return new CuteQt3DInput_QMouseHandlerPrivate();
}

//  Qt3DInput::QMouseHandlerPrivate::~QMouseHandlerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput20QMouseHandlerPrivateD1Ev(
    Qt3DInput::QMouseHandlerPrivate *self) {
  delete self;
}

//  void Qt3DInput::QMouseHandlerPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput20QMouseHandlerPrivate4initEv(
    Qt3DInput::QMouseHandlerPrivate *self) {
  self->init();
}

//  void Qt3DInput::QMouseHandlerPrivate::mouseEvent(const QMouseEventPtr
//      &event)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput20QMouseHandlerPrivate10mouseEventERK14QSharedPointerINS_11QMouseEventEE(
    Qt3DInput::QMouseHandlerPrivate *self,
    const Qt3DInput::QMouseEventPtr *event) {
  self->mouseEvent(*event);
}

//  QMouseHandler *Qt3DInput::QMouseHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QMouseHandler *ritual_ZN9Qt3DInput20QMouseHandlerPrivate6q_funcEv(
    Qt3DInput::QMouseHandlerPrivate *self) {
  return self->q_func();
}

//  const QMouseHandler *Qt3DInput::QMouseHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QMouseHandler *ritual_ZNK9Qt3DInput20QMouseHandlerPrivate6q_funcEv(
    const Qt3DInput::QMouseHandlerPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DInput_QMouseHandlerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QMouseHandlerPrivate(
    Qt3DInput::QMouseHandlerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QMouseHandlerPrivate *>(self)->take(key, call);
}
