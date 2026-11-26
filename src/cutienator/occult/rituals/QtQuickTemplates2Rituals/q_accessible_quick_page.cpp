//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qaccessiblequickpage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickpage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qaccessiblequickcontrol_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtQuickTemplates2/private/qaccessiblequickpage_p.h>
#include <QtQuickTemplates2/private/qquickpage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickcontrol.cpp, line 10, as _ZN23QAccessibleQuickControlC2EP13QQuickControl
inline QAccessibleQuickControl::QAccessibleQuickControl(QQuickControl *control)
    : QAccessibleQuickItem(control)
{
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickpage.cpp, line 15, as _ZNK20QAccessibleQuickPage5childEi
inline QAccessibleInterface *QAccessibleQuickPage::child(int index) const
{
    const QList<QQuickItem*> kids = orderedChildItems();
    if (QQuickItem *item = kids.value(index))
        return QAccessible::queryAccessibleInterface(item);
    return nullptr;
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickpage.cpp, line 23, as _ZNK20QAccessibleQuickPage12indexOfChildEPK20QAccessibleInterface
inline int QAccessibleQuickPage::indexOfChild(const QAccessibleInterface *iface) const
{
    const QList<QQuickItem*> kids = orderedChildItems();
    return (int)kids.indexOf(static_cast<QQuickItem*>(iface->object()));
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

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickpage.cpp, line 43, as _ZNK20QAccessibleQuickPage4pageEv
inline QQuickPage *QAccessibleQuickPage::page() const
{
    return static_cast<QQuickPage*>(object());
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickpage.cpp, line 29, as _ZNK20QAccessibleQuickPage17orderedChildItemsEv
inline QList<QQuickItem *> QAccessibleQuickPage::orderedChildItems() const
{
    // Just ensures that the header is first, and footer is last. Other existing order is kept.
    const QQuickPage *p = page();
    QList<QQuickItem*> kids = childItems();
    const qsizetype hidx = kids.indexOf(p->header());
    if (hidx != -1)
        kids.move(hidx, 0);
    const qsizetype fidx = kids.indexOf(p->footer());
    if (fidx != -1)
        kids.move(fidx, kids.size() - 1);
    return kids;
}
//  -----------------------------------------------------------------------

//  QAccessibleInterface *QAccessibleQuickPage::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK20QAccessibleQuickPage5childEi(
    const QAccessibleQuickPage *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleQuickPage::indexOfChild(const QAccessibleInterface *iface)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QAccessibleQuickPage12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickPage *self,
    const QAccessibleInterface *iface) {
  return self->indexOfChild(iface);
}

//  QQuickPage *QAccessibleQuickPage::page() const
extern "C" Q_DECL_EXPORT
QQuickPage *ritual_ZNK20QAccessibleQuickPage4pageEv(
    const QAccessibleQuickPage *self) {
  return self->page();
}

//  QList<QQuickItem *> QAccessibleQuickPage::orderedChildItems() const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK20QAccessibleQuickPage17orderedChildItemsEv(
    const QAccessibleQuickPage *self) {
  return new QList<QQuickItem *>(self->orderedChildItems());
}

//  QAccessibleInterface *QAccessibleQuickPage::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK20QAccessibleQuickPage5childEi(
    const QAccessibleQuickPage *self,
    int index) {
  return self->QAccessibleQuickPage::child(index);
}

//  int QAccessibleQuickPage::indexOfChild(const QAccessibleInterface *iface)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QAccessibleQuickPage12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleQuickPage *self,
    const QAccessibleInterface *iface) {
  return self->QAccessibleQuickPage::indexOfChild(iface);
}

#endif  // QT_CONFIG(accessibility)
