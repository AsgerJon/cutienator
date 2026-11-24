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
#include <QtGui/qcolor.h>

//  QCss::ColorData::ColorData()
extern "C" Q_DECL_EXPORT
QCss::ColorData *ritual_ZN4QCss9ColorDataC1Ev() {
  return new QCss::ColorData();
}

//  QCss::ColorData::ColorData(const QColor &col)
extern "C" Q_DECL_EXPORT
QCss::ColorData *ritual_ZN4QCss9ColorDataC1ERK6QColor(const QColor *col) {
  return new QCss::ColorData(*col);
}

//  QCss::ColorData::ColorData(QPalette::ColorRole r)
extern "C" Q_DECL_EXPORT
QCss::ColorData *ritual_ZN4QCss9ColorDataC1EN8QPalette9ColorRoleE(
    QPalette::ColorRole r) {
  return new QCss::ColorData(r);
}

//  QCss::ColorData::~ColorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss9ColorDataD1Ev(QCss::ColorData *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
