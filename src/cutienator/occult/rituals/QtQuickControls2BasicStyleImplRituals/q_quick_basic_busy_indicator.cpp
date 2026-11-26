//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasi
//  cbusyindicator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2BasicStyleImpl/QtQuickControls2BasicStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasicbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2BasicStyleImpl/private/qquickbasicbusyindicator_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 13, as local:qquickbasicbusyindicator.cpp:CircleCount
static const int CircleCount = 10;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 14, as local:qquickbasicbusyindicator.cpp:QbbiTotalDuration
static const int QbbiTotalDuration = 100 * CircleCount * 2;

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 22, as local:qquickbasicbusyindicator.cpp:QQuickBasicBusyIndicatorNode
class QQuickBasicBusyIndicatorNode : public QQuickAnimatedNode
{
public:
    QQuickBasicBusyIndicatorNode(QQuickBasicBusyIndicator *item);

    void updateCurrentTime(int time) override;
    void sync(QQuickItem *item) override;

private:
    QColor m_pen;
    QColor m_fill;
};

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 35, as local:qquickbasicbusyindicator.cpp:QQuickBasicBusyIndicatorNode::QQuickBasicBusyIndicatorNode
inline QQuickBasicBusyIndicatorNode::QQuickBasicBusyIndicatorNode(QQuickBasicBusyIndicator *item)
    : QQuickAnimatedNode(item)
{
    setLoopCount(Infinite);
    setDuration(QbbiTotalDuration);
    setCurrentTime(item->elapsed());

    for (int i = 0; i < CircleCount; ++i) {
        QSGTransformNode *transformNode = new QSGTransformNode;
        appendChildNode(transformNode);

        QQuickItemPrivate *d = QQuickItemPrivate::get(item);
        QSGInternalRectangleNode *rectNode = d->sceneGraphContext()->createInternalRectangleNode();
        rectNode->setAntialiasing(true);
        transformNode->appendChildNode(rectNode);
    }
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 161, as _ZN24QQuickBasicBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickBasicBusyIndicator::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
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

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 114, as _ZNK24QQuickBasicBusyIndicator3penEv
inline QColor QQuickBasicBusyIndicator::pen() const
{
    return m_pen;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 119, as _ZN24QQuickBasicBusyIndicator6setPenERK6QColor
inline void QQuickBasicBusyIndicator::setPen(const QColor &pen)
{
    if (pen == m_pen)
        return;

    m_pen = pen;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 128, as _ZNK24QQuickBasicBusyIndicator4fillEv
inline QColor QQuickBasicBusyIndicator::fill() const
{
    return m_fill;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 133, as _ZN24QQuickBasicBusyIndicator7setFillERK6QColor
inline void QQuickBasicBusyIndicator::setFill(const QColor &fill)
{
    if (fill == m_fill)
        return;

    m_fill = fill;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 142, as _ZNK24QQuickBasicBusyIndicator9isRunningEv
inline bool QQuickBasicBusyIndicator::isRunning() const
{
    return isVisible();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 147, as _ZN24QQuickBasicBusyIndicator10setRunningEb
inline void QQuickBasicBusyIndicator::setRunning(bool running)
{
    m_running = running;

    if (m_running)
        setVisible(true);
    // Don't set visible to false if not running, because we use an opacity animation (in QML) to hide ourselves.
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicbusyindicator.cpp, line 156, as _ZNK24QQuickBasicBusyIndicator7elapsedEv
inline int QQuickBasicBusyIndicator::elapsed() const
{
    return m_elapsed;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickBasicBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickBasicBusyIndicator : QQuickBasicBusyIndicator {
  using QQuickBasicBusyIndicator::itemChange;
};

//  const QMetaObject *QQuickBasicBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickBasicBusyIndicator10metaObjectEv(
    const QQuickBasicBusyIndicator *self) {
  return self->metaObject();
}

//  void *QQuickBasicBusyIndicator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickBasicBusyIndicator11qt_metacastEPKc(
    QQuickBasicBusyIndicator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickBasicBusyIndicator::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickBasicBusyIndicator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickBasicBusyIndicator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QColor QQuickBasicBusyIndicator::pen() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24QQuickBasicBusyIndicator3penEv(
    const QQuickBasicBusyIndicator *self) {
  return new QColor(self->pen());
}

//  void QQuickBasicBusyIndicator::setPen(const QColor &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickBasicBusyIndicator6setPenERK6QColor(
    QQuickBasicBusyIndicator *self,
    const QColor *pen) {
  self->setPen(*pen);
}

//  QColor QQuickBasicBusyIndicator::fill() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24QQuickBasicBusyIndicator4fillEv(
    const QQuickBasicBusyIndicator *self) {
  return new QColor(self->fill());
}

//  void QQuickBasicBusyIndicator::setFill(const QColor &fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickBasicBusyIndicator7setFillERK6QColor(
    QQuickBasicBusyIndicator *self,
    const QColor *fill) {
  self->setFill(*fill);
}

//  bool QQuickBasicBusyIndicator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickBasicBusyIndicator9isRunningEv(
    const QQuickBasicBusyIndicator *self) {
  return self->isRunning();
}

//  void QQuickBasicBusyIndicator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickBasicBusyIndicator10setRunningEb(
    QQuickBasicBusyIndicator *self,
    bool running) {
  self->setRunning(running);
}

//  int QQuickBasicBusyIndicator::elapsed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQuickBasicBusyIndicator7elapsedEv(
    const QQuickBasicBusyIndicator *self) {
  return self->elapsed();
}

//  void QQuickBasicBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickBasicBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickBasicBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QSGNode *QQuickBasicBusyIndicator::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN24QQuickBasicBusyIndicator15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickBasicBusyIndicator *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(oldNode, a1);
}

//  void QQuickBasicBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickBasicBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickBasicBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickBasicBusyIndicator *>(self)->OwnQQuickBasicBusyIndicator::itemChange(
      change,
      *data);
}
