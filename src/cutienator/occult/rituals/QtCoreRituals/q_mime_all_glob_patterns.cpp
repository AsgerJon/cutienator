//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimeglobpattern_p.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/QRegularExpression>
#endif
#include <QtCore/QStringList>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 207, as _ZN20QMimeAllGlobPatterns14removeMimeTypeERK7QString
inline void QMimeAllGlobPatterns::removeMimeType(const QString &mimeType)
{
    for (auto &x : m_fastPatterns)
        x.removeAll(mimeType);
    m_highWeightGlobs.removeMimeType(mimeType);
    m_lowWeightGlobs.removeMimeType(mimeType);
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 255, as _ZN20QMimeAllGlobPatterns5clearEv
inline void QMimeAllGlobPatterns::clear()
{
    m_fastPatterns.clear();
    m_highWeightGlobs.clear();
    m_lowWeightGlobs.clear();
}
//  -----------------------------------------------------------------------

//  void QMimeAllGlobPatterns::removeMimeType(const QString &mimeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatterns14removeMimeTypeERK7QString(
    QMimeAllGlobPatterns *self,
    const QString *mimeType) {
  self->removeMimeType(*mimeType);
}

//  void QMimeAllGlobPatterns::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatterns5clearEv(QMimeAllGlobPatterns *self) {
  self->clear();
}

//  QMimeAllGlobPatterns::~QMimeAllGlobPatterns()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeAllGlobPatternsD1Ev(QMimeAllGlobPatterns *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
