//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpalette_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpalette_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPalettePrivate::Data::Data(const Data &other)
extern "C" Q_DECL_EXPORT
QPalettePrivate::Data *ritual_ZN15QPalettePrivate4DataC1ERKS0_(
    const QPalettePrivate::Data *other) {
  return new QPalettePrivate::Data(*other);
}

//  QPalettePrivate::Data::Data()
extern "C" Q_DECL_EXPORT
QPalettePrivate::Data *ritual_ZN15QPalettePrivate4DataC1Ev() {
  return new QPalettePrivate::Data();
}

//  QPalettePrivate::Data::~Data()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPalettePrivate4DataD1Ev(QPalettePrivate::Data *self) {
  delete self;
}
