//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitpalette_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 43, as _ZNK17QQStyleKitPalette15fallbackPaletteEv
inline QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
{
    return m_fallbackPalette;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitPalette::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQStyleKitPalette10metaObjectEv(
    const QQStyleKitPalette *self) {
  return self->metaObject();
}

//  QQStyleKitPalette *QQStyleKitPalette::fallbackPalette() const
extern "C" Q_DECL_EXPORT
QQStyleKitPalette *ritual_ZNK17QQStyleKitPalette15fallbackPaletteEv(
    const QQStyleKitPalette *self) {
  return self->fallbackPalette();
}

//  bool QQStyleKitPalette::isSet(QQuickTheme::Scope scope) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQStyleKitPalette5isSetEN11QQuickTheme5ScopeE(
    const QQStyleKitPalette *self,
    QQuickTheme::Scope scope) {
  return self->isSet(scope);
}

//  void QQStyleKitPalette::markSet(QQuickTheme::Scope scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQStyleKitPalette7markSetEN11QQuickTheme5ScopeE(
    QQStyleKitPalette *self,
    QQuickTheme::Scope scope) {
  self->markSet(scope);
}
