//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  Impl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsStyleKitImpl/QtLabsStyleKitImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitlayout_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 74, as _ZNK20QQStyleKitLayoutItem4itemEv
inline QQuickItem *QQStyleKitLayoutItem::item() const
{
    return m_item;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 97, as _ZNK20QQStyleKitLayoutItem1xEv
inline qreal QQStyleKitLayoutItem::x() const
{
    return m_x;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 111, as _ZNK20QQStyleKitLayoutItem1yEv
inline qreal QQStyleKitLayoutItem::y() const
{
    return m_y;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 125, as _ZNK20QQStyleKitLayoutItem5widthEv
inline qreal QQStyleKitLayoutItem::width() const
{
    return m_width;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 139, as _ZNK20QQStyleKitLayoutItem6heightEv
inline qreal QQStyleKitLayoutItem::height() const
{
    return m_height;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 153, as _ZNK20QQStyleKitLayoutItem9alignmentEv
inline Qt::Alignment QQStyleKitLayoutItem::alignment() const
{
    return m_alignment;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 167, as _ZNK20QQStyleKitLayoutItem7marginsEv
inline QMarginsF QQStyleKitLayoutItem::margins() const
{
    return m_margins;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 181, as _ZNK20QQStyleKitLayoutItem9fillWidthEv
inline bool QQStyleKitLayoutItem::fillWidth() const
{
    return m_fillWidth;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 195, as _ZNK20QQStyleKitLayoutItem10fillHeightEv
inline bool QQStyleKitLayoutItem::fillHeight() const
{
    return m_fillHeight;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitLayoutItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQStyleKitLayoutItem10metaObjectEv(
    const QQStyleKitLayoutItem *self) {
  return self->metaObject();
}

//  QQuickItem *QQStyleKitLayoutItem::item() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQStyleKitLayoutItem4itemEv(
    const QQStyleKitLayoutItem *self) {
  return self->item();
}

//  qreal QQStyleKitLayoutItem::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem1xEv(
    const QQStyleKitLayoutItem *self) {
  return self->x();
}

//  qreal QQStyleKitLayoutItem::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem1yEv(
    const QQStyleKitLayoutItem *self) {
  return self->y();
}

//  qreal QQStyleKitLayoutItem::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem5widthEv(
    const QQStyleKitLayoutItem *self) {
  return self->width();
}

//  qreal QQStyleKitLayoutItem::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQStyleKitLayoutItem6heightEv(
    const QQStyleKitLayoutItem *self) {
  return self->height();
}

//  Qt::Alignment QQStyleKitLayoutItem::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQStyleKitLayoutItem9alignmentEv(
    const QQStyleKitLayoutItem *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  QMarginsF QQStyleKitLayoutItem::margins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK20QQStyleKitLayoutItem7marginsEv(
    const QQStyleKitLayoutItem *self) {
  return new QMarginsF(self->margins());
}

//  bool QQStyleKitLayoutItem::fillWidth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQStyleKitLayoutItem9fillWidthEv(
    const QQStyleKitLayoutItem *self) {
  return self->fillWidth();
}

//  bool QQStyleKitLayoutItem::fillHeight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQStyleKitLayoutItem10fillHeightEv(
    const QQStyleKitLayoutItem *self) {
  return self->fillHeight();
}
