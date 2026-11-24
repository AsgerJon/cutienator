//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitfont_p.h"
#include "qqstylekitpalette_p.h"
#include "qqstylekitcontrols_p.h"
#include "qqstylekitcontrol_p.h"
#include "qqstylekitcustomcontrol_p.h"
#include "qqstylekitstyleandthemebase_p.h"
#include "qqstylekitvariation_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitfont.cpp, line 8, as _ZN14QQStyleKitFontC1EP7QObject
inline QQStyleKitFont::QQStyleKitFont(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpalette.cpp, line 8, as _ZN17QQStyleKitPaletteC1EP7QObject
inline QQStyleKitPalette::QQStyleKitPalette(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 604, as _ZN18QQStyleKitControlsC2EP7QObject
inline QQStyleKitControls::QQStyleKitControls(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 43, as _ZN27QQStyleKitStyleAndThemeBase5fontsEv
inline QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
{
    return &m_fonts;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 67, as _ZN27QQStyleKitStyleAndThemeBase8palettesEv
inline QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
{
    return &m_palettes;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitStyleAndThemeBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQStyleKitStyleAndThemeBase10metaObjectEv(
    const QQStyleKitStyleAndThemeBase *self) {
  return self->metaObject();
}

//  void QQStyleKitStyleAndThemeBase::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQStyleKitStyleAndThemeBase24qt_qmlMarker_uncreatableEv(
    QQStyleKitStyleAndThemeBase *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
extern "C" Q_DECL_EXPORT
QQStyleKitFont *ritual_ZN27QQStyleKitStyleAndThemeBase5fontsEv(
    QQStyleKitStyleAndThemeBase *self) {
  return self->fonts();
}

//  QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
extern "C" Q_DECL_EXPORT
QQStyleKitPalette *ritual_ZN27QQStyleKitStyleAndThemeBase8palettesEv(
    QQStyleKitStyleAndThemeBase *self) {
  return self->palettes();
}
