//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquadpath_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquadpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>

//  void QQuadPath::moveTo(const QVector2D &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath6moveToERK9QVector2D(
    QQuadPath *self,
    const QVector2D *to) {
  self->moveTo(*to);
}

//  void QQuadPath::lineTo(const QVector2D &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath6lineToERK9QVector2D(
    QQuadPath *self,
    const QVector2D *to) {
  self->lineTo(*to);
}

//  void QQuadPath::quadTo(const QVector2D &control, const QVector2D &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath6quadToERK9QVector2DS2_(
    QQuadPath *self,
    const QVector2D *control,
    const QVector2D *to) {
  self->quadTo(*control, *to);
}

//  const Element &QQuadPath::elementAt(int i) const
extern "C" Q_DECL_EXPORT
QQuadPath::Element *ritual_ZNK9QQuadPath9elementAtEi(
    const QQuadPath *self,
    int i) {
  return new QQuadPath::Element(self->elementAt(i));
}

//  int QQuadPath::indexOfChildAt(int i, int childNumber) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath14indexOfChildAtEii(
    const QQuadPath *self,
    int i,
    int childNumber) {
  return self->indexOfChildAt(i, childNumber);
}

//  QRectF QQuadPath::controlPointRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QQuadPath16controlPointRectEv(const QQuadPath *self) {
  return new QRectF(self->controlPointRect());
}

//  Qt::FillRule QQuadPath::fillRule() const
extern "C" Q_DECL_EXPORT
Qt::FillRule ritual_ZNK9QQuadPath8fillRuleEv(const QQuadPath *self) {
  return self->fillRule();
}

//  void QQuadPath::setFillRule(Qt::FillRule rule)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath11setFillRuleEN2Qt8FillRuleE(
    QQuadPath *self,
    Qt::FillRule rule) {
  self->setFillRule(rule);
}

//  void QQuadPath::reserve(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath7reserveEi(QQuadPath *self, int size) {
  self->reserve(size);
}

//  int QQuadPath::elementCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath12elementCountEv(const QQuadPath *self) {
  return self->elementCount();
}

//  bool QQuadPath::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath7isEmptyEv(const QQuadPath *self) {
  return self->isEmpty();
}

//  int QQuadPath::elementCountRecursive() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath21elementCountRecursiveEv(const QQuadPath *self) {
  return self->elementCountRecursive();
}

//  int QQuadPath::lineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath9lineCountEv(const QQuadPath *self) {
  return self->lineCount();
}

//  QQuadPath QQuadPath::fromPainterPath(const QPainterPath &path, PathHints
//      hints)
extern "C" Q_DECL_EXPORT
QQuadPath *ritual_ZN9QQuadPath15fromPainterPathERK12QPainterPath6QFlagsINS_8PathHintEE(
    const QPainterPath *path,
    int hints) {
  return new QQuadPath(
      QQuadPath::fromPainterPath(
          *path,
          QFlags<QQuadPath::PathHint>::fromInt(hints)));
}

//  QPainterPath QQuadPath::toPainterPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK9QQuadPath13toPainterPathEv(const QQuadPath *self) {
  return new QPainterPath(self->toPainterPath());
}

//  QString QQuadPath::asSvgString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QQuadPath11asSvgStringEv(const QQuadPath *self) {
  return new QString(self->asSvgString());
}

//  QQuadPath QQuadPath::subPathsClosed(bool *didClose) const
extern "C" Q_DECL_EXPORT
QQuadPath *ritual_ZNK9QQuadPath14subPathsClosedEPb(
    const QQuadPath *self,
    bool *didClose) {
  return new QQuadPath(self->subPathsClosed(didClose));
}

//  void QQuadPath::addCurvatureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath16addCurvatureDataEv(QQuadPath *self) {
  self->addCurvatureData();
}

//  QQuadPath QQuadPath::flattened() const
extern "C" Q_DECL_EXPORT
QQuadPath *ritual_ZNK9QQuadPath9flattenedEv(const QQuadPath *self) {
  return new QQuadPath(self->flattened());
}

//  void QQuadPath::splitElementAt(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath14splitElementAtEi(QQuadPath *self, int index) {
  self->splitElementAt(index);
}

//  bool QQuadPath::contains(const QVector2D &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath8containsERK9QVector2D(
    const QQuadPath *self,
    const QVector2D *point) {
  return self->contains(*point);
}

