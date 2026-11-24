//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdrag_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickdrag_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickdrag_p.h"
#include "qquickdrag_p_p.h"
#include <private/qguiapplication_p.h>
#include <qpa/qplatformintegration.h>
#include <private/qquickitem_p.h>
#include <QtQuick/private/qquickevents_p_p.h>
#include <private/qquickitemchangelistener_p.h>
#include <private/qquickpixmap_p.h>
#include <private/qv4scopedvalue_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qmimedata.h>
#include <QtCore/qstringconverter.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/qevent.h>
#include <QtGui/qstylehints.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qimagewriter.h>
#ifdef Q_OS_ANDROID
#include <QtQuick/QQuickItemGrabResult>
#endif
#include <qpa/qplatformdrag.h>
#include <QtGui/qdrag.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 66, as _ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *, QQuickGeometryChange change,
                                                    const QRectF &)
{
    if (!change.positionChange() || !active || itemMoved)
        return;
    updatePosition();
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 74, as _ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_
inline void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *, QQuickItem *)
{
    if (!active || dragRestarted)
        return;

    QQuickWindow *newWindow = attachedItem->window();

    if (window != newWindow)
        restartDrag();
    else if (window)
        updatePosition();
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 87, as _ZN25QQuickDragAttachedPrivate14updatePositionEv
inline void QQuickDragAttachedPrivate::updatePosition()
{
    Q_Q(QQuickDragAttached);
    itemMoved = true;
    if (!eventQueued) {
        eventQueued = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::User));
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 97, as _ZN25QQuickDragAttachedPrivate11restartDragEv
inline void QQuickDragAttachedPrivate::restartDrag()
{
    Q_Q(QQuickDragAttached);
    dragRestarted = true;
    if (!eventQueued) {
        eventQueued = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::User));
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 107, as _ZN25QQuickDragAttachedPrivate17deliverEnterEventEv
inline void QQuickDragAttachedPrivate::deliverEnterEvent()
{
    dragRestarted = false;
    itemMoved = false;

    window = attachedItem->window();

    mimeData->m_source = source;
    if (!overrideActions)
        mimeData->m_supportedActions = supportedActions;
    mimeData->m_keys = keys;

    if (window) {
        QDragEnterEvent event(attachedItem->mapToScene(hotSpot), mimeData->m_supportedActions,
                              mimeData, Qt::NoButton, Qt::NoModifier);
        QQuickDropEventEx::setProposedAction(&event, proposedAction);
        deliverEvent(window, &event);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 127, as _ZN25QQuickDragAttachedPrivate16deliverMoveEventEv
inline void QQuickDragAttachedPrivate::deliverMoveEvent()
{
    Q_Q(QQuickDragAttached);

    itemMoved = false;
    if (window) {
        QDragMoveEvent event(attachedItem->mapToScene(hotSpot), mimeData->m_supportedActions,
                             mimeData, Qt::NoButton, Qt::NoModifier);
        QQuickDropEventEx::setProposedAction(&event, proposedAction);
        deliverEvent(window, &event);
        if (target != dragGrabber.target()) {
            target = dragGrabber.target();
            emit q->targetChanged();
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 144, as _ZN25QQuickDragAttachedPrivate17deliverLeaveEventEv
inline void QQuickDragAttachedPrivate::deliverLeaveEvent()
{
    if (window) {
        QDragLeaveEvent event;
        deliverEvent(window, &event);
        window = nullptr;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 153, as _ZN25QQuickDragAttachedPrivate12deliverEventEP12QQuickWindowP6QEvent
inline void QQuickDragAttachedPrivate::deliverEvent(QQuickWindow *window, QEvent *event)
{
    Q_ASSERT(!inEvent);
    inEvent = true;
    QQuickWindowPrivate::get(window)->deliveryAgentPrivate()->deliverDragEvent(&dragGrabber, event);
    inEvent = false;
}

//  from ../qtdeclarative/src/quick/items/qquickdrag.cpp, line 859, as _ZN25QQuickDragAttachedPrivate10loadPixmapEv
inline void QQuickDragAttachedPrivate::loadPixmap()
{
    Q_Q(QQuickDragAttached);

    QUrl loadUrl = imageSource;
    const QQmlContext *context = qmlContext(q->parent());
    if (context)
        loadUrl = context->resolvedUrl(imageSource);
    pixmapLoader.load(context ? context->engine() : nullptr, loadUrl, QRect(), q->imageSourceSize());
}
//  -----------------------------------------------------------------------

//  A QQuickDragAttachedPrivate that Python can take functions over in. Every QQuickDragAttachedPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickDragAttachedPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickDragAttachedPrivateCall1)(const void *, QQuickItem *, QQuickItem *, int *);
class CuteQQuickDragAttachedPrivate : public QQuickDragAttachedPrivate {
public:
  using QQuickDragAttachedPrivate::QQuickDragAttachedPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDragAttachedPrivateCall0 call = reinterpret_cast<CuteQQuickDragAttachedPrivateCall0>(taken[0]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickDragAttachedPrivate::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *parent)
  void itemParentChanged(QQuickItem *a0, QQuickItem *parent) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDragAttachedPrivateCall1 call = reinterpret_cast<CuteQQuickDragAttachedPrivateCall1>(taken[1]);
      call(this, a0, parent, &handled);
      if (handled) return;
    }
    QQuickDragAttachedPrivate::itemParentChanged(a0, parent);
  }
};

//  QQuickDragAttached *QQuickDragAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDragAttached *ritual_ZN25QQuickDragAttachedPrivate6q_funcEv(
    QQuickDragAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickDragAttached *QQuickDragAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDragAttached *ritual_ZNK25QQuickDragAttachedPrivate6q_funcEv(
    const QQuickDragAttachedPrivate *self) {
  return self->q_func();
}

//  void QQuickDragAttachedPrivate::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate22qt_qmlMarker_anonymousEv(
    QQuickDragAttachedPrivate *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickDragAttachedPrivate
//      *QQuickDragAttachedPrivate::get(QQuickDragAttached *attached)
extern "C" Q_DECL_EXPORT
QQuickDragAttachedPrivate *ritual_ZN25QQuickDragAttachedPrivate3getEP18QQuickDragAttached(
    QQuickDragAttached *attached) {
  return QQuickDragAttachedPrivate::get(attached);
}

//  QQuickDragAttachedPrivate::QQuickDragAttachedPrivate()
extern "C" Q_DECL_EXPORT
QQuickDragAttachedPrivate *ritual_ZN25QQuickDragAttachedPrivateC1Ev() {
  return new CuteQQuickDragAttachedPrivate();
}

//  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    QQuickItem *parent) {
  self->itemParentChanged(a0, parent);
}

//  void QQuickDragAttachedPrivate::updatePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate14updatePositionEv(
    QQuickDragAttachedPrivate *self) {
  self->updatePosition();
}

//  void QQuickDragAttachedPrivate::restartDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate11restartDragEv(
    QQuickDragAttachedPrivate *self) {
  self->restartDrag();
}

//  void QQuickDragAttachedPrivate::deliverEnterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate17deliverEnterEventEv(
    QQuickDragAttachedPrivate *self) {
  self->deliverEnterEvent();
}

//  void QQuickDragAttachedPrivate::deliverMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate16deliverMoveEventEv(
    QQuickDragAttachedPrivate *self) {
  self->deliverMoveEvent();
}

//  void QQuickDragAttachedPrivate::deliverLeaveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate17deliverLeaveEventEv(
    QQuickDragAttachedPrivate *self) {
  self->deliverLeaveEvent();
}

//  void QQuickDragAttachedPrivate::deliverEvent(QQuickWindow *window, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate12deliverEventEP12QQuickWindowP6QEvent(
    QQuickDragAttachedPrivate *self,
    QQuickWindow *window,
    QEvent *event) {
  self->deliverEvent(window, event);
}

//  void QQuickDragAttachedPrivate::loadPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickDragAttachedPrivate10loadPixmapEv(
    QQuickDragAttachedPrivate *self) {
  self->loadPixmap();
}

//  a Python function taken by a CuteQQuickDragAttachedPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDragAttachedPrivate(
    QQuickDragAttachedPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDragAttachedPrivate *>(self)->take(key, call);
}

//  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickDragAttachedPrivate::itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickDragAttachedPrivate *self,
    QQuickItem *a0,
    QQuickItem *parent) {
  self->QQuickDragAttachedPrivate::itemParentChanged(a0, parent);
}
