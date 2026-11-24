//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopengltexture.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopengltexture.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtCore/qdebug.h>

//  QOpenGLTexture::QOpenGLTexture(Target target)
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZN14QOpenGLTextureC1ENS_6TargetE(
    QOpenGLTexture::Target target) {
  return new QOpenGLTexture(target);
}

//  QOpenGLTexture::QOpenGLTexture(const QImage &image, MipMapGeneration
//      genMipMaps)
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZN14QOpenGLTextureC1ERK6QImageNS_16MipMapGenerationE(
    const QImage *image,
    QOpenGLTexture::MipMapGeneration genMipMaps) {
  return new QOpenGLTexture(*image, genMipMaps);
}

//  QOpenGLTexture::~QOpenGLTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTextureD1Ev(QOpenGLTexture *self) {
  delete self;
}

//  Target QOpenGLTexture::target() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::Target ritual_ZNK14QOpenGLTexture6targetEv(
    const QOpenGLTexture *self) {
  return self->target();
}

//  bool QOpenGLTexture::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLTexture6createEv(QOpenGLTexture *self) {
  return self->create();
}

//  void QOpenGLTexture::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture7destroyEv(QOpenGLTexture *self) {
  self->destroy();
}

//  bool QOpenGLTexture::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLTexture9isCreatedEv(const QOpenGLTexture *self) {
  return self->isCreated();
}

//  void QOpenGLTexture::bind()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture4bindEv(QOpenGLTexture *self) {
  self->bind();
}

//  void QOpenGLTexture::bind(uint unit, TextureUnitReset reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture4bindEjNS_16TextureUnitResetE(
    QOpenGLTexture *self,
    uint unit,
    QOpenGLTexture::TextureUnitReset reset) {
  self->bind(unit, reset);
}

//  void QOpenGLTexture::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture7releaseEv(QOpenGLTexture *self) {
  self->release();
}

//  void QOpenGLTexture::release(uint unit, TextureUnitReset reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture7releaseEjNS_16TextureUnitResetE(
    QOpenGLTexture *self,
    uint unit,
    QOpenGLTexture::TextureUnitReset reset) {
  self->release(unit, reset);
}

//  bool QOpenGLTexture::isBound() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLTexture7isBoundEv(const QOpenGLTexture *self) {
  return self->isBound();
}

//  bool QOpenGLTexture::isBound(uint unit)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLTexture7isBoundEj(QOpenGLTexture *self, uint unit) {
  return self->isBound(unit);
}

//  void QOpenGLTexture::setFormat(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture9setFormatENS_13TextureFormatE(
    QOpenGLTexture *self,
    QOpenGLTexture::TextureFormat format) {
  self->setFormat(format);
}

//  TextureFormat QOpenGLTexture::format() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::TextureFormat ritual_ZNK14QOpenGLTexture6formatEv(
    const QOpenGLTexture *self) {
  return self->format();
}

//  void QOpenGLTexture::setSize(int width, int height, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture7setSizeEiii(
    QOpenGLTexture *self,
    int width,
    int height,
    int depth) {
  self->setSize(width, height, depth);
}

//  int QOpenGLTexture::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture5widthEv(const QOpenGLTexture *self) {
  return self->width();
}

//  int QOpenGLTexture::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture6heightEv(const QOpenGLTexture *self) {
  return self->height();
}

//  int QOpenGLTexture::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture5depthEv(const QOpenGLTexture *self) {
  return self->depth();
}

//  void QOpenGLTexture::setMipLevels(int levels)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture12setMipLevelsEi(
    QOpenGLTexture *self,
    int levels) {
  self->setMipLevels(levels);
}

//  int QOpenGLTexture::mipLevels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture9mipLevelsEv(const QOpenGLTexture *self) {
  return self->mipLevels();
}

//  int QOpenGLTexture::maximumMipLevels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture16maximumMipLevelsEv(
    const QOpenGLTexture *self) {
  return self->maximumMipLevels();
}

//  void QOpenGLTexture::setLayers(int layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture9setLayersEi(
    QOpenGLTexture *self,
    int layers) {
  self->setLayers(layers);
}

//  int QOpenGLTexture::layers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture6layersEv(const QOpenGLTexture *self) {
  return self->layers();
}

//  int QOpenGLTexture::faces() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture5facesEv(const QOpenGLTexture *self) {
  return self->faces();
}

//  void QOpenGLTexture::setSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture10setSamplesEi(
    QOpenGLTexture *self,
    int samples) {
  self->setSamples(samples);
}

//  int QOpenGLTexture::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture7samplesEv(const QOpenGLTexture *self) {
  return self->samples();
}

