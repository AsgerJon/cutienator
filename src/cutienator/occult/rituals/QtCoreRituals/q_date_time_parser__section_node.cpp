//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(datetimeparser)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qdatetimeparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QDateTimeParser::SectionNode::SectionNode(Section tp, int ps, int ct, int
//      zs)
extern "C" Q_DECL_EXPORT
QDateTimeParser::SectionNode *ritual_ZN15QDateTimeParser11SectionNodeC1ENS_7SectionEiii(
    QDateTimeParser::Section tp,
    int ps,
    int ct,
    int zs) {
  return new QDateTimeParser::SectionNode(tp, ps, ct, zs);
}

//  QString QDateTimeParser::SectionNode::name(Section s)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QDateTimeParser11SectionNode4nameENS_7SectionE(
    QDateTimeParser::Section s) {
  return new QString(QDateTimeParser::SectionNode::name(s));
}

//  QString QDateTimeParser::SectionNode::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser11SectionNode4nameEv(
    const QDateTimeParser::SectionNode *self) {
  return new QString(self->name());
}

//  QString QDateTimeParser::SectionNode::format() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QDateTimeParser11SectionNode6formatEv(
    const QDateTimeParser::SectionNode *self) {
  return new QString(self->format());
}

//  int QDateTimeParser::SectionNode::maxChange() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QDateTimeParser11SectionNode9maxChangeEv(
    const QDateTimeParser::SectionNode *self) {
  return self->maxChange();
}

//  QDateTimeParser::SectionNode::~SectionNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDateTimeParser11SectionNodeD1Ev(
    QDateTimeParser::SectionNode *self) {
  delete self;
}

#endif  // QT_CONFIG(datetimeparser)
