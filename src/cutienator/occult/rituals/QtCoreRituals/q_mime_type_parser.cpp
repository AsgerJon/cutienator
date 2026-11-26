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
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimemagicrulematcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
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
#include <QtCore/private/qmimeprovider_p.h>
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/QFile>
#include <QtCore/QByteArrayMatcher>
#include <QtCore/QDebug>
#include <QtCore/QDateTime>
#include <QtCore/QtEndian>
#if QT_CONFIG(mimetype_database)
#  ifdef MIME_DATABASE_IS_ZSTD
#    include <zstd.h>
#  endif
#  ifdef MIME_DATABASE_IS_GZIP
#    include <zconf.h>
#    include <zlib.h>
#  endif
#endif
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

using namespace Qt::StringLiterals;

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 170, as local:qmimeglobpattern.cpp:isFastPattern
static bool isFastPattern(QStringView pattern)
{
   // starts with "*.", has no other '*' and no other '.'
   return pattern.lastIndexOf(u'*') == 0
      && pattern.lastIndexOf(u'.') == 1
      // and contains no other special character
      && !pattern.contains(u'?')
      && !pattern.contains(u'[')
      ;
}

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 61, as _ZN15QMimeTypeParserD2Ev
inline QMimeTypeParser::~QMimeTypeParser()
    = default;

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1045, as _ZN16QMimeXMLProvider11addMimeTypeERK16QMimeTypeXMLData
inline void QMimeXMLProvider::addMimeType(const QMimeTypeXMLData &mt)
{
    m_nameMimeTypeMap.insert(mt.name, mt);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1040, as _ZN16QMimeXMLProvider14addGlobPatternERK16QMimeGlobPattern
inline void QMimeXMLProvider::addGlobPattern(const QMimeGlobPattern &glob)
{
    m_mimeTypeGlobs.addGlob(glob);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1100, as _ZN16QMimeXMLProvider15addMagicMatcherERK21QMimeMagicRuleMatcher
inline void QMimeXMLProvider::addMagicMatcher(const QMimeMagicRuleMatcher &matcher)
{
    m_magicMatchers.append(matcher);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1078, as _ZN16QMimeXMLProvider8addAliasERK7QStringS2_
inline void QMimeXMLProvider::addAlias(const QString &alias, const QString &name)
{
    m_aliases.insert(alias, name);
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 1059, as _ZN16QMimeXMLProvider9addParentERK7QStringS2_
inline void QMimeXMLProvider::addParent(const QString &child, const QString &parent)
{
    m_parents[child].append(parent);
}

//  from src/corelib/mimetypes/qmimeglobpattern.cpp, line 181, as _ZN20QMimeAllGlobPatterns7addGlobERK16QMimeGlobPattern
inline void QMimeAllGlobPatterns::addGlob(const QMimeGlobPattern &glob)
{
    const QString &pattern = glob.pattern();
    Q_ASSERT(!pattern.isEmpty());

    // Store each patterns into either m_fastPatternDict (*.txt, *.html
    // etc. with default weight 50) or for the rest, like core.*, *.tar.bz2, *~,
    // into highWeightPatternOffset (>50) or lowWeightPatternOffset (<=50).

    if (glob.weight() == 50 && isFastPattern(pattern) && !glob.isCaseSensitive()) {
        // The bulk of the patterns is *.foo with weight 50 --> those go into the fast patterns hash.
        const QString extension = pattern.mid(2).toLower();
        QStringList &patterns = m_fastPatterns[extension]; // find or create
        if (!patterns.contains(glob.mimeType()))
            patterns.append(glob.mimeType());
    } else {
        if (glob.weight() > 50) {
            if (!m_highWeightGlobs.hasPattern(glob.mimeType(), glob.pattern()))
                m_highWeightGlobs.append(glob);
        } else {
            if (!m_lowWeightGlobs.hasPattern(glob.mimeType(), glob.pattern()))
                m_lowWeightGlobs.append(glob);
        }
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QMimeTypeParser may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMimeTypeParser : QMimeTypeParser {
  using QMimeTypeParser::process;
  using QMimeTypeParser::processParent;
  using QMimeTypeParser::processAlias;
  using QMimeTypeParser::processMagicMatcher;
};

//  A QMimeTypeParser that Python can take functions over in. Every QMimeTypeParser
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeTypeParserCall0)(const void *, const QMimeTypeXMLData *, QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeTypeParserCall1)(const void *, const QMimeGlobPattern *, QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeTypeParserCall2)(const void *, const QString *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeTypeParserCall3)(const void *, const QString *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeTypeParserCall4)(const void *, const QMimeMagicRuleMatcher *, int *);
#endif  // QT_CONFIG(mimetype)
class CuteQMimeTypeParser : public QMimeTypeParser {
public:
  using QMimeTypeParser::QMimeTypeParser;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN19QMimeTypeParserBase7processERK16QMimeTypeXMLDataP7QString")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN19QMimeTypeParserBase7processERK16QMimeGlobPatternP7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN19QMimeTypeParserBase13processParentERK7QStringS2_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN19QMimeTypeParserBase12processAliasERK7QStringS2_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN19QMimeTypeParserBase19processMagicMatcherERK21QMimeMagicRuleMatcher")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
    return false;
  }

#if QT_CONFIG(mimetype)
  //  bool QMimeTypeParser::process(const QMimeTypeXMLData &t, QString *a1)
  bool process(const QMimeTypeXMLData &t, QString *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMimeTypeParserCall0 call = reinterpret_cast<CuteQMimeTypeParserCall0>(taken[0]);
      bool given = call(this, &t, a1, &handled);
      if (handled) return given;
    }
    return QMimeTypeParser::process(t, a1);
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  bool QMimeTypeParser::process(const QMimeGlobPattern &glob, QString
  //      *a1)
  bool process(const QMimeGlobPattern &glob, QString *a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMimeTypeParserCall1 call = reinterpret_cast<CuteQMimeTypeParserCall1>(taken[1]);
      bool given = call(this, &glob, a1, &handled);
      if (handled) return given;
    }
    return QMimeTypeParser::process(glob, a1);
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeTypeParser::processParent(const QString &child, const
  //      QString &parent)
  void processParent(const QString &child, const QString &parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMimeTypeParserCall2 call = reinterpret_cast<CuteQMimeTypeParserCall2>(taken[2]);
      call(this, &child, &parent, &handled);
      if (handled) return;
    }
    QMimeTypeParser::processParent(child, parent);
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeTypeParser::processAlias(const QString &alias, const
  //      QString &name)
  void processAlias(const QString &alias, const QString &name) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMimeTypeParserCall3 call = reinterpret_cast<CuteQMimeTypeParserCall3>(taken[3]);
      call(this, &alias, &name, &handled);
      if (handled) return;
    }
    QMimeTypeParser::processAlias(alias, name);
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeTypeParser::processMagicMatcher(const QMimeMagicRuleMatcher
  //      &matcher)
  void processMagicMatcher(const QMimeMagicRuleMatcher &matcher) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMimeTypeParserCall4 call = reinterpret_cast<CuteQMimeTypeParserCall4>(taken[4]);
      call(this, &matcher, &handled);
      if (handled) return;
    }
    QMimeTypeParser::processMagicMatcher(matcher);
  }
#endif  // QT_CONFIG(mimetype)
};

//  QMimeTypeParser::~QMimeTypeParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMimeTypeParserD1Ev(QMimeTypeParser *self) {
  delete self;
}

//  bool QMimeTypeParser::process(const QMimeTypeXMLData &t, QString *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QMimeTypeParser7processERK16QMimeTypeXMLDataP7QString(
    QMimeTypeParser *self,
    const QMimeTypeXMLData *t,
    QString *a1) {
  return self->process(*t, a1);
}

//  bool QMimeTypeParser::process(const QMimeGlobPattern &glob, QString *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QMimeTypeParser7processERK16QMimeGlobPatternP7QString(
    QMimeTypeParser *self,
    const QMimeGlobPattern *glob,
    QString *a1) {
  return self->process(*glob, a1);
}

//  void QMimeTypeParser::processParent(const QString &child, const QString
//      &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMimeTypeParser13processParentERK7QStringS2_(
    QMimeTypeParser *self,
    const QString *child,
    const QString *parent) {
  self->processParent(*child, *parent);
}

