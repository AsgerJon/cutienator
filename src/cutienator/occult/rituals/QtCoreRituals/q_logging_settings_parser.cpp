//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qloggingregistry_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/qstringtokenizer.h>
#include <QtCore/qdir.h>
#include <QtCore/qcoreapplication.h>
#include <qplatformdefs.h>
#if QT_CONFIG(settings)
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#endif
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/private/qtools_p.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qsavefile.h>
#include <QtCore/qlockfile.h>
#endif
#ifdef Q_OS_VXWORKS
#  include <ioLib.h>
#endif
#include <algorithm>
#include <stdlib.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#  include <shlobj.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qloggingregistry.cpp, line 25, as local:qloggingregistry.cpp:warnMsg
#define warnMsg QMessageLogger(QT_MESSAGELOG_FILE, QT_MESSAGELOG_LINE, QT_MESSAGELOG_FUNC, "qt.core.logging").warning

//  from src/corelib/io/qloggingregistry.cpp, line 209, as _ZN22QLoggingSettingsParser13parseNextLineE11QStringView
inline void QLoggingSettingsParser::parseNextLine(QStringView line)
{
    // Remove whitespace at start and end of line:
    line = line.trimmed();

    // comment
    if (line.startsWith(u';'))
        return;

    if (line.startsWith(u'[') && line.endsWith(u']')) {
        // new section
        auto sectionName = line.mid(1).chopped(1).trimmed();
        m_inRulesSection = sectionName.compare("rules"_L1, Qt::CaseInsensitive) == 0;
        return;
    }

    if (m_inRulesSection) {
        const qsizetype equalPos = line.indexOf(u'=');
        if (equalPos != -1) {
            if (line.lastIndexOf(u'=') == equalPos) {
                const auto key = line.left(equalPos).trimmed();
#if QT_CONFIG(settings)
                QString tmp;
                QSettingsPrivate::iniUnescapedKey(key.toUtf8(), tmp);
                QStringView pattern = qToStringViewIgnoringNull(tmp);
#else
                QStringView pattern = key;
#endif
                const auto valueStr = line.mid(equalPos + 1).trimmed();
                int value = -1;
                if (valueStr == "true"_L1)
                    value = 1;
                else if (valueStr == "false"_L1)
                    value = 0;
                QLoggingRule rule(pattern, (value == 1));
                if (rule.flags != 0 && (value != -1))
                    _rules.append(std::move(rule));
                else
                    warnMsg("Ignoring malformed logging rule: '%s'", line.toUtf8().constData());
            } else {
                warnMsg("Ignoring malformed logging rule: '%s'", line.toUtf8().constData());
            }
        }
    }
}

//  from src/corelib/io/qloggingregistry.cpp, line 47, as _ZN12QLoggingRuleC1E11QStringViewb
inline QLoggingRule::QLoggingRule(QStringView pattern, bool enabled) : enabled(enabled)
{
    parse(pattern);
}

//  from src/corelib/io/qsettings.cpp, line 526, as _ZN16QSettingsPrivate15iniUnescapedKeyE14QByteArrayViewR7QString
inline bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, QString &result)
{
    const QString decoded = QString::fromUtf8(key);
    const qsizetype size = decoded.size();
    result.reserve(result.size() + size);
    qsizetype i = 0;
    bool lowercaseOnly = true;
    while (i < size) {
        char16_t ch = decoded.at(i).unicode();

        if (ch == '\\') {
            result += u'/';
            ++i;
            continue;
        }

        if (ch != '%' || i == size - 1) {
            QChar qch(ch);
            if (qch.isUpper())
                lowercaseOnly = false;
            result += qch;
            ++i;
            continue;
        }

        int numDigits = 2;
        qsizetype firstDigitPos = i + 1;

        ch = decoded.at(i + 1).unicode();
        if (ch == 'U') {
            ++firstDigitPos;
            numDigits = 4;
        }

        if (firstDigitPos + numDigits > size) {
            result += u'%';
            ++i;
            continue;
        }

        bool ok;
        ch = QStringView(decoded).sliced(firstDigitPos, numDigits).toUShort(&ok, 16);
        if (!ok) {
            result += u'%';
            ++i;
            continue;
        }

        QChar qch(ch);
        if (qch.isUpper())
            lowercaseOnly = false;
        result += qch;
        i = firstDigitPos + numDigits;
    }
    return lowercaseOnly;
}

