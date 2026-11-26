//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qaccessiblequickcontrol_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/QList>
#include <QtGui/QAccessible>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qaccessiblequickcontrol_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 10, as _ZN23QAccessibleQuickControlC1EP13QQuickControl
inline QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl *control)
    : QAccessibleQuickItem(control)
{
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 15, as _ZNK23QAccessibleQuickControl13attributeKeysEv
inline QList<QAccessible::Attribute> QAccessibleQuickControl::attributeKeys() const
{
    auto keys = QAccessibleQuickItem::attributeKeys();
    if (!keys.contains(QAccessible::Attribute::Locale))
        keys << QAccessible::Attribute::Locale;

    return keys;
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
//  -----------------------------------------------------------------------

//  QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl *control)
extern "C" Q_DECL_EXPORT
QAccessibleQuickControl *ritual_ZN23QAccessibleQuickControlC1EP13QQuickControl(
    QQuickControl *control) {
  return new QAccessibleQuickControl(control);
}

//  QList<QAccessible::Attribute> QAccessibleQuickControl::attributeKeys()
//      const
extern "C" Q_DECL_EXPORT
QList<QAccessible::Attribute> *ritual_ZNK23QAccessibleQuickControl13attributeKeysEv(
    const QAccessibleQuickControl *self) {
  return new QList<QAccessible::Attribute>(self->attributeKeys());
}

//  QVariant QAccessibleQuickControl::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QAccessibleQuickControl14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickControl *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QQuickControl *QAccessibleQuickControl::control() const
extern "C" Q_DECL_EXPORT
QQuickControl *ritual_ZNK23QAccessibleQuickControl7controlEv(
    const QAccessibleQuickControl *self) {
  return self->control();
}

//  QVariant QAccessibleQuickControl::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK23QAccessibleQuickControl14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickControl *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleQuickControl::attributeValue(key));
}

//  a QList<QAccessible::Attribute> a ritual of QAccessibleQuickControl gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAccessibleQuickControl__QList_QAccessible_Attribute(
    QList<QAccessible::Attribute> *self) {
  delete self;
}

#endif  // QT_CONFIG(accessibility)