//  void QMimeTypeParser::processAlias(const QString &alias, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMimeTypeParser12processAliasERK7QStringS2_(
    QMimeTypeParser *self,
    const QString *alias,
    const QString *name) {
  self->processAlias(*alias, *name);
}

//  void QMimeTypeParser::processMagicMatcher(const QMimeMagicRuleMatcher
//      &matcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMimeTypeParser19processMagicMatcherERK21QMimeMagicRuleMatcher(
    QMimeTypeParser *self,
    const QMimeMagicRuleMatcher *matcher) {
  self->processMagicMatcher(*matcher);
}

//  a Python function taken by a CuteQMimeTypeParser, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMimeTypeParser(
    QMimeTypeParser *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMimeTypeParser *>(self)->take(key, call);
}

//  bool QMimeTypeParser::process(const QMimeTypeXMLData &t, QString *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QMimeTypeParser7processERK16QMimeTypeXMLDataP7QString(
    QMimeTypeParser *self,
    const QMimeTypeXMLData *t,
    QString *a1) {
  return static_cast<OwnQMimeTypeParser *>(self)->OwnQMimeTypeParser::process(
      *t,
      a1);
}

//  bool QMimeTypeParser::process(const QMimeGlobPattern &glob, QString *a1)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QMimeTypeParser7processERK16QMimeGlobPatternP7QString(
    QMimeTypeParser *self,
    const QMimeGlobPattern *glob,
    QString *a1) {
  return static_cast<OwnQMimeTypeParser *>(self)->OwnQMimeTypeParser::process(
      *glob,
      a1);
}

//  void QMimeTypeParser::processParent(const QString &child, const QString
//      &parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QMimeTypeParser13processParentERK7QStringS2_(
    QMimeTypeParser *self,
    const QString *child,
    const QString *parent) {
  static_cast<OwnQMimeTypeParser *>(self)->OwnQMimeTypeParser::processParent(
      *child,
      *parent);
}

//  void QMimeTypeParser::processAlias(const QString &alias, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QMimeTypeParser12processAliasERK7QStringS2_(
    QMimeTypeParser *self,
    const QString *alias,
    const QString *name) {
  static_cast<OwnQMimeTypeParser *>(self)->OwnQMimeTypeParser::processAlias(
      *alias,
      *name);
}

//  void QMimeTypeParser::processMagicMatcher(const QMimeMagicRuleMatcher
//      &matcher)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QMimeTypeParser19processMagicMatcherERK21QMimeMagicRuleMatcher(
    QMimeTypeParser *self,
    const QMimeMagicRuleMatcher *matcher) {
  static_cast<OwnQMimeTypeParser *>(self)->OwnQMimeTypeParser::processMagicMatcher(
      *matcher);
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
