//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>

//  const QMetaObject *qdesigner_internal::QDesignerWidgetItem::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal19QDesignerWidgetItem10metaObjectEv(
    const qdesigner_internal::QDesignerWidgetItem *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::QDesignerWidgetItem::qt_metacast(const char
//      *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal19QDesignerWidgetItem11qt_metacastEPKc(
    qdesigner_internal::QDesignerWidgetItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString qdesigner_internal::QDesignerWidgetItem::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal19QDesignerWidgetItem2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::QDesignerWidgetItem::tr(s, c, n));
}

//  QWidget *qdesigner_internal::QDesignerWidgetItem::constWidget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal19QDesignerWidgetItem11constWidgetEv(
    const qdesigner_internal::QDesignerWidgetItem *self) {
  return self->constWidget();
}

//  bool qdesigner_internal::QDesignerWidgetItem::check(const QLayout
//      *layout, QWidget *w, Qt::Orientations *ptrToOrientations)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internal19QDesignerWidgetItem5checkEPK7QLayoutP7QWidgetP6QFlagsIN2Qt11OrientationEE(
    const QLayout *layout,
    QWidget *w,
    Qt::Orientations *ptrToOrientations) {
  return qdesigner_internal::QDesignerWidgetItem::check(
      layout,
      w,
      ptrToOrientations);
}

//  qdesigner_internal::QDesignerWidgetItem as the QWidgetItemV2 it is built
//      on
extern "C" Q_DECL_EXPORT
QWidgetItemV2 *ritual_cast_qdesigner_internal_QDesignerWidgetItem_QWidgetItemV2(
    qdesigner_internal::QDesignerWidgetItem *self) {
  return static_cast<QWidgetItemV2 *>(self);
}

//  QSize qdesigner_internal::QDesignerWidgetItem::minimumSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18qdesigner_internal19QDesignerWidgetItem11minimumSizeEv(
    const qdesigner_internal::QDesignerWidgetItem *self) {
  return new QSize(
      self->qdesigner_internal::QDesignerWidgetItem::minimumSize());
}

//  QSize qdesigner_internal::QDesignerWidgetItem::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18qdesigner_internal19QDesignerWidgetItem8sizeHintEv(
    const qdesigner_internal::QDesignerWidgetItem *self) {
  return new QSize(
      self->qdesigner_internal::QDesignerWidgetItem::sizeHint());
}

//  bool qdesigner_internal::QDesignerWidgetItem::eventFilter(QObject
//      *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18qdesigner_internal19QDesignerWidgetItem11eventFilterEP7QObjectP6QEvent(
    qdesigner_internal::QDesignerWidgetItem *self,
    QObject *watched,
    QEvent *event) {
  return self->qdesigner_internal::QDesignerWidgetItem::eventFilter(
      watched,
      event);
}
