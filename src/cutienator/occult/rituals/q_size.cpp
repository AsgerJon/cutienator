//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsize.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>

//  QSize::QSize()
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN5QSizeC1Ev() {
  return new QSize();
}

//  QSize::QSize(int w, int h)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN5QSizeC1Eii(int w, int h) {
  return new QSize(w, h);
}

//  bool QSize::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QSize6isNullEv(const QSize *self) {
  return self->isNull();
}

//  bool QSize::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QSize7isEmptyEv(const QSize *self) {
  return self->isEmpty();
}

//  bool QSize::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QSize7isValidEv(const QSize *self) {
  return self->isValid();
}

//  int QSize::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QSize5widthEv(const QSize *self) {
  return self->width();
}

//  int QSize::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QSize6heightEv(const QSize *self) {
  return self->height();
}

//  void QSize::setWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSize8setWidthEi(QSize *self, int w) {
  self->setWidth(w);
}

//  void QSize::setHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSize9setHeightEi(QSize *self, int h) {
  self->setHeight(h);
}

//  void QSize::transpose()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSize9transposeEv(QSize *self) {
  self->transpose();
}

//  QSize QSize::transposed() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize10transposedEv(const QSize *self) {
  return new QSize(self->transposed());
}

//  void QSize::scale(int w, int h, Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSize5scaleEiiN2Qt15AspectRatioModeE(
    QSize *self,
    int w,
    int h,
    Qt::AspectRatioMode mode) {
  self->scale(w, h, mode);
}

//  void QSize::scale(const QSize &s, Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSize5scaleERKS_N2Qt15AspectRatioModeE(
    QSize *self,
    const QSize *s,
    Qt::AspectRatioMode mode) {
  self->scale(*s, mode);
}

//  QSize QSize::scaled(int w, int h, Qt::AspectRatioMode mode) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize6scaledEiiN2Qt15AspectRatioModeE(
    const QSize *self,
    int w,
    int h,
    Qt::AspectRatioMode mode) {
  return new QSize(self->scaled(w, h, mode));
}

//  QSize QSize::scaled(const QSize &s, Qt::AspectRatioMode mode) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize6scaledERKS_N2Qt15AspectRatioModeE(
    const QSize *self,
    const QSize *s,
    Qt::AspectRatioMode mode) {
  return new QSize(self->scaled(*s, mode));
}

//  QSize QSize::expandedTo(const QSize &a0) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize10expandedToERKS_(
    const QSize *self,
    const QSize *a0) {
  return new QSize(self->expandedTo(*a0));
}

//  QSize QSize::boundedTo(const QSize &a0) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize9boundedToERKS_(const QSize *self, const QSize *a0) {
  return new QSize(self->boundedTo(*a0));
}

//  QSize QSize::grownBy(QMargins m) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize7grownByE8QMargins(
    const QSize *self,
    const QMargins *m) {
  return new QSize(self->grownBy(*m));
}

//  QSize QSize::shrunkBy(QMargins m) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QSize8shrunkByE8QMargins(
    const QSize *self,
    const QMargins *m) {
  return new QSize(self->shrunkBy(*m));
}

//  QSizeF QSize::toSizeF() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK5QSize7toSizeFEv(const QSize *self) {
  return new QSizeF(self->toSizeF());
}

//  QSize::~QSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QSizeD1Ev(QSize *self) {
  delete self;
}
