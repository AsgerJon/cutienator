//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qq
//  uickuniversalbusyindicator_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2UniversalStyleImpl/QtQuickControls2UniversalStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qquickuniversalbusyindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickuniversalbusyindicator_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
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

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 162, as _ZNK28QQuickUniversalBusyIndicator5countEv
inline int QQuickUniversalBusyIndicator::count() const
{
    return m_count;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 167, as _ZN28QQuickUniversalBusyIndicator8setCountEi
inline void QQuickUniversalBusyIndicator::setCount(int count)
{
    if (m_count == count)
        return;

    m_count = count;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 176, as _ZNK28QQuickUniversalBusyIndicator5colorEv
inline QColor QQuickUniversalBusyIndicator::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 181, as _ZN28QQuickUniversalBusyIndicator8setColorERK6QColor
inline void QQuickUniversalBusyIndicator::setColor(const QColor &color)
{
    if (m_color == color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 190, as _ZNK28QQuickUniversalBusyIndicator7elapsedEv
inline int QQuickUniversalBusyIndicator::elapsed() const
{
    return m_elapsed;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalbusyindicator.cpp, line 195, as _ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickUniversalBusyIndicator::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    if (change == ItemVisibleHasChanged)
        update();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickUniversalBusyIndicator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickUniversalBusyIndicator : QQuickUniversalBusyIndicator {
  using QQuickUniversalBusyIndicator::itemChange;
};

//  const QMetaObject *QQuickUniversalBusyIndicator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickUniversalBusyIndicator10metaObjectEv(
    const QQuickUniversalBusyIndicator *self) {
  return self->metaObject();
}

//  int QQuickUniversalBusyIndicator::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickUniversalBusyIndicator5countEv(
    const QQuickUniversalBusyIndicator *self) {
  return self->count();
}

//  void QQuickUniversalBusyIndicator::setCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUniversalBusyIndicator8setCountEi(
    QQuickUniversalBusyIndicator *self,
    int count) {
  self->setCount(count);
}

//  QColor QQuickUniversalBusyIndicator::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK28QQuickUniversalBusyIndicator5colorEv(
    const QQuickUniversalBusyIndicator *self) {
  return new QColor(self->color());
}

//  void QQuickUniversalBusyIndicator::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUniversalBusyIndicator8setColorERK6QColor(
    QQuickUniversalBusyIndicator *self,
    const QColor *color) {
  self->setColor(*color);
}

//  int QQuickUniversalBusyIndicator::elapsed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickUniversalBusyIndicator7elapsedEv(
    const QQuickUniversalBusyIndicator *self) {
  return self->elapsed();
}

//  void QQuickUniversalBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickUniversalBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickUniversalBusyIndicator::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickUniversalBusyIndicator *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickUniversalBusyIndicator *>(self)->OwnQQuickUniversalBusyIndicator::itemChange(
      change,
      *data);
}
