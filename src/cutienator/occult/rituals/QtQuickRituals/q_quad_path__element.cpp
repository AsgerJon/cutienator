//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquadpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquadpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qdebug.h>

//  QQuadPath::Element::Element()
extern "C" Q_DECL_EXPORT
QQuadPath::Element *ritual_ZN9QQuadPath7ElementC1Ev() {
  return new QQuadPath::Element();
}

//  QQuadPath::Element::Element(QVector2D s, QVector2D c, QVector2D e)
extern "C" Q_DECL_EXPORT
QQuadPath::Element *ritual_ZN9QQuadPath7ElementC1E9QVector2DS1_S1_(
    const QVector2D *s,
    const QVector2D *c,
    const QVector2D *e) {
  return new QQuadPath::Element(*s, *c, *e);
}

//  QQuadPath::Element::Element(QVector2D s, QVector2D e)
extern "C" Q_DECL_EXPORT
QQuadPath::Element *ritual_ZN9QQuadPath7ElementC1E9QVector2DS1_(
    const QVector2D *s,
    const QVector2D *e) {
  return new QQuadPath::Element(*s, *e);
}

//  bool QQuadPath::Element::isSubpathStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7Element14isSubpathStartEv(
    const QQuadPath::Element *self) {
  return self->isSubpathStart();
}

//  bool QQuadPath::Element::isSubpathEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7Element12isSubpathEndEv(
    const QQuadPath::Element *self) {
  return self->isSubpathEnd();
}

//  bool QQuadPath::Element::isLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7Element6isLineEv(const QQuadPath::Element *self) {
  return self->isLine();
}

//  bool QQuadPath::Element::isConvex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7Element8isConvexEv(
    const QQuadPath::Element *self) {
  return self->isConvex();
}

//  QVector2D QQuadPath::Element::startPoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element10startPointEv(
    const QQuadPath::Element *self) {
  return new QVector2D(self->startPoint());
}

//  QVector2D QQuadPath::Element::controlPoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element12controlPointEv(
    const QQuadPath::Element *self) {
  return new QVector2D(self->controlPoint());
}

//  QVector2D QQuadPath::Element::endPoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element8endPointEv(
    const QQuadPath::Element *self) {
  return new QVector2D(self->endPoint());
}

//  QVector2D QQuadPath::Element::midPoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element8midPointEv(
    const QQuadPath::Element *self) {
  return new QVector2D(self->midPoint());
}

//  QVector2D QQuadPath::Element::referencePoint() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element14referencePointEv(
    const QQuadPath::Element *self) {
  return new QVector2D(self->referencePoint());
}

//  Element QQuadPath::Element::segmentFromTo(float t0, float t1) const
extern "C" Q_DECL_EXPORT
QQuadPath::Element *ritual_ZNK9QQuadPath7Element13segmentFromToEff(
    const QQuadPath::Element *self,
    float t0,
    float t1) {
  return new QQuadPath::Element(self->segmentFromTo(t0, t1));
}

//  Element QQuadPath::Element::reversed() const
extern "C" Q_DECL_EXPORT
QQuadPath::Element *ritual_ZNK9QQuadPath7Element8reversedEv(
    const QQuadPath::Element *self) {
  return new QQuadPath::Element(self->reversed());
}

//  int QQuadPath::Element::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath7Element10childCountEv(
    const QQuadPath::Element *self) {
  return self->childCount();
}

//  int QQuadPath::Element::indexOfChild(int childNumber) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath7Element12indexOfChildEi(
    const QQuadPath::Element *self,
    int childNumber) {
  return self->indexOfChild(childNumber);
}

//  QVector2D QQuadPath::Element::pointAtFraction(float t) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element15pointAtFractionEf(
    const QQuadPath::Element *self,
    float t) {
  return new QVector2D(self->pointAtFraction(t));
}

//  QVector2D QQuadPath::Element::tangentAtFraction(float t) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element17tangentAtFractionEf(
    const QQuadPath::Element *self,
    float t) {
  return new QVector2D(self->tangentAtFraction(t));
}

//  QVector2D QQuadPath::Element::normalAtFraction(float t) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QQuadPath7Element16normalAtFractionEf(
    const QQuadPath::Element *self,
    float t) {
  return new QVector2D(self->normalAtFraction(t));
}

//  float QQuadPath::Element::extent() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QQuadPath7Element6extentEv(const QQuadPath::Element *self) {
  return self->extent();
}

//  void QQuadPath::Element::setAsConvex(bool isConvex)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath7Element11setAsConvexEb(
    QQuadPath::Element *self,
    bool isConvex) {
  self->setAsConvex(isConvex);
}

//  void QQuadPath::Element::setFillOnRight(bool isFillOnRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath7Element14setFillOnRightEb(
    QQuadPath::Element *self,
    bool isFillOnRight) {
  self->setFillOnRight(isFillOnRight);
}

//  bool QQuadPath::Element::isFillOnRight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7Element13isFillOnRightEv(
    const QQuadPath::Element *self) {
  return self->isFillOnRight();
}

//  bool QQuadPath::Element::isControlPointOnLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7Element20isControlPointOnLeftEv(
    const QQuadPath::Element *self) {
  return self->isControlPointOnLeft();
}

//  int QQuadPath::Element::intersectionsAtY(float y, float *fractions, bool
//      swapXY) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath7Element16intersectionsAtYEfPfb(
    const QQuadPath::Element *self,
    float y,
    float *fractions,
    bool swapXY) {
  return self->intersectionsAtY(y, fractions, swapXY);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QQuadPath::Element &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRKN9QQuadPath7ElementE(
    const QDebug *a0,
    const QQuadPath::Element *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQuadPath::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath7ElementD1Ev(QQuadPath::Element *self) {
  delete self;
}
