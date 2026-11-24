//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitfont_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 69, as _ZNK14QQStyleKitFont12fallbackFontEv
inline QQStyleKitFont *QQStyleKitFont::fallbackFont() const
{
    return m_fallback;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 83, as _ZNK14QQStyleKitFont12fontForScopeEN11QQuickTheme5ScopeE
inline QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope) const
{
    return m_fonts[int(scope)];
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitFont::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQStyleKitFont10metaObjectEv(
    const QQStyleKitFont *self) {
  return self->metaObject();
}

//  QQStyleKitFont *QQStyleKitFont::fallbackFont() const
extern "C" Q_DECL_EXPORT
QQStyleKitFont *ritual_ZNK14QQStyleKitFont12fallbackFontEv(
    const QQStyleKitFont *self) {
  return self->fallbackFont();
}

//  QFont QQStyleKitFont::fontForScope(QQuickTheme::Scope scope) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQStyleKitFont12fontForScopeEN11QQuickTheme5ScopeE(
    const QQStyleKitFont *self,
    QQuickTheme::Scope scope) {
  return new QFont(self->fontForScope(scope));
}

//  bool QQStyleKitFont::isSet(QQuickTheme::Scope scope) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQStyleKitFont5isSetEN11QQuickTheme5ScopeE(
    const QQStyleKitFont *self,
    QQuickTheme::Scope scope) {
  return self->isSet(scope);
}

//  void QQStyleKitFont::markSet(QQuickTheme::Scope scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQStyleKitFont7markSetEN11QQuickTheme5ScopeE(
    QQStyleKitFont *self,
    QQuickTheme::Scope scope) {
  self->markSet(scope);
}
