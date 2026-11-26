//  Written by hand on 2026-11-25 from
//  QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qdrawutil_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt builds QuickNativeStyle for macOS and Windows only, so the whole
//  file stands under that. Qt's library offers nothing of this class
//  by name: only what its header writes out. The destructor is the
//  implicit one, written as 'delete self' for Python to free it.
//  Not written: the functions 'qDrawBorderPixmap' and the others of
//  the namespace, which are no part of this class.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_MACOS) || defined(Q_OS_WIN)
#include <QtQuickNativeStyle/6.12.0/QtQuickNativeStyle/private/qqc2qdrawutil_p.h>

//  QQC2::QTileRules::QTileRules(Qt::TileRule horizontalRule,
//      Qt::TileRule verticalRule)
extern "C" Q_DECL_EXPORT
QQC2::QTileRules *ritual_ZN4QQC210QTileRulesC1EN2Qt8TileRuleES2_(
    int horizontalRule,
    int verticalRule) {
  return new QQC2::QTileRules(
      static_cast<Qt::TileRule>(horizontalRule),
      static_cast<Qt::TileRule>(verticalRule));
}

//  QQC2::QTileRules::QTileRules(Qt::TileRule rule)
extern "C" Q_DECL_EXPORT
QQC2::QTileRules *ritual_ZN4QQC210QTileRulesC1EN2Qt8TileRuleE(int rule) {
  return new QQC2::QTileRules(static_cast<Qt::TileRule>(rule));
}

//  QQC2::QTileRules::~QTileRules()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QQC210QTileRulesD1Ev(QQC2::QTileRules *self) {
  delete self;
}

#endif  // defined(Q_OS_MACOS) || defined(Q_OS_WIN)
