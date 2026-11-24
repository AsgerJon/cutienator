//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsurfaceformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qsurfaceformat.h>
#include <QtGui/qcolorspace.h>
#include <QtCore/qdebug.h>

//  QSurfaceFormat::QSurfaceFormat()
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZN14QSurfaceFormatC1Ev() {
  return new QSurfaceFormat();
}

//  QSurfaceFormat::QSurfaceFormat(FormatOptions options)
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZN14QSurfaceFormatC1E6QFlagsINS_12FormatOptionEE(
    int options) {
  return new QSurfaceFormat(
      QFlags<QSurfaceFormat::FormatOption>::fromInt(options));
}

//  QSurfaceFormat::QSurfaceFormat(const QSurfaceFormat &other)
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZN14QSurfaceFormatC1ERKS_(
    const QSurfaceFormat *other) {
  return new QSurfaceFormat(*other);
}

//  QSurfaceFormat::~QSurfaceFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormatD1Ev(QSurfaceFormat *self) {
  delete self;
}

//  void QSurfaceFormat::setDepthBufferSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat18setDepthBufferSizeEi(
    QSurfaceFormat *self,
    int size) {
  self->setDepthBufferSize(size);
}

//  int QSurfaceFormat::depthBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat15depthBufferSizeEv(
    const QSurfaceFormat *self) {
  return self->depthBufferSize();
}

//  void QSurfaceFormat::setStencilBufferSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat20setStencilBufferSizeEi(
    QSurfaceFormat *self,
    int size) {
  self->setStencilBufferSize(size);
}

//  int QSurfaceFormat::stencilBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat17stencilBufferSizeEv(
    const QSurfaceFormat *self) {
  return self->stencilBufferSize();
}

//  void QSurfaceFormat::setRedBufferSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat16setRedBufferSizeEi(
    QSurfaceFormat *self,
    int size) {
  self->setRedBufferSize(size);
}

//  int QSurfaceFormat::redBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat13redBufferSizeEv(const QSurfaceFormat *self) {
  return self->redBufferSize();
}

//  void QSurfaceFormat::setGreenBufferSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat18setGreenBufferSizeEi(
    QSurfaceFormat *self,
    int size) {
  self->setGreenBufferSize(size);
}

//  int QSurfaceFormat::greenBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat15greenBufferSizeEv(
    const QSurfaceFormat *self) {
  return self->greenBufferSize();
}

//  void QSurfaceFormat::setBlueBufferSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat17setBlueBufferSizeEi(
    QSurfaceFormat *self,
    int size) {
  self->setBlueBufferSize(size);
}

//  int QSurfaceFormat::blueBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat14blueBufferSizeEv(
    const QSurfaceFormat *self) {
  return self->blueBufferSize();
}

//  void QSurfaceFormat::setAlphaBufferSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat18setAlphaBufferSizeEi(
    QSurfaceFormat *self,
    int size) {
  self->setAlphaBufferSize(size);
}

//  int QSurfaceFormat::alphaBufferSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat15alphaBufferSizeEv(
    const QSurfaceFormat *self) {
  return self->alphaBufferSize();
}

//  void QSurfaceFormat::setSamples(int numSamples)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat10setSamplesEi(
    QSurfaceFormat *self,
    int numSamples) {
  self->setSamples(numSamples);
}

//  int QSurfaceFormat::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat7samplesEv(const QSurfaceFormat *self) {
  return self->samples();
}

//  void QSurfaceFormat::setSwapBehavior(SwapBehavior behavior)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat15setSwapBehaviorENS_12SwapBehaviorE(
    QSurfaceFormat *self,
    QSurfaceFormat::SwapBehavior behavior) {
  self->setSwapBehavior(behavior);
}

//  SwapBehavior QSurfaceFormat::swapBehavior() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat::SwapBehavior ritual_ZNK14QSurfaceFormat12swapBehaviorEv(
    const QSurfaceFormat *self) {
  return self->swapBehavior();
}

//  bool QSurfaceFormat::hasAlpha() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSurfaceFormat8hasAlphaEv(const QSurfaceFormat *self) {
  return self->hasAlpha();
}

//  void QSurfaceFormat::setProfile(OpenGLContextProfile profile)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat10setProfileENS_20OpenGLContextProfileE(
    QSurfaceFormat *self,
    QSurfaceFormat::OpenGLContextProfile profile) {
  self->setProfile(profile);
}

//  OpenGLContextProfile QSurfaceFormat::profile() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat::OpenGLContextProfile ritual_ZNK14QSurfaceFormat7profileEv(
    const QSurfaceFormat *self) {
  return self->profile();
}

//  void QSurfaceFormat::setRenderableType(RenderableType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat17setRenderableTypeENS_14RenderableTypeE(
    QSurfaceFormat *self,
    QSurfaceFormat::RenderableType type) {
  self->setRenderableType(type);
}

