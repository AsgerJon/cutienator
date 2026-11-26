//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/vertexindexer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/vertexindexer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/vertexindexer_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qmap.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/vertexindexer.cpp, line 13, as _ZN13VertexIndexer26getSimilarVertexIndex_fastERKNS_12PackedVertexER4QMapIS0_jERj
inline bool VertexIndexer::getSimilarVertexIndex_fast(const PackedVertex &packed,
                                               QMap<PackedVertex, GLuint> &VertexToOutIndex,
                                               GLuint &result)
{
    QMap<PackedVertex, GLuint>::iterator it = VertexToOutIndex.find(packed);
    if (it == VertexToOutIndex.end()) {
        return false;
    } else {
        result = it.value();
        return true;
    }
}
//  -----------------------------------------------------------------------

//  bool VertexIndexer::getSimilarVertexIndex_fast(const PackedVertex
//      &packed, QMap<PackedVertex, GLuint> &VertexToOutIndex, GLuint
//      &result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13VertexIndexer26getSimilarVertexIndex_fastERKNS_12PackedVertexER4QMapIS0_jERj(
    const VertexIndexer::PackedVertex *packed,
    QMap<VertexIndexer::PackedVertex, GLuint> *VertexToOutIndex,
    GLuint *result) {
  return VertexIndexer::getSimilarVertexIndex_fast(
      *packed,
      *VertexToOutIndex,
      *result);
}

//  VertexIndexer::~VertexIndexer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13VertexIndexerD1Ev(VertexIndexer *self) {
  delete self;
}
