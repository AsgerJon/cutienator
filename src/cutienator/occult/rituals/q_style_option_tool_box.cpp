//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionToolBox::QStyleOptionToolBox()
extern "C" Q_DECL_EXPORT
QStyleOptionToolBox *ritual_ZN19QStyleOptionToolBoxC1Ev() {
  return new QStyleOptionToolBox();
}

//  QStyleOptionToolBox::QStyleOptionToolBox(const QStyleOptionToolBox
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionToolBox *ritual_ZN19QStyleOptionToolBoxC1ERKS_(
    const QStyleOptionToolBox *other) {
  return new QStyleOptionToolBox(*other);
}

//  QStyleOptionToolBox::~QStyleOptionToolBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyleOptionToolBoxD1Ev(QStyleOptionToolBox *self) {
  delete self;
}
