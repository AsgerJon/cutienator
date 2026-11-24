//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qaccessiblequickslider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickslider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qaccessiblequickcontrol_p.h"
#include "qquickcontrol_p.h"
#include "qaccessiblequickslider_p.h"
#include "qquickslider_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 10, as _ZN23QAccessibleQuickControlC2EP13QQuickControl
inline QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl *control)
    : QAccessibleQuickItem(control)
{
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 24, as _ZNK23QAccessibleQuickControl14attributeValueEN11QAccessible9AttributeE
inline QVariant QAccessibleQuickControl::attributeValue(QAccessible::Attribute key) const
{
    if (key == QAccessible::Attribute::Locale)
        return QVariant::fromValue(control()->locale());

    return QAccessibleQuickItem::attributeValue(key);
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 32, as _ZNK23QAccessibleQuickControl7controlEv
inline QQuickControl *QAccessibleQuickControl::control() const
{
    return static_cast<QQuickControl *>(object());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickslider.cpp, line 23, as _ZNK22QAccessibleQuickSlider14attributeValueEN11QAccessible9AttributeE
inline QVariant QAccessibleQuickSlider::attributeValue(QAccessible::Attribute key) const
{
    if (key == QAccessible::Attribute::Orientation)
        return QVariant::fromValue(slider()->orientation());

    return QAccessibleQuickControl::attributeValue(key);
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickslider.cpp, line 31, as _ZNK22QAccessibleQuickSlider6sliderEv
inline QQuickSlider *QAccessibleQuickSlider::slider() const
{
    return static_cast<QQuickSlider *>(object());
}
//  -----------------------------------------------------------------------

//  QVariant QAccessibleQuickSlider::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QAccessibleQuickSlider14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickSlider *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QQuickSlider *QAccessibleQuickSlider::slider() const
extern "C" Q_DECL_EXPORT
QQuickSlider *ritual_ZNK22QAccessibleQuickSlider6sliderEv(
    const QAccessibleQuickSlider *self) {
  return self->slider();
}

//  QVariant QAccessibleQuickSlider::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QAccessibleQuickSlider14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickSlider *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleQuickSlider::attributeValue(key));
}

#endif  // QT_CONFIG(accessibility)
