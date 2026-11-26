//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutglobal_p.h>
#include <QtQuickLayouts/QtQuickLayouts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuickLinearLayout::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickLinearLayout10metaObjectEv(
    const QQuickLinearLayout *self) {
  return self->metaObject();
}

//  void *QQuickLinearLayout::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickLinearLayout11qt_metacastEPKc(
    QQuickLinearLayout *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLinearLayout::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickLinearLayout11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLinearLayout *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickLinearLayout::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickLinearLayout2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickLinearLayout::tr(s, c, n));
}

//  void QQuickLinearLayout::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLinearLayout22qt_qmlMarker_anonymousEv(
    QQuickLinearLayout *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickLinearLayout::QQuickLinearLayout(Qt::Orientation orientation,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickLinearLayout *ritual_ZN18QQuickLinearLayoutC1EN2Qt11OrientationEP10QQuickItem(
    Qt::Orientation orientation,
    QQuickItem *parent) {
  return new QQuickLinearLayout(orientation, parent);
}

//  qreal QQuickLinearLayout::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickLinearLayout7spacingEv(
    const QQuickLinearLayout *self) {
  return self->spacing();
}

//  void QQuickLinearLayout::setSpacing(qreal spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLinearLayout10setSpacingEd(
    QQuickLinearLayout *self,
    qreal spacing) {
  self->setSpacing(spacing);
}

//  bool QQuickLinearLayout::uniformCellSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickLinearLayout16uniformCellSizesEv(
    const QQuickLinearLayout *self) {
  return self->uniformCellSizes();
}

//  void QQuickLinearLayout::setUniformCellSizes(bool uniformCellSizes)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLinearLayout19setUniformCellSizesEb(
    QQuickLinearLayout *self,
    bool uniformCellSizes) {
  self->setUniformCellSizes(uniformCellSizes);
}

//  void QQuickLinearLayout::insertLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLinearLayout17insertLayoutItemsEv(
    QQuickLinearLayout *self) {
  self->insertLayoutItems();
}

//  void QQuickLinearLayout::spacingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLinearLayout14spacingChangedEv(
    QQuickLinearLayout *self) {
  self->spacingChanged();
}

//  void QQuickLinearLayout::uniformCellSizesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLinearLayout23uniformCellSizesChangedEv(
    QQuickLinearLayout *self) {
  self->uniformCellSizesChanged();
}

//  QQuickLinearLayoutPrivate *QQuickLinearLayout::d_func()
extern "C" Q_DECL_EXPORT
QQuickLinearLayoutPrivate *ritual_ZN18QQuickLinearLayout6d_funcEv(
    QQuickLinearLayout *self) {
  return self->d_func();
}

//  const QQuickLinearLayoutPrivate *QQuickLinearLayout::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickLinearLayoutPrivate *ritual_ZNK18QQuickLinearLayout6d_funcEv(
    const QQuickLinearLayout *self) {
  return self->d_func();
}

//  void QQuickLinearLayout::insertLayoutItems()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickLinearLayout17insertLayoutItemsEv(
    QQuickLinearLayout *self) {
  self->QQuickLinearLayout::insertLayoutItems();
}
