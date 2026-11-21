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

//  QStyleOptionFocusRect::~QStyleOptionFocusRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QStyleOptionFocusRectD1Ev(QStyleOptionFocusRect *self) {
  delete self;
}
