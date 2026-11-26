//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandwlshellintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandwlshellintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/private/qwaylandwlshellintegration_p.h>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/QWaylandWlShellSurface>
#include <QtWaylandCompositor/QWaylandQuickShellSurfaceItem>
#include <QtWaylandCompositor/QWaylandSeat>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 257, as _ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QEvent
namespace QtWayland {
inline bool WlShellIntegration::eventFilter(QObject *object, QEvent *event)
{
    if (event->type() == QEvent::MouseMove) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
        return filterMouseMoveEvent(mouseEvent);
    } else if (event->type() == QEvent::MouseButtonRelease) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
        return filterMouseReleaseEvent(mouseEvent);
    }
    return QWaylandQuickShellIntegration::eventFilter(object, event);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 231, as _ZN9QtWayland18WlShellIntegration30handleSurfaceHasContentChangedEv
namespace QtWayland {
inline void WlShellIntegration::handleSurfaceHasContentChanged()
{
    if (m_shellSurface && m_shellSurface->surface()->destinationSize().isEmpty()
            && m_shellSurface->windowType() == Qt::WindowType::Popup) {
        handlePopupClosed();
    }
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 199, as _ZN9QtWayland18WlShellIntegration17handlePopupClosedEv
namespace QtWayland {
inline void WlShellIntegration::handlePopupClosed()
{
    handlePopupRemoved();
    if (m_shellSurface)
        QObject::disconnect(m_shellSurface->surface(), &QWaylandSurface::hasContentChanged,
                            this, &WlShellIntegration::handleSurfaceHasContentChanged);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 207, as _ZN9QtWayland18WlShellIntegration18handlePopupRemovedEv
namespace QtWayland {
inline void WlShellIntegration::handlePopupRemoved()
{
    if (!m_shellSurface || m_shellSurface->shell()->mappedPopups().isEmpty())
        QWaylandQuickShellEventFilter::cancelFilter();
    isPopup = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 214, as _ZNK9QtWayland18WlShellIntegration16devicePixelRatioEv
namespace QtWayland {
inline qreal WlShellIntegration::devicePixelRatio() const
{
    return m_item->window() ? m_item->window()->devicePixelRatio() : 1;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 269, as _ZN9QtWayland18WlShellIntegration20filterMouseMoveEventEP11QMouseEvent
namespace QtWayland {
inline bool WlShellIntegration::filterMouseMoveEvent(QMouseEvent *event)
{
    if (grabberState == GrabberState::Resize) {
        Q_ASSERT(resizeState.seat == m_item->compositor()->seatFor(event));
        if (!resizeState.initialized) {
            resizeState.initialMousePos = event->scenePosition();
            resizeState.initialized = true;
            return true;
        }
        float scaleFactor = m_item->view()->output()->scaleFactor();
        QPointF delta = (event->scenePosition() - resizeState.initialMousePos) / scaleFactor * devicePixelRatio();
        QSize newSize = m_shellSurface->sizeForResize(resizeState.initialSize, delta, resizeState.resizeEdges);
        m_shellSurface->sendConfigure(newSize, resizeState.resizeEdges);
    } else if (grabberState == GrabberState::Move) {
        Q_ASSERT(moveState.seat == m_item->compositor()->seatFor(event));
        QQuickItem *moveItem = m_item->moveItem();
        if (!moveState.initialized) {
            moveState.initialOffset = moveItem->mapFromItem(nullptr, event->scenePosition());
            moveState.initialized = true;
            return true;
        }
        if (!moveItem->parentItem())
            return true;
        QPointF parentPos = moveItem->parentItem()->mapFromItem(nullptr, event->scenePosition());
        moveItem->setPosition(parentPos - moveState.initialOffset);
    }
    return false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandwlshellintegration.cpp, line 298, as _ZN9QtWayland18WlShellIntegration23filterMouseReleaseEventEP11QMouseEvent
namespace QtWayland {
inline bool WlShellIntegration::filterMouseReleaseEvent(QMouseEvent *event)
{
    Q_UNUSED(event);
    if (grabberState != GrabberState::Default) {
        grabberState = GrabberState::Default;
        return true;
    }
    return false;
}
}  // namespace QtWayland
//  -----------------------------------------------------------------------

//  Only a class built on QtWayland::WlShellIntegration may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWayland_WlShellIntegration : QtWayland::WlShellIntegration {
  using QtWayland::WlShellIntegration::eventFilter;
};

//  A QtWayland::WlShellIntegration that Python can take functions over in. Every QtWayland::WlShellIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_WlShellIntegrationCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtWayland_WlShellIntegrationCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtWayland_WlShellIntegrationCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtWayland_WlShellIntegration : public QtWayland::WlShellIntegration {
public:
  using QtWayland::WlShellIntegration::WlShellIntegration;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
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
  //  bool QtWayland::WlShellIntegration::eventFilter(QObject *object,
  //      QEvent *event)
  bool eventFilter(QObject *object, QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall0 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall0>(taken[0]);
      bool given = call(this, object, event, &handled);
      if (handled) return given;
    }
    return QtWayland::WlShellIntegration::eventFilter(object, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall1 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQtWayland_WlShellIntegrationCall2 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall2>(taken[2]);
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
      CuteQtWayland_WlShellIntegrationCall3 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall3>(taken[3]);
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
      CuteQtWayland_WlShellIntegrationCall4 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall4>(taken[4]);
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
      CuteQtWayland_WlShellIntegrationCall5 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall5>(taken[5]);
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
      CuteQtWayland_WlShellIntegrationCall6 call = reinterpret_cast<CuteQtWayland_WlShellIntegrationCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtWayland::WlShellIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland18WlShellIntegration10metaObjectEv(
    const QtWayland::WlShellIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::WlShellIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland18WlShellIntegration11qt_metacastEPKc(
    QtWayland::WlShellIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::WlShellIntegration::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland18WlShellIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::WlShellIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtWayland::WlShellIntegration::~WlShellIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegrationD1Ev(
    QtWayland::WlShellIntegration *self) {
  delete self;
}

//  bool QtWayland::WlShellIntegration::eventFilter(QObject *object, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::WlShellIntegration *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QtWayland::WlShellIntegration::handleStartMove(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration15handleStartMoveEP12QWaylandSeat(
    QtWayland::WlShellIntegration *self,
    QWaylandSeat *seat) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleStartMove(QWaylandSeat *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleStartMove(QWaylandSeat *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleStartResize(QWaylandSeat *seat,
//      QWaylandWlShellSurface::ResizeEdge edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration17handleStartResizeEP12QWaylandSeatN22QWaylandWlShellSurface10ResizeEdgeE(
    QtWayland::WlShellIntegration *self,
    QWaylandSeat *seat,
    QWaylandWlShellSurface::ResizeEdge edges) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleStartResize(QWaylandSeat *,QWaylandWlShellSurface::ResizeEdge)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleStartResize(QWaylandSeat *,QWaylandWlShellSurface::ResizeEdge)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
      const_cast<void *>(static_cast<const void *>(&edges)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetDefaultTopLevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration24handleSetDefaultTopLevelEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetDefaultTopLevel()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetDefaultTopLevel()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetTransient(QWaylandSurface
//      *parentSurface, const QPoint &relativeToParent, bool inactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration18handleSetTransientEP15QWaylandSurfaceRK6QPointb(
    QtWayland::WlShellIntegration *self,
    QWaylandSurface *parentSurface,
    const QPoint *relativeToParent,
    bool inactive) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetTransient(QWaylandSurface *,const QPoint &,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetTransient(QWaylandSurface *,const QPoint &,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&parentSurface)),
      const_cast<void *>(static_cast<const void *>(relativeToParent)),
      const_cast<void *>(static_cast<const void *>(&inactive)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetMaximized(QWaylandOutput
//      *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration18handleSetMaximizedEP14QWaylandOutput(
    QtWayland::WlShellIntegration *self,
    QWaylandOutput *output) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetMaximized(QWaylandOutput *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetMaximized(QWaylandOutput *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&output)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetFullScreen(QWaylandWlShellSu
//      rface::FullScreenMethod method, uint framerate, QWaylandOutput
//      *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration19handleSetFullScreenEN22QWaylandWlShellSurface16FullScreenMethodEjP14QWaylandOutput(
    QtWayland::WlShellIntegration *self,
    QWaylandWlShellSurface::FullScreenMethod method,
    uint framerate,
    QWaylandOutput *output) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetFullScreen(QWaylandWlShellSurface::FullScreenMethod,uint,QWaylandOutput *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetFullScreen(QWaylandWlShellSurface::FullScreenMethod,uint,QWaylandOutput *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&method)),
      const_cast<void *>(static_cast<const void *>(&framerate)),
      const_cast<void *>(static_cast<const void *>(&output)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSetPopup(QWaylandSeat *seat,
//      QWaylandSurface *parent, const QPoint &relativeToParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration14handleSetPopupEP12QWaylandSeatP15QWaylandSurfaceRK6QPoint(
    QtWayland::WlShellIntegration *self,
    QWaylandSeat *seat,
    QWaylandSurface *parent,
    const QPoint *relativeToParent) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetPopup(QWaylandSeat *,QWaylandSurface *,const QPoint &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetPopup(QWaylandSeat *,QWaylandSurface *,const QPoint &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
      const_cast<void *>(static_cast<const void *>(&parent)),
      const_cast<void *>(static_cast<const void *>(relativeToParent)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleShellSurfaceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration27handleShellSurfaceDestroyedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleShellSurfaceDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleShellSurfaceDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleSurfaceHasContentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration30handleSurfaceHasContentChangedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSurfaceHasContentChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSurfaceHasContentChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleRedraw()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration12handleRedrawEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleRedraw()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleRedraw()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::adjustOffsetForNextFrame(const
//      QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration24adjustOffsetForNextFrameERK7QPointF(
    QtWayland::WlShellIntegration *self,
    const QPointF *offset) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "adjustOffsetForNextFrame(const QPointF &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "adjustOffsetForNextFrame(const QPointF &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(offset)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleFullScreenSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration27handleFullScreenSizeChangedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleFullScreenSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleFullScreenSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handleMaximizedSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration26handleMaximizedSizeChangedEv(
    QtWayland::WlShellIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::WlShellIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleMaximizedSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleMaximizedSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::WlShellIntegration::handlePopupClosed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration17handlePopupClosedEv(
    QtWayland::WlShellIntegration *self) {
  self->handlePopupClosed();
}

//  void QtWayland::WlShellIntegration::handlePopupRemoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland18WlShellIntegration18handlePopupRemovedEv(
    QtWayland::WlShellIntegration *self) {
  self->handlePopupRemoved();
}

//  qreal QtWayland::WlShellIntegration::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QtWayland18WlShellIntegration16devicePixelRatioEv(
    const QtWayland::WlShellIntegration *self) {
  return self->devicePixelRatio();
}

//  bool QtWayland::WlShellIntegration::filterMouseMoveEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland18WlShellIntegration20filterMouseMoveEventEP11QMouseEvent(
    QtWayland::WlShellIntegration *self,
    QMouseEvent *event) {
  return self->filterMouseMoveEvent(event);
}

//  bool QtWayland::WlShellIntegration::filterMouseReleaseEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland18WlShellIntegration23filterMouseReleaseEventEP11QMouseEvent(
    QtWayland::WlShellIntegration *self,
    QMouseEvent *event) {
  return self->filterMouseReleaseEvent(event);
}

//  a Python function taken by a CuteQtWayland_WlShellIntegration, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtWayland_WlShellIntegration(
    QtWayland::WlShellIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtWayland_WlShellIntegration *>(self)->take(key, call);
}

//  bool QtWayland::WlShellIntegration::eventFilter(QObject *object, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland18WlShellIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::WlShellIntegration *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQtWayland_WlShellIntegration *>(self)->OwnQtWayland_WlShellIntegration::eventFilter(
      object,
      event);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
