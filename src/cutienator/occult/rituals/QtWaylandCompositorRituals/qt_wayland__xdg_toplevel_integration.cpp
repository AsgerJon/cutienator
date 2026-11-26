//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h>
#include <QtWaylandCompositor/QWaylandXdgSurface>
#include <QtWaylandCompositor/QWaylandCompositor>
#include <QtWaylandCompositor/QWaylandSeat>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 15, as local:qwaylandxdgshellintegration.cpp:handlePopupCreated
namespace QtWayland {
static void handlePopupCreated(QWaylandQuickShellSurfaceItem *parentItem, QWaylandXdgPopup *popup)
{
    if (parentItem->shellSurface() == popup->parentXdgSurface())
        QWaylandQuickShellSurfaceItemPrivate::get(parentItem)->maybeCreateAutoPopup(popup->xdgSurface());
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 117, as _ZN9QtWayland22XdgToplevelIntegration15handleStartMoveEP12QWaylandSeat
namespace QtWayland {
inline void XdgToplevelIntegration::handleStartMove(QWaylandSeat *seat)
{
    grabberState = GrabberState::Move;
    moveState.seat = seat;
    moveState.initialized = false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 48, as _ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObjectP6QEvent
namespace QtWayland {
inline bool XdgToplevelIntegration::eventFilter(QObject *object, QEvent *event)
{
    if (event->type() == QEvent::MouseMove) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
        return filterMouseMoveEvent(mouseEvent);
    } else if (event->type() == QEvent::MouseButtonRelease || event->type() == QEvent::TouchEnd || event->type() == QEvent::TouchCancel) {
        return filterPointerReleaseEvent();
    } else if (event->type() == QEvent::TouchUpdate) {
        QTouchEvent *touchEvent = static_cast<QTouchEvent *>(event);
        return filterTouchUpdateEvent(touchEvent);
    }
    return QWaylandQuickShellIntegration::eventFilter(object, event);
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 62, as _ZN9QtWayland22XdgToplevelIntegration22filterPointerMoveEventERK7QPointF
namespace QtWayland {
inline bool XdgToplevelIntegration::filterPointerMoveEvent(const QPointF &scenePosition)
{
    if (grabberState == GrabberState::Resize) {
        if (!resizeState.initialized) {
            resizeState.initialMousePos = scenePosition;
            resizeState.initialized = true;
            return true;
        }
        QPointF delta = m_item->mapToSurface(scenePosition - resizeState.initialMousePos);
        QSize newSize = m_toplevel->sizeForResize(resizeState.initialWindowSize, delta, resizeState.resizeEdges);
        m_toplevel->sendResizing(newSize);
    } else if (grabberState == GrabberState::Move) {
        QQuickItem *moveItem = m_item->moveItem();
        if (!moveState.initialized) {
            moveState.initialOffset = moveItem->mapFromItem(nullptr, scenePosition);
            moveState.initialized = true;
            return true;
        }
        if (!moveItem->parentItem())
            return true;
        QPointF parentPos = moveItem->parentItem()->mapFromItem(nullptr, scenePosition);
        moveItem->setPosition(parentPos - moveState.initialOffset);
    }
    return false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 100, as _ZN9QtWayland22XdgToplevelIntegration20filterMouseMoveEventEP11QMouseEvent
namespace QtWayland {
inline bool XdgToplevelIntegration::filterMouseMoveEvent(QMouseEvent *event)
{
    Q_ASSERT(grabberState != GrabberState::Move || moveState.seat == m_item->compositor()->seatFor(event));
    Q_ASSERT(grabberState != GrabberState::Resize || resizeState.seat == m_item->compositor()->seatFor(event));

    return filterPointerMoveEvent(event->scenePosition());
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 108, as _ZN9QtWayland22XdgToplevelIntegration25filterPointerReleaseEventEv
namespace QtWayland {
inline bool XdgToplevelIntegration::filterPointerReleaseEvent()
{
    if (grabberState != GrabberState::Default) {
        grabberState = GrabberState::Default;
        return true;
    }
    return false;
}
}  // namespace QtWayland

//  from ../qtwayland/src/compositor/extensions/qwaylandxdgshellintegration.cpp, line 88, as _ZN9QtWayland22XdgToplevelIntegration22filterTouchUpdateEventEP11QTouchEvent
namespace QtWayland {
inline bool XdgToplevelIntegration::filterTouchUpdateEvent(QTouchEvent *event)
{
    if (event->pointCount() == 0)
        return false;

    Q_ASSERT(grabberState != GrabberState::Move || moveState.seat == m_item->compositor()->seatFor(event));
    Q_ASSERT(grabberState != GrabberState::Resize || resizeState.seat == m_item->compositor()->seatFor(event));

    QEventPoint point = event->points().first();
    return filterPointerMoveEvent(point.scenePosition());
 }
}  // namespace QtWayland
//  -----------------------------------------------------------------------

//  Only a class built on QtWayland::XdgToplevelIntegration may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtWayland_XdgToplevelIntegration : QtWayland::XdgToplevelIntegration {
  using QtWayland::XdgToplevelIntegration::eventFilter;
};

//  const QMetaObject *QtWayland::XdgToplevelIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland22XdgToplevelIntegration10metaObjectEv(
    const QtWayland::XdgToplevelIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::XdgToplevelIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland22XdgToplevelIntegration11qt_metacastEPKc(
    QtWayland::XdgToplevelIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::XdgToplevelIntegration::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland22XdgToplevelIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::XdgToplevelIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool QtWayland::XdgToplevelIntegration::eventFilter(QObject *object,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::XdgToplevelIntegration *self,
    QObject *object,
    QEvent *event) {
  return self->eventFilter(object, event);
}

//  void QtWayland::XdgToplevelIntegration::handleStartMove(QWaylandSeat
//      *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration15handleStartMoveEP12QWaylandSeat(
    QtWayland::XdgToplevelIntegration *self,
    QWaylandSeat *seat) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
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

//  void QtWayland::XdgToplevelIntegration::handleStartResize(QWaylandSeat
//      *seat, Qt::Edges edges)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration17handleStartResizeEP12QWaylandSeat6QFlagsIN2Qt4EdgeEE(
    QtWayland::XdgToplevelIntegration *self,
    QWaylandSeat *seat,
    int edges) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleStartResize(QWaylandSeat *,Qt::Edges)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleStartResize(QWaylandSeat *,Qt::Edges)");
  Qt::Edges value1 = QFlags<Qt::Edge>::fromInt(edges);
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&seat)),
      const_cast<void *>(static_cast<const void *>(&value1)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleSetMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration18handleSetMaximizedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetMaximized()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetMaximized()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleUnsetMaximized()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration20handleUnsetMaximizedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleUnsetMaximized()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleUnsetMaximized()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleMaximizedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration22handleMaximizedChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleMaximizedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleMaximizedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleSetFullscreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration19handleSetFullscreenEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSetFullscreen()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSetFullscreen()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleUnsetFullscreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration21handleUnsetFullscreenEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleUnsetFullscreen()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleUnsetFullscreen()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleFullscreenChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration23handleFullscreenChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleFullscreenChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleFullscreenChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleActivatedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration22handleActivatedChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleActivatedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleActivatedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleSurfaceSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration24handleSurfaceSizeChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleSurfaceSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleSurfaceSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleToplevelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration23handleToplevelDestroyedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleToplevelDestroyed()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleToplevelDestroyed()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtWayland::XdgToplevelIntegration::handleMaximizedSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration26handleMaximizedSizeChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
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

//  void QtWayland::XdgToplevelIntegration::handleFullscreenSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland22XdgToplevelIntegration27handleFullscreenSizeChangedEv(
    QtWayland::XdgToplevelIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgToplevelIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleFullscreenSizeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleFullscreenSizeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QtWayland::XdgToplevelIntegration::filterPointerMoveEvent(const
//      QPointF &scenePosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration22filterPointerMoveEventERK7QPointF(
    QtWayland::XdgToplevelIntegration *self,
    const QPointF *scenePosition) {
  return self->filterPointerMoveEvent(*scenePosition);
}

//  bool QtWayland::XdgToplevelIntegration::filterMouseMoveEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration20filterMouseMoveEventEP11QMouseEvent(
    QtWayland::XdgToplevelIntegration *self,
    QMouseEvent *event) {
  return self->filterMouseMoveEvent(event);
}

//  bool QtWayland::XdgToplevelIntegration::filterPointerReleaseEvent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration25filterPointerReleaseEventEv(
    QtWayland::XdgToplevelIntegration *self) {
  return self->filterPointerReleaseEvent();
}

//  bool
//      QtWayland::XdgToplevelIntegration::filterTouchUpdateEvent(QTouchEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtWayland22XdgToplevelIntegration22filterTouchUpdateEventEP11QTouchEvent(
    QtWayland::XdgToplevelIntegration *self,
    QTouchEvent *event) {
  return self->filterTouchUpdateEvent(event);
}

//  bool QtWayland::XdgToplevelIntegration::eventFilter(QObject *object,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QtWayland22XdgToplevelIntegration11eventFilterEP7QObjectP6QEvent(
    QtWayland::XdgToplevelIntegration *self,
    QObject *object,
    QEvent *event) {
  return static_cast<OwnQtWayland_XdgToplevelIntegration *>(self)->OwnQtWayland_XdgToplevelIntegration::eventFilter(
      object,
      event);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
