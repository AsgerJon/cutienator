//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionDockWidget::QStyleOptionDockWidget()
extern "C" Q_DECL_EXPORT
QStyleOptionDockWidget *ritual_ZN22QStyleOptionDockWidgetC1Ev() {
  return new QStyleOptionDockWidget();
}

//  QStyleOptionDockWidget::QStyleOptionDockWidget(const
//      QStyleOptionDockWidget &other)
extern "C" Q_DECL_EXPORT
QStyleOptionDockWidget *ritual_ZN22QStyleOptionDockWidgetC1ERKS_(
    const QStyleOptionDockWidget *other) {
  return new QStyleOptionDockWidget(*other);
}

//  QStyleOptionDockWidget &QStyleOptionDockWidget::operator=(const
//      QStyleOptionDockWidget &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionDockWidget *ritual_ZN22QStyleOptionDockWidgetaSERKS_(
    QStyleOptionDockWidget *self,
    const QStyleOptionDockWidget *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionDockWidget::QStyleOptionDockWidget(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionDockWidget *ritual_ZN22QStyleOptionDockWidgetC1Ei(int version) {
  return new QStyleOptionDockWidget(version);
}

//  QStyleOptionDockWidget::~QStyleOptionDockWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleOptionDockWidgetD1Ev(QStyleOptionDockWidget *self) {
  delete self;
}
