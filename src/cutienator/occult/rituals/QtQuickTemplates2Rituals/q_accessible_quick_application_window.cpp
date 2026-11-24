//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qaccessiblequickapplicationwindow_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickapplicationwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qaccessiblequickapplicationwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickapplicationwindow.cpp, line 28, as _ZNK33QAccessibleQuickApplicationWindow14attributeValueEN11QAccessible9AttributeE
inline QVariant QAccessibleQuickApplicationWindow::attributeValue(QAccessible::Attribute key) const
{
    if (key == QAccessible::Attribute::Locale) {
        Q_ASSERT(applicationWindow());
        return QVariant::fromValue(applicationWindow()->locale());
    }

    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickapplicationwindow.cpp, line 38, as _ZNK33QAccessibleQuickApplicationWindow17applicationWindowEv
inline QQuickApplicationWindow *QAccessibleQuickApplicationWindow::applicationWindow() const
{
    return static_cast<QQuickApplicationWindow *>(object());
}
//  -----------------------------------------------------------------------

//  QVariant
//      QAccessibleQuickApplicationWindow::attributeValue(QAccessible::Attrib
//      ute key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK33QAccessibleQuickApplicationWindow14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickApplicationWindow *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QQuickApplicationWindow
//      *QAccessibleQuickApplicationWindow::applicationWindow() const
extern "C" Q_DECL_EXPORT
QQuickApplicationWindow *ritual_ZNK33QAccessibleQuickApplicationWindow17applicationWindowEv(
    const QAccessibleQuickApplicationWindow *self) {
  return self->applicationWindow();
}

//  QAccessibleQuickApplicationWindow as the QAccessibleAttributesInterface
//      it is built on
extern "C" Q_DECL_EXPORT
QAccessibleAttributesInterface *ritual_cast_QAccessibleQuickApplicationWindow_QAccessibleAttributesInterface(
    QAccessibleQuickApplicationWindow *self) {
  return static_cast<QAccessibleAttributesInterface *>(self);
}

//  QVariant
//      QAccessibleQuickApplicationWindow::attributeValue(QAccessible::Attrib
//      ute key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK33QAccessibleQuickApplicationWindow14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleQuickApplicationWindow *self,
    QAccessible::Attribute key) {
  return new QVariant(
      self->QAccessibleQuickApplicationWindow::attributeValue(
          key));
}

#endif  // QT_CONFIG(accessibility)