//  RenderableType QSurfaceFormat::renderableType() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat::RenderableType ritual_ZNK14QSurfaceFormat14renderableTypeEv(
    const QSurfaceFormat *self) {
  return self->renderableType();
}

//  void QSurfaceFormat::setMajorVersion(int majorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat15setMajorVersionEi(
    QSurfaceFormat *self,
    int majorVersion) {
  self->setMajorVersion(majorVersion);
}

//  int QSurfaceFormat::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat12majorVersionEv(const QSurfaceFormat *self) {
  return self->majorVersion();
}

//  void QSurfaceFormat::setMinorVersion(int minorVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat15setMinorVersionEi(
    QSurfaceFormat *self,
    int minorVersion) {
  self->setMinorVersion(minorVersion);
}

//  int QSurfaceFormat::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat12minorVersionEv(const QSurfaceFormat *self) {
  return self->minorVersion();
}

//  void QSurfaceFormat::setVersion(int major, int minor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat10setVersionEii(
    QSurfaceFormat *self,
    int major,
    int minor) {
  self->setVersion(major, minor);
}

//  bool QSurfaceFormat::stereo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSurfaceFormat6stereoEv(const QSurfaceFormat *self) {
  return self->stereo();
}

//  void QSurfaceFormat::setStereo(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat9setStereoEb(
    QSurfaceFormat *self,
    bool enable) {
  self->setStereo(enable);
}

//  void QSurfaceFormat::setOptions(QSurfaceFormat::FormatOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat10setOptionsE6QFlagsINS_12FormatOptionEE(
    QSurfaceFormat *self,
    int options) {
  self->setOptions(QFlags<QSurfaceFormat::FormatOption>::fromInt(options));
}

//  void QSurfaceFormat::setOption(FormatOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat9setOptionENS_12FormatOptionEb(
    QSurfaceFormat *self,
    QSurfaceFormat::FormatOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QSurfaceFormat::testOption(FormatOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSurfaceFormat10testOptionENS_12FormatOptionE(
    const QSurfaceFormat *self,
    QSurfaceFormat::FormatOption option) {
  return self->testOption(option);
}

//  QSurfaceFormat::FormatOptions QSurfaceFormat::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat7optionsEv(const QSurfaceFormat *self) {
  return static_cast<int>(self->options().toInt());
}

//  int QSurfaceFormat::swapInterval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QSurfaceFormat12swapIntervalEv(const QSurfaceFormat *self) {
  return self->swapInterval();
}

//  void QSurfaceFormat::setSwapInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat15setSwapIntervalEi(
    QSurfaceFormat *self,
    int interval) {
  self->setSwapInterval(interval);
}

//  const QColorSpace &QSurfaceFormat::colorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK14QSurfaceFormat10colorSpaceEv(
    const QSurfaceFormat *self) {
  return new QColorSpace(self->colorSpace());
}

//  void QSurfaceFormat::setColorSpace(const QColorSpace &colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat13setColorSpaceERK11QColorSpace(
    QSurfaceFormat *self,
    const QColorSpace *colorSpace) {
  self->setColorSpace(*colorSpace);
}

#if QT_DEPRECATED_SINCE(6,0)
//  void QSurfaceFormat::setColorSpace(ColorSpace colorSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat13setColorSpaceENS_10ColorSpaceE(
    QSurfaceFormat *self,
    QSurfaceFormat::ColorSpace colorSpace) {
  self->setColorSpace(colorSpace);
}
#endif  // QT_DEPRECATED_SINCE(6,0)

//  void QSurfaceFormat::setDefaultFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat16setDefaultFormatERKS_(
    const QSurfaceFormat *format) {
  QSurfaceFormat::setDefaultFormat(*format);
}

//  QSurfaceFormat QSurfaceFormat::defaultFormat()
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZN14QSurfaceFormat13defaultFormatEv() {
  return new QSurfaceFormat(QSurfaceFormat::defaultFormat());
}

//  void QSurfaceFormat::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSurfaceFormat6detachEv(QSurfaceFormat *self) {
  self->detach();
}

//  bool QSurfaceFormat::equals(const QSurfaceFormat &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QSurfaceFormat6equalsERKS_(
    const QSurfaceFormat *self,
    const QSurfaceFormat *other) {
  return self->equals(*other);
}

//  bool operator==(const QSurfaceFormat &lhs, const QSurfaceFormat &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QSurfaceFormatS1_(
    const QSurfaceFormat *lhs,
    const QSurfaceFormat *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSurfaceFormat &lhs, const QSurfaceFormat &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QSurfaceFormatS1_(
    const QSurfaceFormat *lhs,
    const QSurfaceFormat *rhs) {
  return operator!=(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QSurfaceFormat &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK14QSurfaceFormat(
    const QDebug *a0,
    const QSurfaceFormat *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
