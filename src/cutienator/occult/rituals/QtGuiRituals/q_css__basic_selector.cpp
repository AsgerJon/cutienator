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

//  QCss::BasicSelector::BasicSelector()
extern "C" Q_DECL_EXPORT
QCss::BasicSelector *ritual_ZN4QCss13BasicSelectorC1Ev() {
  return new QCss::BasicSelector();
}

//  QCss::BasicSelector::~BasicSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss13BasicSelectorD1Ev(QCss::BasicSelector *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
