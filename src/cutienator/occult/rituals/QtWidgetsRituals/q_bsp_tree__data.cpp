//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qbsptree_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qbsptree_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBspTree::Data::Data(int n)
extern "C" Q_DECL_EXPORT
QBspTree::Data *ritual_ZN8QBspTree4DataC1Ei(int n) {
  return new QBspTree::Data(n);
}

//  QBspTree::Data::~Data()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QBspTree4DataD1Ev(QBspTree::Data *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
