//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfu
//  sionbusyindicator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2FusionStyleImpl/QtQuickControls2FusionStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfusionbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FusionStyleImpl/private/qquickfusionbusyindicator_p.h>
#include <QtGui/qpainter.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 16, as _ZNK25QQuickFusionBusyIndicator5colorEv
inline QColor QQuickFusionBusyIndicator::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 21, as _ZN25QQuickFusionBusyIndicator8setColorERK6QColor
inline void QQuickFusionBusyIndicator::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 30, as _ZNK25QQuickFusionBusyIndicator9isRunningEv
inline bool QQuickFusionBusyIndicator::isRunning() const
{
    return isVisible();
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 35, as _ZN25QQuickFusionBusyIndicator10setRunningEb
inline void QQuickFusionBusyIndicator::setRunning(bool running)
{
    m_running = running;

    if (m_running) {
        setVisible(true);
        update();
    }
    // Don't set visible to false if not running, because we use an opacity animation (in QML) to hide ourselves.
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 46, as _ZN25QQuickFusionBusyIndicator5paintEP8QPainter
inline void QQuickFusionBusyIndicator::paint(QPainter *painter)
{
    const qreal w = width();
    const qreal h = height();
    if (w <= 0 || h <= 0 || !isRunning())
        return;

    const qreal sz = qMin(w, h);
    const qreal dx = (w - sz) / 2;
    const qreal dy = (h - sz) / 2;
    const int hpw = qRound(qMax(qreal(1), sz / 14)) & -1;
    const int pw = 2 * hpw;
    const QRectF bounds(dx + hpw, dy + hpw, sz - pw - 1, sz - pw - 1);

    QConicalGradient gradient;
    gradient.setCenter(QPointF(dx + sz / 2, dy + sz / 2));
    gradient.setColorAt(0, m_color);
    gradient.setColorAt(0.1, m_color);
    gradient.setColorAt(1, Qt::transparent);

    painter->translate(0.5, 0.5);
    painter->setRenderHint(QPainter::Antialiasing, true);
    painter->setPen(QPen(gradient, pw, Qt::SolidLine));
    painter->drawArc(bounds, 0, 360 * 16);
    painter->setPen(QPen(m_color, pw, Qt::SolidLine, Qt::RoundCap));
    painter->drawArc(bounds, 0, 20 * 16);
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusionbusyindicator.cpp, line 74, as _ZN25QQuickFusionBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickFusionBusyIndicator::itemChange(ItemChange change, const ItemChangeData &data)
{
    QQuickPaintedItem::itemChange(change, data);

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
//  -----------------------------------------------------------------------

//  Only a class built on QQuickFusionBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFusionBusyIndicator : QQuickFusionBusyIndicator {
  using QQuickFusionBusyIndicator::itemChange;
};

//  const QMetaObject *QQuickFusionBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickFusionBusyIndicator10metaObjectEv(
    const QQuickFusionBusyIndicator *self) {
  return self->metaObject();
}

//  QColor QQuickFusionBusyIndicator::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickFusionBusyIndicator5colorEv(
    const QQuickFusionBusyIndicator *self) {
  return new QColor(self->color());
}

//  void QQuickFusionBusyIndicator::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator8setColorERK6QColor(
    QQuickFusionBusyIndicator *self,
    const QColor *color) {
  self->setColor(*color);
}

//  bool QQuickFusionBusyIndicator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickFusionBusyIndicator9isRunningEv(
    const QQuickFusionBusyIndicator *self) {
  return self->isRunning();
}

//  void QQuickFusionBusyIndicator::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator10setRunningEb(
    QQuickFusionBusyIndicator *self,
    bool running) {
  self->setRunning(running);
}

//  void QQuickFusionBusyIndicator::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator5paintEP8QPainter(
    QQuickFusionBusyIndicator *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickFusionBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickFusionBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFusionBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickFusionBusyIndicator::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFusionBusyIndicator5paintEP8QPainter(
    QQuickFusionBusyIndicator *self,
    QPainter *painter) {
  self->QQuickFusionBusyIndicator::paint(painter);
}

//  void QQuickFusionBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickFusionBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFusionBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickFusionBusyIndicator *>(self)->OwnQQuickFusionBusyIndicator::itemChange(
      change,
      *data);
}
