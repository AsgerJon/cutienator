//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionHeader::QStyleOptionHeader()
extern "C" Q_DECL_EXPORT
QStyleOptionHeader *ritual_ZN18QStyleOptionHeaderC1Ev() {
  return new QStyleOptionHeader();
}

//  QStyleOptionHeader::QStyleOptionHeader(const QStyleOptionHeader &other)
extern "C" Q_DECL_EXPORT
QStyleOptionHeader *ritual_ZN18QStyleOptionHeaderC1ERKS_(
    const QStyleOptionHeader *other) {
  return new QStyleOptionHeader(*other);
}

//  QStyleOptionHeader::~QStyleOptionHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStyleOptionHeaderD1Ev(QStyleOptionHeader *self) {
  delete self;
}
