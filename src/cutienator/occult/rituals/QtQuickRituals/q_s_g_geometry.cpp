//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsggeometry.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 2. Kept as it is
//  when the generator runs again.
#include <QtQuick/QtQuick>
#include <QtQuick/qsggeometry.h>
#include <QtCore/qrect.h>

//  const AttributeSet &QSGGeometry::defaultAttributes_Point2D()
extern "C" Q_DECL_EXPORT
QSGGeometry::AttributeSet *ritual_ZN11QSGGeometry25defaultAttributes_Point2DEv() {
  return new QSGGeometry::AttributeSet(
      QSGGeometry::defaultAttributes_Point2D());
}

//  const AttributeSet &QSGGeometry::defaultAttributes_TexturedPoint2D()
extern "C" Q_DECL_EXPORT
QSGGeometry::AttributeSet *ritual_ZN11QSGGeometry33defaultAttributes_TexturedPoint2DEv() {
  return new QSGGeometry::AttributeSet(
      QSGGeometry::defaultAttributes_TexturedPoint2D());
}

//  const AttributeSet &QSGGeometry::defaultAttributes_ColoredPoint2D()
extern "C" Q_DECL_EXPORT
QSGGeometry::AttributeSet *ritual_ZN11QSGGeometry32defaultAttributes_ColoredPoint2DEv() {
  return new QSGGeometry::AttributeSet(
      QSGGeometry::defaultAttributes_ColoredPoint2D());
}

//  QSGGeometry::QSGGeometry(const QSGGeometry::AttributeSet &attribs, int
//      vertexCount, int indexCount, int indexType)
extern "C" Q_DECL_EXPORT
QSGGeometry *ritual_ZN11QSGGeometryC1ERKNS_12AttributeSetEiii(
    const QSGGeometry::AttributeSet *attribs,
    int vertexCount,
    int indexCount,
    int indexType) {
  return new QSGGeometry(*attribs, vertexCount, indexCount, indexType);
}

//  QSGGeometry::~QSGGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometryD1Ev(QSGGeometry *self) {
  delete self;
}

//  void QSGGeometry::setDrawingMode(unsigned int mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry14setDrawingModeEj(
    QSGGeometry *self,
    unsigned int mode) {
  self->setDrawingMode(mode);
}

//  unsigned int QSGGeometry::drawingMode() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK11QSGGeometry11drawingModeEv(
    const QSGGeometry *self) {
  return self->drawingMode();
}

//  void QSGGeometry::allocate(int vertexCount, int indexCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry8allocateEii(
    QSGGeometry *self,
    int vertexCount,
    int indexCount) {
  self->allocate(vertexCount, indexCount);
}

//  int QSGGeometry::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGGeometry11vertexCountEv(const QSGGeometry *self) {
  return self->vertexCount();
}

//  void QSGGeometry::setVertexCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry14setVertexCountEi(QSGGeometry *self, int count) {
  self->setVertexCount(count);
}

//  void *QSGGeometry::vertexData()
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QSGGeometry10vertexDataEv(QSGGeometry *self) {
  return self->vertexData();
}

//  Point2D *QSGGeometry::vertexDataAsPoint2D()
extern "C" Q_DECL_EXPORT
QSGGeometry::Point2D *ritual_ZN11QSGGeometry19vertexDataAsPoint2DEv(
    QSGGeometry *self) {
  return self->vertexDataAsPoint2D();
}

//  TexturedPoint2D *QSGGeometry::vertexDataAsTexturedPoint2D()
extern "C" Q_DECL_EXPORT
QSGGeometry::TexturedPoint2D *ritual_ZN11QSGGeometry27vertexDataAsTexturedPoint2DEv(
    QSGGeometry *self) {
  return self->vertexDataAsTexturedPoint2D();
}

//  ColoredPoint2D *QSGGeometry::vertexDataAsColoredPoint2D()
extern "C" Q_DECL_EXPORT
QSGGeometry::ColoredPoint2D *ritual_ZN11QSGGeometry26vertexDataAsColoredPoint2DEv(
    QSGGeometry *self) {
  return self->vertexDataAsColoredPoint2D();
}

//  const void *QSGGeometry::vertexData() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK11QSGGeometry10vertexDataEv(const QSGGeometry *self) {
  return self->vertexData();
}

//  const Point2D *QSGGeometry::vertexDataAsPoint2D() const
extern "C" Q_DECL_EXPORT
const QSGGeometry::Point2D *ritual_ZNK11QSGGeometry19vertexDataAsPoint2DEv(
    const QSGGeometry *self) {
  return self->vertexDataAsPoint2D();
}

//  const TexturedPoint2D *QSGGeometry::vertexDataAsTexturedPoint2D() const
extern "C" Q_DECL_EXPORT
const QSGGeometry::TexturedPoint2D *ritual_ZNK11QSGGeometry27vertexDataAsTexturedPoint2DEv(
    const QSGGeometry *self) {
  return self->vertexDataAsTexturedPoint2D();
}

//  const ColoredPoint2D *QSGGeometry::vertexDataAsColoredPoint2D() const
extern "C" Q_DECL_EXPORT
const QSGGeometry::ColoredPoint2D *ritual_ZNK11QSGGeometry26vertexDataAsColoredPoint2DEv(
    const QSGGeometry *self) {
  return self->vertexDataAsColoredPoint2D();
}

