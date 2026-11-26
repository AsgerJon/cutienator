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
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h>
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

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 24, as local:qmimetypeparser.cpp:mimeInfoTagC
static const char mimeInfoTagC[] = "mime-info";

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 25, as local:qmimetypeparser.cpp:mimeTypeTagC
static const char mimeTypeTagC[] = "mime-type";

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 26, as local:qmimetypeparser.cpp:mimeTypeAttributeC
static const char mimeTypeAttributeC[] = "type";

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 31, as local:qmimetypeparser.cpp:nameAttributeC
static const char nameAttributeC[] = "name";

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 76, as _ZN19QMimeTypeParserBaseD2Ev
inline QMimeTypeParserBase::~QMimeTypeParserBase()
    = default;

//  from src/corelib/mimetypes/qmimetypeparser.cpp, line 137, as _ZN19QMimeTypeParserBase11parseNumberE11QStringViewPiP7QString
inline bool QMimeTypeParserBase::parseNumber(QStringView n, int *target, QString *errorMessage)
{
    bool ok;
    *target = n.toInt(&ok);
    if (Q_UNLIKELY(!ok)) {
        if (errorMessage)
            *errorMessage = "Not a number '"_L1 + n + "'."_L1;
        return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  A QMimeTypeParserBase that Python can take functions over in. Every QMimeTypeParserBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeTypeParserBaseCall0)(const void *, const QMimeTypeXMLData *, QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeTypeParserBaseCall1)(const void *, const QMimeGlobPattern *, QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeTypeParserBaseCall2)(const void *, const QString *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeTypeParserBaseCall3)(const void *, const QString *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeTypeParserBaseCall4)(const void *, const QMimeMagicRuleMatcher *, int *);
#endif  // QT_CONFIG(mimetype)
class CuteQMimeTypeParserBase : public QMimeTypeParserBase {
public:
  using QMimeTypeParserBase::QMimeTypeParserBase;
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
  //  bool QMimeTypeParserBase::process(const QMimeTypeXMLData &t, QString
  //      *errorMessage)
  bool process(const QMimeTypeXMLData &t, QString *errorMessage) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMimeTypeParserBaseCall0 call = reinterpret_cast<CuteQMimeTypeParserBaseCall0>(taken[0]);
      bool given = call(this, &t, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  bool QMimeTypeParserBase::process(const QMimeGlobPattern &t, QString
  //      *errorMessage)
  bool process(const QMimeGlobPattern &t, QString *errorMessage) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMimeTypeParserBaseCall1 call = reinterpret_cast<CuteQMimeTypeParserBaseCall1>(taken[1]);
      bool given = call(this, &t, errorMessage, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeTypeParserBase::processParent(const QString &child, const
  //      QString &parent)
  void processParent(const QString &child, const QString &parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMimeTypeParserBaseCall2 call = reinterpret_cast<CuteQMimeTypeParserBaseCall2>(taken[2]);
      call(this, &child, &parent, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeTypeParserBase::processAlias(const QString &alias, const
  //      QString &name)
  void processAlias(const QString &alias, const QString &name) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMimeTypeParserBaseCall3 call = reinterpret_cast<CuteQMimeTypeParserBaseCall3>(taken[3]);
      call(this, &alias, &name, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeTypeParserBase::processMagicMatcher(const
  //      QMimeMagicRuleMatcher &matcher)
  void processMagicMatcher(const QMimeMagicRuleMatcher &matcher) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMimeTypeParserBaseCall4 call = reinterpret_cast<CuteQMimeTypeParserBaseCall4>(taken[4]);
      call(this, &matcher, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(mimetype)
};

//  QMimeTypeParserBase::QMimeTypeParserBase()
extern "C" Q_DECL_EXPORT
QMimeTypeParserBase *ritual_ZN19QMimeTypeParserBaseC1Ev() {
  return new CuteQMimeTypeParserBase();
}

//  QMimeTypeParserBase::~QMimeTypeParserBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeTypeParserBaseD1Ev(QMimeTypeParserBase *self) {
  delete self;
}

//  bool QMimeTypeParserBase::parseNumber(QStringView n, int *target, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMimeTypeParserBase11parseNumberE11QStringViewPiP7QString(
    const QString *n,
    int *target,
    QString *errorMessage) {
  return QMimeTypeParserBase::parseNumber(
      QStringView(*n),
      target,
      errorMessage);
}

//  bool QMimeTypeParserBase::process(const QMimeTypeXMLData &t, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMimeTypeParserBase7processERK16QMimeTypeXMLDataP7QString(
    QMimeTypeParserBase *self,
    const QMimeTypeXMLData *t,
    QString *errorMessage) {
  return self->process(*t, errorMessage);
}

//  bool QMimeTypeParserBase::process(const QMimeGlobPattern &t, QString
//      *errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMimeTypeParserBase7processERK16QMimeGlobPatternP7QString(
    QMimeTypeParserBase *self,
    const QMimeGlobPattern *t,
    QString *errorMessage) {
  return self->process(*t, errorMessage);
}

//  void QMimeTypeParserBase::processParent(const QString &child, const
//      QString &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeTypeParserBase13processParentERK7QStringS2_(
    QMimeTypeParserBase *self,
    const QString *child,
    const QString *parent) {
  self->processParent(*child, *parent);
}

//  void QMimeTypeParserBase::processAlias(const QString &alias, const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeTypeParserBase12processAliasERK7QStringS2_(
    QMimeTypeParserBase *self,
    const QString *alias,
    const QString *name) {
  self->processAlias(*alias, *name);
}

//  void QMimeTypeParserBase::processMagicMatcher(const QMimeMagicRuleMatcher
//      &matcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QMimeTypeParserBase19processMagicMatcherERK21QMimeMagicRuleMatcher(
    QMimeTypeParserBase *self,
    const QMimeMagicRuleMatcher *matcher) {
  self->processMagicMatcher(*matcher);
}

//  a Python function taken by a CuteQMimeTypeParserBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMimeTypeParserBase(
    QMimeTypeParserBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMimeTypeParserBase *>(self)->take(key, call);
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
