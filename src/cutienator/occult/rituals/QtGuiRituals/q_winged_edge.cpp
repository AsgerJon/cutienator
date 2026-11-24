//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qpathclipper_p.h"
#include <private/qbezier_p.h>
#include <private/qdatabuffer_p.h>
#include <private/qnumeric_p.h>
#include <qmath.h>
#include <algorithm>
#include <qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpathclipper.cpp, line 872, as _ZN13QPathSegments7setPathERK12QPainterPath
inline void QPathSegments::setPath(const QPainterPath &path)
{
    m_points.reset();
    m_intersections.reset();
    m_segments.reset();

    m_pathId = 0;

    addPath(path);
}

//  from src/gui/painting/qpathclipper.cpp, line 819, as _ZN11QWingedEdgeC1Ev
inline QWingedEdge::QWingedEdge() :
    m_edges(0),
    m_vertices(0),
    m_segments(0)
{
}

//  from src/gui/painting/qpathclipper.cpp, line 1298, as _ZN11QWingedEdge8simplifyEv
inline void QWingedEdge::simplify()
{
    for (int i = 0; i < edgeCount(); ++i) {
        const QPathEdge *ep = edge(i);

        // if both sides are part of the inside then we can collapse the edge
        int flag = 0x3 << 4;
        if ((ep->flag & flag) == flag) {
            removeEdge(i);

            ep->flag &= ~flag;
        }
    }
}

//  from src/gui/painting/qpathclipper.cpp, line 837, as _ZNK11QWingedEdge4nextERKNS_15TraversalStatusE
inline QWingedEdge::TraversalStatus QWingedEdge::next(const QWingedEdge::TraversalStatus &status) const
{
    const QPathEdge *sp = edge(status.edge);
    Q_ASSERT(sp);

    TraversalStatus result;
    result.edge = sp->next(status.traversal, status.direction);
    result.traversal = status.traversal;
    result.direction = status.direction;

    const QPathEdge *rp = edge(result.edge);
    Q_ASSERT(rp);

    if (sp->vertex(status.direction) == rp->vertex(status.direction))
        result.flip();

    return result;
}

//  from src/gui/painting/qpathclipper.cpp, line 1722, as _ZNK11QWingedEdge8isInsideEdd
inline bool QWingedEdge::isInside(qreal x, qreal y) const
{
    int winding = 0;
    for (int i = 0; i < edgeCount(); ++i) {
        const QPathEdge *ep = edge(i);

        // left xor right
        int w = ((ep->flag >> 4) ^ (ep->flag >> 5)) & 1;

        if (!w)
            continue;

        QPointF a = *vertex(ep->first);
        QPointF b = *vertex(ep->second);

        if ((a.y() < y && b.y() > y) || (a.y() > y && b.y() < y)) {
            qreal intersectionX = a.x() + (b.x() - a.x()) * (y - a.y()) / (b.y() - a.y());

            if (intersectionX > x)
                winding += w;
        }
    }

    return winding & 1;
}

//  from src/gui/painting/qpathclipper.cpp, line 1052, as _ZN11QWingedEdge10removeEdgeEi
inline void QWingedEdge::removeEdge(int ei)
{
    QPathEdge *ep = edge(ei);

    TraversalStatus status;
    status.direction = QPathEdge::Forward;
    status.traversal = QPathEdge::RightTraversal;
    status.edge = ei;

    TraversalStatus forwardRight = next(status);
    forwardRight.flipDirection();

    status.traversal = QPathEdge::LeftTraversal;
    TraversalStatus forwardLeft = next(status);
    forwardLeft.flipDirection();

    status.direction = QPathEdge::Backward;
    TraversalStatus backwardLeft = next(status);
    backwardLeft.flipDirection();

    status.traversal = QPathEdge::RightTraversal;
    TraversalStatus backwardRight = next(status);
    backwardRight.flipDirection();

    edge(forwardRight.edge)->setNext(forwardRight.traversal, forwardRight.direction, forwardLeft.edge);
    edge(forwardLeft.edge)->setNext(forwardLeft.traversal, forwardLeft.direction, forwardRight.edge);

    edge(backwardRight.edge)->setNext(backwardRight.traversal, backwardRight.direction, backwardLeft.edge);
    edge(backwardLeft.edge)->setNext(backwardLeft.traversal, backwardLeft.direction, backwardRight.edge);

    ep->setNext(QPathEdge::Forward, ei);
    ep->setNext(QPathEdge::Backward, ei);

    QPathVertex *a = vertex(ep->first);
    QPathVertex *b = vertex(ep->second);

    a->edge = backwardRight.edge;
    b->edge = forwardRight.edge;
}

