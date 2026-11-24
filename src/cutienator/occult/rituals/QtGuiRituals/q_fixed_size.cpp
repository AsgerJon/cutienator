//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfixed_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  QFixedSize::QFixedSize()
extern "C" Q_DECL_EXPORT
QFixedSize *ritual_ZN10QFixedSizeC1Ev() {
  return new QFixedSize();
}

//  QFixedSize::QFixedSize(QFixed _width, QFixed _height)
extern "C" Q_DECL_EXPORT
QFixedSize *ritual_ZN10QFixedSizeC1E6QFixedS0_(
    const QFixed *_width,
    const QFixed *_height) {
  return new QFixedSize(*_width, *_height);
}

//  QSizeF QFixedSize::toSizeF() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK10QFixedSize7toSizeFEv(const QFixedSize *self) {
  return new QSizeF(self->toSizeF());
}

//  QFixedSize QFixedSize::fromSizeF(const QSizeF &s)
extern "C" Q_DECL_EXPORT
QFixedSize *ritual_ZN10QFixedSize9fromSizeFERK6QSizeF(const QSizeF *s) {
  return new QFixedSize(QFixedSize::fromSizeF(*s));
}

//  QFixedSize::~QFixedSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QFixedSizeD1Ev(QFixedSize *self) {
  delete self;
}
