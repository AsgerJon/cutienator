//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/customrenderitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/customrenderitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/private/abstractrenderitem_p.h>
#include <QtDataVisualization/private/customrenderitem_p.h>
#include <QtDataVisualization/private/meshloader_p.h>
#include <QtDataVisualization/private/vertexindexer_p.h>
#include <QtDataVisualization/private/objecthelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 16, as local:objecthelper.cpp:ObjectHelperRef
struct ObjectHelperRef {
    int refCount;
    ObjectHelper *obj;
};

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 8, as _ZN18AbstractRenderItemC2Ev
inline AbstractRenderItem::AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 40, as _ZN16CustomRenderItemD1Ev
inline CustomRenderItem::~CustomRenderItem()
{
    ObjectHelper::releaseObjectHelper(m_renderer, m_object);
}

//  from ../qtdatavis3d/src/datavisualization/utils/objecthelper.cpp, line 28, as _ZN12ObjectHelper17resetObjectHelperEPK18Abstract3DRendererRPS_RK7QString
inline void ObjectHelper::resetObjectHelper(const Abstract3DRenderer *cacheId, ObjectHelper *&obj,
                                     const QString &meshFile)
{
    Q_ASSERT(cacheId);

    if (obj) {
        const QString &oldFile = obj->objectFile();
        if (meshFile == oldFile)
            return; // same file, do nothing
        releaseObjectHelper(cacheId, obj);
    }
    obj = getObjectHelper(cacheId, meshFile);
}

//  from ../qtdatavis3d/src/datavisualization/data/abstractrenderitem.cpp, line 18, as _ZN18AbstractRenderItemD2Ev
inline AbstractRenderItem::~AbstractRenderItem()
{
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 51, as _ZN16CustomRenderItem13setColorTableERK5QListIjE
inline void CustomRenderItem::setColorTable(const QList<QRgb> &colors)
{
    m_colorTable.resize(256);
    for (int i = 0; i < 256; i++) {
        if (i < colors.size()) {
            const QRgb &rgb = colors.at(i);
            m_colorTable[i] = QVector4D(float(qRed(rgb)) / 255.0f,
                                        float(qGreen(rgb)) / 255.0f,
                                        float(qBlue(rgb)) / 255.0f,
                                        float(qAlpha(rgb)) / 255.0f);
        } else {
            m_colorTable[i] = QVector4D(0.0f, 0.0f, 0.0f, 0.0f);
        }
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 67, as _ZN16CustomRenderItem12setMinBoundsERK9QVector3D
inline void CustomRenderItem::setMinBounds(const QVector3D &bounds)
{
    m_minBounds = bounds;
    m_minBoundsNormal = m_minBounds;
    m_minBoundsNormal.setY(-m_minBoundsNormal.y());
    m_minBoundsNormal.setZ(-m_minBoundsNormal.z());
    m_minBoundsNormal = 0.5f * (m_minBoundsNormal + oneVector);
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 76, as _ZN16CustomRenderItem12setMaxBoundsERK9QVector3D
inline void CustomRenderItem::setMaxBounds(const QVector3D &bounds)
{
    m_maxBounds = bounds;
    m_maxBoundsNormal = m_maxBounds;
    m_maxBoundsNormal.setY(-m_maxBoundsNormal.y());
    m_maxBoundsNormal.setZ(-m_maxBoundsNormal.z());
    m_maxBoundsNormal = 0.5f * (m_maxBoundsNormal + oneVector);
}

//  from ../qtdatavis3d/src/datavisualization/data/customrenderitem.cpp, line 85, as _ZN16CustomRenderItem18setSliceFrameColorERK6QColor
inline void CustomRenderItem::setSliceFrameColor(const QColor &color)
{
    const QRgb &rgb = color.rgba();
    m_sliceFrameColor = QVector4D(float(qRed(rgb)) / 255.0f,
                                  float(qGreen(rgb)) / 255.0f,
                                  float(qBlue(rgb)) / 255.0f,
                                  float(1.0f)); // Alpha not supported for frames
}
//  -----------------------------------------------------------------------

//  CustomRenderItem::~CustomRenderItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItemD1Ev(CustomRenderItem *self) {
  delete self;
}

//  void CustomRenderItem::setTexture(GLuint texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem10setTextureEj(
    CustomRenderItem *self,
    GLuint texture) {
  self->setTexture(texture);
}

//  GLuint CustomRenderItem::texture() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK16CustomRenderItem7textureEv(const CustomRenderItem *self) {
  return self->texture();
}

//  ObjectHelper *CustomRenderItem::mesh() const
extern "C" Q_DECL_EXPORT
ObjectHelper *ritual_ZNK16CustomRenderItem4meshEv(
    const CustomRenderItem *self) {
  return self->mesh();
}

//  void CustomRenderItem::setScaling(const QVector3D &scaling)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem10setScalingERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *scaling) {
  self->setScaling(*scaling);
}

