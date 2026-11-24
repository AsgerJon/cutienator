//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qbinaryjson_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBinaryJsonPrivate::IsValidFrame::IsValidFrame(const Base *b, uint sz)
extern "C" Q_DECL_EXPORT
QBinaryJsonPrivate::IsValidFrame *ritual_ZN18QBinaryJsonPrivate12IsValidFrameC1EPKNS_4BaseEj(
    const QBinaryJsonPrivate::Base *b,
    uint sz) {
  return new QBinaryJsonPrivate::IsValidFrame(b, sz);
}

//  QBinaryJsonPrivate::IsValidFrame::~IsValidFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QBinaryJsonPrivate12IsValidFrameD1Ev(
    QBinaryJsonPrivate::IsValidFrame *self) {
  delete self;
}
