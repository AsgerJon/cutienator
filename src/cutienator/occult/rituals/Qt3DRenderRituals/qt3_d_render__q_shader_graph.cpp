//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshadergraph_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadergraph_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshadernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QString>

//  void Qt3DRender::QShaderGraph::addNode(const QShaderNode &node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderGraph7addNodeERKNS_11QShaderNodeE(
    Qt3DRender::QShaderGraph *self,
    const Qt3DRender::QShaderNode *node) {
  self->addNode(*node);
}

//  void Qt3DRender::QShaderGraph::removeNode(const QShaderNode &node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderGraph10removeNodeERKNS_11QShaderNodeE(
    Qt3DRender::QShaderGraph *self,
    const Qt3DRender::QShaderNode *node) {
  self->removeNode(*node);
}

//  QList<QShaderNode> Qt3DRender::QShaderGraph::nodes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QShaderNode> *ritual_ZNK10Qt3DRender12QShaderGraph5nodesEv(
    const Qt3DRender::QShaderGraph *self) {
  return new QList<Qt3DRender::QShaderNode>(self->nodes());
}

//  void Qt3DRender::QShaderGraph::addEdge(const Edge &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderGraph7addEdgeERKNS0_4EdgeE(
    Qt3DRender::QShaderGraph *self,
    const Qt3DRender::QShaderGraph::Edge *edge) {
  self->addEdge(*edge);
}

//  void Qt3DRender::QShaderGraph::removeEdge(const Edge &edge)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderGraph10removeEdgeERKNS0_4EdgeE(
    Qt3DRender::QShaderGraph *self,
    const Qt3DRender::QShaderGraph::Edge *edge) {
  self->removeEdge(*edge);
}

//  QList<Edge> Qt3DRender::QShaderGraph::edges() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QShaderGraph::Edge> *ritual_ZNK10Qt3DRender12QShaderGraph5edgesEv(
    const Qt3DRender::QShaderGraph *self) {
  return new QList<Qt3DRender::QShaderGraph::Edge>(self->edges());
}

//  QList<Statement> Qt3DRender::QShaderGraph::createStatements(const
//      QStringList &enabledLayers) const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QShaderGraph::Statement> *ritual_ZNK10Qt3DRender12QShaderGraph16createStatementsERK5QListI7QStringE(
    const Qt3DRender::QShaderGraph *self,
    const QList<QString> *enabledLayers) {
  return new QList<Qt3DRender::QShaderGraph::Statement>(
      self->createStatements(
          *enabledLayers));
}

//  Qt3DRender::QShaderGraph::~QShaderGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderGraphD1Ev(
    Qt3DRender::QShaderGraph *self) {
  delete self;
}

//  a QList<Qt3DRender::QShaderNode> a ritual of Qt3DRender::QShaderGraph
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderGraph__QList_Qt3DRender_QShaderNode(
    QList<Qt3DRender::QShaderNode> *self) {
  delete self;
}

//  a QList<Qt3DRender::QShaderGraph::Edge> a ritual of
//      Qt3DRender::QShaderGraph gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderGraph__QList_Qt3DRender_QShaderGraph_Edge(
    QList<Qt3DRender::QShaderGraph::Edge> *self) {
  delete self;
}

//  a QList<Qt3DRender::QShaderGraph::Statement> a ritual of
//      Qt3DRender::QShaderGraph gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderGraph__QList_Qt3DRender_QShaderGraph_Statement(
    QList<Qt3DRender::QShaderGraph::Statement> *self) {
  delete self;
}
