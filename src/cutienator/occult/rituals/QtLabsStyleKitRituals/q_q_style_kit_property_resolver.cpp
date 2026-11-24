//  Written by dev_tooling.RitualGenerator from the records of QtLabsStyleKit
//  /6.12.0/QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitpropertyresolver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitpropertyresolver_p.h"
#include "qqstylekitcontrol_p.h"
#include "qqstylekitcontrols_p.h"
#include "qqstylekitvariation_p.h"
#include "qqstylekitstyle_p.h"
#include "qqstylekittheme_p.h"
#include "qqstylekitdebug_p.h"
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtCore/QScopedValueRollback>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitpropertyresolver.cpp, line 135, as _ZN26QQStyleKitPropertyResolver20addVariationToReaderEP16QQStyleKitReaderP27QQStyleKitStyleAndThemeBaseP19QQStyleKitVariation
inline void QQStyleKitPropertyResolver::addVariationToReader(
    QQStyleKitReader *styleReader,
    QQStyleKitStyleAndThemeBase *styleOrTheme,
    QQStyleKitVariation *variation)
{
    /* Add the variation to the StyleReader's list of effective variations.
     * A variation may appear more than once in a type variation list or in
     * an instance variation list, but it only needs to be added once - the
     * first in the list will shadow the other ones anyway. */
    if (!styleReader->m_effectiveVariations.contains(variation))
        styleReader->m_effectiveVariations.append(variation);

    /* We also record in which Style or Theme the variation was found, so that
     * it only takes effect for that specific Style or Theme during property
     * propagation. Note that the same type variation can be used from both the
     * Style and the Theme (its ID can be added to several variation lists). */
    if (!variation->m_usageContext.contains(styleOrTheme))
        variation->m_usageContext.append(styleOrTheme);
}
//  -----------------------------------------------------------------------

//  void QQStyleKitPropertyResolver::addVariationToReader(QQStyleKitReader
//      *styleReader, QQStyleKitStyleAndThemeBase *styleOrTheme,
//      QQStyleKitVariation *variation)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitPropertyResolver20addVariationToReaderEP16QQStyleKitReaderP27QQStyleKitStyleAndThemeBaseP19QQStyleKitVariation(
    QQStyleKitReader *styleReader,
    QQStyleKitStyleAndThemeBase *styleOrTheme,
    QQStyleKitVariation *variation) {
  QQStyleKitPropertyResolver::addVariationToReader(
      styleReader,
      styleOrTheme,
      variation);
}

//  QQStyleKitPropertyResolver::~QQStyleKitPropertyResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQStyleKitPropertyResolverD1Ev(
    QQStyleKitPropertyResolver *self) {
  delete self;
}
