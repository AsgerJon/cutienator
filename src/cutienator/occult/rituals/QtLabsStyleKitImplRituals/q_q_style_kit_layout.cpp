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
#include <QtLabsStyleKitImpl/private/qqstylekitlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 216, as _ZNK16QQStyleKitLayout9containerEv
inline QQuickItem *QQStyleKitLayout::container() const
{
    return m_container;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 285, as _ZNK16QQStyleKitLayout7paddingEv
inline QMarginsF QQStyleKitLayout::padding() const
{
    return m_padding;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 290, as _ZNK16QQStyleKitLayout14contentMarginsEv
inline QMarginsF QQStyleKitLayout::contentMargins() const
{
    return m_contentMargins;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 305, as _ZNK16QQStyleKitLayout7spacingEv
inline qreal QQStyleKitLayout::spacing() const
{
    return m_spacing;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 320, as _ZNK16QQStyleKitLayout10isMirroredEv
inline bool QQStyleKitLayout::isMirrored() const
{
    return m_mirrored;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 335, as _ZNK16QQStyleKitLayout13implicitWidthEv
inline qreal QQStyleKitLayout::implicitWidth() const
{
    return m_implicitWidth;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 340, as _ZNK16QQStyleKitLayout14implicitHeightEv
inline qreal QQStyleKitLayout::implicitHeight() const
{
    return m_implicitHeight;
}

//  from ../qtdeclarative/src/labs/stylekit/impl/qqstylekitlayout.cpp, line 365, as _ZNK16QQStyleKitLayout9isEnabledEv
inline bool QQStyleKitLayout::isEnabled() const
{
    return m_enabled;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQStyleKitLayout10metaObjectEv(
    const QQStyleKitLayout *self) {
  return self->metaObject();
}

//  QQuickItem *QQStyleKitLayout::container() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK16QQStyleKitLayout9containerEv(
    const QQStyleKitLayout *self) {
  return self->container();
}

//  QMarginsF QQStyleKitLayout::padding() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK16QQStyleKitLayout7paddingEv(
    const QQStyleKitLayout *self) {
  return new QMarginsF(self->padding());
}

//  QMarginsF QQStyleKitLayout::contentMargins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK16QQStyleKitLayout14contentMarginsEv(
    const QQStyleKitLayout *self) {
  return new QMarginsF(self->contentMargins());
}

//  qreal QQStyleKitLayout::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQStyleKitLayout7spacingEv(const QQStyleKitLayout *self) {
  return self->spacing();
}

//  bool QQStyleKitLayout::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitLayout10isMirroredEv(
    const QQStyleKitLayout *self) {
  return self->isMirrored();
}

//  qreal QQStyleKitLayout::implicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQStyleKitLayout13implicitWidthEv(
    const QQStyleKitLayout *self) {
  return self->implicitWidth();
}

//  qreal QQStyleKitLayout::implicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQStyleKitLayout14implicitHeightEv(
    const QQStyleKitLayout *self) {
  return self->implicitHeight();
}

//  bool QQStyleKitLayout::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQStyleKitLayout9isEnabledEv(const QQStyleKitLayout *self) {
  return self->isEnabled();
}
