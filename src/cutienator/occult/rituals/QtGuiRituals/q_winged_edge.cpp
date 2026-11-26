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
#include <QtGui/private/qpathclipper_p.h>
#include <QtGui/private/qbezier_p.h>
#include <QtGui/private/qdatabuffer_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/qmath.h>
#include <algorithm>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/painting/qpathclipper.cpp, line 33, as local:qpathclipper.cpp:fuzzyIsNull
static inline bool fuzzyIsNull(qreal d)
{
    if (sizeof(qreal) == sizeof(double))
        return qAbs(d) <= 1e-12;
    else
        return qAbs(d) <= 1e-5f;
}

//  from src/gui/painting/qpathclipper.cpp, line 48, as local:qpathclipper.cpp:dot
static qreal dot(const QPointF &a, const QPointF &b)
{
    return a.x() * b.x() + a.y() * b.y();
}

//  from src/gui/painting/qpathclipper.cpp, line 53, as local:qpathclipper.cpp:normalize
static void normalize(double &x, double &y)
{
    double reciprocal = 1 / qSqrt(x * x + y * y);
    x *= reciprocal;
    y *= reciprocal;
}

//  from src/gui/painting/qpathclipper.cpp, line 60, as local:qpathclipper.cpp:QIntersection
struct QIntersection
{
    qreal alphaA;
    qreal alphaB;

    QPointF pos;
};

//  from src/gui/painting/qpathclipper.cpp, line 69, as local:qpathclipper.cpp:QIntersectionFinder
class QIntersectionFinder
{
public:
    void produceIntersections(QPathSegments &segments);
    bool hasIntersections(const QPathSegments &a, const QPathSegments &b) const;

private:
    bool linesIntersect(const QLineF &a, const QLineF &b) const;
};

//  from src/gui/painting/qpathclipper.cpp, line 146, as local:qpathclipper.cpp:QIntersectionFinder::hasIntersections
inline bool QIntersectionFinder::hasIntersections(const QPathSegments &a, const QPathSegments &b) const
{
    if (a.segments() == 0 || b.segments() == 0)
        return false;

    const QRectF &rb0 = b.elementBounds(0);

    qreal minX = rb0.left();
    qreal minY = rb0.top();
    qreal maxX = rb0.right();
    qreal maxY = rb0.bottom();

    for (int i = 1; i < b.segments(); ++i) {
        const QRectF &r = b.elementBounds(i);
        minX = qMin(minX, r.left());
        minY = qMin(minY, r.top());
        maxX = qMax(maxX, r.right());
        maxY = qMax(maxY, r.bottom());
    }

    QRectF rb(minX, minY, maxX - minX, maxY - minY);

    for (int i = 0; i < a.segments(); ++i) {
        const QRectF &r1 = a.elementBounds(i);

        if (r1.left() > rb.right() || rb.left() > r1.right())
            continue;
        if (r1.top() > rb.bottom() || rb.top() > r1.bottom())
            continue;

        for (int j = 0; j < b.segments(); ++j) {
            const QRectF &r2 = b.elementBounds(j);

            if (r1.left() > r2.right() || r2.left() > r1.right())
                continue;
            if (r1.top() > r2.bottom() || r2.top() > r1.bottom())
                continue;

            if (linesIntersect(a.lineAt(i), b.lineAt(j)))
                return true;
        }
    }

    return false;
}

//  from src/gui/painting/qpathclipper.cpp, line 193, as local:qpathclipper.cpp:TreeNode
namespace {
struct TreeNode
{
    qreal splitLeft;
    qreal splitRight;
    bool leaf;

    int lowestLeftIndex;
    int lowestRightIndex;

    union {
        struct {
            int first;
            int last;
        } interval;
        struct {
            int left;
            int right;
        } children;
    } index;
};
}  // namespace

//  from src/gui/painting/qpathclipper.cpp, line 214, as local:qpathclipper.cpp:RectF
namespace {
struct RectF
{
    qreal x1;
    qreal y1;
    qreal x2;
    qreal y2;
};
}  // namespace