//  bool QQuadPath::contains(const QVector2D &point, int fromIndex, int
//      toIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath8containsERK9QVector2Dii(
    const QQuadPath *self,
    const QVector2D *point,
    int fromIndex,
    int toIndex) {
  return self->contains(*point, fromIndex, toIndex);
}

//  Element::FillSide QQuadPath::fillSideOf(int elementIdx, float elementT)
//      const
extern "C" Q_DECL_EXPORT
QQuadPath::Element::FillSide ritual_ZNK9QQuadPath10fillSideOfEif(
    const QQuadPath *self,
    int elementIdx,
    float elementT) {
  return self->fillSideOf(elementIdx, elementT);
}

//  QVector2D QQuadPath::closestPointOnLine(const QVector2D &p, const
//      QVector2D &sp, const QVector2D &ep)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QQuadPath18closestPointOnLineERK9QVector2DS2_S2_(
    const QVector2D *p,
    const QVector2D *sp,
    const QVector2D *ep) {
  return new QVector2D(QQuadPath::closestPointOnLine(*p, *sp, *ep));
}

//  bool QQuadPath::isPointOnLeft(const QVector2D &p, const QVector2D &sp,
//      const QVector2D &ep)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QQuadPath13isPointOnLeftERK9QVector2DS2_S2_(
    const QVector2D *p,
    const QVector2D *sp,
    const QVector2D *ep) {
  return QQuadPath::isPointOnLeft(*p, *sp, *ep);
}

//  bool QQuadPath::isPointOnLine(const QVector2D &p, const QVector2D &sp,
//      const QVector2D &ep)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QQuadPath13isPointOnLineERK9QVector2DS2_S2_(
    const QVector2D *p,
    const QVector2D *sp,
    const QVector2D *ep) {
  return QQuadPath::isPointOnLine(*p, *sp, *ep);
}

//  bool QQuadPath::isPointNearLine(const QVector2D &p, const QVector2D &sp,
//      const QVector2D &ep)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QQuadPath15isPointNearLineERK9QVector2DS2_S2_(
    const QVector2D *p,
    const QVector2D *sp,
    const QVector2D *ep) {
  return QQuadPath::isPointNearLine(*p, *sp, *ep);
}

//  bool QQuadPath::testHint(PathHint hint) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QQuadPath8testHintENS_8PathHintE(
    const QQuadPath *self,
    QQuadPath::PathHint hint) {
  return self->testHint(hint);
}

//  void QQuadPath::setHint(PathHint hint, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath7setHintENS_8PathHintEb(
    QQuadPath *self,
    QQuadPath::PathHint hint,
    bool on) {
  self->setHint(hint, on);
}

//  PathHints QQuadPath::pathHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QQuadPath9pathHintsEv(const QQuadPath *self) {
  return static_cast<int>(self->pathHints().toInt());
}

//  void QQuadPath::setPathHints(PathHints newHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath12setPathHintsE6QFlagsINS_8PathHintEE(
    QQuadPath *self,
    int newHints) {
  self->setPathHints(QFlags<QQuadPath::PathHint>::fromInt(newHints));
}

//  void QQuadPath::addElement(const QVector2D &control, const QVector2D &to,
//      bool isLine)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath10addElementERK9QVector2DS2_b(
    QQuadPath *self,
    const QVector2D *control,
    const QVector2D *to,
    bool isLine) {
  self->addElement(*control, *to, isLine);
}

//  void QQuadPath::addElement(const Element &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPath10addElementERKNS_7ElementE(
    QQuadPath *self,
    const QQuadPath::Element *e) {
  self->addElement(*e);
}

//  Element::FillSide QQuadPath::coordinateOrderOfElement(const Element
//      &element) const
extern "C" Q_DECL_EXPORT
QQuadPath::Element::FillSide ritual_ZNK9QQuadPath24coordinateOrderOfElementERKNS_7ElementE(
    const QQuadPath *self,
    const QQuadPath::Element *element) {
  return self->coordinateOrderOfElement(*element);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QQuadPath &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK9QQuadPath(
    const QDebug *a0,
    const QQuadPath *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQuadPath::~QQuadPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QQuadPathD1Ev(QQuadPath *self) {
  delete self;
}
