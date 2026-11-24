//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLineEditPrivate::SideWidgetEntry::SideWidgetEntry(QWidget *w, QAction
//      *a, int _flags)
extern "C" Q_DECL_EXPORT
QLineEditPrivate::SideWidgetEntry *ritual_ZN16QLineEditPrivate15SideWidgetEntryC1EP7QWidgetP7QActioni(
    QWidget *w,
    QAction *a,
    int _flags) {
  return new QLineEditPrivate::SideWidgetEntry(w, a, _flags);
}

//  QLineEditPrivate::SideWidgetEntry::~SideWidgetEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate15SideWidgetEntryD1Ev(
    QLineEditPrivate::SideWidgetEntry *self) {
  delete self;
}

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(lineedit)
