//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame()
extern "C" Q_DECL_EXPORT
QStyleOptionTabWidgetFrame *ritual_ZN26QStyleOptionTabWidgetFrameC1Ev() {
  return new QStyleOptionTabWidgetFrame();
}

//  QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame(const
//      QStyleOptionTabWidgetFrame &other)
extern "C" Q_DECL_EXPORT
QStyleOptionTabWidgetFrame *ritual_ZN26QStyleOptionTabWidgetFrameC1ERKS_(
    const QStyleOptionTabWidgetFrame *other) {
  return new QStyleOptionTabWidgetFrame(*other);
}

//  QStyleOptionTabWidgetFrame::~QStyleOptionTabWidgetFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStyleOptionTabWidgetFrameD1Ev(
    QStyleOptionTabWidgetFrame *self) {
  delete self;
}
