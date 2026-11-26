//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qqui
//  ckmaterialbusyindicator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2MaterialStyleImpl/QtQuickControls2MaterialStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/private/qquickmaterialbusyindicator_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
#include <QtGui/qpainter.h>
#include <QtQuick/qsgimagenode.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 30, as local:qquickmaterialbusyindicator.cpp:SpanAnimationDuration
static const int SpanAnimationDuration = 700;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 31, as local:qquickmaterialbusyindicator.cpp:RotationAnimationDuration
static const int RotationAnimationDuration = SpanAnimationDuration * 6;

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 37, as local:qquickmaterialbusyindicator.cpp:QQuickMaterialBusyIndicatorNode
class QQuickMaterialBusyIndicatorNode : public QQuickAnimatedNode
{
public:
    QQuickMaterialBusyIndicatorNode(QQuickMaterialBusyIndicator *item);

    void sync(QQuickItem *item) override;

protected:
    void updateCurrentTime(int time) override;

private:
    int m_lastStartAngle = 0;
    int m_lastEndAngle = 0;
    qreal m_width = 0;
    qreal m_height = 0;
    qreal m_devicePixelRatio = 1;
    QColor m_color;
};

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 56, as local:qquickmaterialbusyindicator.cpp:QQuickMaterialBusyIndicatorNode::QQuickMaterialBusyIndicatorNode
inline QQuickMaterialBusyIndicatorNode::QQuickMaterialBusyIndicatorNode(QQuickMaterialBusyIndicator *item)
    : QQuickAnimatedNode(item)
{
    setLoopCount(Infinite);
    setCurrentTime(item->elapsed());
    setDuration(RotationAnimationDuration);

    QSGImageNode *textureNode = item->window()->createImageNode();
    textureNode->setOwnsTexture(true);
    appendChildNode(textureNode);

    // A texture seems to be required here, but we don't have one yet, as we haven't drawn anything,
    // so just use a blank image.
    QImage blankImage(item->width(), item->height(), QImage::Format_ARGB32_Premultiplied);
    blankImage.fill(Qt::transparent);
    textureNode->setTexture(item->window()->createTextureFromImage(blankImage));
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 135, as local:qquickmaterialbusyindicator.cpp:QQuickMaterialBusyIndicatorNode::sync
inline void QQuickMaterialBusyIndicatorNode::sync(QQuickItem *item)
{
    QQuickMaterialBusyIndicator *indicator = static_cast<QQuickMaterialBusyIndicator *>(item);
    m_color = indicator->color();
    m_width = indicator->width();
    m_height = indicator->height();
    m_devicePixelRatio = indicator->window()->effectiveDevicePixelRatio();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 183, as _ZN27QQuickMaterialBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickMaterialBusyIndicator::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    switch (change) {
    case ItemOpacityHasChanged:
        // If running is set to false and then true within a short period (QTBUG-85860), our
        // OpacityAnimator cancels the 1 => 0 animation (which was for running being set to false),
        // setting opacity to 0 and hence visible to false. This happens _after_ setRunning(true)
        // was called, because the properties were set synchronously but the animation is
        // asynchronous. To account for this situation, we only hide ourselves if we're not running.
        if (qFuzzyIsNull(data.realValue) && !m_running)
            setVisible(false);
        break;
    case ItemVisibleHasChanged:
        update();
        break;
    default:
        break;
    }
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 150, as _ZNK27QQuickMaterialBusyIndicator5colorEv
inline QColor QQuickMaterialBusyIndicator::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 155, as _ZN27QQuickMaterialBusyIndicator8setColorERK6QColor
inline void QQuickMaterialBusyIndicator::setColor(const QColor &color)
{
    if (m_color == color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 164, as _ZNK27QQuickMaterialBusyIndicator9isRunningEv
inline bool QQuickMaterialBusyIndicator::isRunning() const
{
    return m_running;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 169, as _ZN27QQuickMaterialBusyIndicator10setRunningEb
inline void QQuickMaterialBusyIndicator::setRunning(bool running)
{
    m_running = running;

    if (m_running)
        setVisible(true);
    // Don't set visible to false if not running, because we use an opacity animation (in QML) to hide ourselves.
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialbusyindicator.cpp, line 178, as _ZNK27QQuickMaterialBusyIndicator7elapsedEv
inline int QQuickMaterialBusyIndicator::elapsed() const
{
    return m_elapsed;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickMaterialBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMaterialBusyIndicator : QQuickMaterialBusyIndicator {
  using QQuickMaterialBusyIndicator::itemChange;
};

//  const QMetaObject *QQuickMaterialBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickMaterialBusyIndicator10metaObjectEv(
    const QQuickMaterialBusyIndicator *self) {
  return self->metaObject();
}

//  void *QQuickMaterialBusyIndicator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QQuickMaterialBusyIndicator11qt_metacastEPKc(
    QQuickMaterialBusyIndicator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickMaterialBusyIndicator::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QQuickMaterialBusyIndicator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickMaterialBusyIndicator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QColor QQuickMaterialBusyIndicator::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK27QQuickMaterialBusyIndicator5colorEv(
    const QQuickMaterialBusyIndicator *self) {
  return new QColor(self->color());
}

//  void QQuickMaterialBusyIndicator::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialBusyIndicator8setColorERK6QColor(
    QQuickMaterialBusyIndicator *self,
    const QColor *color) {
  self->setColor(*color);
}

//  bool QQuickMaterialBusyIndicator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickMaterialBusyIndicator9isRunningEv(
    const QQuickMaterialBusyIndicator *self) {
  return self->isRunning();
}

//  void QQuickMaterialBusyIndicator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialBusyIndicator10setRunningEb(
    QQuickMaterialBusyIndicator *self,
    bool running) {
  self->setRunning(running);
}

//  int QQuickMaterialBusyIndicator::elapsed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuickMaterialBusyIndicator7elapsedEv(
    const QQuickMaterialBusyIndicator *self) {
  return self->elapsed();
}

//  void QQuickMaterialBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickMaterialBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QSGNode *QQuickMaterialBusyIndicator::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN27QQuickMaterialBusyIndicator15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickMaterialBusyIndicator *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void QQuickMaterialBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickMaterialBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickMaterialBusyIndicator *>(self)->OwnQQuickMaterialBusyIndicator::itemChange(
      change,
      *data);
}
