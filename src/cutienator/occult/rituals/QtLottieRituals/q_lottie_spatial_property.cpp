//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiespatialproperty_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <QtCore/QPointF>
#include <QtCore/QJsonObject>

//  void QLottieSpatialProperty::construct(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLottieSpatialProperty9constructERK11QJsonObject(
    QLottieSpatialProperty *self,
    const QJsonObject *definition) {
  self->construct(*definition);
}

//  EasingSegment<QPointF> QLottieSpatialProperty::parseKeyframe(const
//      QJsonObject keyframe, bool fromExpression)
extern "C" Q_DECL_EXPORT
EasingSegment<QPointF> *ritual_ZN22QLottieSpatialProperty13parseKeyframeE11QJsonObjectb(
    QLottieSpatialProperty *self,
    const QJsonObject *keyframe,
    bool fromExpression) {
  return new EasingSegment<QPointF>(
      self->parseKeyframe(
          *keyframe,
          fromExpression));
}

//  EasingSegment<QPointF> QLottieSpatialProperty::parseKeyframe(const
//      QJsonObject keyframe, const QJsonObject nextKeyframe, bool
//      fromExpression)
extern "C" Q_DECL_EXPORT
EasingSegment<QPointF> *ritual_ZN22QLottieSpatialProperty13parseKeyframeE11QJsonObjectS0_b(
    QLottieSpatialProperty *self,
    const QJsonObject *keyframe,
    const QJsonObject *nextKeyframe,
    bool fromExpression) {
  return new EasingSegment<QPointF>(
      self->parseKeyframe(
          *keyframe,
          *nextKeyframe,
          fromExpression));
}

//  bool QLottieSpatialProperty::update(int frame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QLottieSpatialProperty6updateEi(
    QLottieSpatialProperty *self,
    int frame) {
  return self->update(frame);
}

//  bool QLottieSpatialProperty::hasCurves() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QLottieSpatialProperty9hasCurvesEv(
    const QLottieSpatialProperty *self) {
  return self->hasCurves();
}

//  const QList<QPainterPath> &QLottieSpatialProperty::subPaths() const
extern "C" Q_DECL_EXPORT
QList<QPainterPath> *ritual_ZNK22QLottieSpatialProperty8subPathsEv(
    const QLottieSpatialProperty *self) {
  return new QList<QPainterPath>(self->subPaths());
}

//  void QLottieSpatialProperty::moveTo(const QPointF &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLottieSpatialProperty6moveToERK7QPointF(
    QLottieSpatialProperty *self,
    const QPointF *e) {
  self->moveTo(*e);
}

//  void QLottieSpatialProperty::lineTo(const QPointF &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLottieSpatialProperty6lineToERK7QPointF(
    QLottieSpatialProperty *self,
    const QPointF *e) {
  self->lineTo(*e);
}

//  void QLottieSpatialProperty::cubicTo(const QPointF &c1, const QPointF
//      &c2, const QPointF &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLottieSpatialProperty7cubicToERK7QPointFS2_S2_(
    QLottieSpatialProperty *self,
    const QPointF *c1,
    const QPointF *c2,
    const QPointF *e) {
  self->cubicTo(*c1, *c2, *e);
}

//  QLottieSpatialProperty::~QLottieSpatialProperty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QLottieSpatialPropertyD1Ev(QLottieSpatialProperty *self) {
  delete self;
}

//  void QLottieSpatialProperty::construct(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QLottieSpatialProperty9constructERK11QJsonObject(
    QLottieSpatialProperty *self,
    const QJsonObject *definition) {
  self->QLottieSpatialProperty::construct(*definition);
}

//  bool QLottieSpatialProperty::update(int frame)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QLottieSpatialProperty6updateEi(
    QLottieSpatialProperty *self,
    int frame) {
  return self->QLottieSpatialProperty::update(frame);
}

//  a EasingSegment<QPointF> a ritual of QLottieSpatialProperty gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QLottieSpatialProperty__EasingSegment_QPointF(
    EasingSegment<QPointF> *self) {
  delete self;
}