//  from src/corelib/io/qloggingregistry.cpp, line 98, as _ZN12QLoggingRule5parseE11QStringView
inline void QLoggingRule::parse(QStringView pattern)
{
    QStringView p;

    // strip trailing ".messagetype"
    if (pattern.endsWith(".debug"_L1)) {
        p = pattern.chopped(6); // strlen(".debug")
        messageType = QtDebugMsg;
    } else if (pattern.endsWith(".info"_L1)) {
        p = pattern.chopped(5); // strlen(".info")
        messageType = QtInfoMsg;
    } else if (pattern.endsWith(".warning"_L1)) {
        p = pattern.chopped(8); // strlen(".warning")
        messageType = QtWarningMsg;
    } else if (pattern.endsWith(".critical"_L1)) {
        p = pattern.chopped(9); // strlen(".critical")
        messageType = QtCriticalMsg;
    } else {
        p = pattern;
    }

    const QChar asterisk = u'*';
    if (!p.contains(asterisk)) {
        flags = FullText;
    } else {
        if (p.endsWith(asterisk)) {
            flags |= LeftFilter;
            p = p.chopped(1);
        }
        if (p.startsWith(asterisk)) {
            flags |= RightFilter;
            p = p.mid(1);
        }
        if (p.contains(asterisk)) // '*' only supported at start/end
            flags = PatternFlags();
    }

    category = p.toString();
}

//  from src/corelib/io/qloggingregistry.cpp, line 157, as _ZN22QLoggingSettingsParser10setContentE11QStringViewDs
inline void QLoggingSettingsParser::setContent(QStringView content, char16_t separator)
{
    _rules.clear();
    for (auto line : qTokenize(content, separator))
        parseNextLine(line);
}

//  from src/corelib/io/qloggingregistry.cpp, line 168, as _ZN22QLoggingSettingsParser10setContentEP8_IO_FILE
inline void QLoggingSettingsParser::setContent(FILE *stream)
{
    _rules.clear();

    constexpr size_t ChunkSize = 240;
    QByteArray buffer(ChunkSize, Qt::Uninitialized);
    auto readline = [&](FILE *stream) {
        // Read one line into the buffer

        // fgets() always writes the terminating null into the buffer, so we'll
        // allow it to write to the QByteArray's null (thus the off by 1).
        Q_ASSERT(buffer.size() + 1 == int(buffer.size() + 1));
        char *s = fgets(buffer.begin(), int(buffer.size() + 1), stream);
        if (!s)
            return QByteArrayView{};

        qsizetype len = strlen(s);
        while (len == buffer.size()) {
            // need to grow the buffer
            buffer.resizeForOverwrite(buffer.size() + ChunkSize);
            s = fgets(buffer.end() - ChunkSize, ChunkSize + 1, stream);
            if (!s)
                break;
            len += strlen(s);
        }
        QByteArrayView result(buffer.constBegin(), len);
        if (result.endsWith('\n'))
            result.chop(1);
        return result;
    };

    QByteArrayView line;
    while (!(line = readline(stream)).isNull())
        parseNextLine(QString::fromUtf8(line));
}
//  -----------------------------------------------------------------------

//  void QLoggingSettingsParser::setImplicitRulesSection(bool inRulesSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLoggingSettingsParser23setImplicitRulesSectionEb(
    QLoggingSettingsParser *self,
    bool inRulesSection) {
  self->setImplicitRulesSection(inRulesSection);
}

//  void QLoggingSettingsParser::setContent(QStringView content, char16_t
//      separator)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLoggingSettingsParser10setContentE11QStringViewDs(
    QLoggingSettingsParser *self,
    const QString *content,
    char16_t separator) {
  self->setContent(QStringView(*content), separator);
}

//  void QLoggingSettingsParser::setContent(FILE *stream)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLoggingSettingsParser10setContentEP8_IO_FILE(
    QLoggingSettingsParser *self,
    FILE *stream) {
  self->setContent(stream);
}

//  QList<QLoggingRule> QLoggingSettingsParser::rules() const
extern "C" Q_DECL_EXPORT
QList<QLoggingRule> *ritual_ZNK22QLoggingSettingsParser5rulesEv(
    const QLoggingSettingsParser *self) {
  return new QList<QLoggingRule>(self->rules());
}

//  QLoggingSettingsParser::~QLoggingSettingsParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLoggingSettingsParserD1Ev(QLoggingSettingsParser *self) {
  delete self;
}
