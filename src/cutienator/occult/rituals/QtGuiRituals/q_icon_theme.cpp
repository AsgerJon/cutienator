//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_ICON)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qiconloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef QT_NO_ICON
#include <QtGui/private/qiconloader_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qicon_p.h>
#include <QtGui/QIconEnginePlugin>
#include <QtGui/QPixmapCache>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qfontdatabase.h>
#include <QtGui/QPalette>
#include <QtCore/qmath.h>
#include <QtCore/QList>
#include <QtCore/QDir>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(settings)
#include <QtCore/QSettings>
#endif
#include <QtGui/QPainter>
#include <QtGui/private/qhexstring_p.h>
#include <QtCore/private/qfactoryloader_p.h>
#include <QtGui/private/qfonticonengine_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/image/qiconloader.cpp, line 430, as _ZNK10QIconTheme7parentsEv
#if !defined(QT_NO_ICON)
inline QStringList QIconTheme::parents() const
{
    // Respect explicitly declared parents
    QStringList result = m_parents;

    // Ensure a default fallback for all themes
    const QString fallback = QIconLoader::instance()->fallbackThemeName();
    if (!fallback.isEmpty())
        result.append(fallback);

    // Ensure that all themes fall back to hicolor as the last theme
    result.removeAll("hicolor"_L1);
    result.append("hicolor"_L1);

    return result;
}
#endif  // !defined(QT_NO_ICON)
//  -----------------------------------------------------------------------

//  QIconTheme::QIconTheme()
extern "C" Q_DECL_EXPORT
QIconTheme *ritual_ZN10QIconThemeC1Ev() {
  return new QIconTheme();
}

#if !defined(QT_NO_ICON)
//  QStringList QIconTheme::parents() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QIconTheme7parentsEv(const QIconTheme *self) {
  return new QList<QString>(self->parents());
}
#endif  // !defined(QT_NO_ICON)

//  QList<QIconDirInfo> QIconTheme::keyList() const
extern "C" Q_DECL_EXPORT
QList<QIconDirInfo> *ritual_ZNK10QIconTheme7keyListEv(
    const QIconTheme *self) {
  return new QList<QIconDirInfo>(self->keyList());
}

//  QStringList QIconTheme::contentDirs() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QIconTheme11contentDirsEv(
    const QIconTheme *self) {
  return new QList<QString>(self->contentDirs());
}

//  bool QIconTheme::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QIconTheme7isValidEv(const QIconTheme *self) {
  return self->isValid();
}

//  QIconTheme::~QIconTheme()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QIconThemeD1Ev(QIconTheme *self) {
  delete self;
}

#endif  // !defined(QT_NO_ICON)
