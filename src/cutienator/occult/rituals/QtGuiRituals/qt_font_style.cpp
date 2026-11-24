//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtFontStyle::QtFontStyle(const Key &k)
extern "C" Q_DECL_EXPORT
QtFontStyle *ritual_ZN11QtFontStyleC1ERKNS_3KeyE(const QtFontStyle::Key *k) {
  return new QtFontStyle(*k);
}

//  QtFontStyle::~QtFontStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QtFontStyleD1Ev(QtFontStyle *self) {
  delete self;
}

//  QtFontSize *QtFontStyle::pixelSize(unsigned short size, bool a1)
extern "C" Q_DECL_EXPORT
QtFontSize *ritual_ZN11QtFontStyle9pixelSizeEtb(
    QtFontStyle *self,
    unsigned short size,
    bool a1) {
  return self->pixelSize(size, a1);
}
