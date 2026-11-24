//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qqui
//  ckmaterialripple_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2MaterialStyleImpl/QtQuickControls2MaterialStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialripple_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickmaterialripple_p.h"
#include <QtCore/qmath.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#include <QtQuickTemplates2/private/qquickabstractbutton_p.h>
#include <QtQuickTemplates2/private/qquickabstractbutton_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 271, as _ZNK20QQuickMaterialRipple5colorEv
inline QColor QQuickMaterialRipple::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 276, as _ZN20QQuickMaterialRipple8setColorERK6QColor
inline void QQuickMaterialRipple::setColor(const QColor &color)
{
    if (m_color == color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 285, as _ZNK20QQuickMaterialRipple10clipRadiusEv
inline qreal QQuickMaterialRipple::clipRadius() const
{
    return m_clipRadius;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 290, as _ZN20QQuickMaterialRipple13setClipRadiusEd
inline void QQuickMaterialRipple::setClipRadius(qreal radius)
{
    if (qFuzzyCompare(m_clipRadius, radius))
        return;

    m_clipRadius = radius;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 257, as _ZNK20QQuickMaterialRipple8isActiveEv
inline bool QQuickMaterialRipple::isActive() const
{
    return m_active;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 262, as _ZN20QQuickMaterialRipple9setActiveEb
inline void QQuickMaterialRipple::setActive(bool active)
{
    if (active == m_active)
        return;

    m_active = active;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 299, as _ZNK20QQuickMaterialRipple9isPressedEv
inline bool QQuickMaterialRipple::isPressed() const
{
    return m_pressed;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 329, as _ZNK20QQuickMaterialRipple7triggerEv
inline QQuickMaterialRipple::Trigger QQuickMaterialRipple::trigger() const
{
    return m_trigger;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 334, as _ZN20QQuickMaterialRipple10setTriggerENS_7TriggerE
inline void QQuickMaterialRipple::setTrigger(Trigger trigger)
{
    m_trigger = trigger;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 339, as _ZNK20QQuickMaterialRipple11anchorPointEv
inline QPointF QQuickMaterialRipple::anchorPoint() const
{
    const QRectF bounds = boundingRect();
    const QPointF center = bounds.center();
    if (!m_anchor)
        return center;

    QPointF anchorPoint = bounds.center();
    if (QQuickAbstractButton *button = qobject_cast<QQuickAbstractButton *>(m_anchor))
        anchorPoint = QQuickAbstractButtonPrivate::get(button)->pressPoint;
    anchorPoint = mapFromItem(m_anchor, anchorPoint);

    // calculate whether the anchor point is within the ripple circle bounds,
    // that is, whether waves should start expanding from the anchor point
    const qreal r = qSqrt(bounds.width() * bounds.width() + bounds.height() * bounds.height()) / 2;
    if (QLineF(center, anchorPoint).length() < r)
        return anchorPoint;

    // if the anchor point is outside the ripple circle bounds, start expanding
    // from the intersection point of the ripple circle and a line from its center
    // to the the anchor point
    const qreal p = qAtan2(anchorPoint.y() - center.y(), anchorPoint.x() - center.x());
    return QPointF(center.x() + r * qCos(p), center.y() + r * qSin(p));
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 364, as _ZNK20QQuickMaterialRipple6anchorEv
inline QQuickItem *QQuickMaterialRipple::anchor() const
{
    return m_anchor;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 369, as _ZN20QQuickMaterialRipple9setAnchorEP10QQuickItem
inline void QQuickMaterialRipple::setAnchor(QQuickItem *item)
{
    m_anchor = item;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 374, as _ZNK20QQuickMaterialRipple8diameterEv
inline qreal QQuickMaterialRipple::diameter() const
{
    const qreal w = width();
    const qreal h = height();
    return qSqrt(w * w + h * h);
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 381, as _ZN20QQuickMaterialRipple10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickMaterialRipple::itemChange(ItemChange change, const ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 433, as _ZN20QQuickMaterialRipple10timerEventEP11QTimerEvent
inline void QQuickMaterialRipple::timerEvent(QTimerEvent *event)
{
    QQuickItem::timerEvent(event);

    if (event->timerId() == m_enterDelay)
        enterWave();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 447, as _ZN20QQuickMaterialRipple9enterWaveEv
inline void QQuickMaterialRipple::enterWave()
{
    if (m_enterDelay > 0) {
        killTimer(m_enterDelay);
        m_enterDelay = 0;
    }

    ++m_waves;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 458, as _ZN20QQuickMaterialRipple8exitWaveEv
inline void QQuickMaterialRipple::exitWave()
{
    if (m_enterDelay > 0) {
        killTimer(m_enterDelay);
        m_enterDelay = 0;
    }

    if (m_waves > 0) {
        --m_waves;
        update();
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickMaterialRipple may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMaterialRipple : QQuickMaterialRipple {
  using QQuickMaterialRipple::itemChange;
  using QQuickMaterialRipple::timerEvent;
};

//  const QMetaObject *QQuickMaterialRipple::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickMaterialRipple10metaObjectEv(
    const QQuickMaterialRipple *self) {
  return self->metaObject();
}

//  QColor QQuickMaterialRipple::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickMaterialRipple5colorEv(
    const QQuickMaterialRipple *self) {
  return new QColor(self->color());
}

//  void QQuickMaterialRipple::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple8setColorERK6QColor(
    QQuickMaterialRipple *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQuickMaterialRipple::clipRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickMaterialRipple10clipRadiusEv(
    const QQuickMaterialRipple *self) {
  return self->clipRadius();
}

//  void QQuickMaterialRipple::setClipRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple13setClipRadiusEd(
    QQuickMaterialRipple *self,
    qreal radius) {
  self->setClipRadius(radius);
}

//  bool QQuickMaterialRipple::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickMaterialRipple8isActiveEv(
    const QQuickMaterialRipple *self) {
  return self->isActive();
}

//  void QQuickMaterialRipple::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple9setActiveEb(
    QQuickMaterialRipple *self,
    bool active) {
  self->setActive(active);
}

//  bool QQuickMaterialRipple::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickMaterialRipple9isPressedEv(
    const QQuickMaterialRipple *self) {
  return self->isPressed();
}

//  Trigger QQuickMaterialRipple::trigger() const
extern "C" Q_DECL_EXPORT
QQuickMaterialRipple::Trigger ritual_ZNK20QQuickMaterialRipple7triggerEv(
    const QQuickMaterialRipple *self) {
  return self->trigger();
}

//  void QQuickMaterialRipple::setTrigger(Trigger trigger)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple10setTriggerENS_7TriggerE(
    QQuickMaterialRipple *self,
    QQuickMaterialRipple::Trigger trigger) {
  self->setTrigger(trigger);
}

//  QPointF QQuickMaterialRipple::anchorPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK20QQuickMaterialRipple11anchorPointEv(
    const QQuickMaterialRipple *self) {
  return new QPointF(self->anchorPoint());
}

//  QQuickItem *QQuickMaterialRipple::anchor() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickMaterialRipple6anchorEv(
    const QQuickMaterialRipple *self) {
  return self->anchor();
}

//  void QQuickMaterialRipple::setAnchor(QQuickItem *anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple9setAnchorEP10QQuickItem(
    QQuickMaterialRipple *self,
    QQuickItem *anchor) {
  self->setAnchor(anchor);
}

//  qreal QQuickMaterialRipple::diameter() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickMaterialRipple8diameterEv(
    const QQuickMaterialRipple *self) {
  return self->diameter();
}

//  void QQuickMaterialRipple::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialRipple *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickMaterialRipple::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple10timerEventEP11QTimerEvent(
    QQuickMaterialRipple *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQuickMaterialRipple::enterWave()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple9enterWaveEv(
    QQuickMaterialRipple *self) {
  self->enterWave();
}

//  void QQuickMaterialRipple::exitWave()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple8exitWaveEv(QQuickMaterialRipple *self) {
  self->exitWave();
}

//  void QQuickMaterialRipple::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickMaterialRipple10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialRipple *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickMaterialRipple *>(self)->OwnQQuickMaterialRipple::itemChange(
      change,
      *data);
}

//  void QQuickMaterialRipple::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickMaterialRipple10timerEventEP11QTimerEvent(
    QQuickMaterialRipple *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickMaterialRipple *>(self)->OwnQQuickMaterialRipple::timerEvent(
      event);
}