//  void QOpenGLTexture::setFixedSamplePositions(bool fixed)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture23setFixedSamplePositionsEb(
    QOpenGLTexture *self,
    bool fixed) {
  self->setFixedSamplePositions(fixed);
}

//  bool QOpenGLTexture::isFixedSamplePositions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLTexture22isFixedSamplePositionsEv(
    const QOpenGLTexture *self) {
  return self->isFixedSamplePositions();
}

//  void QOpenGLTexture::allocateStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture15allocateStorageEv(QOpenGLTexture *self) {
  self->allocateStorage();
}

//  void QOpenGLTexture::allocateStorage(PixelFormat pixelFormat, PixelType
//      pixelType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture15allocateStorageENS_11PixelFormatENS_9PixelTypeE(
    QOpenGLTexture *self,
    QOpenGLTexture::PixelFormat pixelFormat,
    QOpenGLTexture::PixelType pixelType) {
  self->allocateStorage(pixelFormat, pixelType);
}

//  bool QOpenGLTexture::isStorageAllocated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLTexture18isStorageAllocatedEv(
    const QOpenGLTexture *self) {
  return self->isStorageAllocated();
}

//  QOpenGLTexture *QOpenGLTexture::createTextureView(Target target,
//      TextureFormat viewFormat, int minimumMipmapLevel, int
//      maximumMipmapLevel, int minimumLayer, int maximumLayer) const
extern "C" Q_DECL_EXPORT
QOpenGLTexture *ritual_ZNK14QOpenGLTexture17createTextureViewENS_6TargetENS_13TextureFormatEiiii(
    const QOpenGLTexture *self,
    QOpenGLTexture::Target target,
    QOpenGLTexture::TextureFormat viewFormat,
    int minimumMipmapLevel,
    int maximumMipmapLevel,
    int minimumLayer,
    int maximumLayer) {
  return self->createTextureView(
      target,
      viewFormat,
      minimumMipmapLevel,
      maximumMipmapLevel,
      minimumLayer,
      maximumLayer);
}

//  bool QOpenGLTexture::isTextureView() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLTexture13isTextureViewEv(
    const QOpenGLTexture *self) {
  return self->isTextureView();
}

//  void QOpenGLTexture::setData(const QImage &image, MipMapGeneration
//      genMipMaps)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture7setDataERK6QImageNS_16MipMapGenerationE(
    QOpenGLTexture *self,
    const QImage *image,
    QOpenGLTexture::MipMapGeneration genMipMaps) {
  self->setData(*image, genMipMaps);
}

//  bool QOpenGLTexture::hasFeature(Feature feature)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLTexture10hasFeatureENS_7FeatureE(
    QOpenGLTexture::Feature feature) {
  return QOpenGLTexture::hasFeature(feature);
}

//  void QOpenGLTexture::setMipBaseLevel(int baseLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture15setMipBaseLevelEi(
    QOpenGLTexture *self,
    int baseLevel) {
  self->setMipBaseLevel(baseLevel);
}

//  int QOpenGLTexture::mipBaseLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture12mipBaseLevelEv(const QOpenGLTexture *self) {
  return self->mipBaseLevel();
}

//  void QOpenGLTexture::setMipMaxLevel(int maxLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setMipMaxLevelEi(
    QOpenGLTexture *self,
    int maxLevel) {
  self->setMipMaxLevel(maxLevel);
}

//  int QOpenGLTexture::mipMaxLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QOpenGLTexture11mipMaxLevelEv(const QOpenGLTexture *self) {
  return self->mipMaxLevel();
}

//  void QOpenGLTexture::setMipLevelRange(int baseLevel, int maxLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture16setMipLevelRangeEii(
    QOpenGLTexture *self,
    int baseLevel,
    int maxLevel) {
  self->setMipLevelRange(baseLevel, maxLevel);
}

//  void QOpenGLTexture::setAutoMipMapGenerationEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture30setAutoMipMapGenerationEnabledEb(
    QOpenGLTexture *self,
    bool enabled) {
  self->setAutoMipMapGenerationEnabled(enabled);
}

//  bool QOpenGLTexture::isAutoMipMapGenerationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLTexture29isAutoMipMapGenerationEnabledEv(
    const QOpenGLTexture *self) {
  return self->isAutoMipMapGenerationEnabled();
}

//  void QOpenGLTexture::generateMipMaps()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture15generateMipMapsEv(QOpenGLTexture *self) {
  self->generateMipMaps();
}

//  void QOpenGLTexture::generateMipMaps(int baseLevel, bool resetBaseLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture15generateMipMapsEib(
    QOpenGLTexture *self,
    int baseLevel,
    bool resetBaseLevel) {
  self->generateMipMaps(baseLevel, resetBaseLevel);
}

