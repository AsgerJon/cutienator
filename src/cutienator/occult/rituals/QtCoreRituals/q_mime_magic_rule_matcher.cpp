//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimemagicrulematcher_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimemagicrulematcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimemagicrule_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimemagicrule_p.h>
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/QList>
#include <QtCore/QDebug>
#include <QtCore/qendian.h>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/private/qmimetype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 49, as _ZNK14QMimeMagicRuleeqERKS_
inline bool QMimeMagicRule::operator==(const QMimeMagicRule &other) const
{
    return m_type == other.m_type &&
           m_value == other.m_value &&
           m_startPos == other.m_startPos &&
           m_endPos == other.m_endPos &&
           m_mask == other.m_mask &&
           m_pattern == other.m_pattern &&
           m_number == other.m_number &&
           m_numberMask == other.m_numberMask &&
           m_matchFunction == other.m_matchFunction;
}

//  from src/corelib/mimetypes/qmimemagicrule.cpp, line 325, as _ZNK14QMimeMagicRule7matchesERK10QByteArray
inline bool QMimeMagicRule::matches(const QByteArray &data) const
{
    const bool ok = m_matchFunction && (this->*m_matchFunction)(data);
    if (!ok)
        return false;

    // No submatch? Then we are done.
    if (m_subMatches.isEmpty())
        return true;

    //qDebug() << "Checking" << m_subMatches.count() << "sub-rules";
    // Check that one of the submatches matches too
    for ( QList<QMimeMagicRule>::const_iterator it = m_subMatches.begin(), end = m_subMatches.end() ;
          it != end ; ++it ) {
        if ((*it).matches(data)) {
            // One of the hierarchies matched -> mimetype recognized.
            return true;
        }
    }
    return false;


}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 26, as _ZN21QMimeMagicRuleMatcherC1ERK7QStringj
inline QMimeMagicRuleMatcher::QMimeMagicRuleMatcher(const QString &mime, unsigned thePriority) :
    m_list(),
    m_priority(thePriority),
    m_mimetype(mime)
{
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 33, as _ZNK21QMimeMagicRuleMatchereqERKS_
inline bool QMimeMagicRuleMatcher::operator==(const QMimeMagicRuleMatcher &other) const
{
    return m_list == other.m_list &&
           m_priority == other.m_priority;
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 39, as _ZN21QMimeMagicRuleMatcher7addRuleERK14QMimeMagicRule
inline void QMimeMagicRuleMatcher::addRule(const QMimeMagicRule &rule)
{
    m_list.append(rule);
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 44, as _ZN21QMimeMagicRuleMatcher8addRulesERK5QListI14QMimeMagicRuleE
inline void QMimeMagicRuleMatcher::addRules(const QList<QMimeMagicRule> &rules)
{
    m_list.append(rules);
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 49, as _ZNK21QMimeMagicRuleMatcher10magicRulesEv
inline QList<QMimeMagicRule> QMimeMagicRuleMatcher::magicRules() const
{
    return m_list;
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 55, as _ZNK21QMimeMagicRuleMatcher7matchesERK10QByteArray
inline bool QMimeMagicRuleMatcher::matches(const QByteArray &data) const
{
    for (const QMimeMagicRule &magicRule : m_list) {
        if (magicRule.matches(data))
            return true;
    }

    return false;
}

//  from src/corelib/mimetypes/qmimemagicrulematcher.cpp, line 66, as _ZNK21QMimeMagicRuleMatcher8priorityEv
inline unsigned QMimeMagicRuleMatcher::priority() const
{
    return m_priority;
}
//  -----------------------------------------------------------------------

//  QMimeMagicRuleMatcher::QMimeMagicRuleMatcher(const QString &mime,
//      unsigned int priority)
extern "C" Q_DECL_EXPORT
QMimeMagicRuleMatcher *ritual_ZN21QMimeMagicRuleMatcherC1ERK7QStringj(
    const QString *mime,
    unsigned int priority) {
  return new QMimeMagicRuleMatcher(*mime, priority);
}

//  void QMimeMagicRuleMatcher::swap(QMimeMagicRuleMatcher &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMimeMagicRuleMatcher4swapERS_(
    QMimeMagicRuleMatcher *self,
    QMimeMagicRuleMatcher *other) {
  self->swap(*other);
}

//  bool QMimeMagicRuleMatcher::operator==(const QMimeMagicRuleMatcher
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QMimeMagicRuleMatchereqERKS_(
    const QMimeMagicRuleMatcher *self,
    const QMimeMagicRuleMatcher *other) {
  return self->operator==(*other);
}

//  void QMimeMagicRuleMatcher::addRule(const QMimeMagicRule &rule)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMimeMagicRuleMatcher7addRuleERK14QMimeMagicRule(
    QMimeMagicRuleMatcher *self,
    const QMimeMagicRule *rule) {
  self->addRule(*rule);
}

//  void QMimeMagicRuleMatcher::addRules(const QList<QMimeMagicRule> &rules)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMimeMagicRuleMatcher8addRulesERK5QListI14QMimeMagicRuleE(
    QMimeMagicRuleMatcher *self,
    const QList<QMimeMagicRule> *rules) {
  self->addRules(*rules);
}

//  QList<QMimeMagicRule> QMimeMagicRuleMatcher::magicRules() const
extern "C" Q_DECL_EXPORT
QList<QMimeMagicRule> *ritual_ZNK21QMimeMagicRuleMatcher10magicRulesEv(
    const QMimeMagicRuleMatcher *self) {
  return new QList<QMimeMagicRule>(self->magicRules());
}

//  bool QMimeMagicRuleMatcher::matches(const QByteArray &data) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QMimeMagicRuleMatcher7matchesERK10QByteArray(
    const QMimeMagicRuleMatcher *self,
    const QByteArray *data) {
  return self->matches(*data);
}

//  unsigned int QMimeMagicRuleMatcher::priority() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK21QMimeMagicRuleMatcher8priorityEv(
    const QMimeMagicRuleMatcher *self) {
  return self->priority();
}

//  QString QMimeMagicRuleMatcher::mimetype() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QMimeMagicRuleMatcher8mimetypeEv(
    const QMimeMagicRuleMatcher *self) {
  return new QString(self->mimetype());
}

//  QMimeMagicRuleMatcher::~QMimeMagicRuleMatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMimeMagicRuleMatcherD1Ev(QMimeMagicRuleMatcher *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
