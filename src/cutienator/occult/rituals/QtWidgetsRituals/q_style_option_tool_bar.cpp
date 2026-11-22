//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
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

//  QStyleOptionToolBar::~QStyleOptionToolBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyleOptionToolBarD1Ev(QStyleOptionToolBar *self) {
  delete self;
}
