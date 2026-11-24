//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QFontEngine::Holder::Holder()
extern "C" Q_DECL_EXPORT
QFontEngine::Holder *ritual_ZN11QFontEngine6HolderC1Ev() {
  return new QFontEngine::Holder();
}

//  QFontEngine::Holder::~Holder()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine6HolderD1Ev(QFontEngine::Holder *self) {
  delete self;
}

//  void QFontEngine::Holder::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine6Holder5resetEv(QFontEngine::Holder *self) {
  self->reset();
}

//  bool QFontEngine::Holder::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine6HolderntEv(const QFontEngine::Holder *self) {
  return self->operator!();
}
