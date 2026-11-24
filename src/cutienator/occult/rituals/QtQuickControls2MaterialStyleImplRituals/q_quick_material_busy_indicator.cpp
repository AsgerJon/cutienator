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
#include "qquickmaterialbusyindicator_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
#include <QtGui/qpainter.h>
#include <QtQuick/qsgimagenode.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
