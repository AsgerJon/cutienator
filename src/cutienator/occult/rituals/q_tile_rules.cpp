//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qdrawutil.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qdrawutil.h>

//  QTileRules::QTileRules(Qt::TileRule horizontalRule, Qt::TileRule
//      verticalRule)
extern "C" Q_DECL_EXPORT
QTileRules *ritual_ZN10QTileRulesC1EN2Qt8TileRuleES1_(
    Qt::TileRule horizontalRule,
    Qt::TileRule verticalRule) {
  return new QTileRules(horizontalRule, verticalRule);
}

//  QTileRules::QTileRules(Qt::TileRule rule)
extern "C" Q_DECL_EXPORT
QTileRules *ritual_ZN10QTileRulesC1EN2Qt8TileRuleE(Qt::TileRule rule) {
  return new QTileRules(rule);
}

//  QTileRules::~QTileRules()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTileRulesD1Ev(QTileRules *self) {
  delete self;
}
