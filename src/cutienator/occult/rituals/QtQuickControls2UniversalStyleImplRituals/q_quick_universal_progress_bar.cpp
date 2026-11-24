//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qq
//  uickuniversalprogressbar_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2UniversalStyleImpl/QtQuickControls2UniversalStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qquickuniversalprogressbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickuniversalprogressbar_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/qsgrectanglenode.h>
#include <QtQuickControls2Impl/private/qquickanimatednode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 242, as _ZNK26QQuickUniversalProgressBar5colorEv
inline QColor QQuickUniversalProgressBar::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 247, as _ZN26QQuickUniversalProgressBar8setColorERK6QColor
inline void QQuickUniversalProgressBar::setColor(const QColor &color)
{
    if (m_color == color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 256, as _ZNK26QQuickUniversalProgressBar8progressEv
inline qreal QQuickUniversalProgressBar::progress() const
{
    return m_progress;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 261, as _ZN26QQuickUniversalProgressBar11setProgressEd
inline void QQuickUniversalProgressBar::setProgress(qreal progress)
{
    if (progress == m_progress)
        return;

    m_progress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 270, as _ZNK26QQuickUniversalProgressBar15isIndeterminateEv
inline bool QQuickUniversalProgressBar::isIndeterminate() const
{
    return m_indeterminate;
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 275, as _ZN26QQuickUniversalProgressBar16setIndeterminateEb
inline void QQuickUniversalProgressBar::setIndeterminate(bool indeterminate)
{
    if (indeterminate == m_indeterminate)
        return;

    m_indeterminate = indeterminate;
    setClip(m_indeterminate);
    update();
}

//  from ../qtdeclarative/src/quickcontrols/universal/impl/qquickuniversalprogressbar.cpp, line 285, as _ZN26QQuickUniversalProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickUniversalProgressBar::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    if (change == ItemVisibleHasChanged)
        update();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickUniversalProgressBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickUniversalProgressBar : QQuickUniversalProgressBar {
  using QQuickUniversalProgressBar::itemChange;
};

//  const QMetaObject *QQuickUniversalProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickUniversalProgressBar10metaObjectEv(
    const QQuickUniversalProgressBar *self) {
  return self->metaObject();
}

//  QColor QQuickUniversalProgressBar::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QQuickUniversalProgressBar5colorEv(
    const QQuickUniversalProgressBar *self) {
  return new QColor(self->color());
}

//  void QQuickUniversalProgressBar::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickUniversalProgressBar8setColorERK6QColor(
    QQuickUniversalProgressBar *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQuickUniversalProgressBar::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QQuickUniversalProgressBar8progressEv(
    const QQuickUniversalProgressBar *self) {
  return self->progress();
}

//  void QQuickUniversalProgressBar::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickUniversalProgressBar11setProgressEd(
    QQuickUniversalProgressBar *self,
    qreal progress) {
  self->setProgress(progress);
}

//  bool QQuickUniversalProgressBar::isIndeterminate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickUniversalProgressBar15isIndeterminateEv(
    const QQuickUniversalProgressBar *self) {
  return self->isIndeterminate();
}

//  void QQuickUniversalProgressBar::setIndeterminate(bool indeterminate)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickUniversalProgressBar16setIndeterminateEb(
    QQuickUniversalProgressBar *self,
    bool indeterminate) {
  self->setIndeterminate(indeterminate);
}

//  void QQuickUniversalProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickUniversalProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickUniversalProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickUniversalProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickUniversalProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickUniversalProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickUniversalProgressBar *>(self)->OwnQQuickUniversalProgressBar::itemChange(
      change,
      *data);
}
