//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datetimeparser)
#if QT_CONFIG(datetimeparser)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>

//  QDateTimeParser::StateNode::StateNode()
extern "C" Q_DECL_EXPORT
QDateTimeParser::StateNode *ritual_ZN15QDateTimeParser9StateNodeC1Ev() {
  return new QDateTimeParser::StateNode();
}

//  QDateTimeParser::StateNode::StateNode(const QDateTime &val, State ok, int
//      pad, bool bad)
extern "C" Q_DECL_EXPORT
QDateTimeParser::StateNode *ritual_ZN15QDateTimeParser9StateNodeC1ERK9QDateTimeNS_5StateEib(
    const QDateTime *val,
    QDateTimeParser::State ok,
    int pad,
    bool bad) {
  return new QDateTimeParser::StateNode(*val, ok, pad, bad);
}

//  QDateTimeParser::StateNode::~StateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDateTimeParser9StateNodeD1Ev(
    QDateTimeParser::StateNode *self) {
  delete self;
}

#endif  // QT_CONFIG(datetimeparser)
#endif  // QT_CONFIG(datetimeparser)
