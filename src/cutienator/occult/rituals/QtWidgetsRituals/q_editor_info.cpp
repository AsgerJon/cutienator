//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QEditorInfo::QEditorInfo(QWidget *e, bool s)
extern "C" Q_DECL_EXPORT
QEditorInfo *ritual_ZN11QEditorInfoC1EP7QWidgetb(QWidget *e, bool s) {
  return new QEditorInfo(e, s);
}

//  QEditorInfo::QEditorInfo()
extern "C" Q_DECL_EXPORT
QEditorInfo *ritual_ZN11QEditorInfoC1Ev() {
  return new QEditorInfo();
}

//  QEditorInfo::~QEditorInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEditorInfoD1Ev(QEditorInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