//  const QVector3D &CustomRenderItem::scaling() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem7scalingEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->scaling());
}

//  void CustomRenderItem::setOrigScaling(const QVector3D &scaling)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem14setOrigScalingERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *scaling) {
  self->setOrigScaling(*scaling);
}

//  const QVector3D &CustomRenderItem::origScaling() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem11origScalingEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->origScaling());
}

//  void CustomRenderItem::setPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem11setPositionERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  const QVector3D &CustomRenderItem::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem8positionEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->position());
}

//  void CustomRenderItem::setOrigPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem15setOrigPositionERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *position) {
  self->setOrigPosition(*position);
}

//  const QVector3D &CustomRenderItem::origPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem12origPositionEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->origPosition());
}

//  void CustomRenderItem::setPositionAbsolute(bool absolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem19setPositionAbsoluteEb(
    CustomRenderItem *self,
    bool absolute) {
  self->setPositionAbsolute(absolute);
}

//  bool CustomRenderItem::isPositionAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem18isPositionAbsoluteEv(
    const CustomRenderItem *self) {
  return self->isPositionAbsolute();
}

//  void CustomRenderItem::setScalingAbsolute(bool absolute)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem18setScalingAbsoluteEb(
    CustomRenderItem *self,
    bool absolute) {
  self->setScalingAbsolute(absolute);
}

//  bool CustomRenderItem::isScalingAbsolute() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem17isScalingAbsoluteEv(
    const CustomRenderItem *self) {
  return self->isScalingAbsolute();
}

//  void CustomRenderItem::setBlendNeeded(bool blend)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem14setBlendNeededEb(
    CustomRenderItem *self,
    bool blend) {
  self->setBlendNeeded(blend);
}

//  bool CustomRenderItem::isBlendNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem13isBlendNeededEv(
    const CustomRenderItem *self) {
  return self->isBlendNeeded();
}

//  void CustomRenderItem::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem10setVisibleEb(
    CustomRenderItem *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool CustomRenderItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem9isVisibleEv(const CustomRenderItem *self) {
  return self->isVisible();
}

//  void CustomRenderItem::setItemPointer(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem14setItemPointerEP13QCustom3DItem(
    CustomRenderItem *self,
    QCustom3DItem *item) {
  self->setItemPointer(item);
}

//  QCustom3DItem *CustomRenderItem::itemPointer() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK16CustomRenderItem11itemPointerEv(
    const CustomRenderItem *self) {
  return self->itemPointer();
}

//  void CustomRenderItem::setValid(bool valid)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem8setValidEb(
    CustomRenderItem *self,
    bool valid) {
  self->setValid(valid);
}

//  bool CustomRenderItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem7isValidEv(const CustomRenderItem *self) {
  return self->isValid();
}

//  void CustomRenderItem::setIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem8setIndexEi(
    CustomRenderItem *self,
    int index) {
  self->setIndex(index);
}

//  int CustomRenderItem::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem5indexEv(const CustomRenderItem *self) {
  return self->index();
}

//  void CustomRenderItem::setShadowCasting(bool shadowCasting)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem16setShadowCastingEb(
    CustomRenderItem *self,
    bool shadowCasting) {
  self->setShadowCasting(shadowCasting);
}

//  bool CustomRenderItem::isShadowCasting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem15isShadowCastingEv(
    const CustomRenderItem *self) {
  return self->isShadowCasting();
}

//  void CustomRenderItem::setFacingCamera(bool facing)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem15setFacingCameraEb(
    CustomRenderItem *self,
    bool facing) {
  self->setFacingCamera(facing);
}

//  bool CustomRenderItem::isFacingCamera() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem14isFacingCameraEv(
    const CustomRenderItem *self) {
  return self->isFacingCamera();
}