//  int QSGGeometry::indexType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGGeometry9indexTypeEv(const QSGGeometry *self) {
  return self->indexType();
}

//  int QSGGeometry::indexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGGeometry10indexCountEv(const QSGGeometry *self) {
  return self->indexCount();
}

//  void QSGGeometry::setIndexCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry13setIndexCountEi(QSGGeometry *self, int count) {
  self->setIndexCount(count);
}

//  void *QSGGeometry::indexData()
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QSGGeometry9indexDataEv(QSGGeometry *self) {
  return self->indexData();
}

//  int QSGGeometry::sizeOfIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGGeometry11sizeOfIndexEv(const QSGGeometry *self) {
  return self->sizeOfIndex();
}

//  const void *QSGGeometry::indexData() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK11QSGGeometry9indexDataEv(const QSGGeometry *self) {
  return self->indexData();
}

//  const uint *QSGGeometry::indexDataAsUInt() const
extern "C" Q_DECL_EXPORT
const uint *ritual_ZNK11QSGGeometry15indexDataAsUIntEv(
    const QSGGeometry *self) {
  return self->indexDataAsUInt();
}

//  const quint16 *QSGGeometry::indexDataAsUShort() const
extern "C" Q_DECL_EXPORT
const quint16 *ritual_ZNK11QSGGeometry17indexDataAsUShortEv(
    const QSGGeometry *self) {
  return self->indexDataAsUShort();
}

//  int QSGGeometry::attributeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGGeometry14attributeCountEv(const QSGGeometry *self) {
  return self->attributeCount();
}

//  const Attribute *QSGGeometry::attributes() const
extern "C" Q_DECL_EXPORT
const QSGGeometry::Attribute *ritual_ZNK11QSGGeometry10attributesEv(
    const QSGGeometry *self) {
  return self->attributes();
}

//  int QSGGeometry::sizeOfVertex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSGGeometry12sizeOfVertexEv(const QSGGeometry *self) {
  return self->sizeOfVertex();
}

//  void QSGGeometry::updateRectGeometry(QSGGeometry *g, const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry18updateRectGeometryEPS_RK6QRectF(
    QSGGeometry *g,
    const QRectF *rect) {
  QSGGeometry::updateRectGeometry(g, *rect);
}

//  void QSGGeometry::updateTexturedRectGeometry(QSGGeometry *g, const QRectF
//      &rect, const QRectF &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry26updateTexturedRectGeometryEPS_RK6QRectFS3_(
    QSGGeometry *g,
    const QRectF *rect,
    const QRectF *sourceRect) {
  QSGGeometry::updateTexturedRectGeometry(g, *rect, *sourceRect);
}

//  void QSGGeometry::updateColoredRectGeometry(QSGGeometry *g, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry25updateColoredRectGeometryEPS_RK6QRectF(
    QSGGeometry *g,
    const QRectF *rect) {
  QSGGeometry::updateColoredRectGeometry(g, *rect);
}

//  void QSGGeometry::setIndexDataPattern(DataPattern p)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry19setIndexDataPatternENS_11DataPatternE(
    QSGGeometry *self,
    QSGGeometry::DataPattern p) {
  self->setIndexDataPattern(p);
}

//  DataPattern QSGGeometry::indexDataPattern() const
extern "C" Q_DECL_EXPORT
QSGGeometry::DataPattern ritual_ZNK11QSGGeometry16indexDataPatternEv(
    const QSGGeometry *self) {
  return self->indexDataPattern();
}

//  void QSGGeometry::setVertexDataPattern(DataPattern p)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry20setVertexDataPatternENS_11DataPatternE(
    QSGGeometry *self,
    QSGGeometry::DataPattern p) {
  self->setVertexDataPattern(p);
}

//  DataPattern QSGGeometry::vertexDataPattern() const
extern "C" Q_DECL_EXPORT
QSGGeometry::DataPattern ritual_ZNK11QSGGeometry17vertexDataPatternEv(
    const QSGGeometry *self) {
  return self->vertexDataPattern();
}

//  void QSGGeometry::markIndexDataDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry18markIndexDataDirtyEv(QSGGeometry *self) {
  self->markIndexDataDirty();
}

//  void QSGGeometry::markVertexDataDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry19markVertexDataDirtyEv(QSGGeometry *self) {
  self->markVertexDataDirty();
}

//  float QSGGeometry::lineWidth() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QSGGeometry9lineWidthEv(const QSGGeometry *self) {
  return self->lineWidth();
}

//  void QSGGeometry::setLineWidth(float w)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry12setLineWidthEf(QSGGeometry *self, float w) {
  self->setLineWidth(w);
}

//  quint16 *QSGGeometry::indexDataAsUShort()
extern "C" Q_DECL_EXPORT
quint16 *ritual_ZN11QSGGeometry17indexDataAsUShortEv(
    QSGGeometry *self) {
  return self->indexDataAsUShort();
}

//  uint *QSGGeometry::indexDataAsUInt()
extern "C" Q_DECL_EXPORT
uint *ritual_ZN11QSGGeometry15indexDataAsUIntEv(
    QSGGeometry *self) {
  return self->indexDataAsUInt();
}
