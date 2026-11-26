//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformiconloader_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/qqml.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 9, as _ZNK22QQuickLabsPlatformIcon6sourceEv
inline QUrl QQuickLabsPlatformIcon::source() const
{
    return m_source;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 19, as _ZNK22QQuickLabsPlatformIcon4nameEv
inline QString QQuickLabsPlatformIcon::name() const
{
    return m_name;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 29, as _ZNK22QQuickLabsPlatformIcon6isMaskEv
inline bool QQuickLabsPlatformIcon::isMask() const
{
    return m_mask;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 13, as _ZN28QQuickLabsPlatformIconLoaderC1EiP7QObject
inline QQuickLabsPlatformIconLoader::QQuickLabsPlatformIconLoader(int slot, QObject *parent)
    : m_parent(parent),
      m_slot(slot),
      m_enabled(false)
{
    Q_ASSERT(slot != -1 && parent);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 21, as _ZNK28QQuickLabsPlatformIconLoader9isEnabledEv
inline bool QQuickLabsPlatformIconLoader::isEnabled() const
{
    return m_enabled;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 26, as _ZN28QQuickLabsPlatformIconLoader10setEnabledEb
inline void QQuickLabsPlatformIconLoader::setEnabled(bool enabled)
{
    m_enabled = enabled;
    if (m_enabled)
        loadIcon();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 33, as _ZNK28QQuickLabsPlatformIconLoader7toQIconEv
inline QIcon QQuickLabsPlatformIconLoader::toQIcon() const
{
    QIcon fallback = QPixmap::fromImage(image());
    QIcon icon = QIcon::fromTheme(m_icon.name(), fallback);
    icon.setIsMask(m_icon.isMask());
    return icon;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 41, as _ZNK28QQuickLabsPlatformIconLoader4iconEv
inline QQuickLabsPlatformIcon QQuickLabsPlatformIconLoader::icon() const
{
    return m_icon;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 46, as _ZN28QQuickLabsPlatformIconLoader7setIconERK22QQuickLabsPlatformIcon
inline void QQuickLabsPlatformIconLoader::setIcon(const QQuickLabsPlatformIcon& icon)
{
    m_icon = icon;
    if (m_enabled)
        loadIcon();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 53, as _ZN28QQuickLabsPlatformIconLoader8loadIconEv
inline void QQuickLabsPlatformIconLoader::loadIcon()
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

//  QQuickLabsPlatformIconLoader::QQuickLabsPlatformIconLoader(int slot,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformIconLoader *ritual_ZN28QQuickLabsPlatformIconLoaderC1EiP7QObject(
    int slot,
    QObject *parent) {
  return new QQuickLabsPlatformIconLoader(slot, parent);
}

//  bool QQuickLabsPlatformIconLoader::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickLabsPlatformIconLoader9isEnabledEv(
    const QQuickLabsPlatformIconLoader *self) {
  return self->isEnabled();
}

//  void QQuickLabsPlatformIconLoader::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformIconLoader10setEnabledEb(
    QQuickLabsPlatformIconLoader *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  QIcon QQuickLabsPlatformIconLoader::toQIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK28QQuickLabsPlatformIconLoader7toQIconEv(
    const QQuickLabsPlatformIconLoader *self) {
  return new QIcon(self->toQIcon());
}

//  QQuickLabsPlatformIcon QQuickLabsPlatformIconLoader::icon() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformIcon *ritual_ZNK28QQuickLabsPlatformIconLoader4iconEv(
    const QQuickLabsPlatformIconLoader *self) {
  return new QQuickLabsPlatformIcon(self->icon());
}

//  void QQuickLabsPlatformIconLoader::setIcon(const QQuickLabsPlatformIcon
//      &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformIconLoader7setIconERK22QQuickLabsPlatformIcon(
    QQuickLabsPlatformIconLoader *self,
    const QQuickLabsPlatformIcon *icon) {
  self->setIcon(*icon);
}

//  void QQuickLabsPlatformIconLoader::loadIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformIconLoader8loadIconEv(
    QQuickLabsPlatformIconLoader *self) {
  self->loadIcon();
}
