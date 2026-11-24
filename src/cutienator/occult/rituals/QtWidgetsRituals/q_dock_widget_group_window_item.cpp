//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mainwindow)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  QDockWidgetGroupWindowItem::QDockWidgetGroupWindowItem(QDockWidgetGroupWi
//      ndow *parent)
extern "C" Q_DECL_EXPORT
QDockWidgetGroupWindowItem *ritual_ZN26QDockWidgetGroupWindowItemC1EP22QDockWidgetGroupWindow(
    QDockWidgetGroupWindow *parent) {
  return new QDockWidgetGroupWindowItem(parent);
}

//  QSize QDockWidgetGroupWindowItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK26QDockWidgetGroupWindowItem11minimumSizeEv(
    const QDockWidgetGroupWindowItem *self) {
  return new QSize(self->minimumSize());
}

//  QSize QDockWidgetGroupWindowItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK26QDockWidgetGroupWindowItem11maximumSizeEv(
    const QDockWidgetGroupWindowItem *self) {
  return new QSize(self->maximumSize());
}

//  QSize QDockWidgetGroupWindowItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK26QDockWidgetGroupWindowItem8sizeHintEv(
    const QDockWidgetGroupWindowItem *self) {
  return new QSize(self->sizeHint());
}

//  QWidget *QDockWidgetGroupWindowItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK26QDockWidgetGroupWindowItem6widgetEv(
    const QDockWidgetGroupWindowItem *self) {
  return self->widget();
}

//  QLayout *QDockWidgetGroupWindowItem::lay() const
extern "C" Q_DECL_EXPORT
QLayout *ritual_ZNK26QDockWidgetGroupWindowItem3layEv(
    const QDockWidgetGroupWindowItem *self) {
  return self->lay();
}

//  QSize QDockWidgetGroupWindowItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK26QDockWidgetGroupWindowItem11minimumSizeEv(
    const QDockWidgetGroupWindowItem *self) {
  return new QSize(self->QDockWidgetGroupWindowItem::minimumSize());
}

//  QSize QDockWidgetGroupWindowItem::maximumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK26QDockWidgetGroupWindowItem11maximumSizeEv(
    const QDockWidgetGroupWindowItem *self) {
  return new QSize(self->QDockWidgetGroupWindowItem::maximumSize());
}

//  QSize QDockWidgetGroupWindowItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK26QDockWidgetGroupWindowItem8sizeHintEv(
    const QDockWidgetGroupWindowItem *self) {
  return new QSize(self->QDockWidgetGroupWindowItem::sizeHint());
}

//  QWidget *QDockWidgetGroupWindowItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK26QDockWidgetGroupWindowItem6widgetEv(
    const QDockWidgetGroupWindowItem *self) {
  return self->QDockWidgetGroupWindowItem::widget();
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(mainwindow)
