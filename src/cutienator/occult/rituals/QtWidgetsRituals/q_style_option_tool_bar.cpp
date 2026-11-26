//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(toolbar)
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionToolBar::QStyleOptionToolBar()
extern "C" Q_DECL_EXPORT
QStyleOptionToolBar *ritual_ZN19QStyleOptionToolBarC1Ev() {
  return new QStyleOptionToolBar();
}

//  QStyleOptionToolBar::QStyleOptionToolBar(const QStyleOptionToolBar
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionToolBar *ritual_ZN19QStyleOptionToolBarC1ERKS_(
    const QStyleOptionToolBar *other) {
  return new QStyleOptionToolBar(*other);
}

//  QStyleOptionToolBar &QStyleOptionToolBar::operator=(const
//      QStyleOptionToolBar &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionToolBar *ritual_ZN19QStyleOptionToolBaraSERKS_(
    QStyleOptionToolBar *self,
    const QStyleOptionToolBar *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionToolBar::QStyleOptionToolBar(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionToolBar *ritual_ZN19QStyleOptionToolBarC1Ei(int version) {
  return new QStyleOptionToolBar(version);
}

//  QStyleOptionToolBar::~QStyleOptionToolBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyleOptionToolBarD1Ev(QStyleOptionToolBar *self) {
  delete self;
}

#endif  // QT_CONFIG(toolbar)
