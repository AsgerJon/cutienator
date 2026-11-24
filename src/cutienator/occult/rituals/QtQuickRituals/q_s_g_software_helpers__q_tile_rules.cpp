//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalimagenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGSoftwareHelpers::QTileRules::QTileRules(Qt::TileRule horizontalRule,
//      Qt::TileRule verticalRule)
extern "C" Q_DECL_EXPORT
QSGSoftwareHelpers::QTileRules *ritual_ZN18QSGSoftwareHelpers10QTileRulesC1EN2Qt8TileRuleES2_(
    Qt::TileRule horizontalRule,
    Qt::TileRule verticalRule) {
  return new QSGSoftwareHelpers::QTileRules(horizontalRule, verticalRule);
}

//  QSGSoftwareHelpers::QTileRules::QTileRules(Qt::TileRule rule)
extern "C" Q_DECL_EXPORT
QSGSoftwareHelpers::QTileRules *ritual_ZN18QSGSoftwareHelpers10QTileRulesC1EN2Qt8TileRuleE(
    Qt::TileRule rule) {
  return new QSGSoftwareHelpers::QTileRules(rule);
}

//  QSGSoftwareHelpers::QTileRules::~QTileRules()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSGSoftwareHelpers10QTileRulesD1Ev(
    QSGSoftwareHelpers::QTileRules *self) {
  delete self;
}
