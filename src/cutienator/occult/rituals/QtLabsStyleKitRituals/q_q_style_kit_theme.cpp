//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekittheme_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqstylekitstyleandthemebase_p.h"
#include "qqstylekitvariation_p.h"
#include "qqstylekitfont_p.h"
#include "qqstylekitcontrols_p.h"
#include "qqstylekitcontrol_p.h"
#include "qqstylekitcustomcontrol_p.h"
#include <QtQuickTemplates2/private/qquicktheme_p.h>
#include <QtQuick/private/qquickpalette_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include "qqstylekittheme_p.h"
#include "qqstylekitstyle_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 21, as _ZN27QQStyleKitStyleAndThemeBaseC2EP7QObject
inline QQStyleKitStyleAndThemeBase::QQStyleKitStyleAndThemeBase(QObject *parent)
    : QQStyleKitControls(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 67, as _ZN27QQStyleKitStyleAndThemeBase8palettesEv
inline QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
{
    return &m_palettes;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitstyleandthemebase.cpp, line 43, as _ZN27QQStyleKitStyleAndThemeBase5fontsEv
inline QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
{
    return &m_fonts;
}

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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 725, as _ZN18QQStyleKitControls17componentCompleteEv
inline void QQStyleKitControls::componentComplete()
{
    for (auto *obj : children()) {
        if (auto *customControl = qobject_cast<QQStyleKitCustomControl *>(obj)) {
            const QQStyleKitExtendableControlType type = customControl->controlType();
            const QQStyleKitExtendableControlType reserved
                = QQStyleKitExtendableControlType(QQStyleKitReader::ControlType::Unspecified);
            if (type >= reserved)
                qmlWarning(this) << "CustomControls must use a controlType less than " << reserved;
            if (m_controls.contains(type))
                qmlWarning(this) << "CustomControl registered more than once: " << type;
            m_controls.insert(type, customControl);
        }
    }
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 110, as _ZNK15QQStyleKitTheme5styleEv
inline QQStyleKitStyle *QQStyleKitTheme::style() const
{
    QObject *parentObj = parent();
    if (!parentObj)
        return nullptr;
    Q_ASSERT(qobject_cast<QQStyleKitStyle *>(parentObj));
    return static_cast<QQStyleKitStyle *>(parentObj);
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 221, as _ZN15QQStyleKitTheme17componentCompleteEv
inline void QQStyleKitTheme::componentComplete()
{
    QQStyleKitControls::componentComplete();
    m_completed = true;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekittheme.cpp, line 185, as _ZN15QQStyleKitTheme16updateThemeFontsEv
inline void QQStyleKitTheme::updateThemeFonts()
{
    const QQStyleKitFont *fonts = this->fonts();
    if (!fonts)
        return;

    // Collect font fallback chain
    QVector<const QQStyleKitFont *> fbChain;
    for (auto *fb = fonts; fb; fb = fb->fallbackFont())
        fbChain.append(fb);

    auto resolveFromFontChain = [&](QQuickTheme::Scope scope) -> QFont
    {
        QFont result;

        // Apply from farthest fallback -> local
        for (int i = fbChain.size() - 1; i >= 0; --i) {
            const QQStyleKitFont *fb = fbChain[i];
            // Apply system font first as a base, and override with scope-specific font
            if (scope != QQuickTheme::System && fb->isSet(QQuickTheme::System)) {
                result = fb->fontForScope(QQuickTheme::System).resolve(result);
            }
            if (fb->isSet(scope)) {
                result = fb->fontForScope(scope).resolve(result);
            }
        }

        return result;
    };

    for (int i = 0; i < NScopes; ++i) {
        const QQuickTheme::Scope scope = static_cast<QQuickTheme::Scope>(i);
        m_effectiveFonts[i] = resolveFromFontChain(scope);
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitTheme::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQStyleKitTheme10metaObjectEv(
    const QQStyleKitTheme *self) {
  return self->metaObject();
}

//  QQStyleKitStyle *QQStyleKitTheme::style() const
extern "C" Q_DECL_EXPORT
QQStyleKitStyle *ritual_ZNK15QQStyleKitTheme5styleEv(
    const QQStyleKitTheme *self) {
  return self->style();
}

//  void QQStyleKitTheme::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitTheme17componentCompleteEv(QQStyleKitTheme *self) {
  self->componentComplete();
}

//  void QQStyleKitTheme::updateThemeFonts()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQStyleKitTheme16updateThemeFontsEv(QQStyleKitTheme *self) {
  self->updateThemeFonts();
}
