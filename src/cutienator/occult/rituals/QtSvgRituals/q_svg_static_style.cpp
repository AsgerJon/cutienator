//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSvgStaticStyle::QSvgStaticStyle()
extern "C" Q_DECL_EXPORT
QSvgStaticStyle *ritual_ZN15QSvgStaticStyleC1Ev() {
  return new QSvgStaticStyle();
}

//  QSvgStaticStyle::~QSvgStaticStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStaticStyleD1Ev(QSvgStaticStyle *self) {
  delete self;
}

//  void QSvgStaticStyle::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStaticStyle5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgStaticStyle *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgStaticStyle::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSvgStaticStyle6revertEP8QPainterR15QSvgExtraStates(
    QSvgStaticStyle *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  QSvgStyleProperty *QSvgStaticStyle::property(QSvgStyleProperty::Type
//      type) const
extern "C" Q_DECL_EXPORT
QSvgStyleProperty *ritual_ZNK15QSvgStaticStyle8propertyEN17QSvgStyleProperty4TypeE(
    const QSvgStaticStyle *self,
    QSvgStyleProperty::Type type) {
  return self->property(type);
}

//  bool QSvgStaticStyle::isDefaultProperty(QSvgStyleProperty::Type type)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSvgStaticStyle17isDefaultPropertyEN17QSvgStyleProperty4TypeE(
    const QSvgStaticStyle *self,
    QSvgStyleProperty::Type type) {
  return self->isDefaultProperty(type);
}
