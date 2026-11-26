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

//  QStyleOptionHeader &QStyleOptionHeader::operator=(const
//      QStyleOptionHeader &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionHeader *ritual_ZN18QStyleOptionHeaderaSERKS_(
    QStyleOptionHeader *self,
    const QStyleOptionHeader *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionHeader::QStyleOptionHeader(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionHeader *ritual_ZN18QStyleOptionHeaderC1Ei(int version) {
  return new QStyleOptionHeader(version);
}

//  QStyleOptionHeader::~QStyleOptionHeader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStyleOptionHeaderD1Ev(QStyleOptionHeader *self) {
  delete self;
}
