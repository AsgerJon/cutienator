//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionFocusRect::QStyleOptionFocusRect()
extern "C" Q_DECL_EXPORT
QStyleOptionFocusRect *ritual_ZN21QStyleOptionFocusRectC1Ev() {
  return new QStyleOptionFocusRect();
}

//  QStyleOptionFocusRect::QStyleOptionFocusRect(const QStyleOptionFocusRect
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionFocusRect *ritual_ZN21QStyleOptionFocusRectC1ERKS_(
    const QStyleOptionFocusRect *other) {
  return new QStyleOptionFocusRect(*other);
}

//  QStyleOptionFocusRect &QStyleOptionFocusRect::operator=(const
//      QStyleOptionFocusRect &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionFocusRect *ritual_ZN21QStyleOptionFocusRectaSERKS_(
    QStyleOptionFocusRect *self,
    const QStyleOptionFocusRect *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionFocusRect::QStyleOptionFocusRect(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionFocusRect *ritual_ZN21QStyleOptionFocusRectC1Ei(int version) {
  return new QStyleOptionFocusRect(version);
}

//  QStyleOptionFocusRect::~QStyleOptionFocusRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QStyleOptionFocusRectD1Ev(QStyleOptionFocusRect *self) {
  delete self;
}
