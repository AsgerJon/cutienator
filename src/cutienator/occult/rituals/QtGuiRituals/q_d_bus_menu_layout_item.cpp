//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qdbusmenutypes_p.h>
#include <QDBusConnection>
#include <QDBusMetaType>
#include <QtGui/QImage>
#include <QtGui/QIcon>
#include <QtGui/QImage>
#include <QtGui/QPixmap>
#include <QtCore/QDebug>
#include <QtCore/QtEndian>
#include <QtCore/QBuffer>
#if QT_CONFIG(shortcut)
#  include <QtGui/private/qkeysequence_p.h>
#endif
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/private/qdbusplatformmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 13, as _Z7qLcMenuv
inline const QLoggingCategory &qLcMenu()
{
    static const QLoggingCategory category("qt.qpa.menu");
    return category;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 158, as _ZN13QDBusMenuItemC1EPK21QDBusPlatformMenuItem
inline QDBusMenuItem::QDBusMenuItem(const QDBusPlatformMenuItem *item)
    : m_id(item->dbusID())
{
    if (item->isSeparator()) {
        m_properties.insert("type"_L1, "separator"_L1);
    } else {
        m_properties.insert("label"_L1, convertMnemonic(item->text()));
        if (item->menu())
            m_properties.insert("children-display"_L1, "submenu"_L1);
        m_properties.insert("enabled"_L1, item->isEnabled());
        if (item->isCheckable()) {
            QString toggleType = item->hasExclusiveGroup() ? "radio"_L1 : "checkmark"_L1;
            m_properties.insert("toggle-type"_L1, toggleType);
            m_properties.insert("toggle-state"_L1, item->isChecked() ? 1 : 0);
        }
#ifndef QT_NO_SHORTCUT
        const QKeySequence &scut = item->shortcut();
        if (!scut.isEmpty()) {
            QDBusMenuShortcut shortcut = convertKeySequence(scut);
            m_properties.insert("shortcut"_L1, QVariant::fromValue(shortcut));
        }
#endif
        const QIcon &icon = item->icon();
        if (!icon.name().isEmpty()) {
            m_properties.insert("icon-name"_L1, icon.name());
        } else if (!icon.isNull()) {
            QBuffer buf;
            icon.pixmap(16).save(&buf, "PNG");
            m_properties.insert("icon-data"_L1, buf.data());
        }
    }
    m_properties.insert("visible"_L1, item->isVisible());
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 258, as _ZNK17QDBusPlatformMenu5itemsEv
inline const QList<QDBusPlatformMenuItem *> QDBusPlatformMenu::items() const
{
    return m_items;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 203, as _ZN13QDBusMenuItem15convertMnemonicERK7QString
inline QString QDBusMenuItem::convertMnemonic(const QString &label)
{
    // convert only the first occurrence of ampersand which is not at the end
    // dbusmenu uses underscore instead of ampersand
    int idx = label.indexOf(u'&');
    if (idx < 0 || idx == label.size() - 1)
        return label;
    QString ret(label);
    ret[idx] = u'_';
    return ret;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 216, as _ZN13QDBusMenuItem18convertKeySequenceERK12QKeySequence
#if !defined(QT_NO_SHORTCUT)
inline QDBusMenuShortcut QDBusMenuItem::convertKeySequence(const QKeySequence &sequence)
{
    QDBusMenuShortcut shortcut;
    for (int i = 0; i < sequence.count(); ++i) {
        QStringList tokens;
        auto modifiers = sequence[i].keyboardModifiers();
        if (modifiers & Qt::MetaModifier)
            tokens << QStringLiteral("Super");
        if (modifiers & Qt::ControlModifier)
            tokens << QStringLiteral("Control");
        if (modifiers & Qt::AltModifier)
            tokens << QStringLiteral("Alt");
        if (modifiers & Qt::ShiftModifier)
            tokens << QStringLiteral("Shift");
        if (modifiers & Qt::KeypadModifier)
            tokens << QStringLiteral("Num");

        QString keyName = QKeySequencePrivate::keyName(sequence[i].key(), QKeySequence::PortableText);
        if (keyName == "+"_L1)
            tokens << QStringLiteral("plus");
        else if (keyName == "-"_L1)
            tokens << QStringLiteral("minus");
        else
            tokens << keyName;
        shortcut << tokens;
    }
    return shortcut;
}
#endif  // !defined(QT_NO_SHORTCUT)

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 93, as _ZN19QDBusMenuLayoutItem8populateEPK17QDBusPlatformMenuiRK5QListI7QStringE
inline void QDBusMenuLayoutItem::populate(const QDBusPlatformMenu *menu, int depth, const QStringList &propertyNames)
{
    const auto items = menu->items();
    for (QDBusPlatformMenuItem *item : items) {
        QDBusMenuLayoutItem child;
        child.populate(item, depth - 1, propertyNames);
        m_children << child;
    }
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 103, as _ZN19QDBusMenuLayoutItem8populateEPK21QDBusPlatformMenuItemiRK5QListI7QStringE
inline void QDBusMenuLayoutItem::populate(const QDBusPlatformMenuItem *item, int depth, const QStringList &propertyNames)
{
    m_id = item->dbusID();
    QDBusMenuItem proxy(item);
    m_properties = proxy.m_properties;

    const QDBusPlatformMenu *menu = static_cast<const QDBusPlatformMenu *>(item->menu());
    if (depth != 0 && menu)
        populate(menu, depth, propertyNames);
}
//  -----------------------------------------------------------------------

#if !defined(QT_NO_SHORTCUT)
//  void QDBusMenuLayoutItem::populate(const QDBusPlatformMenu *menu, int
//      depth, const QStringList &propertyNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMenuLayoutItem8populateEPK17QDBusPlatformMenuiRK5QListI7QStringE(
    QDBusMenuLayoutItem *self,
    const QDBusPlatformMenu *menu,
    int depth,
    const QList<QString> *propertyNames) {
  self->populate(menu, depth, *propertyNames);
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_SHORTCUT)
//  void QDBusMenuLayoutItem::populate(const QDBusPlatformMenuItem *item, int
//      depth, const QStringList &propertyNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMenuLayoutItem8populateEPK21QDBusPlatformMenuItemiRK5QListI7QStringE(
    QDBusMenuLayoutItem *self,
    const QDBusPlatformMenuItem *item,
    int depth,
    const QList<QString> *propertyNames) {
  self->populate(item, depth, *propertyNames);
}
#endif  // !defined(QT_NO_SHORTCUT)

//  QDBusMenuLayoutItem::~QDBusMenuLayoutItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMenuLayoutItemD1Ev(QDBusMenuLayoutItem *self) {
  delete self;
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