//  void QOpenGLTexture::setSwizzleMask(SwizzleComponent component,
//      SwizzleValue value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setSwizzleMaskENS_16SwizzleComponentENS_12SwizzleValueE(
    QOpenGLTexture *self,
    QOpenGLTexture::SwizzleComponent component,
    QOpenGLTexture::SwizzleValue value) {
  self->setSwizzleMask(component, value);
}

//  void QOpenGLTexture::setSwizzleMask(SwizzleValue r, SwizzleValue g,
//      SwizzleValue b, SwizzleValue a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setSwizzleMaskENS_12SwizzleValueES0_S0_S0_(
    QOpenGLTexture *self,
    QOpenGLTexture::SwizzleValue r,
    QOpenGLTexture::SwizzleValue g,
    QOpenGLTexture::SwizzleValue b,
    QOpenGLTexture::SwizzleValue a) {
  self->setSwizzleMask(r, g, b, a);
}

//  SwizzleValue QOpenGLTexture::swizzleMask(SwizzleComponent component)
//      const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::SwizzleValue ritual_ZNK14QOpenGLTexture11swizzleMaskENS_16SwizzleComponentE(
    const QOpenGLTexture *self,
    QOpenGLTexture::SwizzleComponent component) {
  return self->swizzleMask(component);
}

//  void QOpenGLTexture::setDepthStencilMode(DepthStencilMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture19setDepthStencilModeENS_16DepthStencilModeE(
    QOpenGLTexture *self,
    QOpenGLTexture::DepthStencilMode mode) {
  self->setDepthStencilMode(mode);
}

//  DepthStencilMode QOpenGLTexture::depthStencilMode() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::DepthStencilMode ritual_ZNK14QOpenGLTexture16depthStencilModeEv(
    const QOpenGLTexture *self) {
  return self->depthStencilMode();
}

//  void QOpenGLTexture::setComparisonFunction(ComparisonFunction function)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture21setComparisonFunctionENS_18ComparisonFunctionE(
    QOpenGLTexture *self,
    QOpenGLTexture::ComparisonFunction function) {
  self->setComparisonFunction(function);
}

//  ComparisonFunction QOpenGLTexture::comparisonFunction() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::ComparisonFunction ritual_ZNK14QOpenGLTexture18comparisonFunctionEv(
    const QOpenGLTexture *self) {
  return self->comparisonFunction();
}

//  void QOpenGLTexture::setComparisonMode(ComparisonMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture17setComparisonModeENS_14ComparisonModeE(
    QOpenGLTexture *self,
    QOpenGLTexture::ComparisonMode mode) {
  self->setComparisonMode(mode);
}

//  ComparisonMode QOpenGLTexture::comparisonMode() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::ComparisonMode ritual_ZNK14QOpenGLTexture14comparisonModeEv(
    const QOpenGLTexture *self) {
  return self->comparisonMode();
}

//  void QOpenGLTexture::setMinificationFilter(Filter filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture21setMinificationFilterENS_6FilterE(
    QOpenGLTexture *self,
    QOpenGLTexture::Filter filter) {
  self->setMinificationFilter(filter);
}

//  Filter QOpenGLTexture::minificationFilter() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::Filter ritual_ZNK14QOpenGLTexture18minificationFilterEv(
    const QOpenGLTexture *self) {
  return self->minificationFilter();
}

//  void QOpenGLTexture::setMagnificationFilter(Filter filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture22setMagnificationFilterENS_6FilterE(
    QOpenGLTexture *self,
    QOpenGLTexture::Filter filter) {
  self->setMagnificationFilter(filter);
}

//  Filter QOpenGLTexture::magnificationFilter() const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::Filter ritual_ZNK14QOpenGLTexture19magnificationFilterEv(
    const QOpenGLTexture *self) {
  return self->magnificationFilter();
}

//  void QOpenGLTexture::setMinMagFilters(Filter minificationFilter, Filter
//      magnificationFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture16setMinMagFiltersENS_6FilterES0_(
    QOpenGLTexture *self,
    QOpenGLTexture::Filter minificationFilter,
    QOpenGLTexture::Filter magnificationFilter) {
  self->setMinMagFilters(minificationFilter, magnificationFilter);
}

//  void QOpenGLTexture::setMaximumAnisotropy(float anisotropy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture20setMaximumAnisotropyEf(
    QOpenGLTexture *self,
    float anisotropy) {
  self->setMaximumAnisotropy(anisotropy);
}

//  float QOpenGLTexture::maximumAnisotropy() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QOpenGLTexture17maximumAnisotropyEv(
    const QOpenGLTexture *self) {
  return self->maximumAnisotropy();
}

//  void QOpenGLTexture::setWrapMode(WrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture11setWrapModeENS_8WrapModeE(
    QOpenGLTexture *self,
    QOpenGLTexture::WrapMode mode) {
  self->setWrapMode(mode);
}