//  from src/gui/painting/qpathclipper.cpp, line 1234, as _ZN11QWingedEdge6insertERK11QPathVertex
inline int QWingedEdge::insert(const QPathVertex &vertex)
{
    if (!m_vertices.isEmpty()) {
        const QPathVertex &last = m_vertices.last();
        if (vertex.x == last.x && vertex.y == last.y)
            return m_vertices.size() - 1;

        for (int i = 0; i < m_vertices.size(); ++i) {
            const QPathVertex &v = m_vertices.at(i);
            if (qFuzzyCompare(v.x, vertex.x) && qFuzzyCompare(v.y, vertex.y)) {
                return i;
            }
        }
    }

    m_vertices << vertex;
    return m_vertices.size() - 1;
}

//  from src/gui/painting/qpathclipper.cpp, line 997, as _ZNK11QWingedEdge16findInsertStatusEii
inline QWingedEdge::TraversalStatus QWingedEdge::findInsertStatus(int vi, int ei) const
{
    const QPathVertex *vp = vertex(vi);

    Q_ASSERT(vp);
    Q_ASSERT(ei >= 0);
    Q_ASSERT(vp->edge >= 0);

    int position = vp->edge;
    qreal d = 128.;

    TraversalStatus status;
    status.direction = edge(vp->edge)->directionTo(vi);
    status.traversal = QPathEdge::RightTraversal;
    status.edge = vp->edge;

#ifdef QDEBUG_CLIPPER
    const QPathEdge *ep = edge(ei);
    qDebug() << "Finding insert status for edge" << ei << "at vertex" << QPointF(*vp) << ", angles: " << ep->angle << ep->invAngle;
#endif

    do {
        status = next(status);
        status.flip();

        Q_ASSERT(edge(status.edge)->vertex(status.direction) == vi);
        qreal d2 = delta(vi, ei, status.edge);

#ifdef QDEBUG_CLIPPER
        const QPathEdge *op = edge(status.edge);
        qDebug() << "Delta to edge" << status.edge << d2 << ", angles: " << op->angle << op->invAngle;
#endif

        if (d2 < d) {
            position = status.edge;
            d = d2;
        }
    } while (status.edge != vp->edge);

    status.traversal = QPathEdge::LeftTraversal;
    status.direction = QPathEdge::Forward;
    status.edge = position;

    if (edge(status.edge)->vertex(status.direction) != vi)
        status.flip();

#ifdef QDEBUG_CLIPPER
    qDebug() << "Inserting edge" << ei << "to" << (status.traversal == QPathEdge::LeftTraversal ? "left" : "right") << "of edge" << status.edge;
#endif

    Q_ASSERT(edge(status.edge)->vertex(status.direction) == vi);

    return status;
}

//  from src/gui/painting/qpathclipper.cpp, line 973, as _ZNK11QWingedEdge5deltaEiii
inline qreal QWingedEdge::delta(int vertex, int a, int b) const
{
    const QPathEdge *ap = edge(a);
    const QPathEdge *bp = edge(b);

    double a_angle = ap->angle;
    double b_angle = bp->angle;

    if (vertex == ap->second)
        a_angle = ap->invAngle;

    if (vertex == bp->second)
        b_angle = bp->invAngle;

    double result = b_angle - a_angle;

    if (result >= 128.)
        return result - 128.;
    else if (result < 0)
        return result + 128.;
    else
        return result;
}
//  -----------------------------------------------------------------------

//  QWingedEdge::QWingedEdge()
extern "C" Q_DECL_EXPORT
QWingedEdge *ritual_ZN11QWingedEdgeC1Ev() {
  return new QWingedEdge();
}

