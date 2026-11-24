//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qloggingregistry.cpp, line 39, as _ZN12QLoggingRuleC1Ev
inline QLoggingRule::QLoggingRule()
{
}

//  from src/corelib/io/qloggingregistry.cpp, line 57, as _ZNK12QLoggingRule4passE13QLatin1String9QtMsgType
inline int QLoggingRule::pass(QLatin1StringView cat, QtMsgType msgType) const
{
    // check message type
    if (messageType > -1 && messageType != msgType)
        return 0;

    if (flags == FullText) {
        // full match
        if (category == cat)
            return (enabled ? 1 : -1);
        else
            return 0;
    }

    const qsizetype idx = cat.indexOf(category);
    if (idx >= 0) {
        if (flags == MidFilter) {
            // matches somewhere
            return (enabled ? 1 : -1);
        } else if (flags == LeftFilter) {
            // matches left
            if (idx == 0)
                return (enabled ? 1 : -1);
        } else if (flags == RightFilter) {
            // matches right
            if (idx == (cat.size() - category.size()))
                return (enabled ? 1 : -1);
        }
    }
    return 0;
}
//  -----------------------------------------------------------------------

//  QLoggingRule::QLoggingRule()
extern "C" Q_DECL_EXPORT
QLoggingRule *ritual_ZN12QLoggingRuleC1Ev() {
  return new QLoggingRule();
}

//  int QLoggingRule::pass(QLatin1StringView categoryName, QtMsgType type)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLoggingRule4passE13QLatin1String9QtMsgType(
    const QLoggingRule *self,
    const QLatin1String *categoryName,
    QtMsgType type) {
  return self->pass(*categoryName, type);
}

//  QLoggingRule::~QLoggingRule()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLoggingRuleD1Ev(QLoggingRule *self) {
  delete self;
}

//  QList<QLoggingRule>::QList()
extern "C" Q_DECL_EXPORT
QList<QLoggingRule> *ritual_list_make_QLoggingRule() {
  return new QList<QLoggingRule>();
}

//  void QList<QLoggingRule>::append(const QLoggingRule &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLoggingRule(
    QList<QLoggingRule> *self,
    const QLoggingRule *element) {
  self->append(*element);
}

//  qsizetype QList<QLoggingRule>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLoggingRule(const QList<QLoggingRule> *self) {
  return self->size();
}

//  const QLoggingRule &QList<QLoggingRule>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLoggingRule *ritual_list_at_QLoggingRule(
    const QList<QLoggingRule> *self,
    long long index) {
  return new QLoggingRule(self->at(index));
}

//  QList<QLoggingRule>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLoggingRule(QList<QLoggingRule> *self) {
  delete self;
}