//  void QOpenGLTexture::setWrapMode(CoordinateDirection direction, WrapMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture11setWrapModeENS_19CoordinateDirectionENS_8WrapModeE(
    QOpenGLTexture *self,
    QOpenGLTexture::CoordinateDirection direction,
    QOpenGLTexture::WrapMode mode) {
  self->setWrapMode(direction, mode);
}

//  WrapMode QOpenGLTexture::wrapMode(CoordinateDirection direction) const
extern "C" Q_DECL_EXPORT
QOpenGLTexture::WrapMode ritual_ZNK14QOpenGLTexture8wrapModeENS_19CoordinateDirectionE(
    const QOpenGLTexture *self,
    QOpenGLTexture::CoordinateDirection direction) {
  return self->wrapMode(direction);
}

//  void QOpenGLTexture::setBorderColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setBorderColorERK6QColor(
    QOpenGLTexture *self,
    const QColor *color) {
  self->setBorderColor(*color);
}

//  void QOpenGLTexture::setBorderColor(float r, float g, float b, float a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setBorderColorEffff(
    QOpenGLTexture *self,
    float r,
    float g,
    float b,
    float a) {
  self->setBorderColor(r, g, b, a);
}

//  void QOpenGLTexture::setBorderColor(int r, int g, int b, int a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setBorderColorEiiii(
    QOpenGLTexture *self,
    int r,
    int g,
    int b,
    int a) {
  self->setBorderColor(r, g, b, a);
}

//  void QOpenGLTexture::setBorderColor(uint r, uint g, uint b, uint a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture14setBorderColorEjjjj(
    QOpenGLTexture *self,
    uint r,
    uint g,
    uint b,
    uint a) {
  self->setBorderColor(r, g, b, a);
}

//  QColor QOpenGLTexture::borderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QOpenGLTexture11borderColorEv(
    const QOpenGLTexture *self) {
  return new QColor(self->borderColor());
}

//  void QOpenGLTexture::borderColor(float *border) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QOpenGLTexture11borderColorEPf(
    const QOpenGLTexture *self,
    float *border) {
  self->borderColor(border);
}

//  void QOpenGLTexture::borderColor(int *border) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QOpenGLTexture11borderColorEPi(
    const QOpenGLTexture *self,
    int *border) {
  self->borderColor(border);
}

//  void QOpenGLTexture::borderColor(unsigned int *border) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QOpenGLTexture11borderColorEPj(
    const QOpenGLTexture *self,
    unsigned int *border) {
  self->borderColor(border);
}

//  void QOpenGLTexture::setMinimumLevelOfDetail(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture23setMinimumLevelOfDetailEf(
    QOpenGLTexture *self,
    float value) {
  self->setMinimumLevelOfDetail(value);
}

//  float QOpenGLTexture::minimumLevelOfDetail() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QOpenGLTexture20minimumLevelOfDetailEv(
    const QOpenGLTexture *self) {
  return self->minimumLevelOfDetail();
}

//  void QOpenGLTexture::setMaximumLevelOfDetail(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture23setMaximumLevelOfDetailEf(
    QOpenGLTexture *self,
    float value) {
  self->setMaximumLevelOfDetail(value);
}

//  float QOpenGLTexture::maximumLevelOfDetail() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QOpenGLTexture20maximumLevelOfDetailEv(
    const QOpenGLTexture *self) {
  return self->maximumLevelOfDetail();
}

//  void QOpenGLTexture::setLevelOfDetailRange(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture21setLevelOfDetailRangeEff(
    QOpenGLTexture *self,
    float min,
    float max) {
  self->setLevelOfDetailRange(min, max);
}

//  void QOpenGLTexture::setLevelofDetailBias(float bias)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLTexture20setLevelofDetailBiasEf(
    QOpenGLTexture *self,
    float bias) {
  self->setLevelofDetailBias(bias);
}

//  float QOpenGLTexture::levelofDetailBias() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK14QOpenGLTexture17levelofDetailBiasEv(
    const QOpenGLTexture *self) {
  return self->levelofDetailBias();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QOpenGLTexture *t)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK14QOpenGLTexture(
    const QDebug *dbg,
    const QOpenGLTexture *t) {
  return new QDebug(operator<<(*dbg, t));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QOpenGLTexturePrivate *QOpenGLTexture::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLTexturePrivate *ritual_ZN14QOpenGLTexture6d_funcEv(
    QOpenGLTexture *self) {
  return self->d_func();
}

//  const QOpenGLTexturePrivate *QOpenGLTexture::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLTexturePrivate *ritual_ZNK14QOpenGLTexture6d_funcEv(
    const QOpenGLTexture *self) {
  return self->d_func();
}

#endif  // !defined(QT_NO_OPENGL)
