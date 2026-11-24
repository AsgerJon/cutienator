//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treeview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTreeViewItem::QTreeViewItem()
extern "C" Q_DECL_EXPORT
QTreeViewItem *ritual_ZN13QTreeViewItemC1Ev() {
  return new QTreeViewItem();
}

//  QTreeViewItem::~QTreeViewItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTreeViewItemD1Ev(QTreeViewItem *self) {
  delete self;
}

#endif  // QT_CONFIG(treeview)
