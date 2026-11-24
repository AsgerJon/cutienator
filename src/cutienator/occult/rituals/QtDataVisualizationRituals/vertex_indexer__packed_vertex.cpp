//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/vertexindexer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/vertexindexer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool VertexIndexer::PackedVertex::operator<(const PackedVertex that)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13VertexIndexer12PackedVertexltES0_(
    const VertexIndexer::PackedVertex *self,
    const VertexIndexer::PackedVertex *that) {
  return self->operator<(*that);
}

//  VertexIndexer::PackedVertex::~PackedVertex()
extern "C" Q_DECL_EXPORT
void ritual_ZN13VertexIndexer12PackedVertexD1Ev(
    VertexIndexer::PackedVertex *self) {
  delete self;
}
