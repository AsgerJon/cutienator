//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionFrame::QStyleOptionFrame()
extern "C" Q_DECL_EXPORT
QStyleOptionFrame *ritual_ZN17QStyleOptionFrameC1Ev() {
  return new QStyleOptionFrame();
}

//  QStyleOptionFrame::QStyleOptionFrame(const QStyleOptionFrame &other)
extern "C" Q_DECL_EXPORT
QStyleOptionFrame *ritual_ZN17QStyleOptionFrameC1ERKS_(
    const QStyleOptionFrame *other) {
  return new QStyleOptionFrame(*other);
}

//  QStyleOptionFrame &QStyleOptionFrame::operator=(const QStyleOptionFrame
//      &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionFrame *ritual_ZN17QStyleOptionFrameaSERKS_(
    QStyleOptionFrame *self,
    const QStyleOptionFrame *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionFrame::QStyleOptionFrame(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionFrame *ritual_ZN17QStyleOptionFrameC1Ei(int version) {
  return new QStyleOptionFrame(version);
}

//  QStyleOptionFrame::~QStyleOptionFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QStyleOptionFrameD1Ev(QStyleOptionFrame *self) {
  delete self;
}
