//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtFontStyle::Key::Key()
extern "C" Q_DECL_EXPORT
QtFontStyle::Key *ritual_ZN11QtFontStyle3KeyC1Ev() {
  return new QtFontStyle::Key();
}

//  QtFontStyle::Key::Key(const Key &o)
extern "C" Q_DECL_EXPORT
QtFontStyle::Key *ritual_ZN11QtFontStyle3KeyC1ERKS0_(
    const QtFontStyle::Key *o) {
  return new QtFontStyle::Key(*o);
}

//  bool QtFontStyle::Key::operator==(const Key &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QtFontStyle3KeyeqERKS0_(
    const QtFontStyle::Key *self,
    const QtFontStyle::Key *other) {
  return self->operator==(*other);
}

//  bool QtFontStyle::Key::operator!=(const Key &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QtFontStyle3KeyneERKS0_(
    const QtFontStyle::Key *self,
    const QtFontStyle::Key *other) {
  return self->operator!=(*other);
}

//  QtFontStyle::Key::~Key()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QtFontStyle3KeyD1Ev(QtFontStyle::Key *self) {
  delete self;
}
