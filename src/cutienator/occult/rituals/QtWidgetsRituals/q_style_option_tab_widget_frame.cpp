//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(tabwidget)
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

//  QStyleOptionTabWidgetFrame &QStyleOptionTabWidgetFrame::operator=(const
//      QStyleOptionTabWidgetFrame &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionTabWidgetFrame *ritual_ZN26QStyleOptionTabWidgetFrameaSERKS_(
    QStyleOptionTabWidgetFrame *self,
    const QStyleOptionTabWidgetFrame *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionTabWidgetFrame::QStyleOptionTabWidgetFrame(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionTabWidgetFrame *ritual_ZN26QStyleOptionTabWidgetFrameC1Ei(
    int version) {
  return new QStyleOptionTabWidgetFrame(version);
}

//  QStyleOptionTabWidgetFrame::~QStyleOptionTabWidgetFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStyleOptionTabWidgetFrameD1Ev(
    QStyleOptionTabWidgetFrame *self) {
  delete self;
}

#endif  // QT_CONFIG(tabwidget)
