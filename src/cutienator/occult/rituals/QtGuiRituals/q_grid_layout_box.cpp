//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGridLayoutBox::QGridLayoutBox()
extern "C" Q_DECL_EXPORT
QGridLayoutBox *ritual_ZN14QGridLayoutBoxC1Ev() {
  return new QGridLayoutBox();
}

//  void QGridLayoutBox::add(const QGridLayoutBox &other, int stretch, qreal
//      spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGridLayoutBox3addERKS_id(
    QGridLayoutBox *self,
    const QGridLayoutBox *other,
    int stretch,
    qreal spacing) {
  self->add(*other, stretch, spacing);
}

//  void QGridLayoutBox::combine(const QGridLayoutBox &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGridLayoutBox7combineERKS_(
    QGridLayoutBox *self,
    const QGridLayoutBox *other) {
  self->combine(*other);
}

//  void QGridLayoutBox::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGridLayoutBox9normalizeEv(QGridLayoutBox *self) {
  self->normalize();
}

//  const qreal &QGridLayoutBox::q_sizes(int which) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGridLayoutBox7q_sizesEi(
    const QGridLayoutBox *self,
    int which) {
  return self->q_sizes(which);
}

//  QGridLayoutBox::~QGridLayoutBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGridLayoutBoxD1Ev(QGridLayoutBox *self) {
  delete self;
}
