//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSvgAnimatedStyle::QSvgAnimatedStyle()
extern "C" Q_DECL_EXPORT
QSvgAnimatedStyle *ritual_ZN17QSvgAnimatedStyleC1Ev() {
  return new QSvgAnimatedStyle();
}

//  QSvgAnimatedStyle::~QSvgAnimatedStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgAnimatedStyleD1Ev(QSvgAnimatedStyle *self) {
  delete self;
}

//  void QSvgAnimatedStyle::apply(QPainter *p, const QSvgNode *node,
//      QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgAnimatedStyle5applyEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgAnimatedStyle *self,
    QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->apply(p, node, *states);
}

//  void QSvgAnimatedStyle::revert(QPainter *p, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgAnimatedStyle6revertEP8QPainterR15QSvgExtraStates(
    QSvgAnimatedStyle *self,
    QPainter *p,
    QSvgExtraStates *states) {
  self->revert(p, *states);
}

//  void QSvgAnimatedStyle::savePaintingState(const QPainter *p, const
//      QSvgNode *node, QSvgExtraStates &states)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgAnimatedStyle17savePaintingStateEPK8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgAnimatedStyle *self,
    const QPainter *p,
    const QSvgNode *node,
    QSvgExtraStates *states) {
  self->savePaintingState(p, node, *states);
}

//  void QSvgAnimatedStyle::fetchStyleState(const QSvgAbstractAnimation
//      *animation, QSvgStyleState &currentStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgAnimatedStyle15fetchStyleStateEPK21QSvgAbstractAnimationR14QSvgStyleState(
    QSvgAnimatedStyle *self,
    const QSvgAbstractAnimation *animation,
    QSvgStyleState *currentStyle) {
  self->fetchStyleState(animation, *currentStyle);
}

//  void QSvgAnimatedStyle::applyStyle(QPainter *p, QSvgExtraStates &states,
//      const QSvgStyleState &currentStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgAnimatedStyle10applyStyleEP8QPainterR15QSvgExtraStatesRK14QSvgStyleState(
    QSvgAnimatedStyle *self,
    QPainter *p,
    QSvgExtraStates *states,
    const QSvgStyleState *currentStyle) {
  self->applyStyle(p, *states, *currentStyle);
}