//  void QWingedEdge::simplify()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWingedEdge8simplifyEv(QWingedEdge *self) {
  self->simplify();
}

//  int QWingedEdge::edgeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWingedEdge9edgeCountEv(const QWingedEdge *self) {
  return self->edgeCount();
}

//  QPathEdge *QWingedEdge::edge(int edge)
extern "C" Q_DECL_EXPORT
QPathEdge *ritual_ZN11QWingedEdge4edgeEi(QWingedEdge *self, int edge) {
  return self->edge(edge);
}

//  const QPathEdge *QWingedEdge::edge(int edge) const
extern "C" Q_DECL_EXPORT
const QPathEdge *ritual_ZNK11QWingedEdge4edgeEi(
    const QWingedEdge *self,
    int edge) {
  return self->edge(edge);
}

//  int QWingedEdge::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QWingedEdge11vertexCountEv(const QWingedEdge *self) {
  return self->vertexCount();
}

//  int QWingedEdge::addVertex(const QPointF &p)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QWingedEdge9addVertexERK7QPointF(
    QWingedEdge *self,
    const QPointF *p) {
  return self->addVertex(*p);
}

//  QPathVertex *QWingedEdge::vertex(int vertex)
extern "C" Q_DECL_EXPORT
QPathVertex *ritual_ZN11QWingedEdge6vertexEi(QWingedEdge *self, int vertex) {
  return self->vertex(vertex);
}

//  const QPathVertex *QWingedEdge::vertex(int vertex) const
extern "C" Q_DECL_EXPORT
const QPathVertex *ritual_ZNK11QWingedEdge6vertexEi(
    const QWingedEdge *self,
    int vertex) {
  return self->vertex(vertex);
}

//  TraversalStatus QWingedEdge::next(const TraversalStatus &status) const
extern "C" Q_DECL_EXPORT
QWingedEdge::TraversalStatus *ritual_ZNK11QWingedEdge4nextERKNS_15TraversalStatusE(
    const QWingedEdge *self,
    const QWingedEdge::TraversalStatus *status) {
  return new QWingedEdge::TraversalStatus(self->next(*status));
}

//  bool QWingedEdge::isInside(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWingedEdge8isInsideEdd(
    const QWingedEdge *self,
    qreal x,
    qreal y) {
  return self->isInside(x, y);
}

//  QPathEdge::Traversal QWingedEdge::flip(QPathEdge::Traversal traversal)
extern "C" Q_DECL_EXPORT
QPathEdge::Traversal ritual_ZN11QWingedEdge4flipEN9QPathEdge9TraversalE(
    QPathEdge::Traversal traversal) {
  return QWingedEdge::flip(traversal);
}

//  QPathEdge::Direction QWingedEdge::flip(QPathEdge::Direction direction)
extern "C" Q_DECL_EXPORT
QPathEdge::Direction ritual_ZN11QWingedEdge4flipEN9QPathEdge9DirectionE(
    QPathEdge::Direction direction) {
  return QWingedEdge::flip(direction);
}

//  void QWingedEdge::removeEdge(int ei)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWingedEdge10removeEdgeEi(QWingedEdge *self, int ei) {
  self->removeEdge(ei);
}

//  int QWingedEdge::insert(const QPathVertex &vertex)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QWingedEdge6insertERK11QPathVertex(
    QWingedEdge *self,
    const QPathVertex *vertex) {
  return self->insert(*vertex);
}

//  TraversalStatus QWingedEdge::findInsertStatus(int vertex, int edge) const
extern "C" Q_DECL_EXPORT
QWingedEdge::TraversalStatus *ritual_ZNK11QWingedEdge16findInsertStatusEii(
    const QWingedEdge *self,
    int vertex,
    int edge) {
  return new QWingedEdge::TraversalStatus(
      self->findInsertStatus(
          vertex,
          edge));
}

//  qreal QWingedEdge::delta(int vertex, int a, int b) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11QWingedEdge5deltaEiii(
    const QWingedEdge *self,
    int vertex,
    int a,
    int b) {
  return self->delta(vertex, a, b);
}
