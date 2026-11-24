//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitdelegate_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h>
#include <QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/private/qquickimplicitsizeitem_p_p.h>
#include <QtQuickControls2Impl/private/qquickcolorimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 72, as _ZNK18QQStyleKitDelegate13delegateStyleEv
inline QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle() const
{
    return m_delegateProperties;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitdelegate.cpp, line 103, as _ZN18QQStyleKitDelegate18updateImplicitSizeEv
inline void QQStyleKitDelegate::updateImplicitSize()
{
    if (!m_delegateProperties)
        return;

    /* The implicit size of this item is determined by the following priority:
     * 1. The width/height set on DelegateStyle (clamped to minimumWidth/minimumHeight)
     * 2. The implicit size of the image overlay (if present)
     * 3. Zero */
    const qreal widthInStyle = qMax(m_delegateProperties->minimumWidth(), m_delegateProperties->width());
    const qreal heightInStyle = qMax(m_delegateProperties->minimumHeight(), m_delegateProperties->height());
    setImplicitWidth(widthInStyle > 0 || !m_imageOverlay ? widthInStyle : m_imageOverlay->implicitWidth());
    setImplicitHeight(heightInStyle > 0 || !m_imageOverlay ? heightInStyle : m_imageOverlay->implicitHeight());
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQStyleKitDelegate10metaObjectEv(
    const QQStyleKitDelegate *self) {
  return self->metaObject();
}

//  QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle() const
extern "C" Q_DECL_EXPORT
QQStyleKitDelegateProperties *ritual_ZNK18QQStyleKitDelegate13delegateStyleEv(
    const QQStyleKitDelegate *self) {
  return self->delegateStyle();
}

//  void QQStyleKitDelegate::updateImplicitSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQStyleKitDelegate18updateImplicitSizeEv(
    QQStyleKitDelegate *self) {
  self->updateImplicitSize();
}
