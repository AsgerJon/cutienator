//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPathEdge::QPathEdge(int a, int b)
extern "C" Q_DECL_EXPORT
QPathEdge *ritual_ZN9QPathEdgeC1Eii(int a, int b) {
  return new QPathEdge(a, b);
}

//  int QPathEdge::next(Traversal traversal, Direction direction) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QPathEdge4nextENS_9TraversalENS_9DirectionE(
    const QPathEdge *self,
    QPathEdge::Traversal traversal,
    QPathEdge::Direction direction) {
  return self->next(traversal, direction);
}

//  void QPathEdge::setNext(Traversal traversal, Direction direction, int
//      next)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPathEdge7setNextENS_9TraversalENS_9DirectionEi(
    QPathEdge *self,
    QPathEdge::Traversal traversal,
    QPathEdge::Direction direction,
    int next) {
  self->setNext(traversal, direction, next);
}

//  void QPathEdge::setNext(Direction direction, int next)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPathEdge7setNextENS_9DirectionEi(
    QPathEdge *self,
    QPathEdge::Direction direction,
    int next) {
  self->setNext(direction, next);
}

//  Direction QPathEdge::directionTo(int vertex) const
extern "C" Q_DECL_EXPORT
QPathEdge::Direction ritual_ZNK9QPathEdge11directionToEi(
    const QPathEdge *self,
    int vertex) {
  return self->directionTo(vertex);
}

//  int QPathEdge::vertex(Direction direction) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QPathEdge6vertexENS_9DirectionE(
    const QPathEdge *self,
    QPathEdge::Direction direction) {
  return self->vertex(direction);
}

//  QPathEdge::~QPathEdge()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPathEdgeD1Ev(QPathEdge *self) {
  delete self;
}
