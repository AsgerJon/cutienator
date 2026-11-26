//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtCore/qdebug.h>
#include <QtGui/qpaintdevice.h>
#include <QtGui/qfontdatabase.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qfontinfo.h>
#include <QtGui/qpainter.h>
#include <QtCore/qhash.h>
#include <QtCore/qdatastream.h>
#include <QtGui/qguiapplication.h>
#include <QtCore/qstringlist.h>
#include <QtGui/qscreen.h>
#include <QtCore/qthread.h>
#include <QtCore/qthreadstorage.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <limits.h>
#include <QtGui/qpa/qplatformscreen.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformfontdatabase.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtCore/QMutexLocker>
#include <QtCore/QMutex>
#include <algorithm>
#include <array>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qfont.cpp, line 52, as _ZNK8QFontDef10exactMatchERKS_
inline bool QFontDef::exactMatch(const QFontDef &other) const
{
    /*
      QFontDef comparison is more complicated than just simple
      per-member comparisons.

      When comparing point/pixel sizes, either point or pixelsize
      could be -1.  in This case we have to compare the non negative
      size value.

      This test will fail if the point-sizes differ by 1/2 point or
      more or they do not round to the same value.  We have to do this
      since our API still uses 'int' point-sizes in the API, but store
      deci-point-sizes internally.

      To compare the family members, we need to parse the font names
      and compare the family/foundry strings separately.  This allows
      us to compare e.g. "Helvetica" and "Helvetica [Adobe]" with
      positive results.
    */
    if (pixelSize != -1 && other.pixelSize != -1) {
        if (pixelSize != other.pixelSize)
            return false;
    } else if (pointSize != -1 && other.pointSize != -1) {
        if (pointSize != other.pointSize)
            return false;
    } else {
        return false;
    }

    if (!ignorePitch && !other.ignorePitch && fixedPitch != other.fixedPitch)
        return false;

    if (stretch != 0 && other.stretch != 0 && stretch != other.stretch)
        return false;

    if (families.size() != other.families.size())
        return false;

    QString this_family, this_foundry, other_family, other_foundry;
    for (int i = 0; i < families.size(); ++i) {
        QFontDatabasePrivate::parseFontName(families.at(i), this_foundry, this_family);
        QFontDatabasePrivate::parseFontName(other.families.at(i), other_foundry, other_family);
        if (this_family != other_family || this_foundry != other_foundry)
            return false;
    }

    if (variableAxisValues != other.variableAxisValues)
        return false;

    return (styleHint     == other.styleHint
            && styleStrategy == other.styleStrategy
            && weight        == other.weight
            && style        == other.style
            && this_family   == other_family
            && (styleName.isEmpty() || other.styleName.isEmpty() || styleName == other.styleName)
            && (this_foundry.isEmpty()
                || other_foundry.isEmpty()
                || this_foundry == other_foundry)
       );
}
//  -----------------------------------------------------------------------

//  QFontDef::QFontDef()
extern "C" Q_DECL_EXPORT
QFontDef *ritual_ZN8QFontDefC1Ev() {
  return new QFontDef();
}

//  QString QFontDef::family() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QFontDef6familyEv(const QFontDef *self) {
  return new QString(self->family());
}

//  bool QFontDef::exactMatch(const QFontDef &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QFontDef10exactMatchERKS_(
    const QFontDef *self,
    const QFontDef *other) {
  return self->exactMatch(*other);
}

//  bool QFontDef::operator==(const QFontDef &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QFontDefeqERKS_(
    const QFontDef *self,
    const QFontDef *other) {
  return self->operator==(*other);
}

//  bool QFontDef::operator<(const QFontDef &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QFontDefltERKS_(
    const QFontDef *self,
    const QFontDef *other) {
  return self->operator<(*other);
}

//  QFontDef::~QFontDef()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QFontDefD1Ev(QFontDef *self) {
  delete self;
}
