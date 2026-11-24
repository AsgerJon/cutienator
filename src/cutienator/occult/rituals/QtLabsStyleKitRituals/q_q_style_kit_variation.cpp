//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitglobal_p.h>
#include <QtLabsStyleKit/QtLabsStyleKit>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsStyleKit/private/qqstylekitcontrols_p.h>
#include <QtLabsStyleKit/private/qqstylekitcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h>
#include <QtLabsStyleKit/private/qqstylekitvariation_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h>
#include <QtLabsStyleKit/private/qqstylekitstyle_p.h>
#include <QtLabsStyleKit/private/qqstylekittheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitcontrols.cpp, line 604, as _ZN18QQStyleKitControlsC2EP7QObject
inline QQStyleKitControls::QQStyleKitControls(QObject *parent)
    : QObject(parent)
{
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 186, as _ZN27QQStyleKitVariationAttachedC1EP7QObject
inline QQStyleKitVariationAttached::QQStyleKitVariationAttached(QObject *parent)
    : QObject(parent)
{
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

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 148, as _ZN19QQStyleKitVariation17componentCompleteEv
inline void QQStyleKitVariation::componentComplete()
{
    QQStyleKitControls::componentComplete();

    /* Whenever there is a Style or Theme change, the list of StyleVariations that affects a
     * StyleReader needs to be rebuilt. And in order to know which StyleVariations that should
     * be taken into consideration, we need to know which Style each StyleVariation belongs to. */
    bool styleOrThemeFound = false;
    for (QObject *current = parent(); current; current = current->parent()) {
        if (auto *styleOrTheme = qobject_cast<QQStyleKitStyleAndThemeBase *>(current)) {
            styleOrTheme->m_styleVariations.append(this);
            styleOrThemeFound = true;
            break;
        }
    }
    if (!styleOrThemeFound)
        qmlWarning(this) << "A StyleVariation needs to be a descendant of the Style it belongs to!";
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 172, as _ZNK19QQStyleKitVariation4nameEv
inline QString QQStyleKitVariation::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/labs/stylekit/qqstylekitvariation.cpp, line 219, as _ZN19QQStyleKitVariation23resetVariationsForStyleEP15QQStyleKitStyle
inline void QQStyleKitVariation::resetVariationsForStyle(QQStyleKitStyle *style)
{
    /* The usage context stored in a StyleVariation tells which Style or Theme uses it.
     * After a theme change, we therefore need to rebuild this context list, since the
     * old theme needs to be removed, and the new theme might need to be added.
     * Since we also need to update which variations will now be effective for the existing
     * StyleReaders, we simply clear the context here, and leave it to QQStyleKitPropertyResolver
     * to rebuild both the effective variations and the context in one pass later.
     * (QQStyleKitReader::resetReadersForStyle() will set the m_effectiveVariationsDirty
     * flag, which will trigger the rebuild).
     *
     * As an optimization, we also update m_hasVariations to reflect whether any variations
     * exist at all. If not, variations don't need to be taken into consideration during
     * style property look-up. */
    style->m_hasVariations = false;

    for (QQStyleKitStyle *current = style; current; current = current->fallbackStyle()) {
        if (!current->m_styleVariations.isEmpty()) {
            style->m_hasVariations = true;
            for (QQStyleKitVariation *variation : current->m_styleVariations)
                variation->m_usageContext.clear();
        }

        if (QQStyleKitTheme *theme = current->theme()) {
            if (!theme->m_styleVariations.isEmpty()) {
                style->m_hasVariations = true;
                for (QQStyleKitVariation *variation : theme->m_styleVariations)
                    variation->m_usageContext.clear();
            }
        }
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQStyleKitVariation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQStyleKitVariation10metaObjectEv(
    const QQStyleKitVariation *self) {
  return self->metaObject();
}

//  void QQStyleKitVariation::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQStyleKitVariation21qt_qmlMarker_attachedEv(
    QQStyleKitVariation *self) {
  self->qt_qmlMarker_attached();
}

//  void QQStyleKitVariation::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQStyleKitVariation17componentCompleteEv(
    QQStyleKitVariation *self) {
  self->componentComplete();
}

//  QString QQStyleKitVariation::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQStyleKitVariation4nameEv(
    const QQStyleKitVariation *self) {
  return new QString(self->name());
}

//  void QQStyleKitVariation::resetVariationsForStyle(QQStyleKitStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQStyleKitVariation23resetVariationsForStyleEP15QQStyleKitStyle(
    QQStyleKitStyle *style) {
  QQStyleKitVariation::resetVariationsForStyle(style);
}
