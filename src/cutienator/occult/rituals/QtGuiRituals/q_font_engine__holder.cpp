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

//  QFontEngine::Holder::Holder(void *p, qt_destroy_func_t d)
extern "C" Q_DECL_EXPORT
QFontEngine::Holder *ritual_ZN11QFontEngine6HolderC1EPvPFvS1_E(
    void *p,
    void *d) {
  return new QFontEngine::Holder(p, reinterpret_cast<qt_destroy_func_t>(d));
}

//  QFontEngine::Holder::~Holder()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine6HolderD1Ev(QFontEngine::Holder *self) {
  delete self;
}

//  QFontEngine::Holder::Holder(Holder &&other)
extern "C" Q_DECL_EXPORT
QFontEngine::Holder *ritual_ZN11QFontEngine6HolderC1EOS0_(
    QFontEngine::Holder *other) {
  return new QFontEngine::Holder(std::move(*other));
}

//  Holder &QFontEngine::Holder::operator=(Holder &&other)
extern "C" Q_DECL_EXPORT
QFontEngine::Holder *ritual_ZN11QFontEngine6HolderaSEOS0_(
    QFontEngine::Holder *self,
    QFontEngine::Holder *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QFontEngine::Holder::swap(Holder &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine6Holder4swapERS0_(
    QFontEngine::Holder *self,
    QFontEngine::Holder *other) {
  self->swap(*other);
}

//  void *QFontEngine::Holder::get() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QFontEngine6Holder3getEv(const QFontEngine::Holder *self) {
  return self->get();
}

//  void *QFontEngine::Holder::release()
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QFontEngine6Holder7releaseEv(QFontEngine::Holder *self) {
  return self->release();
}

//  void QFontEngine::Holder::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontEngine6Holder5resetEv(QFontEngine::Holder *self) {
  self->reset();
}

//  qt_destroy_func_t QFontEngine::Holder::get_deleter() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QFontEngine6Holder11get_deleterEv(
    const QFontEngine::Holder *self) {
  return reinterpret_cast<void *>(self->get_deleter());
}

//  bool QFontEngine::Holder::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFontEngine6HolderntEv(const QFontEngine::Holder *self) {
  return self->operator!();
}
