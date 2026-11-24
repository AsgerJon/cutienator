//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquicknativeiconloader_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativeiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicknativeiconloader_p.h"
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/qqml.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 13, as _ZN22QQuickNativeIconLoaderC1EiP7QObject
inline QQuickNativeIconLoader::QQuickNativeIconLoader(int slot, QObject *parent)
    : m_parent(parent),
      m_slot(slot),
      m_enabled(false)
{
    Q_ASSERT(slot != -1 && parent);
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 21, as _ZNK22QQuickNativeIconLoader9isEnabledEv
inline bool QQuickNativeIconLoader::isEnabled() const
{
    return m_enabled;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 26, as _ZN22QQuickNativeIconLoader10setEnabledEb
inline void QQuickNativeIconLoader::setEnabled(bool enabled)
{
    m_enabled = enabled;
    if (m_enabled)
        loadIcon();
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 33, as _ZNK22QQuickNativeIconLoader7toQIconEv
inline QIcon QQuickNativeIconLoader::toQIcon() const
{
    const QIcon fallback = QPixmap::fromImage(image());
    return QIcon::fromTheme(m_icon.name(), fallback);
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 39, as _ZNK22QQuickNativeIconLoader4iconEv
inline QQuickIcon QQuickNativeIconLoader::icon() const
{
    return m_icon;
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 44, as _ZN22QQuickNativeIconLoader7setIconERK10QQuickIcon
inline void QQuickNativeIconLoader::setIcon(const QQuickIcon &icon)
{
    m_icon = icon;
    if (m_enabled)
        loadIcon();
}

//  from ../qtdeclarative/src/quicktemplates/qquicknativeiconloader.cpp, line 51, as _ZN22QQuickNativeIconLoader8loadIconEv
inline void QQuickNativeIconLoader::loadIcon()
{
    if (m_icon.source().isEmpty()) {
        clear(m_parent);
    } else {
        load(qmlEngine(m_parent), m_icon.source());
        if (m_slot != -1 && isLoading()) {
            connectFinished(m_parent, m_slot);
            m_slot = -1;
        }
    }

    if (!isLoading())
        m_parent->metaObject()->method(m_slot).invoke(m_parent);
}
//  -----------------------------------------------------------------------

//  QQuickNativeIconLoader::QQuickNativeIconLoader(int slot, QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickNativeIconLoader *ritual_ZN22QQuickNativeIconLoaderC1EiP7QObject(
    int slot,
    QObject *parent) {
  return new QQuickNativeIconLoader(slot, parent);
}

//  bool QQuickNativeIconLoader::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickNativeIconLoader9isEnabledEv(
    const QQuickNativeIconLoader *self) {
  return self->isEnabled();
}

//  void QQuickNativeIconLoader::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickNativeIconLoader10setEnabledEb(
    QQuickNativeIconLoader *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  QIcon QQuickNativeIconLoader::toQIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK22QQuickNativeIconLoader7toQIconEv(
    const QQuickNativeIconLoader *self) {
  return new QIcon(self->toQIcon());
}

//  QQuickIcon QQuickNativeIconLoader::icon() const
extern "C" Q_DECL_EXPORT
QQuickIcon *ritual_ZNK22QQuickNativeIconLoader4iconEv(
    const QQuickNativeIconLoader *self) {
  return new QQuickIcon(self->icon());
}

//  void QQuickNativeIconLoader::setIcon(const QQuickIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickNativeIconLoader7setIconERK10QQuickIcon(
    QQuickNativeIconLoader *self,
    const QQuickIcon *icon) {
  self->setIcon(*icon);
}

//  void QQuickNativeIconLoader::loadIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickNativeIconLoader8loadIconEv(
    QQuickNativeIconLoader *self) {
  self->loadIcon();
}
