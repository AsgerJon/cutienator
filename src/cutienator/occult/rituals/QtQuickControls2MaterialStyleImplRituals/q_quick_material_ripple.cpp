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
#include <QtQuickControls2MaterialStyleImpl/private/qquickmaterialripple_p.h>
#include <QtCore/qmath.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#include <QtQuickTemplates2/private/qquickabstractbutton_p.h>
#include <QtQuickTemplates2/private/qquickabstractbutton_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 18, as local:qquickmaterialripple.cpp:RIPPLE_ENTER_DELAY
static const int RIPPLE_ENTER_DELAY = 80;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 19, as local:qquickmaterialripple.cpp:OPACITY_ENTER_DURATION_FAST
static const int OPACITY_ENTER_DURATION_FAST = 120;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 146, as local:qquickmaterialripple.cpp:QQuickMaterialRippleBackgroundNode
class QQuickMaterialRippleBackgroundNode : public QQuickAnimatedNode
{
    Q_OBJECT

public:
    QQuickMaterialRippleBackgroundNode(QQuickMaterialRipple *ripple);

    void updateCurrentTime(int time) override;
    void sync(QQuickItem *item) override;

private:
    void updateBackgroundNode();

    bool m_active = false;

    qreal m_opacity = 0.0;
    qreal m_newOpacity = 0.0;

    QQuickWindow *m_window = nullptr;
    QMetaObject::Connection m_animationConnection;
};

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 168, as local:qquickmaterialripple.cpp:QQuickMaterialRippleBackgroundNode::QQuickMaterialRippleBackgroundNode
inline QQuickMaterialRippleBackgroundNode::QQuickMaterialRippleBackgroundNode(QQuickMaterialRipple *ripple)
    : QQuickAnimatedNode(ripple)
{
    setDuration(OPACITY_ENTER_DURATION_FAST);

    QSGOpacityNode *opacityNode = new QSGOpacityNode;
    opacityNode->setOpacity(0.0);
    appendChildNode(opacityNode);

    QQuickItemPrivate *d = QQuickItemPrivate::get(ripple);
    QSGInternalRectangleNode *rectNode = d->sceneGraphContext()->createInternalRectangleNode();
    rectNode->setAntialiasing(true);
    opacityNode->appendChildNode(rectNode);

    m_window = ripple->window();
    connect(this, &QQuickAnimatedNode::started, this, [this]() {
        this->m_animationConnection = connect(
            this->m_window,
            &QQuickWindow::beforeFrameBegin,
            this,
            &QQuickMaterialRippleBackgroundNode::updateBackgroundNode,
            Qt::DirectConnection);
    });
    connect(this, &QQuickAnimatedNode::stopped,
            this, [this]() { disconnect(this->m_animationConnection); });
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 195, as local:qquickmaterialripple.cpp:QQuickMaterialRippleBackgroundNode::updateCurrentTime
inline void QQuickMaterialRippleBackgroundNode::updateCurrentTime(int time)
{
    qreal opacity = time / static_cast<qreal>(duration());
    if (!m_active)
        opacity = 1.0 - opacity;

    QSGOpacityNode *opacityNode = static_cast<QSGOpacityNode *>(firstChild());
    Q_ASSERT(opacityNode->type() == QSGNode::OpacityNodeType);
    m_newOpacity = opacity;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 240, as local:qquickmaterialripple.cpp:QQuickMaterialRippleBackgroundNode::updateBackgroundNode
inline void QQuickMaterialRippleBackgroundNode::updateBackgroundNode()
{
    if (m_opacity == m_newOpacity)
        return;

    m_opacity = m_newOpacity;
    QSGOpacityNode *opacityNode = static_cast<QSGOpacityNode *>(firstChild());
    Q_ASSERT(opacityNode->type() == QSGNode::OpacityNodeType);
    opacityNode->setOpacity(m_opacity);
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

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 304, as _ZN20QQuickMaterialRipple10setPressedEb
inline void QQuickMaterialRipple::setPressed(bool pressed)
{
    if (pressed == m_pressed)
        return;

    m_pressed = pressed;

    if (!isEnabled()) {
        exitWave();
        return;
    }

    if (pressed) {
        if (m_trigger == Press)
            prepareWave();
        else
            exitWave();
    } else {
        if (m_trigger == Release)
            enterWave();
        else
            exitWave();
    }
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

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialripple.cpp, line 441, as _ZN20QQuickMaterialRipple11prepareWaveEv
inline void QQuickMaterialRipple::prepareWave()
{
    if (m_enterDelay <= 0)
        m_enterDelay = startTimer(RIPPLE_ENTER_DELAY);
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

//  void *QQuickMaterialRipple::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickMaterialRipple11qt_metacastEPKc(
    QQuickMaterialRipple *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMaterialRipple::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickMaterialRipple11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMaterialRipple *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QQuickMaterialRipple::setPressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple10setPressedEb(
    QQuickMaterialRipple *self,
    bool pressed) {
  self->setPressed(pressed);
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

//  QSGNode *QQuickMaterialRipple::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN20QQuickMaterialRipple15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMaterialRipple *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void QQuickMaterialRipple::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple10timerEventEP11QTimerEvent(
    QQuickMaterialRipple *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QQuickMaterialRipple::prepareWave()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMaterialRipple11prepareWaveEv(
    QQuickMaterialRipple *self) {
  self->prepareWave();
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