//  void CustomRenderItem::setRenderer(Abstract3DRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem11setRendererEP18Abstract3DRenderer(
    CustomRenderItem *self,
    Abstract3DRenderer *renderer) {
  self->setRenderer(renderer);
}

//  void CustomRenderItem::setLabelItem(bool isLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem12setLabelItemEb(
    CustomRenderItem *self,
    bool isLabel) {
  self->setLabelItem(isLabel);
}

//  bool CustomRenderItem::isLabel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem7isLabelEv(const CustomRenderItem *self) {
  return self->isLabel();
}

//  void CustomRenderItem::setTextureWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem15setTextureWidthEi(
    CustomRenderItem *self,
    int width) {
  self->setTextureWidth(width);
}

//  int CustomRenderItem::textureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem12textureWidthEv(
    const CustomRenderItem *self) {
  return self->textureWidth();
}

//  void CustomRenderItem::setTextureHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem16setTextureHeightEi(
    CustomRenderItem *self,
    int height) {
  self->setTextureHeight(height);
}

//  int CustomRenderItem::textureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem13textureHeightEv(
    const CustomRenderItem *self) {
  return self->textureHeight();
}

//  void CustomRenderItem::setTextureDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem15setTextureDepthEi(
    CustomRenderItem *self,
    int depth) {
  self->setTextureDepth(depth);
}

//  int CustomRenderItem::textureDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem12textureDepthEv(
    const CustomRenderItem *self) {
  return self->textureDepth();
}

//  int CustomRenderItem::textureSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem11textureSizeEv(
    const CustomRenderItem *self) {
  return self->textureSize();
}

//  void CustomRenderItem::setColorTable(const QList<QVector4D> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem13setColorTableERK5QListI9QVector4DE(
    CustomRenderItem *self,
    const QList<QVector4D> *colors) {
  self->setColorTable(*colors);
}

//  void CustomRenderItem::setColorTable(const QList<QRgb> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem13setColorTableERK5QListIjE(
    CustomRenderItem *self,
    const QList<QRgb> *colors) {
  self->setColorTable(*colors);
}

//  const QList<QVector4D> &CustomRenderItem::colorTable() const
extern "C" Q_DECL_EXPORT
QList<QVector4D> *ritual_ZNK16CustomRenderItem10colorTableEv(
    const CustomRenderItem *self) {
  return new QList<QVector4D>(self->colorTable());
}

//  void CustomRenderItem::setVolume(bool volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem9setVolumeEb(
    CustomRenderItem *self,
    bool volume) {
  self->setVolume(volume);
}

//  bool CustomRenderItem::isVolume() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem8isVolumeEv(const CustomRenderItem *self) {
  return self->isVolume();
}

//  void CustomRenderItem::setTextureFormat(QImage::Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem16setTextureFormatEN6QImage6FormatE(
    CustomRenderItem *self,
    QImage::Format format) {
  self->setTextureFormat(format);
}

//  QImage::Format CustomRenderItem::textureFormat() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK16CustomRenderItem13textureFormatEv(
    const CustomRenderItem *self) {
  return self->textureFormat();
}

//  void CustomRenderItem::setSliceIndexX(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem14setSliceIndexXEi(
    CustomRenderItem *self,
    int index) {
  self->setSliceIndexX(index);
}

//  void CustomRenderItem::setSliceIndexY(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem14setSliceIndexYEi(
    CustomRenderItem *self,
    int index) {
  self->setSliceIndexY(index);
}

//  void CustomRenderItem::setSliceIndexZ(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem14setSliceIndexZEi(
    CustomRenderItem *self,
    int index) {
  self->setSliceIndexZ(index);
}

//  const QVector3D &CustomRenderItem::sliceFractions() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem14sliceFractionsEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->sliceFractions());
}

//  int CustomRenderItem::sliceIndexX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem11sliceIndexXEv(
    const CustomRenderItem *self) {
  return self->sliceIndexX();
}

//  int CustomRenderItem::sliceIndexY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem11sliceIndexYEv(
    const CustomRenderItem *self) {
  return self->sliceIndexY();
}

//  int CustomRenderItem::sliceIndexZ() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16CustomRenderItem11sliceIndexZEv(
    const CustomRenderItem *self) {
  return self->sliceIndexZ();
}

