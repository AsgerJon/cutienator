//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qqui
//  ckmaterialprogressbar_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2MaterialStyleImpl/QtQuickControls2MaterialStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2MaterialStyleImpl/6.12.0/QtQuickControls2MaterialStyleImpl/private/qquickmaterialprogressbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickmaterialprogressbar_p.h"
#include <QtCore/qmath.h>
#include <QtCore/qeasingcurve.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtQuick/qsgrectanglenode.h>
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

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 150, as _ZNK25QQuickMaterialProgressBar5colorEv
inline QColor QQuickMaterialProgressBar::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 155, as _ZN25QQuickMaterialProgressBar8setColorERK6QColor
inline void QQuickMaterialProgressBar::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 164, as _ZNK25QQuickMaterialProgressBar8progressEv
inline qreal QQuickMaterialProgressBar::progress() const
{
    return m_progress;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 169, as _ZN25QQuickMaterialProgressBar11setProgressEd
inline void QQuickMaterialProgressBar::setProgress(qreal progress)
{
    if (progress == m_progress)
        return;

    m_progress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 178, as _ZNK25QQuickMaterialProgressBar15isIndeterminateEv
inline bool QQuickMaterialProgressBar::isIndeterminate() const
{
    return m_indeterminate;
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 183, as _ZN25QQuickMaterialProgressBar16setIndeterminateEb
inline void QQuickMaterialProgressBar::setIndeterminate(bool indeterminate)
{
    if (indeterminate == m_indeterminate)
        return;

    m_indeterminate = indeterminate;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/material/impl/qquickmaterialprogressbar.cpp, line 192, as _ZN25QQuickMaterialProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE
inline void QQuickMaterialProgressBar::itemChange(QQuickItem::ItemChange change, const QQuickItem::ItemChangeData &data)
{
    QQuickItem::itemChange(change, data);
    if (change == ItemVisibleHasChanged)
        update();
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickMaterialProgressBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickMaterialProgressBar : QQuickMaterialProgressBar {
  using QQuickMaterialProgressBar::itemChange;
};

//  const QMetaObject *QQuickMaterialProgressBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickMaterialProgressBar10metaObjectEv(
    const QQuickMaterialProgressBar *self) {
  return self->metaObject();
}

//  QColor QQuickMaterialProgressBar::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QQuickMaterialProgressBar5colorEv(
    const QQuickMaterialProgressBar *self) {
  return new QColor(self->color());
}

//  void QQuickMaterialProgressBar::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar8setColorERK6QColor(
    QQuickMaterialProgressBar *self,
    const QColor *color) {
  self->setColor(*color);
}

//  qreal QQuickMaterialProgressBar::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickMaterialProgressBar8progressEv(
    const QQuickMaterialProgressBar *self) {
  return self->progress();
}

//  void QQuickMaterialProgressBar::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar11setProgressEd(
    QQuickMaterialProgressBar *self,
    qreal progress) {
  self->setProgress(progress);
}

//  bool QQuickMaterialProgressBar::isIndeterminate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickMaterialProgressBar15isIndeterminateEv(
    const QQuickMaterialProgressBar *self) {
  return self->isIndeterminate();
}

//  void QQuickMaterialProgressBar::setIndeterminate(bool indeterminate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar16setIndeterminateEb(
    QQuickMaterialProgressBar *self,
    bool indeterminate) {
  self->setIndeterminate(indeterminate);
}

//  void QQuickMaterialProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickMaterialProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  void QQuickMaterialProgressBar::itemChange(ItemChange change, const
//      ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickMaterialProgressBar10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickMaterialProgressBar *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  static_cast<OwnQQuickMaterialProgressBar *>(self)->OwnQQuickMaterialProgressBar::itemChange(
      change,
      *data);
}
