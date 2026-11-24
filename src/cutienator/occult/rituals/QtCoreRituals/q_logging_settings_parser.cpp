//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qloggingregistry_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qloggingregistry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  void QLoggingSettingsParser::setImplicitRulesSection(bool inRulesSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLoggingSettingsParser23setImplicitRulesSectionEb(
    QLoggingSettingsParser *self,
    bool inRulesSection) {
  self->setImplicitRulesSection(inRulesSection);
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