//  void CustomRenderItem::setAlphaMultiplier(float mult)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem18setAlphaMultiplierEf(
    CustomRenderItem *self,
    float mult) {
  self->setAlphaMultiplier(mult);
}

//  float CustomRenderItem::alphaMultiplier() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16CustomRenderItem15alphaMultiplierEv(
    const CustomRenderItem *self) {
  return self->alphaMultiplier();
}

//  void CustomRenderItem::setPreserveOpacity(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem18setPreserveOpacityEb(
    CustomRenderItem *self,
    bool enable) {
  self->setPreserveOpacity(enable);
}

//  bool CustomRenderItem::preserveOpacity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem15preserveOpacityEv(
    const CustomRenderItem *self) {
  return self->preserveOpacity();
}

//  void CustomRenderItem::setUseHighDefShader(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem19setUseHighDefShaderEb(
    CustomRenderItem *self,
    bool enable) {
  self->setUseHighDefShader(enable);
}

//  bool CustomRenderItem::useHighDefShader() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem16useHighDefShaderEv(
    const CustomRenderItem *self) {
  return self->useHighDefShader();
}

//  void CustomRenderItem::setMinBounds(const QVector3D &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem12setMinBoundsERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *bounds) {
  self->setMinBounds(*bounds);
}

//  const QVector3D &CustomRenderItem::minBounds() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem9minBoundsEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->minBounds());
}

//  void CustomRenderItem::setMaxBounds(const QVector3D &bounds)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem12setMaxBoundsERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *bounds) {
  self->setMaxBounds(*bounds);
}

//  const QVector3D &CustomRenderItem::maxBounds() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem9maxBoundsEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->maxBounds());
}

//  const QVector3D &CustomRenderItem::minBoundsNormal() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem15minBoundsNormalEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->minBoundsNormal());
}

//  const QVector3D &CustomRenderItem::maxBoundsNormal() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem15maxBoundsNormalEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->maxBoundsNormal());
}

//  void CustomRenderItem::setDrawSlices(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem13setDrawSlicesEb(
    CustomRenderItem *self,
    bool enable) {
  self->setDrawSlices(enable);
}

//  bool CustomRenderItem::drawSlices() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem10drawSlicesEv(
    const CustomRenderItem *self) {
  return self->drawSlices();
}

//  void CustomRenderItem::setDrawSliceFrames(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem18setDrawSliceFramesEb(
    CustomRenderItem *self,
    bool enable) {
  self->setDrawSliceFrames(enable);
}

//  bool CustomRenderItem::drawSliceFrames() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16CustomRenderItem15drawSliceFramesEv(
    const CustomRenderItem *self) {
  return self->drawSliceFrames();
}

//  void CustomRenderItem::setSliceFrameColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem18setSliceFrameColorERK6QColor(
    CustomRenderItem *self,
    const QColor *color) {
  self->setSliceFrameColor(*color);
}

//  const QVector4D &CustomRenderItem::sliceFrameColor() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK16CustomRenderItem15sliceFrameColorEv(
    const CustomRenderItem *self) {
  return new QVector4D(self->sliceFrameColor());
}

//  void CustomRenderItem::setSliceFrameWidths(const QVector3D &widths)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem19setSliceFrameWidthsERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *widths) {
  self->setSliceFrameWidths(*widths);
}

//  const QVector3D &CustomRenderItem::sliceFrameWidths() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem16sliceFrameWidthsEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->sliceFrameWidths());
}

//  void CustomRenderItem::setSliceFrameGaps(const QVector3D &gaps)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem17setSliceFrameGapsERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *gaps) {
  self->setSliceFrameGaps(*gaps);
}

//  const QVector3D &CustomRenderItem::sliceFrameGaps() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem14sliceFrameGapsEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->sliceFrameGaps());
}

//  void CustomRenderItem::setSliceFrameThicknesses(const QVector3D
//      &thicknesses)
extern "C" Q_DECL_EXPORT
void ritual_ZN16CustomRenderItem24setSliceFrameThicknessesERK9QVector3D(
    CustomRenderItem *self,
    const QVector3D *thicknesses) {
  self->setSliceFrameThicknesses(*thicknesses);
}

//  const QVector3D &CustomRenderItem::sliceFrameThicknesses() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16CustomRenderItem21sliceFrameThicknessesEv(
    const CustomRenderItem *self) {
  return new QVector3D(self->sliceFrameThicknesses());
}