//  from src/gui/painting/qpathclipper.cpp, line 559, as local:qpathclipper.cpp:QKdPointTree
class QKdPointTree
{
public:
    enum Traversal {
        TraverseBoth,
        TraverseLeft,
        TraverseRight,
        TraverseNone
    };

    struct Node {
        int point;
        int id;

        Node *left;
        Node *right;
    };

    QKdPointTree(const QPathSegments &segments)
        : m_segments(&segments)
        , m_nodes(m_segments->points())
        , m_id(0)
    {
        m_nodes.resize(m_segments->points());

        for (int i = 0; i < m_nodes.size(); ++i) {
            m_nodes.at(i).point = i;
            m_nodes.at(i).id = -1;
        }

        m_rootNode = build(0, m_nodes.size());
    }

    int build(int begin, int end, int depth = 0);

    Node *rootNode()
    {
        return &m_nodes.at(m_rootNode);
    }

    inline int nextId()
    {
        return m_id++;
    }

private:
    const QPathSegments *m_segments;
    QDataBuffer<Node> m_nodes;

    int m_rootNode;
    int m_id;
};

//  from src/gui/painting/qpathclipper.cpp, line 627, as local:qpathclipper.cpp:component
static inline qreal component(const QPointF &point, unsigned int i)
{
    Q_ASSERT(i < 2);
    const qreal components[] = { point.x(), point.y() };
    return components[i];
}

//  from src/gui/painting/qpathclipper.cpp, line 670, as local:qpathclipper.cpp:QKdPointFinder
class QKdPointFinder
{
public:
    QKdPointFinder(int point, const QPathSegments &segments, QKdPointTree &tree)
        : m_result(-1)
        , m_segments(&segments)
        , m_tree(&tree)
    {
        pointComponents[0] = segments.pointAt(point).x();
        pointComponents[1] = segments.pointAt(point).y();
    }

    inline QKdPointTree::Traversal operator()(QKdPointTree::Node &node, int depth)
    {
        if (m_result != -1)
            return QKdPointTree::TraverseNone;

        const QPointF &nodePoint = m_segments->pointAt(node.point);

        const qreal pivotComponents[] = { nodePoint.x(), nodePoint.y() };

        const qreal pivot = pivotComponents[depth & 1];
        const qreal value = pointComponents[depth & 1];

        if (fuzzyIsNull(pivot - value)) {
            const qreal pivot2 = pivotComponents[(depth + 1) & 1];
            const qreal value2 = pointComponents[(depth + 1) & 1];

            if (fuzzyIsNull(pivot2 - value2)) {
                if (node.id < 0)
                    node.id = m_tree->nextId();

                m_result = node.id;
                return QKdPointTree::TraverseNone;
            } else
                return QKdPointTree::TraverseBoth;
        } else if (value < pivot) {
            return QKdPointTree::TraverseLeft;
        } else {
            return QKdPointTree::TraverseRight;
        }
    }

    int result() const
    {
        return m_result;
    }

private:
    qreal pointComponents[2];
    int m_result;
    const QPathSegments *m_segments;
    QKdPointTree *m_tree;
};

//  from src/gui/painting/qpathclipper.cpp, line 1092, as local:qpathclipper.cpp:commonEdge
static int commonEdge(const QWingedEdge &list, int a, int b)
{
    const QPathVertex *ap = list.vertex(a);
    Q_ASSERT(ap);

    const QPathVertex *bp = list.vertex(b);
    Q_ASSERT(bp);

    if (ap->edge < 0 || bp->edge < 0)
        return -1;

    QWingedEdge::TraversalStatus status;
    status.edge = ap->edge;
    status.direction = list.edge(status.edge)->directionTo(a);
    status.traversal = QPathEdge::RightTraversal;

    do {
        const QPathEdge *ep = list.edge(status.edge);

        if ((ep->first == a && ep->second == b)
            || (ep->first == b && ep->second == a))
            return status.edge;

        status = list.next(status);
        status.flip();
    } while (status.edge != ap->edge);

    return -1;
}

