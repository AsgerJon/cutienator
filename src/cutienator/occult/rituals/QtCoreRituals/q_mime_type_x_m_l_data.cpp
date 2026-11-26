//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimetypeparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimetypeparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/private/qmimetype_p.h>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QDebug>
#include <QtCore/QDir>
#include <QtCore/QXmlStreamReader>
#include <QtCore/QXmlStreamWriter>
#include <QtCore/QStack>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 324, as _ZN16QMimeTypeXMLData5clearEv
inline void QMimeTypeXMLData::clear()
{
    hasGlobDeleteAll = false;
    name.clear();
    localeComments.clear();
    genericIconName.clear();
    iconName.clear();
    globPatterns.clear();
}

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 334, as _ZN16QMimeTypeXMLData14addGlobPatternERK7QString
inline void QMimeTypeXMLData::addGlobPattern(const QString &pattern)
{
    globPatterns.append(pattern);
}
//  -----------------------------------------------------------------------

//  void QMimeTypeXMLData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeTypeXMLData5clearEv(QMimeTypeXMLData *self) {
  self->clear();
}

//  void QMimeTypeXMLData::addGlobPattern(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeTypeXMLData14addGlobPatternERK7QString(
    QMimeTypeXMLData *self,
    const QString *pattern) {
  self->addGlobPattern(*pattern);
}

//  QMimeTypeXMLData::~QMimeTypeXMLData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QMimeTypeXMLDataD1Ev(QMimeTypeXMLData *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
