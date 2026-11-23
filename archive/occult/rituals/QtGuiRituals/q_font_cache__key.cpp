//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/QtGui>
#include <QtGui/6.12.0/QtGui/private/qfont_p.h>

//  QFontCache::Key::Key()
extern "C" Q_DECL_EXPORT
QFontCache::Key *ritual_ZN10QFontCache3KeyC1Ev() {
  return new QFontCache::Key();
}

//  bool QFontCache::Key::operator<(const Key &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QFontCache3KeyltERKS0_(
    const QFontCache::Key *self,
    const QFontCache::Key *other) {
  return self->operator<(*other);
}

//  bool QFontCache::Key::operator==(const Key &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QFontCache3KeyeqERKS0_(
    const QFontCache::Key *self,
    const QFontCache::Key *other) {
  return self->operator==(*other);
}

//  QFontCache::Key::~Key()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFontCache3KeyD1Ev(QFontCache::Key *self) {
  delete self;
}