//  from src/gui/painting/qpathclipper.cpp, line 1122, as local:qpathclipper.cpp:computeAngle
static double computeAngle(const QPointF &v)
{
#if 1
    if (v.x() == 0) {
        return v.y() <= 0 ? 0 : 64.;
    } else if (v.y() == 0) {
        return v.x() <= 0 ? 32. : 96.;
    }

    double vx = v.x();
    double vy = v.y();
    normalize(vx, vy);
    if (vy < 0) {
        if (vx < 0) { // 0 - 32
            return -32. * vx;
        } else { // 96 - 128
            return 128. - 32. * vx;
        }
    } else { // 32 - 96
        return 64. + 32. * vx;
    }
#else
    // doesn't seem to be robust enough
    return qAtan2(v.x(), v.y()) + Q_PI;
#endif
}

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

//  from src/gui/painting/qpathclipper.cpp, line 1149, as _ZN11QWingedEdge7addEdgeERK7QPointFS2_
inline int QWingedEdge::addEdge(const QPointF &a, const QPointF &b)
{
    int fi = insert(a);
    int si = insert(b);

    return addEdge(fi, si);
}

//  from src/gui/painting/qpathclipper.cpp, line 1157, as _ZN11QWingedEdge7addEdgeEii
inline int QWingedEdge::addEdge(int fi, int si)
{
    if (fi == si)
        return -1;

    int common = commonEdge(*this, fi, si);
    if (common >= 0)
        return common;

    m_edges << QPathEdge(fi, si);

    int ei = m_edges.size() - 1;

    QPathVertex *fp = vertex(fi);
    QPathVertex *sp = vertex(si);

    QPathEdge *ep = edge(ei);

    const QPointF tangent = QPointF(*sp) - QPointF(*fp);
    ep->angle = computeAngle(tangent);
    ep->invAngle = ep->angle + 64;
    if (ep->invAngle >= 128)
        ep->invAngle -= 128;

    QPathVertex *vertices[2] = { fp, sp };
    QPathEdge::Direction dirs[2] = { QPathEdge::Backward, QPathEdge::Forward };

#ifdef QDEBUG_CLIPPER
    printf("** Adding edge %d / vertices: %.07f %.07f, %.07f %.07f\n", ei, fp->x, fp->y, sp->x, sp->y);
#endif

    for (int i = 0; i < 2; ++i) {
        QPathVertex *vp = vertices[i];
        if (vp->edge < 0) {
            vp->edge = ei;
            ep->setNext(dirs[i], ei);
        } else {
            int vi = ep->vertex(dirs[i]);
            Q_ASSERT(vertex(vi) == vertices[i]);

            TraversalStatus os = findInsertStatus(vi, ei);
            QPathEdge *op = edge(os.edge);

            Q_ASSERT(vertex(op->vertex(os.direction)) == vertices[i]);

            TraversalStatus ns = next(os);
            ns.flipDirection();
            QPathEdge *np = edge(ns.edge);

            op->setNext(os.traversal, os.direction, ei);
            np->setNext(ns.traversal, ns.direction, ei);

            int oe = os.edge;
            int ne = ns.edge;

            os = next(os);
            ns = next(ns);

            os.flipDirection();
            ns.flipDirection();

            Q_ASSERT(os.edge == ei);
            Q_ASSERT(ns.edge == ei);

            ep->setNext(os.traversal, os.direction, oe);
            ep->setNext(ns.traversal, ns.direction, ne);
        }
    }

    Q_ASSERT(ep->next(QPathEdge::RightTraversal, QPathEdge::Forward) >= 0);
    Q_ASSERT(ep->next(QPathEdge::RightTraversal, QPathEdge::Backward) >= 0);
    Q_ASSERT(ep->next(QPathEdge::LeftTraversal, QPathEdge::Forward) >= 0);
    Q_ASSERT(ep->next(QPathEdge::LeftTraversal, QPathEdge::Backward) >= 0);

    return ei;
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

//  int QWingedEdge::addEdge(const QPointF &a, const QPointF &b)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QWingedEdge7addEdgeERK7QPointFS2_(
    QWingedEdge *self,
    const QPointF *a,
    const QPointF *b) {
  return self->addEdge(*a, *b);
}

//  int QWingedEdge::addEdge(int vertexA, int vertexB)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QWingedEdge7addEdgeEii(
    QWingedEdge *self,
    int vertexA,
    int vertexB) {
  return self->addEdge(vertexA, vertexB);
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
