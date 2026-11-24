//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(cssparser)
#if !defined(QT_NO_CSSPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>

//  QCss::BrushData::BrushData()
extern "C" Q_DECL_EXPORT
QCss::BrushData *ritual_ZN4QCss9BrushDataC1Ev() {
  return new QCss::BrushData();
}

//  QCss::BrushData::BrushData(const QBrush &br)
extern "C" Q_DECL_EXPORT
QCss::BrushData *ritual_ZN4QCss9BrushDataC1ERK6QBrush(const QBrush *br) {
  return new QCss::BrushData(*br);
}

//  QCss::BrushData::BrushData(QPalette::ColorRole r)
extern "C" Q_DECL_EXPORT
QCss::BrushData *ritual_ZN4QCss9BrushDataC1EN8QPalette9ColorRoleE(
    QPalette::ColorRole r) {
  return new QCss::BrushData(r);
}

//  QCss::BrushData::~BrushData()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss9BrushDataD1Ev(QCss::BrushData *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
