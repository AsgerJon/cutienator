//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfontdatabase.h>
#include <QtGui/private/qfontdatabase_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qalgorithms.h>
#include <QtGui/qguiapplication.h>
#include <QtCore/qvarlengtharray.h> // here or earlier - workaround for VC++6
#include <QtCore/qthread.h>
#include <QtCore/qmutex.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformfontdatabase.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtCore/qcache.h>
#include <QtCore/qmath.h>
#include <stdlib.h>
#include <algorithm>
#ifdef Q_OS_WIN
#include <QtGui/private/qwindowsfontdatabasebase_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/text/qfontdatabase.cpp, line 56, as local:qfontdatabase.cpp:getFontWeight
static int getFontWeight(const QString &weightString)
{
    QString s = weightString.toLower();

    // Order here is important. We want to match the common cases first, but we
    // must also take care to acknowledge the cost of our tests.
    //
    // As a result, we test in two orders; the order of commonness, and the
    // order of "expense".
    //
    // A simple string test is the cheapest, so let's do that first.
    // Test in decreasing order of commonness
    if (s == "normal"_L1 || s == "regular"_L1)
        return QFont::Normal;
    if (s == "bold"_L1)
        return QFont::Bold;
    if (s == "semibold"_L1 || s == "semi bold"_L1 || s == "demibold"_L1 || s == "demi bold"_L1)
        return QFont::DemiBold;
    if (s == "medium"_L1)
        return QFont::Medium;
    if (s == "black"_L1)
        return QFont::Black;
    if (s == "light"_L1)
        return QFont::Light;
    if (s == "thin"_L1)
        return QFont::Thin;
    const QStringView s2 = QStringView{s}.mid(2);
    if (s.startsWith("ex"_L1) || s.startsWith("ul"_L1)) {
            if (s2 == "tralight"_L1 || s == "tra light"_L1)
                return QFont::ExtraLight;
            if (s2 == "trabold"_L1 || s2 == "tra bold"_L1)
                return QFont::ExtraBold;
    }

    // Next up, let's see if contains() matches: slightly more expensive, but
    // still fast enough.
    if (s.contains("bold"_L1)) {
        if (s.contains("demi"_L1))
            return QFont::DemiBold;
        return QFont::Bold;
    }
    if (s.contains("thin"_L1))
        return QFont::Thin;
    if (s.contains("light"_L1))
        return QFont::Light;
    if (s.contains("black"_L1))
        return QFont::Black;

    // Now, we perform string translations & comparisons with those.
    // These are (very) slow compared to simple string ops, so we do these last.
    // As using translated values for such things is not very common, this should
    // not be too bad.
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Normal", "The Normal or Regular font weight"), Qt::CaseInsensitive) == 0)
        return QFont::Normal;
    const QString translatedBold = QCoreApplication::translate("QFontDatabase", "Bold").toLower();
    if (s == translatedBold)
        return QFont::Bold;
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Demi Bold"), Qt::CaseInsensitive) == 0)
        return QFont::DemiBold;
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Medium", "The Medium font weight"), Qt::CaseInsensitive) == 0)
        return QFont::Medium;
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Black"), Qt::CaseInsensitive) == 0)
        return QFont::Black;
    const QString translatedLight = QCoreApplication::translate("QFontDatabase", "Light").toLower();
    if (s == translatedLight)
        return QFont::Light;
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Thin"), Qt::CaseInsensitive) == 0)
        return QFont::Thin;
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Extra Light"), Qt::CaseInsensitive) == 0)
        return QFont::ExtraLight;
    if (s.compare(QCoreApplication::translate("QFontDatabase", "Extra Bold"), Qt::CaseInsensitive) == 0)
        return QFont::ExtraBold;

    // And now the contains() checks for the translated strings.
    //: The word for "Extra" as in "Extra Bold, Extra Thin" used as a pattern for string searches
    const QString translatedExtra = QCoreApplication::translate("QFontDatabase", "Extra").toLower();
    if (s.contains(translatedBold)) {
        //: The word for "Demi" as in "Demi Bold" used as a pattern for string searches
        QString translatedDemi = QCoreApplication::translate("QFontDatabase", "Demi").toLower();
        if (s .contains(translatedDemi))
            return QFont::DemiBold;
        if (s.contains(translatedExtra))
            return QFont::ExtraBold;
        return QFont::Bold;
    }

    if (s.contains(translatedLight)) {
        if (s.contains(translatedExtra))
            return QFont::ExtraLight;
        return QFont::Light;
    }
    return QFont::Normal;
}

//  from src/gui/text/qfontdatabase.cpp, line 151, as _ZN11QtFontStyle3KeyC1ERK7QString
inline QtFontStyle::Key::Key(const QString &styleString)
    : style(QFont::StyleNormal), weight(QFont::Normal), stretch(0)
{
    weight = getFontWeight(styleString);

    if (!styleString.isEmpty()) {
        // First the straightforward no-translation checks, these are fast.
        if (styleString.contains("Italic"_L1))
            style = QFont::StyleItalic;
        else if (styleString.contains("Oblique"_L1))
            style = QFont::StyleOblique;

        // Then the translation checks. These aren't as fast.
        else if (styleString.contains(QCoreApplication::translate("QFontDatabase", "Italic")))
            style = QFont::StyleItalic;
        else if (styleString.contains(QCoreApplication::translate("QFontDatabase", "Oblique")))
            style = QFont::StyleOblique;
    }
}
//  -----------------------------------------------------------------------

//  QtFontStyle::Key::Key(const QString &styleString)
extern "C" Q_DECL_EXPORT
QtFontStyle::Key *ritual_ZN11QtFontStyle3KeyC1ERK7QString(
    const QString *styleString) {
  return new QtFontStyle::Key(*styleString);
}

//  QtFontStyle::Key::Key()
extern "C" Q_DECL_EXPORT
QtFontStyle::Key *ritual_ZN11QtFontStyle3KeyC1Ev() {
  return new QtFontStyle::Key();
}

//  QtFontStyle::Key::Key(const Key &o)
extern "C" Q_DECL_EXPORT
QtFontStyle::Key *ritual_ZN11QtFontStyle3KeyC1ERKS0_(
    const QtFontStyle::Key *o) {
  return new QtFontStyle::Key(*o);
}

//  bool QtFontStyle::Key::operator==(const Key &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QtFontStyle3KeyeqERKS0_(
    const QtFontStyle::Key *self,
    const QtFontStyle::Key *other) {
  return self->operator==(*other);
}

//  bool QtFontStyle::Key::operator!=(const Key &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QtFontStyle3KeyneERKS0_(
    const QtFontStyle::Key *self,
    const QtFontStyle::Key *other) {
  return self->operator!=(*other);
}

//  QtFontStyle::Key::~Key()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QtFontStyle3KeyD1Ev(QtFontStyle::Key *self) {
  delete self;
}
